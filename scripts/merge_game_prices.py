# -*- coding: utf-8 -*-
"""Merge the topuplist game tiers into docs/assets/games/prices.json.

The capture step (capture_topuplist_game.py) already returns USD and English
tier names, so there is no FX step here: `price` is the coupon-adjusted figure
the source itself displays, and a single-source product has one price per tier,
so lowest == highest == average — the same row shape the picker cards read.

Two clean-ups the source needs:
  * its tiers repeat once per region/spec ("425 Cores" five times for Wild
    Rift, "(MY)/(ID)/(US)" suffixes for MLBB). The picker shows the tier name
    alone, so duplicates would be indistinguishable — they are folded to the
    cheapest of the same name.
  * "60Coins" and "60  Diamonds" are tidied so the list reads evenly.

The five existing /games/ keys (pubg-mobile, pubg-gcoin, hok, arena-breakout,
where-winds-meet) keep their multi-source ranges and are never touched.
"""
import json
import os
import re
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
TIERS = os.path.join(HERE, "_game_tiers")
PRICES = os.path.join(HERE, "..", "docs", "assets", "games", "prices.json")
DOCS = os.path.join(HERE, "..", "docs")

# One entry per new card. `key` is the prices.json key, the card id and the
# `data-game` the script fills; `slug` is the capture file in _game_tiers/.
# `badge` is the corner tag before the script runs, `channels` the platform
# line in the card footer.
GAMES = [
    {"key": "freefire", "slug": "freefire", "name": "Free Fire",
     "badge": "Mobile", "channels": "Mobile"},
    {"key": "blood-strike", "slug": "blood-strike", "name": "Blood Strike",
     "badge": "Mobile", "channels": "Mobile"},
    {"key": "pokemon-go", "slug": "pokemon-go", "name": "Pokémon GO",
     "badge": "Mobile", "channels": "Mobile"},
    {"key": "mobile-legends", "slug": "mobile-legends",
     "name": "Mobile Legends: Bang Bang", "badge": "Mobile", "channels": "Mobile"},
    {"key": "honkai-star-rail", "slug": "honkai-star-rail",
     "name": "Honkai: Star Rail", "badge": "Mobile", "channels": "Mobile &middot; PC"},
    {"key": "genshin", "slug": "genshin", "name": "Genshin Impact",
     "badge": "Mobile", "channels": "Mobile &middot; PC"},
    {"key": "wuthering-waves", "slug": "wuthering-waves",
     "name": "Wuthering Waves", "badge": "Mobile", "channels": "Mobile &middot; PC"},
    {"key": "zzz", "slug": "zzz", "name": "Zenless Zone Zero",
     "badge": "Mobile", "channels": "Mobile &middot; PC"},
    {"key": "nikke", "slug": "nikke", "name": "GODDESS OF VICTORY: NIKKE",
     "badge": "Mobile", "channels": "Mobile &middot; PC"},
    {"key": "identity-v", "slug": "identity-v", "name": "Identity V",
     "badge": "Mobile", "channels": "Mobile"},
    {"key": "clash-of-clans", "slug": "clash-of-clans", "name": "Clash of Clans",
     "badge": "Mobile", "channels": "Mobile"},
    {"key": "clash-royale", "slug": "clash-royale", "name": "Clash Royale",
     "badge": "Mobile", "channels": "Mobile"},
    {"key": "brawl-stars", "slug": "brawl-stars", "name": "Brawl Stars",
     "badge": "Mobile", "channels": "Mobile"},
    {"key": "love-and-deepspace", "slug": "love-and-deepspace",
     "name": "Love and Deepspace", "badge": "Mobile", "channels": "Mobile"},
    {"key": "eggy-party", "slug": "eggy-party", "name": "Eggy Party",
     "badge": "Mobile", "channels": "Mobile"},
    {"key": "harry-potter", "slug": "harry-potter",
     "name": "Harry Potter: Magic Awakened", "badge": "Mobile", "channels": "Mobile"},
    {"key": "arena-of-valor", "slug": "arena-of-valor", "name": "Arena of Valor",
     "badge": "Mobile", "channels": "Mobile"},
    {"key": "once-human", "slug": "once-human", "name": "Once Human",
     "badge": "PC", "channels": "PC &middot; Mobile"},
    {"key": "delta-force", "slug": "delta-force", "name": "Delta Force",
     "badge": "PC", "channels": "PC &middot; Mobile"},
    {"key": "valorant", "slug": "valorant", "name": "VALORANT",
     "badge": "PC", "channels": "PC"},
    {"key": "marvel-rivals", "slug": "marvel-rivals", "name": "Marvel Rivals",
     "badge": "PC", "channels": "PC"},
    {"key": "arknights-endfield", "slug": "arknights-endfield",
     "name": "Arknights: Endfield", "badge": "PC", "channels": "PC &middot; Mobile"},
    {"key": "diablo-iv", "slug": "diablo-iv", "name": "Diablo IV",
     "badge": "PC", "channels": "PC"},
    {"key": "lol-wild-rift", "slug": "lol-wild-rift",
     "name": "League of Legends: Wild Rift", "badge": "Mobile", "channels": "Mobile"},
    {"key": "whiteout-survival", "slug": "whiteout-survival-top-up",
     "name": "Whiteout Survival", "badge": "Mobile", "channels": "Mobile &middot; PC"},
]

