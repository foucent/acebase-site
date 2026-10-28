---
title: "Live Streaming & Entertainment Top-Ups | 30 Platforms, Tier by Tier"
description: "Tier-by-tier USD prices for 30 live-streaming and entertainment top-ups: Douyin, Bigo Live, Poppo, Tango, Telegram Stars, CapCut. Pick a tier, quote in chat."
updated: 2026-10-22
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
     + 第一张礼品卡。

     2026-10-21（第三次拆分，这次只拆游戏）：用户要「增加一个Game类目」，问过
     之后选的是「游戏代储汇总页 /games/」—— 开头 5 张游戏卡整块搬到新页，这一
     页只剩 6 张礼品卡 + 7 张充值卡（18 → 13 张）。卡片 id / data-game 没改，
     prices.json 原样在用；第一张换成 Amazon 礼品卡（补 fetchpriority="high"、
     去掉 loading="lazy"）。标题从「代储与礼品卡价格参考」改成「礼品卡与充值卡
     价格参考」，description 与 JSON-LD 的 WebPage / ItemList（18 → 13）/
     Breadcrumb 同步。**/topup/#pubg-mobile 这类锚点从今天起失效**；五个游戏
     详情页连同 honor-of-kings.md、topup-prices.md 的存根改指 /games/（卡片
     id 没改，锚点落在新页同名卡上）。「相关」云里这一页的标签跟着换成
     「礼品卡与充值卡价格参考」，并补上「游戏代储」。

     2026-10-22：整页换血（用户：「将 topuplist.com/category/entertainment 页中的
     商品添加到 /topup/，并将原来的 /topup/ 页中的商品删除」）。13 张数字码卡
     **全部删掉**，换成 topuplist 娱乐分类（直播 / 语音房 / 社交 App 充值）的精选
     30 款：原有 14 款直播平台（抖音 / 快手 / Bigo / MICO / Poppo / Tango /
     Mango / MIGO / 超级直播 / Dazz / Xena / 比心 / Ludo Club / Yalla Ludo）＋
     按知名度补的 16 款（StarMaker / SUGO / IMO / Chamet / Likee / Telegram /
     Party Star / CapCut / ZEPETO / HeeSay / Soulchill / DiDO / QQ 币 / QQ VIP /
     YY / Nimo TV）。分类页 44 款，其余 14 款 MENA 小平台与预付卡不上。
     · 卡片与 Product 列表都成了生成物：`scripts/build_topup_page.py` 维护
       `TOPUP:CARDS` 标记区与 JSON-LD 里 `"itemListElement"` 那段（ld+json 里
       不能放 HTML 注释，所以后者靠形状定位，不靠标记）；键表单一事实源是
       `scripts/merge_ent_prices.py` 的 `ENTERTAINMENT`。
     · 价格只有一个来源：`scripts/capture_topuplist_entertainment.py` 在页面上下文
       里同源 fetch 官方 JSON API（lang=en，美元，已扣优惠券），
       `merge_ent_prices.py` 去重排序后写 prices.json 的 30 个键 —— 同一档位
       lowest / highest / average 相等，不再是多来源区间。原来的新元换算价一并
       作废（currency 已是 USD，fx 字段留着当历史）。
     · 档位名里有中文的（比心的「比心币」等）在合并脚本里换成英文，并断言 30 组
       title 一个 CJK 字符都没有 —— 选择器会原样显示。
     · 六张礼品卡在 /gift-cards/ 还有一份副本，不受影响；七张充值码（Fortnite /
       Apex / PlayStation / Switch Online / eShop / Steam / GoCash）只在这一页，
       今天起全站不再出现，数据键留在 prices.json 里不删。/cdkeys/ 的存根
       改指 /gift-cards/（原来带锚点指这一页的码卡，锚点已失效）。
     · 30 张品牌图全部用 `prep_brands.py --safe` 重出（2400×500、墨迹 ≤ 画布
       一半），否则 5:2 的 wordmark 只画中间 52% 会把字尾切掉（poppo 原来 63.6%）。
     · 首页仍是 19 张（TOP-UP 6 / GAME 6 / GIFT CARDS 6 / BLOG 1）—— 类目数没变，
       gen_home.py 照旧每类取最新六张；title / description 是站点级的，没动。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <header class="ab-section__head">
      <h1 class="ab-section__title">Live Streaming &amp; Entertainment Top-Ups</h1>
    </header>
    <p class="ab-section__lead">Pick your platform and tier, send us your account or ID in chat, and we top it up.</p>
  </section>

  <section class="ab-section">
    <div class="ab-list ab-list--expandable ab-list--pricing">
