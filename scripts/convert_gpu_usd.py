#!/usr/bin/env python3
"""One-off: convert the GPU pages from pegged HK$ figures to USD.

The eight docs/games/rtx-*.md pages quote prices in Hong Kong dollars at a
hardcoded peg of 7.839076 HKD/USD (the original generator, _tmp_ocr/
gen_gpu_pages.py, carries `RATE = 7.839076`). USD is the base currency
everywhere else on the site, so these pages were the only place a visitor saw a
currency they never asked for.

Two jobs:

1. Every ``HK$N`` becomes ``$round(N / RATE)``.

2. The inline trend chart is re-axed. Its five gridlines sit at fixed y
   positions, so rounding the tick *labels* without redrawing the polyline
   would mislabel the data by up to half a tick. Instead the six plotted
   values are recovered from the existing geometry, converted, and redrawn
   against an axis whose ticks are whole dollars.

   The two points that carry a visible label (历史底价 and 现价) take their
   value from the label rather than from the geometry, because rtx-5060's
   最低 label and its own plotted point disagree — the geometry says 2460, the
   label says 2630, and the sparkline agrees with 2460, so the label was
   hand-edited at some point without regenerating the chart. Trusting the
   label keeps every price a visitor could already read unchanged.

Run from the repo root:  python scripts/convert_gpu_usd.py [--dry-run]
"""
from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

# The peg every figure on these pages was generated with.
RATE = 7.839076

# Chart geometry, identical in all eight pages.
GRID_YS = [20, 55, 90, 125, 160]
TOP_Y, BOT_Y = GRID_YS[0], GRID_YS[-1]
X_POINTS = [45, 175, 305, 435, 520, 570]
# The two labelled points. Each label's offset from its dot is read back off
# the page being converted, since the pages do not agree on it.
LOW_LABEL_X, CUR_LABEL_X = 45, 565

# "Nice" axis steps in dollars, mirroring the HKD list in gen_gpu_pages.py.
USD_STEPS = [10, 15, 20, 25, 50, 75, 100, 150, 200, 250, 500, 1000, 2000, 5000]

MONEY_RE = re.compile(r"HK\$([0-9][0-9,]*)")
LINE_D_RE = re.compile(r'<path d="M 45,(\d+)((?: L \d+,\d+){5})"')
TICK_RE = re.compile(r'<text x="38" y="(\d+)">HK\$([0-9][0-9,]*)</text>')
LOW_RE = re.compile(r'<text x="45" y="(\d+)"([^>]*)>HK\$([0-9][0-9,]*) \(最低\)</text>')
CUR_RE = re.compile(r'<text x="565" y="(\d+)"([^>]*)>HK\$([0-9][0-9,]*) \(现价\)</text>')
AREA_D_RE = re.compile(r'<path d="M 45,\d+(?: L \d+,\d+){5} L 570,160 L 45,160 Z"')


def money(n: float) -> str:
    return "$" + format(int(round(n)), ",")


def to_usd(hkd: float) -> float:
    return hkd / RATE


def pick_axis(vmin: float, vmax: float):
    """Five gridlines, whole-dollar ticks, both ends bracketing the data.

    Same shape as gen_gpu_pages.pick_axis, but it guarantees ticks[-1] equals
    the axis maximum — the original could return a top tick below its own
    yMax, which would leave the highest gridline labelled with the wrong
    value.
    """
    span = vmax - vmin
    pad = max(span * 0.12, 10)
    lo, hi = vmin - pad, vmax + pad
    for step in USD_STEPS:
        if (hi - lo) / 4 > step:
            continue
        ymin = int(math.floor(lo / step)) * step
        ymax = ymin + 4 * step
        if ymax >= hi:
            return ymin, ymax, [ymin + i * step for i in range(5)]
    raise ValueError(f"no USD step brackets [{lo:.2f}, {hi:.2f}]")


