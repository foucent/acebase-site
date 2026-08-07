"""Capture OffGamers PUBG page layout, colors, and screenshot."""
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

URL = "https://www.offgamers.com/product/pubg-mobile-direct-top-up"
ROOT = Path(__file__).resolve().parent


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto(URL, wait_until="networkidle", timeout=120_000)
        await page.wait_for_timeout(5000)

        # dismiss region banner if present
        for sel in [
            "button:has-text(\"Don't show again\")",
            "button:has-text('close')",
            "[aria-label='Close']",
        ]:
            try:
                btn = page.locator(sel).first
                if await btn.count() and await btn.is_visible():
                    await btn.click(timeout=2000)
                    await page.wait_for_timeout(500)
            except Exception:
                pass

        await page.screenshot(path=str(ROOT / "_og_pubg_full.png"), full_page=False)

        styles = await page.evaluate(
            """() => {
            const pick = (el) => {
              if (!el) return null;
              const cs = getComputedStyle(el);
              const r = el.getBoundingClientRect();
              return {
                tag: el.tagName,
                class: el.className,
                text: (el.innerText || '').slice(0, 80),
                x: Math.round(r.x), y: Math.round(r.y),
                w: Math.round(r.width), h: Math.round(r.height),
                bg: cs.backgroundColor,
                color: cs.color,
                fontSize: cs.fontSize,
                fontWeight: cs.fontWeight,
                border: cs.border,
                borderRadius: cs.borderRadius,
                padding: cs.padding,
                margin: cs.margin,
              };
            };
            const q = (s) => document.querySelector(s);
            const qa = (s) => [...document.querySelectorAll(s)].slice(0, 8).map(pick);
            return {
              bodyBg: getComputedStyle(document.body).backgroundColor,
              root: pick(q('#q-app')),
              buyBtn: pick(q('button') && [...document.querySelectorAll('button')].find(b => /buy now/i.test(b.innerText))),
              h1: pick(q('h1')),
              chips: qa('.q-chip, [class*="chip"], [class*="service"]'),
              denoms: qa('button').filter(b => b && /UC/i.test(b.text)),
              productImg: pick(q('img[src*="offer"]')),
              breadcrumb: pick(q('[class*="breadcrumb"], nav')),
              banner: pick([...document.querySelectorAll('*')].find(e => /double-check the product region/i.test(e.innerText || ''))),
              cssLinks: [...document.querySelectorAll('link[rel="stylesheet"]')].map(l => l.href),
            };
          }"""
        )

        html_snippet = await page.evaluate(
            """() => {
            const app = document.querySelector('#q-app');
            return app ? app.innerHTML.slice(0, 25000) : '';
          }"""
        )

        await browser.close()

    (ROOT / "_og_pubg_styles.json").write_text(
        json.dumps(styles, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (ROOT / "_og_pubg_html_snip.html").write_text(html_snippet, encoding="utf-8")
    print("saved styles + screenshot")


if __name__ == "__main__":
    asyncio.run(main())
