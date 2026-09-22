#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate docs/index.md — the front page, assembled entirely from other pages.

The homepage has no content of its own. The rule is one line: **every card on
the front page is the newest six cards of a category, copied out of that
category's page.**

`Category` means the top-level nav in mkdocs.yml — TECH, TOP-UP, STYLE, FAQ —
read from that file rather than listed here, so a category added to the nav
reaches the front page with no edit to this script. A category whose page holds
no cards (FAQ) contributes nothing; "如果有的话" is the whole of that rule, and
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

`Newest` is a section's own 更新于 date, not the page's. A page can hold more
than one section and they do not have to be in date order — /tech puts its
prices (09-21) above its photo sets (09-22) — so the section a card sits in is
what dates it. Within one date the page's own order stands. The consequence
worth knowing: a page whose cards all share one date, which is every page but
/tech, is ordered by position alone, so the six taken are the six written first.

The frontmatter's `updated:` is the fallback for a section that carries no
stamp. It is not a substitute for one: a page that has cards and no date at all
is named on stderr rather than dated by guesswork, because an invented date
would reorder the whole front page.

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


# ---------------------------------------------------------------- sources

def nav_categories() -> list[tuple[str, str]]:
    """[(label, page)] from mkdocs.yml's nav, in nav order.

    A line-based reader rather than PyYAML, the same trade frontmatter() makes:
    the nav here is flat, one `- LABEL: path` per line, and pulling in a parser
    for six lines is not worth a dependency.

    Three things it has to get right. The label may carry a hyphen (TOP-UP), so
    `\\w+` will not do. The comments interleaved between the entries sit at
    exactly the entries' own indent, so they have to be skipped by name rather
    than by shape. And the block has to be bounded: `extra.family` and
    `extra.channels` are also `- key: value` lists, and `extra:` comes *before*
    `nav:` in the file, so a scan that is not anchored to the two-space indent
    and closed at the next top-level key finds those first.
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
        entry = re.match(r"^  - ([\w-]+):\s*(\S+)\s*$", line)
        if entry:
            out.append((entry.group(1), entry.group(2)))
    if not out:
        sys.exit("mkdocs.yml 的 nav 里一条都没解析出来")
    return out


# A section head's date, in both spellings the site uses:
#   更新于 2026-09-22                              (/tech, /sim-gear)
#   更新于 <span class="js-prices-updated">…</span>  (/topup — rewritten in the
#                                                    browser from prices.json)
STAMP = re.compile(r"更新于\s*(?:<span[^>]*>)?\s*(\d{4}-\d{2}-\d{2})")
# A lookahead, so finditer reports where each section starts rather than
# consuming the tag: those offsets are what cards_of() indexes the file with.
SECTION = re.compile(r'(?=<section class="ab-section")')
ARTICLE = re.compile(r"<article\b[^>]*>.*?</article>", re.S)
CLASS = re.compile(r'<article\b[^>]*\bclass="([^"]*)"')


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
        date = STAMP.search(chunk)
        date = date.group(1) if date else stamp
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
    # is the only order a one-section page like /sim-gear/ has.
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
      <span class="ab-stamp" aria-hidden="true">更新于 {stamp}</span>
      <h2 class="ab-section__title">{esc(title)}</h2>
    </header>
    <div class="ab-list ab-list--feed">
{chr(10).join(cards)}
    </div>
  </section>'''


def build() -> str:
    items: list[tuple[str, int, int, str]] = []
    counts: list[tuple[str, int]] = []

    for order, (label, rel) in enumerate(nav_categories()):
        if rel == "index.md":
            continue            # the front page is not one of its own sources
        pool = cards_of(rel)[:CATEGORY_LIMIT]
        counts.append((label, len(pool)))
        for position, (date, lead, html) in enumerate(pool):
            items.append((date, order, position, verbatim(html, lead)))

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
title: AceBase — 游戏代储、礼品卡与显卡价格参考
description: AceBase 汇集游戏代储、直播平台充值、电子礼品卡与 RTX 显卡价格参考，逐档对比并在同一页呈现最新行情。
icon: material/home
hide:
  - navigation
  - title
  - toc
---

<div class="ab-mag" markdown="0">
{section("latest", "最近更新", stamp, cards)}

  <p class="ab-mag__foot">全部数据更新至 {stamp} · 报价以在线咨询为准</p>

</div>
'''


if __name__ == "__main__":
    body = build()          # built whole before anything is written, so a run
    out = DOCS / "index.md"  # that fails leaves the previous page standing
    out.write_text(body, encoding="utf-8")
    print(f"wrote {out} ({len(body.splitlines())} lines)")
