#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Import the eight 穿搭写真 sets from the download folder into the STYLE page.

The source is a folder of douyin stills (``~/Downloads/style``), one post per
download timestamp: 18 files, 8 sets. This script writes the web-sized copies
into ``docs/assets/gallery/wallpapers/style/`` and prints the ``<article>``
block for each set, ready to paste into ``docs/style/index.md``.

It prints the markup rather than writing the page because the STYLE page is
hand-written — only ``docs/index.md`` is generated, and that one stays the
generator's alone. The card body itself comes from ``ab_cards.card()``, the
same component every other card on the site is drawn with, so the two grids
cannot drift into looking like two different components. What this script adds is the
four attributes that turn the card into a lightbox opener (see the CARD_SEL
block in photo-wall.js).

The page holds cards this importer did not make — the six car cards, style-10,
and the two look cards the user rewrote by hand (style-02, style-03) — so
``--check`` compares the six it can still draw and lists the rest in
``NOT_MINE`` rather than calling them extra.

The set ORDER is authored, not derived. The download timestamps run out of
order (130700…130852), so sorting the folder cannot produce the reading order,
and the numbering decides both the filenames and the card order. The table
below is the only place that order exists. A file whose title is not in the
table fails the run and prints the titles actually found — inventing an order
silently is the one thing this script must never do.

The resize is reverse-engineered from ``style_01_*.jpg``, which was imported
before this script existed: 1440 wide, JPEG q82, progressive, 4:2:0. The
``round()`` is load-bearing — it is what makes 7008px land on 2559, the height
the shipped style_01 file has.

The originals are NOT copied into ``素材/``. That directory is gitignored —
"Source material, not site content, and this repo is public" — and the rule was
added by the very commit that imported style_01, so the previous import kept
its originals out too. 25.5MB is 1.7x all the gallery art on the site. The
manifest written here carries a sha1 per file instead, so the batch can be
identified without the bytes.

Run from the repo root:

    python scripts/import_style_sets.py            # write images + print markup
    python scripts/import_style_sets.py --dry-run  # print sizes and markup only
    python scripts/import_style_sets.py --check    # diff against the live page
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SRC = Path.home() / "Downloads" / "style"
OUT_DIR = DOCS / "assets" / "gallery" / "wallpapers" / "style"
PAGE = DOCS / "style" / "index.md"
MANIFEST = ROOT / "scripts" / "_style_sets_20260921.json"

sys.path.insert(0, str(ROOT / "scripts"))
from ab_cards import card, esc  # noqa: E402  the site's shared card builder

# The card body, the same one ab_cards.card() draws for every grid on the site.
# The label was 「画廊」 until 2026-09-23, when the page moved from /sim-gear/ to
# /style/ and every card on it — these eight, style-10, and the six car cards
# that used to read 「实拍」 — took the category's own name. uncrate.css
# uppercases it, so the source string and the rendered STYLE differ in case.
CAT = "STYLE"
EXCERPT = "点开可看整套。"
MORE = "查看图集"
MEDIA = "portrait"  # the 3:4 cover frame — the homepage's 穿搭写真 card uses it

MAX_W = 1440
QUALITY = 82
FIRST_SET = 2  # style_01 is already on /gallery/ as the 穿搭写真 tile

# Cards on the STYLE page this importer cannot reproduce, and so must not report
# as drift by --check. Three groups, for two different reasons:
#
#   car-01…06   the six car cards, merged into /style/ from the retired /car/
#               page on 2026-09-22. Not this importer's at all.
#   style-10    added by hand on 2026-09-23 (its three frames and its markup
#               come from _tmp_ocr/style10_prep/prep.py, outside this repo,
#               which prints the card by calling markup() below).
#   style-02    one of the eight, but the user replaced its copy on 2026-09-23 —
#               a look name, a sentence, then three pieces each with a price.
#               Later the same day it became a fold card like /topup/'s: the
#               sentence stays out, the three pieces sit behind a 展开 cue in an
#               .ab-ec-list grid, and the card carries --fold --ec --look. Later
#               still the sentence went, and the card was asked to stand level
#               with style-03: the window holds two rows and the third is behind
#               展开. Either shape is beyond card(), which escapes `excerpt` into
#               one run of text, so the card was hand-written instead. Its
#               pictures are still the set's.
#   style-03    the same treatment, same day, from the same page, then rewritten
#               three times that day: cut to two rows, then concealed behind a
#               fold (收起时两件都藏，点展开才出现), and finally simply shown — no
#               sentence, the two priced pieces sitting where a plain card keeps
#               its sentence, and .ab-card__more's 查看图集 at the end. It carries
#               no --fold at all; see the no-fold look card in uncrate.css for
#               why the fold lost. Hand-written for the same reason; its
#               pictures are still the set's.
#
# Without this list --check has been failing since the merge — it lists the car
# cards as 多余的卡片, and because the check stopped being able to pass, nobody
# read its output either way. It now watches the six cards it can still draw.
NOT_MINE = {
    "car-01", "car-02", "car-03", "car-04", "car-05", "car-06",
    "style-02",
    "style-03",
    "style-10",
}

