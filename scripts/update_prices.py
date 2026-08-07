#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fetch game top-up prices for the acebase.cc games hub and write a shared
prices.json consumed by docs/javascripts/games-prices.js.

Sources (tried in order):
  1. OffGamers API (sls.offgamers.com) — offer/product/seo_info + offer/search/lite
  2. Static fallback prices below (used when the API has no matching term)

Usage:
  python scripts/update_prices.py            # write docs/assets/games/prices.json
  python scripts/update_prices.py --dry-run  # print what would be written, no file
"""
import argparse
import json
import os
import ssl
import sys
import time
import urllib.parse
import urllib.request
from datetime import date, datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "docs", "assets", "games", "prices.json")

# OffGamers seo_term candidates per game (first match wins).
# Add the real seo_term once known, e.g. "valorant-points" -> "valorant-points-gift-card".
SEO_TERMS = {
    "valorant": ["valorant-points", "riot-points", "valorant"],
    "apex": ["apex-coins", "apex-legends", "apex"],
    "cs2": ["cs2", "counter-strike-2", "counter-strike"],
    "delta-force": ["delta-force", "delta-force-top-up"],
}

# Static fallback prices: [official, acebase] per tier. Only used if the
# OffGamers API returns nothing for a game. Delta Force mirrors the live
# /topup/delta-force/ page; others are reference placeholders.
FALLBACK = {
    "valorant": [
        {"title": "535 VP", "official": 4.99, "acebase": 4.49},
        {"title": "1060 VP", "official": 9.99, "acebase": 8.99},
        {"title": "2200 VP", "official": 19.99, "acebase": 17.99},
        {"title": "5650 VP", "official": 49.99, "acebase": 44.99},
        {"title": "11500 VP", "official": 99.99, "acebase": 89.99},
    ],
    "apex": [
        {"title": "500 Apex Coins", "official": 4.99, "acebase": 4.49},
        {"title": "1000 Apex Coins", "official": 9.99, "acebase": 8.99},
        {"title": "2000 Apex Coins", "official": 19.99, "acebase": 17.99},
        {"title": "4000 Apex Coins", "official": 39.99, "acebase": 35.99},
    ],
    "cs2": [
        {"title": "CS2 Case Key", "official": 2.49, "acebase": 2.29},
        {"title": "Steam Wallet $5", "official": 5.00, "acebase": 4.69},
        {"title": "Steam Wallet $10", "official": 10.00, "acebase": 9.39},
        {"title": "Steam Wallet $20", "official": 20.00, "acebase": 18.79},
    ],
    "delta-force": [
        {"title": "60 Delta Coins", "official": 0.98, "acebase": 0.55},
        {"title": "300 + 20 Delta Coins", "official": 4.77, "acebase": 2.74},
        {"title": "650 + 50 Delta Coins", "official": 9.78, "acebase": 5.62},
        {"title": "1300 + 120 Delta Coins", "official": 19.17, "acebase": 11.25},
        {"title": "6500 + 500 Delta Coins", "official": 95.85, "acebase": 57.69},
    ],
}

_CTX = ssl.create_default_context()
_CTX.check_hostname = False
_CTX.verify_mode = ssl.CERT_NONE
_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


def _get(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": _UA})
    with urllib.request.urlopen(req, timeout=timeout, context=_CTX) as r:
        return json.loads(r.read().decode("utf-8"))


def offgamers_offers(seo_term):
    """Return list of {title, official, acebase} via OffGamers API, or None."""
    try:
        info = _get(
            "https://sls.offgamers.com/offer/product/seo_info"
            f"?seo_term={urllib.parse.quote(seo_term)}&currency=USD"
        )
        payload = info.get("payload") or {}
        if not payload.get("service_id"):
            return None
        svc = payload["service_id"]
        brand = payload["brand_id"]
        lite = _get(
            "https://sls.offgamers.com/offer/search/lite"
            f"?service_id={svc}&brand_id={brand}&region_id=dbced0da-9266-4d46-884b-4a49c345e55c"
            "&country=US&currency=USD"
        )
        offers = []
        for col in (lite.get("payload") or {}).get("results", []):
            for o in col.get("offer_results", []):
                price = float(o.get("display_price") or o.get("converted_unit_price") or 0)
                if price <= 0:
                    continue
                offers.append(
                    {
                        "title": o.get("title") or "Top-Up",
                        "official": round(price / 0.9, 2),  # API price ≈ our discounted price
                        "acebase": round(price, 2),
                    }
                )
        return offers or None
    except Exception as e:
        print(f"  [offgamers] {seo_term}: {e}", file=sys.stderr)
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="print result without writing")
    args = ap.parse_args()

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    games = {}
    for game, terms in SEO_TERMS.items():
        got = None
        for t in terms:
            print(f"  {game}: trying '{t}' …")
            got = offgamers_offers(t)
            if got:
                print(f"  {game}: {len(got)} offers from OffGamers")
                break
            time.sleep(0.4)
        games[game] = got if got else FALLBACK.get(game, [])
        if not got:
            print(f"  {game}: using static fallback ({len(games[game])} tiers)")

    data = {"updated": now, "games": games}
    if args.dry_run:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return

    out = os.path.normpath(OUT)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
