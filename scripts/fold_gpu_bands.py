#!/usr/bin/env python3
"""One-off: put the GPU bands' price rows behind a click.

uncrate's listing shows one line per item and keeps the rest behind Read More;
the GPU bands read the same way now. Each band's lead sentence becomes the
summary of a <details>, and the four price rows plus the fetch date move inside
it. The consult link stays outside — that is the action, not the detail.

<details> rather than a script: the summary is a real focusable control, so the
fold opens with the keyboard and still works with JavaScript switched off,
which matters on a page whose figures are the reason it exists.

Only the ten GPU pages are touched. The lead sentence itself is unchanged —
this moves markup around it, so no figure and no wording moves.

Run from the repo root:  python scripts/fold_gpu_bands.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs" / "games"

# The lead, then the two blocks that become the "more". Anchored on the closing
# </p> of each so a stray span inside them cannot end the match early.
BAND_RE = re.compile(
    r"(?P<indent>[ ]*)<p class=\"ab-hero__excerpt\">(?P<lead>.*?)</p>\n"
    r"\n"
    r"(?P<detail>[ ]*<p class=\"ab-ec-list\">.*?</p>\n"
    r"\n"
    r"[ ]*<p class=\"ab-ec-foot\">.*?</p>\n)",
    re.S,
)

# File -> how many bands it must contain. A number here is a promise: if a page
# gains or loses a band the count fails loudly rather than folding half of it.
#
# The overview has since moved to /tech and its bands became cards; the entry is
# kept because this is a record of a finished run, not a script with a future.
PAGES = {
    "gpu-prices.md": 9,
    "gpu-deals.md": 1,
    "rtx-3060.md": 1,
    "rtx-3060-ti.md": 1,
    "rtx-4070-ti-super.md": 1,
    "rtx-4080.md": 1,
    "rtx-4080-super.md": 1,
    "rtx-4090.md": 1,
    "rtx-5060.md": 1,
    "rtx-5060-ti.md": 1,
}


def fold(match: re.Match) -> str:
    pad, lead, detail = match.group("indent"), match.group("lead"), match.group("detail")
    inner = "\n".join(("  " + ln) if ln.strip() else ln for ln in detail.rstrip("\n").split("\n"))
    return (
        f'{pad}<details class="ab-fold">\n'
        f'{pad}  <summary class="ab-fold__summary">\n'
        f'{pad}    <span class="ab-fold__lead">{lead}</span>\n'
        f'{pad}    <span class="ab-fold__cue">'
        f'<span class="ab-fold__cue-more">展开</span>'
        f'<span class="ab-fold__cue-less">收起</span></span>\n'
        f'{pad}  </summary>\n'
        f'\n'
        f'{inner}\n'
        f'{pad}</details>\n'
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    for name, expected in PAGES.items():
        path = DOCS / name
        text = path.read_text(encoding="utf-8")
        if "ab-fold" in text:
            raise SystemExit(f"{name}: already folded")
        new, count = BAND_RE.subn(fold, text)
        if count != expected:
            raise SystemExit(f"{name}: folded {count} bands, expected {expected}")
        if "ab-hero__excerpt" in new:
            raise SystemExit(f"{name}: a lead was left unfolded")
        if not args.dry_run:
            path.write_text(new, encoding="utf-8")
        print(f"{'would fold' if args.dry_run else 'folded'} {count:>2}  {name}")


if __name__ == "__main__":
    main()
