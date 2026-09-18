#!/usr/bin/env python3
"""One-off: re-lay-out the GPU pages in the article template.

docs/games/pubg-gcoin.md — an uncrate-style article: a band of artwork, then
left-aligned copy carrying the headline numbers, and nothing else — is the
house treatment for a single product's price page. The GPU pages predate it and
still use the card/table/chart template: gpu-prices stacks nine summary cards
with sparklines, and each of the eight rtx-*.md pages carries a hand-drawn
trend chart plus four volatility tiles.

This rewrites all nine into that article layout. Per model: the product art as
the band, then 当前市场均价 / 历史最低 / 近 30 天均价 / 近 30 天区间 as one line
each, the fetch date, and a consult link. The sparkline, the four volatility
tiles and the 走势点评 prose go away with the template that held them.

Two things it has to reconcile on the way:

1. The band artwork carried a printed price ("显卡价格监测 · 当前均价 $506") from
   the *old* dataset — the one the eight rtx-*.md pages and the art were
   generated together from, before the daily series in _tmp_ocr/gpu_trend/
   replaced it. The art was repriced here so the band and the rows under it
   could not show two prices for one card. That artwork has since been retired
   in favour of product photos (docs/assets/games/rtx-*.jpg), so step 1 below
   now rewrites nine files nothing links to; it stays as a record.

2. Every figure is read back out of the existing gpu-prices.md rather than
   recomputed, so the numbers a visitor already sees do not move — only the
   markup around them. Hence the script also owns the 8 rtx pages: they take
   the same figures from the same table, which is what retires the old dataset.

Run from the repo root:  python scripts/restyle_gpu_pages.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

OVERVIEW = DOCS / "games" / "gpu-prices.md"

# "显卡价格监测 · 当前均价 $506" — the second <text> of every product art SVG.
# Only the figure moves; the wording around it is left exactly as it was, so the
# art carries no edit of ours beyond the number it was wrong about.
ART_PRICE_RE = re.compile(r"(· 当前均价 )\$[0-9,]+")

CARD_RE = re.compile(
    r'<section class="mg-gpu-card" id="(?P<slug>[^"]+)">(?P<body>.*?)</section>',
    re.S,
)
TAGS_RE = re.compile(r'<li>([^<]+)</li>')
CHANGE_RE = re.compile(r'class="mg-gpu-card__stat__change[^"]*">([^<]+)<')
NOTE_RE = re.compile(
    r"当前均价 (?P<last>\$[\d,]+)，对比参考期内历史最低 (?P<low>\$[\d,]+)"
    r"（(?P<low_d>[\d-]+)）溢价约 (?P<prem>[\d.]+)%；近 30 天均价约 (?P<avg30>\$[\d,]+)，"
    r"价格区间 (?P<min30>\$[\d,]+) – (?P<max30>\$[\d,]+)。数据截至 (?P<date>[\d-]+)。"
)
RELATED_RE = re.compile(
    r'<div class="admonition note mg-games__note">\s*'
    r'<p class="admonition-title">相关</p>.*?</div>',
    re.S,
)


def parse_overview(text: str) -> list[dict]:
    """One dict per model, in page order — the only place these figures live."""
    models = []
    for m in CARD_RE.finditer(text):
        body = m.group("body")
        note = NOTE_RE.search(body)
        change = CHANGE_RE.search(body)
        if not (note and change):
            raise SystemExit(f"{m.group('slug')}: could not read the card note")
        models.append({
            "slug": m.group("slug"),
            "name": re.search(r"mg-gpu-card__model\">([^<]+)<", body).group(1),
            "tags": TAGS_RE.findall(body),
            "change": change.group(1).lstrip("▲▼― ").strip(),
            **note.groupdict(),
        })
    if not models:
        raise SystemExit("no .mg-gpu-card found — already restyled?")
    return models


def art_alt(m: dict) -> str:
    return f"{m['name']} 显卡价格参考"


def tidy_related(block: str) -> str:
    """Re-indent the carried-over 相关 admonition to one line per tag.

    Lifted verbatim out of the old page, where the opening and closing tags
    sit at column 0 and the two <p>s are indented under them.
    """
    lines = [ln.strip() for ln in block.strip().splitlines() if ln.strip()]
    out = [lines[0]] + [f"  {ln}" for ln in lines[1:-1]] + [lines[-1]]
    return "\n".join(out)


def excerpt(m: dict) -> str:
    """The one-line lead: what the card is, what it costs, where it is going.

    Built from the card's own tag chips — architecture, memory, segment — so
    the prose cannot drift from the specs printed beside it.
    """
    arch, mem, segment = m["tags"][0], m["tags"][1], m["tags"][-1]
    return f"{arch}、{mem} 的{segment}，现价 {m['last']}，{m['change']}。"


def rows(m: dict) -> str:
    """uncrate's Everyday Carry shape: 名称 / 值. — one line per figure."""
    items = [
        ("当前市场均价", m["last"]),
        (f"历史最低（{m['low_d']}）", m["low"]),
        ("近 30 天均价", m["avg30"]),
        ("近 30 天区间", f"{m['min30']} – {m['max30']}"),
    ]
    out = []
    for label, value in items:
        out.append(
            f'        <span class="ab-ec-item">{label}'
            f'<span class="ab-ec-sep">/</span>'
            f'<span class="ab-ec-price">{value}</span>.</span>'
        )
    return "<br>\n".join(out)


