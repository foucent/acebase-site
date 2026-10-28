# -*- coding: utf-8 -*-
"""Regenerate the card grid and Product list on docs/games/index.md.

Thirty-one cards is too much markup to keep in hand-written Markdown, so the
page carries a marked region for the grid and this script rewrites both the grid
and the JSON-LD Product list from merge_game_prices.GAMES and .QUOTE (the single
lists of keys, names and platforms):

    <!-- GAMES:CARDS:START --> … <!-- GAMES:CARDS:END -->

The Product list gets no markers: it sits inside
<script type="application/ld+json">, where an HTML comment is not legal JSON
and invalidated the whole graph. It is found by its own shape instead.

The five cards that predate the topuplist import are copied out of the page
byte for byte and put back unchanged — they carry attributes (the first card's
fetchpriority, pubg-gcoin's data-discount) that a template would have to know
about. Only ids missing from the page are generated, then the whole grid is
re-emitted in KEEP + GAMES + QUOTE order so the JSON-LD position always matches
the card order. Quote cards are the exception: they are re-emitted from the
table on every run, because their copy is the table's, not the page's.

Everything that would break the build is checked before the file is written:
card count, unique ids, balanced <article> tags (gen_home.py counts them),
a prices.json row for every priced card, and a 2400×500 brand image for every
card.
"""
import html
import json
import os
import re
import struct
import sys
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
PAGE = os.path.join(ROOT, "docs", "games", "index.md")
PRICES = os.path.join(ROOT, "docs", "assets", "games", "prices.json")
BRANDS = os.path.join(ROOT, "docs", "assets", "games", "brand")

CARDS_START = "<!-- GAMES:CARDS:START -->"
CARDS_END = "<!-- GAMES:CARDS:END -->"
ITEMS_START = "<!-- GAMES:ITEMS:START -->"
ITEMS_END = "<!-- GAMES:ITEMS:END -->"

TOTAL = 31
CARD_CLASS = ("ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate "
              "ab-card--picker ab-card--wordmark")
QUOTE_CLASS = ("ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate "
               "ab-card--quote ab-card--wordmark")


