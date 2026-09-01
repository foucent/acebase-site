#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge Honor of Kings top-up prices scraped from bittopup + topuplist into
per-tier lowest / highest / average, convert HKD -> USD, and write into
docs/assets/games/prices.json under games.hok.

Source data: C:\\1Work\\_tmp_ocr\\hok_scrape.json (written by scrape_hok.py)
"""
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PRICES_JSON = os.path.normpath(os.path.join(HERE, "..", "docs", "assets", "games", "prices.json"))
SCRAPE_JSON = r"C:\1Work\_tmp_ocr\hok_scrape.json"
FX_API = "https://open.er-api.com/v6/latest/HKD"
FX_FALLBACK = 7.80  # HKD per USD

# Official HoK token tiers: (purchase_qty, bonus_qty)
TIERS = [(80, 0), (240, 0), (400, 0), (560, 0), (800, 30), (1200, 45),
         (2400, 108), (4000, 180), (8000, 360)]


def norm_topuplist(t):
    """'800+30' -> (800, 30); '240' -> (240, 0)."""
    m = re.match(r"([\d,]+)\s*(?:\+\s*([\d,]+))?", t)
    if not m:
        return None
    a = int(m.group(1).replace(",", ""))
    b = int(m.group(2).replace(",", "")) if m.group(2) else 0
    return (a, b) if (a, b) in TIERS else None


def norm_bittopup(t):
    """bittopup shows total tokens; match to an official tier."""
    m = re.match(r"([\d,]+)", t)
    if not m:
        return None
    a = int(m.group(1).replace(",", ""))
    for base, bonus in TIERS:
        if a == base:
            return (base, bonus)
    for base, bonus in TIERS:
        if a == base + bonus:  # e.g. 2508 = 2400 + 108
            return (base, bonus)
    return None


def tier_title(base, bonus):
    return f"{base} + {bonus} 点券" if bonus else f"{base} 点券"


def hkd_to_usd_rate():
    try:
        req = urllib.request.Request(FX_API, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read().decode("utf-8"))
        usd = d.get("rates", {}).get("USD")
        if usd:
            rate = 1.0 / float(usd)
            print(f"[fx] live rate: 1 USD = {rate:.4f} HKD")
            return rate
    except Exception as e:
        print(f"[fx] API failed ({e}); using fallback {FX_FALLBACK}", file=sys.stderr)
    return FX_FALLBACK


def main():
    scraped = json.load(open(SCRAPE_JSON, encoding="utf-8"))
    bt_text = scraped["bittopup"].get("text", "")
    tl_text = scraped["topuplist"].get("text", "")

    sources = {}  # tier -> {"bittopup": p, "topuplist": p}
    re_bt = re.compile(
        r"([\d,]+)\s*Tokens\s*\n+\s*Honor of Kings\s*\n+\s*Discount:[^\n]*\n+\s*HK\$ ?([\d,]+\.\d\d)"
    )
    for m in re_bt.finditer(bt_text):
        tier = norm_bittopup(m.group(1))
        if not tier:
            print(f"[bt] unmatched: {m.group(1)}")
            continue
        sources.setdefault(tier, {})["bittopup"] = float(m.group(2).replace(",", ""))

    re_tl = re.compile(r"([\d,]+(?:\s*\+\s*[\d,]+)?)\s*点券\s*\n+\s*HK\$ ?([\d,]+\.\d\d)")
    for m in re_tl.finditer(tl_text):
        tier = norm_topuplist(m.group(1))
        if not tier:
            print(f"[tl] unmatched: {m.group(1)}")
            continue
        sources.setdefault(tier, {})["topuplist"] = float(m.group(2).replace(",", ""))

    rate = hkd_to_usd_rate()
    rows = []
    for (base, bonus) in sorted(sources, key=lambda t: t[0]):
        prices = list(sources[(base, bonus)].values())
        usd = [round(p / rate, 2) for p in prices]
        r = {
            "title": tier_title(base, bonus),
            "lowest": min(usd),
            "highest": max(usd),
            "average": round(sum(usd) / len(usd), 2),
            "sources": {k: round(v / rate, 2) for k, v in sources[(base, bonus)].items()},
        }
        rows.append(r)
        print(f"  {r['title']:18s} ${r['lowest']:6.2f} ${r['highest']:6.2f} ${r['average']:6.2f} | {r['sources']}")

    d = json.load(open(PRICES_JSON, encoding="utf-8"))
    d["games"]["hok"] = [{k: v for k, v in r.items() if k != "sources"} for r in rows]
    d["currency"] = "USD"
    d["updated"] = "2026-09-02"
    json.dump(d, open(PRICES_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote {PRICES_JSON} ({len(rows)} hok tiers)")


if __name__ == "__main__":
    main()
