#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate docs/index.md — the front page, assembled entirely from other pages.

The homepage has no content of its own. The rule is one line: **every card on
the front page is the newest six cards of a category, copied out of that
category's page.**

`Category` means the top-level nav in mkdocs.yml — TOP-UP, GAME, GIFT CARDS,
BOOSTING, BLOG —
read from that file rather than listed here, so a category added to the nav
reaches the front page with no edit to this script. A category whose page holds
no cards contributes nothing; "如果有的话" is the whole of that rule, and
the run summary prints a 0 so a category cannot quietly stop contributing.

The cards are copied, not re-drawn. This script used to rebuild each one from a
per-category pool of its own — its own title, its own excerpt, its own picture,
its own price — which meant every card existed twice and the two copies could
drift. Now the `<article>` block is lifted whole out of the page it lives on,
attributes and all, so the front page can only ever show what the category page
shows; the lightbox, the fold and the price ladder keep working because the
markup that drives them came along. Two things are touched on the way: the
indentation is normalised to the front page's depth, and the source page's own
first-image priority is taken off (the front page promotes its own first card).

Two pages may carry the same card now — since 2026-10-21 /gift-cards/ holds a
copy of /topup/'s six gift cards. The front page is one document: a repeated id
would give it two elements with that id and leave the second card's price
picker empty, because games-prices.js fills the first `[data-game]` it finds.
So cards are deduped by article id, and a repeated card belongs to the category
that holds fewer cards — the more dedicated page — with nav order breaking a
tie; the other page moves on to its next card, and the run prints what it
skipped. Nav order alone decided this until 2026-10-21, when TOP-UP was moved
ahead of GIFT CARDS: TOP-UP's thirteen cards would have claimed all six gift
cards and GIFT CARDS would have put nothing on the front page.

`Newest` is a section head's own 更新于 date, not the page's. A page can hold
more than one section and they do not have to be in date order, so the section a
card sits in is what dates it; within one date the page's own order stands, so
the six taken are the six written first. No page on the site has more than one
section today — /topup/ had three and /tech/ two until 2026-09-22 merged each
into a single grid — but the loop still reads sections, because that is how a
page that grows a second one gets dated.

The frontmatter's `updated:` is the fallback for a section that carries no
stamp, and since 2026-09-22 that is every page with cards on it: /topup/,
/tech/ (today /figures/) and /style/ (today /gift-cards/) all lost their
section heads that day.
It is not a
substitute for a stamp: a page that has cards and no date at all is named on
stderr rather than dated by guesswork, because an invented date would reorder
the whole front page.

Run from the repo root:  python scripts/gen_home.py
"""
from __future__ import annotations

import re
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from ab_cards import esc, frontmatter  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
MKDOCS = ROOT / "mkdocs.yml"

# How many cards one category may put on the front page.
CATEGORY_LIMIT = 6

# ...except where a category says otherwise. BLOG has held one card since
# 2026-10-22: /blog/ became a list of nine news rows that day, and a row is a
# wide, tall block — six of them would bury the front page under one category,
# while one is the "latest story" slot the old single card filled. The page
# itself caps nothing; only this front-page slice does.
CATEGORY_LIMIT_BY_LABEL = {"BLOG": 1}


# ---------------------------------------------------------------- sources

def nav_categories() -> list[tuple[str, str]]:
    """[(label, page)] from mkdocs.yml's nav, in nav order.

    A line-based reader rather than PyYAML, the same trade frontmatter() makes:
    the nav here is flat, one `- LABEL: path` per line, and pulling in a parser
    for six lines is not worth a dependency.

    Three things it has to get right. The label may carry a hyphen (TOP-UP) **or
    a space** (Gift Cards, added 2026-09-24) — the pattern was `[\\w-]+` until
    that day, and a label with a space in it simply did not match: the category
    dropped off the homepage with no error anywhere, which is the one failure
    mode here that nothing else would catch. So the label is now everything up
    to the colon. The comments interleaved between the entries sit at exactly
    the entries' own indent, so they have to be skipped by name rather than by
    shape. And the block has to be bounded: `extra.family` and `extra.channels`
    are also `- key: value` lists, and `extra:` comes *before* `nav:` in the
    file, so a scan that is not anchored to the two-space indent and closed at
    the next top-level key finds those first.
    """
    lines = MKDOCS.read_text(encoding="utf-8").splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.rstrip() == "nav:")
    except StopIteration:
        sys.exit("mkdocs.yml 里找不到顶格的 `nav:`")
    out: list[tuple[str, str]] = []
    for line in lines[start + 1:]:
        if line.strip() and not line[:1].isspace():
            break                                   # the next top-level key
        entry = re.match(r"^  - ([^:]+?):\s*(\S+)\s*$", line)
        if entry:
            out.append((entry.group(1).strip(), entry.group(2)))
    if not out:
        sys.exit("mkdocs.yml 的 nav 里一条都没解析出来")
    return out


# A section head's date, in both spellings the site has used:
#   更新于 2026-09-22                              (/style's head, until
#                                                    2026-09-22)
#   更新于 <span class="js-prices-updated">…</span>  (/topup's, rewritten in the
#                                                    browser from prices.json)
# No page has a head stamp today — every page that carries cards lost its head
# on 2026-09-22 — so the whole front page is dated by frontmatter. This stays
# for the page that grows a head back.
STAMP = re.compile(r"(?:数据)?更新于\s*(?:<span[^>]*>)?\s*(\d{4}-\d{2}-\d{2})|Data updated\s*(?:<span[^>]*>)?\s*(\d{4}-\d{2}-\d{2})")
# …and it has to be found inside a head. Every card also carries a
# `数据更新于 2026-09-21` footer of its own, so an unscoped search over the
# section would take the first card's footer for the section's date: /topup/ has
# no head since 2026-09-22 and would be dated by whichever price card happens to
# be written first — a card's own date moving would reorder the front page.
# (/tech/ — today /figures/ — has no head either but no footers to trip over
# since its price cards came out on 2026-09-22.) A section with no head has no stamp, and falls back
# as below.
HEAD = re.compile(r'<header class="ab-section__head">(.*?)</header>', re.S)
# A lookahead, so finditer reports where each section starts rather than
# consuming the tag: those offsets are what cards_of() indexes the file with.
SECTION = re.compile(r'(?=<section class="ab-section")')
ARTICLE = re.compile(r"<article\b[^>]*>.*?</article>", re.S)
CLASS = re.compile(r'<article\b[^>]*\bclass="([^"]*)"')
# The same card can sit on two pages — /gift-cards/ since 2026-10-21 carries a
# copy of /topup/'s six, by design. The front page is one document, so an id may
# appear only once: a second copy would repeat the id and, worse, leave its
# price picker empty (games-prices.js fills the first `[data-game]` it finds).
# Dedupe by article id; the category with fewer cards keeps it (see build()).
CARD_ID = re.compile(r'<article\b[^>]*\bid="([^"]*)"')


def page_updated(rel: str) -> str | None:
    """A page's `updated:` frontmatter, or None when it has none."""
    date = frontmatter(rel).get("updated", "").strip()
    return date if re.fullmatch(r"\d{4}-\d{2}-\d{2}", date) else None


