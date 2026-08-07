# -*- coding: utf-8 -*-
from pathlib import Path
import json
import re

p = Path("docs/gift-cards/roblox-gift-card-us.md")
t = p.read_text(encoding="utf-8")
for face in ("10", "15", "20", "25", "50", "100"):
    t = t.replace(
        f'data-item-name="Roblox Gift Card (US) ${face}"',
        f'data-item-name="Roblox 礼品卡（美国） ${face}"',
    )
t = t.replace(
    "US-region Roblox digital gift card",
    "美国区 Roblox 数字礼品卡",
)
t = t.replace("face value · Digital PIN", "面额 · 数字 PIN")
p.write_text(t, encoding="utf-8", newline="\n")

jp = Path("docs/snipcart/products.json")
data = json.loads(jp.read_text(encoding="utf-8"))
for item in data:
    face = item["id"].rsplit("-", 1)[-1]
    item["name"] = f"Roblox 礼品卡（美国） ${face}"
    item["description"] = f"美国区 Roblox 数字礼品卡 · ${face} 面额 · 数字 PIN"
jp.write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
print("ok")
