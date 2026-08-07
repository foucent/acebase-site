# -*- coding: utf-8 -*-
from pathlib import Path
import re

fps = Path("docs/fps-top-up")
gift = Path("docs/gift-cards")

nav_fps_order = [
    "arena-breakout-infinite-top-up.md",
    "point-blank-cash-sea.md",
    "point-blank-pb-cash.md",
    "valorant-point-ph-top-up.md",
    "valorant-point-my-top-up.md",
    "valorant-point-th-top-up.md",
    "valorant-point-id-top-up.md",
    "mecha-break-top-up.md",
    "pubg-mobile-uc-top-up-global.md",
    "pubg-mobile-uc-top-up.md",
    "pubg-mobile-tw-top-up.md",
    "pubgm-uc-indonesia.md",
    "pubg-mobile-rp-global.md",
    "pubg-mobile-rp-my.md",
    "pubg-mobile-rp-tw.md",
    "pubg-mobile-lite-indonesia-top-up.md",
    "pubg-new-state-nc.md",
    "free-fire-diamonds-top-up.md",
    "free-fire-diamonds-my-top-up.md",
    "free-fire-latam-diamonds-top-up.md",
    "free-fire-id-diamonds-top-up.md",
    "free-fire-th-diamonds-top-up.md",
    "free-fire-diamonds-eu-tr.md",
    "free-fire-diamonds-br-top-up.md",
    "free-fire-diamonds-tw-top-up.md",
    "free-fire-bd-diamonds-top-up.md",
    "free-fire-diamonds-vn-top-up.md",
    "free-fire-max-diamonds-top-up.md",
    "blood-strike-gold-top-up.md",
    "blood-strike-pass-top-up.md",
    "blood-strike-gold-pass-mena.md",
    "knives-out-vouchers.md",
    "knives-out-package.md",
    "arena-breakout-bonds-top-up.md",
    "arena-breakout-pass-package-top-up.md",
    "delta-force-top-up-global.md",
    "garena-delta-force-top-up.md",
    "garena-delta-force-malaysia-top-up.md",
    "garena-delta-force-indonesia-top-up.md",
    "garena-delta-force-thailand-top-up.md",
    "garena-delta-force-taiwan-top-up.md",
    "garena-delta-force-latam-top-up.md",
    "garena-delta-force-mena-top-up.md",
    "farlight-84-diamonds.md",
    "crossfire-legends-sea-top-up.md",
    "garena-call-of-duty-mobile-top-up-my-sg.md",
    "garena-codm-top-up.md",
    "garena-call-of-duty-mobile-tw-top-up.md",
    "rainbow-six-mobile-top-up.md",
    "marvel-rivals-top-up.md",
    "the-division-resurgence-top-up.md",
    "warframe-mobile-top-up.md",
    "ballistic-hero-vng-top-up.md",
    "t3-arena-t-gems-top-up.md",
    "destiny-rising-top-up.md",
    "snowbreak-containment-zone-top-up.md",
    "valorant-point-sg-top-up.md",
    "undawn-rc-eu-top-up.md",
    "undawn-rc-na-top-up.md",
    "undawn-package-eu-top-up.md",
    "undawn-package-na-top-up.md",
    "garena-undawn-rc-my-top-up.md",
    "garena-undawn-rc-id-top-up.md",
    "garena-undawn-rc-ph-top-up.md",
    "garena-undawn-paket-id-top-up.md",
    "acecraft-global-top-up.md",
    "mini-world-royale-top-up.md",
    "sausage-man-candies.md",
    "x-clash-top-up.md",
]

nav_gift_order = [
    "roblox-gift-card-us.md",
    "escape-from-tarkov.md",
    "arena-breakout-infinite.md",
    "hunt-showdown.md",
    "delta-force.md",
    "call-of-duty-warzone.md",
    "gray-zone-warfare.md",
    "marauders.md",
    "vigor.md",
    "stalker-2.md",
    "single-player-tarkov.md",
]


def read_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("title:"):
            return line[6:].strip().strip('"').strip("'")
    return path.stem


title_by_file = {}
for fn in nav_fps_order:
    title_by_file[fn] = read_title(fps / fn)
for fn in nav_gift_order:
    title_by_file[fn] = read_title(gift / fn)

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
for fn in nav_fps_order:
    index_lines.append(f"- [{title_by_file[fn]}](fps-top-up/{fn})")
index_lines += ["", "## 礼品卡", ""]
for fn in nav_gift_order:
    index_lines.append(f"- [{title_by_file[fn]}](gift-cards/{fn})")
Path("docs/index.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8", newline="\n")

yml_path = Path("mkdocs.yml")
yml = yml_path.read_text(encoding="utf-8")
yml = re.sub(r"(language:\s*)\S+", r"\1zh", yml, count=1)
yml = re.sub(
    r'snipcart_deferred_title:\s*".*?"',
    'snipcart_deferred_title: "使用 Wise 付款"',
    yml,
    count=1,
)
yml = re.sub(
    r'snipcart_deferred_instructions:\s*".*?"',
    'snipcart_deferred_instructions: "点击下单后，将打开 WhatsApp 并附带订单信息。请按订单号通过 Wise 转账精确金额；确认到账后发放数字 PIN。"',
    yml,
    count=1,
)

nav_lines = ["nav:", "  - 首页: index.md", "  - 直接充值:"]
for fn in nav_fps_order:
    nav_lines.append(f'      - "{title_by_file[fn]}": fps-top-up/{fn}')
nav_lines.append("  - 礼品卡:")
for fn in nav_gift_order:
    nav_lines.append(f'      - "{title_by_file[fn]}": gift-cards/{fn}')
nav_block = "\n".join(nav_lines) + "\n"
yml = re.sub(r"\nnav:\n.*", "\n" + nav_block, yml, count=1, flags=re.S)
yml_path.write_text(yml, encoding="utf-8", newline="\n")
print("ok", len(nav_fps_order), len(nav_gift_order))
