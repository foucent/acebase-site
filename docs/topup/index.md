---
title: 代储与礼品卡价格参考 | 游戏充值 · 礼品卡 · 直播代储行情
description: AceBase 代储与礼品卡价格参考 —— PUBG Mobile UC、Honor of Kings 等 5 款游戏的代储档位，以及抖音、快手、Bigo Live、MICO、Poppo Live、Tango Live、MIGO LIVE 等 14 个直播与语音平台的逐档参考价（美元计价）。数据更新至 2026-09-21。
updated: 2026-09-24
hide:
  - title
  - toc
---

<!-- 2026-10-05：照 /cdkeys/ 的做法整页对齐 —— 价格阶梯换成规格选择器。
     十九张卡各加 ab-card--picker，<details>/<summary> 折行换成普通 <div>，
     展开/收起提示与「或」一并撤掉；ab-cat 标签（TOP-UP / 直播 / 语音 … 那行）
     与每张卡的 ab-fold__lead 简介也去掉，卡片只剩 标题 / 规格 <select> / CTA
     三段，与 /cdkeys/、/gift-cards/ 逐字同形。这一页没有 FAQ 段落，JSON-LD
     的 WebPage / ItemList / BreadcrumbList 原样保留。
     CSS 与 JS 都不用改：picker 的样式块和 games-prices.js 里的分支按
     ab-card--picker 触发；十九个 data-game 在 prices.json 里原样都在，只有
     pubg-gcoin 一张带 data-discount（-9%），其余靠首档价，选择器逐档填得满。
     截图封面：第一张仍是 fetchpriority="high"，其余 lazy。

     同一天用户还说「图太小」，十九张卡再加一个 ab-card--wordmark：这十九张
     图都是 2400×500 的品牌横幅（logo 居中、实际只占 300～1188×300），塞进
     240×320 的竖板里按宽度缩，logo 只剩 30px 高、上下全是空板；改成 5:2 的
     通栏横幅（宽度＝卡片宽减去文案的 20px 内边距），object-fit: cover 恰好
     取到横幅中央 1250px 宽的一条 —— 最宽的 Arena Breakout（1188px）也放得下，
     不裁任何 logo —— logo 放到约 67px 高。样式在 uncrate.css 的
     ab-card--wordmark 块里，gen_home.py 会把类一起带到首页副本。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <div class="ab-list ab-list--expandable ab-list--pricing">
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="pubg-mobile">
      <div class="ab-card__media">
        <span class="ab-card__badge">手游</span>
        <img src="/assets/games/brand/pubg-mobile.png" alt="PUBG Mobile UC 代储价格参考" fetchpriority="high" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">PUBG Mobile UC<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 PUBG Mobile UC 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="pubg-mobile">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">手游 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="pubg-gcoin">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-9%</span>
        <img src="/assets/games/brand/pubg-gcoin.png" alt="PUBG G-COIN 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">PUBG G-COIN<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 PUBG G-COIN 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="pubg-gcoin" data-discount="-9%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">PC &middot; 主机 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="hok">
      <div class="ab-card__media">
        <span class="ab-card__badge">手游</span>
        <img src="/assets/games/brand/hok.png" alt="Honor of Kings 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Honor of Kings<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Honor of Kings 点券的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="hok">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">手游 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="arena-breakout">
      <div class="ab-card__media">
        <span class="ab-card__badge">手游</span>
        <img src="/assets/games/brand/arena-breakout.png" alt="Arena Breakout 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Arena Breakout<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Arena Breakout Bonds 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="arena-breakout">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">手游 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="where-winds-meet">
      <div class="ab-card__media">
        <span class="ab-card__badge">手游</span>
        <img src="/assets/games/brand/where-winds-meet.png" alt="燕云十六声 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">燕云十六声<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 燕云十六声 长鸣珠的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="where-winds-meet">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">手游 &middot; PC &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="douyin-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/douyin-top-up.png" alt="抖音直播 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">抖音直播<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询抖音直播的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="douyin-top-up">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="kwi-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/kwi-top-up.png" alt="快手 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">快手<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询快手的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="kwi-top-up">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="bigo-live">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/bigo-live.png" alt="Bigo Live 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Bigo Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Bigo Live 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="bigo-live">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="mico-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/mico-top-up.png" alt="MICO 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">MICO<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 MICO 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="mico-top-up">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="poppo-live">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/poppo-live.png" alt="Poppo Live 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Poppo Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Poppo Live 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="poppo-live">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="tango-live-recharge">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/tango-live-recharge.png" alt="Tango Live 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Tango Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Tango Live 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="tango-live-recharge">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="mango">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/mango.png" alt="Mango Live 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Mango Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Mango Live 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="mango">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="migo-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/migo-top-up.png" alt="MIGO LIVE 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">MIGO LIVE<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 MIGO LIVE 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="migo-top-up">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="superlive">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/superlive.png" alt="超级直播 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">超级直播<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询超级直播的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="superlive">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="dazz-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/dazz-top-up.png" alt="Dazz Live 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Dazz Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Dazz Live 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="dazz-top-up">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="xena-live-group-voice">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/xena-live-group-voice.png" alt="Xena Live：群组语音 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Xena Live：群组语音<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Xena Live 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="xena-live-group-voice">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="bixin-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/bixin-top-up.png" alt="比心 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">比心<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询比心的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="bixin-top-up">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="ludo-club">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/ludo-club.png" alt="Ludo Club 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Ludo Club<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Ludo Club 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="ludo-club">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--shop ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="yalla-ludo">
      <div class="ab-card__media">
        <span class="ab-card__badge">平台代储</span>
        <img src="/assets/games/brand/yalla-ludo.png" alt="Yalla Ludo 代储价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Yalla Ludo<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我想咨询 Yalla Ludo 的实时价格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="yalla-ludo">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">平台代储 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    </div>
  </section>

