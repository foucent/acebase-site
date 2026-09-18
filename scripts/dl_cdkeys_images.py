#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download topuplist cdkeys product images to docs/assets/gift-cards/."""
import json
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent  # acebase.cc
OUT = BASE / "docs" / "assets" / "gift-cards"
OUT.mkdir(parents=True, exist_ok=True)

PROD = json.load(
    open(BASE / "scripts" / "_topuplist_cdkeys_products.json", encoding="utf-8")
)

HDRS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Referer": "https://topuplist.com/",
}


def dl(url: str, dest: Path):
    req = urllib.request.Request(url, headers=HDRS)
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    dest.write_bytes(data)
    return len(data)


for d in PROD:
    slug = d.get("slug")
    url = d.get("ogImage") or ""
    if not slug or not url:
        print(f"skip {slug or '?'} (no ogImage)")
        continue
    ext = url.split("?")[0].rsplit(".", 1)[-1] or "jpg"
    dest = OUT / f"{slug}.{ext}"
    if dest.exists():
        print(f"skip {slug} (exists)")
        continue
    try:
        n = dl(url, dest)
        print(f"ok {slug}: {n} bytes -> {dest.relative_to(BASE)}")
    except Exception as e:
        print(f"FAIL {slug}: {e}")
