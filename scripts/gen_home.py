#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate docs/index.md — the front page, assembled entirely from other pages.

The homepage has no content of its own. Every card is a product that already
exists on one of the category pages; nothing here is hand-picked, so there is
nothing here to update when a price moves — update the category page and the
front page follows. The only editorial decision left is the date each page
carries, which decides the order.

The date is authored, not derived, and lives in the page's frontmatter as
`updated:`. File mtime was the obvious alternative and is the wrong one: a
fresh `git clone` stamps every file with the checkout time, so the front page
would reorder itself on a machine it was never edited on, and a stylesheet
tweak would push unrelated pages to the top. A page missing the key is skipped
loudly rather than silently — see page_date().

Every category is capped at CATEGORY_LIMIT entries. Fourteen live-streaming
platforms or thirteen gift cards all carry one date, because that is how they
are updated, so without a cap whichever category was touched last would take
the whole page. Within a category the newest go first; between categories the
order is purely by date.

Everything numeric comes from the same files the inner pages use, so the two
can never drift:

    docs/assets/games/prices.json        every /topup tier: games, cards,
                                         live platforms (USD)
    docs/topup/index.md                  the kickers, pictures and sentences
    docs/gallery/index.md                gallery set captions and covers
    docs/games/*.md frontmatter          card titles, excerpts, dates

Prices are emitted as .ab-money spans. Every price on the site is USD — that is
the base currency the data files are stored in and the only one displayed — so
the span is markup, not a conversion hook. The GPU pages quote their figures as
static text, so their cards carry prose only rather than a price that would
drift out of step with the page it links to.

Run from the repo root:  python scripts/gen_home.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"


# ---------------------------------------------------------------- helpers

def load_json(rel: str):
    with (DOCS / rel).open(encoding="utf-8") as fh:
        return json.load(fh)


def money(amount: float) -> str:
    """A .ab-money span — data attributes for scripts, `$` text for readers."""
    shown = f"${amount:,.2f}"
    return (f'<span class="ab-money" data-ab-amount="{amount}" '
            f'data-ab-base="USD">{shown}</span>')


def frontmatter(rel: str) -> dict:
    """Minimal YAML frontmatter reader — avoids a PyYAML dependency for the
    three flat scalar keys we need."""
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


def page_date(rel: str) -> str | None:
    """A page's `updated:` frontmatter, or None if it has none.

    None takes every card on that page off the homepage. That is deliberate —
    a page with no date has no defensible place in a list sorted by date, and
    pretending otherwise (today's date, mtime, a neighbour's date) would put an
    invented figure on the front page. But it must not be quiet: a page that
    silently stopped appearing on the homepage is a page nobody would notice
    had gone, so it says so on stderr and the build carries on.
    """
    date = frontmatter(rel).get("updated", "").strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        print(f"  ! {rel}: no usable `updated:` in the frontmatter — its "
              f"products are off the homepage", file=sys.stderr)
        return None
    return date


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


# ---------------------------------------------------------------- content

# GPU models, newest first — empty since the eight RTX 40/30 系 and 5060/5060 Ti
# pages were retired. A card here is a link to a model's own page, and the only
# model still on the site is RTX 5050, which has never had one: it survives as a
# card on /tech with no destination. So TECH is now the deals band alone, and
# the list stays as the place a future model page would be declared.
GPU_CARDS: list[tuple[str, str, str]] = []

# Games: image-led where an illustration exists, text-led where it does not.
# pubg-gcoin deliberately shares no illustration with pubg-mobile — a repeated
# picture reads as a mistake, so it takes the text treatment instead.
#
# (title, key, illustration) — the key is the name the tier data is filed under
# in prices.json and the id of that game's card on /topup, which is where the
# card now sends a reader: the five game pages were retired on 2026-09-21 and
# their price block is part of the /topup card. The titles here stay the
# homepage's own — it names the two Chinese games in Chinese where /topup names
# them in English. The sentence under each title is read off /topup instead of
# kept here, so there is one copy of it.
GAME_CARDS = [
    ("王者荣耀", "hok", "/assets/games/honor-of-kings.svg"),
    ("PUBG Mobile", "pubg-mobile", "/assets/games/pubg-mobile.svg"),
    ("PUBG G-COIN", "pubg-gcoin", None),
    ("暗区突围", "arena-breakout", None),
    ("燕云十六声", "where-winds-meet", None),
]

# The one-page deal band. It is a single SKU rather than a model range, so its
# title and photo are read off the page — the page already names the exact card
# and its price, and a copy of that name here would be a second place to keep
# in step.
DEAL_PAGE = "games/gpu-deals.md"

# Where a GPU card sends a reader who wants to buy one. Amazon's front page,
# not a listing for the card: AceBase quotes what a model costs, it does not
# stock one, so the honest destination is the marketplace itself. The link is
# outbound and opens in a new tab; the card's own title still goes to the model
# page, so the reader keeps both routes.
AMAZON_HOME = "https://www.amazon.com/"

# The card kickers, in the order the feed falls back to when two categories
# share a date. TECH leads because it holds the page's own product photos.
GROUP_ORDER = ["TECH", "直播代储", "TOP-UP", "STYLE", "SHOP"]

# How many entries one category may put on the front page. The homepage itself
# is not capped — see the module docstring.
CATEGORY_LIMIT = 10


def parse_shop_cards() -> list[dict]:
    """Every SHOP card on /topup, in page order.

    The thirteen gift cards and cdkeys moved off /gift-cards/ onto /topup/ on
    2026-09-21, and the markdown table this used to read went with that page.
    It reads the cards themselves now.

    Split on `<article ` and parse one block at a time: a single regex with a
    lazy tail matches straight across two cards the moment one of them is
    missing an element, and a picture quietly taken from the card below it is
    not something a printed line count would show. A block that is missing what
    is needed is named on stderr rather than counted and dropped.

    The kicker does the selecting — `ab-cat` SHOP, the same bare string
    GROUP_ORDER holds — so a fourteenth card added to /topup reaches the front
    page with no edit here and there is no key list to fall out of step. It is
    also why that kicker has to stay plain text: anything else inside it, a pill
    or an image, would fail the comparison and take all thirteen off the page.
    """
    text = (DOCS / "topup" / "index.md").read_text(encoding="utf-8")
    found: list[dict] = []
    for block in text.split("<article ")[1:]:
        cat = re.search(r'<p class="ab-cat">(.*?)</p>', block, re.S)
        if not cat or cat.group(1).strip() != "SHOP":
            continue
        cid = re.search(r'id="([^"]+)"', block)
        title = re.search(r'<h3 class="ab-card__title">(.*?)</h3>', block, re.S)
        art = re.search(r'data-art="([^"]+)"', block)
        if not (cid and title and art):
            print("  ! a SHOP card on /topup is missing id, <h3> or data-art: "
                  + repr(re.sub(r"\s+", " ", block[:80])), file=sys.stderr)
            continue
        off = re.search(r'data-discount="([^"]+)"', block)
        found.append({
            "id": cid.group(1),
            "name": re.sub(r"<[^>]+>", "", title.group(1)).strip(),
            "art": art.group(1),
            "off": off.group(1) if off else "",
        })
    return found


def parse_live_cards() -> list[dict]:
    """Every card in /topup's third section, in page order.

    The fourteen live-streaming platforms moved off /games/live-prices/ onto
    /topup/ on 2026-09-21, and the data file this used to read went with that
    page. It reads the cards themselves now, the way the gift cards above them
    are read.

    Selected by section, not by kicker: the other two sections carry the site's
    own names (TOP-UP, SHOP) but these cards keep their platform's category —
    直播, 语音, 陪玩社交, 休闲游戏 — which is the only thing on the front page
    that tells a reader what kind of product a card is. A named section is also
    the sturdier boundary; the kickers here are six different strings and are
    meant to stay that way.
    """
    text = (DOCS / "topup" / "index.md").read_text(encoding="utf-8")
    start = text.index('<section class="ab-section" id="live">')
    section = text[start:text.index("</section>", start)]
    found: list[dict] = []
    for block in section.split("<article ")[1:]:
        cid = re.search(r'id="([^"]+)"', block)
        title = re.search(r'<h3 class="ab-card__title">(.*?)</h3>', block, re.S)
        cat = re.search(r'<p class="ab-cat">(.*?)</p>', block, re.S)
        lead = re.search(r'<span class="ab-fold__lead">(.*?)</span>', block, re.S)
        if not (cid and title and cat and lead):
            print("  ! a live card on /topup is missing id, <h3>, ab-cat or the "
                  "fold lead: " + repr(re.sub(r"\s+", " ", block[:80])),
                  file=sys.stderr)
            continue
        found.append({
            "id": cid.group(1),
            "name": re.sub(r"<[^>]+>", "", title.group(1)).strip(),
            "cat": cat.group(1).strip(),
            "lead": lead.group(1).strip(),
        })
    return found


def parse_deal_cards() -> list[tuple[str, str]]:
    """(title, image) for each band on the deals page, in page order."""
    text = (DOCS / DEAL_PAGE).read_text(encoding="utf-8")
    band = re.compile(
        r'<article class="ab-hero ab-hero--article[^"]*">\s*'
        r'<div class="ab-hero__media">\s*<img src="(?P<img>[^"]+)"[^>]*>.*?'
        r'<h2 class="ab-hero__title">(?P<title>.*?)</h2>', re.S)
    return [(re.sub(r"<[^>]+>", "", m.group("title")).strip(), m.group("img"))
            for m in band.finditer(text)]


def topup_blurbs() -> dict[str, str]:
    """game key -> the one-sentence description on that game's /topup card.

    The five game pages that used to be excerpted here are gone, and the
    description they carried is now the opening sentence of the /topup card —
    same words, so this reads them rather than keeping a second copy that could
    drift. Keyed off the card's own id, which is the prices.json key.
    """
    text = (DOCS / "topup" / "index.md").read_text(encoding="utf-8")
    card_re = re.compile(
        r'<article class="ab-card[^"]*" id="(?P<id>[^"]+)">.*?'
        r'<span class="ab-fold__lead">(?P<lead>.*?)</span>', re.S)
    return {m.group("id"): m.group("lead").strip() for m in card_re.finditer(text)}


def parse_gallery_sets() -> list[tuple[str, str]]:
    """(caption, cover) for every wall tile that carries one, in wall order.

    The tiles whose alt is empty are the figure-photo sets. The gallery page has
    no name for them, and inventing one here would put a title on the homepage
    that the page it links to does not use — so they stay off the front page and
    STYLE never fills its ten.
    """
    text = (DOCS / "gallery" / "index.md").read_text(encoding="utf-8")
    tile = re.compile(
        r'<a class="sc-wall__tile[^"]*" href="[^"]+"[^>]*>'
        r'<img src="(?P<img>[^"]+)" alt="(?P<alt>[^"]*)"')
    return [(m.group("alt").strip(), m.group("img"))
            for m in tile.finditer(text) if m.group("alt").strip()]


# ---------------------------------------------------------------- markup

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

    `more=None` drops the link row altogether. The TOP-UP cards use it: they
    send a reader to the anchoring card on /topup, which is also where the title
    and the picture already point, so a third route to the same anchor would be
    a row that only repeats what the card has just said."""
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


def section(sec_id, title, stamp, cards) -> str:
    """One grid of cards under one head.

    The list carries `ab-list--feed`: the feed mixes text-only cards with three
    different image ratios, and the grid stretches every card in a row to the
    tallest of them, which would pad a two-line live-platform card out to the
    height of the 3:4 portrait beside it. See the rule in uncrate.css.
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
    prices = load_json("assets/games/prices.json")

    pools: dict[str, list[tuple[str, str]]] = {}

    # ---- TECH：显卡型号 + 好价 ------------------------------------------
    # GPU_CARDS 现在是空的（型号页已下线），这一段只剩显卡好价。循环留着不删，
    # 是为了哪天再加型号页时不必把它重写一遍。
    # 卡片按钮行和 /tech 上那张显卡卡一样，是一行两个链接：阅读全文 或 去亚马逊
    # 购买。/tech 那张的第一个链接是「展开」（页面上确实有个折叠档位表），这里
    # 没有折叠，第一个链接就落在卡片自己要通向的页面上 —— 标题和图之外再给一个
    # 入口，和 uncrate 的 Read More 一个道理。
    tech: list[tuple[str, str]] = []
    for name, rel, img in GPU_CARDS:
        date = page_date(rel)
        if date:
            tech.append((date, card(
                name, "/" + rel.replace(".md", "/"), "TECH", excerpt_of(rel),
                img, media="photo", more="阅读全文",
                more_or=("去亚马逊购买", AMAZON_HOME))))
    deal_date = page_date(DEAL_PAGE)
    if deal_date:
        for title, img in parse_deal_cards():
            tech.append((deal_date, card(
                title, "/" + DEAL_PAGE.replace(".md", "/"), "TECH",
                excerpt_of(DEAL_PAGE), img, media="photo", more="阅读全文",
                more_or=("去亚马逊购买", AMAZON_HOME))))
    pools["TECH"] = tech

    # /topup 的日期先算出来：这一页 2026-09-21 起装着三段商品 —— 5 款游戏、
    # 13 张礼品卡与卡密、14 个直播平台 —— 三段同一天更新，页面也只有一个
    # updated。三段的卡片日期都取这一个值。
    topup_date = page_date("topup/index.md")

    # ---- 直播代储：/topup 第三段的 14 个平台 ----------------------------
    # 这一组在导航里没有自己的一格，卡片挂在 TECH 下面，但配额是独立的一份 ——
    # 14 个平台同一天更新，和显卡好价共用一个 10 条的上限会把好价挤掉。
    #
    # 这十张是纯文字卡：/games/live-prices/ 那张老页给每张卡配过一条 24:5 的
    # 品牌横带，首页从来没用过它，搬进 /topup 之后也不用 —— 卡片自己的媒体框
    # 已经在用那张图了，首页再放一次就是同一页上两张一样的图。
    if topup_date:
        pool = []
        for g in parse_live_cards():
            tiers = prices["games"].get(g["id"], [])
            if not tiers:
                print(f"  ! {g['id']} 不在 prices.json 里 —— "
                      f"先跑 scripts/merge_live_prices.py", file=sys.stderr)
                continue
            lo = min(t["lowest"] for t in tiers)
            pool.append((topup_date, card(
                g["name"], f"/topup/#{g['id']}", g["cat"], g["lead"],
                None, f"{money(lo)} 起 · {len(tiers)} 个档位", "查看档位")))
        pools["直播代储"] = pool

    # ---- TOP-UP：全部 5 款游戏 -----------------------------------------
    # href 是 /topup 上那张卡的锚点，不是另一个页面 —— 详情页 2026-09-21 下线后
    # 卡片就是终点。既然标题和图已经把读者送过去了，卡片不再带 footer 链接：
    # /topup 自己的卡上那个「查看档位」同一批去掉，首页这张是同一张卡。
    if topup_date:
        blurbs = topup_blurbs()
        pool = []
        for name, key, art in GAME_CARDS:
            tiers = prices["games"].get(key, [])
            meta = ""
            if tiers:
                lo = min(t.get("lowest", t.get("acebase", 0)) for t in tiers)
                meta = f"{money(lo)} 起 · {len(tiers)} 个档位"
            pool.append((topup_date, card(
                name, f"/topup/#{key}", "TOP-UP", blurbs.get(key, ""),
                art, meta, more=None, media="square")))
        pools["TOP-UP"] = pool

    # ---- STYLE：图库里有标题的图集 -------------------------------------
    gallery_date = page_date("gallery/index.md")
    if gallery_date:
        pools["STYLE"] = [(gallery_date, card(
            caption, "/gallery/", "画廊", "点开可看整套。",
            img, more="查看图集", media="portrait"))
            for caption, img in parse_gallery_sets()]

    # ---- SHOP：/topup 第二段的 13 张礼品卡与卡密 -------------------------
    # /gift-cards/ 2026-09-21 整页下线，商品按 /topup 的卡片模板重排，成了那一页的
    # 第二段。所以这里既没有第二个页面也没有第二份价格：面额和价都从 /topup 的卡和
    # 它读的那份 prices.json 来，卡上的 data-art 是首页唯一还需要的 3:4 配图
    # ——/topup 自己用的是 24:5 品牌条，两者不同图。
    #
    # 日期跟着 /topup 走：两段同一天更新，页面也没有第二个 updated。首页那 10 条
    # 上限之内，第 10 张因此从「PUBG G-COIN 卡密」换成了 Nintendo Switch Online。
    shop_date = topup_date
    if shop_date:
        pool = []
        for g in parse_shop_cards():
            tiers = prices["games"].get(g["id"], [])
            if not tiers:
                print(f"  ! {g['id']} 不在 prices.json 里 —— "
                      f"先跑 scripts/merge_giftcard_prices.py", file=sys.stderr)
                continue
            lo = min(t["lowest"] for t in tiers)
            span = (f"{tiers[0]['title']} – {tiers[-1]['title']}"
                    if len(tiers) > 1 else tiers[0]["title"])
            meta = f"{money(lo)} 起 · 面额 {span}"
            if g["off"]:
                meta += f" · <span class='ab-card__off'>{esc(g['off'])}</span>"
            pool.append((shop_date, card(
                g["name"], f"/topup/#{g['id']}", "SHOP",
                f"{len(tiers)} 种面额可选，卡密秒发。",
                g["art"], meta, "查看面额", media="portrait")))
        pools["SHOP"] = pool

    # ---- 排序 ----------------------------------------------------------
    # Per category: newest first, then capped. Across categories: by date, and
    # for a date two categories share, by GROUP_ORDER. Two stable passes rather
    # than one compound key, because a sort key that mixes a descending date
    # with ascending tie-breakers is a key nobody can read.
    items: list[tuple[str, str, int, str]] = []
    for group in GROUP_ORDER:
        pool = sorted(pools.get(group, []), key=lambda t: t[0], reverse=True)
        for order, (date, html) in enumerate(pool[:CATEGORY_LIMIT]):
            items.append((date, group, order, html))
    items.sort(key=lambda t: (GROUP_ORDER.index(t[1]), t[2]))
    items.sort(key=lambda t: t[0], reverse=True)

    cards = [html for _date, _group, _order, html in items]
    stamp = max((date for date, _g, _o, _h in items), default="")
    print(f"  {len(cards)} cards: " + "、".join(
        f"{g} {sum(1 for i in items if i[1] == g)}" for g in GROUP_ORDER
        if any(i[1] == g for i in items)))

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
    out = DOCS / "index.md"
    body = build()
    out.write_text(body, encoding="utf-8")
    print(f"wrote {out} ({len(body.splitlines())} lines)")
