# -*- coding: utf-8 -*-
"""Build the 直播代储价格参考 page from the scraped topuplist tier JSON.

Reads scripts/_live_tiers/<slug>.json (native currency, written by
capture_topuplist_live.py), converts to the site's USD base via a live FX rate,
writes docs/assets/games/live-prices.json, and regenerates
docs/games/live-prices.md.

The page is one uncrate article per platform — band, name, description, then the
tier ladder as one line per tier. The ladder is fetched by live-prices.js from
the JSON this writes, the same way the per-game pages fetch prices.json, so the
band art is the only thing the markup and the data file both need: it lives at
docs/assets/games/brand/<slug>.png.

Source names never appear on the site.

Usage:  python scripts/build_live_prices.py [--keep-date]
          --keep-date  stamp the page with the date already in
                       live-prices.json. Use it when only the layout changed.
Then:   python -m mkdocs build
"""
import argparse
import datetime
import json
import os
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TL = os.path.join(HERE, "_live_tiers")
SITE = os.path.dirname(HERE)
OUT_JSON = os.path.join(SITE, "docs", "assets", "games", "live-prices.json")
OUT_MD = os.path.join(SITE, "docs", "games", "live-prices.md")

# slug -> (display name, pill label, badge, Chinese description)
PRODUCTS = [
    ("douyin-top-up", "抖音直播", "抖音", "直播",
     "抖音是国内头部的短视频与直播平台，抖币用于直播打赏与送礼。"),
    ("kwi-top-up", "快手", "快手", "直播",
     "快手是国内头部的短视频与直播平台，快币用于直播打赏与购买礼物。"),
    ("bigo-live", "Bigo Live", "Bigo Live", "直播",
     "Bigo Live 是全球流行的直播社交平台，Diamonds 用于购买礼物打赏主播。"),
    ("mico-top-up", "MICO", "MICO", "社交直播",
     "MICO 是面向全球的社交与直播平台，平台币用于互动与礼物打赏。"),
    ("poppo-live", "Poppo Live", "Poppo Live", "直播",
     "Poppo Live 是主打视频直播与语音房的社交平台，Coins 用于送礼与互动。"),
    ("tango-live-recharge", "Tango Live", "Tango Live", "直播",
     "Tango Live 是全球化的视频直播平台，金币用于打赏主播与解锁互动特效。"),
    ("mango", "Mango Live", "Mango Live", "直播",
     "Mango Live 是全球化的视频直播平台，Diamonds 用于购买礼物打赏主播。"),
    ("migo-top-up", "MIGO LIVE", "MIGO LIVE", "直播",
     "MIGO LIVE 是全球化的直播社交平台，金币用于打赏主播与房间互动。"),
    ("superlive", "超级直播", "超级直播", "直播",
     "超级直播是面向东南亚市场的直播社交平台，金币用于礼物打赏与互动。"),
    ("dazz-top-up", "Dazz Live", "Dazz Live", "直播",
     "Dazz Live 是主打语音房与视频直播的社交平台，Coins 用于互动与送礼物。"),
    ("xena-live-group-voice", "Xena Live：群组语音", "Xena Live", "语音",
     "Xena Live 以群组语音房为核心玩法，Coins 用于房间互动与礼物。"),
    ("bixin-top-up", "比心", "比心", "陪玩社交",
     "比心是游戏陪玩与语音社交平台，比心币与比心钻石用于下单陪玩与互动。"),
    ("ludo-club", "Ludo Club", "Ludo Club", "休闲游戏",
     "Ludo Club 是线上飞行棋休闲游戏，Cash 用于购买骰子与游戏道具。"),
    ("yalla-ludo", "Yalla Ludo", "Yalla Ludo", "休闲游戏",
     "Yalla Ludo 是中东地区流行的飞行棋与语音房应用，Diamonds 与 Gold 用于道具与互动。"),
]


