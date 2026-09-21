#!/usr/bin/env python3
"""One-off: let a shut /tech card show its price.

The four price rows are the reason the card exists and they were the one thing
a shut card did not show: a reader got a photo, a model name and a sentence,
and had to open the fold to learn what anything costs.

A shut <details> hides its content whole — there is no such thing as a
partially open one — so the block cannot both stay inside the fold and be half
readable. It moves out to sit beside the fold, and the fold's own `open`
attribute drives it through the sibling combinator:

    .ab-fold[open] ~ .ab-ec-list   { max-height: none }

which needs no :has() and keeps working with JavaScript off. The fold is a
state holder now: it owns the two attributes that matter (open, and the cue
that flips with it) and the block it reveals is the next sibling.

The cards are marked `ab-card--fold` in the same pass. `.ab-card__copy` is
shared with the homepage, and the new rules hang the reserved space for the
action line on it; without a hook that only these nine cards carry, the
homepage's forty-one would each grow by the height of a line nobody drew.

Only /tech is touched. The nine band pages — the eight model pages and the
deals page — keep their rows inside the fold, because they have the width to
print all four at once.

Run from the repo root:  python scripts/card_price_peek.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PAGE = DOCS / "tech" / "index.md"

EXPECTED = 9

# The two paragraphs the fold body is made of, and the </details> that used to
# close over them. Anchored on </summary> so the match cannot start anywhere
# else in the card.
BODY_RE = re.compile(
    r"\n\n"
    r"(?P<list>[ ]*<p class=\"ab-ec-list\">.*?</p>)\n\n"
    r"(?P<foot>[ ]*<p class=\"ab-ec-foot\">.*?</p>)\n"
    r"(?P<close>[ ]*</details>)",
    re.S,
)

CARD_RE = re.compile(r"<article class=\"ab-card ab-card--photo\" id=\"")


def rewrite(text: str) -> tuple[str, int]:
    moved = 0

    def swap(m: re.Match) -> str:
        nonlocal moved
        moved += 1
        return (
            f"\n{m.group('close')}\n\n"
            f"{m.group('list')}\n\n"
            f"{m.group('foot')}"
        )

    text = BODY_RE.sub(swap, text)

    text, marked = CARD_RE.subn(
        "<article class=\"ab-card ab-card--photo ab-card--fold\" id=\"", text
    )
    if marked != moved:
        raise SystemExit(
            f"{moved} price blocks moved but {marked} cards marked — a card "
            f"that has one and not the other is broken, so nothing was written"
        )
    return text, moved


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    text = PAGE.read_text(encoding="utf-8")

    if "ab-card--fold" in text:
        raise SystemExit(f"{PAGE.name} is already rewritten")
    if BODY_RE.search(text) is None:
        raise SystemExit(
            "no <details> still closes over a price block — has this already "
            "been run, or did the cards get rebuilt from somewhere else?"
        )

    out, moved = rewrite(text)
    if moved != EXPECTED:
        raise SystemExit(
            f"rewrote {moved} cards, expected {EXPECTED} — the page holds nine "
            f"models and a partial run would leave some cards opening a fold "
            f"that no longer hides anything"
        )
    if BODY_RE.search(out) or out.count("ab-card--fold") != EXPECTED:
        raise SystemExit("a price block survived the move")

    print(f"{PAGE.relative_to(ROOT)}: {moved} price blocks moved out of their "
          f"folds, {moved} cards marked ab-card--fold")
    if args.dry_run:
        print("dry run, nothing written")
        return 0
    PAGE.write_text(out, encoding="utf-8")
    print("written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
