#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge game top-up prices scraped from bittopup / seagm / topuplist into
per-tier lowest / highest / average, convert HKD -> USD with a live FX rate,
and write the result into docs/assets/games/prices.json.

Sources (all expose HKD):
  - bittopup : https://bittopup.com/goods/<game>
  - seagm    : https://www.seagm.com/<locale>/<game>
  - topuplist: https://topuplist.com/<locale>/product/<slug>

Free FX rate API (no key): https://open.er-api.com/v6/latest/HKD
"""
import json
import os
import re
import sys
import urllib.request

TMP = r"C:\Users\fouce\AppData\Local\Temp"
HERE = os.path.dirname(os.path.abspath(__file__))
PRICES_JSON = os.path.normpath(os.path.join(HERE, "..", "docs", "assets", "games", "prices.json"))
FX_API = "https://open.er-api.com/v6/latest/HKD"
FX_FALLBACK = 7.80  # HKD per USD (peg band ~7.75-7.85) if API is unreachable

sys.path.insert(0, HERE)
from parse_pubg_prices import parse_bittopup, parse_topuplist, parse_seagm


def norm_tier(t):
    """Normalize tier label: '300+25 UC' -> '300 + 25 UC', '60 UC' -> '60 UC'."""
    t = t.strip()
    t = re.sub(r"\s+", " ", t)
    m = re.match(r"([\d,]+)\s*\+\s*([\d,]+) UC", t)
    if m:
        a, b = m.group(1).replace(",", ""), m.group(2).replace(",", "")
        return f"{a} + {b} UC"
    m2 = re.match(r"([\d,]+) UC", t)
    if m2:
        return f"{m2.group(1).replace(',', '')} UC"
    return t


def hkd_to_usd_rate():
    """Return HKD per USD via the free open.er-api.com rate, fallback 7.80."""
    try:
        req = urllib.request.Request(FX_API, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            d = json.loads(r.read().decode("utf-8"))
        usd = d.get("rates", {}).get("USD")
        if usd:
            # API returns 1 HKD = X USD; we need HKD per USD = 1/X
            rate = 1.0 / float(usd)
            print(f"[fx] live rate: 1 USD = {rate:.4f} HKD (from open.er-api.com)")
            return rate
    except Exception as e:
        print(f"[fx] API failed ({e}); using fallback {FX_FALLBACK}", file=sys.stderr)
    return FX_FALLBACK


def main():
    # --- source data files (written by Playwright/curl scraping) ---
    seagm = parse_seagm(open(os.path.join(TMP, "seagm_pubg.html"), encoding="utf-8", errors="replace").read())
    bt = parse_bittopup(open(os.path.join(TMP, "pubg_bittopup.txt"), encoding="utf-8", errors="replace").read())
    tl = parse_topuplist(open(os.path.join(TMP, "pubg_topuplist.txt"), encoding="utf-8", errors="replace").read())

    # source -> {tier: discounted_price}  (use discounted/sale price for comparison)
    sources = {}
    for t, p in seagm:
        sources.setdefault(norm_tier(t), []).append(("seagm", p))
    for t, p, _o in bt:
        sources.setdefault(norm_tier(t), []).append(("bittopup", p))
    for t, p, _o in tl:
        sources.setdefault(norm_tier(t), []).append(("topuplist", p))

    # build rows for UC tiers only (exclude WOW Coins)
    rows = []
    for tier in sorted(sources, key=lambda x: int(re.match(r"(\d+)", x).group(1))):
        if "WOW" in tier:
            continue
        prices = [p for _s, p in sources[tier]]
        if not prices:
            continue
        rows.append({
            "title": tier,
            "lowest": round(min(prices), 2),
            "highest": round(max(prices), 2),
            "average": round(sum(prices) / len(prices), 2),
            "sources": {s: p for s, p in sources[tier]},
        })

    rate = hkd_to_usd_rate()
    usd_rows = [
        {k: (round(v / rate, 2) if k in ("lowest", "highest", "average") else v) for k, v in r.items()}
        for r in rows
    ]

    print(f"\n=== merged (USD, {rate:.4f} HKD/USD) ===")
    for r in usd_rows:
        print(f"  {r['title']:16s} ${r['lowest']:6.2f} ${r['highest']:6.2f} ${r['average']:6.2f} | {r['sources']}")

    # Update prices.json (pubg-mobile) with the range schema + currency
    d = json.load(open(PRICES_JSON, encoding="utf-8"))
    d["games"]["pubg-mobile"] = [{k: v for k, v in r.items() if k != "sources"} for r in usd_rows]
    d["currency"] = "USD"
    d["updated"] = "2026-08-08"
    json.dump(d, open(PRICES_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote {PRICES_JSON}")


if __name__ == "__main__":
    main()
