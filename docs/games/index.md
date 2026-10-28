---
title: "Game Top-Up Prices | 30 Games, Tier by Tier"
description: "Tier-by-tier USD reference prices for 30 game top-ups: PUBG Mobile, Honor of Kings, Genshin Impact, VALORANT, Mobile Legends and more. Pick a tier, confirm the quote in chat."
updated: 2026-10-21
hide:
  - title
  - toc
---

<!-- 2026-10-21：新增 GAME 类目（用户：「增加一个Game类目」）。问过之后选的是
     「游戏代储汇总页 /games/」：/topup/ 开头那 5 张游戏代储卡（PUBG Mobile UC、
     PUBG G-COIN、Honor of Kings、Arena Breakout、Where Winds Meet）**整块搬到这里**，
     /topup/ 只剩 6 张礼品卡 + 7 张充值卡（18 → 13 张）。

     卡片逐字照搬，id / data-game / 角标 / 页脚都没改 —— prices.json 的五个
     key 原样在用，games-prices.js 按 data-game 填档位，改价不用改标记。
     只有一处没跟过来：PUBG Mobile 在 /topup/ 上是第一张、带
     fetchpriority="high"；到这里仍是第一张，属性不动。/topup/ 的第一张换成
     Amazon 礼品卡（补上 fetchpriority="high"，去掉 loading="lazy"）。

     **锚点搬家**：/topup/#pubg-mobile 这类地址从今天起不再有目标。redirect_maps
     里五个游戏详情页（games/pubg-mobile.md、pubg-gcoin.md、hok.md、
     arena-breakout.md、where-winds-meet.md）连同 honor-of-kings.md 与
     topup-prices.md 原先都指 /topup/，现在改指 /games/ —— 卡片 id 没改，
     存根带着锚点跳过来仍然落在卡上。

     nav：按用户选的位置插在 GIFT CARDS 与 TOP-UP 之间，标签 GAME。
     **同一天稍晚导航重排，这一格挪到 TOP-UP 之后** —— 顺序变成 TOP-UP /
     GAME / GIFT CARDS / BOOSTING / BLOG（NEWS 改名 BLOG、FAQ 撤掉），
     首页取卡不受影响，22 张不变。
     gen_home.py 把 nav 当类目表，首页因此多一排 GAME 5 张（17 → 22），
     TOP-UP 那排继续按卡片 id 去重（六张礼品卡归 GIFT CARDS），顺延到
     6 张充值卡。连带改过六个页面的「相关」云、README 的 URL 表，以及仓库外
     _tmp_ocr/sweep_overflow.py 的 PAGES。版式照 /topup/ 原样：
     --picker + --wordmark，品牌横幅、规格选择器、内联档位价。

     ## 同日晚些：5 张 → 30 张
     用户：「将 https://topuplist.com/category/game-top-up 页中的商品以
     /games/ 页中的样式为模板，复刻到 /games/ 页中」。问过之后选的是
     「精选 30 款」「品牌字标」「现有 5 款各自保留」。新增 25 款按 topuplist
     分类页自己的顺序取，跳过 /topup/ 已上架的同款（一个游戏全站只给一个价）。

     数据：scripts/capture_topuplist_game.py 走它的 JSON API，在页面上下文里
     同源 fetch（过 Cloudflare），lang=en + user_currency=USD，所以档位名是英文、
     价格本来就是美元，不换汇。源站把同一款按区服重复上架（Delta Force 6 套、
     MLBB 3 套、VALORANT 5 套同名），scripts/merge_game_prices.py 只取没有区服
     后缀的那一套（全都带后缀时取档位最多的区服），同名去重取最低价，按「数字
     档位在前、同一货币成组」排序，每组最多 24 档。新键的行形沿用老键
     （title / lowest / highest / average），单一来源所以三个数相同。
     delta-force 与 valorant 两个键是 /topup/ 时代留下的孤儿行（全站没有
     data-game 引用），这次直接换成新行；其余 43 个键一字未动。

     标记：卡片区一对标记（GAMES:CARDS），由 scripts/build_games_page.py 从
     merge_game_prices.GAMES 生成。JSON-LD 的 Product 列表**不放标记**——
     那段在 ld+json 脚本块里，HTML 注释不是合法 JSON，会把整个 @graph 弄成
     解析失败；脚本按 "@type": "ItemList" 后面那
     "itemListElement": [ … ] 的形状就地重写。现有 5 张卡是从本页原样取出再
     放回的（fetchpriority、data-discount 都保留），第一张仍是 PUBG Mobile；
     新增的 25 张是模板生成的。
     品牌图在 _tmp_ocr/brand_img 一款一进程抓、prep_brands 出 2400x500 透明横幅。

     首页：GAME 那排按每类最多 6 张取，5 → 6 张（第六张是 Free Fire）。
     prices.json 的 updated 提到 2026-10-21，games-prices.js 的缓存版本
     升到 20261021b。

     ## 2026-10-26：PUBG Mobile UC 的 Buy 先填 UID 再进聊天
     用户：「这个页面中的 PUBG Mobile UC 在点击购买后，需要用户输入uid进行
     充值，需要你参考 https://topuplist.com/product/pubgm 页面，做一个弹窗
     购买结算页面」。topuplist 那边只有两件事要买方给：UID 和档位，然后
     Buy Now。我们的站没有收银台，价格一律「聊天里确认」，所以弹窗收 UID +
     确认档位，再把整单（游戏、档位、Player ID）拼成一条消息交给 Crisp，付款
     仍在聊天里完成。

     ## 同日晚：改成两步（订单 → 人工转账）
     用户又贴来一整套「人工核对 + Wise / 银行电汇」的行业做法，要求照着优化。
     海外代充这类高客单价的通行流程是：选套餐 → 结算页选 Wise / 手动转账 →
     系统生成临时订单号和汇款指引（收款邮箱 / IBAN + 唯一备注号）→ 买方转账、
     传凭证 → 人工核对到账 → 履约。于是弹窗分两步：
       01 ORDER     Player ID + 档位（档位和卡上的下拉同一份数据）
       02 PAYMENT   支付方式（Wise 转账 / PayPal）+ 订单号
                    AB-YYMMDD-XXXXXX + 金额、Player ID、档位 + 收款信息
                    + 三步说明（转账时填订单号 → 传凭证 → 人工核对后到账）
     两张方式卡的定位：Wise = 大额订单（人工核对的电汇），PayPal = 小额订单。
     **界面上不写金额门槛**（哪个数以下算小额是内部规则，不是对用户的承诺）。
     代码里仍按 `PAYPAL_UNDER` 预选：参考价低于它预选 PayPal，高于它预选 Wise；
     买方自己点过单选钮之后就按他选的来，直到重开弹窗。PayPal 这条路没有收款
     账号可给 —— 用户把订单交进聊天后，由人工在聊天里发一条**在线付款链接**，
     第 2 步的说明和「Where to pay」那行都这么写，**不要在前端编一个链接出来**。
     第 2 步的「SEND ORDER IN CHAT」把整单交给 Crisp（订单号、UID、档位、参考
     价、支付方式都在消息里），人工核对在聊天那头做 —— 本站没有后端，也不
     假装扣款，弹窗上明写 "Nothing is charged on this page."

     收款账号**绝不写进 docs/ 下的任何文件**：mkdocs.yml 的 extra.payment.wise
     （email / name / iban）由 overrides/main.html 注入成 window.AB_PAYMENT，
     checkout.js 读它。三项都空着就是「账号在聊天里给」，第 2 步显示
     "Account details come in chat — wait for them before transferring."，
     不会自己编一个账号；填了才显示收款邮箱 / IBAN，各带复制按钮。

     ## 2026-10-26 收尾：整页 30 张卡都用这套弹窗
     用户：「以这个卡片为模板，将 /games/ 页中所有商品都同样优化成这样」。于是
     本页每一张卡的 Buy 都从 `ab-crisp-open` 换成 `ab-checkout-trigger`，各挂
     `data-checkout="<卡 id / prices.json 的键>"` 与 `data-checkout-name="<卡上
     的 h3 标题>"`。这一步是一次性脚本 _tmp_ocr/games_checkout_enable.py 改的
     （幂等：已经带 data-checkout 的卡跳过），加新卡就手写这两个属性，或重跑
     脚本。**礼品卡 / 充值码 / 账号页面仍然直连聊天** —— 那些不是充进游戏 ID，
     不该问 Player ID。

     30 款游戏的账号 ID 不止一种形状：纯数字（PUBG、Genshin、Free Fire…）、
     name#tag（VALORANT、Diablo IV）、数字带括号里的服务器（Mobile Legends
     的 12345678(1234)）。所以输入框改成通用的「Player ID / account」，只拦
     明显的垃圾输入（字符集与长度，见 checkout.js 的 ID_RE），不再要求纯数字；
     提示语让用户连 #tag / (服务器) 一起贴进去。**校验不是风控，聊天里还要人工
     核一遍**。

     实现：docs/javascripts/checkout.js（ES5，全站加载，页面上没有
     [data-checkout] 就直接退出）+ docs/stylesheets/checkout.css。档位不是另
     取一份：games-prices.js 现在把取到的行挂到 window.AceBaseGameRows，弹窗
     读同一份，和卡上的下拉不可能对不上。弹窗用原生 <dialog>（Esc、焦点陷阱、
     背景 inert 都由浏览器给）。crisp.js 的 capture 监听靠 `ab-crisp-open`
     类名认领点击，所以这些卡的类名必须换掉，否则会同时开聊天和弹窗；
     checkout.js 里另有一道兜底，见到 [data-checkout] 就主动摘掉那个类。

     验收：_tmp_ocr/pubg_checkout_probe.py（先在旧构建上跑红，再验绿）。
     探针把 window.$crisp 换成记录器，好断言交给聊天的整条消息。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <header class="ab-section__head">
      <h1 class="ab-section__title">Game Top-Up Prices</h1>
    </header>
    <p class="ab-section__lead">Pick your game and tier, send us your account and region in chat, and we deliver the top-up.</p>
  </section>

  <section class="ab-section">
    <div class="ab-list ab-list--expandable ab-list--pricing">
