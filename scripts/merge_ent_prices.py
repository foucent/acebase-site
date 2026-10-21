# -*- coding: utf-8 -*-
"""Merge the topuplist entertainment tiers into docs/assets/games/prices.json.

The capture step (capture_topuplist_entertainment.py) already returns USD and
English tier names, so there is no FX step: `price` is the coupon-adjusted
figure the source displays, and a single-source product has one price per tier,
so lowest == highest == average — the row shape the picker cards read.

What this file owns:
  * ENTERTAINMENT — the 30 platforms /topup/ shows, in card order. This table is
    the single source of truth: build_topup_page.py imports it, and the capture
    script only fetches the slugs listed here.
  * the tier clean-ups the source needs (a few Chinese units survive lang=en,
    the same tier repeats once per region, spacing is uneven).
  * the price rows for exactly those 30 keys. Every other key in prices.json —
    the six gift cards /gift-cards/ still shows, the /games/ keys — is left
    untouched.

    python scripts/merge_ent_prices.py
"""
import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
TIERS = os.path.join(HERE, "_ent_tiers")
PRICES = os.path.join(HERE, "..", "docs", "assets", "games", "prices.json")

# key = prices.json key = card id = data-game = brand image file name.
# slug = capture file in _ent_tiers/. Order here is the order on the page:
# the fourteen platforms that were already there, then the sixteen added.
ENTERTAINMENT = [
    {"key": "douyin-top-up", "slug": "douyin-top-up", "name": "Douyin Live"},
    {"key": "kwi-top-up", "slug": "kwi-top-up", "name": "Kuaishou Live"},
    {"key": "bigo-live", "slug": "bigo-live", "name": "Bigo Live"},
    {"key": "mico-top-up", "slug": "mico-top-up", "name": "MICO"},
    {"key": "poppo-live", "slug": "poppo-live", "name": "Poppo Live"},
    {"key": "tango-live-recharge", "slug": "tango-live-recharge", "name": "Tango Live"},
    {"key": "mango", "slug": "mango", "name": "Mango Live"},
    {"key": "migo-top-up", "slug": "migo-top-up", "name": "MIGO Live"},
    {"key": "superlive", "slug": "superlive", "name": "SuperLive"},
    {"key": "dazz-top-up", "slug": "dazz-top-up", "name": "Dazz Live"},
    {"key": "xena-live-group-voice", "slug": "xena-live-group-voice", "name": "Xena Live"},
    {"key": "bixin-top-up", "slug": "bixin-top-up", "name": "Bi Xin"},
    {"key": "ludo-club", "slug": "ludo-club", "name": "Ludo Club"},
    {"key": "yalla-ludo", "slug": "yalla-ludo", "name": "Yalla Ludo"},
    {"key": "starmaker", "slug": "starmaker", "name": "StarMaker"},
    {"key": "sugo-top-up", "slug": "sugo-top-up", "name": "SUGO"},
    {"key": "imo-top-up", "slug": "imo-top-up", "name": "IMO"},
    {"key": "chamet", "slug": "chamet", "name": "Chamet"},
    {"key": "likee", "slug": "likee", "name": "Likee"},
    {"key": "telegram", "slug": "telegram", "name": "Telegram"},
    {"key": "party-star", "slug": "party-star", "name": "Party Star"},
    {"key": "capcut", "slug": "capcut", "name": "CapCut"},
    {"key": "zepeto", "slug": "zepeto", "name": "ZEPETO"},
    {"key": "heesay-top-up", "slug": "heesay-top-up", "name": "HeeSay"},
    {"key": "soulchill", "slug": "soulchill", "name": "Soulchill"},
    {"key": "dido", "slug": "dido", "name": "DiDO"},
    {"key": "qqcoin-top-up", "slug": "qqcoin-top-up", "name": "QQ Coin"},
    {"key": "qqvip-top-up", "slug": "qqvip-top-up", "name": "QQ VIP"},
    {"key": "yy-live", "slug": "yy-live", "name": "YY Live"},
    {"key": "nimo-tv", "slug": "nimo-tv", "name": "Nimo TV"},
]

MAX_TIERS = 24          # per currency group: longer than this stops scanning
REGION = re.compile(r"\s*[(（]([^()（）]{1,14})[)）]\s*$")
CJK = re.compile("[㐀-鿿　-〿＀-￯]")

# lang=en still leaves Chinese on a few tier names (Bi Xin's "10 比心币", and
# occasionally the Douyin/Kuaishou units). The picker prints the title as-is,
# so each unit is mapped to English; anything unmapped fails the CJK assert at
# the end rather than shipping Chinese onto the page.
UNIT = [
    # Longer units first: 比心钻石 must win over the bare 钻石 rule.
    ("比心钻石", "Bi Xin Diamonds"), ("比心币", "Bi Xin Coins"),
    ("快币", "Kuaishou Coins"), ("抖币", "Douyin Coins"),
    ("音浪", "Yinlang"), ("元气", "Yuanqi"), ("钻石", "Diamonds"),
    ("金币", "Coins"), ("元", "Yuan"),
]


