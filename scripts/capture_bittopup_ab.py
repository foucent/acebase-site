import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

URL = "https://bittopup.com/zh/goods/Arena-Breakout-Bonds"
OUT = Path(__file__).resolve().parent


async def main() -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        await page.goto(URL, wait_until="domcontentloaded", timeout=90000)
        await page.wait_for_timeout(8000)
        imgs = await page.evaluate(
            """() => [...document.querySelectorAll('img')].map(i => ({src:i.src, alt:i.alt, w:i.width}))"""
        )
        await page.screenshot(path=str(OUT / "_bittopup_ab.png"))
        await browser.close()
    (OUT / "_bittopup_ab_imgs.json").write_text(json.dumps(imgs, ensure_ascii=False, indent=2), encoding="utf-8")
    for i in imgs[:12]:
        print(i)


asyncio.run(main())
