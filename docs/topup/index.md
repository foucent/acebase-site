---
title: 代储与礼品卡价格参考 | 游戏充值行情
description: AceBase 代储与礼品卡价格参考 —— PUBG Mobile UC 等 5 款游戏代储、Amazon / Apple / Google Play / Netflix / Xbox / Kammelna 等 6 种礼品卡、以及 Fortnite / Steam / PlayStation 等 7 种充值卡与充值码的逐档参考价（美元计价）。数据更新至 2026-09-21。
updated: 2026-10-13
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
     ab-card--wordmark 块里，gen_home.py 会把类一起带到首页副本。

     2026-10-13：燕云十六声之后的 14 张平台代储卡（抖音直播 / 快手 / Bigo Live /
     MICO / Poppo Live / Tango Live / Mango Live / MIGO LIVE / 超级直播 /
     Dazz Live / Xena Live / 比心 / Ludo Club / Yalla Ludo）整批删除，这一页只剩
     5 款游戏。卡片、CSS、JS 都不用改：ab-card--shop 在这一页已无卡使用
     （/gift-cards/ 仍在用），prices.json 里那 14 个 data-game 的档位数据、以及
     /assets/games/brand/ 下对应的 14 张品牌图都保留未动 —— 没有卡片再引用它们，
     删数据反而要动 merge_live_prices.py。frontmatter 的 description、JSON-LD 的
     WebPage 描述与 ItemList（19 → 5）同步改到 5 款。
     首页要跟着重生成：gen_home.py 按「每类最新六张」抓卡，TOP-UP 只剩 5 张，
     原先排在第 6 位的抖音直播卡随之从首页消失。

     2026-10-13（当天第二次）：/gift-cards/（6 张）与 /cdkeys/（7 张）两页整体并回
     这一页 —— 十三张卡原样搬过来，两页连目录一起删掉，URL 在 redirect_maps 里
     留存根指过来（带锚点，`/cdkeys/#gocash-card` → `/topup/#gocash-card`，卡片 id
     没改所以锚点仍然有效）。**这正好是 2026-09-21 → 09-24 那次拆分的逆操作**：
     09-21 十三张卡就从这一页拆出去、当天在 /gift-cards/ 与 /cdkeys/ 上各立成
     一个类目，现在合回来，页面回到拆分前的构成（5 代储 + 6 礼品卡 + 7 充值码 = 18），
     连标题都不用改 —— 「代储与礼品卡价格参考」正是拆分前这一页的名字。
     三处按现有版式对齐，不是照搬：
     ① 十三张卡各加 ab-card--wordmark，与五张游戏卡逐字同形（图都是
        /assets/games/brand/ 下现成的 2400×500 品牌横幅 —— 十三张一直躺在
        仓库里没人引用，就是这次要用的）；
     ② 十三张卡各自原有的 ab-card--shop 去掉：--shop 只钉 .ab-ec-list 的 84px
        窗口，而 --picker 那一段写在它后面、同为 0-4-0，早就把它退掉了
        （见 uncrate.css 的 --picker 注释），留着是死类，去掉才叫「全页同形」；
     ③ amazon 与 fortnite 两张原先是各自页面的第一张、带 fetchpriority="high"，
        搬过来是中段卡，这个属性连同 loading="lazy" 一起补正。
     /assets/gift-cards/ 下那十三张 360×480 产品图从此没有卡片引用（jawaker.png、
     pubg-gcoins.webp 更早已是孤儿）—— 与品牌横幅的关系是「同一商品的两种素材」，
     留着不动，删图是另一件事。
     首页跟着重生成：Gift Cards 与 CDKeys 两个类目从 nav 里消失，首页只剩
     FIGURES 与 TOP-UP 两排；TOP-UP 是 18 张卡，按「每类最新六张」只上 5 张游戏
     + 第一张礼品卡。 -->

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
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 PUBG Mobile UC。">购买</a>
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
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 PUBG G-COIN。">购买</a>
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
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Honor of Kings 点券。">购买</a>
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
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Arena Breakout Bonds。">购买</a>
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
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 燕云十六声 长鸣珠。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="where-winds-meet">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">手游 &middot; PC &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="amazon-gift-card-us">
      <div class="ab-card__media">
        <span class="ab-card__badge">电子卡密</span>
        <img src="/assets/games/brand/amazon-gift-card-us.png" alt="Amazon 礼品卡（美国）价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Amazon 礼品卡（美国）<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Amazon 礼品卡（美国）。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="amazon-gift-card-us">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">电子卡密 &middot; 美区 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="apple-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge">电子卡密</span>
        <img src="/assets/games/brand/apple-gift-card.png" alt="Apple 礼品卡价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Apple 礼品卡<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Apple 礼品卡。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="apple-gift-card">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">电子卡密 &middot; App Store 与 iTunes &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="google-play-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge">电子卡密</span>
        <img src="/assets/games/brand/google-play-gift-card.png" alt="Google Play 礼品卡价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Google Play 礼品卡<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Google Play 礼品卡。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="google-play-gift-card">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">电子卡密 &middot; Google Play &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="netflix-gift-card-us">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-16%</span>
        <img src="/assets/games/brand/netflix-gift-card-us.png" alt="Netflix 礼品卡（美国）价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Netflix 礼品卡（美国）<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Netflix 礼品卡（美国）。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="netflix-gift-card-us" data-discount="-16%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">电子卡密 &middot; 美区 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="xbox-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge">电子卡密</span>
        <img src="/assets/games/brand/xbox-gift-card.png" alt="Xbox Live 礼品卡价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Xbox Live 礼品卡<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Xbox Live 礼品卡。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="xbox-gift-card">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">电子卡密 &middot; Xbox 与 Microsoft Store &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="kammelna-gift-card">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-4%</span>
        <img src="/assets/games/brand/kammelna-gift-card.png" alt="Kammelna 礼品卡价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Kammelna 礼品卡<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Kammelna 礼品卡。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="kammelna-gift-card" data-discount="-4%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">手游 &middot; 中东区 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="fortnite-vbucks-card">
      <div class="ab-card__media">
        <span class="ab-card__badge">全平台</span>
        <img src="/assets/games/brand/fortnite-vbucks-card.png" alt="Fortnite 充值卡（V-Bucks）价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Fortnite 充值卡（V-Bucks）<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Fortnite 充值卡（V-Bucks）。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="fortnite-vbucks-card">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">全平台 &middot; Epic &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="apex-legends-coins-card">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-7%</span>
        <img src="/assets/games/brand/apex-legends-coins-card.png" alt="Apex Legends 充值卡（Coins）价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Apex Legends 充值卡（Coins）<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Apex Legends 充值卡（Coins）。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="apex-legends-coins-card" data-discount="-7%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">PC &middot; 主机 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="playstation-network-card-us">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-40%</span>
        <img src="/assets/games/brand/playstation-network-card-us.png" alt="PlayStation Network 充值卡（美国）价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">PlayStation Network 充值卡（美国）<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 PlayStation Network 充值卡（美国）。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="playstation-network-card-us" data-discount="-40%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">主机 &middot; 美区 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="nintendo-switch-online">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-23%</span>
        <img src="/assets/games/brand/nintendo-switch-online.png" alt="Nintendo Switch Online 会员资格价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Nintendo Switch Online 会员资格<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Nintendo Switch Online 会员资格。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="nintendo-switch-online" data-discount="-23%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">Switch &middot; 会员订阅 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="nintendo-eshop-card-us">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-4%</span>
        <img src="/assets/games/brand/nintendo-eshop-card-us.png" alt="Nintendo eShop 充值卡（美国）价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Nintendo eShop 充值卡（美国）<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Nintendo eShop 充值卡（美国）。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="nintendo-eshop-card-us" data-discount="-4%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">Switch &middot; 美区 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="steam-wallet-card-us">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-1%</span>
        <img src="/assets/games/brand/steam-wallet-card-us.png" alt="Steam 钱包充值码（美国）价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Steam 钱包充值码（美国）<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 Steam 钱包充值码（美国）。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="steam-wallet-card-us" data-discount="-1%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">PC &middot; 美区 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="gocash-card">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-5%</span>
        <img src="/assets/games/brand/gocash-card.png" alt="GoCash 充值卡（全球）价格参考" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">GoCash 充值卡（全球）<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="你好，我要购买 GoCash 充值卡（全球）。">购买</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="gocash-card" data-discount="-5%">
          <span class="ab-ec-loading">正在加载最新价格&hellip;</span>
        </p>

        <p class="ab-ec-foot">全球 &middot; 数据更新于 <span class="js-prices-updated">2026-09-21</span> &middot; 报价以在线咨询为准</p>
      </div>
    </article>
    </div>
  </section>

