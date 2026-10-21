---
title: "Game News | Patch Notes, Guides & Launch Dates"
description: "Game news and guides: Delta Force ammo charts, AFK Journey and ZZZ patch notes, K/DA skins, VALORANT bundles and EA FC 26. Read the condensed story in place."
updated: 2026-10-22
hide:
  - title
  - toc
---

<!-- 2026-10-22：整页改成资讯列表（用户：「模仿 https://www.topuplive.com/news/
     页中的排版，并将第一页的内容添到 /blog/（把内容改成符合自己网站的），并去掉
     Haruo the Alien …… 卡片」）。问过之后定的两件事：**第一页内容全部改写进来**、
     **首页 BLOG 仍只取 1 张**。

     版式：topuplive 的资讯页是一列横排的条目 —— 左边 16:9 缩略图，右边标题、
     日期·分类、两三行摘要、Read More。这里原样搬过来，只换成站内语言：
     缩略图左、标题句首大写（站内卡片标题本是全大写，长标题全大写读不动，
     故这一种卡片单独关掉）、日期·分类一行小字、摘要两三行，折子仍是
     <details>（ab-fold），点开在同一行里展开压缩稿，不是外链。

     内容：来源站第一页共 10 条，改写 9 条。**没有收的是那条 2024-08-09 的
     公司新闻**（TOPUPLIVE 自家招商稿，正文通篇是它自己的平台、只有一张印满
     对方品牌的宣传图、且已过两年），不属本站的资讯。其余九条都按本站口径重写：
     英文、不点来源站名、不写促销话术，文末留一行 Source；能用站内页面接的
     都接过去（/games/#delta-force、/games/#zzz、/games/#valorant、
     /games/#arknights-endfield、/topup/#bigo-live）。

     图片：每条一张 16:9 封面，docs/assets/news/<slug>/cover.jpg（1000×563，
     由 _tmp_ocr/news_covers.py 从来源站列表缩略图裁切生成；ZZZ 3.3 那张原图
     2.47:1、标题横贯整幅，直接裁会切字，改用模糊底 + 整图居中的画法）。
     文章内不再放图集，原来那套 2×2 缩略图（.ab-card__shots）随 Haruo 卡一起
     撤掉，CSS 里对应规则也删了。

     2026-10-21：NEWS 改名 **BLOG**（用户：「将News改为blog」，问过之后选的是
     标签与地址都改）：目录 docs/news/ → docs/blog/，地址 /news/ → /blog/，
     /news/ 由 redirect_maps 出存根指过来（带锚点）。页面标题、正文、卡片一个
     字没动，只把 JSON-LD 里写死的旧绝对地址同步成 /blog/；图片仍在
     docs/assets/news/，资源路径不跟改名（改它要连带动图名与 data-gallery）。
     同一天导航重排，这一格从第一格挪到最后一格。

     2026-10-20：新增 NEWS 类目，nav 第一格（原来的 HOME 让位，首页 / 仍由
     gen_home.py 生成，点字标 ACEBASE 回去）。正文中文、nav 标签英文，和全站
     一致。

     这一页的前身是 /card-test/ 的排版测试页：用户给了一篇 gamebase 新闻
     https://news.gamebase.com.tw/news/detail/99441732
     （《Haruo the Alien》/《宇宙人ハルオ君》，第三人称射击，PC Steam），
     要求「以 /services/ 上 无畏契约 电脑调试 $9.9 那张卡的大小为模板」排成
     一张卡看效果。看过之后决定把它留成正式的资讯页，于是：
       · 页面搬到 /news/，资产目录一并搬到 docs/assets/news/；
       · 卡片去掉 $9.9（资讯不卖东西），动作行从「购买」改成「阅读原文」，
         新窗口打开原文，rel="noopener"；
       · 页面文案改成真的资讯页介绍，不再是测试页。

     2026-10-20 第二版（用户：「阅读原文 不需跳转到原页面，而是将原页面中的
     内容进行压缩，点击阅读原文后是一个展开效果，并将原文中的图片变成灯箱
     效果」）：
       · 动作行不再是外链，改成 <details class="ab-fold">，「阅读原文 / 收起」
         就在原来那一行，展开后文章的压缩稿排在卡里。
       · 展开的是压缩稿，不是原文全文，来源行写在文末。
       · 四张图 02–05 按原文顺序排成 2×2 缩略图，点开是站内的灯箱。
         这一版在 2026-10-22 随整页改版撤掉。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <header class="ab-section__head">
      <h1 class="ab-section__title">Game News</h1>
    </header>
    <p class="ab-section__lead">Patch notes, guides and launch coverage, newest first. Tap &ldquo;Read article&rdquo; to expand the condensed story in place.</p>
  </section>

  <section class="ab-section">
    <div class="ab-newsfeed">

      <article class="ab-card ab-card--row" id="delta-force-ammo">
        <div class="ab-card__media">
          <img src="/assets/news/delta-force-ammo-chart-guide/cover.jpg" alt="Delta Force ammo chart guide cover" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Delta Force Ammo Chart: Which Rounds Beat Which Armour</h3>
          <p class="ab-card__meta"><time datetime="2026-10-21">21 Oct 2026</time> &middot; Delta Force</p>
          <p class="ab-card__excerpt">Ammo one level above the target&rsquo;s armour does full damage; one level below cuts it to a coin flip. The penetration table, what each tier costs per round, and what to carry.</p>
          <details class="ab-fold ab-card__read">
            <summary class="ab-fold__summary">
              <span class="ab-fold__cue"><span class="ab-fold__cue-more">Read article</span><span class="ab-fold__cue-less">Show less</span></span>
            </summary>
            <div class="ab-card__article">
              <p>In Delta Force Operations, penetration is decided by the gap between your ammo level and the target&rsquo;s armour level, not by the gun. Match the level and the shot does full damage; one level under drops it to roughly half, two under to a quarter, three or more leaves 5&ndash;10% &mdash; a wasted magazine in most fights.</p>
              <p>The full table, armour across and ammo down: level 1 ammo gets 50% through level 1 armour and 25/10/5/5/5% through the rest. Level 2 runs 75/50/25/10/5/5. Level 3 runs 90/75/50/25/10/5. Level 4 runs 100/90/75/50/25/10. Level 5 runs 100/100/90/75/50/25, and level 6 runs 100/100/100/90/75/50. Anything at or above the armour level is a clean hit.</p>
              <p>The price ladder repeats in every calibre. Tier 1 and 2 rounds cost next to nothing per round, general-purpose tier 3 sits at 300&ndash;500, tier 4 at 1,500&ndash;2,000 and tier 5 at 4,500&ndash;6,000. 5.56 goes RRLP &rarr; FMJ &rarr; M855 &rarr; M855A1 &rarr; M995; 5.45 goes LP &rarr; T45M &rarr; PS &rarr; BP &rarr; AP; 7.62&times;39 goes PRS &rarr; T &rarr; PS &rarr; BT &rarr; BS; 7.62&times;51 jumps straight from M80 at tier 4 to M62 at tier 5.</p>
              <p>Carry one tier above the armour you expect to meet. Against unarmoured targets a cheap round &mdash; RIP for flesh &mdash; saves credits and kills just as fast, while nothing under tier 5 is worth a slot against tier 5 and 6 plates. Damage also falls off with range, so a high-penetration round at distance still loses bite.</p>
              <p>Delta Coins and their tier prices are on our <a href="/games/#delta-force">Delta Force page</a>. If you are earning them in-game instead, budget for ammo before anything else: a raid&rsquo;s ammo bill usually costs more than the kit it goes into.</p>
              <p class="ab-card__source">Source: Delta Force Operations ammo data, October 2026.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="afk-journey-182">
        <div class="ab-card__media">
          <img src="/assets/news/afk-journey-version-1-8-2-update/cover.jpg" alt="AFK Journey 1.8.2 patch preview art" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">AFK Journey 1.8.2: Marene, Baden and Thane Join the Veil of Memories Season</h3>
          <p class="ab-card__meta"><time datetime="2026-10-21">21 Oct 2026</time> &middot; AFK Journey</p>
          <p class="ab-card__excerpt">Three heroes in one patch, a new Primal Lord, four events and a redeem code for 500 Diamonds and 20,000 Gold. What 1.8.2 adds, and what to settle before it lands.</p>
          <details class="ab-fold ab-card__read">
            <summary class="ab-fold__summary">
              <span class="ab-fold__cue"><span class="ab-fold__cue-more">Read article</span><span class="ab-fold__cue-less">Show less</span></span>
            </summary>
            <div class="ab-card__article">
              <p>Farlight Games has published the patch preview for AFK Journey 1.8.2, the second half of the Veil of Memories season that opened with 1.8.1. The headline is three new heroes &mdash; Marene, Baden and Thane &mdash; with Baden dated 29 October on the Japanese server schedule and the global rollout expected to follow closely.</p>
              <p>Marene arrives with Stormbound Seas, a limited-time hero event. Treasure Rush adds a casual AFK PvP activity, Horn Rally is guild co-op PvE, and Autumn Legend is a battle-prediction event. Grave Alchemist is the new Primal Lord, Harak gets an Enhance Force upgrade, and Senea receives a skin called Azure Aria. Two new Merlin cosmetics &mdash; Early Departer Garbz and Night of Frights &mdash; close out the patch list.</p>
              <p>Three heroes in one update is a recruitment decision, not a shopping list. Marene is the event hero and is the one with a date attached; Baden and Thane are worth judging on their kits once the in-game interface shows them. The preview also carries a redeem code for 500 Diamonds and 20,000 Gold &mdash; codes expire, so claim it the day the patch goes live.</p>
              <p>Dragon Crystals are still the fastest route to summons, so decide the pack size against the banner you are actually pulling rather than stocking up in advance.</p>
              <p class="ab-card__source">Source: AFK Journey 1.8.2 patch preview, October 2026.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="zzz-city-fund">
        <div class="ab-card__media">
          <img src="/assets/news/zzz-3-3-new-eridu-city-fund/cover.jpg" alt="Zenless Zone Zero 3.3 New Eridu City Fund banner" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">ZZZ 3.3 City Fund: Growth vs Premium, and What the Certificate Buys</h3>
          <p class="ab-card__meta"><time datetime="2026-10-21">21 Oct 2026</time> &middot; Zenless Zone Zero</p>
          <p class="ab-card__excerpt">680 Polychromes up front, an avatar and a namecard, and a Great Builder&rsquo;s Certificate at level 30 that trades for one of seven W-Engines &mdash; before the 30 November deadline.</p>
          <details class="ab-fold ab-card__read">
            <summary class="ab-fold__summary">
              <span class="ab-fold__cue"><span class="ab-fold__cue-more">Read article</span><span class="ab-fold__cue-less">Show less</span></span>
            </summary>
            <div class="ab-card__article">
              <p>The New Eridu City Fund returns in Zenless Zone Zero 3.3 on three tracks. Basic is free and unlocked automatically from the start of the season; Growth is the paid track; Premium includes Growth plus a set of instant extras. Expansion Tasks and the free track stay open to everyone, but buying a plan or upgrading one closes an hour before the event ends.</p>
              <p>Growth grants 680 Polychromes and the Trick or Treat! avatar immediately, then adds the Horror Tale: Childhood Edition namecard and upgrade materials as your Fund Level rises. Premium stacks 208 more Polychromes, a menu decoration set, a W-Engine Microcontroller Unit, a Resonating Core and Ether Batteries on top.</p>
              <p>The reward easiest to overlook is the Great Builder&rsquo;s Certificate. Reach Fund Level 30, claim it, and pick one W-Engine from a selection of seven, the A-Rank Bloodmarrow Coffer among them. It belongs to this Fund period: unused, it expires with the season.</p>
              <p>For value, Growth is the buy for players who will actually finish the track. Premium only pays if the cosmetics and materials matter to you as well; if it is Polychromes alone, compare the package against buying currency directly.</p>
              <p>Monochrome tiers in USD are listed on our <a href="/games/#zzz">Zenless Zone Zero page</a>.</p>
              <p class="ab-card__source">Source: Zenless Zone Zero 3.3 City Fund announcement.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="zzz-spooky-funhouse">
        <div class="ab-card__media">
          <img src="/assets/news/zzz-spooky-funhouse-tales-guide/cover.jpg" alt="Zenless Zone Zero Spooky Funhouse Tales event art" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">ZZZ Spooky Funhouse Tales: Scare the Guests, Keep the Outfit</h3>
          <p class="ab-card__meta"><time datetime="2026-10-21">21 Oct 2026</time> &middot; Zenless Zone Zero</p>
          <p class="ab-card__excerpt">The 3.3 Halloween event runs 22 October to 30 November: three stage groups, a Fright score mode, and an Angels of Delusion outfit for clearing every Mission stage.</p>
          <details class="ab-fold ab-card__read">
            <summary class="ab-fold__summary">
              <span class="ab-fold__cue"><span class="ab-fold__cue-more">Read article</span><span class="ab-fold__cue-less">Show less</span></span>
            </summary>
            <div class="ab-card__article">
              <p>Spooky Funhouse Tales opens on 22 October 2026 at 10:00 and closes on 30 November at 03:59, server time. Entry needs Inter-Knot Level 20 and Main Story Chapter 1 &ndash; Intermission; the VR game itself is at the HIA Club, through Patsy.</p>
              <p>Mission Mode carries the progression. Three themed groups of stages unlock in sequence, and each stage asks you to plan scares and steer a Trickmobile at the funhouse&rsquo;s visitors rather than win a straight fight. Clearing Mission Mode is also what unlocks Challenge Mode, which scores runs on a Fright meter &mdash; optimisation, not progression.</p>
              <p>The reward list: Polychromes, Hamster Cage Pass, upgrade materials, the A-Rank W-Engine Candlelit Scheme, the Prankster and Mischievous Proxy accessories, and &mdash; for clearing every Mission stage &mdash; the limited-time Angels of Delusion outfit, claimed through the Angels Support Operation rewards.</p>
              <p>Do Mission Mode first and collect what it unlocks, then go back for Fright scores. The end date is fixed, and a skipped Mission stage costs the outfit rather than a handful of materials.</p>
              <p>Monochrome tiers in USD are listed on our <a href="/games/#zzz">Zenless Zone Zero page</a>.</p>
              <p class="ab-card__source">Source: Zenless Zone Zero 3.3 event announcement.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="lol-kda-firestarter">
        <div class="ab-card__media">
          <img src="/assets/news/league-of-legends-kda-firestarter-skins/cover.jpg" alt="League of Legends K/DA FIRESTARTER skins key art" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">K/DA FIRESTARTER: Four Skins, Patch 26.22 and What They Cost in RP</h3>
          <p class="ab-card__meta"><time datetime="2026-10-21">21 Oct 2026</time> &middot; League of Legends</p>
          <p class="ab-card__excerpt">Ahri, Akali, Evelynn and Kai&rsquo;Sa are back in red and silver. Three store skins at 1,350 or 1,820 RP, one Mythic through the Sanctum, and a date Riot has not confirmed.</p>
          <details class="ab-fold ab-card__read">
            <summary class="ab-fold__summary">
              <span class="ab-fold__cue"><span class="ab-fold__cue-more">Read article</span><span class="ab-fold__cue-less">Show less</span></span>
            </summary>
            <div class="ab-card__article">
              <p>Riot released the K/DA single &ldquo;FIRESTARTER&rdquo; on 19 October 2026, with Miyeon and Soyeon of i-dle, Sophie Powers and Mimi Webb voicing Ahri, Akali, Evelynn and Kai&rsquo;Sa. Community coverage puts the matching skins in Patch 26.22 on 4 November; Riot has published neither a store date nor a complete price list.</p>
              <p>Reported pricing: Ahri and Kai&rsquo;Sa at 1,350 RP each (Epic), Evelynn at 1,820 RP (Legendary, with extra voice lines and animations). Akali&rsquo;s FIRESTARTER skin is reported as a Mythic variant, Ignition, drawn from The Sanctum at up to 16,000 RP with a 40-pull cap at 400 RP a pull. Evelynn also gets a second Mythic, Hitmaker.</p>
              <p>Chromas run eight each for Ahri and Kai&rsquo;Sa and six for Evelynn, with the ruby versions marked as 2026 bundle exclusives. The store skins stay on sale after the event; the Mythic versions leave when the window closes.</p>
              <p>Treat the date and the Sanctum figures as reported until the patch notes land. If you are buying RP ahead of 4 November, 1,350 covers an Epic and 1,820 the Legendary, so size the pack to the skin you actually want.</p>
              <p class="ab-card__source">Source: Riot Games announcement and community reports, October 2026.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="bigo-free-diamonds">
        <div class="ab-card__media">
          <img src="/assets/news/latest-tips-for-maximizing-free-bigo-live-diamonds/cover.jpg" alt="Bigo Live app on a phone" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Free Bigo Live Diamonds: What Actually Works</h3>
          <p class="ab-card__meta"><time datetime="2026-05-18">18 May 2026</time> &middot; Bigo Live</p>
          <p class="ab-card__excerpt">Daily logins, in-app missions and referrals are the only routes that pay; generators are not. What each method returns, and how to tell a promotion from a scam.</p>
          <details class="ab-fold ab-card__read">
            <summary class="ab-fold__summary">
              <span class="ab-fold__cue"><span class="ab-fold__cue-more">Read article</span><span class="ab-fold__cue-less">Show less</span></span>
            </summary>
            <div class="ab-card__article">
              <p>Diamonds on Bigo Live come from three legitimate places: the daily login reward, in-app missions and events, and referrals. Anything offering unlimited diamonds for a password or an app install is harvesting accounts.</p>
              <p>Daily rewards are small but they compound &mdash; users report 5&ndash;20 diamonds a day, with streak multipliers on some accounts. Missions and seasonal events are the bigger source, often 50&ndash;200 diamonds a task, and the event banner is where the new ones appear first.</p>
              <p>Referrals pay both sides: milestone rewards for the inviter and a bonus for the invitee, with platform-run promotions sometimes adding coupons on top. Read the terms before sharing a link, because a threshold usually decides whether anyone is paid at all.</p>
              <p>When a gift or a streamer goal is time-limited, a top-up is the reliable route. Our <a href="/topup/#bigo-live">Bigo Live tiers</a> are priced per tier in USD, and a small pack costs less than what a failed &ldquo;free&rdquo; offer usually asks of your account.</p>
              <p class="ab-card__source">Source: Bigo Live in-app rewards, May 2026.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="valorant-bundles">
        <div class="ab-card__media">
          <img src="/assets/news/valorant-new-bundles-leaked-content-release-date-and-price/cover.jpg" alt="VALORANT Kuronami 2.0 weapon skins" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Kuronami 2.0 and Holo Meridian: The Two Bundles That Shipped in April</h3>
          <p class="ab-card__meta"><time datetime="2026-04-15">15 Apr 2026</time> &middot; VALORANT</p>
          <p class="ab-card__excerpt">Kuronami 2.0 arrived with Patch 12.08 and Holo Meridian on 16 April &mdash; five weapons each, a melee in both, and premium pricing in line with Riot&rsquo;s recent sets.</p>
          <details class="ab-fold ab-card__read">
            <summary class="ab-fold__summary">
              <span class="ab-fold__cue"><span class="ab-fold__cue-more">Read article</span><span class="ab-fold__cue-less">Show less</span></span>
            </summary>
            <div class="ab-card__article">
              <p>KURONAMI 2.0 landed with Patch 12.08 (V26A3) as the follow-up to the original set, with a different weapon lineup from 1.0 and the usual upgraders and variants. Holo Meridian followed on 16 April 2026 and covers five weapons across the roles players actually buy for.</p>
              <p>Both sit in the premium bracket. Kuronami 2.0 was expected to hold the 1.0 price, around 6,760 VP, since the set is a gold-tier collection; Holo Meridian is priced in line with the recent premium bundles &mdash; expensive, but not out of step with what Riot has been charging.</p>
              <p>What they share is shape: a melee in the bundle, variants on the guns, and the same choice between buying the set whole and picking single weapons from the store. The bundle is the better rate per weapon; the single is the better buy if you only use one gun.</p>
              <p>If VP is running short, our <a href="/games/#valorant">VALORANT page</a> lists the tiers in USD. Compare the pack you would need against the bundle price rather than against the discount on the pack.</p>
              <p class="ab-card__source">Source: Riot Games patch notes and previews, April 2026.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="arknights-endfield-currency">
        <div class="ab-card__media">
          <img src="/assets/news/top-up-arknights-endfield-secure-instant-game-currency-at-topuplive/cover.jpg" alt="Arknights: Endfield key art" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Arknights: Endfield Currency: What It Buys and How a Top-Up Delivers</h3>
          <p class="ab-card__meta"><time datetime="2026-02-05">5 Feb 2026</time> &middot; Arknights: Endfield</p>
          <p class="ab-card__excerpt">Premium currency in Endfield goes to operators, skins, resource packs and event passes. What a top-up needs from you &mdash; an ID, not a password &mdash; and how long it takes.</p>
          <details class="ab-fold ab-card__read">
            <summary class="ab-fold__summary">
              <span class="ab-fold__cue"><span class="ab-fold__cue-more">Read article</span><span class="ab-fold__cue-less">Show less</span></span>
            </summary>
            <div class="ab-card__article">
              <p>Endfield&rsquo;s economy runs on premium currency bought in packs. It pays for new operators and their storylines, skins, resource packs that speed up progression, and event passes &mdash; the same set of things that gives the shop its pull during a limited event.</p>
              <p>A third-party top-up asks for an ID, not a password. Delivery goes straight to the account with no code to redeem, and our <a href="/games/#arknights-endfield">Endfield page</a> works the same way: pick a tier, send the player ID in chat, and the balance lands within minutes.</p>
              <p>Three things are worth checking before ordering: the server and region the account sits on, the tier that matches the pack you would otherwise buy in-game, and the player ID itself &mdash; one wrong digit is the usual reason an order stalls. Orders that never deliver are refunded.</p>
              <p>Because Endfield&rsquo;s content arrives in waves, think in tiers rather than one large purchase: a small pack covers a single unlock, while the larger ones are for banner pulls and event passes.</p>
              <p class="ab-card__source">Source: Arknights: Endfield store listings, February 2026.</p>
            </div>
          </details>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="ea-fc-26-launch">
        <div class="ab-card__media">
          <img src="/assets/news/ea-fc-26-standard-edition-launches-september-26/cover.jpg" alt="EA FC 26 cover art" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">EA FC 26: The September Launch, Two Editions and the FUT Rework</h3>
          <p class="ab-card__meta"><time datetime="2025-06-23">23 Jun 2025</time> &middot; EA FC</p>
          <p class="ab-card__excerpt">Standard Edition launched on 26 September with Ultimate buyers a week early. What each edition cost, what pre-ordering bought, and how Ultimate Team changed.</p>
          <details class="ab-fold ab-card__read">
            <summary class="ab-fold__summary">
              <span class="ab-fold__cue"><span class="ab-fold__cue-more">Read article</span><span class="ab-fold__cue-less">Show less</span></span>
            </summary>
            <div class="ab-card__article">
              <p>EA FC 26 shipped on 26 September 2025, with Ultimate Edition buyers getting seven days of early access from 19 September &mdash; the head start EA has run for years. Standard Edition was priced at around &pound;55 / $70 and the Ultimate at &pound;80 / $100; the Chinese Steam region listed it at 248 CNY.</p>
              <p>Pre-ordering the Ultimate Edition before 26 August carried in-game bonuses. A Switch 2 version was expected under EA&rsquo;s partnership with Nintendo but was never confirmed for that launch window.</p>
              <p>Ultimate Team took the structural work: Roles and PlayStyles reworked how positions behave, eight new FUT Heroes slipped out through partner studio Nexon, and an open-world &ldquo;exploration&rdquo; mode was reported as in early development. EA&rsquo;s stated goal, after a divisive FC 25 cycle, was a reset aimed at lapsed players.</p>
              <p>Coins decide how quickly a FUT squad comes together. If you are starting fresh, buy them in tiers as you build rather than in one lump &mdash; our <a href="/games/">game top-up pages</a> list what we carry.</p>
              <p class="ab-card__source">Source: EA Sports announcements and launch coverage, 2025.</p>
            </div>
          </details>
        </div>
      </article>

    </div>
  </section>

