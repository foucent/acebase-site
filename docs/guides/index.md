---
title: Guides
description: AceBase Guides — the settings sheet for every game we cover.
hide:
  - title
  - toc
---

<!-- 2026-11-01 按用户要求重排（「将 http://127.0.0.1:8000/curated/ 以
     http://127.0.0.1:8003/blog/ 为模板 1:1 进行排版，并从 /blog/ 取三条内容
     进行样式填充」）。同日 CURATED 改名 **PICKS**（用户：「/curated/ 改成
     picks」）：目录 docs/curated/ → docs/picks/、地址 /curated/ → /picks/、
     nav 标签与页内 title/description/h1 一起改，旧地址没有留存根。
     隔天 PICKS 又改名 **STACK**（2026-11-02，用户「将 picks 改为STACK」）：
     目录 docs/picks/ → docs/guides/、地址 /picks/ → /guides/、导航标签、首页
     那张卡与页内 title/description/h1 一起改；/picks/ 同样不留跳转，
     与 /curated/ 同待遇。

     版式 1:1 取自 acebase.cc 的 /blog/：`.ab-mag` 里两节 —— 第一节是
     `.ab-section` 的页头（h1 + 导语），第二节的 `.ab-newsfeed` 里每条一张
     `.ab-card--row` 横排卡（左 16:9 封面，右标题 / 日期·分类 / 两三行摘要）。
     这套 CSS 在两个站是同源的，uncrate.css 里 `.ab-newsfeed` 与
     `.ab-card--row` 那一段逐字相同，所以本页不用新增任何样式。

     内容：取了 /blog/ 最新的三条（PUBG × IVE Love Dive、Delta Force Ammo、
     AFK Journey 1.8.2），标题、日期、分类、摘要与封面图一字未改；封面从
     acebase.cc 的 docs/assets/news/<slug>/cover.jpg 原样拷到本站同路径
     （1000x563，16:9，无需裁切）。

     问过之后定的两件事：「Read article」动作行**去掉**（本站没有文章详情页，
     不外链到 8003），原来那 10 张收藏品卡片**删除**（整页备份在
     C:\tmp\sumei\retired_pages\curated-products-2026-11-01\；它们用到的
     /assets/archive/ 图片未动）。

     /blog/ 页尾那段 ItemList JSON-LD 没有搬过来：它写的是 acebase.cc 的
     绝对地址与本页不存在的详情页，搬过来只会输出错的结构化数据。

     2026-11-02 加第二段「Tool Stack」：用户给了 10 个网站（Raycast Store、
     Product Hunt、v0、Awesome-Selfhosted、Open Source Agenda、shadcn/ui、
     Linear、AlternativeTo、Arc Boosts Gallery、Terminal Trove），要求按本页
     版式收录，封面图自找、每条给一个到站点的按钮。卡片沿用 .ab-card--row，
     多挂 .ab-card--tool，按钮样式见 uncrate.css 的「the directory cards」段。
     封面是各站首页的 1600×900 截图（`_tmp_ocr/stack_shots.py` 等脚本，代理
     10808），居中裁 16:9 缩到 1000×563，放在 /assets/guides/<slug>/cover.jpg。

     几处要留意的事实（卡上照实写，不替它们圆场）：
     - v0.dev 现在 301 到 v0.app，按钮指向 v0.app。
     - opensourceagenda.com 已易主（301 到 ucrothrealty.com），站点没了，
       卡片按钮指向 Wayback 存档。
     - Product Hunt、AlternativeTo 会挡爬虫（Cloudflare），封面取自 Wayback
       快照，按钮仍指活的站点。
     - arc.net/boosts 已 301 回 arc.net（Arc 2026-12-22 停服），封面用 2023
       年的 Boosts Gallery 快照，按钮仍指原地址。

     同日用户又让删掉 /blog/ 搬来的那三张新闻卡（PUBG × IVE、Delta Force、
     AFK Journey，连带它们那节 `.ab-newsfeed`），只留站点目录；页头 H1 与
     「Tool Stack」小标题当次保留、页头导语改成目录的说法。同一天稍后用户
     又要求「全站都删除类似这样的小标题」，页头那节（h1「Stack」+ 导语）随之
     删掉，只留「Tool Stack」小节标题。封面文件
     /assets/news/<slug>/cover.jpg 没删（资源不跟内容走），页面上已无引用。

     2026-11-08 又加了一节「Settings Guides」：19 个游戏的设置速查页，每页一个
     目录 docs/guides/<slug>/、一个地址 /guides/<slug>/，卡是内链（与上面十张
     外链工具卡不同）。同一天用户说「将导航和目录 stack改为guides」，于是
     docs/stack/ → docs/guides/、/stack/ → /guides/、nav 标签 STACK → GUIDES，
     十九个子页与 /assets/stack/ → /assets/guides/ 一起搬；旧地址 /stack/ 与
     /assets/stack/ 都不留存根（与本工作区改名惯例一致）。小节标题「Tool Stack」
     是这批工具自己的名字，没跟着改。

     2026-11-08 用户把这一整段（「Tool Stack」小标题 + 十张工具卡）贴回来，
     说「这些内容删除」：两节整段删掉，页面只剩 Settings Guides 一节（十九张
     设置速查卡）。十张卡的外链、摘要、封面文件与 uncrate.css 的
     .ab-card--tool 样式都没删（资源不跟内容走，样式以后可能还用）；十九个
     详情页页脚原来说「rest of the Tool Stack」，一并改成只提设置速查
     （_tmp_ocr/ps_pages_finish.py 的 FOOT 同步改，免得重跑又写回旧话）。 -->

