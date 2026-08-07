#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the 5 top-up game hub pages (pubg-mobile, pubg-gcoin, cod-cold-war,
honor-of-kings, arena-breakout) using the CS2 game-page template."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(HERE, "..", "docs")
PRICES = os.path.join(DOCS, "assets", "games", "prices.json")


def page(slug, name, hero_img, game_key, topup_url, lead, section_title,
         price_title, streamers, news, faq, related, lo, hi):
    s_html = ""
    for sn, smeta, sslug in streamers:
        s_html += (
            f'      <a class="mg-games__streamer" href="https://www.twitch.tv/{sn.lower()}" rel="noopener">\n'
            f'        <span class="mg-games__streamer-avatar"><img src="/assets/games/streamers/{sslug}.svg" alt="{sn}" width="64" height="64" loading="lazy"></span>\n'
            f'        <span class="mg-games__streamer-name">{sn}</span>\n'
            f'        <span class="mg-games__streamer-meta">{smeta}</span>\n'
            f'      </a>\n'
        )
    n_html = ""
    for d, t in news:
        n_html += (
            f'      <li class="mg-games__news-item">\n'
            f'        <span class="mg-games__news-date">{d}</span>\n'
            f'        <a href="https://liquipedia.net/" rel="noopener">{t}</a>\n'
            f'      </li>\n'
        )
    q_items = []
    for q, a in faq:
        q_items.append(
            '        { "@type": "Question", "name": "%s", '
            '"acceptedAnswer": { "@type": "Answer", "text": "%s" } },'
            % (q, a)
        )
    q_html = "\n".join(q_items).rstrip(",")

    return """---
title: %s Top-Up & Discounts
description: Best %s discount top-up, esports news and top Twitch streamers. Compare official vs AceBase prices and top up via live chat.
hide:
  - title
  - toc
---

<div class="mg-games" markdown="0">

  <section class="mg-games__hero" style="--mg-games-hero-image: url('/assets/games/%s')">
    <div class="mg-games__hero-body">
      <p class="mg-games__brand">AceBase</p>
      <h1 class="mg-games__title">%s Top-Up &amp; Discounts</h1>
      <p class="mg-games__lead">%s</p>
      <div class="mg-games__actions">
        <a class="mg-games__btn mg-games__btn--primary" href="%s">Discount Top-Up</a>
        <a class="mg-games__btn mg-games__btn--ghost" href="https://t.me/Acebase_cc" rel="noopener">Squad / Boost</a>
      </div>
    </div>
  </section>

  <section class="mg-games__prices" id="prices">
    <div class="mg-games__section-head">
      <h2 class="mg-games__section-title">%s</h2>
      <span class="mg-games__updated">Updated <span id="%s-updated">recently</span></span>
    </div>
    <div class="mg-games__price-table" data-game="%s" id="%s-price-table">
      <p class="mg-games__loading">Loading latest prices&hellip;</p>
    </div>
    <p class="mg-games__hint">Prices are reference only &mdash; confirm the final quote &amp; stock with our chat before ordering.</p>
  </section>

  <section class="mg-games__streamers">
    <h2 class="mg-games__section-title">%s Twitch Streamers</h2>
    <div class="mg-games__streamers-grid">
%s    </div>
  </section>

  <section class="mg-games__news">
    <h2 class="mg-games__section-title">%s News</h2>
    <ul class="mg-games__news-list">
%s    </ul>
  </section>

</div>

<div class="admonition note mg-games__note">
  <p class="admonition-title">Related</p>
  <p>%s</p>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Product",
      "name": "%s Top-Up",
      "description": "Discounted %s top-up (Global).",
      "brand": { "@type": "Brand", "name": "AceBase" },
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "%s",
        "highPrice": "%s",
        "availability": "https://schema.org/InStock"
      }
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
%s
      ]
    }
  ]
}
</script>
""" % (
        name, name, hero_img, name, lead, topup_url, price_title, game_key,
        game_key, game_key, section_title, s_html, name, n_html, related,
        name, name, lo, hi, q_html,
    )


