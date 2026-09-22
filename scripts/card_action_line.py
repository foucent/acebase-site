#!/usr/bin/env python3
"""One-off: put each /tech card's 展开 and 去亚马逊购买 on one line.

uncrate ends every listing entry the same way — "Read More or Buy from X", one
centred line, both links set alike, a small connective between them. The card
had them stacked: 展开 ran on from the end of the lead sentence, and 去亚马逊购买
sat on a line of its own below the fold. They are one line now.

The awkward part is structural, not visual. 展开 is what opens the fold and has
to stay inside <summary> — a summary is a real focusable control, which is why
the fold was built on <details> in the first place, and it has to keep working
with JavaScript off. The buy link has to stay out of the summary: a link that is
also the disclosure control is one mis-click away from a tab nobody asked for.

So the action line goes *inside* the summary and the buy link rides along with
it as a sibling of the control rather than as part of its label. A click on an
interactive descendant does not run the summary's activation behaviour, so the
link follows without toggling — but that is a claim about browser behaviour, not
about markup. It was checked in a browser, not assumed: clicking the link left
details.open at false and clicking the cue still opened and closed the fold, at
1440px and at 390px, and the fold still opened with JavaScript disabled.

Only /tech is touched. The ten band pages keep the run-on cue they were built
with, so this is a card change and not a site-wide one.

Run from the repo root:  python scripts/card_action_line.py [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
PAGE = DOCS / "tech" / "index.md"

sys.path.insert(0, str(ROOT / "scripts"))
from ab_cards import AMAZON_HOME  # noqa: E402

EXPECTED = 9

# The cue and the </summary> that closed it, as tech_card_grid.py wrote them.
CUE_RE = re.compile(
    r"(?P<pad>[ ]*)<span class=\"ab-fold__cue\">"
    r"<span class=\"ab-fold__cue-more\">展开</span>"
    r"<span class=\"ab-fold__cue-less\">收起</span></span>\n"
    r"(?P<qpad>[ ]*)</summary>\n"
)

# The CTA paragraph the action line replaces.
MORE_RE = re.compile(
    r"[ ]*<p class=\"ab-card__more\">"
    r"<a href=\"[^\"]+\" target=\"_blank\" rel=\"noopener\">去亚马逊购买</a></p>\n"
)


def rewrite(text: str) -> str:
    def act(m: re.Match) -> str:
        pad, qpad = m.group("pad"), m.group("qpad")
        return (
            f'{pad}<span class="ab-fold__act">\n'
            f'{pad}  <span class="ab-fold__cue">'
            f'<span class="ab-fold__cue-more">展开</span>'
            f'<span class="ab-fold__cue-less">收起</span></span>\n'
            f'{pad}  <em class="ab-fold__or">或</em>\n'
            f'{pad}  <a class="ab-fold__buy" href="{AMAZON_HOME}"'
            f' target="_blank" rel="noopener">去亚马逊购买</a>\n'
            f'{pad}</span>\n'
            f'{qpad}</summary>\n'
        )

    text, cues = CUE_RE.subn(act, text)
    text, mores = MORE_RE.subn("", text)
    if cues != EXPECTED:
        raise SystemExit(f"rewrote {cues} action lines, expected {EXPECTED}")
    if mores != EXPECTED:
        raise SystemExit(f"removed {mores} CTA paragraphs, expected {EXPECTED}")
    if "ab-card__more" in text:
        raise SystemExit("a .ab-card__more was left behind")
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    text = PAGE.read_text(encoding="utf-8")
    if "ab-fold__act" in text:
        raise SystemExit(f"{PAGE.name}: already rewritten")
    out = rewrite(text)

    if not args.dry_run:
        PAGE.write_text(out, encoding="utf-8")
    verb = "would rewrite" if args.dry_run else "rewrote"
    print(f"{verb} {EXPECTED} action lines in {PAGE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
