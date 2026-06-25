import re
from pathlib import Path

html = Path(r"c:\1Work\acebase.cc\model\niko-page.html").read_text(encoding="utf-8")

for sid in ["cs2_mouse", "cs2_crosshair", "cs2_viewmodel", "cs2_video"]:
    m = re.search(rf'<section id="{sid}".*?(?=</section>)', html, re.S)
    if not m:
        print(f"=== {sid} NOT FOUND ===")
        continue
    print(f"=== {sid} ===")
    block = m.group(0)
    for th, td in re.findall(r"<tr[^>]*>.*?<th>([^<]+)</th><td>(.*?)</td>", block, re.S):
        td = re.sub(r"<[^>]+>", " ", td)
        td = re.sub(r"\s+", " ", td).strip()
        print(f"{th}: {td}")
    print()

codes = re.findall(r"CSGO-[A-Za-z0-9-]+", html)
print("codes:", list(dict.fromkeys(codes))[:3])

m = re.search(r'id="gear".*?(?=</section>)', html, re.S)
if m:
    print("=== gear ===")
    for h4 in re.findall(r"<h4><a[^>]*>([^<]+)</a></h4>", m.group(0)):
        print(h4)

m = re.search(r'id="skins".*?(?=</section>)', html, re.S)
if m:
    print("=== skins ===")
    items = re.findall(
        r'<div class="skin-card__title">(.*?)</div>.*?<div class="skin-card__subtitle">(.*?)</div>',
        m.group(0),
        re.S,
    )
    for title, sub in items:
        title = re.sub(r"<[^>]+>", "", title).strip()
        sub = re.sub(r"<[^>]+>", "", sub).strip()
        print(f"{title} | {sub}")

# avatar
av = re.search(r'class="attachment-200x200[^"]*"[^>]*src="([^"]+)"', html)
print("avatar:", av.group(1) if av else "none")

# crosshair svg from page if any
svg = re.search(r'id="cs2_crosshair".*?<svg[^>]*viewBox="0 0 50 50".*?</svg>', html, re.S)
if svg:
    print("has crosshair svg")
