#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge Arena Breakout (暗区突围) Bonds top-up prices from bittopup + topuplist +
topuplive into per-tier lowest/highest/average, convert HKD -> USD, write into
prices.json under games.arena-breakout.

Source data: C:\\1Work\\_tmp_ocr\\ab_scrape.json (written by scrape_ab.py)
"""
import json
import os
import re
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PRICES_JSON = os.path.normpath(os.path.join(HERE, "..", "docs", "assets", "games", "prices.json"))
SCRAPE_JSON = r"C:\1Work\_tmp_ocr\ab_scrape.json"
FX_API = "https://open.er-api.com/v6/latest/HKD"
FX_FALLBACK = 7.80

ORDER = ["60 + 6 Bonds", "310 + 25 Bonds", "630 + 45 Bonds", "1580 + 110 Bonds",
         "3200 + 200 Bonds", "6500 + 320 Bonds", "13000 + 640 Bonds"]


def canon(num):
    """'1,300' -> '1300'"""
    return num.replace(",", "")


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
        print(f"[fx] API failed ({e}); using fallback {FX_FALLBACK}", file=__import__("sys").stderr)
    return FX_FALLBACK


def parse_bittopup(text):
    """Card layout: tier title, 暗区突围, 折扣 line, then discounted HK$ (list follows)."""
    out = {}
    re_tier = re.compile(r"([\d,]+) \+ ([\d,]+) Bonds\s*\n\s*\n\s*暗区突围\s*\n\s*\n\s*折扣:[^\n]*\n\s*HK\$ ?([\d,]+\.\d\d)")
    for m in re_tier.finditer(text):
        tier = f"{canon(m.group(1))} + {canon(m.group(2))} Bonds"
        price = float(m.group(3).replace(",", ""))  # discounted price
        out.setdefault(tier, price)
    return out


def parse_topuplist(text):
    """tier label like '60+6 Tokens', then discounted HK$ then list HK$."""
    out = {}
    re_tier = re.compile(r"(\d+)\+(\d+) Tokens\s*\n\s*HK\$([\d,]+\.\d\d)\s*\n\s*HK\$([\d,]+\.\d\d)")
    for m in re_tier.finditer(text):
        tier = f"{canon(m.group(1))} + {canon(m.group(2))} Bonds"
        price = float(m.group(3).replace(",", ""))
        out.setdefault(tier, price)
    return out


def parse_topuplive(text):
    """tier line ('60 + 6 Bonds', ' *2' bundle excluded), then 'HK$', then price lines."""
    out = {}
    re_tier = re.compile(r"([\d,]+) \+ ([\d,]+) Bonds(?! ?\*)\s*\n\s*HK\$\s*\n\s*([\d,]+\.\d\d)\s*\n\s*([\d,]+\.\d\d)")
    for m in re_tier.finditer(text):
        tier = f"{canon(m.group(1))} + {canon(m.group(2))} Bonds"
        price = float(m.group(3).replace(",", ""))  # first price line = discounted
        out.setdefault(tier, price)
    return out


def main():
    scraped = json.load(open(SCRAPE_JSON, encoding="utf-8"))
    sources = {}  # tier -> {"bittopup": p, "topuplist": p, "topuplive": p}
    for name, parser in (("bittopup", parse_bittopup),
                         ("topuplist", parse_topuplist),
                         ("topuplive", parse_topuplive)):
        text = scraped.get(name, {}).get("text", "")
        parsed = parser(text)
        print(f"[{name}] parsed {len(parsed)} tiers: {parsed}")
        for tier, p in parsed.items():
            sources.setdefault(tier, {})[name] = p

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
    d["games"]["arena-breakout"] = [{k: v for k, v in r.items() if k != "sources"} for r in rows]
    d["currency"] = "USD"
    d["updated"] = "2026-09-03"
    json.dump(d, open(PRICES_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"wrote {PRICES_JSON} ({len(rows)} arena-breakout tiers)")


if __name__ == "__main__":
    main()
