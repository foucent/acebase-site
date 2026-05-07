import os
import re
import requests
import html2text
from readability import Document
from urllib.parse import urlparse
from pathlib import Path

# ================= 配置区 =================
# 建议使用绝对路径，防止找不到文件夹
# 请将下方路径修改为您电脑上 Hugo 项目的真实地址
HUGO_BASE_PATH = Path(r"C:\你的路径\my_hugo_site") 

# 预定义子目录
POSTS_DIR = HUGO_BASE_PATH / "content" / "posts"
IMAGES_DIR = HUGO_BASE_PATH / "static" / "images" / "posts"

# 伪装浏览器，防止被网站拦截 (403错误)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
# ==========================================

def setup_env():
    """确保 Hugo 相关目录存在"""
    POSTS_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

def download_image(url, save_path):
    """下载图片并保存"""
    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        if res.status_code == 200:
            save_path.write_bytes(res.content)
            return True
    except Exception as e:
        print(f"  [!] 图片下载失败: {url} -> {e}")
    return False

def clean_filename(filename):
    """清理文件名中的非法字符，防止 Windows 报错"""
    # 替换 Windows 不允许的字符: \ / : * ? " < > |
    return re.sub(r'[\\/:*?"<>|]', '_', filename).strip()

def collect_article(url):
    print(f"[*] 正在处理: {url}")
    
    try:
        # 1. 抓取网页
        response = requests.get(url, headers=HEADERS, timeout=20)
        response.encoding = response.apparent_encoding # 自动识别编码，防止中文乱码
        
        # 2. 提取正文
        doc = Document(response.text)
        title = doc.title()
        safe_title = clean_filename(title)
        clean_html = doc.summary()
        
        # 3. 转化为 Markdown
        h = html2text.HTML2Text()
        h.body_width = 0  # 不限制行宽，保持原始排版
        h.ignore_links = False
        markdown_content = h.handle(clean_html)
        
        # 4. 处理图片本地化[cite: 1, 2]
        post_img_dir = IMAGES_DIR / safe_title
        post_img_dir.mkdir(parents=True, exist_ok=True)
        
        # 匹配 Markdown 中的图片语法 ![]()
        img_urls = re.findall(r'!\[.*?\]\((.*?)\)', markdown_content)
        
        print(f"[*] 发现 {len(img_urls)} 张图片，开始下载...")
        for i, img_url in enumerate(img_urls):
            # 处理相对路径图片
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif not img_url.startswith('http'):
                continue
                
            ext = os.path.splitext(urlparse(img_url).path)[-1] or ".jpg"
            img_name = f"{i+1}{ext}"
            save_path = post_img_dir / img_name
            
            if download_image(img_url, save_path):
                # 替换为 Hugo 的本地静态路径[cite: 1, 2]
                hugo_rel_path = f"/images/posts/{safe_title}/{img_name}"
                markdown_content = markdown_content.replace(img_url, hugo_rel_path)
        
        # 5. 生成 Hugo 文章文件
        post_file = POSTS_DIR / f"{safe_title}.md"
        front_matter = (
            "---\n"
            f"title: \"{title}\"\n"
            f"date: 2026-05-07\n"
            "draft: false\n"
            "---\n\n"
        )
        
        post_file.write_text(front_matter + markdown_content, encoding="utf-8")
        print(f"[+] 成功！文章已存至: {post_file}")

    except Exception as e:
        print(f"[-] 处理失败: {e}")

if __name__ == "__main__":
    setup_env()
    target_url = input("请输入文章 URL: ").strip()
    if target_url:
        collect_article(target_url)