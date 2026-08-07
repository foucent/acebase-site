"""Scrape BitTopup Arena Breakout Bonds page."""
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

URL = "https://bittopup.com/zh/goods/Arena-Breakout-Bonds"
OUT = Path(__file__).resolve().parent / "_bittopup_ab_scrape.json"


async def main() -> None:
    captured = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})
        page.on(
            "response",
            lambda resp: captured.append({"url": resp.url, "status": resp.status})
            if resp.status == 200 and "json" in (resp.headers.get("content-type") or "")
            else None,
        )
        await page.goto(URL, wait_until="networkidle", timeout=120_000)
        await page.wait_for_timeout(6000)
        title = await page.title()
        text = await page.inner_text("body")
        html = await page.content()
        await page.screenshot(path=str(OUT.with_suffix(".png")), full_page=False)
        await browser.close()

    OUT.write_text(
        json.dumps({"url": URL, "title": title, "text": text[:12000], "html_len": len(html)}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("saved", OUT)
    print("title:", title)
    print(text[:3500])


if __name__ == "__main__":
    asyncio.run(main())
