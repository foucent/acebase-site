#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Download topuplist gift-card product images to docs/assets/gift-cards/."""
import json
import urllib.request
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent  # acebase.cc
OUT = BASE / "docs" / "assets" / "gift-cards"
OUT.mkdir(parents=True, exist_ok=True)

IMGS = {
    "jawaker": "https://file.topuplist.com/2026/05/1779442489_KQQsvjMRkG.png",
    "kammelna": "https://file.topuplist.com/2026/05/1779440553_xqOfyY3kUI.png",
    "amazon": "https://file.topuplist.com/2026/05/1779439589_GsrH7xkPEE.png",
    "netflix": "https://file.topuplist.com/2026/05/1779438630_tkyN2tT55D.png",
    "xbox": "https://file.topuplist.com/2026/05/1779354552_T2cDB9QkkK.png",
    "apple": "https://file.topuplist.com/2026/05/1779352474_gIGvqXOrWI.png",
    "google": "https://file.topuplist.com/2026/05/1779270351_YVnoJRCdv9.png",
}

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


for slug, url in IMGS.items():
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