def article(m: dict, level: int, anchor: bool) -> str:
    tid = f' id="{m["slug"]}"' if anchor else ""
    return f'''  <article class="ab-hero ab-hero--article ab-hero--photo"{tid}>
    <div class="ab-hero__media">
      <img src="/assets/games/{m["slug"]}.jpg" alt="{art_alt(m)}" loading="lazy" decoding="async">
    </div>
    <div class="ab-hero__copy">
      <p class="ab-cat"><a href="/games/gpu-prices/">显卡价格参考</a></p>
      <h{level} class="ab-hero__title">{m["name"]}</h{level}>
      <p class="ab-hero__excerpt">{excerpt(m)}</p>

      <p class="ab-ec-list">
{rows(m)}
      </p>

      <p class="ab-ec-foot">数据更新于 {m["date"]} &middot; 报价以在线咨询为准</p>

      <p class="ab-hero__more">
        <a class="ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 {m["name"]} 的实时价格与装机搭配。">实时价格咨询</a>
      </p>
    </div>
  </article>'''


def build_overview(models: list[dict], related: str, date: str) -> str:
    name_list = "、".join(m["name"] for m in models)
    chips = "\n".join(
        f'    <a href="#{m["slug"]}">{m["name"]}</a>' for m in models
    )
    body = "\n\n".join(article(m, 2, True) for m in models)
    items = ",\n".join(
        f'        {{ "@type": "Product", "position": {i + 1}, '
        f'"name": "{m["name"]}" }}'
        for i, m in enumerate(models)
    )
    related = tidy_related(related)
    return f'''---
title: 显卡价格参考 | RTX 显卡行情总览
description: AceBase 显卡价格参考 —— 逐个型号列出 NVIDIA GeForce RTX 50/40/30 系共 {len(models)} 个型号的当前市场均价、历史最低与近 30 天区间（美元计价）。数据更新至 {date}。
hide:
  - title
  - toc
---

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <header class="ab-section__head">
      <span class="ab-stamp" aria-hidden="true">更新于 {date}</span>
      <h1 class="ab-section__title">显卡价格参考</h1>
    </header>
    <p class="ab-section__lead">覆盖 NVIDIA GeForce RTX 50/40/30 系共 {len(models)} 个型号 —— {name_list}，逐个列出当前市场均价、历史最低与近 30 天区间（美元计价，持续更新）。</p>
    <div class="mg-gpu-models" role="navigation" aria-label="已收录型号">
{chips}
    </div>
  </section>

{body}

</div>

{related}

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "WebPage",
      "name": "显卡价格参考",
      "description": "AceBase 显卡价格参考总览，覆盖 RTX 50/40/30 系 {len(models)} 个型号的当前市场均价、历史最低与近 30 天区间。数据更新至 {date}。",
      "url": "https://acebase.cc/games/gpu-prices/"
    }},
    {{
      "@type": "ItemList",
      "name": "显卡价格参考 · RTX 系列",
      "numberOfItems": "{len(models)}",
      "itemListElement": [
{items}
      ]
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "首页", "item": "https://acebase.cc/" }},
        {{ "@type": "ListItem", "position": 2, "name": "电脑组件", "item": "https://acebase.cc/pc-components/" }},
        {{ "@type": "ListItem", "position": 3, "name": "显卡价格参考", "item": "https://acebase.cc/games/gpu-prices/" }}
      ]
    }}
  ]
}}
</script>
'''