# The five keys already on the page: ranges from several sources, left alone.
KEEP = ["pubg-mobile", "pubg-gcoin", "hok", "arena-breakout", "where-winds-meet"]

# Quote-only cards, 2026-10-29. These are services, not tier lists: the source
# quotes per order, so there is nothing for main() to merge and no prices.json
# row behind them — build_games_page skips its row check for these keys but
# still wants the 2400x500 brand image. The card lists what is sold and sends
# the reader to chat for the price (`line`); `msg` is the sentence Buy opens
# the chat with. No `foot`: the user asked for the platform line to go
# (2026-10-29), so this card carries no footnote at all.
#
# CS2 comes from an 8591 listing (seller 松鼠遊戲, id 2370886087) whose only
# figure is the platform's NT$10 unit price — a nominal listing price, not a
# tier. Nothing is converted to USD and nothing is printed: the site quotes in
# USD only, $0.31 would read as the price of a skin, and NT$10 belongs to the
# listing rather than to an order. The card therefore shows no figure anywhere;
# the number is given in the chat.
QUOTE = [
    {"key": "cs2", "name": "CS2 Skins &amp; Credits", "badge": "PC",
     "alt": "Counter-Strike 2",
     "line": "Skins through BUFF or YouPin &mdash; no real-name account, no "
             "seven-day wait &mdash; plus SkinClub, 5E, FACEIT, BUFF credit, "
             "knife upgrades and name-change cards.",
     "msg": "Hi, I'd like a quote for CS2 skins or credits."},
]

MAX_TIERS = 24          # per currency group: longer than this stops scanning
REGION = re.compile(r"\s*[(（]([^()（）]{1,14})[)）]\s*$")


def clean_name(name):
    """Drop the region/spec suffix and tidy spacing so duplicates collapse."""
    n = REGION.sub("", name.strip())
    n = re.sub(r"\s+", " ", n)
    n = re.sub(r"(?<=\d)(?=[A-Za-z])", " ", n)      # 60Coins -> 60 Coins
    n = re.sub(r"\s*\+\s*", " + ", n)               # 300 +30 -> 300 + 30
    n = re.sub(r"^1\s+(?=[A-Za-z])", "", n)         # "1 Strike Pass" -> "Strike Pass"
    n = re.sub(r"\bpass\b", "Pass", n)              # Monthly pass -> Monthly Pass
    return n.strip()


def pick_region(skus):
    """One region's tiers — the card has no region picker.

    topuplist lists the same item once per server ("(MY)", "(ID)", "Delta
    Coins (Latam)"…). Merged blindly, one picker shows three different prices
    for "64 + 6 Diamonds". Prefer the rows with no region tag (the neutral
    set); if every row is tagged, take the region with the most tiers.
    """
    plain, by_region = [], []
    for s in skus:
        name = s.get("name") or ""
        m = REGION.search(name)
        if m:
            by_region.append((m.group(1), s))
        else:
            plain.append(s)
    if plain:
        return plain, None
    if not by_region:
        return [], None
    counts = {}
    for region, _ in by_region:
        counts[region] = counts.get(region, 0) + 1
    region = max(counts, key=lambda r: counts[r])
    return [s for r, s in by_region if r == region], region


