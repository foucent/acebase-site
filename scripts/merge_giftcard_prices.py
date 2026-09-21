#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the gift-card and cdkey denominations into prices.json.

These thirteen products moved off the old /gift-cards/ page onto /topup/ on
2026-09-21, where every card quotes its tiers out of prices.json like the five
game cards above it. The catalog below is the whole source: each denomination
carries a single retail price, there is no range to compute and no endpoint to
re-scrape, so nothing here names a vendor either.

Each key is also the card's id on /topup and its brand-plate filename, and the
tier order here is the order the rows print in — the first tier is the one the
shut card shows in red.

Re-run chain, and the order matters: scripts/update_prices.py FIRST, then this.
update_prices.py starts from `games = {}` and rewrites the whole file from its
own SEO_TERMS, so it drops all thirteen keys below (and `currency`) — running it
after this one leaves thirteen cards reading 价格即将上线. After a re-run, bump
the cache-busting version in docs/javascripts/games-prices.js to match UPDATED,
and the static .js-prices-updated text on the page.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRICES_JSON = os.path.normpath(
    os.path.join(HERE, "..", "docs", "assets", "games", "prices.json"))

UPDATED = "2026-09-21"

# key -> [(tier label, USD), ...] in page order, cheapest first.
CARDS = {
    "amazon-gift-card-us": [
        ("5 USD", 4.95), ("10 USD", 9.90), ("20 USD", 19.80),
        ("35 USD", 34.65), ("50 USD", 49.50), ("100 USD", 99.00),
    ],
    "apple-gift-card": [
        ("5 USD", 4.50), ("10 USD", 9.00), ("20 USD", 18.00), ("50 USD", 45.00),
        ("100 USD", 90.00), ("200 USD", 181.80), ("500 USD", 454.50),
    ],
    "google-play-gift-card": [
        ("5 USD", 4.95), ("10 USD", 9.90), ("15 USD", 14.85),
        ("25 USD", 24.75), ("50 USD", 49.50), ("100 USD", 99.00),
    ],
    "netflix-gift-card-us": [
        ("20 USD", 20.25), ("25 USD", 25.20), ("30 USD", 29.70),
        ("50 USD", 49.50), ("60 USD", 59.40), ("100 USD", 94.50),
    ],
    "xbox-gift-card": [
        ("5 USD", 4.59), ("10 USD", 8.97), ("15 USD", 13.49), ("20 USD", 17.99),
        ("25 USD", 22.03), ("50 USD", 43.91), ("100 USD", 88.19),
    ],
    "kammelna-gift-card": [
        ("30 天", 8.09), ("90 天", 19.79), ("180 天", 36.89), ("365 天", 66.59),
        ("4000 金卡", 11.42), ("12000 金卡", 26.21), ("50000 金卡", 103.41),
        ("100000 金卡", 199.71), ("250000 金卡", 485.91),
    ],
    "fortnite-vbucks-card": [
        ("1000 V-Bucks", 8.99), ("2800 V-Bucks", 22.49),
        ("5000 V-Bucks", 35.99), ("13500 V-Bucks", 89.99),
    ],
    "apex-legends-coins-card": [
        ("1000 Coins", 10.01), ("2150 Coins", 20.18), ("4350 Coins", 33.54),
        ("6700 Coins", 49.76), ("10500 Coins", 101.41),
    ],
    "playstation-network-card-us": [
        ("1 USD", 1.07), ("2 USD", 2.15), ("3 USD", 3.04), ("4 USD", 3.95),
        ("10 USD", 9.00), ("25 USD", 21.60), ("50 USD", 44.10), ("75 USD", 66.60),
        ("100 USD", 89.10), ("150 USD", 133.20), ("200 USD", 178.20),
    ],
    "nintendo-switch-online": [
        ("3 个月", 8.69), ("12 个月", 19.13),
    ],
    "nintendo-eshop-card-us": [
        ("10 USD", 8.81), ("20 USD", 17.54), ("35 USD", 30.14), ("50 USD", 43.19),
    ],
    "steam-wallet-card-us": [
        ("5 USD", 5.12), ("10 USD", 10.16), ("20 USD", 20.33), ("25 USD", 25.19),
        ("30 USD", 28.61), ("50 USD", 47.69), ("100 USD", 99.27),
    ],
    "gocash-card": [
        ("5 USD", 4.31), ("10 USD", 8.54), ("15 USD", 13.49),
        ("20 USD", 17.09), ("50 USD", 43.19), ("100 USD", 86.39),
    ],
}


def main():
    d = json.load(open(PRICES_JSON, encoding="utf-8"))
    tiers_written = 0

    for key, tiers in CARDS.items():
        if not tiers:
            raise SystemExit(f"{key}: 没有档位")
        # renderEcList treats `rows[0].lowest == null` as no data and prints the
        # 价格即将上线 placeholder for the whole card, so the entry tier has to
        # be a real number — a typo here empties a card on the page instead of
        # failing anywhere a test would see it.
        for label, price in tiers:
            if not isinstance(price, (int, float)) or price <= 0:
                raise SystemExit(f"{key}/{label}: 价格必须是正数，实际 {price!r}")
        # One retail price per tier, so the three fields are the same number.
        # The range columns exist because the game cards are scraped from
        # several channels; there is nothing to average here and inventing a
        # spread would put a made-up figure on the page.
        d["games"][key] = [
            {"title": label, "lowest": price, "highest": price, "average": price}
            for label, price in tiers
        ]
        tiers_written += len(tiers)
        print(f"  {key:32s} {len(tiers):2d} 档  ${tiers[0][1]:.2f} 起")

    # update_prices.py writes only {"updated", "games"} and would drop this.
    d["currency"] = "USD"
    d["updated"] = UPDATED

    json.dump(d, open(PRICES_JSON, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"wrote {PRICES_JSON}  ({len(CARDS)} keys, {tiers_written} tiers, "
          f"updated={UPDATED})")
    print(f"!! 记得同步 docs/javascripts/games-prices.js 的版本号 "
          f"-> {UPDATED.replace('-', '')}")


if __name__ == "__main__":
    main()