def load_games_table():
    """Import merge_game_prices without running it (and under python -I, where
    the script directory is not on sys.path)."""
    spec = importlib.util.spec_from_file_location(
        "merge_game_prices", os.path.join(HERE, "merge_game_prices.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def card_block(key, name, badge, channels, alt, first, updated):
    """One picker card, matching the markup the page already uses."""
    lazy = "" if first else ' loading="lazy"'
    return f"""<article class="{CARD_CLASS}" id="{key}">
      <div class="ab-card__media">
        <span class="ab-card__badge">{badge}</span>
        <img src="/assets/games/brand/{key}.png" alt="{alt}"{lazy} decoding="async">
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

        <p class="ab-ec-foot">{channels} &middot; Data updated <span class="js-prices-updated">{updated}</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>"""


def card_block_quote(key, q, first):
    """One quote card: no picker, no ladder, no prices.json row.

    The two classes that carry a price — --picker and --quote — never meet: a
    picker's block is one <select> filled from prices.json, and this one is a
    sentence that names what is sold. What they share is the rest of the card,
    so a quote card sits in the same grid without a hole where the control was.
    Buy keeps `ab-crisp-open` (the /topup/ cards' own handoff): there is no
    price to build a checkout sheet around, so the chat is the whole flow.
    """
    lazy = "" if first else ' loading="lazy"'
    # The footnote is optional: a quote card that has nothing to put under the
    # service line omits the element, rather than shipping an empty <p> that
    # --quote still lays out (CS2, 2026-10-29: the platform line was removed).
    foot = (f'\n\n        <p class="ab-ec-foot">{q["foot"]}</p>'
            if q.get("foot") else "")
    return f"""<article class="{QUOTE_CLASS}" id="{key}">
      <div class="ab-card__media">
        <span class="ab-card__badge">{q['badge']}</span>
        <img src="/assets/games/brand/{key}.png" alt="{q['alt']}"{lazy} decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">{q['name']}<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="{q['msg']}">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list">{q['line']}</p>{foot}
      </div>
</article>"""


def png_size(path):
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    return struct.unpack(">II", head[16:24])


def main():
    mg = load_games_table()
    text = open(PAGE, encoding="utf-8").read()
    prices = json.load(open(PRICES, encoding="utf-8"))
    updated = prices["updated"]

    # ---- existing cards, verbatim
    by_id = {}
    for m in re.finditer(r"<article\b[^>]*\bid=\"([^\"]+)\"[^>]*>.*?</article>",
                         text, re.S):
        by_id[m.group(1)] = m.group(0)

    # The five originals lead (PUBG Mobile first, it owns fetchpriority), then
    # the topuplist order, then the quote-only cards. KEEP is the same list
    # merge_game_prices leaves alone.
    quotes = {q["key"]: q for q in mg.QUOTE}
    order = list(mg.KEEP) + [g["key"] for g in mg.GAMES] + list(quotes)
    missing = [k for k in order if k not in by_id]
    print(f"existing cards: {len(by_id)}   to generate: {len(missing)}")

    blocks = []
    for i, key in enumerate(order):
        game = next((g for g in mg.GAMES if g["key"] == key), None)
        if key in quotes:
            # Always rebuilt from QUOTE: the table is this card's only writer,
            # so editing the copy there must not leave the page's copy behind.
            blocks.append(card_block_quote(key, quotes[key], first=(i == 0)))
        elif key in by_id:
            blocks.append(by_id[key])
        elif game:
            blocks.append(card_block(
                key, game["name"], game["badge"], game["channels"],
                f"{game['name']} top-up price reference",
                first=(i == 0), updated=updated))
        else:
            sys.exit(f"{key} is in KEEP but has no card on the page")

    stray = [k for k in by_id if k not in order]
    if stray:
        sys.exit(f"cards on the page but not in GAMES: {stray} — add them to "
                 f"the table or delete them first")

    # ---- checks
    ids = order
    if len(ids) != TOTAL:
        sys.exit(f"{len(ids)} cards, expected {TOTAL}")
    if len(set(ids)) != len(ids):
        sys.exit("duplicate key in the card order")
    for key in ids:
        if key in quotes:
            # No prices.json row by design — see merge_game_prices.QUOTE.
            p = os.path.join(BRANDS, key + ".png")
            if not os.path.exists(p):
                sys.exit(f"{key}: missing brand image {p}")
            if png_size(p) != (2400, 500):
                sys.exit(f"{key}: brand image is {png_size(p)}, expected (2400, 500)")
            continue
        if key not in prices["games"] or not prices["games"][key]:
            sys.exit(f"{key}: no rows in prices.json")
        if isinstance(prices["games"][key][0], dict) and \
                "lowest" not in prices["games"][key][0]:
            sys.exit(f"{key}: prices.json row is not the picker shape")
        p = os.path.join(BRANDS, key + ".png")
        if not os.path.exists(p):
            sys.exit(f"{key}: missing brand image {p}")
        size = png_size(p)
        if size != (2400, 500):
            sys.exit(f"{key}: brand image is {size}, expected (2400, 500)")
    joined = "\n".join(blocks)
    if joined.count("<article") != TOTAL or joined.count("</article>") != TOTAL:
        sys.exit(f"generated {joined.count('<article')} opening and "
                 f"{joined.count('</article>')} closing tags, expected {TOTAL}")

    # Only the opening line needs the container's 4-space indent: the rest of
    # each block already carries its own nesting, both for the cards copied out
    # of the page and for the generated ones.
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
        # start at the first card's line so its indentation survives
        line_start = text.rindex("\n", 0, first) + 1
        text = text[:line_start] + new_grid + text[last:]

    # ---- Product list
    names = []
    for block in blocks:
        m = re.search(r'<h3 class="ab-card__title">([^<]+)<span', block)
        if not m:
            sys.exit("cannot read a card title")
        # html.unescape: a card title may carry &amp;, which is markup in the
        # grid and should be a plain & in the Product list's JSON.
        names.append((re.search(r'\bid="([^"]+)"', block).group(1),
                      html.unescape(m.group(1)).strip()))

    items = ",\n".join(
        '        { "@type": "Product", "position": %d, "name": "%s", '
        '"url": "https://acebase.cc/games/#%s" }' % (i + 1, name, key)
        for i, (key, name) in enumerate(names))
    # No markers here: the Product list lives inside a <script type=
    # "application/ld+json"> block, and an HTML comment is not legal JSON —
    # a marker pair there made the whole graph unparseable. The array is
    # located by its own shape instead and rewritten in place.
    new_items = "\n" + items + "\n      "

    if ITEMS_START in text:          # a page built before the fix still has them
        a = text.index(ITEMS_START)
        b = text.index(ITEMS_END) + len(ITEMS_END)
        text = text[:a] + new_items + text[b:]
    else:
        # Search from the JSON-LD block, not from the top of the file. The
        # page's own Chinese comment *describes* this shape ("@type":
        # "ItemList" followed by "itemListElement": [ … ]), and on 2026-10-29
        # the unanchored search matched that prose first: it overwrote two
        # lines of the comment with the Product array and left the real list a
        # card short. The script block is the only place the shape is JSON.
        ld = text.index('<script type="application/ld+json">')
        a = text.index('"itemListElement": [', text.index('"@type": "ItemList"', ld))
        a = a + len('"itemListElement": [')
        b = text.index("]", a)
        text = text[:a] + new_items + text[b:]

    text = re.sub(r'"numberOfItems": "\d+"', '"numberOfItems": "%d"' % TOTAL, text)

    # ---- whole-file sanity before writing
    if text.count("<article") != text.count("</article>"):
        sys.exit("unbalanced <article> after render — gen_home.py counts these")

    open(PAGE, "w", encoding="utf-8", newline="\n").write(text)
    print(f"wrote {PAGE}: {TOTAL} cards, Product list 1..{TOTAL}")


if __name__ == "__main__":
    main()