</div>

<div class="admonition note mg-games__note">
  <p class="admonition-title">相关</p>
  <p><a href="/">首页</a> &middot; <a href="/sourcing/">代购与代拍</a> &middot; <a href="/boosting/">游戏代练与陪玩</a> &middot; <a href="/services/">游戏调试服务</a> &middot; <a href="/faq/">购买指南</a></p>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "name": "代储与礼品卡价格参考",
      "description": "AceBase 代储与礼品卡价格参考，5 款游戏（PUBG Mobile UC、PUBG G-COIN、Honor of Kings、Arena Breakout、燕云十六声）的代储档位、6 种礼品卡与 7 种充值卡充值码的各档位参考价。数据更新至 2026-09-21。",
      "url": "https://acebase.cc/topup/"
    },
    {
      "@type": "ItemList",
      "name": "代储与礼品卡价格参考",
      "numberOfItems": "18",
      "itemListElement": [
        { "@type": "Product", "position": 1, "name": "PUBG Mobile UC", "url": "https://acebase.cc/topup/#pubg-mobile" },
        { "@type": "Product", "position": 2, "name": "PUBG G-COIN", "url": "https://acebase.cc/topup/#pubg-gcoin" },
        { "@type": "Product", "position": 3, "name": "Honor of Kings", "url": "https://acebase.cc/topup/#hok" },
        { "@type": "Product", "position": 4, "name": "Arena Breakout", "url": "https://acebase.cc/topup/#arena-breakout" },
        { "@type": "Product", "position": 5, "name": "燕云十六声", "url": "https://acebase.cc/topup/#where-winds-meet" },
        { "@type": "Product", "position": 6, "name": "Amazon 礼品卡（美国）", "url": "https://acebase.cc/topup/#amazon-gift-card-us" },
        { "@type": "Product", "position": 7, "name": "Apple 礼品卡", "url": "https://acebase.cc/topup/#apple-gift-card" },
        { "@type": "Product", "position": 8, "name": "Google Play 礼品卡", "url": "https://acebase.cc/topup/#google-play-gift-card" },
        { "@type": "Product", "position": 9, "name": "Netflix 礼品卡（美国）", "url": "https://acebase.cc/topup/#netflix-gift-card-us" },
        { "@type": "Product", "position": 10, "name": "Xbox Live 礼品卡", "url": "https://acebase.cc/topup/#xbox-gift-card" },
        { "@type": "Product", "position": 11, "name": "Kammelna 礼品卡", "url": "https://acebase.cc/topup/#kammelna-gift-card" },
        { "@type": "Product", "position": 12, "name": "Fortnite 充值卡（V-Bucks）", "url": "https://acebase.cc/topup/#fortnite-vbucks-card" },
        { "@type": "Product", "position": 13, "name": "Apex Legends 充值卡（Coins）", "url": "https://acebase.cc/topup/#apex-legends-coins-card" },
        { "@type": "Product", "position": 14, "name": "PlayStation Network 充值卡（美国）", "url": "https://acebase.cc/topup/#playstation-network-card-us" },
        { "@type": "Product", "position": 15, "name": "Nintendo Switch Online 会员资格", "url": "https://acebase.cc/topup/#nintendo-switch-online" },
        { "@type": "Product", "position": 16, "name": "Nintendo eShop 充值卡（美国）", "url": "https://acebase.cc/topup/#nintendo-eshop-card-us" },
        { "@type": "Product", "position": 17, "name": "Steam 钱包充值码（美国）", "url": "https://acebase.cc/topup/#steam-wallet-card-us" },
        { "@type": "Product", "position": 18, "name": "GoCash 充值卡（全球）", "url": "https://acebase.cc/topup/#gocash-card" }
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