def reaxis_chart(text: str, slug: str, report: list) -> str:
    """Recover the plotted series, convert it, redraw against a USD axis.

    The value scale comes from the two labelled points alone — their printed
    price and their printed y — rather than from the tick labels. Those labels
    cannot be trusted: on the six pages other than rtx-5060 / rtx-5060-ti they
    are written top-to-bottom in *ascending* order (so a page whose 现价 sits
    high on the chart is labelled with a low value at the top), and on no page
    do the labels, the polyline and the two printed prices agree under any one
    linear map. Anchoring on the two prices keeps every visible number exactly
    as it was and rebuilds the axis around them.
    """
    m = LINE_D_RE.search(text)
    tick_matches = TICK_RE.findall(text)
    low_m = LOW_RE.search(text)
    cur_m = CUR_RE.search(text)
    if not (m and len(tick_matches) == 5 and low_m and cur_m):
        report.append(f"  {slug}: chart not matched — left as-is")
        return text

    ys = [int(m.group(1))] + [int(v) for v in re.findall(r"L \d+,(\d+)", m.group(2))]
    low_hkd = float(low_m.group(3).replace(",", ""))
    cur_hkd = float(cur_m.group(3).replace(",", ""))
    if ys[0] == ys[-1]:
        report.append(f"  {slug}: both labelled points share a y — skipped")
        return text

    # value(y) = a + b*y, pinned to the two labelled points.
    b = (cur_hkd - low_hkd) / (ys[-1] - ys[0])
    a = low_hkd - b * ys[0]
    if b >= 0:
        report.append(f"  {slug}: chart is drawn value-up-side-down — skipped")
        return text

    usd = [to_usd(a + b * y) for y in ys]
    ymin, ymax, ticks = pick_axis(min(usd), max(usd))

    def yp(v: float) -> int:
        return int(round(BOT_Y - (v - ymin) / (ymax - ymin) * (BOT_Y - TOP_Y)))

    new_ys = [yp(v) for v in usd]
    if not all(TOP_Y <= y <= BOT_Y for y in new_ys):
        report.append(f"  {slug}: redrawn points escape the plot — skipped")
        return text

    line_d = "M " + " L ".join(f"{x},{y}" for x, y in zip(X_POINTS, new_ys))
    area_d = line_d + f" L {X_POINTS[-1]},{BOT_Y} L {X_POINTS[0]},{BOT_Y} Z"

    # 1. tick labels, top-down and therefore descending — the six mislabelled
    #    pages come out the right way up as a side effect.
    for (y, old), val in zip(tick_matches, reversed(ticks)):
        text = text.replace(
            f'<text x="38" y="{y}">HK${old}</text>',
            f'<text x="38" y="{y}">{money(val)}</text>',
        )

    # 2. the two paths and the six vertex dots.
    text = text.replace(m.group(0), f'<path d="{line_d}"')
    text = AREA_D_RE.sub(f'<path d="{area_d}"', text, count=1)
    for x, old_y, new_y in zip(X_POINTS, ys, new_ys):
        text = text.replace(f'<circle cx="{x}" cy="{old_y}" ', f'<circle cx="{x}" cy="{new_y}" ')

    # 3. the two value labels.
    #
    #    最低 is the leftmost point, so its label used to be centred on the dot
    #    at x=45 — which puts it in the same gutter as the tick labels (they end
    #    at x=38). With the ticks 35px apart and the type 10px, that gutter only
    #    has four slivers of clear rows, and the dot does not always land in one:
    #    on rtx-5060 the re-axed dot sits 4px from the $375 tick and the two
    #    strings render on top of each other. Move the label to the right of its
    #    dot instead. The leftmost point is the historical low, so the curve
    #    always rises away from it and the text sits in clear space below.
    #
    #    现价 stays end-anchored at x=565. It extends left over the plot interior
    #    and never reaches the tick gutter, so it is already safe.
    low_attrs = low_m.group(2).replace('text-anchor="middle"', 'text-anchor="start"')
    text = text.replace(
        low_m.group(0),
        f'<text x="{LOW_LABEL_X + 9}" y="{min(max(new_ys[0] + 4, 14), 176)}"{low_attrs}>'
        f"{money(usd[0])} (最低)</text>",
    )
    cur_dy = int(cur_m.group(1)) - ys[-1]
    text = text.replace(
        cur_m.group(0),
        f'<text x="{CUR_LABEL_X}" y="{max(new_ys[-1] + cur_dy, 14)}"{cur_m.group(2)}>'
        f"{money(usd[-1])} (现价)</text>",
    )

    old_order = "↓" if float(tick_matches[0][1].replace(",", "")) > float(
        tick_matches[4][1].replace(",", "")
    ) else "↑(inverted labels)"
    report.append(
        f"  {slug}: {old_order} axis {'/'.join(money(t) for t in ticks)}\n"
        f"      points {', '.join(money(v) for v in usd)}"
    )
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    report: list[str] = []
    files = sorted(DOCS.glob("games/rtx-*.md")) + [DOCS / "tech" / "index.md"]
    report.append("charts:")
    md_changed = 0

    for path in files:
        text = path.read_text(encoding="utf-8")
        original = text

        if "mg-gpu-chart" in text:
            text = reaxis_chart(text, path.stem, report)

        # Everything else — price cards, stat tables, ranges, prose — is a
        # straight unit change.
        text = MONEY_RE.sub(lambda m: money(int(m.group(1).replace(",", "")) / RATE), text)

        if text != original:
            md_changed += 1
            if not args.dry_run:
                path.write_text(text, encoding="utf-8")

    # The hero and sparkline SVGs carry HK$ in <text> nodes only — no axis, so
    # no geometry to redo, just the unit.
    svgs = sorted(DOCS.glob("assets/games/rtx-*.svg")) + sorted(
        DOCS.glob("assets/games/spark/rtx-*.svg")
    )
    svg_values = 0
    for path in svgs:
        text = path.read_text(encoding="utf-8")
        text, n = MONEY_RE.subn(
            lambda m: money(int(m.group(1).replace(",", "")) / RATE), text
        )
        if n:
            svg_values += n
            if not args.dry_run:
                path.write_text(text, encoding="utf-8")

    print("\n".join(report))
    verb = "would change" if args.dry_run else "written"
    print(f"\n{md_changed} .md file(s) {verb}")
    print(f"{len(svgs)} svg file(s) checked, {svg_values} value(s) {verb}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