</div>

<div class="admonition note mg-games__note">
  <p class="admonition-title">相关</p>
  <p><a href="/">首页</a> &middot; <a href="/figures/">FIGURES</a> &middot; <a href="/gift-cards/">Gift Cards</a> &middot; <a href="/cdkeys/">CDKeys</a> &middot; <a href="/faq/">购买指南</a></p>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "name": "代储与礼品卡价格参考",
      "description": "AceBase 代储与礼品卡价格参考，5 款游戏的各档位充值参考价，以及抖音、快手、Bigo Live、MICO、Poppo Live、Tango Live、Mango Live、MIGO LIVE、超级直播、Dazz Live、Xena Live、比心、Ludo Club、Yalla Ludo 共 14 个直播与语音平台的充值档位。数据更新至 2026-09-21。",
      "url": "https://acebase.cc/topup/"
    },
    {
      "@type": "ItemList",
      "name": "代储与礼品卡价格参考",
      "numberOfItems": "19",
      "itemListElement": [
        { "@type": "Product", "position": 1, "name": "PUBG Mobile UC", "url": "https://acebase.cc/topup/#pubg-mobile" },
        { "@type": "Product", "position": 2, "name": "PUBG G-COIN", "url": "https://acebase.cc/topup/#pubg-gcoin" },
        { "@type": "Product", "position": 3, "name": "Honor of Kings", "url": "https://acebase.cc/topup/#hok" },
        { "@type": "Product", "position": 4, "name": "Arena Breakout", "url": "https://acebase.cc/topup/#arena-breakout" },
        { "@type": "Product", "position": 5, "name": "燕云十六声", "url": "https://acebase.cc/topup/#where-winds-meet" },
        { "@type": "Product", "position": 6, "name": "抖音直播", "url": "https://acebase.cc/topup/#douyin-top-up" },
        { "@type": "Product", "position": 7, "name": "快手", "url": "https://acebase.cc/topup/#kwi-top-up" },
        { "@type": "Product", "position": 8, "name": "Bigo Live", "url": "https://acebase.cc/topup/#bigo-live" },
        { "@type": "Product", "position": 9, "name": "MICO", "url": "https://acebase.cc/topup/#mico-top-up" },
        { "@type": "Product", "position": 10, "name": "Poppo Live", "url": "https://acebase.cc/topup/#poppo-live" },
        { "@type": "Product", "position": 11, "name": "Tango Live", "url": "https://acebase.cc/topup/#tango-live-recharge" },
        { "@type": "Product", "position": 12, "name": "Mango Live", "url": "https://acebase.cc/topup/#mango" },
        { "@type": "Product", "position": 13, "name": "MIGO LIVE", "url": "https://acebase.cc/topup/#migo-top-up" },
        { "@type": "Product", "position": 14, "name": "超级直播", "url": "https://acebase.cc/topup/#superlive" },
        { "@type": "Product", "position": 15, "name": "Dazz Live", "url": "https://acebase.cc/topup/#dazz-top-up" },
        { "@type": "Product", "position": 16, "name": "Xena Live：群组语音", "url": "https://acebase.cc/topup/#xena-live-group-voice" },
        { "@type": "Product", "position": 17, "name": "比心", "url": "https://acebase.cc/topup/#bixin-top-up" },
        { "@type": "Product", "position": 18, "name": "Ludo Club", "url": "https://acebase.cc/topup/#ludo-club" },
        { "@type": "Product", "position": 19, "name": "Yalla Ludo", "url": "https://acebase.cc/topup/#yalla-ludo" }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "首页", "item": "https://acebase.cc/" },
        { "@type": "ListItem", "position": 2, "name": "代储与礼品卡价格参考", "item": "https://acebase.cc/topup/" }
      ]
    }
  ]
}
</script>
