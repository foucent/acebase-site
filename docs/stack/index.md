---
title: Stack
description: AceBase Stack — ten sites worth a tab, from open-source indexes to the places that launch new software.
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
     目录 docs/picks/ → docs/stack/、地址 /picks/ → /stack/、导航标签、首页
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
     10808），居中裁 16:9 缩到 1000×563，放在 /assets/stack/<slug>/cover.jpg。

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
     /assets/news/<slug>/cover.jpg 没删（资源不跟内容走），页面上已无引用。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <header class="ab-section__head">
      <h2 class="ab-section__title">Tool Stack</h2>
    </header>
  </section>

  <section class="ab-section">
    <div class="ab-newsfeed" aria-label="Tool Stack directory">

      <article class="ab-card ab-card--row ab-card--tool" id="raycast-store">
        <div class="ab-card__media">
          <img src="/assets/stack/raycast-store/cover.jpg" alt="The Raycast Store page: a dark hero over a grid of app icons" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Raycast Store</h3>
          <p class="ab-card__meta">Productivity &middot; macOS</p>
          <p class="ab-card__excerpt">Raycast&rsquo;s extension store: scripts, workflows and AI commands shelved like gear in a high-contrast dark interface. The clearest picture of what a modern desktop stack actually looks like.</p>
          <p class="ab-card__more"><a href="https://www.raycast.com/store" target="_blank" rel="noopener">Visit raycast.com</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--tool" id="product-hunt">
        <div class="ab-card__media">
          <img src="/assets/stack/product-hunt/cover.jpg" alt="Product Hunt&rsquo;s homepage with today&rsquo;s top products listed down the left and product landscapes on the right" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Product Hunt</h3>
          <p class="ab-card__meta">Launches &middot; Products</p>
          <p class="ab-card__excerpt">Where new SaaS, AI tools and indie open-source projects surface first, ranked by the people who build and use them. The daily list is the closest thing to a live map of what the industry is reaching for.</p>
          <p class="ab-card__more"><a href="https://www.producthunt.com/" target="_blank" rel="noopener">Visit producthunt.com</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--tool" id="v0">
        <div class="ab-card__media">
          <img src="/assets/stack/v0/cover.jpg" alt="The v0 landing page with a What do you want to create prompt box and template cards below it" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">v0 by Vercel</h3>
          <p class="ab-card__meta">Front-end &middot; AI</p>
          <p class="ab-card__excerpt">Vercel&rsquo;s generative UI builder: describe a screen, get components and code back. Monochrome, minimal and about as close to the front of AI-assisted front-end work as a tool gets.</p>
          <p class="ab-card__more"><a href="https://v0.app/" target="_blank" rel="noopener">Visit v0.app</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--tool" id="awesome-selfhosted">
        <div class="ab-card__media">
          <img src="/assets/stack/awesome-selfhosted/cover.jpg" alt="The Awesome-Selfhosted index with a category sidebar on the left and project entries carrying licence badges" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Awesome-Selfhosted</h3>
          <p class="ab-card__meta">Open source &middot; Self-hosting</p>
          <p class="ab-card__excerpt">The big list of self-hosted software: private clouds, NAS services, Docker apps. Everything you can run on your own box instead of renting by the month, sorted by what it does.</p>
          <p class="ab-card__more"><a href="https://awesome-selfhosted.net/" target="_blank" rel="noopener">Visit awesome-selfhosted.net</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--tool" id="open-source-agenda">
        <div class="ab-card__media">
          <img src="/assets/stack/open-source-agenda/cover.jpg" alt="Open Source Agenda&rsquo;s homepage with a project search box and the latest blog posts in a row" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Open Source Agenda</h3>
          <p class="ab-card__meta">Open source &middot; Index &middot; Archived</p>
          <p class="ab-card__excerpt">Open-source projects sorted by topic and stack, laid out as clean cards instead of a wall of READMEs. The domain has since changed hands, so the button opens the last good archive.</p>
          <p class="ab-card__more"><a href="https://web.archive.org/web/20240615233410/https://www.opensourceagenda.com/" target="_blank" rel="noopener">Visit the archive</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--tool" id="shadcn-ui">
        <div class="ab-card__media">
          <img src="/assets/stack/shadcn-ui/cover.jpg" alt="The shadcn/ui homepage over a grid of component previews" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">shadcn/ui</h3>
          <p class="ab-card__meta">Front-end &middot; Components</p>
          <p class="ab-card__excerpt">The open-source component library a good deal of the front-end world has standardised on: copied into your project as code, styled with Tailwind, dark by default. Cyberminimalism with the source in your hand.</p>
          <p class="ab-card__more"><a href="https://ui.shadcn.com/" target="_blank" rel="noopener">Visit ui.shadcn.com</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--tool" id="linear">
        <div class="ab-card__media">
          <img src="/assets/stack/linear/cover.jpg" alt="Linear&rsquo;s dark homepage with a product development headline above a screenshot of an issue board" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Linear</h3>
          <p class="ab-card__meta">Product &middot; Workflow</p>
          <p class="ab-card__excerpt">Issue tracking built for teams that live on the keyboard: instant transitions, tight shortcuts, a dark interface that has set the tone for a lot of software design since.</p>
          <p class="ab-card__more"><a href="https://linear.app/" target="_blank" rel="noopener">Visit linear.app</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--tool" id="alternativeto">
        <div class="ab-card__media">
          <img src="/assets/stack/alternativeto/cover.jpg" alt="AlternativeTo&rsquo;s homepage with a search box and rows of news cards about apps and their alternatives" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">AlternativeTo</h3>
          <p class="ab-card__meta">Open source &middot; Alternatives</p>
          <p class="ab-card__excerpt">Type in the paid app and get the free and open-source ones that do the same job, ranked by user votes. The most practical route off a subscription stack.</p>
          <p class="ab-card__more"><a href="https://alternativeto.net/" target="_blank" rel="noopener">Visit alternativeto.net</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--tool" id="arc-boosts">
        <div class="ab-card__media">
          <img src="/assets/stack/arc-boosts/cover.jpg" alt="Arc&rsquo;s Boost Gallery with a sidebar on the left and a grid of community remixes of Gmail, Twitter and YouTube" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Arc Boosts Gallery</h3>
          <p class="ab-card__meta">Browsers &middot; Customisation</p>
          <p class="ab-card__excerpt">Community CSS and JS remixes for the Arc browser, browsable by site. Arc is being wound down, so the gallery now reads as a record of what people did to their own internet.</p>
          <p class="ab-card__more"><a href="https://arc.net/boosts" target="_blank" rel="noopener">Visit arc.net/boosts</a></p>
        </div>
      </article>

      <article class="ab-card ab-card--row ab-card--tool" id="terminal-trove">
        <div class="ab-card__media">
          <img src="/assets/stack/terminal-trove/cover.jpg" alt="Terminal Trove&rsquo;s green-on-black homepage with a search box and buttons to explore or randomise a tool" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Terminal Trove</h3>
          <p class="ab-card__meta">CLI &middot; Terminal</p>
          <p class="ab-card__excerpt">A directory of terminal tools — TUI clients, CLI utilities, Rust rewrites — set in green on black for people who would rather not reach for the mouse. The hard end of the stack.</p>
          <p class="ab-card__more"><a href="https://terminaltrove.com/" target="_blank" rel="noopener">Visit terminaltrove.com</a></p>
        </div>
      </article>

    </div>
  </section>

</div>