<div class="ab-mag" markdown="0">

  <!-- 2026-11-08 紧接着那一次：用户「Settings Guides 和下面的横线也去掉」，
       连带 <header class="ab-section__head"> 一起删（横线就是它的
       border-bottom），id="settings-guides" 挂到装卡片的 <section> 上，
       十九个详情页页脚的 /guides/#settings-guides 照旧能跳到网格。
       下面两块是 ps_pages_finish.py 的生成区，改模板才算数。 -->
  <!-- settings-guides:start -->
  <section class="ab-section" id="settings-guides">
    <div class="ab-newsfeed" aria-label="Settings guides">

      <article class="ab-card ab-card--row ab-card--guide" id="cs2-settings">
        <div class="ab-card__media">
          <a href="/guides/cs2-settings/"><img src="/assets/guides/settings/cs2-settings.jpg" alt="CS2 settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/cs2-settings/">CS2 settings</a></h3>
          <p class="ab-card__meta">Tactical shooter</p>
          <p class="ab-card__excerpt">Counter-Strike 2 is won in small margins: a clear picture, accurate audio cues and a mouse that travels exactly as far as your hand expects.</p>
          <p class="ab-card__more"><a href="/guides/cs2-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="valorant-settings">
        <div class="ab-card__media">
          <a href="/guides/valorant-settings/"><img src="/assets/guides/settings/valorant-settings.jpg" alt="VALORANT settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/valorant-settings/">VALORANT settings</a></h3>
          <p class="ab-card__meta">Tactical shooter</p>
          <p class="ab-card__excerpt">With a time to kill this short, VALORANT rewards a clean picture and a sensitivity you can repeat under pressure far more than any visual flourish.</p>
          <p class="ab-card__more"><a href="/guides/valorant-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="fortnite-settings">
        <div class="ab-card__media">
          <a href="/guides/fortnite-settings/"><img src="/assets/guides/settings/fortnite-settings.jpg" alt="Fortnite settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/fortnite-settings/">Fortnite settings</a></h3>
          <p class="ab-card__meta">Battle royale</p>
          <p class="ab-card__excerpt">The game gives frames far more weight than looks, so a competitive build strips the graphics back and keeps the frame counter on screen.</p>
          <p class="ab-card__more"><a href="/guides/fortnite-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="apex-legends-settings">
        <div class="ab-card__media">
          <a href="/guides/apex-legends-settings/"><img src="/assets/guides/settings/apex-legends-settings.jpg" alt="Apex Legends settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/apex-legends-settings/">Apex Legends settings</a></h3>
          <p class="ab-card__meta">Battle royale</p>
          <p class="ab-card__excerpt">Apex Legends rewards a clean, high-frame image far more than it rewards good looks, and the pro scene builds its setups around that.</p>
          <p class="ab-card__more"><a href="/guides/apex-legends-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="warzone-settings">
        <div class="ab-card__media">
          <a href="/guides/warzone-settings/"><img src="/assets/guides/settings/warzone-settings.jpg" alt="Call of Duty: Warzone settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/warzone-settings/">Call of Duty: Warzone settings</a></h3>
          <p class="ab-card__meta">Battle royale</p>
          <p class="ab-card__excerpt">Warzone pays you back in frames: a fast, steady refresh rate tightens tracking and shortens the gap between your hand and the screen.</p>
          <p class="ab-card__more"><a href="/guides/warzone-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="pubg-settings">
        <div class="ab-card__media">
          <a href="/guides/pubg-settings/"><img src="/assets/guides/settings/pubg-settings.jpg" alt="PUBG: Battlegrounds settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/pubg-settings/">PUBG: Battlegrounds settings</a></h3>
          <p class="ab-card__meta">Battle royale</p>
          <p class="ab-card__excerpt">PUBG is a heavy game that rewards frames and clean sightlines over spectacle, so most of the visual menu gets pushed down.</p>
          <p class="ab-card__more"><a href="/guides/pubg-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="rainbow-six-siege-settings">
        <div class="ab-card__media">
          <a href="/guides/rainbow-six-siege-settings/"><img src="/assets/guides/settings/rainbow-six-siege-settings.jpg" alt="Rainbow Six Siege settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/rainbow-six-siege-settings/">Rainbow Six Siege settings</a></h3>
          <p class="ab-card__meta">Tactical shooter</p>
          <p class="ab-card__excerpt">Siege is a game of tiny silhouettes and one-shot angles, so clarity and a repeatable hand beat visual polish every time.</p>
          <p class="ab-card__more"><a href="/guides/rainbow-six-siege-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="overwatch-2-settings">
        <div class="ab-card__media">
          <a href="/guides/overwatch-2-settings/"><img src="/assets/guides/settings/overwatch-2-settings.jpg" alt="Overwatch 2 settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/overwatch-2-settings/">Overwatch 2 settings</a></h3>
          <p class="ab-card__meta">Hero shooter</p>
          <p class="ab-card__excerpt">Overwatch 2 holds a high frame rate on almost any hardware, so the settings that matter most are the ones that keep your view clean and your aim steady.</p>
          <p class="ab-card__more"><a href="/guides/overwatch-2-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="marvel-rivals-settings">
        <div class="ab-card__media">
          <a href="/guides/marvel-rivals-settings/"><img src="/assets/guides/settings/marvel-rivals-settings.jpg" alt="Marvel Rivals settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/marvel-rivals-settings/">Marvel Rivals settings</a></h3>
          <p class="ab-card__meta">Hero shooter</p>
          <p class="ab-card__excerpt">Marvel Rivals rewards a clean, fast picture more than a pretty one, so most of the work is deciding which effects you can live without.</p>
          <p class="ab-card__more"><a href="/guides/marvel-rivals-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="fragpunk-settings">
        <div class="ab-card__media">
          <a href="/guides/fragpunk-settings/"><img src="/assets/guides/settings/fragpunk-settings.jpg" alt="FragPunk settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/fragpunk-settings/">FragPunk settings</a></h3>
          <p class="ab-card__meta">Hero shooter</p>
          <p class="ab-card__excerpt">FragPunk runs well out of the box, but its video menu hides a second layer of switches that decide how much clutter sits between your crosshair and the enemy.</p>
          <p class="ab-card__more"><a href="/guides/fragpunk-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="the-finals-settings">
        <div class="ab-card__media">
          <a href="/guides/the-finals-settings/"><img src="/assets/guides/settings/the-finals-settings.jpg" alt="THE FINALS settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/the-finals-settings/">THE FINALS settings</a></h3>
          <p class="ab-card__meta">Shooter</p>
          <p class="ab-card__excerpt">Matches in THE FINALS are short and the arena keeps changing shape, so a clear picture and honest audio beat cinematic detail every time.</p>
          <p class="ab-card__more"><a href="/guides/the-finals-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="xdefiant-settings">
        <div class="ab-card__media">
          <a href="/guides/xdefiant-settings/"><img src="/assets/guides/settings/xdefiant-settings.jpg" alt="XDefiant settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/xdefiant-settings/">XDefiant settings</a></h3>
          <p class="ab-card__meta">Shooter</p>
          <p class="ab-card__excerpt">XDefiant settles fights in a blink, so a soft picture or a laggy input path costs you the trade before you can react.</p>
          <p class="ab-card__more"><a href="/guides/xdefiant-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="spectre-divide-settings">
        <div class="ab-card__media">
          <a href="/guides/spectre-divide-settings/"><img src="/assets/guides/settings/spectre-divide-settings.jpg" alt="Spectre Divide settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/spectre-divide-settings/">Spectre Divide settings</a></h3>
          <p class="ab-card__meta">Tactical shooter</p>
          <p class="ab-card__excerpt">This is a shooter built for competition, so the settings that matter are the ones that keep the picture clean and the frame rate high.</p>
          <p class="ab-card__more"><a href="/guides/spectre-divide-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="delta-force-settings">
        <div class="ab-card__media">
          <a href="/guides/delta-force-settings/"><img src="/assets/guides/settings/delta-force-settings.jpg" alt="Delta Force settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/delta-force-settings/">Delta Force settings</a></h3>
          <p class="ab-card__meta">Extraction shooter</p>
          <p class="ab-card__excerpt">Delta Force fights happen across wide maps where a clean, high frame rate beats film-quality lighting, and most of the heavy graphics options ship switched on.</p>
          <p class="ab-card__more"><a href="/guides/delta-force-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="arc-raiders-settings">
        <div class="ab-card__media">
          <a href="/guides/arc-raiders-settings/"><img src="/assets/guides/settings/arc-raiders-settings.jpg" alt="ARC Raiders settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/arc-raiders-settings/">ARC Raiders settings</a></h3>
          <p class="ab-card__meta">Extraction shooter</p>
          <p class="ab-card__excerpt">It is a game that rewards a clear picture more than a stripped-down one, so the baseline below keeps most of the scenery while cutting the options that cost latency or visibility.</p>
          <p class="ab-card__more"><a href="/guides/arc-raiders-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="battlefield-6-settings">
        <div class="ab-card__media">
          <a href="/guides/battlefield-6-settings/"><img src="/assets/guides/settings/battlefield-6-settings.jpg" alt="Battlefield 6 settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/battlefield-6-settings/">Battlefield 6 settings</a></h3>
          <p class="ab-card__meta">Shooter</p>
          <p class="ab-card__excerpt">Battlefield 6 is well optimized, but its defaults still put a lot of visual noise between you and the fight.</p>
          <p class="ab-card__more"><a href="/guides/battlefield-6-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="deadlock-settings">
        <div class="ab-card__media">
          <a href="/guides/deadlock-settings/"><img src="/assets/guides/settings/deadlock-settings.jpg" alt="Deadlock settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/deadlock-settings/">Deadlock settings</a></h3>
          <p class="ab-card__meta">MOBA shooter</p>
          <p class="ab-card__excerpt">Deadlock is still being patched, so the values that age best are the ones that keep the frame rate high and the picture clean.</p>
          <p class="ab-card__more"><a href="/guides/deadlock-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="dota-2-settings">
        <div class="ab-card__media">
          <a href="/guides/dota-2-settings/"><img src="/assets/guides/settings/dota-2-settings.jpg" alt="Dota 2 settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/dota-2-settings/">Dota 2 settings</a></h3>
          <p class="ab-card__meta">MOBA</p>
          <p class="ab-card__excerpt">Dota 2 is a light game by modern standards, so most of the picture-quality options can be turned down without touching the frame rate.</p>
          <p class="ab-card__more"><a href="/guides/dota-2-settings/">Open the settings</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--guide" id="league-of-legends-settings">
        <div class="ab-card__media">
          <a href="/guides/league-of-legends-settings/"><img src="/assets/guides/settings/league-of-legends-settings.jpg" alt="League of Legends settings cover" loading="lazy" decoding="async"></a>
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title"><a href="/guides/league-of-legends-settings/">League of Legends settings</a></h3>
          <p class="ab-card__meta">MOBA</p>
          <p class="ab-card__excerpt">League of Legends asks very little of your hardware, so the settings that pay off are the ones that clear the screen and shorten every click.</p>
          <p class="ab-card__more"><a href="/guides/league-of-legends-settings/">Open the settings</a></p>
        </div>
      </article>
    </div>
  </section>
  <!-- settings-guides:end -->

</div>