<!-- GAMES:CARDS:START -->
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="pubg-mobile">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/pubg-mobile.png" alt="PUBG Mobile UC top-up price reference" fetchpriority="high" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">PUBG Mobile UC<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="pubg-mobile" data-checkout-name="PUBG Mobile UC" data-crisp-msg="Hi, I'd like to buy PUBG Mobile UC.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="pubg-mobile">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="pubg-gcoin">
      <div class="ab-card__media">
        <span class="ab-card__badge ab-card__badge--off">-9%</span>
        <img src="/assets/games/brand/pubg-gcoin.png" alt="PUBG G-COIN top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">PUBG G-COIN<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="pubg-gcoin" data-checkout-name="PUBG G-COIN" data-crisp-msg="Hi, I'd like to buy PUBG G-COIN.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="pubg-gcoin" data-discount="-9%">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">PC &middot; Console &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="hok">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/hok.png" alt="Honor of Kings top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Honor of Kings<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="hok" data-checkout-name="Honor of Kings" data-crisp-msg="Hi, I'd like to buy Honor of Kings Tokens.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="hok">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="arena-breakout">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/arena-breakout.png" alt="Arena Breakout top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Arena Breakout<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="arena-breakout" data-checkout-name="Arena Breakout" data-crisp-msg="Hi, I'd like to buy Arena Breakout Bonds.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="arena-breakout">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="where-winds-meet">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/where-winds-meet.png" alt="Where Winds Meet top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Where Winds Meet<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="where-winds-meet" data-checkout-name="Where Winds Meet" data-crisp-msg="Hi, I'd like to buy a Where Winds Meet top-up.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="where-winds-meet">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; PC &middot; Data updated <span class="js-prices-updated">2026-09-21</span> &middot; Final quote confirmed in chat</p>
      </div>
    </article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="freefire">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/freefire.png" alt="Free Fire top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Free Fire<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="freefire" data-checkout-name="Free Fire" data-crisp-msg="Hi, I'd like to buy Free Fire.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="freefire">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="blood-strike">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/blood-strike.png" alt="Blood Strike top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Blood Strike<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="blood-strike" data-checkout-name="Blood Strike" data-crisp-msg="Hi, I'd like to buy Blood Strike.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="blood-strike">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="pokemon-go">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/pokemon-go.png" alt="Pokémon GO top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Pokémon GO<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="pokemon-go" data-checkout-name="Pokémon GO" data-crisp-msg="Hi, I'd like to buy Pokémon GO.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="pokemon-go">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="mobile-legends">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/mobile-legends.png" alt="Mobile Legends: Bang Bang top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Mobile Legends: Bang Bang<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="mobile-legends" data-checkout-name="Mobile Legends: Bang Bang" data-crisp-msg="Hi, I'd like to buy Mobile Legends: Bang Bang.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="mobile-legends">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="honkai-star-rail">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/honkai-star-rail.png" alt="Honkai: Star Rail top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Honkai: Star Rail<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="honkai-star-rail" data-checkout-name="Honkai: Star Rail" data-crisp-msg="Hi, I'd like to buy Honkai: Star Rail.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="honkai-star-rail">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; PC &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="genshin">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/genshin.png" alt="Genshin Impact top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Genshin Impact<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="genshin" data-checkout-name="Genshin Impact" data-crisp-msg="Hi, I'd like to buy Genshin Impact.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="genshin">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; PC &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="wuthering-waves">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/wuthering-waves.png" alt="Wuthering Waves top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Wuthering Waves<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="wuthering-waves" data-checkout-name="Wuthering Waves" data-crisp-msg="Hi, I'd like to buy Wuthering Waves.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="wuthering-waves">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; PC &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="zzz">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/zzz.png" alt="Zenless Zone Zero top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Zenless Zone Zero<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="zzz" data-checkout-name="Zenless Zone Zero" data-crisp-msg="Hi, I'd like to buy Zenless Zone Zero.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="zzz">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; PC &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="nikke">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/nikke.png" alt="GODDESS OF VICTORY: NIKKE top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">GODDESS OF VICTORY: NIKKE<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="nikke" data-checkout-name="GODDESS OF VICTORY: NIKKE" data-crisp-msg="Hi, I'd like to buy GODDESS OF VICTORY: NIKKE.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="nikke">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; PC &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="identity-v">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/identity-v.png" alt="Identity V top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Identity V<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="identity-v" data-checkout-name="Identity V" data-crisp-msg="Hi, I'd like to buy Identity V.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="identity-v">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="clash-of-clans">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/clash-of-clans.png" alt="Clash of Clans top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Clash of Clans<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="clash-of-clans" data-checkout-name="Clash of Clans" data-crisp-msg="Hi, I'd like to buy Clash of Clans.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="clash-of-clans">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="clash-royale">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/clash-royale.png" alt="Clash Royale top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Clash Royale<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="clash-royale" data-checkout-name="Clash Royale" data-crisp-msg="Hi, I'd like to buy Clash Royale.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="clash-royale">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="brawl-stars">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/brawl-stars.png" alt="Brawl Stars top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Brawl Stars<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="brawl-stars" data-checkout-name="Brawl Stars" data-crisp-msg="Hi, I'd like to buy Brawl Stars.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="brawl-stars">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="love-and-deepspace">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/love-and-deepspace.png" alt="Love and Deepspace top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Love and Deepspace<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="love-and-deepspace" data-checkout-name="Love and Deepspace" data-crisp-msg="Hi, I'd like to buy Love and Deepspace.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="love-and-deepspace">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="eggy-party">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/eggy-party.png" alt="Eggy Party top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Eggy Party<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="eggy-party" data-checkout-name="Eggy Party" data-crisp-msg="Hi, I'd like to buy Eggy Party.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="eggy-party">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="harry-potter">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/harry-potter.png" alt="Harry Potter: Magic Awakened top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Harry Potter: Magic Awakened<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="harry-potter" data-checkout-name="Harry Potter: Magic Awakened" data-crisp-msg="Hi, I'd like to buy Harry Potter: Magic Awakened.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="harry-potter">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="arena-of-valor">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/arena-of-valor.png" alt="Arena of Valor top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Arena of Valor<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="arena-of-valor" data-checkout-name="Arena of Valor" data-crisp-msg="Hi, I'd like to buy Arena of Valor.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="arena-of-valor">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="once-human">
      <div class="ab-card__media">
        <span class="ab-card__badge">PC</span>
        <img src="/assets/games/brand/once-human.png" alt="Once Human top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Once Human<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="once-human" data-checkout-name="Once Human" data-crisp-msg="Hi, I'd like to buy Once Human.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="once-human">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">PC &middot; Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="delta-force">
      <div class="ab-card__media">
        <span class="ab-card__badge">PC</span>
        <img src="/assets/games/brand/delta-force.png" alt="Delta Force top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Delta Force<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="delta-force" data-checkout-name="Delta Force" data-crisp-msg="Hi, I'd like to buy Delta Force.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="delta-force">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">PC &middot; Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="valorant">
      <div class="ab-card__media">
        <span class="ab-card__badge">PC</span>
        <img src="/assets/games/brand/valorant.png" alt="VALORANT top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">VALORANT<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="valorant" data-checkout-name="VALORANT" data-crisp-msg="Hi, I'd like to buy VALORANT.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="valorant">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">PC &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="marvel-rivals">
      <div class="ab-card__media">
        <span class="ab-card__badge">PC</span>
        <img src="/assets/games/brand/marvel-rivals.png" alt="Marvel Rivals top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Marvel Rivals<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="marvel-rivals" data-checkout-name="Marvel Rivals" data-crisp-msg="Hi, I'd like to buy Marvel Rivals.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="marvel-rivals">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">PC &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="arknights-endfield">
      <div class="ab-card__media">
        <span class="ab-card__badge">PC</span>
        <img src="/assets/games/brand/arknights-endfield.png" alt="Arknights: Endfield top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Arknights: Endfield<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="arknights-endfield" data-checkout-name="Arknights: Endfield" data-crisp-msg="Hi, I'd like to buy Arknights: Endfield.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="arknights-endfield">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">PC &middot; Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="diablo-iv">
      <div class="ab-card__media">
        <span class="ab-card__badge">PC</span>
        <img src="/assets/games/brand/diablo-iv.png" alt="Diablo IV top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Diablo IV<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="diablo-iv" data-checkout-name="Diablo IV" data-crisp-msg="Hi, I'd like to buy Diablo IV.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="diablo-iv">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">PC &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="lol-wild-rift">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/lol-wild-rift.png" alt="League of Legends: Wild Rift top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">League of Legends: Wild Rift<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="lol-wild-rift" data-checkout-name="League of Legends: Wild Rift" data-crisp-msg="Hi, I'd like to buy League of Legends: Wild Rift.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="lol-wild-rift">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <article class="ab-card ab-card--brand ab-card--fold ab-card--ec ab-card--plate ab-card--picker ab-card--wordmark" id="whiteout-survival">
      <div class="ab-card__media">
        <span class="ab-card__badge">Mobile</span>
        <img src="/assets/games/brand/whiteout-survival.png" alt="Whiteout Survival top-up price reference" loading="lazy" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">Whiteout Survival<span class="ab-card__price"></span></h3>
        <div class="ab-fold">
          <div class="ab-fold__summary">
            <span class="ab-fold__act">
              <a class="ab-fold__buy ab-checkout-trigger" href="#" data-checkout="whiteout-survival" data-checkout-name="Whiteout Survival" data-crisp-msg="Hi, I'd like to buy Whiteout Survival.">Buy</a>
            </span>
          </div>
        </div>

        <p class="ab-ec-list" data-game="whiteout-survival">
          <span class="ab-ec-loading">Loading the latest prices&hellip;</span>
        </p>

        <p class="ab-ec-foot">Mobile &middot; PC &middot; Data updated <span class="js-prices-updated">2026-10-21</span> &middot; Final quote confirmed in chat</p>
      </div>
