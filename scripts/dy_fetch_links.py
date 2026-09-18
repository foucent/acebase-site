# -*- coding: utf-8 -*-
"""Resolve Douyin share links -> metadata (images or video URLs)."""
import re, json, sys, time, html
import urllib.request

LINKS = [
    ("蜜桃内裤",      "https://v.douyin.com/j9-Zy_4C07w/"),
    ("睡衣家居服",    "https://v.douyin.com/STS3Fuv8Hms/"),
    ("约会蕾丝睡衣",  "https://v.douyin.com/BSC6HDAabFU/"),
    ("兴业银行定投",  "https://v.douyin.com/TJECUhutWCI/"),
    ("DOTA2 TI上海",  "https://v.douyin.com/1zkJtARsQEE/"),
]

UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"

def get(url, headers):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode('utf-8', 'replace'), r.geturl()

def find_keys(o, key, out):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == key: out.append(v)
            find_keys(v, key, out)
    elif isinstance(o, list):
        for x in o: find_keys(x, key, out)

def resolve(short):
    # resolve short link to iesdouyin share/video/<id>
    req = urllib.request.Request(short, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            final = r.geturl()
    except Exception as e:
        return None, str(e)
    m = re.search(r'/share/(?:video|note|slide)/(\d+)', final)
    if not m:
        m = re.search(r'/video/(\d+)', final)
    return (m.group(1) if m else None), final

for label, link in LINKS:
    aweme, final = resolve(link)
    print("="*60)
    print(f"[{label}] {link} -> {final}")
    if not aweme:
        print("  !! could not extract aweme_id"); continue
    print("  aweme_id:", aweme)
    try:
        page, _ = get(final, {"User-Agent": UA})
    except Exception as e:
        print("  !! page fetch failed:", e); continue
    m = re.search(r'_ROUTER_DATA = ', page)
    if not m:
        print("  !! no _ROUTER_DATA"); continue
    start = page.find('_ROUTER_DATA = ') + len('_ROUTER_DATA = ')
    depth = 0; end = start
    for idx in range(start, len(page)):
        c = page[idx]
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0: end = idx + 1; break
    try:
        data = json.loads(page[start:end])
    except Exception as e:
        print("  !! json parse failed:", e); continue
    imgs = []; vids = []; descs = []; authors = []
    find_keys(data, 'images', imgs); find_keys(data, 'play_addr', vids)
    find_keys(data, 'desc', descs); find_keys(data, 'nickname', authors)
    n_img = sum(len(v) if isinstance(v, list) else 1 for v in imgs)
    desc = (descs[0] if descs else '').replace('\n', ' ')[:40]
    author = authors[0] if authors else ''
    vurl = None
    if vids:
        u = vids[0].get('url_list', []) if isinstance(vids[0], dict) else vids[0]
        vurl = u[0] if u else None
    print(f"  author={author!r} desc={desc!r}")
    print(f"  images_blocks={len(imgs)} (total={n_img})  video={'yes' if vurl else 'no'}")
    if n_img:
        first = imgs[0]['url_list'] if isinstance(imgs[0], dict) else imgs[0]
        print("  img[0]:", (first[0] if first else None))
    if vurl: print("  video:", vurl[:120])
    time.sleep(1)
