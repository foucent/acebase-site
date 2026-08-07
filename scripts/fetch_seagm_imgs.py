# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

url = "https://www.seagm.com/zh-hk/pubg-mobile-tw-top-up"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
html = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "replace")
imgs = re.findall(r"https?://[^\"'\\s>]+\.(?:png|jpg|jpeg|webp)(?:\?[^\"'\\s>]*)?", html, re.I)
seen = []
for u in imgs:
    if u in seen:
        continue
    seen.append(u)
    low = u.lower()
    if any(k in low for k in ("pubg", "uc", "product", "cdn", "image", "tw", "game")):
        print(u)
Path("scripts/_seagm_snip.html").write_text(html[:50000], encoding="utf-8")
print("saved snip, imgs", len(seen))
