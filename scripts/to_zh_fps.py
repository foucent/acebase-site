# -*- coding: utf-8 -*-
"""Regenerate FPS top-up pages in Chinese from shared template."""
from pathlib import Path
import re

root = Path(r"c:/1Work/acebase.cc/docs/fps-top-up")

CURRENCY_HINTS = [
    (r"\bUC\b", "UC"),
    (r"Diamonds?", "钻石"),
    (r"\bVP\b|Valorant Point", "VP"),
    (r"\bCP\b", "CP"),
    (r"Golds?", "金币"),
    (r"Bonds?", "Bond"),
    (r"Corite", "Corite"),
    (r"T-Gems?", "T-Gems"),
    (r"\bNC\b", "NC"),
    (r"BattleCoin", "BattleCoin"),
    (r"Candies", "糖果"),
    (r"Vouchers?", "点券"),
    (r"\bRC\b", "RC"),
    (r"Cash", "Cash"),
    (r"Pass", "通行证 / 礼包"),
]

REGION_HINTS = [
    (r"Global|全球", "全球"),
    (r"\bMY\b|Malaysia|马来", "马来西亚"),
    (r"Taiwan|\bTW\b|台湾", "台湾"),
    (r"Indonesia|\bID\b|印尼", "印度尼西亚"),
    (r"Philippines|\bPH\b|菲律宾", "菲律宾"),
    (r"Thailand|\bTH\b|泰国", "泰国"),
    (r"Singapore|\bSG\b|新加坡", "新加坡"),
    (r"\bLATAM\b", "拉美"),
    (r"\bEU\b|Europe", "欧洲"),
    (r"\bNA\b|North America", "北美"),
    (r"\bBR\b|Brazil", "巴西"),
    (r"\bBD\b|Bangladesh", "孟加拉"),
    (r"\bVN\b|Vietnam", "越南"),
    (r"\bTR\b|Turkey", "土耳其"),
    (r"\bSEA\b", "东南亚"),
    (r"\bMENA\b", "中东 / 北非"),
    (r"\bKH\b", "柬埔寨"),
]

TITLE_ZH = {
    "Arena Breakout: Infinite Top Up": "暗区突围：无限 直充",
    "Point Blank Cash(SEA)": "Point Blank Cash（东南亚）",
    "Point Blank Cash(ID)": "Point Blank Cash（印尼）",
    "Valorant Point Philippines": "Valorant Point 菲律宾",
    "Valorant Point Malaysia": "Valorant Point 马来西亚",
    "Valorant Point Thailand": "Valorant Point 泰国",
    "Valorant Point Indonesia": "Valorant Point 印尼",
    "Valorant Point Singapore": "Valorant Point 新加坡",
    "Mecha BREAK Corite Top Up": "Mecha BREAK Corite 直充",
    "PUBG Mobile UC(Global)": "PUBG Mobile UC（全球）",
    "PUBG Mobile UC(MY)": "PUBG Mobile UC（马来西亚）",
    "PUBG Mobile UC(Taiwan)": "PUBG Mobile UC（台湾）",
    "PUBG Mobile UC(Indonesia)": "PUBG Mobile UC（印尼）",
    "PUBG Mobile Royale Pass Pack(Global)": "PUBG Mobile 皇家通行证礼包（全球）",
    "PUBG Mobile Royale Pass Pack(MY)": "PUBG Mobile 皇家通行证礼包（马来西亚）",
    "PUBG Mobile Royale Pass Pack(TW)": "PUBG Mobile 皇家通行证礼包（台湾）",
    "PUBG Mobile Lite BattleCoin(Indonesia)": "PUBG Mobile Lite BattleCoin（印尼）",
    "New State Mobile NC": "New State Mobile NC",
    "Free Fire Diamonds": "Free Fire 钻石",
    "Free Fire Diamonds(MY/SG/PH/KH)": "Free Fire 钻石（MY/SG/PH/KH）",
    "Free Fire Diamonds(LATAM)": "Free Fire 钻石（拉美）",
    "Free Fire Diamonds(ID)": "Free Fire 钻石（印尼）",
    "Free Fire Diamonds(TH)": "Free Fire 钻石（泰国）",
    "Free Fire Diamonds(EU/TR)": "Free Fire 钻石（欧/土）",
    "Free Fire Diamonds(BR)": "Free Fire 钻石（巴西）",
    "Free Fire Diamonds(TW)": "Free Fire 钻石（台湾）",
    "Free Fire Diamonds(BD)": "Free Fire 钻石（孟加拉）",
    "Free Fire Diamonds(VN)": "Free Fire 钻石（越南）",
    "Free Fire Max Diamonds": "Free Fire Max 钻石",
    "Blood Strike Golds": "Blood Strike 金币",
    "Blood Strike Pass": "Blood Strike 通行证",
    "Blood Strike Max": "Blood Strike Max",
    "Knives Out Vouchers": "荒野行动 点券",
    "Knives Out Package": "荒野行动 礼包",
    "Arena Breakout Bonds": "暗区突围 Bond",
    "Arena Breakout Pass & Packages": "暗区突围 通行证与礼包",
    "Delta Force Global Top Up": "三角洲行动 全球直充",
    "Garena Delta Force SEA Top Up": "Garena 三角洲行动 东南亚直充",
    "Garena Delta Force Malaysia Top Up": "Garena 三角洲行动 马来西亚直充",
    "Garena Delta Force Indonesia Top Up": "Garena 三角洲行动 印尼直充",
    "Garena Delta Force Thailand Top Up": "Garena 三角洲行动 泰国直充",
    "Garena Delta Force Taiwan Top Up": "Garena 三角洲行动 台湾直充",
    "Garena Delta Force Latam Top Up": "Garena 三角洲行动 拉美直充",
    "Garena Delta Force MENA Top Up": "Garena 三角洲行动 中东北非直充",
    "Farlight 84 Diamonds": "Farlight 84 钻石",
    "Crossfire: Legends SEA Top Up": "穿越火线：枪战王者 东南亚直充",
    "Garena Call of Duty Mobile Top Up(MY/SG)": "Garena 使命召唤手游直充（MY/SG）",
    "Garena Call of Duty Mobile CP": "Garena 使命召唤手游 CP",
    "Garena Call of Duty Mobile(TW)Top Up": "Garena 使命召唤手游（台湾）直充",
    "Rainbow Six Mobile Top Up": "彩虹六号手游直充",
    "Marvel Rivals Top Up": "漫威争锋直充",
    "The Division Resurgence Top Up": "全境封锁：复苏直充",
    "Warframe Mobile Top Up": "Warframe 手游直充",
    "Ballistic Hero VNG SEA Top Up": "Ballistic Hero VNG 东南亚直充",
    "T3 Arena T-Gems": "T3 Arena T-Gems",
    "Destiny: Rising Top Up": "命运：崛起直充",
    "Snowbreak: Containment Zone Top Up": "尘白禁区直充",
    "Undawn RC(EU)": "黎明觉醒 RC（欧洲）",
    "Undawn RC(NA)": "黎明觉醒 RC（北美）",
    "Undawn Package(EU)": "黎明觉醒 礼包（欧洲）",
    "Undawn Package(NA)": "黎明觉醒 礼包（北美）",
    "Garena Undawn RC & Package(MY/SG)": "Garena 黎明觉醒 RC 与礼包（MY/SG）",
    "Garena Undawn RC(Indonesia)": "Garena 黎明觉醒 RC（印尼）",
    "Garena Undawn RC(Philippines)": "Garena 黎明觉醒 RC（菲律宾）",
    "Garena Undawn Paket(Indonesia)": "Garena 黎明觉醒 礼包（印尼）",
    "ACECRAFT Global Top Up": "ACECRAFT 全球直充",
    "Mini World Royale Top Up": "迷你世界大逃杀直充",
    "Sausage Man Candies": "香肠派对 糖果",
    "X-Clash Top Up": "X-Clash 直充",
}


