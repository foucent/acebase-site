# -*- coding: utf-8 -*-
"""Keep only MY / Global / Taiwan FPS pages; delete the rest; refresh nav+index."""
from pathlib import Path
import re

root = Path(r"c:/1Work/acebase.cc")
fps = root / "docs" / "fps-top-up"

KEEP = {
    "acecraft-global-top-up.md",
    "delta-force-top-up-global.md",
    "free-fire-diamonds-my-top-up.md",
    "free-fire-diamonds-tw-top-up.md",
    "garena-call-of-duty-mobile-top-up-my-sg.md",
    "garena-call-of-duty-mobile-tw-top-up.md",
    "garena-delta-force-malaysia-top-up.md",
    "garena-delta-force-taiwan-top-up.md",
    "garena-undawn-rc-my-top-up.md",
    "pubg-mobile-rp-global.md",
    "pubg-mobile-rp-my.md",
    "pubg-mobile-rp-tw.md",
    "pubg-mobile-tw-top-up.md",
    "pubg-mobile-uc-top-up-global.md",
    "pubg-mobile-uc-top-up.md",  # Malaysia
    "valorant-point-my-top-up.md",
}

# Stable display order for nav/index
ORDER = [
    "valorant-point-my-top-up.md",
    "pubg-mobile-uc-top-up-global.md",
    "pubg-mobile-uc-top-up.md",
    "pubg-mobile-tw-top-up.md",
    "pubg-mobile-rp-global.md",
    "pubg-mobile-rp-my.md",
    "pubg-mobile-rp-tw.md",
    "free-fire-diamonds-my-top-up.md",
    "free-fire-diamonds-tw-top-up.md",
    "delta-force-top-up-global.md",
    "garena-delta-force-malaysia-top-up.md",
    "garena-delta-force-taiwan-top-up.md",
    "garena-call-of-duty-mobile-top-up-my-sg.md",
    "garena-call-of-duty-mobile-tw-top-up.md",
    "garena-undawn-rc-my-top-up.md",
    "acecraft-global-top-up.md",
]


def read_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("title:"):
            return line[6:].strip().strip('"').strip("'")
    return path.stem


deleted = []
for p in sorted(fps.glob("*.md")):
    if p.name not in KEEP:
        p.unlink()
        deleted.append(p.name)

kept = []
for name in ORDER:
    path = fps / name
    if not path.exists():
        raise SystemExit(f"missing keep file: {name}")
    kept.append((read_title(path), name))

# gift cards from existing index
gift_lines = []
index_path = root / "docs" / "index.md"
old = index_path.read_text(encoding="utf-8")
m = re.search(r"## 礼品卡\n\n([\s\S]*)$", old)
gift_block = m.group(1).rstrip() + "\n" if m else ""

index_lines = [
    "# AceBase",
    "",
    "硬核玩家基地：游戏直充、礼品卡与相关购买说明。",
    "",
    "---",
    "",
    "## 直接充值",
    "",
]
for title, name in kept:
    index_lines.append(f"- [{title}](fps-top-up/{name})")
index_lines += ["", "## 礼品卡", "", gift_block.rstrip(), ""]
index_path.write_text("\n".join(index_lines) + "\n", encoding="utf-8", newline="\n")

yml_path = root / "mkdocs.yml"
yml = yml_path.read_text(encoding="utf-8")
nav_lines = ["nav:", "  - 首页: index.md", "  - 直接充值:"]
for title, name in kept:
    nav_lines.append(f'      - "{title}": fps-top-up/{name}')
# preserve gift cards nav from existing yml
gm = re.search(r"  - 礼品卡:\n([\s\S]*)$", yml)
if not gm:
    raise SystemExit("gift cards nav missing")
nav_lines.append("  - 礼品卡:")
nav_lines.append(gm.group(1).rstrip())
nav_block = "\n".join(nav_lines) + "\n"
yml = re.sub(r"\nnav:\n.*", "\n" + nav_block, yml, count=1, flags=re.S)
yml_path.write_text(yml, encoding="utf-8", newline="\n")

print(f"kept {len(kept)}, deleted {len(deleted)}")
for t, n in kept:
    print(" KEEP", n, "->", t)
print("---")
for n in deleted:
    print(" DEL", n)