</article>
    <!-- GAMES:CARDS:END -->
    </div>
  </section>

</div>

<div class="admonition note mg-games__note">
  <p class="admonition-title">Related</p>
  <p><a href="/">Home</a> &middot; <a href="/gift-cards/">Gift Cards</a> &middot; <a href="/topup/">Gift Cards &amp; Top-Up Codes</a> &middot; <a href="/boosting/">Boosting</a> &middot; <a href="/accounts/">Accounts</a></p>
</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://acebase.cc/games/",
      "url": "https://acebase.cc/games/",
      "name": "Game Top-Up Prices",
      "description": "AceBase Game: tier-by-tier reference prices (USD) for 30 game top-ups, including PUBG Mobile UC, PUBG G-COIN, Honor of Kings, Genshin Impact and VALORANT.",
      "inLanguage": "en",
      "isPartOf": {"@type": "WebSite", "name": "AceBase", "url": "https://acebase.cc/"}
    },
    {
      "@type": "ItemList",
      "name": "Game Top-Up Prices",
      "numberOfItems": "30",
      "itemListElement": [

        { "@type": "Product", "position": 1, "name": "PUBG Mobile UC", "url": "https://acebase.cc/games/#pubg-mobile" },
        { "@type": "Product", "position": 2, "name": "PUBG G-COIN", "url": "https://acebase.cc/games/#pubg-gcoin" },
        { "@type": "Product", "position": 3, "name": "Honor of Kings", "url": "https://acebase.cc/games/#hok" },
        { "@type": "Product", "position": 4, "name": "Arena Breakout", "url": "https://acebase.cc/games/#arena-breakout" },
        { "@type": "Product", "position": 5, "name": "Where Winds Meet", "url": "https://acebase.cc/games/#where-winds-meet" },
        { "@type": "Product", "position": 6, "name": "Free Fire", "url": "https://acebase.cc/games/#freefire" },
        { "@type": "Product", "position": 7, "name": "Blood Strike", "url": "https://acebase.cc/games/#blood-strike" },
        { "@type": "Product", "position": 8, "name": "Pokémon GO", "url": "https://acebase.cc/games/#pokemon-go" },
        { "@type": "Product", "position": 9, "name": "Mobile Legends: Bang Bang", "url": "https://acebase.cc/games/#mobile-legends" },
        { "@type": "Product", "position": 10, "name": "Honkai: Star Rail", "url": "https://acebase.cc/games/#honkai-star-rail" },
        { "@type": "Product", "position": 11, "name": "Genshin Impact", "url": "https://acebase.cc/games/#genshin" },
        { "@type": "Product", "position": 12, "name": "Wuthering Waves", "url": "https://acebase.cc/games/#wuthering-waves" },
        { "@type": "Product", "position": 13, "name": "Zenless Zone Zero", "url": "https://acebase.cc/games/#zzz" },
        { "@type": "Product", "position": 14, "name": "GODDESS OF VICTORY: NIKKE", "url": "https://acebase.cc/games/#nikke" },
        { "@type": "Product", "position": 15, "name": "Identity V", "url": "https://acebase.cc/games/#identity-v" },
        { "@type": "Product", "position": 16, "name": "Clash of Clans", "url": "https://acebase.cc/games/#clash-of-clans" },
        { "@type": "Product", "position": 17, "name": "Clash Royale", "url": "https://acebase.cc/games/#clash-royale" },
        { "@type": "Product", "position": 18, "name": "Brawl Stars", "url": "https://acebase.cc/games/#brawl-stars" },
        { "@type": "Product", "position": 19, "name": "Love and Deepspace", "url": "https://acebase.cc/games/#love-and-deepspace" },
        { "@type": "Product", "position": 20, "name": "Eggy Party", "url": "https://acebase.cc/games/#eggy-party" },
        { "@type": "Product", "position": 21, "name": "Harry Potter: Magic Awakened", "url": "https://acebase.cc/games/#harry-potter" },
        { "@type": "Product", "position": 22, "name": "Arena of Valor", "url": "https://acebase.cc/games/#arena-of-valor" },
        { "@type": "Product", "position": 23, "name": "Once Human", "url": "https://acebase.cc/games/#once-human" },
        { "@type": "Product", "position": 24, "name": "Delta Force", "url": "https://acebase.cc/games/#delta-force" },
        { "@type": "Product", "position": 25, "name": "VALORANT", "url": "https://acebase.cc/games/#valorant" },
        { "@type": "Product", "position": 26, "name": "Marvel Rivals", "url": "https://acebase.cc/games/#marvel-rivals" },
        { "@type": "Product", "position": 27, "name": "Arknights: Endfield", "url": "https://acebase.cc/games/#arknights-endfield" },
        { "@type": "Product", "position": 28, "name": "Diablo IV", "url": "https://acebase.cc/games/#diablo-iv" },
        { "@type": "Product", "position": 29, "name": "League of Legends: Wild Rift", "url": "https://acebase.cc/games/#lol-wild-rift" },
        { "@type": "Product", "position": 30, "name": "Whiteout Survival", "url": "https://acebase.cc/games/#whiteout-survival" }
      
      ]
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://acebase.cc/" },
        { "@type": "ListItem", "position": 2, "name": "Game Top-Up", "item": "https://acebase.cc/games/" }
      ]
    }
  ]
}
</script>