def clean_name(name):
    """English units, no region suffix, even spacing — so duplicates collapse."""
    n = (name or "").strip()
    for zh, en in UNIT:
        if zh in n:
            n = re.sub(r"(\d+)\s*" + zh, r"\1 " + en, n)
            n = n.replace(zh, en)
    # QQ VIP's tiers come with full-width brackets and a space before the
    # closing one: "(QQ VIP 1 Month )". Only the brackets are normalised — the
    # label inside is the plan name, which the picker has to show.
    n = n.replace("（", "(").replace("）", ")")
    n = re.sub(r"\(\s+", "(", n)
    n = re.sub(r"\s+\)", ")", n)
    # QQ VIP repeats the plan in brackets on some tiers and not on others
    # ("QQ Membership Monthly Card (QQ VIP 1 Month)"), which would split one
    # plan into two rows. The plan is already in the name, so drop it.
    n = re.sub(r"\s*\((?:QQ SVIP|QQ VIP)[^()]*\)\s*$", "", n)
    n = REGION.sub("", n)
    n = re.sub(r"\s+", " ", n)
    n = re.sub(r"(?<=\d)(?=[A-Za-z])", " ", n)      # 60Coins -> 60 Coins
    n = re.sub(r"\s*\+\s*", " + ", n)               # 300 +30 -> 300 + 30
    n = re.sub(r"\bpass\b", "Pass", n)
    # ZEPETO's largest tier is spelled "300000 Coin" at the source; the picker
    # prints the title as-is, and one singular among twelve plurals reads as a
    # typo on our own page. \b after the word keeps "Q Coins" out of it.
    n = re.sub(r"\b(\d+) Coin\b", r"\1 Coins", n)
    return n.strip()


def rows_for(product):
    """The picker rows for one product.

    Unlike the games, none of these products repeat a tier per region inside
    one product's sku list — every capture's names are plain ("500 Coins"), so
    there is no region set to pick between. Duplicates that remain are the same
    tier sold at several prices, folded to the cheapest.
    """
    fp = os.path.join(TIERS, product["slug"] + ".json")
    if not os.path.exists(fp):
        sys.exit(f"missing capture: {fp}")
    data = json.load(open(fp, encoding="utf-8"))

    best, original, order = {}, {}, []
    for sku in data.get("skus") or []:
        price = sku.get("price")
        if price is None or price <= 0:
            continue
        title = clean_name(sku.get("name"))
        if not title:
            continue
        if title not in best:
            best[title] = price
            original[title] = sku.get("original")
            order.append(title)
        elif price < best[title]:
            best[title] = price
            original[title] = sku.get("original")

    rows = [{"title": t, "lowest": round(best[t], 2), "highest": round(best[t], 2),
             "average": round(best[t], 2)} for t in order]

    def unit(r):
        return r["title"].split()[-1].lower()

    def size(r):
        m = re.match(r"(\d+)", r["title"])
        return int(m.group(1)) if m else 10 ** 9

    # These platforms sell in several currencies per product (Coins and Gold,
    # ZEMs and Coins), and price does NOT climb with size the way it does on
    # /games/ — a mid-size tier sold in a cheaper region can cost less than a
    # smaller one. So each currency run is ordered by price, and the runs are
    # ordered by their cheapest tier: the picker reads cheapest-first and
    # rows[0] (the title price) is the entry price.
    groups = {}
    for r in rows:
        groups.setdefault(unit(r), []).append(r)
    runs = [sorted(g, key=lambda r: (r["lowest"], size(r)))
            for g in groups.values()]
    runs.sort(key=lambda g: (g[0]["lowest"], size(g[0])))

    out = []
    for run in runs:
        if len(run) > MAX_TIERS:
            # Keep the entry tiers the reader compares, plus the two largest so
            # the card still shows where the range ends.
            run = run[: MAX_TIERS - 2] + run[-2:]
        out.extend(run)

    # The corner badge: a discount percentage once the script runs, the static
    # Live tag otherwise (games-prices.js writes rows[0].off over the badge and
    # adds the --off class).
    if out:
        orig = original.get(out[0]["title"])
        try:
            orig = float(orig or 0)
        except (TypeError, ValueError):
            orig = 0
        if orig > out[0]["lowest"] > 0:
            pct = int(round((1 - out[0]["lowest"] / orig) * 100))
            if pct > 0:
                out[0] = dict(out[0], off=f"-{pct}%")
    return out


def main():
    data = json.load(open(PRICES, encoding="utf-8"))
    games = data["games"]

    keys = [p["key"] for p in ENTERTAINMENT]
    if len(set(keys)) != len(keys):
        sys.exit("duplicate key in ENTERTAINMENT")

    for product in ENTERTAINMENT:
        rows = rows_for(product)
        if not rows:
            sys.exit(f"{product['key']}: capture produced no tiers")
        bad = [r["title"] for r in rows if CJK.search(r["title"])]
        if bad:
            sys.exit(f"{product['key']}: Chinese left in tier titles: {bad}")
        games[product["key"]] = rows
        lo = min(r["lowest"] for r in rows)
        hi = max(r["lowest"] for r in rows)
        print(f"{product['key']:<24} {len(rows):2d} tiers  {lo:>7.2f} .. {hi:>8.2f} USD"
              f"  {rows[0].get('off', '')}")

    data["updated"] = date.today().isoformat()
    data["currency"] = "USD"
    data.setdefault("fx", {"SGD": 0.783322, "asOf": ""})

    with open(PRICES, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n{len(ENTERTAINMENT)} products merged; prices.json updated {data['updated']}")
    print("remember: bump games-prices.js cache version")


if __name__ == "__main__":
    main()
