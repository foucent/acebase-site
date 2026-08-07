import re
from pathlib import Path

t = Path("_bt_ab.html").read_text(encoding="utf-8", errors="ignore")
imgs = re.findall(r'https?://[^"\']+\.(?:png|jpg|webp|jpeg)[^"\']*', t, re.I)
for u in dict.fromkeys(imgs):
    print(u)
