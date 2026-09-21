#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merge the fourteen live-streaming platform tiers into prices.json.

These fourteen platforms moved off the old /games/live-prices/ page onto /topup/
on 2026-09-21, where every card quotes its tiers out of prices.json like the
eighteen cards above it. Each key is also the card's id on /topup and its
brand-plate filename, and the tier order here is the order the rows print in —
the entry tier is the one a shut card shows in red.

The tiers themselves come from scripts/_live_tiers/<slug>.json: the source's own
pages in SGD, captured on 2026-09-10 and NOT re-scraped here. What a re-run
refreshes is the FX — every figure on the page is `sale * today's SGD->USD` — so
the prices move while the denominations stay put. To change which denominations
are on offer, re-run the capture script that wrote those caches first (the
scripts/capture_*.py one for this set) and this second.

A card shows one saving figure, the entry tier's, where it is largest. It is
computed here rather than written onto the card the way the gift cards'
`data-discount` is: that one is the source's own list-price discount and is not
derivable from prices.json at all, while this one is `list` against `ref` and
would go stale on every re-run if it were typed into the page.

Re-run chain, and the order matters: scripts/update_prices.py FIRST, then
merge_giftcard_prices.py and this one. update_prices.py starts from `games = {}`
and rewrites the whole file from its own table, so it drops all twenty-seven
merged keys (and `currency` and `fx`) — running it after this leaves every one of
those cards reading 价格即将上线. After a re-run, bump the cache-busting version
in docs/javascripts/games-prices.js to match UPDATED and the static
.js-prices-updated text on the page, as the last lines here remind you.

Usage:  python scripts/merge_live_prices.py [--keep-fx]
          --keep-fx  convert with the rate already stored in prices.json and
                     skip the lookup — for a data-only re-run, or offline.
"""
import argparse
import datetime
import json
import math
import os
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TL = os.path.join(HERE, "_live_tiers")
PRICES_JSON = os.path.normpath(
    os.path.join(HERE, "..", "docs", "assets", "games", "prices.json"))

# Page order of /topup's third section, which is also the order these print in.
SLUGS = [
    "douyin-top-up", "kwi-top-up", "bigo-live", "mico-top-up", "poppo-live",
    "tango-live-recharge", "mango", "migo-top-up", "superlive", "dazz-top-up",
    "xena-live-group-voice", "bixin-top-up", "ludo-club", "yalla-ludo",
]


def fx_rate(base="SGD", target="USD", keep=False):
    """Today's rate, or the one the last run stored.

    The stored rate is a day old at worst and the source quotes to the cent, so
    reusing it beats being unable to rebuild the data at all — which is exactly
    when someone is offline and still needs to re-merge.
    """
    stored = {}
    if os.path.exists(PRICES_JSON):
        with open(PRICES_JSON, encoding="utf-8") as f:
            stored = (json.load(f).get("fx") or {})
    if keep:
        if stored.get(base) is None:
            raise SystemExit(f"--keep-fx: {PRICES_JSON} 里没有存过 {base} 汇率")
        print(f"--keep-fx: 用已存的 {base}->{target} {stored[base]} "
              f"(as of {stored.get('asOf', '?')})")
        return float(stored[base]), stored.get("asOf", "")
    try:
        url = "https://open.er-api.com/v6/latest/" + base
        with urllib.request.urlopen(url, timeout=30) as r:
            d = json.loads(r.read().decode("utf-8"))
        if d.get("result") != "success":
            raise ValueError(json.dumps(d)[:200])
        return float(d["rates"][target]), d.get("time_last_update_utc", "")
    except Exception as e:
        if stored.get(base) is not None:
            print(f"! FX lookup failed ({e})\n"
                  f"  reusing the rate already in prices.json: {stored[base]} "
                  f"(as of {stored.get('asOf', '?')})")
            return float(stored[base]), stored.get("asOf", "")
        raise


def off_of(ref, lst):
    """The entry tier's saving as the page prints it — "-19%", or None.

    The same arithmetic and the same rounding as the offPill() this replaced in
    live-prices.js: the percentage is read off the already-rounded USD figures,
    and a half goes up. Python's round() takes halves to even instead, which
    would print a different number than the page has shown since 2026-09-10.
    """
    if not (lst and lst > ref):
        return None
    return "-{}%".format(int(math.floor((1 - ref / lst) * 100 + 0.5)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--keep-fx", action="store_true",
        help="skip the lookup and convert with the rate already in prices.json")
    args = ap.parse_args()

    rate, asof = fx_rate(keep=args.keep_fx)
    if not args.keep_fx:
        print(f"FX SGD->USD = {rate}  (as of {asof})")
    updated = datetime.date.today().isoformat()

    with open(PRICES_JSON, encoding="utf-8") as f:
        d = json.load(f)
    d.setdefault("games", {})

    tiers_written = 0
    pills = []
    for slug in SLUGS:
        fp = os.path.join(TL, slug + ".json")
        with open(fp, encoding="utf-8") as f:
            raw = json.load(f)
        tiers = []
        for t in raw["tiers"]:
            if not t.get("sale"):
                continue
            tiers.append({
                "title": t["name"],
                "ref": round(t["sale"] * rate, 2),
                "list": round(t["original"] * rate, 2)
                        if t.get("original") else None,
            })
        if not tiers:
            raise SystemExit(f"{slug}: 没有档位（{fp}）")
        # Cheapest first: the source's DOM order is arbitrary and games-prices.js
        # renders the rows exactly as they are stored, so this sort is the page's
        # sort. It also decides which tier wears the pill.
        tiers.sort(key=lambda r: r["ref"])
        for t in tiers:
            if not isinstance(t["ref"], (int, float)) or t["ref"] <= 0:
                raise SystemExit(f"{slug}/{t['title']}: 价格必须是正数，"
                                 f"实际 {t['ref']!r}")
        # One retail price per tier, so the three columns are the same number.
        # The range columns exist because the game cards are scraped across
        # several channels; a strike price is not a spread and inventing one
        # would put a made-up figure on the page.
        rows = [{"title": t["title"], "lowest": t["ref"], "highest": t["ref"],
                 "average": t["ref"]} for t in tiers]
        off = off_of(tiers[0]["ref"], tiers[0]["list"])
        if off:
            # Entry tier only: a card holds one saving figure and sixteen of
            # them down the ladder is noise. games-prices.js reads it from row
            # zero, the same place it lands here.
            rows[0]["off"] = off
            pills.append(off)
        d["games"][slug] = rows
        tiers_written += len(tiers)
        print(f"  {slug:<24} {len(tiers):>2} 档  入口 {tiers[0]['title']:<16} "
              f"${tiers[0]['ref']:>7.2f}"
              + (f"  (标价 ${tiers[0]['list']:.2f})  {off}" if off else ""))

    # update_prices.py writes only {"updated", "games"} and would drop these two.
    d["currency"] = "USD"
    d["fx"] = {"SGD": round(rate, 6), "asOf": asof}
    d["updated"] = updated

    with open(PRICES_JSON, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"wrote {PRICES_JSON}  ({len(SLUGS)} keys, {tiers_written} tiers, "
          f"updated={updated})")
    print(f"  入口折扣 {len(pills)} 个：{'、'.join(pills)}")
    print(f"!! 记得同步 docs/javascripts/games-prices.js 的版本号 "
          f"-> {updated.replace('-', '')}")


if __name__ == "__main__":
    main()
