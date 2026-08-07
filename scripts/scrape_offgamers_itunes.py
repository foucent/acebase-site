"""Scrape rendered OffGamers iTunes gift card page."""
import asyncio
import json
import re
from pathlib import Path

from playwright.async_api import async_playwright

URL = (
    "https://www.offgamers.com/sg/product/itunes-gift-cards"
    "?region_id=7d30e8c8-dd06-429c-9d14-56025ad62aaf"
)
OUT = Path(__file__).resolve().parent / "_offgamers_itunes_scrape.json"


async def main() -> None:
    captured: list[dict] = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1440, "height": 900})

        async def on_response(resp) -> None:
            url = resp.url
            if resp.status != 200:
                return
            if not any(x in url for x in ("offgamers.com",)):
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
        html = await page.content()

        # grab structured bits if present
        selectors = [
            "h1",
            ".product-title",
            "[class*='product']",
            "[class*='region']",
            "[class*='denomination']",
            "[class*='price']",
        ]
        snippets: dict[str, str] = {}
        for sel in selectors:
            loc = page.locator(sel)
            count = await loc.count()
            if count:
                parts = []
                for i in range(min(count, 20)):
                    try:
                        parts.append((await loc.nth(i).inner_text()).strip())
                    except Exception:
                        pass
                snippets[sel] = "\n---\n".join(p for p in parts if p)

        await browser.close()

    payload = {
        "url": URL,
        "title": title,
        "text": text,
        "snippets": snippets,
        "captured": captured,
        "html_len": len(html),
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("saved", OUT)
    print("title:", title)
    print("text preview:\n", text[:3000])
    print("captured json:", len(captured))
    for c in captured:
        print(" ", c["url"][:140])


if __name__ == "__main__":
    asyncio.run(main())