# (title derived from the filename, title to show on the card).
# The order IS the style_NN numbering and the card order. One entry is
# hand-made: the post's own title is just "更新！", and the picture is a black
# dress with fishnet tights and patent heels, so the card takes its title from
# the post's hashtags instead.
SETS = [
    ("可爱蝴蝶结登场", "可爱蝴蝶结登场"),
    ("更新！", "高跟鞋 · 连裤袜"),
    ("来选一张最喜欢的吧！", "来选一张最喜欢的吧！"),
    ("水墨", "水墨"),
    ("祝你好运，要天天开心", "祝你好运，要天天开心"),
    ("紫裙摆", "紫裙摆"),
    ("薄雾余灰", "薄雾余灰"),
    ("蝉鸣不止的夏日总会结束", "蝉鸣不止的夏日总会结束"),
]

# 懒语本语-{title}。#tags-{YYYYMMDD_HHMMSS}_{n}.jpg — greedy head, so the match
# lands on the last stamp-shaped run before the index. The tag run is truncated
# by the downloader and ends in "...", which is why the head cannot be parsed
# further than the first "。".
STEM_RE = re.compile(r"^(?P<head>.+)-(?P<ts>\d{8}_\d{6})_(?P<n>\d+)\.jpg$")


def scan() -> dict[str, dict]:
    """Group the source folder by download timestamp — one stamp, one post."""
    if not SRC.is_dir():
        raise SystemExit(f"找不到素材目录：{SRC}")
    groups: dict[str, dict] = {}
    for p in sorted(SRC.glob("*.jpg")):
        m = STEM_RE.match(p.name)
        if not m:
            raise SystemExit(f"文件名不合格式：{p.name}")
        title = m.group("head").split("-", 1)[-1].split("。", 1)[0]
        g = groups.setdefault(m.group("ts"), {"title": title, "files": []})
        g["files"].append((int(m.group("n")), p))
    for g in groups.values():
        g["files"].sort()
    return groups


def order(groups: dict[str, dict]) -> list[dict]:
    """Line the groups up with SETS, or stop and say what was actually found."""
    found: dict[str, list] = {}
    for ts, g in groups.items():
        found.setdefault(g["title"], []).append((ts, g))

    if sorted(found) != sorted(t for t, _ in SETS):
        print("素材里读到的标题：", file=sys.stderr)
        for t in sorted(found):
            print(f"  {t!r} ×{len(found[t])}", file=sys.stderr)
        print(f"\n脚本 SETS 表里是：{[t for t, _ in SETS]}", file=sys.stderr)
        raise SystemExit("标题对不上，先更新 SETS 表再跑 —— 顺序不猜。")

    out = []
    for i, (want, card_title) in enumerate(SETS):
        hits = found[want]
        if len(hits) != 1:
            raise SystemExit(f"{want!r} 匹配到 {len(hits)} 组，时间戳撞了，人工看一下。")
        ts, g = hits[0]
        number = FIRST_SET + i
        urls = [
            f"/assets/gallery/wallpapers/style/style_{number:02d}_{n:02d}.jpg"
            for n, _ in g["files"]
        ]
        out.append({
            "slug": f"style-{number:02d}",
            "title": card_title,
            "src_title": want,
            "ts": ts,
            "files": g["files"],
            "urls": urls,
        })
    return out


