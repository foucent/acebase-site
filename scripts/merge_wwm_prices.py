#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge Where Winds Meet (Yan Yun 16 Sheng) top-up prices from bittopup + topuplist
into per-tier lowest/highest/average, convert HKD -> USD, write into prices.json
under games.where-winds-meet.

Source data: C:\\1Work\\_tmp_ocr\\wwm_scrape.json (written by scrape_wwm.py)
"""
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PRICES_JSON = os.path.normpath(os.path.join(HERE, "..", "docs", "assets", "games", "prices.json"))
SCRAPE_JSON = r"C:\1Work\_tmp_ocr\wwm_scrape.json"
FX_API = "https://open.er-api.com/v6/latest/HKD"
FX_FALLBACK = 7.80

# bittopup's Elite Battle Pass row is data-corrupted (sale price > list price);
# drop that source row for this tier.
BT_EXCLUDE = {"Elite Battle Pass"}

# Display order: Echo Beads ascending, then passes.
ORDER = ["60 Echo Beads", "180 Echo Beads", "300 Echo Beads", "600 Echo Beads",
         "900 Echo Beads", "1800 Echo Beads", "3000 Echo Beads", "6000 Echo Beads",
         "12000 Echo Beads", "Monthly Pass", "Elite Battle Pass", "Premium Battle Pass"]


def norm(t):
    t = t.strip()
    t = re.sub(r"^Where Winds Meet\s+", "", t)
    t = re.sub(r"^1\s+", "", t)
    return t


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
        r"Where Winds Meet\s+([^\n]+?)\s*\n\s*\n\s*燕云十六声\s*\n\s*\n\s*折扣:[^\n]*\n\s*HK\$ ?([\d,]+\.\d\d)"
    )
    for m in re_bt.finditer(bt_text):
        tier = norm(m.group(1))
        if tier in BT_EXCLUDE:
            print(f"[bt] excluded corrupted tier: {tier}")
            continue
        if tier not in ORDER:
            print(f"[bt] unmatched: {tier}")
            continue
        sources.setdefault(tier, {})["bittopup"] = float(m.group(2).replace(",", ""))

    re_tl = re.compile(r"((?:[\d,]+(?: Echo Beads)?|1(?: Monthly Pass| Elite Battle Pass| Premium Battle Pass)))\s*\n\s*HK\$ ?([\d,]+\.\d\d)")
    for m in re_tl.finditer(tl_text):
        tier = norm(m.group(1))
        if tier not in ORDER:
            print(f"[tl] unmatched: {tier}")
            continue
        sources.setdefault(tier, {})["topuplist"] = float(m.group(2).replace(",", ""))

    rate = hkd_to_usd_rate()
    rows = []
    for tier in ORDER:
        if tier not in sources:
            continue
        usd = [round(p / rate, 2) for p in sources[tier].values()]
        r = {
            "title": tier,
            "lowest": min(usd),
            "highest": max(usd),
            "average": round(sum(usd) / len(usd), 2),
            "sources": {k: round(v / rate, 2) for k, v in sources[tier].items()},
        }
        rows.append(r)
        print(f"  {r['title']:18s} ${r['lowest']:6.2f} ${r['highest']:6.2f} ${r['average']:6.2f} | {r['sources']}")

    d = json.load(open(PRICES_JSON, encoding="utf-8"))
    d["games"]["where-winds-meet"] = [{k: v for k, v in r.items() if k != "sources"} for r in rows]
    d["currency"] = "USD"
    d["updated"] = "2026-09-02"
    json.dump(d, open(PRICES_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote {PRICES_JSON} ({len(rows)} where-winds-meet tiers)")


if __name__ == "__main__":
    main()
