"""Extract OffGamers PUBG UI token details."""
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

URL = "https://www.offgamers.com/product/pubg-mobile-direct-top-up"
OUT = Path(__file__).resolve().parent / "_og_pubg_tokens.json"


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto(URL, wait_until="networkidle", timeout=120_000)
        await page.wait_for_timeout(4000)

        tokens = await page.evaluate(
            """() => {
            const cs = (el) => el ? getComputedStyle(el) : null;
            const info = (el) => {
              if (!el) return null;
              const s = cs(el);
              const r = el.getBoundingClientRect();
              return {
                text: (el.innerText || '').trim().slice(0, 60),
                class: el.className,
                w: Math.round(r.width), h: Math.round(r.height),
                bg: s.backgroundColor, color: s.color,
                border: s.border, borderRadius: s.borderRadius,
                fontSize: s.fontSize, fontWeight: s.fontWeight,
                boxShadow: s.boxShadow,
              };
            };
            const buttons = [...document.querySelectorAll('button')];
            const ucBtns = buttons.filter(b => /UC/i.test(b.innerText));
            const tabs = [...document.querySelectorAll('[role="tab"], .q-tab')];
            const layout = document.querySelector('.q-layout');
            const mainBg = layout ? cs(layout).background : null;
            const cards = [...document.querySelectorAll('.q-card, [class*="rounded"]')].slice(0, 5);
            return {
              layoutBg: mainBg ? mainBg.background : null,
              bodyClass: document.body.className,
              title: info(document.querySelector('h4, .text-h4')),
              regionChip: info([...document.querySelectorAll('*')].find(e => (e.innerText||'').trim() === 'Global')),
              tabs: tabs.map(info),
              ucFirst: info(ucBtns[0]),
              ucActive: info(ucBtns.find(b => b.classList.contains('active') || b.getAttribute('aria-pressed') === 'true') || ucBtns[6]),
              userId: info(document.querySelector('input')),
              qty: info(document.querySelector('[class*="stepper"], .q-field--outlined')),
              price: info([...document.querySelectorAll('*')].find(e => /USD/.test(e.innerText||'') && e.children.length === 0)),
              buyBtn: info(buttons.find(b => /buy now/i.test(b.innerText))),
              breadcrumb: info([...document.querySelectorAll('*')].find(e => /^Home\\s*\\/\\s*Games$/m.test((e.innerText||'').trim()))),
            };
          }"""
        )
        await browser.close()

    OUT.write_text(json.dumps(tokens, ensure_ascii=False, indent=2), encoding="utf-8")
    print(OUT.read_text(encoding="utf-8")[:3000])


if __name__ == "__main__":
    asyncio.run(main())
