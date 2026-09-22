#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The AceBase card component and the page frontmatter reader behind it.

These lived in gen_home.py while the homepage drew its own cards from them.
It does not any more — it copies whole `<article>` blocks out of the category
pages (see gen_home.py) — so the component moved here, where the scripts that
still build cards can reach it without importing a generator they have nothing
to do with:

    import_style_sets.py   card, esc            还在跑：/sim-gear/ 的八张卡
    tech_card_grid.py      AMAZON_HOME, esc, excerpt_of
    card_action_line.py    AMAZON_HOME

The two behind still name gen_home in their docstrings; that was true when they
were written and they are histories of a past edit rather than tools to re-run.
What matters here is that the function they call produces the same markup it
did then: the card body is one component, and a card on /sim-gear/ that came out
of `card()` has to keep looking like every other card on the site.

What did NOT come along is `money()`. Its only callers were the homepage's own
five pools, and those are gone; a `.ab-money` span on the site now comes from
prices.json through games-prices.js, not from a Python format string.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# Where a card sends a reader who wants to buy the thing. Amazon's front page,
# not a listing: AceBase quotes what a model costs, it does not stock one, so
# the honest destination is the marketplace itself. The link is outbound and
# opens in a new tab; the card's own title still goes to the model page, so the
# reader keeps both routes.
AMAZON_HOME = "https://www.amazon.com/"


def frontmatter(rel: str) -> dict:
    """Minimal YAML frontmatter reader — avoids a PyYAML dependency for the
    three flat scalar keys the site's scripts need."""
    text = (DOCS / rel).read_text(encoding="utf-8")
    m = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return {}
    out: dict[str, str] = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^(\w+):\s*(.*)$", line)
        if km:
            out[km.group(1)] = km.group(2).strip().strip('"').strip("'")
    return out


def excerpt_of(rel: str, fallback: str = "") -> str:
    """The descriptive half of a page's SEO description.

    Those descriptions are written as "标题 —— 正文。理由。" with the marketing
    tail attached, so take what follows the dash and drop the trailing
    boilerplate sentence. Falls back to the whole string when there is no dash.
    """
    desc = frontmatter(rel).get("description", "").strip()
    if not desc:
        return fallback
    body = re.split(r"—{2,}", desc)[-1].strip()
    body = re.sub(r"[，,（(]\s*(美元计价|港币计价|持续更新)\s*[)）]?", "", body)
    body = re.sub(r"数据更新至\s*\d{4}-\d{2}-\d{2}。?", "", body)
    body = re.sub(r"AceBase.*$", "", body).strip()
    if body and body[-1] not in "。！？.!?":
        body += "。"
    return body or desc


def esc(text: str) -> str:
    return (text.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;").replace('"', "&quot;"))


def card(title, href, cat, excerpt, img=None, meta="", more="阅读全文", media="",
         more_href=None, more_or=None) -> str:
    """`media` names the frame the image is drawn at — see the media-frames
    block in uncrate.css. It is the source's own ratio, not a house one:
    "photo" 4:3, "square" 1:1, "portrait" 3:4.

    `more_href` points the CTA somewhere other than the card itself: the GPU
    cards offer to buy, so their link leaves the site while the title and the
    image stay on it. An absolute href opens in a new tab; nothing else about
    the card changes.

    `more_or` is a (label, url) pair that turns the CTA into the two-link action
    line — 阅读全文 或 去亚马逊购买 — the same one /tech puts under each of its
    cards, so the two grids read as one component. The first link keeps the
    card's own destination; the pair is the second.

    `more=None` drops the link row altogether. The TOP-UP cards used it: they
    sent a reader to the anchoring card on /topup, which is also where the title
    and the picture already pointed, so a third route to the same anchor would
    be a row that only repeats what the card has just said."""
    media_html = ""
    cls = "ab-card ab-card--text"
    if img:
        cls = f"ab-card ab-card--{media}" if media else "ab-card"
        media_html = (f'\n      <a class="ab-card__media" href="{href}" tabindex="-1" aria-hidden="true">'
                      f'\n        <img src="{img}" alt="" loading="lazy" decoding="async">'
                      f'\n      </a>')
    meta_html = f'\n        <p class="ab-card__meta">{meta}</p>' if meta else ""

    def link(label, url, indent):
        blank = ' target="_blank" rel="noopener"' if url.startswith("http") else ""
        return f'{indent}<a href="{url}"{blank}>{label}</a>'

    more_url = more_href or href
    if more is None:
        more_html = ""
    elif more_or:
        label2, url2 = more_or
        more_html = (
            '\n        <p class="ab-card__more ab-card__more--split">\n'
            + link(more, more_url, " " * 10) + "\n"
            + f'{" " * 10}<em class="ab-card__or">或</em>\n'
            + link(label2, url2, " " * 10) + "\n"
            + "        </p>")
    else:
        blank = ' target="_blank" rel="noopener"' if more_url.startswith("http") else ""
        more_html = f'\n        <p class="ab-card__more"><a href="{more_url}"{blank}>{more}</a></p>'
    return f'''    <article class="{cls}">{media_html}
      <div class="ab-card__copy">
        <p class="ab-cat">{esc(cat)}</p>
        <h3 class="ab-card__title"><a href="{href}">{esc(title)}</a></h3>
        <p class="ab-card__excerpt">{esc(excerpt)}</p>{meta_html}{more_html}
      </div>
    </article>'''