def build_model_page(old: str, m: dict, related: str) -> str:
    """A standalone model page: the same one-article body, its own head.

    The frontmatter description is rewritten because the homepage card for this
    page is generated from it (gen_home.excerpt_of), and the old one advertised
    a 深度解析 that no longer exists on the page.
    """
    head = re.match(r"^---\r?\n(.*?)\r?\n---", old, re.S).group(1)
    title = re.search(r"^title:\s*(.+)$", head, re.M).group(1).strip()
    desc = (f"{m['name']} 显卡价格参考 —— {'、'.join(m['tags'])}，现价 {m['last']}。"
            f"AceBase 汇总当前市场均价、历史最低与近 30 天区间（美元计价）。")
    related = tidy_related(related)
    return f'''---
title: {title}
description: {desc}
hide:
  - title
  - toc
---

<div class="ab-mag" markdown="0">

{article(m, 1, False)}

</div>

{related}
'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    text = OVERVIEW.read_text(encoding="utf-8")
    models = parse_overview(text)
    by_slug = {m["slug"]: m for m in models}
    related = RELATED_RE.search(text).group(0)
    date = models[0]["date"]
    assert len({m["date"] for m in models}) == 1, "cards disagree on the fetch date"

    writes: list[tuple[Path, str]] = []

    # 1. the nine product-art SVGs, repriced to the dataset the rows quote.
    for m in models:
        path = DOCS / "assets" / "games" / f"{m['slug']}.svg"
        svg = path.read_text(encoding="utf-8")
        old_price = ART_PRICE_RE.search(svg)
        if not old_price:
            print(f"  {m['slug']}: art has no printed price — left as-is")
            continue
        new_svg, n = ART_PRICE_RE.subn(rf"\g<1>{m['last']}", svg)
        if n != 1:
            raise SystemExit(f"{path}: matched {n} price nodes")
        writes.append((path, new_svg))

    # 2. the overview.
    writes.append((OVERVIEW, build_overview(models, related, date)))

    # 3. the eight standalone pages, minus rtx-5050 (it has no page of its own).
    for path in sorted(DOCS.glob("games/rtx-*.md")):
        m = by_slug.get(path.stem)
        if not m:
            print(f"  {path.name}: no card on gpu-prices — left as-is")
            continue
        old = path.read_text(encoding="utf-8")
        rel = RELATED_RE.search(old)
        if not rel:
            raise SystemExit(f"{path}: no 相关 block to carry over")
        writes.append((path, build_model_page(old, m, rel.group(0))))

    for path, content in writes:
        print(f"  {path.relative_to(ROOT)}")
        if not args.dry_run:
            path.write_text(content, encoding="utf-8")

    verb = "would write" if args.dry_run else "written"
    print(f"\n{len(writes)} file(s) {verb}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
