---
title: News
description: AceBase News — free-game offers worth claiming, and the ones about to cost money.
hide:
  - title
  - toc
---

<!-- 2026-11-08 用户：「将 http://127.0.0.1:8003/news/ 以 …/guides/ 为模板，将
     https://www.4gamers.com.tw/news/category/1118/限時免費🆓 页中的限制免费的前10条
     内容添加进来」。这一页原先是手写占位（一张空网格 + 一句 "Nothing here yet"，
     商品在更早一次被搬去了 /top-ups/），现在换成和 /guides/ 一样的行卡列表：
     `.ab-mag` 里一节 `.ab-section`，`.ab-newsfeed` 十张 `.ab-card--row`
     （16:9 封面 1000×563、标题、kicker、两行导语、一行动作），没有页头也没有
     小节标题 —— /guides/ 那天刚把标题和横线删掉，模板就照它现在的样子来。

     文案是自己写的英文摘要，不搬原文；**页面上不出现来源站名，也不链到来源站**。
     封面取各篇的横幅图，居中裁 16:9 缩到 1000×563，落在
     /assets/news/<slug>/cover.jpg —— 与 2026-10-22 那批 /blog/ 卡同一套路径约定。
     抓取脚本在 _tmp_ocr：`news4g_articles.py`（正文）、`news4g_links.py`
     （商店链接）、`news4g_covers.py`（封面）。列表来自该分类的 `of-category`
     接口（站点是 SPA，直接开页面抓不到）。

     取的是该分类当时的第 1~10 条，**第 4 条是 DLsite R18 成人作品**，不放到
     这个站上，用第 11 条（Hexologic）补位 —— 所以是十条、不是十条加一条。
     顺序按分类的时间倒序（新的在上）。其中三条（A New Beginning、Asleep、
     Hexologic）抓取时活动已经结束，卡片照实写「Ran until …」。

     2026-11-08 晚用户：「不要直接跳到商店页，而是要有详情页我，在详情页里再跳转
     到商店页」。所以**卡片的三个链接现在都指 /news/<slug>/ 详情页，动作行改成
     「See the details」，这一页上不再有任何商店外链**；商店链接只出现在
     `docs/news/<slug>/index.md` 里，版式照 /guides/ 的详情页（hero + 带小节标题的
     表格与段落）。加一条新的限免内容时，要同时建一张卡和一页详情。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <div class="ab-newsfeed" aria-label="News">

      <article class="ab-card ab-card--row" id="good-morning-human">
        <div class="ab-card__media">
          <a href="/news/good-morning-human/"><img src="/assets/news/good-morning-human/cover.jpg" alt="GMH - Good Morning Human cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/news/good-morning-human/">GMH - Good Morning Human is free to keep on the Epic Games Store</a></h3>
          <p class="ab-card__meta">Epic Games Store · Free until Nov 9</p>
          <p class="ab-card__excerpt">A synthwave racer from W-9000 Studio: steer a ship down neon tracks, dodge what the track throws at you and shoot the barriers you cannot. A developer-run giveaway, so it never reaches the store's front page.</p>
          <p class="ab-card__more"><a href="/news/good-morning-human/">See the details</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="flotsam">
        <div class="ab-card__media">
          <a href="/news/flotsam/"><img src="/assets/news/flotsam/cover.jpg" alt="Flotsam cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/news/flotsam/">Flotsam is this week's free game on the Epic Games Store</a></h3>
          <p class="ab-card__meta">Epic Games Store · Free until Nov 13</p>
          <p class="ab-card__excerpt">Pajama Llama's ocean survival builder — raft floating junk into a town, desalinate, purify your catch and keep a people alive with no land left. This week's giveaway also carries an Idle Champions pack.</p>
          <p class="ab-card__more"><a href="/news/flotsam/">See the details</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="last-gambit">
        <div class="ab-card__media">
          <a href="/news/last-gambit/"><img src="/assets/news/last-gambit/cover.jpg" alt="Last Gambit cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/news/last-gambit/">Last Gambit goes paid on Nov 13, and is free to keep until then</a></h3>
          <p class="ab-card__meta">Steam · Free until Nov 13</p>
          <p class="ab-card__excerpt">Trabucco team's roguelike chess: start with nothing, then grow an army of 27 pieces — a knight that turns into a unicorn, a queen that steps off the board — up a branching map. The 1.0 launch ends the free run.</p>
          <p class="ab-card__more"><a href="/news/last-gambit/">See the details</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="epic-world-hunt-for-quest">
        <div class="ab-card__media">
          <a href="/news/epic-world-hunt-for-quest/"><img src="/assets/news/epic-world-hunt-for-quest/cover.jpg" alt="Epic World - Hunt For Quest cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/news/epic-world-hunt-for-quest/">Epic World - Hunt For Quest is free to keep on Epic this week</a></h3>
          <p class="ab-card__meta">Epic Games Store · Free until Nov 9</p>
          <p class="ab-card__excerpt">Yash Future Tech's platformer: 42 levels across seven worlds, three characters, thirteen kinds of enemy and a chest of gold to take back from an orc king. Another developer-run giveaway that never shows on the front page.</p>
          <p class="ab-card__more"><a href="/news/epic-world-hunt-for-quest/">See the details</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="quiztopia">
        <div class="ab-card__media">
          <a href="/news/quiztopia/"><img src="/assets/news/quiztopia/cover.jpg" alt="Quiztopia: The Ultimate Trivia cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/news/quiztopia/">Quiztopia: The Ultimate Trivia is free on Epic until Nov 9</a></h3>
          <p class="ab-card__meta">Epic Games Store · Free until Nov 9</p>
          <p class="ab-card__excerpt">Six question sets — maths, science, geography, general knowledge, English and pictures — with ten levels each. It normally sells for about NT$110, and this giveaway closes early on the morning of Nov 9.</p>
          <p class="ab-card__more"><a href="/news/quiztopia/">See the details</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="gladiator-blades-of-fury">
        <div class="ab-card__media">
          <a href="/news/gladiator-blades-of-fury/"><img src="/assets/news/gladiator-blades-of-fury/cover.jpg" alt="Gladiator: Blades of Fury cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/news/gladiator-blades-of-fury/">Gladiator: Blades of Fury is free to keep on Epic this week</a></h3>
          <p class="ab-card__meta">Epic Games Store · Free until Nov 9</p>
          <p class="ab-card__excerpt">Medieval melee from Yash Future Tech: four tribes, twenty fighters, combos and slow-motion counters across seven arenas, in tournaments or quick matches. Developer-run, so it never appears on the store's front page.</p>
          <p class="ab-card__more"><a href="/news/gladiator-blades-of-fury/">See the details</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="a-new-beginning-final-cut">
        <div class="ab-card__media">
          <a href="/news/a-new-beginning-final-cut/"><img src="/assets/news/a-new-beginning-final-cut/cover.jpg" alt="A New Beginning: Final Cut cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/news/a-new-beginning-final-cut/">A New Beginning: Final Cut was free on GOG for 24 hours</a></h3>
          <p class="ab-card__meta">GOG · Ran until Nov 2</p>
          <p class="ab-card__excerpt">Daedalic's point-and-click about a time traveller trying to stop a climate catastrophe, drawn as a graphic novel with animated comic panels. The 24-hour window shut on Nov 2; copies claimed then stay in the library.</p>
          <p class="ab-card__more"><a href="/news/a-new-beginning-final-cut/">See the details</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="asleep-act-1">
        <div class="ab-card__media">
          <a href="/news/asleep-act-1/"><img src="/assets/news/asleep-act-1/cover.jpg" alt="Asleep: Act 1 cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/news/asleep-act-1/">Asleep: Act 1 was free to keep on Steam until Nov 3</a></h3>
          <p class="ab-card__meta">Steam · Ran until Nov 3</p>
          <p class="ab-card__excerpt">Black Hole Games' pixel horror: Ana Lúcia is lost in her own nightmare and a torch is all that stands between her and the dark — some enemies flee the light, some hunt it. The free window closed on Nov 3.</p>
          <p class="ab-card__more"><a href="/news/asleep-act-1/">See the details</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="colleccct">
        <div class="ab-card__media">
          <a href="/news/colleccct/"><img src="/assets/news/colleccct/cover.jpg" alt="Colleccct cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/news/colleccct/">Colleccct is free on Steam, and heading for a $1 price</a></h3>
          <p class="ab-card__meta">Steam · Free for now</p>
          <p class="ab-card__excerpt">middlepattern's incremental shooter: a craft fires on its own, abstract shapes burst into motes, and the motes buy upgrades without a pause. The developer is moving it to a one-dollar price to fund the next update.</p>
          <p class="ab-card__more"><a href="/news/colleccct/">See the details</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row" id="hexologic">
        <div class="ab-card__media">
          <a href="/news/hexologic/"><img src="/assets/news/hexologic/cover.jpg" alt="Hexologic cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/news/hexologic/">Hexologic was free to keep on Steam for two days</a></h3>
          <p class="ab-card__meta">Steam · Ran until Nov 1</p>
          <p class="ab-card__excerpt">MythicOwl's sudoku on a hexagonal grid: fill the cells so every line, in all three directions, sums to the number on its edge, across six worlds and ninety levels. The two-day window closed on Nov 1.</p>
          <p class="ab-card__more"><a href="/news/hexologic/">See the details</a></p>
        </div>
      </article>
    </div>
  </section>

</div>
