# -*- coding: utf-8 -*-
"""抖音视频下载工具：解析分享链接 → 下载无水印 mp4 到指定目录

用法（任选其一）：
  1) 命令行直接传链接：
     python dy_download_videos.py "https://v.douyin.com/xxx/" "https://v.douyin.com/yyy/"
  2) 粘贴模式：从标准输入逐行粘贴（每条链接一行），输入结束后按 Ctrl+Z（Windows）再回车：
     python dy_download_videos.py -
  3) 直接改下面的 LINKS 列表后运行：
     python dy_download_videos.py

去重：已成功下载的视频会记录在 RECORD_FILE 里，重复运行相同的链接会自动跳过。
"""
import re, json, os, sys, time, datetime, urllib.request

# ================= 配置 =================
OUT_DIR = r"C:\Users\fouce\Downloads"
RECORD_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dy_downloaded.json")
# ========================================

UA = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
      "Referer": "https://www.douyin.com/"}
MAX_PER_FILE_SEC = 180          # 单文件整体下载时限，防卡死
LINKS = []                      # 方式3：想改目录/批量时填在这里

ILLEGAL = re.compile(r'[\/:*?"<>|\x00-\x1f]')


def http(url, headers=None, timeout=30):
    req = urllib.request.Request(url, headers=headers or UA)
    return urllib.request.urlopen(req, timeout=timeout)


def resolve(short):
    with http(short) as r:
        final = r.geturl()
    m = re.search(r'/share/(?:video|note|slide)/(\d+)', final) or re.search(r'/video/(\d+)', final)
    return (m.group(1) if m else None), final


def parse_router(page):
    start = page.find('_ROUTER_DATA = ')
    if start < 0:
        return None
    start += len('_ROUTER_DATA = ')
    depth = 0; end = start
    for idx in range(start, len(page)):
        c = page[idx]
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0: end = idx + 1; break
    return json.loads(page[start:end])


def find_keys(o, key, out):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key: out.append(v)
            find_keys(v, key, out)
    elif isinstance(o, list):
        for x in o: find_keys(x, key, out)


def sanitize(name):
    name = ILLEGAL.sub('_', name)
    return name.strip(' .') or 'untitled'


def download_video(video_id, out_path):
    """流式下载无水印视频，带整体时限，返回字节数。超时抛异常由外层清理半截文件。"""
    url = f"https://aweme.snssdk.com/aweme/v1/play/?video_id={video_id}&ratio=720p&line=0"
    deadline = time.time() + MAX_PER_FILE_SEC
    with http(url, timeout=60) as r, open(out_path, "wb") as f:
        total = 0
        while True:
            if time.time() > deadline:
                raise TimeoutError(f"over {MAX_PER_FILE_SEC}s deadline")
            chunk = r.read(65536)
            if not chunk: break
            f.write(chunk); total += len(chunk)
    return total


def load_record():
    if os.path.exists(RECORD_FILE):
        try:
            with open(RECORD_FILE, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_record(record):
    with open(RECORD_FILE, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)


def process_link(link, record):
    try:
        aweme, final = resolve(link)
        if not aweme:
            print(f"SKIP {link}: no aweme_id"); return
        with http(final) as r:
            page = r.read().decode('utf-8', 'replace')
        data = parse_router(page)
        authors = []; descs = []; plays = []
        find_keys(data, 'nickname', authors)
        find_keys(data, 'desc', descs)
        find_keys(data, 'play_addr', plays)
        author = sanitize(authors[0] if authors else 'unknown')
        title = sanitize(descs[0] if descs else 'untitled')[:30]
        vid = None
        for p in plays:
            u = p.get('url_list', []) if isinstance(p, dict) else p
            for uu in u:
                m = re.search(r'video_id=([^&\s]+)', uu)
                if m: vid = m.group(1); break
            if vid: break
        if not vid:
            print(f"SKIP {link}: no video_id"); return

        # 去重：同一 video_id 已下载过则跳过
        if vid in record:
            print(f"SKIP {link}: already downloaded -> {record[vid]}"); return

        ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        fname = f"{author}-{title}...-{ts}.mp4"
        out = os.path.join(OUT_DIR, fname)
        size = download_video(vid, out)
        record[vid] = fname
        save_record(record)
        print(f"OK  {fname}  ({size/1e6:.1f} MB)")
        time.sleep(1)
    except Exception as e:
        # 清理半截文件
        for f in os.listdir(OUT_DIR):
            if f.startswith("tmp_") or f.endswith(".part"):
                try: os.remove(os.path.join(OUT_DIR, f))
                except OSError: pass
        print(f"ERR {link}: {type(e).__name__}: {e}")


def collect_links():
    args = sys.argv[1:]
    if args:
        if args == ["-"]:
            print("粘贴链接（每行一个），结束后按 Ctrl+Z + 回车：")
            return [l.strip() for l in sys.stdin if l.strip()]
        return args
    if LINKS:
        return LINKS
    print("未提供链接。用法见脚本顶部 docstring，或运行:")
    print('  python dy_download_videos.py "https://v.douyin.com/xxx/"')
    sys.exit(1)


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    links = collect_links()
    print(f"目标目录: {OUT_DIR}，共 {len(links)} 条链接")
    record = load_record()
    for link in links:
        process_link(link, record)
    print("完成。")
