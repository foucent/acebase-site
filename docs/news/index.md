---
title: 游戏资讯 | 新作、测试与发售动态
description: AceBase 游戏资讯：新作、测试与发售消息一条一张卡，卡片沿用站内服务卡尺寸，点开在卡里读压缩稿、看图集。首条《宇宙人哈鲁奥》：第三人称射击新作，支持简繁中文。
updated: 2026-10-20
hide:
  - title
  - toc
---

<!-- 2026-10-20：新增 NEWS 类目，nav 第一格（原来的 HOME 让位，首页 / 仍由
     gen_home.py 生成，点字标 ACEBASE 回去）。正文中文、nav 标签英文，和全站
     一致。

     这一页的前身是 /card-test/ 的排版测试页：用户给了一篇 gamebase 新闻
     https://news.gamebase.com.tw/news/detail/99441732
     （《宇宙人哈鲁奥》/《宇宙人ハルオ君》，第三人称射击，PC Steam），
     要求「以 /services/ 上 无畏契约 电脑调试 $9.9 那张卡的大小为模板」排成
     一张卡看效果。看过之后决定把它留成正式的资讯页，于是：
       · 页面搬到 /news/，资产目录一并搬到 docs/assets/news/；
       · 卡片去掉 $9.9（资讯不卖东西），动作行从「购买」改成「阅读原文」，
         新窗口打开原文，rel="noopener"；
       · 页面文案改成真的资讯页介绍，不再是测试页。

     卡片结构照 /services/ 的 ab-card--service 原样：1:1 方框（240×240）、
     一行摘要、动作行只有一个链接。区别只有标题里没有 ab-card__price，
     动作链接不是 ab-crisp-open。

     封面 docs/assets/news/haruo/01.jpg 由 _tmp_ocr/prep_cardtest_cover.py
     生成：新闻主图是 1440×810，标题字压在下面三分之一，直接裁成方图会把
     标题切掉，所以用同一张图放大模糊、压暗做底，整张 16:9 原图居中叠上去，
     得到 1440×1440 的方图，方框里铺满不留白。

     以后加一条资讯：复制这张卡、换 id 与封面，日期写进本页 frontmatter 的
     updated:（gen_home.py 靠它给首页取最新六张）。

     2026-10-20 第二版（用户：「阅读原文 不需跳转到原页面，而是将原页面中的
     内容进行压缩，点击阅读原文后是一个展开效果，并将原文中的图片变成灯箱
     效果」）：
       · 动作行不再是外链，改成 <details class="ab-fold">，「阅读原文 / 收起」
         就在原来那一行，展开后文章的压缩稿排在卡里 —— 和 /games/gpu-deals/
         的显卡说明用同一个折子组件（uncrate.css 的 ab-fold），键盘可开、
         关掉 JS 也能开。
       · 展开的是压缩稿，不是原文全文：四段（发布信息 / 世界与玩法 / 复制体
         的代价 / 语音），繁转简，来源行写在文末；原文不再外链。
       · 四张图 02–05 按原文顺序排成 2×2 缩略图，点开是站内的灯箱
         （photo-wall.js），可以左右翻，Esc 关。素材由 _tmp_ocr/prep_haruo_shots.py
         从原文 1440×810 缩到 1000 宽写进 docs/assets/news/haruo/。
         01.jpg 仍是那张方封面，不进图集。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <header class="ab-section__head">
      <h1 class="ab-section__title">游戏资讯</h1>
    </header>
    <p class="ab-section__lead">游戏资讯：新作、测试与发售的消息，一条一张卡，卡片尺寸沿用站内的服务卡。卡片上是一段摘要，点「阅读原文」在卡里展开这篇消息的压缩稿，文中的图点开看大图。</p>
  </section>

  <section class="ab-section">
    <div class="ab-list ab-list--expandable ab-list--pricing">
    <article class="ab-card ab-card--brand ab-card--plate ab-card--service ab-card--news" id="haruo-news-card">
      <div class="ab-card__media">
        <img src="/assets/news/haruo/01.jpg" alt="《宇宙人哈鲁奥》游戏主视觉" fetchpriority="high" decoding="async">
      </div>
      <div class="ab-card__copy">
        <h3 class="ab-card__title">宇宙人哈鲁奥</h3>
        <p class="ab-card__excerpt">第三人称射击新作：在沉没的科研设施里探索、回收物资，对付战前防卫系统与实验生物；复制体死后再生产，但基因会劣化。支持简繁中文，发售日未定。</p>
        <details class="ab-fold ab-card__read">
          <summary class="ab-fold__summary">
            <span class="ab-fold__cue"><span class="ab-fold__cue-more">阅读原文</span><span class="ab-fold__cue-less">收起</span></span>
          </summary>
          <div class="ab-card__article">
            <p>独立发行商 Waku Waku Games 宣布，由モヤシ技研开发的第三人称射击游戏《宇宙人哈鲁奥》将推出 PC（Steam）版，商店页已经上线，支持日文、英文、繁体中文与简体中文，发售日未定。</p>
            <div class="ab-card__shots">
              <a class="ab-news-shot" href="/assets/news/haruo/02.jpg" data-gallery="[&quot;/assets/news/haruo/02.jpg&quot;, &quot;/assets/news/haruo/03.jpg&quot;, &quot;/assets/news/haruo/04.jpg&quot;, &quot;/assets/news/haruo/05.jpg&quot;]" data-start="0" data-buy="" data-caption="宇宙人哈鲁奥 · 主视觉" aria-label="查看大图：主视觉"><img src="/assets/news/haruo/02.jpg" alt="《宇宙人哈鲁奥》主视觉" loading="lazy" decoding="async"></a>
              <a class="ab-news-shot" href="/assets/news/haruo/03.jpg" data-gallery="[&quot;/assets/news/haruo/02.jpg&quot;, &quot;/assets/news/haruo/03.jpg&quot;, &quot;/assets/news/haruo/04.jpg&quot;, &quot;/assets/news/haruo/05.jpg&quot;]" data-start="1" data-buy="" data-caption="宇宙人哈鲁奥 · 与实验生物交火" aria-label="查看大图：与实验生物交火"><img src="/assets/news/haruo/03.jpg" alt="《宇宙人哈鲁奥》与实验生物交火" loading="lazy" decoding="async"></a>
              <a class="ab-news-shot" href="/assets/news/haruo/04.jpg" data-gallery="[&quot;/assets/news/haruo/02.jpg&quot;, &quot;/assets/news/haruo/03.jpg&quot;, &quot;/assets/news/haruo/04.jpg&quot;, &quot;/assets/news/haruo/05.jpg&quot;]" data-start="2" data-buy="" data-caption="宇宙人哈鲁奥 · 设施内部" aria-label="查看大图：设施内部"><img src="/assets/news/haruo/04.jpg" alt="《宇宙人哈鲁奥》设施内部" loading="lazy" decoding="async"></a>
              <a class="ab-news-shot" href="/assets/news/haruo/05.jpg" data-gallery="[&quot;/assets/news/haruo/02.jpg&quot;, &quot;/assets/news/haruo/03.jpg&quot;, &quot;/assets/news/haruo/04.jpg&quot;, &quot;/assets/news/haruo/05.jpg&quot;]" data-start="3" data-buy="" data-caption="宇宙人哈鲁奥 · 过场演出" aria-label="查看大图：过场演出"><img src="/assets/news/haruo/05.jpg" alt="《宇宙人哈鲁奥》过场演出" loading="lazy" decoding="async"></a>
            </div>
            <p>世界因战争与气候变化沉入海底。两名主角「鞍月枫」与「黑石梢」潜入被遗弃的水下科研设施，一边回收物资，一边寻找过去某项计划造出的神秘物体。设施里还留着战前的防卫系统与各种实验生物，是把敌人清光，还是避开它们悄悄完成任务，由玩家决定。</p>
            <p>两人都是复制技术的产物：死后可以重新生产复活，但基因会劣化，被击败的次数越多能力越弱，任务也越难。探索时还要管身体状态——长时间不进食会饿得跑不动，吃太多会呕吐，出发前记得给她们上厕所的时间。</p>
            <p>发售日目前未定；据开发团队在 X 上的说法，游戏一部分场景会有全语音演出。</p>
            <p class="ab-card__source">来源：游戏基地 Gamebase，2026-10-20</p>
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
      "@id": "https://acebase.cc/news/",
      "url": "https://acebase.cc/news/",
      "name": "游戏资讯 | 新作、测试与发售动态",
      "description": "AceBase 游戏资讯：新作、测试与发售消息一条一张卡，点开在卡里读压缩稿、看图集。",
      "inLanguage": "zh-CN",
      "isPartOf": {"@type": "WebSite", "name": "AceBase", "url": "https://acebase.cc/"}
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "首页", "item": "https://acebase.cc/"},
        {"@type": "ListItem", "position": 2, "name": "游戏资讯", "item": "https://acebase.cc/news/"}
      ]
    },
    {
      "@type": "ItemList",
      "numberOfItems": 1,
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "NewsArticle",
            "name": "宇宙人哈鲁奥",
            "url": "https://news.gamebase.com.tw/news/detail/99441732"
          }
        }
      ]
    }
  ]
}
</script>
