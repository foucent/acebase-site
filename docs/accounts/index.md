---
title: "Accounts | Steam, YouTube, Spotify, Netflix, Gemini & ChatGPT"
description: "Game, streaming and AI accounts: Steam by region, YouTube, Spotify, Netflix, Gemini and ChatGPT. Prices in USD, the final quote confirmed in chat."
updated: 2026-10-25
hide:
  - title
  - toc
---

<!-- 2026-10-25：新起的 ACCOUNTS 类目（用户：「参考 https://acebase.cc/gift-cards/
     的卡片和页面样式，增加 Accounts 导航和类目，将 https://www.eldorado.gg/
     steam-accounts/oa/80abf73f-a17e-4c7b-a755-e67ea923eef6 商品加到进去，它有
     几个选项，有美区，台湾地区，日本地区，乌克兰地区」）。

     版式整页照 /gift-cards/：一个 section 头 + ab-card--picker 卡片网格（**全部
     商品同一个网格，不分小类** —— 用户 2026-10-25 的原话「该页面内的商品不用
     分类」），价格由 prices.json 的键 + games-prices.js 的 renderPicker() 填进
     下拉与标题价。**改了 prices.json 要同时把 games-prices.js 顶部的
     ?v=20261025 改掉**，否则浏览器会用缓存。

     六张卡：
     - steam-account：Eldorado 上 Ada_Store 的四个独立 offer（同一款 fresh
       Steam 账号，按区拆开卖），2026-10-25 用站内 API `/api/flexibleOffers/<id>`
       取得，四区同价 $0.50 —— 美区 80abf73f…、台湾 1e17da60…、日本 f2d97530…、
       乌克兰 78fd18c3…。卖家自述即时发货、邮箱与密码可改、无挂机无外挂。
     - spotify-account / youtube-account / netflix-account / gemini-account /
       chatai-account：来自 accountboy.com（zh-cn-cny 页面，2026-10-25 抓 SSR
       里的 window.__INIT_STATIC_PROPS__ 取 skuMap）。**用户明说「代充、额度
       充值、续费等选项不要加入进来」**，所以只取各页「账号」那一组：Spotify
       只留 3/12 个月会员账号（续费不要）、YouTube 只留账号组七个（APP 安装包组、
       月付专区代开不要）、Gemini 只留账号组两个（代充、邀请链接、下载号不要）、
       Netflix 只留共享/独享三个会员（安卓 APP 包不要）、ChatAI 只留 ChatAI账号
       与 ChatGPT Plus 独享账号两个（代充、codex额度充值不要）。卖家原价人民币，
       按 open.er-api.com 当天汇率（1 CNY = 0.149495 USD）折美元写进 prices.json，
       页尾有一段说明这件事。

     2026-10-25 晚些时候用户又去掉了 Valorant 那张卡（「去掉Valorant Account
     $3.99 这个商品」），prices.json 的 `valorant-account` 键一并删掉；品牌图
     assets/games/brand/valorant.png 是 /games/ 那张卡在用的，**不能删**。

     卡 id 也是 data-game；Buy 的 data-crisp-msg 由 renderPicker() 按所选规
     格补上 ", spec …" 的尾巴。

     相关云照全站形状（首页 + 各类目、不自链），JSON-LD 在页尾（ItemList 6 项）。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <header class="ab-section__head">
      <h1 class="ab-section__title">Accounts</h1>
    </header>
    <p class="ab-section__lead">Pick the listing that fits you, send us a message in chat, and we hand over a ready-to-play account with the login details changed to yours &mdash; the final price is confirmed there.</p>
  </section>

  <section class="ab-section">
    <div class="ab-list ab-list--expandable ab-list--pricing">
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="steam-account">
      <div class="ab-card__media">
        <span class="ab-card__badge">Account</span>
        <img src="/assets/games/brand/steam-wallet-card-us.png" alt="Steam account price reference" fetchpriority="high" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Steam Account<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy a Steam account.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="steam-account">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Fresh account &middot; Email &amp; password changeable &middot; Instant handover &middot; Data updated <span class="js-prices-updated">2026-10-25</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>

    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="spotify-account">
      <div class="ab-card__media">
        <span class="ab-card__badge">Account</span>
        <img src="/assets/games/brand/spotify.png" alt="Spotify account price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Spotify Account<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy a Spotify account.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="spotify-account">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Premium already opened &middot; Do not change the region or plan &middot; Instant handover &middot; Data updated <span class="js-prices-updated">2026-10-25</span></p>
      </div>
    </article>

    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="youtube-account">
      <div class="ab-card__media">
        <span class="ab-card__badge">Account</span>
        <img src="/assets/games/brand/youtube.png" alt="YouTube account price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">YouTube Account<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy a YouTube account.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="youtube-account">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Ships with a recovery email &middot; Change the password and email after handover &middot; Instant handover &middot; Data updated <span class="js-prices-updated">2026-10-25</span></p>
      </div>
    </article>

    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="netflix-account">
      <div class="ab-card__media">
        <span class="ab-card__badge">Account</span>
        <img src="/assets/games/brand/netflix-gift-card-us.png" alt="Netflix account price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Netflix Account<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy a Netflix account.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="netflix-account">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">30 days of Premium &middot; A shared seat must not have its password changed &middot; Instant handover &middot; Data updated <span class="js-prices-updated">2026-10-25</span></p>
      </div>
    </article>

    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="gemini-account">
      <div class="ab-card__media">
        <span class="ab-card__badge">Account</span>
        <img src="/assets/games/brand/gemini.png" alt="Gemini account price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Gemini Account<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy a Gemini account.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="gemini-account">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Plan already opened &middot; Email &amp; password changeable &middot; Instant handover &middot; Data updated <span class="js-prices-updated">2026-10-25</span></p>
      </div>
    </article>

    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="chatai-account">
      <div class="ab-card__media">
        <span class="ab-card__badge">Account</span>
        <img src="/assets/games/brand/chatgpt.png" alt="ChatGPT account price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">ChatGPT Account<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy a ChatGPT account.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="chatai-account">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Plan already opened &middot; Email &amp; password changeable &middot; Instant handover &middot; Data updated <span class="js-prices-updated">2026-10-25</span></p>
      </div>
    </article>
    </div>
  </section>

  <section class="ab-section">
    <p class="ab-section__lead">The Steam region is where the account itself is registered &mdash; it decides which Steam store you shop in and what currency its games are listed at. Tell us where you play and we match the account to it; tell us in chat if you need a region that is not listed here.</p>
    <p class="ab-section__lead">The streaming and AI accounts come from a second supplier and are priced in US dollars at the exchange rate of the day, so the figure moves with the rate rather than with the plan. Most are handed over already opened: Spotify and the Netflix seats arrive with Premium running, YouTube ships with a recovery email you should rebind to your own, and a shared Netflix seat stops working the moment its password is changed &mdash; that one is a seat, not a private account. Every account carries a three-day after-sales window for problems with the login itself; anything you break by changing the plan or the region on a live listing is outside it.</p>
  </section>

