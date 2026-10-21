# -*- coding: utf-8 -*-
"""Scrape topuplist's entertainment catalog + per-product tiers via its JSON API.

Same harness as capture_topuplist_game.py: the category page itself 404s and a
bare HTTP client gets challenged, so the fetch runs inside a real browser page,
same-origin, carrying the session cookies (user_currency=USD). With lang=en the
tier names come back in English and the prices in USD — no FX step downstream.

Writes scripts/_ent_tiers/_catalog.json (all 44, in the site's order) and one
<slug>.json per fetched product. Only the slugs in merge_ent_prices.ENTERTAINMENT
are fetched; --force re-fetches a cached one.

    python scripts/capture_topuplist_entertainment.py [slug ...] [--force]
"""
import asyncio
import json
import os
import sys

from playwright.async_api import async_playwright
from playwright_stealth import Stealth

BASE = "https://topuplist.com"
API = BASE + "/api/user/products"
CATEGORY = "entertainment"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "_ent_tiers")
os.makedirs(OUT, exist_ok=True)

FETCH_JSON = """async (url) => {
  const r = await fetch(url, {headers: {'accept': 'application/json'}, credentials: 'same-origin'});
  const text = await r.text();
  let data = null;
  try { data = JSON.parse(text); } catch (e) {}
  return {status: r.status, data: data, head: text.slice(0, 120)};
}"""


async def get(pg, url, tries=3):
    for n in range(tries):
        res = await pg.evaluate(FETCH_JSON, url)
        if res["status"] == 200 and res["data"] is not None:
            return res["data"]
        print("   ! %s -> %s %r" % (url.split("?")[-1][:60], res["status"], res["head"]))
        await pg.wait_for_timeout(4000 * (n + 1))
    raise SystemExit("API kept failing: %s" % url)


def selected():
    """The 30 keys the page shows, imported from the merge table."""
    sys.path.insert(0, HERE)
    import merge_ent_prices as m
    return [p["slug"] for p in m.ENTERTAINMENT]


async def main():
    want = [a for a in sys.argv[1:] if not a.startswith("-")]
    force = "--force" in sys.argv
    keep = selected()

    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(user_agent=UA, viewport={"width": 1440, "height": 1000},
                                  locale="en-US", timezone_id="Asia/Hong_Kong")
        await Stealth().apply_stealth_async(ctx)
        pg = await ctx.new_page()
        await pg.goto(BASE + "/en", wait_until="domcontentloaded", timeout=90000)
        await pg.wait_for_timeout(2500)
        print("title:", await pg.title())

        # ---- catalog: every page of the category
        items, page, last = [], 1, 1
        while page <= last:
            data = await get(pg, "%s?category_slug=%s&lang=en&page=%d&per_page=21"
                             % (API, CATEGORY, page))
            meta = data.get("meta") or {}
            last = int(meta.get("last_page") or 1)
            for it in data.get("data") or []:
                items.append({
                    "slug": it.get("slug"), "name": it.get("name"),
                    "sku_name": it.get("sku_name"), "price": it.get("price"),
                    "original_price": it.get("original_price"),
                    "off": it.get("max_discount_percent"),
                    "type": it.get("type"), "image": it.get("image"),
                    "rating": it.get("avg_rating"), "reviews": it.get("review_count"),
                    "order": len(items) + 1,
                })
            print("   page %d/%d: +%d (total %d)"
                  % (page, last, len(data.get("data") or []), len(items)))
            page += 1
            await pg.wait_for_timeout(1500)
        json.dump({"category": CATEGORY, "count": len(items), "items": items},
                  open(os.path.join(OUT, "_catalog.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)

        # ---- tiers: explicit argv, else every selected slug
        slugs = want or keep
        unknown = [s for s in slugs if s not in keep]
        if unknown:
            raise SystemExit("not in ENTERTAINMENT: %s" % unknown)
        for slug in slugs:
            fp = os.path.join(OUT, slug + ".json")
            if os.path.exists(fp) and not force:
                print("skip (cached):", slug)
                continue
            data = await get(pg, "%s/%s?lang=en" % (API, slug))
            d = data.get("data") or {}
            skus = []
            for s in d.get("skus") or []:
                price = s.get("price")
                if price is None:
                    continue
                coupon = s.get("coupon_discount_amount") or 0
                skus.append({
                    "name": (s.get("name") or "").strip(),
                    "price": round(float(price) - float(coupon), 2),
                    "original": s.get("original_price"),
                    "stock": s.get("stock"),
                })
            json.dump({"slug": slug, "name": d.get("name"), "currency": "USD",
                       "skus": skus},
                      open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print("saved %-26s %-28s tiers=%d"
                  % (slug, str(d.get("name"))[:28].encode("ascii", "replace").decode(),
                     len(skus)))
            await pg.wait_for_timeout(1200)
        await b.close()


asyncio.run(main())
