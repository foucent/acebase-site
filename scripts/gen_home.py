#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate docs/index.md — the uncrate-style magazine homepage.

The homepage is a curated front page, not an index: a handful of sections,
each a short selection rather than the full set. Everything numeric comes
from the same files the inner pages use, so the two can never drift:

    docs/assets/games/prices.json        game top-up tiers (USD)
    docs/assets/games/live-prices.json   live-streaming platform tiers (USD)
    docs/gift-cards/index.md             gift-card denominations (USD)
    docs/games/*.md frontmatter          card titles and excerpts

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
from datetime import datetime, timezone
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
    two flat scalar keys we need."""
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


def mtime(rel: str) -> str:
    ts = (DOCS / rel).stat().st_mtime
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%d")


def esc(text: str) -> str:
    return (text.replace("&", "&amp;").replace("<", "&lt;")
                .replace(">", "&gt;").replace('"', "&quot;"))


# ---------------------------------------------------------------- content

# GPU models, newest first. Drawn from docs/games/*.md so the excerpt matches
# the destination page word for word.
GPU_CARDS = [
    ("RTX 5060 Ti", "games/rtx-5060-ti.md", "/assets/games/rtx-5060-ti-card.jpg"),
    ("RTX 5060", "games/rtx-5060.md", "/assets/games/rtx-5060-card.jpg"),
    ("RTX 4090", "games/rtx-4090.md", "/assets/games/rtx-4090-card.jpg"),
    ("RTX 4080 Super", "games/rtx-4080-super.md", "/assets/games/rtx-4080-super-card.jpg"),
]

# The rest of the range, for the GEAR section. Split rather than repeated: the
# two sections lead to different pages (TECH to the price tables, GEAR to the
# component hub), and the same four cards twice on one screen reads as a bug.
# RTX 5050 is absent because it has no page of its own — it survives only as an
# inline card on gpu-prices — so there is nothing to link a card to.
GEAR_CARDS = [
    ("RTX 4070 Ti Super", "games/rtx-4070-ti-super.md", "/assets/games/rtx-4070-ti-super-card.jpg"),
    ("RTX 4080", "games/rtx-4080.md", "/assets/games/rtx-4080-card.jpg"),
    ("RTX 3060 Ti", "games/rtx-3060-ti.md", "/assets/games/rtx-3060-ti-card.jpg"),
    ("RTX 3060", "games/rtx-3060.md", "/assets/games/rtx-3060-card.jpg"),
]

# 模拟装置 has no stock yet, so its three announced directions are the cards —
# written from that page's own placeholder text rather than invented products.
SIM_CARDS = [
    ("模拟驾驶", "赛车方向盘、踏板、手刹与排挡等。"),
    ("飞行模拟", "飞行摇杆、节流阀、脚舵等。"),
    ("座舱与支架", "模拟座舱支架、显示器支架与震动反馈等周边。"),
]

# Games: image-led where an illustration exists, text-led where it does not.
# pubg-gcoin deliberately shares no illustration with pubg-mobile — a repeated
# picture reads as a mistake, so it takes the text treatment instead.
GAME_CARDS = [
    ("王者荣耀", "games/hok.md", "/assets/games/honor-of-kings.svg", "hok"),
    ("PUBG Mobile", "games/pubg-mobile.md", "/assets/games/pubg-mobile.svg", "pubg-mobile"),
    ("PUBG G-COIN", "games/pubg-gcoin.md", None, "pubg-gcoin"),
    ("暗区突围", "games/arena-breakout.md", None, "arena-breakout"),
    ("燕云十六声", "games/where-winds-meet.md", None, "where-winds-meet"),
]

LIVE_PICKS = [
    ("douyin-top-up", "抖音直播"),
    ("bigo-live", "Bigo Live"),
    ("kwi-top-up", "快手"),
    ("tango-live-recharge", "Tango Live"),
]

GIFT_PICKS = [
    "Amazon 礼品卡（美国）",
    "Apple 礼品卡",
    "Netflix 礼品卡（美国）",
    "PlayStation Network 充值卡（美国）",
    "Steam 钱包充值码（美国）",
    "Nintendo eShop 充值卡（美国）",
]

# Real captions lifted from docs/gallery/index.md. The image is the first frame
# of the set, the same one the wall tile shows; the card frame is 3:4 against a
# 0.56-ratio photo, so `object-fit: cover` crops it to the middle 75%.
GALLERY_PICKS = [
    ("穿搭写真", "/assets/gallery/wallpapers/style/style_01_01.jpg"),
    ("夜航星电竞", "/assets/gallery/wallpapers/nightvoyage/nightvoyage_01_01.jpg"),
    ("三角洲行动", "/assets/gallery/wallpapers/anime/anime_01_01.jpg"),
    ("中二病也要谈恋爱", "/assets/gallery/wallpapers/anime/anime_03_01.jpg"),
]


def parse_gift_cards() -> dict[str, dict]:
    """Pull image, denominations and headline price out of the gift-card page's
    generated markdown table."""
    text = (DOCS / "gift-cards" / "index.md").read_text(encoding="utf-8")
    row = re.compile(
        r'<img src="(?P<img>[^"]+)" alt="(?P<alt>[^"]+)"'
        r'(?P<rest>[^>]*)>\s*\|\s*(?P<name>[^|]+?)\s*\|\s*'
        r'<span class="ab-money" data-ab-amount="(?P<price>[\d.]+)"'
    )
    found: dict[str, dict] = {}
    for m in row.finditer(text):
        denoms = re.search(r'data-denoms="([^"]+)"', m.group("rest"))
        discount = re.search(r'data-discount="([^"]+)"', m.group("rest"))
        found[m.group("name").strip()] = {
            "img": m.group("img"),
            "alt": m.group("alt"),
            "price": float(m.group("price")),
            "denoms": [d.split(":")[0] for d in denoms.group(1).split(",")] if denoms else [],
            "discount": discount.group(1) if discount else "",
        }
    return found


# ---------------------------------------------------------------- markup

def card(title, href, cat, excerpt, img=None, meta="", more="阅读全文", media="") -> str:
    """`media` names the frame the image is drawn at — see the media-frames
    block in uncrate.css. It is the source's own ratio, not a house one:
    "photo" 4:3, "square" 1:1, "portrait" 3:4."""
    media_html = ""
    cls = "ab-card ab-card--text"
    if img:
        cls = f"ab-card ab-card--{media}" if media else "ab-card"
        media_html = (f'\n      <a class="ab-card__media" href="{href}" tabindex="-1" aria-hidden="true">'
                      f'\n        <img src="{img}" alt="" loading="lazy" decoding="async">'
                      f'\n      </a>')
    meta_html = f'\n        <p class="ab-card__meta">{meta}</p>' if meta else ""
    return f'''    <article class="{cls}">{media_html}
      <div class="ab-card__copy">
        <p class="ab-cat">{esc(cat)}</p>
        <h3 class="ab-card__title"><a href="{href}">{esc(title)}</a></h3>
        <p class="ab-card__excerpt">{esc(excerpt)}</p>{meta_html}
        <p class="ab-card__more"><a href="{href}">{more}</a></p>
      </div>
    </article>'''


def section(sec_id, title, stamp, cards, all_href=None, all_label=None,
            tail=None) -> str:
    """`tail` renders as its own grid under the first one.

    The grid stretches every card in a row to the tallest of them, which is
    what keeps a row of image cards even. It is the wrong thing when the row
    mixes treatments: a short text card beside a 3:4 portrait gets padded out
    to the portrait's height and reads as an empty box. A section whose two
    halves are different kinds of card therefore takes a second grid rather
    than a longer first one.
    """
    head_all = ""
    if all_href:
        head_all = (f'\n      <a class="ab-section__all" href="{all_href}">'
                    f'{esc(all_label)} &rarr;</a>')
    tail_html = ""
    if tail:
        tail_html = f'''
    <div class="ab-list">
{chr(10).join(tail)}
    </div>'''
    return f'''
  <section class="ab-section" id="{sec_id}">
    <header class="ab-section__head">
      <span class="ab-stamp" aria-hidden="true">更新于 {stamp}</span>
      <h2 class="ab-section__title">{esc(title)}</h2>{head_all}
    </header>
    <div class="ab-list">
{chr(10).join(cards)}
    </div>{tail_html}
  </section>'''


def build() -> str:
    prices = load_json("assets/games/prices.json")
    live = load_json("assets/games/live-prices.json")
    gifts = parse_gift_cards()

    sections = []

    # ---- 显卡价格参考 -------------------------------------------------
    gpu_cards = [
        card(name, "/" + rel.replace(".md", "/"), "TECH",
             excerpt_of(rel), img, media="photo")
        for name, rel, img in GPU_CARDS
    ]
    sections.append(section(
        "gpu", "TECH", "2026-09-09", gpu_cards,
        "/games/gpu-prices/", "全部 9 个型号"))

    # ---- GEAR ---------------------------------------------------------
    gear_cards = [
        card(name, "/" + rel.replace(".md", "/"), "GEAR",
             excerpt_of(rel), img, media="photo")
        for name, rel, img in GEAR_CARDS
    ]
    sections.append(section(
        "gear", "GEAR", mtime("pc-components/index.md"), gear_cards,
        "/pc-components/", "全部 9 个型号"))

    # ---- 代储价格参考 -------------------------------------------------
    game_cards = []
    for name, rel, img, key in GAME_CARDS:
        tiers = prices["games"].get(key, [])
        meta = ""
        if not img and tiers:
            lo = min(t.get("lowest", t.get("acebase", 0)) for t in tiers)
            meta = f"{money(lo)} 起 · {len(tiers)} 个档位"
        game_cards.append(card(name, "/" + rel.replace(".md", "/"),
                               "GAME", excerpt_of(rel), img, meta,
                               media="square"))
    sections.append(section(
        "topup", "GAME", prices["updated"], game_cards,
        "/games/topup-prices/", "全部 10 款游戏"))

    # ---- 直播代储价格参考 ---------------------------------------------
    live_cards = []
    for key, label in LIVE_PICKS:
        item = live["products"].get(key)
        if not item:
            continue
        tiers = item.get("tiers", [])
        lo = min(t["ref"] for t in tiers) if tiers else 0
        meta = f"{money(lo)} 起 · {len(tiers)} 个档位"
        # The note opens by naming the platform, which the title already says.
        note = re.sub(r"^[^，。]{1,24}?是", "", item.get("note", "")).strip()
        live_cards.append(card(label, "/games/live-prices/",
                               item.get("badge", "直播代储"), note,
                               None, meta, "查看档位"))
    sections.append(section(
        "live", "APP", live["updated"], live_cards,
        "/games/live-prices/", "全部 14 个平台"))

    # ---- STYLE --------------------------------------------------------
    # Text-led at the top: the section has no products to photograph yet.
    # The gallery picks ride at the end of it rather than in a section of
    # their own — both are the look-at-this half of the site, the half that
    # is not a price table. Each gallery card keeps its own 画廊 label and
    # its own link, so a reader can still tell which half they are in.
    # The stamp takes the newer of the two, so it tracks whichever moved.
    sim_cards = [
        card(title, "/sim-gear/", "STYLE", desc, None, "", "查看专区")
        for title, desc in SIM_CARDS
    ]
    gallery_cards = [
        card(caption, "/gallery/", "画廊", "出自 AceBase 图库，点开可看整套。", img,
             more="查看图集", media="portrait")
        for caption, img in GALLERY_PICKS
    ]
    sections.append(section(
        "style", "STYLE",
        max(mtime("sim-gear/index.md"), mtime("gallery/index.md")),
        sim_cards, "/sim-gear/", "专区主页", tail=gallery_cards))

    # ---- 礼品卡 -------------------------------------------------------
    gift_cards = []
    for name in GIFT_PICKS:
        g = gifts.get(name)
        if not g:
            continue
        denoms = g["denoms"]
        span = f"{denoms[0]} – {denoms[-1]}" if len(denoms) > 1 else (denoms[0] if denoms else "")
        meta = f"{money(g['price'])} 起 · 面额 {span}"
        if g["discount"]:
            meta += f" · <span class='ab-card__off'>{esc(g['discount'])}</span>"
        gift_cards.append(card(name, "/gift-cards/", "SHOP",
                               f"{len(denoms)} 种面额可选，卡密秒发。" if denoms else "卡密秒发。",
                               g["img"], meta, "查看面额", media="portrait"))
    sections.append(section(
        "gift-cards", "SHOP", mtime("gift-cards/index.md"), gift_cards,
        "/gift-cards/", "全部 14 款"))

    # ---- hero ---------------------------------------------------------
    hero = f'''  <article class="ab-hero">
    <div class="ab-hero__media">
      <a href="/games/gpu-prices/">
        <img src="/assets/games/rtx-5050-card.jpg" alt="显卡价格参考" fetchpriority="high" decoding="async">
      </a>
      <span class="ab-stamp ab-stamp--hero" aria-hidden="true">更新于 2026-09-09</span>
    </div>
    <div class="ab-hero__copy">
      <p class="ab-cat"><a href="/games/gpu-prices/">TECH</a></p>
      <h2 class="ab-hero__title"><a href="/games/gpu-prices/">9 款 RTX 显卡，全网均价一次看完</a></h2>
      <p class="ab-hero__excerpt">{esc(excerpt_of("games/gpu-prices.md"))}</p>
      <p class="ab-hero__more"><a href="/games/gpu-prices/">阅读全文</a></p>
    </div>
  </article>'''

    latest = max(prices["updated"], live["updated"])
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

{hero}
{''.join(sections)}

  <p class="ab-mag__foot">全部数据更新至 {latest} · 报价以在线咨询为准</p>

</div>
'''


if __name__ == "__main__":
    out = DOCS / "index.md"
    out.write_text(build(), encoding="utf-8")
    print(f"wrote {out} ({len(build().splitlines())} lines)")