def cards_of(rel: str) -> list[tuple[str, str, str]]:
    """[(section date, source indent, article html)] — newest section first.

    A card is an `<article>` whose class list holds `ab-card` — there is exactly
    one `<article>` on the site that is not a card, the hero band on
    games/gpu-deals.md, and it is excluded by that test rather than by the page
    it sits on.

    `<article>` open and close counts are compared before anything is taken.
    The extraction is a lazy regex, and a page that lost a closing tag would
    silently swallow the rest of itself into one card; the count turns that into
    a named failure at the top of the run instead of a strange-looking page.
    """
    path = DOCS / rel
    if not path.exists():
        sys.exit(f"mkdocs.yml 的 nav 指向 {rel}，但 docs/ 里没有这个文件")
    text = path.read_text(encoding="utf-8")
    opens, closes = text.count("<article"), text.count("</article>")
    if opens != closes:
        sys.exit(f"{rel}: <article> 开闭不配平（{opens} / {closes}）")

    stamp = page_updated(rel)
    out: list[tuple[str, str, str]] = []
    undated = 0
    # The sections as (start, end) spans of the whole file. Splitting the text
    # instead would hand back chunks whose offsets no longer point into it, and
    # lead_of() indexes the file — one card per section would silently take its
    # neighbour's indent.
    bounds = [0] + [m.start() for m in SECTION.finditer(text)] + [len(text)]
    for start, end in zip(bounds, bounds[1:]):
        chunk = text[start:end]
        head = HEAD.search(chunk)
        date = STAMP.search(head.group(1)) if head else None
        date = (date.group(1) or date.group(2)) if date else stamp
        for art in ARTICLE.finditer(chunk):
            cls = CLASS.match(art.group(0))
            if not cls or "ab-card" not in cls.group(1).split():
                continue
            if date:
                out.append((date, lead_of(text, start + art.start()),
                            art.group(0)))
            else:
                undated += 1
    if undated:
        print(f"  ! {rel}: {undated} 张卡片所在的那一段没有「更新于 …」，页面 "
              f"frontmatter 也没有可用的 updated: —— 这几张不上首页",
              file=sys.stderr)
    # Stable, so cards sharing a section date keep the page's own order — which
    # is the only order a one-section page like /gift-cards/ has.
    out.sort(key=lambda t: t[0], reverse=True)
    return out


def lead_of(text: str, at: int) -> str:
    """The whitespace the source page indents its card with."""
    return text[text.rfind("\n", 0, at) + 1:at]


def verbatim(html: str, lead: str) -> str:
    """The source card, re-indented to the front page's depth.

    The regex match starts at `<article`, so the first line arrives without the
    source's indent while every line under it still carries one. The first line
    goes back onto that baseline, the block is dedented by it and re-indented to
    the front page's four — which is a no-op today, every card on the site being
    written at four already. It is done this way round so a card copied out of a
    deeper page stays put instead of drifting four spaces per nesting level.

    The only other change: the source page's own first card carries
    `fetchpriority="high"`, and six of those on one page is six images claiming
    the first screen. They come off here and the front page puts one back on its
    own first card — see promote().
    """
    lines = html.replace(' fetchpriority="high"', "").split("\n")
    lines[0] = lead + lines[0]
    return textwrap.indent(textwrap.dedent("\n".join(lines)), "    ")