def guess_currency(title: str) -> str:
    for pat, name in CURRENCY_HINTS:
        if re.search(pat, title, re.I):
            return name
    return "游戏币"


def guess_region(title: str) -> str:
    for pat, name in REGION_HINTS:
        if re.search(pat, title, re.I):
            return name
    return "对应"


def category_link(text: str) -> tuple[str, str]:
    if re.search(r"Mobile|手游|UC|Free Fire|PUBG|CODM|Undawn|黎明", text, re.I):
        return (
            "手机游戏直充",
            "https://www.seagm.com/zh-hk/direct-topup?code=mobile-game",
        )
    return (
        "游戏直充",
        "https://www.seagm.com/zh-hk/direct-topup?code=game-direct-top-up",
    )


def build(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    title_m = re.search(r"^title:\s*(.+)$", text, re.M)
    src_m = re.search(r"^source_url:\s*(.+)$", text, re.M)
    date_m = re.search(r"^date:\s*(.+)$", text, re.M)
    en_title = (title_m.group(1).strip() if title_m else path.stem).replace("（", "(").replace("）", ")")
    zh_title = TITLE_ZH.get(en_title, TITLE_ZH.get(en_title.replace(" ", ""), en_title))
    # normalize lookup without weird spacing
    if zh_title == en_title:
        for k, v in TITLE_ZH.items():
            if k.replace(" ", "") == en_title.replace(" ", ""):
                zh_title = v
                break
    source = src_m.group(1).strip() if src_m else "https://www.seagm.com/zh-hk/"
    date = date_m.group(1).strip() if date_m else "2026-07-19"
    currency = guess_currency(en_title)
    region = guess_region(en_title)
    cat_name, cat_url = category_link(en_title + " " + zh_title)

    body = f"""---
title: {zh_title}
description: {zh_title} 直充说明与到账须知
source_url: {source}
date: {date}
---

# {zh_title}

**{zh_title}** 直充，可用于皮肤、通行证及其他游戏内消费。

面向 **{region}** 账号的射击 / FPS 类直充。货币：**{currency}**。付款成功后通常即时到账。

- 分类：[{cat_name}]({cat_url})
- 商品页：[{zh_title}]({source})
- 下单前请确认账号 ID、区服 / 渠道（官方 / Garena 等）

!!! warning "重要"
    直充订单一般 **不支持退款与退货**。不同区服或渠道账号不可混用——请仔细核对 ID。

---

## 面额（{currency}）

面额与均价会定时采集。请以 [销售页]({source}) 的实时信息为准。

---

## 如何充值？

1. 打开 SEAGM 商品页，按提示填写游戏账号 / Player ID / UID
2. 选择面额或礼包
3. 付款完成后，额度通常直接发到游戏账号

---

## 在 SEAGM 购买

商品页：[{zh_title}]({source})
"""
    path.write_text(body, encoding="utf-8", newline="\n")
    print("OK", path.name, "->", zh_title)


def main() -> None:
    for path in sorted(root.glob("*.md")):
        build(path)


if __name__ == "__main__":
    main()
