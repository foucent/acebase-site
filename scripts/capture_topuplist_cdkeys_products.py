#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capture each topuplist cdkeys product page: tiers + prices + full-size image."""
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

SLUGS = [
    "fortnite-card",
    "apex-legends",
    "playstation",
    "pubg-gcoins",
    "ns-membership",
    "nintendo-eshop",
    "steam-wallet",
    "gocash-card",
]
BASE = "https://topuplist.com/zh-cn/product/"
OUT = Path(__file__).resolve().parent


async def one(page, slug) -> dict:
    url = BASE + slug
    await page.goto(url, wait_until="domcontentloaded", timeout=90000)
    await page.wait_for_timeout(6000)
    for _ in range(6):
        await page.mouse.wheel(0, 1200)
        await page.wait_for_timeout(500)
    await page.wait_for_timeout(1500)
    data = await page.evaluate(
        """() => {
          const img = document.querySelector('h1') || document.body;
          const og = document.querySelector('meta[property="og:image"]');
          return {
            h1: (document.querySelector('h1')||{}).innerText || '',
            title: document.title,
            ogImage: og ? og.content : '',
            html: document.documentElement.innerText
          };
        }"""
    )
    lines = [l.strip() for l in data["html"].splitlines() if l.strip()]
    return {
        "slug": slug,
        "title": data["title"],
        "h1": data["h1"],
        "ogImage": data["ogImage"],
        "lines": lines,
    }


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        results = []
        for slug in SLUGS:
            try:
                r = await one(page, slug)
                results.append(r)
                print(f"[{slug}] h1={r['h1'][:40]!r} lines={len(r['lines'])}")
            except Exception as e:
                print(f"[{slug}] ERROR {e}")
                results.append({"slug": slug, "error": str(e)})
        await browser.close()
    (OUT / "_topuplist_cdkeys_products.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("saved", len(results), "products")


asyncio.run(main())
