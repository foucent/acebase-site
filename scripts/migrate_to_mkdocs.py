# -*- coding: utf-8 -*-
"""Migrate Hugo AceBase content into a MyGear-wiki-style MkDocs Material site."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT.parent / "mygear-wiki"
POSTS = ROOT / "content" / "posts"
SHORTCODES = ROOT / "layouts" / "shortcodes"
DOCS = ROOT / "docs"
OVERRIDES = ROOT / "overrides"

SLUG_OVERRIDES = {
    "7 CS2 Trivia Facts You Definitely Never Noticed-en.md": ("guides", "cs2-trivia-facts"),
    "AK vs Galil The Most Heartbreaking Economic Paradox in CS2-en.md": ("guides", "ak-vs-galil"),
    "Cache Map Complete Guide-en.md": ("guides", "cache-map-complete-guide"),
    "CS2 8 Hardcore Details You Never Noticed From Frame Drop Mechanics to AI Sound Card Tech-en.md": (
        "guides",
        "cs2-hardcore-details",
    ),
    "CS2 R8 Revolver The Anti-Human Charging God of Wheelchairs-en.md": ("guides", "cs2-r8-revolver"),
    "CS2 Three Dark Features Scalping Ecosystem Cheat Tolerance and Internet Cafe Ban-en.md": (
        "guides",
        "cs2-three-dark-features",
    ),
    "How Much Do You Actually Lose Opening Terminal Crates Classic Cases Are the Rational Player Way-en.md": (
        "guides",
        "terminal-crates-vs-classic-cases",
    ),
    "miHoYo UE5 Realistic Fantasy New Game First Look-en.md": ("guides", "mihoyo-ue5-first-look"),
    "The Hidden Rhythm of AK Spray Control-en.md": ("guides", "ak-spray-control"),
    "ZOWIE New Mousepad Professional Debut-en.md": ("guides", "zowie-mousepad-debut"),
    "model.md": ("guides", "model-notes"),
}

PLAYER_MAP = {
    "s1mple": "players/s1mple.md",
    "niko": "players/niko.md",
    "m0nesy": "players/m0nesy.md",
    "ropz": "players/ropz.md",
    "zywoo": "players/zywoo.md",
    "xantares": "players/xantares.md",
    "tenz": "players/tenz.md",
    "kyousuke": "players/kyousuke.md",
    "aspas": "players/aspas.md",
    "zmjjkk": "players/zmjjkk.md",
    "donk": "players/donk.md",
}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta: dict = {}
    for line in parts[1].splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        meta[key] = val
    return meta, parts[2].lstrip("\n")


def slugify(name: str) -> str:
    name = re.sub(r"\.md$", "", name)
    name = re.sub(r"-en$|-zh$", "", name, flags=re.I)
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    return name.strip("-")[:60] or "page"


def expand_shortcodes(body: str) -> str:
    def repl(match: re.Match) -> str:
        name = match.group(1)
        path = SHORTCODES / f"{name}.html"
        if not path.exists():
            return f"<!-- missing shortcode: {name} -->"
        html = path.read_text(encoding="utf-8")
        return f'\n\n<div class="ace-embed" markdown="0">\n{html}\n</div>\n\n'

    body = re.sub(r"\{\{<\s*([\w-]+)\s*>\}\}", repl, body)
    body = re.sub(r"\{\{%\s*([\w-]+)\s*%\}\}", repl, body)
    return body


def strip_leading_h1(body: str) -> str:
    return re.sub(r"^#\s+.+\n+", "", body.lstrip(), count=1)


def detect_section_and_slug(filename: str, body: str, meta: dict) -> tuple[str, str]:
    if filename in SLUG_OVERRIDES:
        return SLUG_OVERRIDES[filename]

    sc = re.findall(r"\{\{<\s*ps-([\w-]+)-settings\s*>\}\}", body)
    if sc:
        player = sc[0].lower().replace("_", "")
        # normalize m0nesy etc already fine
        return "players", player

    # Chinese player posts without readable filename
    title = meta.get("title", "")
    for key in PLAYER_MAP:
        if key.lower() in title.lower() or key.lower() in filename.lower():
            return "players", key

    tags = meta.get("tags", "").lower()
    cats = meta.get("categories", "").lower()
    if "player" in cats or "选手" in title or "设置" in title:
        return "players", slugify(filename)
    if filename.endswith("-en.md") or "CS2" in title or "VALORANT" in title or "CSGO" in cats.upper():
        return "guides", slugify(filename)
    return "guides", slugify(filename)


def write_page(section: str, slug: str, meta: dict, body: str) -> Path:
    out_dir = DOCS / section
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{slug}.md"
    title = meta.get("title", slug)
    desc = meta.get("description", "")
    date = meta.get("date", "")
    image = meta.get("image", "")

    # fix local image paths from Hugo /images/... to relative
    body = body.replace('src="/images/', 'src="../images/')
    body = re.sub(r"!\[]\(/images/", r"![](../images/", body)

    lines = ["---", f'title: "{title}"']
    if desc:
        lines.append(f'description: "{desc}"')
    if date:
        lines.append(f"date: {date}")
    if image:
        lines.append(f"image: {image}")
    lines.append("---")
    lines.append("")
    lines.append(body.rstrip() + "\n")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def copy_framework() -> None:
    if DOCS.exists():
        # keep migrating into docs; wipe generated only
        for child in list(DOCS.iterdir()):
            if child.name in {"images"}:
                continue
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    else:
        DOCS.mkdir(parents=True)

    # styles / js from wiki
    css_dir = DOCS / "stylesheets"
    js_dir = DOCS / "javascripts"
    css_dir.mkdir(parents=True, exist_ok=True)
    js_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(WIKI / "docs" / "stylesheets" / "extra.css", css_dir / "extra.css")
    for js in (WIKI / "docs" / "javascripts").glob("*.js"):
        shutil.copy2(js, js_dir / js.name)

    # overrides
    if OVERRIDES.exists():
        shutil.rmtree(OVERRIDES)
    shutil.copytree(WIKI / "overrides", OVERRIDES)

    # images
    img_src = ROOT / "assets" / "images"
    img_dst = DOCS / "images"
    if img_src.exists():
        if img_dst.exists():
            shutil.rmtree(img_dst)
        shutil.copytree(img_src, img_dst)

    # requirements
    (ROOT / "requirements.txt").write_text(
        "# click>=8.3 silently disables mkdocs serve livereload\n"
        "click==8.2.1\n"
        "mkdocs>=1.6\n"
        "mkdocs-material>=9.6\n"
        "mkdocs-redirects>=1.2\n",
        encoding="utf-8",
    )


def build_nav(pages: dict[str, list[tuple[str, str]]]) -> str:
    """pages: section -> [(title, path)]"""
    lines = [
        "site_name: AceBase",
        "site_url: https://acebase.cc/",
        "repo_url: https://acebase.cc/",
        "repo_name: AceBase",
        "theme:",
        "  name: material",
        "  custom_dir: overrides",
        "  language: custom",
        "  palette:",
        "    scheme: default",
        "    primary: teal",
        "    accent: teal",
        "  icon:",
        "    repo: material/controller-classic",
        "  features:",
        "    - search.suggest",
        "    - search.highlight",
        "    - content.code.copy",
        "    - content.tables.scroll",
        "    - navigation.sections",
        "",
        "plugins:",
        "  - search",
        "",
        "markdown_extensions:",
        "  - toc",
        "  - tables",
        "  - fenced_code",
        "  - md_in_html",
        "",
        "extra_css:",
        "  - stylesheets/extra.css",
        "  - stylesheets/player-settings.css",
        "",
        "extra_javascript:",
        "  - javascripts/gallery-lightbox.js",
        "",
        "watch:",
        "  - overrides",
        "",
        "extra:",
        "  social:",
        "    - icon: material/controller-classic",
        "      link: https://acebase.cc/",
        "      name: AceBase",
        "",
        "nav:",
        "  - Home: index.md",
    ]

    section_titles = {
        "players": "Player Settings",
        "guides": "Guides & Articles",
    }
    for key in ("players", "guides"):
        items = pages.get(key, [])
        if not items:
            continue
        lines.append(f"  - {section_titles[key]}:")
        for title, rel in sorted(items, key=lambda x: x[0].lower()):
            # escape quotes in title for yaml
            safe = title.replace('"', "'")
            lines.append(f'      - "{safe}": {rel}')
    return "\n".join(lines) + "\n"


def write_index(pages: dict[str, list[tuple[str, str]]]) -> None:
    players = sorted(pages.get("players", []), key=lambda x: x[0].lower())
    guides = sorted(pages.get("guides", []), key=lambda x: x[0].lower())

    lines = [
        "# AceBase",
        "",
        "硬核玩家基地：CS2 / VALORANT 选手配置、电竞深度教程与前沿硬件调优。",
        "",
        "---",
        "",
        "## Player Settings",
        "",
        "Pro player mouse, crosshair, video, and gear setups.",
        "",
    ]
    if players:
        lines.append("| Player | Page |")
        lines.append("| --- | --- |")
        for title, rel in players:
            lines.append(f"| {title} | [{title}]({rel}) |")
        lines.append("")
    lines += [
        "---",
        "",
        "## Guides & Articles",
        "",
        "Map guides, mechanics deep-dives, and esports notes.",
        "",
    ]
    if guides:
        for title, rel in guides:
            lines.append(f"- [{title}]({rel})")
        lines.append("")
    (DOCS / "index.md").write_text("\n".join(lines), encoding="utf-8")


def extract_player_settings_css() -> None:
    """Pull shared .ps-* CSS once from any shortcode into docs CSS."""
    css_chunks = []
    for path in sorted(SHORTCODES.glob("ps-*-settings.html")):
        text = path.read_text(encoding="utf-8")
        m = re.search(r"<style>(.*?)</style>", text, re.S)
        if m:
            css_chunks.append(m.group(1))
            break
    out = DOCS / "stylesheets" / "player-settings.css"
    if css_chunks:
        out.write_text("/* Player settings cards (from Hugo shortcodes) */\n" + css_chunks[0], encoding="utf-8")
    else:
        out.write_text("/* no player settings css found */\n", encoding="utf-8")


def strip_style_from_embed(html: str) -> str:
    return re.sub(r"<style>.*?</style>\s*", "", html, flags=re.S)


def main() -> None:
    copy_framework()
    extract_player_settings_css()

    pages: dict[str, list[tuple[str, str]]] = {"players": [], "guides": []}
    used_slugs: set[tuple[str, str]] = set()

    for path in sorted(POSTS.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        section, slug = detect_section_and_slug(path.name, body, meta)
        key = (section, slug)
        if key in used_slugs:
            slug = f"{slug}-{len(used_slugs)}"
            key = (section, slug)
        used_slugs.add(key)

        body = expand_shortcodes(body)
        # remove duplicated <style> blocks now that CSS is external
        body = strip_style_from_embed(body)
        body = strip_leading_h1(body)

        out = write_page(section, slug, meta, body)
        rel = f"{section}/{out.name}"
        title = meta.get("title", slug)
        # shorten player nav titles
        if section == "players":
            m = re.search(r"(s1mple|NiKo|m0NESY|ropz|ZywOo|XANTARES|TenZ|kyousuke|aspas|ZmjjKK|donk)", title, re.I)
            if m:
                title = m.group(1)
            elif slug:
                title = slug
        pages[section].append((title, rel))
        print(f"OK {path.name} -> {rel}")

    write_index(pages)
    (ROOT / "mkdocs.yml").write_text(build_nav(pages), encoding="utf-8")

    # deploy workflow
    wf = ROOT / ".github" / "workflows"
    wf.mkdir(parents=True, exist_ok=True)
    # keep old hugo.yml but add/replace deploy
    (wf / "deploy-mkdocs.yml").write_text(
        """name: Deploy AceBase (MkDocs)
on:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Build site
        run: mkdocs build
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
          cname: acebase.cc
""",
        encoding="utf-8",
    )

    # .gitignore
    gi = ROOT / ".gitignore"
    existing = gi.read_text(encoding="utf-8") if gi.exists() else ""
    extras = ["site/", "__pycache__/", "*.pyc", ".hugo_build.lock"]
    for e in extras:
        if e not in existing:
            existing += ("\n" if existing and not existing.endswith("\n") else "") + e + "\n"
    gi.write_text(existing, encoding="utf-8")

    print("Done. Pages:", {k: len(v) for k, v in pages.items()})


if __name__ == "__main__":
    main()
