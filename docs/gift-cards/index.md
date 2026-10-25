---
title: "Gift Card Prices | Amazon, Apple, Google Play, Netflix, Xbox, Kammelna"
description: "AceBase Gift Cards: tier-by-tier reference prices (USD) for Amazon, Apple, Google Play, Netflix, Xbox and Kammelna gift cards. Digital codes sent after ordering; prices are recomputed with FX and the final quote is confirmed in chat."
updated: 2026-10-21
hide:
  - title
  - toc
---

<!-- 2026-10-21：/sourcing/ 那一格换成 Gift Cards（用户：「将
     http://127.0.0.1:8003/sourcing/ 改为 Gift Cards，包括链接」）。问过之后
     三件事定下来：

     ① URL 改成 /gift-cards/ —— 这个地址 2026-09-24 到 2026-10-13 之间正是
        Gift Cards 的正式地址，并回 /topup/ 后只剩一张指 /topup/ 的存根。
        这次把那条存根删掉，/sourcing/ 反过来出一张指这里的存根。
     ② 六张卡从 /topup/ **复制**过来（用户选的「复制一份」），不是搬走：
        /topup/ 的 18 张卡原样不动。档位价格由 prices.json + games-prices.js
        按 data-game 填，两页自然同步；卡上的标题、角标、页脚文案是静态的，
        以后改文案要改两处，改价不用。
     ③ /sourcing/ 上原来的八张手办卡整页删掉（用户选的「整页删掉」）；63 张
        图仍留在 /assets/gallery/gear/，和 /services/、/sim-gear/ 撤页时一样不删。
        /figures/、/proxy-buy/、/gear/、/tech/ 四条旧存根原先指 /sourcing/，
        内容已经没了，改为直接指首页（不再多跳一次）。

     nav 的 SOURCING 一格改成 GIFT CARDS；gen_home.py 把这份 nav 当类目表，
     首页那排由六张 SOURCING 卡换成六张礼品卡（总数仍是 17 张）。连带改过
     六个页面的「相关」云、README 的 URL 表，以及仓库外
     _tmp_ocr/sweep_overflow.py 的 PAGES。卡片版式照 /topup/ 原样：
     --picker + --wordmark，品牌横幅、规格选择器、内联档位价。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <header class="ab-section__head">
      <h1 class="ab-section__title">Gift Card Prices</h1>
    </header>
    <p class="ab-section__lead">Pick your card and tier, send us the region in chat, and we send the code there &mdash; the final price is confirmed there.</p>
  </section>

  <section class="ab-section">
    <div class="ab-list ab-list--expandable ab-list--pricing">
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="amazon-gift-card-us">
      <div class="ab-card__media">
        <span class="ab-card__badge">Digital code</span>
        <img src="/assets/games/brand/amazon-gift-card-us.png" alt="Amazon Gift Card (US) price reference" fetchpriority="high" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Amazon Gift Card (US)<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy an Amazon Gift Card (US).">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="amazon-gift-card-us">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Digital code &middot; US region &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="apple-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge">Digital code</span>
        <img src="/assets/games/brand/apple-gift-card.png" alt="Apple Gift Card price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Apple Gift Card<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy an Apple Gift Card.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="apple-gift-card">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Digital code &middot; App Store &amp; iTunes &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="google-play-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge">Digital code</span>
        <img src="/assets/games/brand/google-play-gift-card.png" alt="Google Play Gift Card price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Google Play Gift Card<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy a Google Play Gift Card.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="google-play-gift-card">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Digital code &middot; Google Play &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="netflix-gift-card-us">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-16%</span>
        <img src="/assets/games/brand/netflix-gift-card-us.png" alt="Netflix Gift Card (US) price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Netflix Gift Card (US)<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy a Netflix Gift Card (US).">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="netflix-gift-card-us" data-discount="-16%">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Digital code &middot; US region &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="xbox-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge">Digital code</span>
        <img src="/assets/games/brand/xbox-gift-card.png" alt="Xbox Live Gift Card price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Xbox Live Gift Card<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy an Xbox Live Gift Card.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="xbox-gift-card">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Digital code &middot; Xbox &amp; Microsoft Store &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="kammelna-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-4%</span>
        <img src="/assets/games/brand/kammelna-gift-card.png" alt="Kammelna Gift Card price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Kammelna Gift Card<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy a Kammelna Gift Card.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="kammelna-gift-card" data-discount="-4%">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; MENA region &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    </div>
  </section>

</div>

<div class="admonition note mg-games__note">
  <p class="admonition-title">Related</p>
  <p><a href="/">Home</a> &middot; <a href="/games/">Game Top-Up</a> &middot; <a href="/topup/">Gift Cards &amp; Top-Up Codes</a> &middot; <a href="/boosting/">Boosting</a> &middot; <a href="/accounts/">Accounts</a></p>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://acebase.cc/gift-cards/",
      "url": "https://acebase.cc/gift-cards/",
      "name": "Gift Card Prices | Amazon, Apple, Google Play, Netflix, Xbox, Kammelna",
      "description": "AceBase Gift Cards: tier-by-tier reference prices (USD) for Amazon, Apple, Google Play, Netflix, Xbox and Kammelna gift cards.",
      "inLanguage": "en",
      "isPartOf": {"@type": "WebSite", "name": "AceBase", "url": "https://acebase.cc/"}
    },
    {
      "@type": "ItemList",
      "name": "Gift Card Prices",
      "numberOfItems": "6",
      "itemListElement": [
        { "@type": "Product", "position": 1, "name": "Amazon Gift Card (US)", "url": "https://acebase.cc/gift-cards/#amazon-gift-card-us" },
        { "@type": "Product", "position": 2, "name": "Apple Gift Card", "url": "https://acebase.cc/gift-cards/#apple-gift-card" },
        { "@type": "Product", "position": 3, "name": "Google Play Gift Card", "url": "https://acebase.cc/gift-cards/#google-play-gift-card" },
        { "@type": "Product", "position": 4, "name": "Netflix Gift Card (US)", "url": "https://acebase.cc/gift-cards/#netflix-gift-card-us" },
        { "@type": "Product", "position": 5, "name": "Xbox Live Gift Card", "url": "https://acebase.cc/gift-cards/#xbox-gift-card" },
        { "@type": "Product", "position": 6, "name": "Kammelna Gift Card", "url": "https://acebase.cc/gift-cards/#kammelna-gift-card" }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://acebase.cc/" },
        { "@type": "ListItem", "position": 2, "name": "Gift Cards", "item": "https://acebase.cc/gift-cards/" }
      ]
    }
  ]
}
</script>