GAMES = [
    dict(
        slug="pubg-mobile", name="PUBG Mobile", hero_img="pubg-mobile.svg",
        game_key="pubg-mobile", topup_url="/topup/pubg-mobile-direct/",
        lead="Top up UC (Unknown Cash) at a discount, follow the latest esports news, and watch the top PUBG Mobile Twitch streamers.",
        section_title="Top PUBG Mobile", price_title="PUBG Mobile UC &mdash; Official vs AceBase",
        streamers=[("Shroud", "FPS legend", "shroud"), ("summit1g", "FPS veteran", "summit1g"),
                   ("s1mple", "GOAT", "s1mple"), ("TGLTN", "PUBG star", "tgltn")],
        news=[("2026-07-29", "PMGC qualifiers heat up &mdash; regions battle for a spot at the finals"),
              ("2026-07-15", "New season brings map changes and a refreshed battle pass"),
              ("2026-07-02", "Top teams shake up rosters ahead of the next split")],
        faq=[("How do I top up PUBG Mobile UC with AceBase?",
              "Visit our PUBG Mobile top-up page, pick an amount, and confirm the quote in live chat."),
             ("Is PUBG Mobile UC top-up safe?",
              "Yes. We top up through the official store only. See our safety guide.")],
        related='<a href="/topup/pubg-mobile-direct/">PUBG Mobile Top-Up</a> &middot; <a href="/guides/safety/">Top-Up Safety Guide</a> &middot; <a href="/gallery/wallpapers/">Wallpapers</a>',
        lo="0.79", hi="321.76",
    ),
    dict(
        slug="pubg-gcoin", name="PUBG G-COIN", hero_img="pubg-gcoin.svg",
        game_key="pubg-gcoin", topup_url="/topup/pubg-gcoin/",
        lead="Top up PUBG PC G-COIN CDK at a discount, follow the latest esports news, and watch the top PUBG Twitch streamers.",
        section_title="Top PUBG", price_title="PUBG G-COIN CDK &mdash; Official vs AceBase",
        streamers=[("Shroud", "FPS legend", "shroud"), ("summit1g", "FPS veteran", "summit1g"),
                   ("xChocoBars", "PUBG streamer", "xchocobars"), ("Kaymind", "Pro player", "kaymind")],
        news=[("2026-07-27", "PUBG Season update ships new weapons and ranked changes"),
              ("2026-07-13", "Esports circuit announces next global tournament window"),
              ("2026-06-30", "Player skins and crates rotate in the monthly store update")],
        faq=[("How do I redeem G-COIN CDK?",
              "We send the CDK to your email. Redeem it on the PUBG official redemption page or Steam client."),
             ("Is G-COIN top-up safe?",
              "Yes. Codes are sourced from official channels. See our safety guide.")],
        related='<a href="/topup/pubg-gcoin/">PUBG G-COIN Top-Up</a> &middot; <a href="/guides/safety/">Top-Up Safety Guide</a> &middot; <a href="/gallery/wallpapers/">Wallpapers</a>',
        lo="3.11", hi="62.28",
    ),
    dict(
        slug="cod-cold-war", name="COD Black Ops Cold War", hero_img="cod-cold-war.svg",
        game_key="cod-cold-war", topup_url="/topup/cod-black-ops-cold-war/",
        lead="Get Call of Duty: Black Ops Cold War codes and Points at a discount, follow the latest esports news, and watch top COD Twitch streamers.",
        section_title="Top COD", price_title="COD Black Ops Cold War &mdash; Official vs AceBase",
        streamers=[("Scump", "COD icon", "scump"), ("Dashy", "Pro player", "dashy"),
                   ("Zer0", "FPS star", "zer0"), ("Nadeshot", "Creator", "nadeshot")],
        news=[("2026-07-28", "CDL championship weekend set &mdash; teams clash for the title"),
              ("2026-07-14", "Season update brings new operators and balance changes"),
              ("2026-07-01", "Ranked play reworks rotation for the new season")],
        faq=[("How do I get COD Black Ops Cold War codes with AceBase?",
              "Visit our COD top-up page, pick an edition or Points pack, and confirm in live chat."),
             ("How do I redeem my code?",
              "We email the activation code. Redeem it on your Xbox/Microsoft account.")],
        related='<a href="/topup/cod-black-ops-cold-war/">COD Cold War Codes</a> &middot; <a href="/guides/safety/">Top-Up Safety Guide</a> &middot; <a href="/gallery/wallpapers/">Wallpapers</a>',
        lo="5.32", hi="81.22",
    ),
    dict(
        slug="honor-of-kings", name="Honor of Kings", hero_img="honor-of-kings.svg",
        game_key="honor-of-kings", topup_url="/topup/honor-of-kings/",
        lead="Top up Honor of Kings Tokens at a discount, follow the latest esports news, and watch the top HOK Twitch streamers.",
        section_title="Top Honor of Kings", price_title="Honor of Kings Tokens &mdash; Official vs AceBase",
        streamers=[("Gemini", "HOK star", "gemini"), ("Dreamy", "Top player", "dreamy"),
                   ("XiaoMo", "HOK pro", "xiaomo"), ("Qing", "Creator", "qing")],
        news=[("2026-07-26", "KPL split finals announced &mdash; top teams to battle for the trophy"),
              ("2026-07-11", "New hero and skin drop in the latest update"),
              ("2026-06-29", "Balance patch tunes several popular heroes")],
        faq=[("How do I top up Honor of Kings Tokens with AceBase?",
              "Visit our Honor of Kings top-up page, pick an amount, and confirm in live chat."),
             ("Is HOK top-up safe?",
              "Yes. We top up through the official store only. See our safety guide.")],
        related='<a href="/topup/honor-of-kings/">Honor of Kings Top-Up</a> &middot; <a href="/guides/safety/">Top-Up Safety Guide</a> &middot; <a href="/gallery/wallpapers/">Wallpapers</a>',
        lo="1.95", hi="13.02",
    ),
    dict(
        slug="arena-breakout", name="Arena Breakout", hero_img="arena-breakout.svg",
        game_key="arena-breakout", topup_url="/topup/arena-breakout-bonds/",
        lead="Top up Arena Breakout Bonds at a discount, follow the latest esports news, and watch the top Arena Breakout Twitch streamers.",
        section_title="Top Arena Breakout", price_title="Arena Breakout Bonds &mdash; Official vs AceBase",
        streamers=[("s1mple", "GOAT", "s1mple"), ("Zer0", "FPS star", "zer0"),
                   ("TYLOO", "Team", "tyloo"), ("Shroud", "FPS legend", "shroud")],
        news=[("2026-07-30", "Arena Breakout global esports series reveals prize pool"),
              ("2026-07-16", "New gear crate rotation and event missions go live"),
              ("2026-07-03", "Season 3 patch adds operator rebalance and map updates")],
        faq=[("How do I top up Arena Breakout Bonds with AceBase?",
              "Visit our Arena Breakout top-up page, pick an amount, and confirm the quote in live chat."),
             ("Is Arena Breakout top-up safe?",
              "Yes. We top up through the official store only. See our safety guide.")],
        related='<a href="/topup/arena-breakout-bonds/">Arena Breakout Top-Up</a> &middot; <a href="/guides/safety/">Top-Up Safety Guide</a> &middot; <a href="/gallery/wallpapers/">Wallpapers</a>',
        lo="3.02", hi="115.37",
    ),
]


def main():
    games_dir = os.path.join(DOCS, "games")
    os.makedirs(games_dir, exist_ok=True)
    for g in GAMES:
        fn = os.path.join(games_dir, g["slug"] + ".md")
        with open(fn, "w", encoding="utf-8") as f:
            f.write(page(**g))
        print("wrote", fn)


if __name__ == "__main__":
    main()
