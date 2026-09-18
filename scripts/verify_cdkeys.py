#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Playwright verification of the gift-cards + cdkeys grids on acebase site."""
import asyncio
import sys

from playwright.async_api import async_playwright

URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8006/gift-cards/"


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 1600})
        errors = []
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        page.on("pageerror", lambda e: errors.append(str(e)))
        await page.goto(URL, wait_until="networkidle", timeout=60000)
        await page.wait_for_timeout(1500)

        n_grids = await page.evaluate("document.querySelectorAll('.mg-preowned-grid--giftcards').length")
        print("grids:", n_grids)

        cards = await page.evaluate(
            """() => Array.from(document.querySelectorAll('.mg-preowned-grid--giftcards')).map((g, gi) => ({
                grid: gi,
                count: g.querySelectorAll('.mg-preowned-card').length,
                cards: Array.from(g.querySelectorAll('.mg-preowned-card')).map(c => ({
                  title: (c.querySelector('.mg-preowned-card__title')||{}).textContent,
                  hasMedia: !!c.querySelector('.mg-preowned-card__media img'),
                  hasBadge: (c.querySelector('.mg-preowned-card__badge')||{}).textContent || '',
                  opts: (c.querySelector('.mg-preowned-card__opts-select')||{}).options
                      ? c.querySelector('.mg-preowned-card__opts-select').options.length : 0,
                  price: (c.querySelector('.mg-preowned-card__price')||{}).textContent || '',
                  discount: (c.querySelector('.mg-preowned-card__price .mg-gc-off')||{}).textContent || '',
                  cartName: (c.querySelector('.mg-preowned-card__cart')||{}).getAttribute('data-name') || '',
                  cartPrice: (c.querySelector('.mg-preowned-card__cart')||{}).getAttribute('data-price') || ''
                }))
              }))"""
        )
        for g in cards:
            print(f"--- grid {g['grid']}: {g['count']} cards ---")
            for c in g["cards"]:
                print(
                    f"  {c['title']} | media={c['hasMedia']} badge={c['hasBadge']} "
                    f"opts={c['opts']} price={c['price']!r} off={c['discount']!r} "
                    f"cart={c['cartName']} @ {c['cartPrice']}"
                )

        # Interaction: change a denomination on a cdkeys card and check price + cart update
        interact = await page.evaluate(
            """() => {
              const cards = document.querySelectorAll('.mg-preowned-grid--giftcards .mg-preowned-card');
              const target = Array.from(cards).find(c => /Fortnite/.test(c.textContent));
              if (!target) return {err: 'no fortnite card'};
              const sel = target.querySelector('.mg-preowned-card__opts-select');
              const priceEl = target.querySelector('.mg-preowned-card__price');
              const btn = target.querySelector('.mg-preowned-card__cart');
              sel.value = '5000 V-Bucks';
              sel.dispatchEvent(new Event('change', {bubbles: true}));
              return {
                sel: sel.value,
                opts: sel.options.length,
                price: priceEl.textContent,
                cartName: btn.getAttribute('data-name'),
                cartPrice: btn.getAttribute('data-price'),
                aria: btn.getAttribute('aria-label')
              };
            }"""
        )
        print("fortnite select 5000 V-Bucks ->", interact)

        # USD is the only currency shown, and the header carries no switcher.
        currency = await page.evaluate(
            """() => {
              const c = document.querySelector('.mg-preowned-grid--giftcards .mg-preowned-card .mg-preowned-card__price');
              return {
                price: (c || {}).textContent || '',
                switcher: !!document.querySelector('#ab-currency-select'),
                legacy: typeof window.AceBaseCurrency
              };
            }"""
        )
        print("currency ->", currency)

        print("console errors:", errors if errors else "none")


asyncio.run(main())