def encode(setdef: dict, dry_run: bool) -> list[dict]:
    """Write the web-sized copies. Returns what was written, for the manifest."""
    written = []
    for (n, src), url in zip(setdef["files"], setdef["urls"]):
        dst = DOCS / url.lstrip("/")
        with Image.open(src) as im:
            im = im.convert("RGB")
            if im.width > MAX_W:
                im = im.resize(
                    (MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS
                )
            w, h = im.size
            if not dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                im.save(
                    dst,
                    "JPEG",
                    quality=QUALITY,
                    optimize=True,
                    progressive=True,
                    subsampling=2,
                )
        written.append({
            "n": n,
            "src": src.name,
            "sha1": hashlib.sha1(src.read_bytes()).hexdigest(),
            "out": url,
            "w": w,
            "h": h,
            "kb": round((dst.stat().st_size if not dry_run else 0) / 1024),
        })
    return written


def markup(setdef: dict, first: bool) -> str:
    """The card, built by the homepage's own card()."""
    body = card(
        setdef["title"], setdef["urls"][0], CAT, EXCERPT,
        setdef["urls"][0], more=MORE, media=MEDIA,
    )
    # The opener attributes. minify_html is off in mkdocs.yml precisely so the
    # &quot;-escaped JSON in data-gallery survives the build.
    gallery_json = json.dumps(setdef["urls"], ensure_ascii=False).replace('"', "&quot;")
    old = f'    <article class="ab-card ab-card--{MEDIA}">'
    new = (
        f'    <article class="ab-card ab-card--{MEDIA} ab-card--lightbox"'
        f' id="{setdef["slug"]}"'
        f' data-gallery="{gallery_json}"'
        f' data-caption="{esc(setdef["title"])}"'
        f' data-look="{setdef["slug"]}"'
        f' data-buy="#">'
    )
    assert old in body, "ab_cards.card() 的形状变了，注入点要重新锚定"
    body = body.replace(old, new, 1)
    if first:
        # The first card is above the fold on every width.
        body = body.replace('loading="lazy"', 'fetchpriority="high"', 1)
    return body


def page_articles() -> dict[str, str]:
    """The cards currently on the STYLE page, keyed by id."""
    text = PAGE.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(
        r'^    <article class="ab-card ab-card--portrait ab-card--lightbox".*?^    </article>$',
        text,
        re.S | re.M,
    ):
        block = m.group(0)
        out[re.search(r'id="([^"]+)"', block).group(1)] = block
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只打印，不落盘")
    ap.add_argument("--check", action="store_true",
                    help="和页面里现有的卡片逐字对比，有差非零退出")
    args = ap.parse_args()

    setdefs = order(scan())
    blocks = []
    manifest = []
    total_kb = 0

    for i, setdef in enumerate(setdefs):
        written = encode(setdef, args.dry_run or args.check)
        manifest.append({
            "folder": f"style_{FIRST_SET + i:02d}",
            "key": f"懒语本语-{setdef['src_title']}-{setdef['ts']}",
            "title": setdef["title"],
            "count": len(written),
            "urls": setdef["urls"],
            "src": [
                {k: w[k] for k in ("n", "src", "sha1", "w", "h")} for w in written
            ],
        })
        for w in written:
            total_kb += w["kb"]
        print(
            f"{setdef['slug']}  {setdef['title']:<12} "
            f"{len(written)} 张  "
            + "  ".join(f"{w['w']}x{w['h']}/{w['kb']}KB" for w in written)
        )
        blocks.append(markup(setdef, first=(i == 0)))

    print()

    stale = sorted({s["slug"] for s in setdefs} & NOT_MINE)

    if args.check:
        live = page_articles()
        drift = [k for k in live if k not in {s["slug"] for s in setdefs}
                 and k not in NOT_MINE]
        for setdef, block in zip(setdefs, blocks):
            if setdef["slug"] in NOT_MINE:
                continue
            if live.get(setdef["slug"]) != block:
                raise SystemExit(f"{setdef['slug']} 和页面上的不一样，跑一次不带参数的。")
        if drift:
            raise SystemExit(f"页面上有多余的卡片：{drift}")
        print(f"脚本管的 {len(setdefs) - len(stale)} 张卡与页面上的逐字一致"
              f"（另有 {len(NOT_MINE)} 张不归它管，见 NOT_MINE）。")
        return

    if not args.dry_run:
        MANIFEST.write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(f"写入 {MANIFEST.relative_to(ROOT)}（{total_kb / 1024:.1f}MB 出图）")
        print()

    if stale:
        print(f"  ! {'、'.join(stale)} 的文案改过（见 NOT_MINE）—— 下面打印的这几张"
              f"还是旧的，别拿它们覆盖页面。")
        print()
    print('在 <div class="ab-list"> 里按顺序粘贴：')
    print()
    print("\n\n".join(blocks))


if __name__ == "__main__":
    main()
