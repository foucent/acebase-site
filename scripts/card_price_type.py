"""Give /tech's price rows a label element and no slash.

The rows read "名称 / $价格." and the slash is doing the separating work. Taking
it out leaves the label and the price as two bare runs of text in a span, which
is fine for one line of prose and useless for four rows of figures: without an
element around each there is nothing for the stylesheet to line up, and the
values would start at a different x on every row because the labels are
different widths.

So each row gains a .ab-ec-label and the price moves out to where the slash was.
The full stop comes along with it — left outside it would be a third run and
start a column of its own in the grid the stylesheet now builds, and it belongs
to the figure anyway.

This edits source, so it refuses to run twice and says what it found. Nothing
here is generated: docs/tech/index.md is hand-maintained and no script writes
back to it.

    /c/1Work/penv/Scripts/python.exe scripts/card_price_type.py --dry-run
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "tech" / "index.md"

ROW = re.compile(
    r'<span class="ab-ec-item">'
    r'(?P<label>.+?)'
    r'<span class="ab-ec-sep">/</span>'
    r'<span class="ab-ec-price">(?P<price>.+?)</span>'
    r'(?P<dot>\.?)'
    r'</span>'
)

EXPECTED = 36  # nine cards, four rows each


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    text = PAGE.read_text(encoding="utf-8")

    if "ab-ec-label" in text:
        print("! this page has already been converted — nothing to do")
        return 1
    found = len(ROW.findall(text))
    if found != EXPECTED:
        print(f"! expected {EXPECTED} rows, matched {found} — not touching it")
        return 1

    def rewrite(m: re.Match[str]) -> str:
        return (
            '<span class="ab-ec-item">'
            f'<span class="ab-ec-label">{m["label"]}</span>'
            f'<span class="ab-ec-price">{m["price"]}{m["dot"]}</span>'
            "</span>"
        )

    new = ROW.sub(rewrite, text)

    left = new.count('class="ab-ec-sep"')
    print(f"{found} rows rewritten, {left} slashes left in the page")
    if left:
        print("! the slashes were the point — stopping before writing")
        return 1

    if args.dry_run:
        first = new.find('<span class="ab-ec-item">')
        print(new[first:first + 220])
        print("(dry run, nothing written)")
        return 0

    PAGE.write_text(new, encoding="utf-8")
    print(f"wrote {PAGE.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