def rows_for(game):
    fp = os.path.join(TIERS, game["slug"] + ".json")
    if not os.path.exists(fp):
        sys.exit(f"missing capture: {fp}")
    data = json.load(open(fp, encoding="utf-8"))

    skus, region = pick_region(data.get("skus") or [])
    if region:
        print(f"   {game['key']}: every tier is region-tagged, using {region}")

    best, order = {}, []
    for sku in skus:
        price = sku.get("price")
        if price is None or price <= 0:
            continue
        title = clean_name(sku.get("name") or "")
        if not title:
            continue
        if title not in best:
            best[title] = price
            order.append(title)
        else:
            best[title] = min(best[title], price)

    rows = [{"title": t, "lowest": round(best[t], 2), "highest": round(best[t], 2),
             "average": round(best[t], 2)} for t in order]

    # Group by the currency in the name ("… Coupons" vs "… Vouchers"), so a
    # game sold in two currencies reads as two runs instead of one interleaved
    # list; number-led tiers come first because those are the ones compared.
    def unit(r):
        return r["title"].split()[-1].lower()

    def numbered(r):
        return 0 if r["title"][:1].isdigit() else 1

    rows.sort(key=lambda r: (numbered(r), unit(r), r["lowest"]))

    # Cap each currency run on its own: cutting the whole list would take the
    # top of one currency and leave the other ending mid-range.
    out = []
    run = []
    for r in rows + [None]:
        if r is not None and (not run or unit(r) == unit(run[0])):
            run.append(r)
            continue
        if len(run) > MAX_TIERS:
            # Keep the entry tiers — the ones a reader actually compares — and
            # the two largest, so the card still shows where the range ends.
            run = run[: MAX_TIERS - 2] + run[-2:]
        out.extend(run)
        run = [r] if r is not None else []
    return out


def referenced(key):
    """True if any page asks for this key via data-game="…"."""
    pat = 'data-game="%s"' % key
    for root, _, files in os.walk(DOCS):
        for f in files:
            if not f.endswith((".md", ".html")):
                continue
            try:
                if pat in open(os.path.join(root, f), encoding="utf-8").read():
                    return True
            except UnicodeDecodeError:
                continue
    return False


def main():
    data = json.load(open(PRICES, encoding="utf-8"))
    games = data["games"]

    for key in KEEP:
        if key not in games:
            sys.exit(f"existing /games/ key disappeared: {key}")

    for game in GAMES:
        key = game["key"]
        if key in KEEP:
            sys.exit(f"{key} is one of the untouched keys")
        old = games.get(key)
        if old and "lowest" not in old[0]:
            # An {official, acebase} row is the retired /topup/ shape. If no
            # page still asks for it the row is orphaned and can be replaced;
            # if one does, the two pages would fight over one key.
            if referenced(key):
                sys.exit(f"{key} still has an official/acebase row that a page "
                         f"reads — pick another key instead of overwriting it")
            print(f"   note: replacing orphaned /topup/-era row for {key}")
        rows = rows_for(game)
        games[key] = rows
        lo = min(r["lowest"] for r in rows)
        hi = max(r["lowest"] for r in rows)
        print(f"{key:<22} {len(rows):2d} tiers  {lo:>8.2f} .. {hi:>8.2f} USD")

    data["updated"] = date.today().isoformat()
    data["currency"] = "USD"
    # No conversion happens any more, but the field is part of the file's shape
    # and the live-price page reads it; keep the last known rate rather than
    # dropping the key.
    data.setdefault("fx", {"SGD": 0.783322, "asOf": ""})

    ordered = {}
    for k, v in games.items():
        ordered[k] = v
    data["games"] = ordered

    with open(PRICES, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"\n{len(GAMES)} products merged; prices.json updated {data['updated']}")
    print("remember: bump games-prices.js cache version")


if __name__ == "__main__":
    main()
