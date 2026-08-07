"""Build apple gift card page data from OffGamers scrape."""
import json
from pathlib import Path

scrape = json.loads(Path("_offgamers_itunes_scrape.json").read_text(encoding="utf-8"))
offers = []
for c in scrape["captured"]:
    if "search/lite" in c["url"] and "7d30e8c8" in c["url"]:
        for group in c["body"]["payload"]["results"]:
            for o in group["offer_results"]:
                offers.append(
                    {
                        "title": o["title"],
                        "price_sgd": o["display_price"],
                        "price_cny": o["unit_price"],
                        "sold_out": o.get("is_sold_out", False),
                        "qty": o.get("available_qty", 0),
                        "offer_id": o["offer_id"],
                    }
                )

# OffGamers UI order from rendered page
order = [
    "CNY 1,000",
    "CNY 648",
    "CNY 500",
    "CNY 200",
    "CNY 100",
    "CNY 300",
    "CNY 68",
    "CNY 50",
    "CNY 30",
    "CNY 20",
    "CNY 15",
    "CNY 12",
    "CNY 10",
    "CNY 6",
]
by_title = {o["title"]: o for o in offers}
ordered = [by_title[t] for t in order if t in by_title]
Path("_apple_offers.json").write_text(
    json.dumps(ordered, ensure_ascii=False, indent=2), encoding="utf-8"
)
print(json.dumps(ordered, ensure_ascii=False, indent=2))
