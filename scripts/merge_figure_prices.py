#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the eight /figures/ cards' prices into prices.json.

The eight cards on /figures/ carry the same price machinery the three price
pages do — an `ab-ec-list[data-game]` block that docs/javascripts/games-prices.js
fills from prices.json — so that the card's title price, its corner badge and
its foot date all come from one place the way they do on /topup/ and /cdkeys/.

What is different is where the numbers come from. Every other merge script
translates a source it captured (a shop's tiers, a wallet's list price, an FX
rate against a cached denomination). **These are placeholder figures**: the page
shipped before anyone had quoted the eight pieces, and the user asked for
random prices to start with. They are marked as such on the cards themselves
(「示例价」 in the foot line) so a reader cannot mistake them for a quote.

The randomness is seeded per card id, so a re-run reproduces the same numbers
rather than reshuffling the page every time the script is touched. **Replacing
these with real prices means editing PRICES below (or writing them from a
source, the way merge_live_prices.py does) and re-running** — nothing else on
the page has to move.

One row per card, of the same shape the fourteen live platforms use: a single
retail price, so lowest/highest/average are the same number and no range is
invented. Rows carry no `off` — a figure has no list price to discount against,
so the card keeps the channel tag it ships with instead of a saving.

Re-run chain, and the order matters: scripts/update_prices.py FIRST, then every
merge_*.py. update_prices.py starts from `games = {}` and rewrites the whole
file from its own table, so it drops every merged key (and `currency` and `fx`)
— running it after this leaves all eight cards reading 价格即将上线. After a
re-run, bump the fallback version in docs/javascripts/games-prices.js to match
UPDATED, or a returning reader keeps the cached copy of prices.json and sees
the old numbers (a stale cache is served silently).

Usage:  python scripts/merge_figure_prices.py
"""
import datetime
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
PRICES_JSON = os.path.normpath(
    os.path.join(HERE, "..", "docs", "assets", "games", "prices.json"))

# Card id -> (row label, placeholder price in USD). The ids are the cards' own
# ids on /figures/, which is what ab-ec-list[data-game] resolves against.
#
# The label is what the row is called. Nothing draws it today — the --figure
# branch in games-prices.js leaves the block empty, the price already sitting at
# the end of the card's title — but it is the field every other key in this file
# carries, and a row without one would be the odd one out the day the branch
# changes.
PRICES = {
    "gear-13": ("初音未来 With You 2021 1/7", None),
    "gear-14": ("流萤 春日手信", None),
    "gear-15": ("风堇 Hyacine", None),
    "gear-16": ("游戏机初音未来", None),
    "gear-17": ("黄裙明日香", None),
    "gear-18": ("紫伞与黑风衣", None),
    "gear-19": ("CCSTOYS 山姆·费舍尔", None),
    "gear-20": ("猫猫《药屋少女的呢喃》1/7", None),
}

# Placeholder range, in USD. 1/7 scale figures run roughly this band; the low
# end suits a prize figure, the top a limited one.
LOW, HIGH = 79, 259


def placeholder(card_id):
    """A stable pseudo-random price for one card.

    Seeded by the id, so the eight numbers are arbitrary but fixed: re-running
    this script does not reshuffle the page, and a diff after a re-run is empty
    unless the id set or the range changed.
    """
    rng = random.Random("figures/" + card_id)
    return float(rng.randint(LOW, HIGH)) - 0.01


def main():
    with open(PRICES_JSON, encoding="utf-8") as f:
        d = json.load(f)
    d.setdefault("games", {})

    written = []
    for card_id, (label, price) in PRICES.items():
        if price is None:
            price = placeholder(card_id)
        d["games"][card_id] = [{
            "title": label,
            "lowest": round(price, 2),
            "highest": round(price, 2),
            "average": round(price, 2),
        }]
        written.append((card_id, label, price))

    d["updated"] = datetime.date.today().isoformat()
    # update_prices.py drops these two keys when it rewrites the file, so every
    # merge script puts them back — the site displays one currency and one rate
    # table, and a missing `currency` is read as "no data" by some tooling.
    d.setdefault("currency", "USD")
    d.setdefault("fx", {})

    with open(PRICES_JSON, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"{PRICES_JSON}")
    for card_id, label, price in written:
        print(f"  {card_id}  ${price:>7.2f}  {label}")
    print(f"updated = {d['updated']}  (共 {len(d['games'])} 个 key)")
    print("\n接下来：改 docs/javascripts/games-prices.js 里那个 "
          f"\"20260921\" 的兜底版本号为 {d['updated'].replace('-', '')}")


if __name__ == "__main__":
    main()
