# -*- coding: utf-8 -*-
"""Scrape topuplist's game top-up catalog + per-product tiers via its JSON API.

The site is Nuxt behind Cloudflare: the listing page only renders 21 of 105
products, and a bare request to /api/user/products is challenged. Going through
a real browser context fixes both — the fetch runs same-origin with the session
cookies the site itself set (user_country_code=US, user_currency=USD), so the
prices come back in USD and, with lang=en, the tier names come back in English.
No FX conversion and no Chinese-to-English mapping downstream.

Displayed price = skus[].price - skus[].coupon_discount_amount (the API's
`price` is the pre-coupon figure; the rendered product page subtracts the
coupon). The listing's own `price` field is already net.

Writes scripts/_game_tiers/_catalog.json (all 105, in the site's order) and
scripts/_game_tiers/<slug>.json (one per fetched product).
"""
import asyncio
import json
import os
import sys

from playwright.async_api import async_playwright
from playwright_stealth import Stealth

BASE = "https://topuplist.com"
API = BASE + "/api/user/products"
CATEGORY = "game-top-up"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "_game_tiers")
os.makedirs(OUT, exist_ok=True)

# Same-origin fetch from inside the page: carries cookies, survives the bot check
# that rejects a bare HTTP client after a couple of requests.
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
        print(f"   ! {url.split('?')[-1][:60]} -> {res['status']} {res['head']!r}")
        await pg.wait_for_timeout(4000 * (n + 1))
    raise SystemExit(f"API kept failing: {url}")


async def main():
    want = [a for a in sys.argv[1:] if not a.startswith("-")]
    force = "--force" in sys.argv

    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(user_agent=UA, viewport={"width": 1440, "height": 1000},
                                  locale="en-US", timezone_id="Asia/Hong_Kong")
        await Stealth().apply_stealth_async(ctx)
        pg = await ctx.new_page()
        await pg.goto(f"{BASE}/en/category/{CATEGORY}", wait_until="domcontentloaded",
                      timeout=90000)
        await pg.wait_for_timeout(2500)
        print("title:", await pg.title())

        # ---- catalog: every page of the category
        items, page, last = [], 1, 1
        while page <= last:
            data = await get(pg, f"{API}?category_slug={CATEGORY}&lang=en&page={page}&per_page=21")
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
            print(f"   page {page}/{last}: +{len(data.get('data') or [])} (total {len(items)})")
            page += 1
            await pg.wait_for_timeout(1500)
        json.dump({"category": CATEGORY, "count": len(items), "items": items},
                  open(os.path.join(OUT, "_catalog.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)

        if "--catalog-only" in sys.argv:
            await b.close()
            return

        # ---- tiers: explicit argv, else every product in the catalog
        slugs = want or [it["slug"] for it in items]
        for slug in slugs:
            fp = os.path.join(OUT, slug + ".json")
            if os.path.exists(fp) and not force:
                print("skip (cached):", slug)
                continue
            data = await get(pg, f"{API}/{slug}?lang=en")
            d = data.get("data") or {}
            skus = []
            for s in d.get("skus") or []:
                price = s.get("price")
                coupon = s.get("coupon_discount_amount") or 0
                if price is None:
                    continue
                skus.append({
                    "name": (s.get("name") or "").strip(),
                    "price": round(float(price) - float(coupon), 2),
                    "original": s.get("original_price"),
                    "stock": s.get("stock"),
                })
            json.dump({"slug": slug, "name": d.get("name"), "currency": "USD",
                       "skus": skus},
                      open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f"saved {slug:<32} {str(d.get('name'))[:30]:<30} tiers={len(skus)}")
            await pg.wait_for_timeout(1200)
        await b.close()


asyncio.run(main())
