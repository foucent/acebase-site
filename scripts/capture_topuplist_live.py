# -*- coding: utf-8 -*-
"""Scrape topuplist live-streaming category products -> tier price JSON.

Writes scripts/_live_tiers/<slug>.json with the native-currency values plus the
product display name, so scripts/build_live_prices.py can convert to the site's
USD base. Source names are never surfaced on the site itself.

topuplist sits behind Cloudflare and ignores any attempt to force a display
currency (the server re-derives it from IP geolocation), so this runs under
playwright_stealth and scrapes whatever currency the edge happens to serve.
"""
import asyncio
import json
import os
import re
import sys
from playwright.async_api import async_playwright
from playwright_stealth import Stealth

CATEGORY = "https://topuplist.com/zh-cn/category/live-streaming"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "_live_tiers")
os.makedirs(OUT, exist_ok=True)

# JS: pull every tier card (name div carries the tier name in its title attr).
PARSE_TIERS = """() => {
  const out = [];
  document.querySelectorAll('div[title]').forEach(el => {
    const name = (el.getAttribute('title') || '').trim();
    if (!name) return;
    const root = el.parentElement;
    if (!root) return;
    const spans = [...root.querySelectorAll('span')];
    const isStrike = s => String(s.className || '').includes('line-through');
    const sale = spans.find(s => !isStrike(s) && /[0-9]/.test(s.textContent));
    const orig = spans.find(s => isStrike(s));
    if (!sale) return;
    const num = t => {
      const m = String(t || '').replace(/,/g, '').match(/[0-9]+[.]?[0-9]*/);
      return m ? parseFloat(m[0]) : null;
    };
    out.push({name: name,
              sale: num(sale.textContent),
              original: orig ? num(orig.textContent) : null});
  });
  return out;
}"""


async def wait_ready(pg, minlen=1500, tries=25):
    for _ in range(tries):
        await pg.wait_for_timeout(1200)
        try:
            if await pg.evaluate("() => document.body.innerText.length") > minlen:
                return True
        except Exception:
            pass
    return False


async def main():
    slugs = sys.argv[1:]
    async with async_playwright() as p:
        b = await p.chromium.launch()
        ctx = await b.new_context(user_agent=UA, viewport={"width": 1440, "height": 1000},
                                  locale="zh-CN", timezone_id="Asia/Hong_Kong")
        await Stealth().apply_stealth_async(ctx)
        pg = await ctx.new_page()

        if not slugs:
            await pg.goto(CATEGORY, wait_until="domcontentloaded", timeout=90000)
            await wait_ready(pg)
            slugs = await pg.evaluate(
                """() => [...new Set([...document.querySelectorAll('a[href*="/product/"]')]
                     .map(a => a.getAttribute('href').split('/product/').pop()))]"""
            )
            print("category:", await pg.title())
            print("slugs:", slugs)

        for slug in slugs:
            fp = os.path.join(OUT, slug + ".json")
            if os.path.exists(fp):
                print("skip (cached):", slug)
                continue
            await pg.goto(f"https://topuplist.com/zh-cn/product/{slug}",
                          wait_until="domcontentloaded", timeout=90000)
            await wait_ready(pg)
            await pg.wait_for_timeout(1200)
            tiers = await pg.evaluate(PARSE_TIERS)
            # de-dup by name, drop non-numeric
            seen, clean = set(), []
            for t in tiers:
                if t["sale"] is None or t["name"] in seen:
                    continue
                seen.add(t["name"])
                clean.append(t)
            meta = await pg.evaluate(
                """() => ({
                  h1: (document.querySelector('h1') || {}).textContent || '',
                  title: document.title
                })"""
            )
            json.dump({"slug": slug, "h1": meta["h1"].strip(), "title": meta["title"],
                       "tiers": clean},
                      open(fp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f"saved {slug:<28} h1={meta['h1'].strip()[:30]!r} tiers={len(clean)}")
        await b.close()


asyncio.run(main())
