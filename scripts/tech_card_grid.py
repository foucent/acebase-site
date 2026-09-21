#!/usr/bin/env python3
"""One-off: move the GPU overview to /tech and re-lay it out as a card grid.

The page used to be nine full-width bands, one model per row. It is now the
same two-column card grid the homepage's TECH section uses — photograph, the
TECH label, the model name, one line of prose, and a 去亚马逊购买 link — so a
reader who arrives from the homepage finds the same cards at the top of the
section they clicked through to.

What moves and what does not:

  * The figures do not move. Each card's four price rows are lifted verbatim
    out of the band that used to hold them, markup and all.
  * The visible line on each card is the model page's own frontmatter
    description, read through gen_home.excerpt_of — the same function that
    writes the homepage card. One model therefore reads identically in both
    places; a card whose line came from anywhere else would say one thing on
    the homepage and another here.
  * RTX 5050 has no page of its own (games/rtx-5050.md is a retired URL, it
    redirects here), so it has no frontmatter to read and no page to link to.
    Its card keeps the band's own lead sentence and carries no link on the
    title or the photograph; the Amazon link is still the action.

The four rows go behind the same <details> fold the bands used, for the same
reason: the card is a listing entry, the figures are what you open it for.

The card's CTA is not the band's. uncrate closes a listing entry with "Read More
or Buy from X" on one line, and the card does the same: the cue and the buy link
share an .ab-fold__act row. The buy link sits inside the summary with the cue so
the two can share a line at all — see scripts/card_action_line.py, which is
where that markup was actually introduced and where the reasoning lives.

Run from the repo root:  python scripts/tech_card_grid.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SRC = DOCS / "games" / "gpu-prices.md"
DST = DOCS / "tech" / "index.md"

sys.path.insert(0, str(ROOT / "scripts"))
from gen_home import AMAZON_HOME, esc, excerpt_of  # noqa: E402

# A band, whole. Anchored on the id and on the closing </article> so nothing
# inside can end the match early.
BAND_RE = re.compile(
    r'  <article class="ab-hero ab-hero--article ab-hero--photo" id="(?P<slug>[^"]+)">\n'
    r'    <div class="ab-hero__media">\n'
    r'      <img src="(?P<img>[^"]+)"[^>]*>\n'
    r'    </div>\n'
    r'    <div class="ab-hero__copy">\n'
    r'      <p class="ab-cat">.*?</p>\n'
    r'      <h2 class="ab-hero__title">(?P<name>[^<]+)</h2>\n'
    r'(?P<body>.*?)\n'
    r'  </article>\n',
    re.S,
)
LEAD_RE = re.compile(r'<span class="ab-fold__lead">(?P<lead>.*?)</span>')
LIST_RE = re.compile(r'[ ]*<p class="ab-ec-list">\n(?P<rows>.*?)\n[ ]*</p>', re.S)
FOOT_RE = re.compile(r'[ ]*<p class="ab-ec-foot">(?P<foot>.*?)</p>')
HEAD_RE = re.compile(r'  <section class="ab-section">\n(?P<head>.*?)\n  </section>\n', re.S)

EXPECTED = 9


def read_bands(text: str) -> list[dict]:
    models = []
    for m in BAND_RE.finditer(text):
        body = m.group("body")
        lead, rows, foot = LEAD_RE.search(body), LIST_RE.search(body), FOOT_RE.search(body)
        if not (lead and rows and foot):
            raise SystemExit(f"{m.group('slug')}: could not read the band")
        slug = m.group("slug")
        page = DOCS / "games" / f"{slug}.md"
        models.append({
            "slug": slug,
            "name": m.group("name"),
            "img": m.group("img"),
            "rows": rows.group("rows"),
            "foot": foot.group("foot").strip(),
            # No page means no frontmatter to read and nowhere to link.
            "line": excerpt_of(f"games/{slug}.md", lead.group("lead")) if page.exists() else lead.group("lead"),
            "href": f"/games/{slug}/" if page.exists() else "",
        })
    if len(models) != EXPECTED:
        raise SystemExit(f"read {len(models)} bands, expected {EXPECTED}")
    return models


def card(m: dict) -> str:
    """One grid entry. The shape is the homepage's `card()` output; the fold is
    the band's own, kept so the figures are still one click away rather than
    gone."""
    if m["href"]:
        media = (f'      <a class="ab-card__media" href="{m["href"]}" tabindex="-1" aria-hidden="true">\n'
                 f'        <img src="{m["img"]}" alt="" loading="lazy" decoding="async">\n'
                 f'      </a>')
        title = f'<a href="{m["href"]}">{esc(m["name"])}</a>'
    else:
        media = (f'      <div class="ab-card__media">\n'
                 f'        <img src="{m["img"]}" alt="{esc(m["name"])} 显卡价格参考" loading="lazy" decoding="async">\n'
                 f'      </div>')
        title = esc(m["name"])
    return f'''    <article class="ab-card ab-card--photo" id="{m["slug"]}">
{media}
      <div class="ab-card__copy">
        <p class="ab-cat">TECH</p>
        <h3 class="ab-card__title">{title}</h3>
        <details class="ab-fold">
          <summary class="ab-fold__summary">
            <span class="ab-fold__lead">{m["line"]}</span>
            <span class="ab-fold__act">
              <span class="ab-fold__cue"><span class="ab-fold__cue-more">展开</span><span class="ab-fold__cue-less">收起</span></span>
              <em class="ab-fold__or">或</em>
              <a class="ab-fold__buy" href="{AMAZON_HOME}" target="_blank" rel="noopener">去亚马逊购买</a>
            </span>
          </summary>

        <p class="ab-ec-list">
{m["rows"]}
        </p>

        <p class="ab-ec-foot">{m["foot"]}</p>
        </details>
      </div>
    </article>'''


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not SRC.exists():
        raise SystemExit(f"{SRC} is gone — already moved?")
    text = SRC.read_text(encoding="utf-8")
    if DST.exists():
        raise SystemExit(f"{DST} already exists")

    models = read_bands(text)

    head = HEAD_RE.search(text)
    if not head:
        raise SystemExit("could not read the section head")
    # The head's copy is carried over as-is; only the URLs inside it move.
    carried = head.group("head")
    body_start = head.end()

    rest = text[body_start:]
    # Everything from the 相关 admonition on — the related links and the JSON-LD.
    # The `</div>` that closed .ab-mag sits just above it and is re-emitted below.
    tail = rest[rest.index('<div class="admonition'):]

    out = (
        text[:head.start()]
        + '  <section class="ab-section">\n' + carried + '\n\n'
        + '    <div class="ab-list ab-list--expandable">\n'
        + "\n".join(card(m) for m in models)
        + '\n    </div>\n  </section>\n\n</div>\n\n'
        + tail
    ).replace("/games/gpu-prices/", "/tech/")

    # The old path must not survive anywhere on the page — a card, the JSON-LD
    # url, the breadcrumb. A stale one would send a reader to a 404 the moment
    # the redirect is retired.
    if "/games/gpu-prices/" in out:
        raise SystemExit("an unrewritten /games/gpu-prices/ link survived")
    if out.count('class="ab-card ab-card--photo"') != EXPECTED:
        raise SystemExit("card count is wrong")

    if not args.dry_run:
        DST.parent.mkdir(parents=True, exist_ok=True)
        DST.write_text(out, encoding="utf-8")
        SRC.unlink()
    print(f"{'would write' if args.dry_run else 'wrote'} {DST} ({len(out.splitlines())} lines), "
          f"removed {SRC.name}")
    for m in models:
        print(f"  {m['name']:18s} {'linked' if m['href'] else 'no page':8s} {m['line'][:34]}")


if __name__ == "__main__":
    main()