def fx_rate(base="SGD", target="USD"):
    """Today's rate, or the one the last run stored.

    The stored rate is a day old at worst and the tiers are quoted to the cent,
    so reusing it beats being unable to rebuild the page at all — which is
    exactly when the layout is being changed and someone needs to look at it.
    """
    try:
        url = "https://open.er-api.com/v6/latest/" + base
        with urllib.request.urlopen(url, timeout=30) as r:
            d = json.loads(r.read().decode("utf-8"))
        if d.get("result") != "success":
            raise ValueError(json.dumps(d)[:200])
        return float(d["rates"][target]), d.get("time_last_update_utc", "")
    except Exception as e:
        if os.path.exists(OUT_JSON):
            fx = (json.load(open(OUT_JSON, encoding="utf-8")).get("fx") or {})
            if fx.get(base) is not None:
                print(f"! FX lookup failed ({e})\n"
                      f"  reusing the rate already in live-prices.json: "
                      f"{fx[base]} (as of {fx.get('asOf', '?')})")
                return float(fx[base]), fx.get("asOf", "")
        raise


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--keep-date", action="store_true",
        help="rebuild the page from the figures already converted in "
             "live-prices.json and leave that file alone — for a layout change "
             "that does not refresh the tiers")
    args = ap.parse_args()

    if args.keep_date:
        # A layout change must not reprice anything. Re-running the conversion
        # would apply today's FX rate to tiers scraped on an earlier date, which
        # moves every figure on the page while the data behind it is unchanged.
        if not os.path.exists(OUT_JSON):
            raise SystemExit("--keep-date needs an existing " + OUT_JSON)
        with open(OUT_JSON, encoding="utf-8") as f:
            data = json.load(f)
        today = data["updated"]
        print(f"reusing live-prices.json as written ({today}) — tiers untouched")
    else:
        rate, asof = fx_rate()
        print(f"FX SGD->USD = {rate}  (as of {asof})")
        today = datetime.date.today().isoformat()

        products = {}
        for slug, name, pill, badge, note in PRODUCTS:
            fp = os.path.join(TL, slug + ".json")
            with open(fp, encoding="utf-8") as f:
                raw = json.load(f)
            tiers = []
            for t in raw["tiers"]:
                if not t.get("sale"):
                    continue
                tiers.append({
                    "title": t["name"],
                    "ref": round(t["sale"] * rate, 2),
                    "list": round(t["original"] * rate, 2) if t.get("original") else None,
                })
            if not tiers:
                raise SystemExit("no tiers for " + slug)
            # Cheapest tier first — the source's DOM order is arbitrary.
            tiers.sort(key=lambda r: r["ref"])
            products[slug] = {
                "name": name, "pill": pill, "badge": badge, "note": note,
                "tiers": tiers,
            }
            print(f"  {slug:<24} {len(tiers):>2} 档  cheap={tiers[0]['title']} "
                  f"{tiers[0]['ref']} (list {tiers[0]['list']})")

        data = {
            "updated": today,
            "currency": "USD",
            "fx": {"SGD": round(rate, 6), "asOf": asof},
            "products": products,
        }
        with open(OUT_JSON, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
        print("wrote", OUT_JSON)

    products = data["products"]

    total = len(products)
    pills = "\n".join(
        f'    <a href="#{slug}">{products[slug]["pill"]}</a>'
        for slug, _n, _p, _b, _d in PRODUCTS
    )

    def cta_name(n):
        # Space before 充值 only for Latin-ending names ("Bigo Live 充值" but
        # "抖音直播充值"), matching CJK typesetting.
        return n + (" " if n[-1].isascii() and n[-1].isalnum() else "")

    articles = []
    for i, (slug, name, pill, badge, note) in enumerate(PRODUCTS):
        # The first band is the one above the fold, so it is fetched eagerly;
        # the other thirteen are lazy. Asking for an image to be both high
        # priority and lazy is a contradiction, and lazy wins.
        attrs = ' fetchpriority="high"' if i == 0 else ' loading="lazy"'
        articles.append(f"""  <article class="ab-hero ab-hero--article ab-hero--brand" id="{slug}">
    <div class="ab-hero__media">
      <img src="/assets/games/brand/{slug}.png" alt="{name} 代储价格参考"{attrs} decoding="async">
    </div>
    <div class="ab-hero__copy">
      <p class="ab-cat"><a href="/games/live-prices/">直播代储价格参考</a></p>
      <h2 class="ab-hero__title">{name}</h2>
      <p class="ab-hero__excerpt">{note}</p>

      <p class="ab-ec-list" data-product="{slug}">
        <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
      </p>

      <p class="ab-ec-foot">{badge} &middot; 数据更新于 {today} &middot; 报价以在线咨询为准</p>

      <p class="ab-hero__more">
        <a class="ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询{cta_name(pill)}充值的实时价格。">实时价格咨询</a>
      </p>
    </div>
  </article>""")

    # The ladder itself is fetched, but its endpoints are known here. Putting
    # them in the static HTML as an AggregateOffer is how a crawler gets to read
    # a price at all — the alternative is that every figure on this page lives
    # only in the browser.
    def offers(slug):
        tiers = products[slug]["tiers"]
        return (f'"offers": {{ "@type": "AggregateOffer", "priceCurrency": "USD", '
                f'"lowPrice": "{tiers[0]["ref"]:.2f}", '
                f'"highPrice": "{tiers[-1]["ref"]:.2f}", '
                f'"offerCount": "{len(tiers)}", '
                f'"availability": "https://schema.org/InStock" }}')

    items = ",\n".join(
        '        {{ "@type": "Product", "position": {}, "name": "{}", '
        '"url": "https://acebase.cc/games/live-prices/#{}", {} }}'
        .format(i + 1, name, slug, offers(slug))
        for i, (slug, name, _p, _b, _d) in enumerate(PRODUCTS)
    )

    md = f"""---
title: 直播代储价格参考 | 直播与语音平台充值行情
description: AceBase 直播代储价格参考 —— 汇总抖音、快手、Bigo Live、MICO、Poppo Live 等 {total} 个直播与语音社交平台的各档位充值参考价（美元计价）。数据更新至 {today}。
hide:
  - title
  - toc
---

<div class="ab-mag" markdown="0" data-prices-ver="{today}">

  <section class="ab-section">
    <header class="ab-section__head">
      <span class="ab-stamp" aria-hidden="true">更新于 {today}</span>
      <h1 class="ab-section__title">直播代储价格参考</h1>
    </header>
    <p class="ab-section__lead">覆盖 {total} 个直播、语音与社交平台 —— 逐个列出该平台当前在售的全部充值档位与参考价（美元计价，持续更新）。</p>
    <div class="mg-gpu-models" role="navigation" aria-label="已收录平台">
{pills}
    </div>
  </section>

{chr(10).join(articles)}

</div>

<div class="admonition note mg-games__note">
  <p class="admonition-title">相关</p>
  <p><a href="/games/topup-prices/">代储价格参考</a> &middot; <a href="/games/gpu-prices/">显卡价格参考</a> &middot; <a href="/gift-cards/">礼品卡</a> &middot; <a href="/gallery/">画廊</a></p>
</div>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "WebPage",
      "name": "直播代储价格参考",
      "description": "AceBase 直播代储价格参考，覆盖 {total} 个直播、语音与社交平台的各档位充值参考价。数据更新至 {today}。",
      "url": "https://acebase.cc/games/live-prices/"
    }},
    {{
      "@type": "ItemList",
      "name": "直播代储价格参考 · 直播与语音平台充值",
      "numberOfItems": "{total}",
      "itemListElement": [
{items}
      ]
    }},
    {{
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "首页", "item": "https://acebase.cc/" }},
        {{ "@type": "ListItem", "position": 2, "name": "直播代储价格参考", "item": "https://acebase.cc/games/live-prices/" }}
      ]
    }}
  ]
}}
</script>
"""
    with open(OUT_MD, "w", encoding="utf-8", newline="\n") as f:
        f.write(md)
    print("wrote", OUT_MD, f"({total} articles)")


main()