</div>

<div class="admonition note mg-games__note">
  <p class="admonition-title">Related</p>
  <p><a href="/">Home</a> &middot; <a href="/games/">Game Top-Up</a> &middot; <a href="/topup/">Gift Cards &amp; Top-Up Codes</a> &middot; <a href="/boosting/">Boosting</a></p>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://acebase.cc/accounts/",
      "url": "https://acebase.cc/accounts/",
      "name": "Accounts | Steam, YouTube, Spotify, Netflix, Gemini & ChatGPT",
      "description": "Game, streaming and AI accounts: Steam by region, YouTube, Spotify, Netflix, Gemini and ChatGPT.",
      "inLanguage": "en",
      "isPartOf": {"@type": "WebSite", "name": "AceBase", "url": "https://acebase.cc/"}
    },
    {
      "@type": "ItemList",
      "name": "Accounts",
      "numberOfItems": "6",
      "itemListElement": [
        { "@type": "Product", "position": 1, "name": "Steam Account", "url": "https://acebase.cc/accounts/#steam-account" },
        { "@type": "Product", "position": 2, "name": "Spotify Account", "url": "https://acebase.cc/accounts/#spotify-account" },
        { "@type": "Product", "position": 3, "name": "YouTube Account", "url": "https://acebase.cc/accounts/#youtube-account" },
        { "@type": "Product", "position": 4, "name": "Netflix Account", "url": "https://acebase.cc/accounts/#netflix-account" },
        { "@type": "Product", "position": 5, "name": "Gemini Account", "url": "https://acebase.cc/accounts/#gemini-account" },
        { "@type": "Product", "position": 6, "name": "ChatGPT Account", "url": "https://acebase.cc/accounts/#chatai-account" }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://acebase.cc/" },
        { "@type": "ListItem", "position": 2, "name": "Accounts", "item": "https://acebase.cc/accounts/" }
      ]
    }
  ]
}
</script>
