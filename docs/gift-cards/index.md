---
title: Gift Cards | 礼品卡价格参考
description: AceBase Gift Cards —— Amazon、Apple、Google Play、Netflix、Xbox、Kammelna 六种礼品卡的逐档参考价（美元计价）。数据更新至 2026-09-24。
updated: 2026-09-24
hide:
  - title
  - toc
---

<!-- 2026-09-24：这一格原来是 STYLE（穿搭写真 9 套 + 汽车实拍 6 套的图集页，
     在 docs/style/ 下）。用户要把它改名成 Gift Cards 并清空，六张礼品卡从
     /topup/ 的第二段整块搬到这里 —— markup 逐字照搬，只把卡上那行分类标签
     （原先是那三个大写字母）改成 Gift Cards；页尾那段「礼品卡常见问题」与它的
     FAQPage 结构化数据
     也跟着过来了。价格阶梯不用改任何 JS：games-prices.js 全站加载，六个
     data-game 在 prices.json 里原样都在。
     旧 /style/ 指回首页（redirect_maps），那 15 张图集卡连图一起从站上撤掉 ——
     整站副本 MyStyle.com（2026-09-24 做的）里还留着完整的一份。 -->

<!-- 2026-10-05：照 /cdkeys/ 的做法整页对齐 —— 价格阶梯换成规格选择器。
     六张卡各加 ab-card--picker，<details>/<summary> 折行换成普通 <div>，
     展开/收起提示与「或」一并撤掉；ab-cat 标签（Gift Cards 那行）与每张卡的
     ab-fold__lead 简介也去掉，卡片只剩 标题 / 规格 <select> / CTA 三段，
     与 /cdkeys/ 逐字同形。页尾「礼品卡常见问题」连同它的 FAQPage 结构化数据
     一起删掉（模板页没有这一段），ItemList 与 BreadcrumbList 原样保留。
     CSS 与 JS 都不用改：picker 的样式块和 games-prices.js 里的分支按
     ab-card--picker 触发，正好落在 /cdkeys/ 那些卡同一套规则上；六个
     data-game 在 prices.json 里原样都在，选择器逐档填得满。
     图集页时代留下的 MyStyle.com 整站副本不受影响。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <div class="ab-list ab-list--expandable ab-list--pricing">
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker" id="amazon-gift-card-us">
      <div class="ab-card__media">
        <span class="ab-card__badge">电子卡密</span>
        <img src="/assets/gift-cards/amazon.png" alt="Amazon 礼品卡（美国）价格参考" fetchpriority="high" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Amazon 礼品卡（美国）<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Amazon 礼品卡（美国）的实时价格。">咨询实时价格或购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="amazon-gift-card-us">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">电子卡密 &middot; 美区 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker" id="apple-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge">电子卡密</span>
        <img src="/assets/gift-cards/apple.png" alt="Apple 礼品卡价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Apple 礼品卡<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Apple 礼品卡的实时价格。">咨询实时价格或购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="apple-gift-card">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">电子卡密 &middot; App Store 与 iTunes &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker" id="google-play-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge">电子卡密</span>
        <img src="/assets/gift-cards/google.png" alt="Google Play 礼品卡价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Google Play 礼品卡<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Google Play 礼品卡的实时价格。">咨询实时价格或购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="google-play-gift-card">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">电子卡密 &middot; Google Play &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker" id="netflix-gift-card-us">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-16%</span>
        <img src="/assets/gift-cards/netflix.png" alt="Netflix 礼品卡（美国）价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Netflix 礼品卡（美国）<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Netflix 礼品卡（美国）的实时价格。">咨询实时价格或购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="netflix-gift-card-us" data-discount="-16%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">电子卡密 &middot; 美区 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker" id="xbox-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge">电子卡密</span>
        <img src="/assets/gift-cards/xbox.png" alt="Xbox Live 礼品卡价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Xbox Live 礼品卡<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Xbox Live 礼品卡的实时价格。">咨询实时价格或购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="xbox-gift-card">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">电子卡密 &middot; Xbox 与 Microsoft Store &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker" id="kammelna-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-4%</span>
        <img src="/assets/gift-cards/kammelna.png" alt="Kammelna 礼品卡价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Kammelna 礼品卡<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Kammelna 礼品卡的实时价格。">咨询实时价格或购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="kammelna-gift-card" data-discount="-4%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">手游 &middot; 中东区 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    </div>
  </section>

</div>

<div class="admonition note mg-games__note">
  <p class="admonition-title">相关</p>
  <p><a href="/">首页</a> &middot; <a href="/gear/">电竞房与桌搭</a> &middot; <a href="/topup/">代储与礼品卡价格参考</a> &middot; <a href="/cdkeys/">CDKeys</a> &middot; <a href="/faq/">购买指南</a></p>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "name": "礼品卡价格参考",
      "description": "AceBase Gift Cards，Amazon、Apple、Google Play、Netflix、Xbox、Kammelna 六种礼品卡的逐档参考价（美元计价）。数据更新至 2026-09-24。",
      "url": "https://acebase.cc/gift-cards/"
    },
    {
      "@type": "ItemList",
      "name": "礼品卡价格参考",
      "numberOfItems": "6",
      "itemListElement": [
        { "@type": "Product", "position": 1, "name": "Amazon 礼品卡（美国）", "url": "https://acebase.cc/gift-cards/#amazon-gift-card-us" },
        { "@type": "Product", "position": 2, "name": "Apple 礼品卡", "url": "https://acebase.cc/gift-cards/#apple-gift-card" },
        { "@type": "Product", "position": 3, "name": "Google Play 礼品卡", "url": "https://acebase.cc/gift-cards/#google-play-gift-card" },
        { "@type": "Product", "position": 4, "name": "Netflix 礼品卡（美国）", "url": "https://acebase.cc/gift-cards/#netflix-gift-card-us" },
        { "@type": "Product", "position": 5, "name": "Xbox Live 礼品卡", "url": "https://acebase.cc/gift-cards/#xbox-gift-card" },
        { "@type": "Product", "position": 6, "name": "Kammelna 礼品卡", "url": "https://acebase.cc/gift-cards/#kammelna-gift-card" }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "首页", "item": "https://acebase.cc/" },
        { "@type": "ListItem", "position": 2, "name": "Gift Cards", "item": "https://acebase.cc/gift-cards/" }
      ]
    }
  ]
}
</script>