def promote(html: str) -> str:
    """Give one card's first image the first-screen priority."""
    img = re.search(r"<img\b[^>]*>", html)
    if not img:
        print("  ! 首页第一张卡片没有 <img>，没有东西可提升", file=sys.stderr)
        return html
    tag = img.group(0)
    if "fetchpriority" in tag:
        return html
    tag = (tag[:-2] + ' fetchpriority="high"/>' if tag.endswith("/>")
           else tag[:-1] + ' fetchpriority="high">')
    return html[:img.start()] + tag + html[img.end():]


# ---------------------------------------------------------------- markup

def section(sec_id, title, stamp, cards) -> str:
    """One grid of cards under one head.

    The list carries `ab-list--feed`: the feed mixes text-only cards with three
    different image ratios, and the grid stretches every card in a row to the
    tallest of them, which would pad a short card out to the height of the 3:4
    portrait beside it. See the rule in uncrate.css.
    """
    return f'''
  <section class="ab-section" id="{sec_id}">
    <header class="ab-section__head">
      <span class="ab-stamp" aria-hidden="true">Updated {stamp}</span>
      <h2 class="ab-section__title">{esc(title)}</h2>
    </header>
    <div class="ab-list ab-list--feed">
{chr(10).join(cards)}
    </div>
  </section>'''


def card_key(html: str) -> str:
    """The card's article id, or the whole block when it has none."""
    m = CARD_ID.search(html)
    return m.group(1) if m else html


def build() -> str:
    items: list[tuple[str, int, int, str]] = []
    counts: list[tuple[str, int]] = []
    dupes: list[tuple[str, str, str]] = []      # (giver, key, keeper)

    cats = []
    for order, (label, rel) in enumerate(nav_categories()):
        if rel == "index.md":
            continue            # the front page is not one of its own sources
        cats.append((order, label, cards_of(rel)))

    # Which category shows a repeated card: the one holding the fewest cards —
    # the page the card belongs to — with nav order breaking a tie. Plain nav
    # order was the rule until 2026-10-21; reordering TOP-UP ahead of GIFT
    # CARDS would then have handed it /gift-cards/'s own six copies.
    owner: dict[str, tuple[int, int, str]] = {}
    for order, label, cards in cats:
        for _date, _lead, html in cards:
            key = card_key(html)
            held = owner.get(key)
            if held is None or len(cards) < held[0]:
                owner[key] = (len(cards), order, label)

    for order, label, cards in cats:
        limit = CATEGORY_LIMIT_BY_LABEL.get(label, CATEGORY_LIMIT)
        pool = []
        for date, lead, html in cards:
            key = card_key(html)
            if owner[key][1] != order:
                dupes.append((label, key, owner[key][2]))
                continue
            pool.append((date, lead, html))
            if len(pool) == limit:
                break
        counts.append((label, len(pool)))
        for position, (date, lead, html) in enumerate(pool):
            items.append((date, order, position, verbatim(html, lead)))
    if dupes:
        gave: dict[tuple[str, str], list[str]] = {}
        for giver, key, keeper in dupes:
            gave.setdefault((giver, keeper), []).append(key)
        print("  · 重复卡归卡片更少的类目：" + "；".join(
            f"{giver} 让出 {len(keys)} 张给 {keeper}（{'、'.join(keys)}）"
            for (giver, keeper), keys in gave.items()))

    # Two stable passes rather than one compound key: a key that mixes a
    # descending date with ascending tie-breakers is a key nobody can read, and
    # `reverse=True` on the compound one would reverse the tie-breakers too.
    items.sort(key=lambda t: (t[1], t[2]))          # nav order, then page order
    items.sort(key=lambda t: t[0], reverse=True)    # newest first

    cards = [html for _date, _order, _pos, html in items]
    if cards:
        cards[0] = promote(cards[0])

    stamp = max((date for date, _o, _p, _h in items), default="")
    print(f"  {len(cards)} cards: "
          + "、".join(f"{label} {n}" for label, n in counts))

    return f'''---
title: AceBase — Game Top-Up, Gift Cards & GPU Prices
description: AceBase tracks game top-ups, live-stream credit, digital gift cards and RTX GPU prices, comparing every tier on one page.
icon: material/home
hide:
  - navigation
  - title
  - toc
---

<div class="ab-mag" markdown="0">
{section("latest", "Latest updates", stamp, cards)}

  <p class="ab-mag__foot">All data updated {stamp} · Final quote confirmed in chat</p>

</div>
'''


if __name__ == "__main__":
    body = build()          # built whole before anything is written, so a run
    out = DOCS / "index.md"  # that fails leaves the previous page standing
    out.write_text(body, encoding="utf-8")
    print(f"wrote {out} ({len(body.splitlines())} lines)")