<!-- TOPUP:CARDS:START -->
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="douyin-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/douyin-top-up.png" alt="Douyin Live top-up price reference" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Douyin Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Douyin Live.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="douyin-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="kwi-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/kwi-top-up.png" alt="Kuaishou Live top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Kuaishou Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Kuaishou Live.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="kwi-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="bigo-live">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/bigo-live.png" alt="Bigo Live top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Bigo Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Bigo Live.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="bigo-live">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="mico-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/mico-top-up.png" alt="MICO top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">MICO<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy MICO.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="mico-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="poppo-live">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/poppo-live.png" alt="Poppo Live top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Poppo Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Poppo Live.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="poppo-live">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="tango-live-recharge">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/tango-live-recharge.png" alt="Tango Live top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Tango Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Tango Live.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="tango-live-recharge">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="mango">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/mango.png" alt="Mango Live top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Mango Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Mango Live.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="mango">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="migo-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/migo-top-up.png" alt="MIGO Live top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">MIGO Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy MIGO Live.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="migo-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="superlive">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/superlive.png" alt="SuperLive top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">SuperLive<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy SuperLive.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="superlive">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="dazz-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/dazz-top-up.png" alt="Dazz Live top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Dazz Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Dazz Live.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="dazz-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="xena-live-group-voice">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/xena-live-group-voice.png" alt="Xena Live top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Xena Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Xena Live.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="xena-live-group-voice">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="bixin-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/bixin-top-up.png" alt="Bi Xin top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Bi Xin<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Bi Xin.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="bixin-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="ludo-club">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/ludo-club.png" alt="Ludo Club top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Ludo Club<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Ludo Club.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="ludo-club">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="yalla-ludo">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/yalla-ludo.png" alt="Yalla Ludo top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Yalla Ludo<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Yalla Ludo.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="yalla-ludo">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="starmaker">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/starmaker.png" alt="StarMaker top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">StarMaker<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy StarMaker.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="starmaker">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="sugo-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/sugo-top-up.png" alt="SUGO top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">SUGO<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy SUGO.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="sugo-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="imo-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/imo-top-up.png" alt="IMO top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">IMO<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy IMO.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="imo-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="chamet">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/chamet.png" alt="Chamet top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Chamet<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Chamet.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="chamet">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="likee">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/likee.png" alt="Likee top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Likee<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Likee.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="likee">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="telegram">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/telegram.png" alt="Telegram top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Telegram<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Telegram.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="telegram">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="party-star">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/party-star.png" alt="Party Star top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Party Star<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Party Star.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="party-star">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="capcut">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/capcut.png" alt="CapCut top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">CapCut<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy CapCut.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="capcut">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="zepeto">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/zepeto.png" alt="ZEPETO top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">ZEPETO<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy ZEPETO.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="zepeto">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="heesay-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/heesay-top-up.png" alt="HeeSay top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">HeeSay<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy HeeSay.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="heesay-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="soulchill">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/soulchill.png" alt="Soulchill top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Soulchill<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Soulchill.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="soulchill">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="dido">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/dido.png" alt="DiDO top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">DiDO<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy DiDO.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="dido">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="qqcoin-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/qqcoin-top-up.png" alt="QQ Coin top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">QQ Coin<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy QQ Coin.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="qqcoin-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="qqvip-top-up">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/qqvip-top-up.png" alt="QQ VIP top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">QQ VIP<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy QQ VIP.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="qqvip-top-up">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="yy-live">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/yy-live.png" alt="YY Live top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">YY Live<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy YY Live.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="yy-live">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="nimo-tv">
      <div class="ab-card__media">
        <span class="ab-card__badge">Live</span>
        <img src="/assets/games/brand/nimo-tv.png" alt="Nimo TV top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Nimo TV<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-crisp-open" href="#" data-crisp-msg="Hi, I'd like to buy Nimo TV.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="nimo-tv">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Account or ID &middot; Data updated <span class="js-prices-updated">2026-10-22</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <!-- TOPUP:CARDS:END -->
    </div>
  </section>

</div>

