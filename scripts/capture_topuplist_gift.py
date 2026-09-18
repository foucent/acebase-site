#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Capture topuplist gift-cards category page via Playwright (403 to curl)."""
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

URL = "https://topuplist.com/zh-cn/category/gift-cards"
OUT = Path(__file__).resolve().parent


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto(URL, wait_until="domcontentloaded", timeout=90000)
        await page.wait_for_timeout(10000)
        # scroll to trigger lazy loading
        for _ in range(8):
            await page.mouse.wheel(0, 1500)
            await page.wait_for_timeout(800)
        await page.wait_for_timeout(3000)
        html = await page.content()
        (OUT / "_topuplist_gift.html").write_text(html, encoding="utf-8")
        await page.screenshot(path=str(OUT / "_topuplist_gift.png"), full_page=True)
        # structured extraction: product links + names + prices + imgs
        data = await page.evaluate(
            """() => {
              const out = [];
              const seen = new Set();
              document.querySelectorAll('a[href*="product"]').forEach(a => {
                const href = a.href;
                if (seen.has(href)) return;
                const img = a.querySelector('img');
                const text = (a.innerText || '').replace(/\\n+/g, ' | ').trim();
                const title = (a.getAttribute('title') || a.getAttribute('aria-label') || '').trim();
                if (!text && !title) return;
                seen.add(href);
                out.push({
                  href,
                  title,
                  text,
                  img: img ? img.src : '',
                  imgAlt: img ? img.alt : ''
                });
              });
              return out;
            }"""
        )
        (OUT / "_topuplist_gift.json").write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"captured {len(data)} product cards")
        for d in data[:8]:
            print(f"  {d['title'][:60]} | {d['text'][:90]}")
        await browser.close()


asyncio.run(main())