</div>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": "https://acebase.cc/blog/",
      "url": "https://acebase.cc/blog/",
      "name": "Game News | Patch Notes, Guides & Launch Dates",
      "description": "Game news and guides: Delta Force ammo charts, AFK Journey and ZZZ patch notes, K/DA skins, VALORANT bundles and EA FC 26. Read the condensed story in place.",
      "inLanguage": "en",
      "isPartOf": {"@type": "WebSite", "name": "AceBase", "url": "https://acebase.cc/"}
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://acebase.cc/"},
        {"@type": "ListItem", "position": 2, "name": "Game News", "item": "https://acebase.cc/blog/"}
      ]
    },
    {
      "@type": "ItemList",
      "numberOfItems": 9,
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "item": {"@type": "NewsArticle", "name": "Delta Force Ammo Chart: Which Rounds Beat Which Armour", "url": "https://acebase.cc/blog/#delta-force-ammo", "datePublished": "2026-10-21"}},
        {"@type": "ListItem", "position": 2, "item": {"@type": "NewsArticle", "name": "AFK Journey 1.8.2: Marene, Baden and Thane Join the Veil of Memories Season", "url": "https://acebase.cc/blog/#afk-journey-182", "datePublished": "2026-10-21"}},
        {"@type": "ListItem", "position": 3, "item": {"@type": "NewsArticle", "name": "ZZZ 3.3 City Fund: Growth vs Premium, and What the Certificate Buys", "url": "https://acebase.cc/blog/#zzz-city-fund", "datePublished": "2026-10-21"}},
        {"@type": "ListItem", "position": 4, "item": {"@type": "NewsArticle", "name": "ZZZ Spooky Funhouse Tales: Scare the Guests, Keep the Outfit", "url": "https://acebase.cc/blog/#zzz-spooky-funhouse", "datePublished": "2026-10-21"}},
        {"@type": "ListItem", "position": 5, "item": {"@type": "NewsArticle", "name": "K/DA FIRESTARTER: Four Skins, Patch 26.22 and What They Cost in RP", "url": "https://acebase.cc/blog/#lol-kda-firestarter", "datePublished": "2026-10-21"}},
        {"@type": "ListItem", "position": 6, "item": {"@type": "NewsArticle", "name": "Free Bigo Live Diamonds: What Actually Works", "url": "https://acebase.cc/blog/#bigo-free-diamonds", "datePublished": "2026-05-18"}},
        {"@type": "ListItem", "position": 7, "item": {"@type": "NewsArticle", "name": "Kuronami 2.0 and Holo Meridian: The Two Bundles That Shipped in April", "url": "https://acebase.cc/blog/#valorant-bundles", "datePublished": "2026-04-15"}},
        {"@type": "ListItem", "position": 8, "item": {"@type": "NewsArticle", "name": "Arknights: Endfield Currency: What It Buys and How a Top-Up Delivers", "url": "https://acebase.cc/blog/#arknights-endfield-currency", "datePublished": "2026-02-05"}},
        {"@type": "ListItem", "position": 9, "item": {"@type": "NewsArticle", "name": "EA FC 26: The September Launch, Two Editions and the FUT Rework", "url": "https://acebase.cc/blog/#ea-fc-26-launch", "datePublished": "2025-06-23"}}
      ]
    }
  ]
}
</script>
