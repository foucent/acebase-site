"""Scrape OffGamers PUBG Mobile direct top-up page."""
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright

URL = "https://www.offgamers.com/product/pubg-mobile-direct-top-up"
OUT = Path(__file__).resolve().parent / "_offgamers_pubg_scrape.json"


async def main() -> None:
    captured: list[dict] = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})

        async def on_response(resp) -> None:
            url = resp.url
            if resp.status != 200 or "offgamers.com" not in url:
                return
            ct = resp.headers.get("content-type", "")
            if "json" not in ct and not url.endswith(".json"):
                return
            try:
                body = await resp.json()
            except Exception:
                return
            captured.append({"url": url, "body": body})

        page.on("response", on_response)
        await page.goto(URL, wait_until="networkidle", timeout=120_000)
        await page.wait_for_timeout(8000)

        title = await page.title()
        text = await page.inner_text("body")
        await browser.close()

    payload = {"url": URL, "title": title, "text": text, "captured": captured}
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("saved", OUT)
    print("title:", title)
    print("text preview:\n", text[:4000])
    for c in captured:
        if any(k in c["url"] for k in ("search/lite", "keyword_info", "seo_info", "products/search")):
            print(" ", c["url"][:160])


if __name__ == "__main__":
    asyncio.run(main())
