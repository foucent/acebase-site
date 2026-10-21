# -*- coding: utf-8 -*-
"""Regenerate the card grid and Product list on docs/topup/index.md.

Thirty cards is too much markup to keep in hand-written Markdown, so the page
carries a marked region for the grid and this script rewrites both the grid and
the JSON-LD Product list from merge_ent_prices.ENTERTAINMENT (the single list of
keys and names):

    <!-- TOPUP:CARDS:START --> … <!-- TOPUP:CARDS:END -->

The Product list gets no markers: it sits inside <script type="application/
ld+json">, where an HTML comment is not legal JSON and invalidated the whole
graph on /games/. It is found by its own shape instead.

When the markers are absent (the page built before this script) the 13 old code
cards are replaced in place: the region runs from the first <article> to the
last </article>, and the markers are written around the generated grid.

Everything that would break the build is checked before the file is written:
card count, unique ids, balanced <article> tags (gen_home.py counts them), a
prices.json row for every card, and a 2400×500 brand image for every card.
"""
import json
import os
import re
import struct
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
PAGE = os.path.join(ROOT, "docs", "topup", "index.md")
PRICES = os.path.join(ROOT, "docs", "assets", "games", "prices.json")
BRANDS = os.path.join(ROOT, "docs", "assets", "games", "brand")

CARDS_START = "<!-- TOPUP:CARDS:START -->"
CARDS_END = "<!-- TOPUP:CARDS:END -->"
ITEMS_START = "<!-- TOPUP:ITEMS:START -->"
ITEMS_END = "<!-- TOPUP:ITEMS:END -->"

TOTAL = 30
CARD_CLASS = ("ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate "
              "ab-card--picker ab-card--wordmark")


def load_table():
    """Import merge_ent_prices without running it (and under python -I, where
    the script directory is not on sys.path)."""
    spec = importlib.util.spec_from_file_location(
        "merge_ent_prices", os.path.join(HERE, "merge_ent_prices.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def card_block(key, name, first, updated):
    """One picker card, matching the markup the page already uses."""
    lazy = "" if first else ' loading="lazy"'
    return f"""<article class="{CARD_CLASS}" id="{key}">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/{key}.png" alt="{name} top-up price reference"{lazy} decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">{name}<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy {name}.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="{key}">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">{updated}</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>"""


def png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


def main():
    mt = load_table()
    text = open(PAGE, encoding="utf-8").read()
    prices = json.load(open(PRICES, encoding="utf-8"))
    updated = prices["updated"]
    products = mt.ENTERTAINMENT
    keys = [p["key"] for p in products]

    # ---- checks
    if len(keys) != TOTAL:
        sys.exit(f"{len(keys)} keys in ENTERTAINMENT, expected {TOTAL}")
    if len(set(keys)) != len(keys):
        sys.exit("duplicate key in ENTERTAINMENT")
    for key in keys:
        rows = prices["games"].get(key)
        if not rows:
            sys.exit(f"{key}: no rows in prices.json")
        if "lowest" not in rows[0]:
            sys.exit(f"{key}: prices.json row is not the picker shape")
        p = os.path.join(BRANDS, key + ".png")
        if not os.path.exists(p):
            sys.exit(f"{key}: missing brand image {p}")
        size = png_size(p)
        if size != (2400, 500):
            sys.exit(f"{key}: brand image is {size}, expected (2400, 500)")

    blocks = [card_block(p["key"], p["name"], first=(i == 0), updated=updated)
              for i, p in enumerate(products)]
    joined = "\n".join(blocks)
    if joined.count("<article") != TOTAL or joined.count("</article>") != TOTAL:
        sys.exit(f"generated {joined.count('<article')} opening and "
                 f"{joined.count('</article>')} closing tags, expected {TOTAL}")

    grid = "\n".join("    " + b for b in blocks)
    new_grid = f"{CARDS_START}\n{grid}\n    {CARDS_END}"

    # ---- cards region: replace or create
    if CARDS_START in text:
        a = text.index(CARDS_START)
        b = text.index(CARDS_END) + len(CARDS_END)
        text = text[:a] + new_grid + text[b:]
    else:
        first = text.index("<article")
        last = text.rindex("</article>") + len("</article>")
        line_start = text.rindex("\n", 0, first) + 1
        text = text[:line_start] + new_grid + text[last:]

    # ---- Product list
    items = ",\n".join(
        '        { "@type": "Product", "position": %d, "name": "%s", '
        '"url": "https://acebase.cc/topup/#%s" }' % (i + 1, p["name"], p["key"])
        for i, p in enumerate(products))
    new_items = "\n" + items + "\n      "

    if ITEMS_START in text:          # a page built before the fix still has them
        a = text.index(ITEMS_START)
        b = text.index(ITEMS_END) + len(ITEMS_END)
        text = text[:a] + new_items + text[b:]
    else:
        a = text.index('"itemListElement": [', text.index('"@type": "ItemList"'))
        a = a + len('"itemListElement": [')
        b = text.index("]", a)
        text = text[:a] + new_items + text[b:]

    text = re.sub(r'"numberOfItems": "\d+"', '"numberOfItems": "%d"' % TOTAL, text)

    # ---- whole-file sanity before writing
    if text.count("<article") != text.count("</article>"):
        sys.exit("unbalanced <article> after render — gen_home.py counts these")
    if text.count("<article") != TOTAL:
        sys.exit(f"{text.count('<article')} cards on the page after render, "
                 f"expected {TOTAL}")

    open(PAGE, "w", encoding="utf-8", newline="\n").write(text)
    print(f"wrote {PAGE}: {TOTAL} cards, Product list 1..{TOTAL}")


if __name__ == "__main__":
    main()
