import json
from pathlib import Path

data = json.loads(Path("_offgamers_pubg_scrape.json").read_text(encoding="utf-8"))
lines = []
for c in data["captured"]:
    url = c["url"]
    if any(x in url for x in ("search/lite", "keyword_info", "seo_info", "products/search")):
        lines.append(f"=== {url}\n")
        lines.append(json.dumps(c["body"], ensure_ascii=False, indent=2)[:12000])
        lines.append("\n\n")
Path("_offgamers_pubg_products.txt").write_text("".join(lines), encoding="utf-8")

# extract offers
for c in data["captured"]:
    if "search/lite" in c["url"]:
        offers = []
        for group in c["body"]["payload"]["results"]:
            for o in group["offer_results"]:
                offers.append({
                    "title": o["title"],
                    "price": o["display_price"],
                    "currency": o["display_currency"],
                    "sold_out": o.get("is_sold_out", False),
                    "qty": o.get("available_qty", 0),
                })
        print(json.dumps(offers, ensure_ascii=False, indent=2))
