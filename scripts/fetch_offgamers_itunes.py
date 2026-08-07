"""Fetch OffGamers iTunes gift card page data via public JSON assets."""
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGION_ID = "7d30e8c8-dd06-429c-9d14-56025ad62aaf"
SEO = "itunes-gift-cards"
SERVICE_ID = "fdf75033-56ee-4ce6-929c-1f9c93a4c642"
BRAND_ID = "9853ae0e-2a86-44de-870d-c1896f54b602"


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def main() -> None:
    categories = json.loads(fetch("https://assets.offgamers.com/offer/categories.json?v=2"))
    entry = categories.get(SEO, {})
    print("category entry:", json.dumps(entry, ensure_ascii=False, indent=2))

    blob = json.dumps(categories, ensure_ascii=False)
    if REGION_ID in blob:
        idx = blob.index(REGION_ID)
        print("region context:", blob[max(0, idx - 200) : idx + 400])
    else:
        print("region_id not in categories.json")

    # probe common offer asset paths
    candidates = [
        f"https://assets.offgamers.com/offer/{SEO}.json?v=2",
        f"https://assets.offgamers.com/offer/{SEO}/{REGION_ID}.json?v=2",
        f"https://assets.offgamers.com/offer/regions/{REGION_ID}.json?v=2",
        f"https://assets.offgamers.com/offer/{SERVICE_ID}_{BRAND_ID}.json?v=2",
        f"https://assets.offgamers.com/offer/{SERVICE_ID}_{BRAND_ID}/{REGION_ID}.json?v=2",
        f"https://assets.offgamers.com/offer/products/{SEO}.json?v=2",
        f"https://assets.offgamers.com/offer/products/{SEO}/{REGION_ID}.json?v=2",
    ]
    for url in candidates:
        try:
            data = fetch(url)
            out = ROOT / "_og_probe.json"
            out.write_bytes(data)
            print("OK", url, "bytes", len(data))
            try:
                parsed = json.loads(data)
                print("  keys:", list(parsed.keys())[:10] if isinstance(parsed, dict) else type(parsed))
            except json.JSONDecodeError:
                print("  not json:", data[:120])
        except Exception as exc:
            print("FAIL", url, exc)

    # search vue app bundle for API patterns
    app_url = "https://static.offgamers.com/OffGamers/assetsvue20260728165631/js/offgamers-vue-app.js"
    app = fetch(app_url).decode("utf-8", errors="ignore")
    patterns = sorted(set(re.findall(r"assets\.offgamers\.com/offer/[a-zA-Z0-9_./?=-]+", app)))
    print("offer paths in app.js:", len(patterns))
    for p in patterns[:30]:
        print(" ", p)


if __name__ == "__main__":
    main()
