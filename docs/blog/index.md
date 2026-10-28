---
title: "Game News | Patch Notes, Guides & Launch Dates"
description: "Game news and guides: PUBG × IVE Love Dive, Delta Force ammo charts, AFK Journey and ZZZ patch notes, K/DA skins and VALORANT bundles."
updated: 2026-10-29
hide:
  - title
  - toc
---

<!-- 2026-10-29：第十条（PUBG × IVE Love Dive）加在最前，ItemList 一并从 9 改成
     10、后续序号顺延；导语与 description 里点了这一条。封面由官方主视觉缩到
     1000x563，见 _tmp_ocr/pubg_ive_cover.py。 -->

<!-- 2026-10-22 第二版（用户：「blog每篇文章点击Read article后应该是跳到独立的
     详情页」）：行内折叠撤掉。九条正文各自搬到 docs/blog/<slug>/index.md
     （地址 /blog/<slug>/，slug 就是原来那一行的 id），行里只剩一个
     Read article 链接指过去；首页那一张随之变成外链（gen_home.py 整行搬，
     故链接一律写根绝对地址）。行内折叠用的 .ab-card--row 那几条
     （__read / __article / __source / ab-fold）随之删掉，详情页另起一套
     .ab-article 版式；本页 ItemList 改指九个独立地址，每个详情页带自己的
     NewsArticle JSON-LD。正文、封面、标题、摘要一字未改。

     2026-10-22：整页改成资讯列表（用户：「模仿 https://www.topuplive.com/news/
     页中的排版，并将第一页的内容添到 /blog/（把内容改成符合自己网站的），并去掉
     Haruo the Alien …… 卡片」）。问过之后定的两件事：**第一页内容全部改写进来**、
     **首页 BLOG 仍只取 1 张**。

     版式：topuplive 的资讯页是一列横排的条目 —— 左边 16:9 缩略图，右边标题、
     日期·分类、两三行摘要、Read More。这里原样搬过来，只换成站内语言：
     缩略图左、标题句首大写（站内卡片标题本是全大写，长标题全大写读不动，
     故这一种卡片单独关掉）、日期·分类一行小字、摘要两三行，折子仍是
     <details>（ab-fold），点开在同一行里展开压缩稿，不是外链。（行内折叠
     在当天第二版就换成独立页了，见上。）

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
    <p class="ab-section__lead">Patch notes, guides and launch coverage, newest first. Each story opens on a page of its own.</p>
  </section>

  <section class="ab-section">
    <div class="ab-newsfeed">

      <article class="ab-card ab-card--row" id="pubg-ive-love-dive">
        <div class="ab-card__media">
          <img src="/assets/news/pubg-ive-love-dive/cover.jpg" alt="The six members of IVE in school uniforms among ruined statues, under pink chrome LOVE DIVE lettering" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">PUBG × IVE Love Dive: Three Rondo Zones, Six Idols, a November Launch</h3>
          <p class="ab-card__meta"><time datetime="2026-10-28">28 Oct 2026</time> &middot; PUBG</p>
          <p class="ab-card__excerpt">KRAFTON&rsquo;s crossover with IVE puts three LOVE DIVE areas on Rondo and all six members in game as outfits, with themed clothing, armour, weapon skins and emotes. PC on 4 November, consoles on 12 November.</p>
          <p class="ab-card__more"><a href="/blog/pubg-ive-love-dive/">Read article</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="delta-force-ammo">
        <div class="ab-card__media">
          <img src="/assets/news/delta-force-ammo-chart-guide/cover.jpg" alt="Delta Force ammo chart guide cover" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Delta Force Ammo Chart: Which Rounds Beat Which Armour</h3>
          <p class="ab-card__meta"><time datetime="2026-10-21">21 Oct 2026</time> &middot; Delta Force</p>
          <p class="ab-card__excerpt">Ammo one level above the target&rsquo;s armour does full damage; one level below cuts it to a coin flip. The penetration table, what each tier costs per round, and what to carry.</p>
          <p class="ab-card__more"><a href="/blog/delta-force-ammo/">Read article</a></p>
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
          <p class="ab-card__more"><a href="/blog/afk-journey-182/">Read article</a></p>
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
          <p class="ab-card__more"><a href="/blog/zzz-city-fund/">Read article</a></p>
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
          <p class="ab-card__more"><a href="/blog/zzz-spooky-funhouse/">Read article</a></p>
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
          <p class="ab-card__more"><a href="/blog/lol-kda-firestarter/">Read article</a></p>
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
          <p class="ab-card__more"><a href="/blog/bigo-free-diamonds/">Read article</a></p>
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
          <p class="ab-card__more"><a href="/blog/valorant-bundles/">Read article</a></p>
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
          <p class="ab-card__more"><a href="/blog/arknights-endfield-currency/">Read article</a></p>
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
          <p class="ab-card__more"><a href="/blog/ea-fc-26-launch/">Read article</a></p>
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
      "description": "Game news and guides: PUBG × IVE Love Dive, Delta Force ammo charts, AFK Journey and ZZZ patch notes, K/DA skins and VALORANT bundles.",
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
      "numberOfItems": 10,
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "item": {"@type": "NewsArticle", "name": "PUBG × IVE Love Dive: Three Rondo Zones, Six Idols, a November Launch", "url": "https://acebase.cc/blog/pubg-ive-love-dive/", "datePublished": "2026-10-28"}},
        {"@type": "ListItem", "position": 2, "item": {"@type": "NewsArticle", "name": "Delta Force Ammo Chart: Which Rounds Beat Which Armour", "url": "https://acebase.cc/blog/delta-force-ammo/", "datePublished": "2026-10-21"}},
        {"@type": "ListItem", "position": 3, "item": {"@type": "NewsArticle", "name": "AFK Journey 1.8.2: Marene, Baden and Thane Join the Veil of Memories Season", "url": "https://acebase.cc/blog/afk-journey-182/", "datePublished": "2026-10-21"}},
        {"@type": "ListItem", "position": 4, "item": {"@type": "NewsArticle", "name": "ZZZ 3.3 City Fund: Growth vs Premium, and What the Certificate Buys", "url": "https://acebase.cc/blog/zzz-city-fund/", "datePublished": "2026-10-21"}},
        {"@type": "ListItem", "position": 5, "item": {"@type": "NewsArticle", "name": "ZZZ Spooky Funhouse Tales: Scare the Guests, Keep the Outfit", "url": "https://acebase.cc/blog/zzz-spooky-funhouse/", "datePublished": "2026-10-21"}},
        {"@type": "ListItem", "position": 6, "item": {"@type": "NewsArticle", "name": "K/DA FIRESTARTER: Four Skins, Patch 26.22 and What They Cost in RP", "url": "https://acebase.cc/blog/lol-kda-firestarter/", "datePublished": "2026-10-21"}},
        {"@type": "ListItem", "position": 7, "item": {"@type": "NewsArticle", "name": "Free Bigo Live Diamonds: What Actually Works", "url": "https://acebase.cc/blog/bigo-free-diamonds/", "datePublished": "2026-05-18"}},
        {"@type": "ListItem", "position": 8, "item": {"@type": "NewsArticle", "name": "Kuronami 2.0 and Holo Meridian: The Two Bundles That Shipped in April", "url": "https://acebase.cc/blog/valorant-bundles/", "datePublished": "2026-04-15"}},
        {"@type": "ListItem", "position": 9, "item": {"@type": "NewsArticle", "name": "Arknights: Endfield Currency: What It Buys and How a Top-Up Delivers", "url": "https://acebase.cc/blog/arknights-endfield-currency/", "datePublished": "2026-02-05"}},
        {"@type": "ListItem", "position": 10, "item": {"@type": "NewsArticle", "name": "EA FC 26: The September Launch, Two Editions and the FUT Rework", "url": "https://acebase.cc/blog/ea-fc-26-launch/", "datePublished": "2025-06-23"}}
      ]
    }
  ]
}
</script>