<div class="admonition note mg-games__note">
  <p class="admonition-title">Related</p>
  <p><a href="/">Home</a> &middot; <a href="/gift-cards/">Gift Cards</a> &middot; <a href="/games/">Game Top-Up</a> &middot; <a href="/boosting/">Boosting</a> &middot; <a href="/accounts/">Accounts</a></p>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "name": "Live Streaming & Entertainment Top-Ups",
      "description": "Tier-by-tier USD prices for 30 live-streaming and entertainment top-ups: Douyin, Bigo Live, Poppo, Tango, Telegram Stars, CapCut. Pick a tier, quote in chat.",
      "url": "https://acebase.cc/topup/"
    },
    {
      "@type": "ItemList",
      "name": "Live Streaming & Entertainment Top-Ups",
      "numberOfItems": "30",
      "itemListElement": [
        { "@type": "Product", "position": 1, "name": "Douyin Live", "url": "https://acebase.cc/topup/#douyin-top-up" },
        { "@type": "Product", "position": 2, "name": "Kuaishou Live", "url": "https://acebase.cc/topup/#kwi-top-up" },
        { "@type": "Product", "position": 3, "name": "Bigo Live", "url": "https://acebase.cc/topup/#bigo-live" },
        { "@type": "Product", "position": 4, "name": "MICO", "url": "https://acebase.cc/topup/#mico-top-up" },
        { "@type": "Product", "position": 5, "name": "Poppo Live", "url": "https://acebase.cc/topup/#poppo-live" },
        { "@type": "Product", "position": 6, "name": "Tango Live", "url": "https://acebase.cc/topup/#tango-live-recharge" },
        { "@type": "Product", "position": 7, "name": "Mango Live", "url": "https://acebase.cc/topup/#mango" },
        { "@type": "Product", "position": 8, "name": "MIGO Live", "url": "https://acebase.cc/topup/#migo-top-up" },
        { "@type": "Product", "position": 9, "name": "SuperLive", "url": "https://acebase.cc/topup/#superlive" },
        { "@type": "Product", "position": 10, "name": "Dazz Live", "url": "https://acebase.cc/topup/#dazz-top-up" },
        { "@type": "Product", "position": 11, "name": "Xena Live", "url": "https://acebase.cc/topup/#xena-live-group-voice" },
        { "@type": "Product", "position": 12, "name": "Bi Xin", "url": "https://acebase.cc/topup/#bixin-top-up" },
        { "@type": "Product", "position": 13, "name": "Ludo Club", "url": "https://acebase.cc/topup/#ludo-club" },
        { "@type": "Product", "position": 14, "name": "Yalla Ludo", "url": "https://acebase.cc/topup/#yalla-ludo" },
        { "@type": "Product", "position": 15, "name": "StarMaker", "url": "https://acebase.cc/topup/#starmaker" },
        { "@type": "Product", "position": 16, "name": "SUGO", "url": "https://acebase.cc/topup/#sugo-top-up" },
        { "@type": "Product", "position": 17, "name": "IMO", "url": "https://acebase.cc/topup/#imo-top-up" },
        { "@type": "Product", "position": 18, "name": "Chamet", "url": "https://acebase.cc/topup/#chamet" },
        { "@type": "Product", "position": 19, "name": "Likee", "url": "https://acebase.cc/topup/#likee" },
        { "@type": "Product", "position": 20, "name": "Telegram", "url": "https://acebase.cc/topup/#telegram" },
        { "@type": "Product", "position": 21, "name": "Party Star", "url": "https://acebase.cc/topup/#party-star" },
        { "@type": "Product", "position": 22, "name": "CapCut", "url": "https://acebase.cc/topup/#capcut" },
        { "@type": "Product", "position": 23, "name": "ZEPETO", "url": "https://acebase.cc/topup/#zepeto" },
        { "@type": "Product", "position": 24, "name": "HeeSay", "url": "https://acebase.cc/topup/#heesay-top-up" },
        { "@type": "Product", "position": 25, "name": "Soulchill", "url": "https://acebase.cc/topup/#soulchill" },
        { "@type": "Product", "position": 26, "name": "DiDO", "url": "https://acebase.cc/topup/#dido" },
        { "@type": "Product", "position": 27, "name": "QQ Coin", "url": "https://acebase.cc/topup/#qqcoin-top-up" },
        { "@type": "Product", "position": 28, "name": "QQ VIP", "url": "https://acebase.cc/topup/#qqvip-top-up" },
        { "@type": "Product", "position": 29, "name": "YY Live", "url": "https://acebase.cc/topup/#yy-live" },
        { "@type": "Product", "position": 30, "name": "Nimo TV", "url": "https://acebase.cc/topup/#nimo-tv" }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://acebase.cc/" },
        { "@type": "ListItem", "position": 2, "name": "Live Streaming & Entertainment Top-Ups", "item": "https://acebase.cc/topup/" }
      ]
    }
  ]
}
</script>
