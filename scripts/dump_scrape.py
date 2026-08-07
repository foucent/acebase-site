import json
from pathlib import Path

data = json.loads(Path("_offgamers_itunes_scrape.json").read_text(encoding="utf-8"))
lines = []
for c in data["captured"]:
    url = c["url"]
    if any(x in url for x in ("search", "seo_info", "lite", "product_settings", "keyword_info")):
        lines.append(f"=== {url}\n")
        lines.append(json.dumps(c["body"], ensure_ascii=False, indent=2))
        lines.append("\n\n")
Path("_offgamers_itunes_products.txt").write_text("".join(lines), encoding="utf-8")
print("done", len(lines))
