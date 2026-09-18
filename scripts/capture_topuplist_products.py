#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capture each topuplist gift-card product page: lowest tier price + denominations."""
import asyncio
import json
import re
from pathlib import Path

from playwright.async_api import async_playwright

SLUGS = [
    "jawaker-gift-card",
    "kammelna-gift-card",
    "amazon-gift-card",
    "netflix-gift-card",
    "xbox-live",
    "apple-gift-card",
    "google-play",
]
BASE = "https://topuplist.com/zh-cn/product/"
OUT = Path(__file__).resolve().parent


async def one(page, slug) -> dict:
    url = BASE + slug
    await page.goto(url, wait_until="domcontentloaded", timeout=90000)
    await page.wait_for_timeout(6000)
    # scroll to reveal tiers
    for _ in range(6):
        await page.mouse.wheel(0, 1200)
        await page.wait_for_timeout(500)
    await page.wait_for_timeout(1500)
    data = await page.evaluate(
        """() => {
          const out = { h1: (document.querySelector('h1')||{}).innerText || '',
                        title: document.title,
                        html: document.documentElement.innerText };
          return out;
        }"""
    )
    text = data["html"]
    # keep only the region around denomination-like lines (numbers + price)
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    return {
        "slug": slug,
        "title": data["title"],
        "h1": data["h1"],
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
                print(f"[{slug}] title={r['title'][:50]!r} h1={r['h1'][:40]!r} lines={len(r['lines'])}")
            except Exception as e:
                print(f"[{slug}] ERROR {e}")
                results.append({"slug": slug, "error": str(e)})
        await browser.close()
    (OUT / "_topuplist_products.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("saved", len(results), "products")


asyncio.run(main())
