---
title: Premium gaming gear, priced and sourced
description: AceBase — premium gaming gear, priced and sourced for you. Paste a product link, get the lowest sourcing price by email, and have us buy and ship it.
icon: material/home
hide:
  - title
  - toc
---

<!-- This page was /gear/ until 2026-11-08, when the user asked for it to be the
     site's front door (「将 /gear/ 改成 /」, after 「将 /gear/ 变成 Home 页，然后 /
     指向这个页面」). The file moved here whole; /gear/ is gone rather than
     redirected, which is how this workspace retires an address (see
     /top-up/'s note on the same point). The ten-tile "Latest" feed that used
     to sit here was not thrown away: it moved to /latest/ (not in the nav) and
     gen_home_recent.py writes there now. Nothing inside the page changed — the
     hero, the email dialog, the three steps, the four banners and the shelf of
     cards are the ones described below. -->


<!-- DESIRE and GROOM became one STYLE page (2026-11-02, user: 「将 DESIRE GROOM
     合并成Style」). The Desire cards come first, then the Groom cards, each
     block in the order it had on its own page. Nothing inside a card changed:
     ids, data-gallery paths and the pictures themselves still live under
     /assets/desire/ and /assets/groom/, because an asset folder is a file name,
     not a category. -->

<!-- STYLE became MEDIA (2026-11-05, user: 「将 https://acebase.cc/style/ 改为
     MEDIA」): directory docs/style/ → docs/media/, address /style/ → /media/,
     nav label, page title, description, the list's aria-label and the two
     homepage tiles all followed. The cards did not move: their ids, order and
     pictures stay as they were, and the pictures keep their own folders
     (/assets/desire/, /assets/groom/ and the four /assets/style/ files the Air
     Jordan card uses) because an asset folder is a file name, not a category.
     /style/ is left with no redirect, same as /groom/, /curated/ and /picks/. -->

<!-- MEDIA became GEAR (2026-11-05, user: 「将 …/media/ 改成 gear」): directory
     docs/media/ → docs/gear/, address /media/ → /gear/, nav label, page title,
     description, the list's aria-label and the two homepage tiles all
     followed. /media/ is left with no redirect. The address /gear/ is the one
     this site gave up earlier the same day when GEAR became SUBS — the two
     renames do not overlap: that page moved to /subs/, this one moved in.
     The cards did not move, and the pictures keep their folders (/assets/
     desire/, /assets/groom/, /assets/style/ and /assets/gear/), because an
     asset folder is a file name, not a category. -->

<!-- Pruned to five cards (2026-11-05, user: 「将 18D Oil Shiny Pantyhose +
     Strappy Stiletto Sandals Request Sourcing 以后面的卡片删除」, then
     「… Request Sourcing 也删除」). Everything the page carried before the
     five keyboards is gone; the five keyboards are now the whole catalogue.
     The page as it stood before each cut is in C:\tmp\sumei\retired_pages\
     (gear-index-20261105-before-prune.md) and in git history. The pictures
     the deleted cards used are still on disk under /assets/desire/,
     /assets/groom/ and /assets/style/: the cards were removed, the files were
     not. -->

<!-- Rebuilt on the Superbuy homepage's layout (2026-11-08, user: 「将
     http://127.0.0.1:8003/gear/ 页面模仿 https://www.superbuy.com/cn/page/
     homepage/，不需要「大家都在聊什么？ 来自 Superbuy 社区的真实好物、晒单
     与心得。」的内容」). What came over, measured at 1440 on that page:
       hero          600px, gradient #f5faff → #e0f2ff 45% → #74a1e0, h1
                     36px/800, meta 14px/500 #6f6f78, search 760x64 white
                     radius 32 with a 48px #0559ff submit, white 36px chips;
       journey       white 1200x132 card radius 24 lifted 54px over the
                     hero's foot, three steps (left/centre/right), chevron
                     track with three #0559ff dots;
       feature row   four 304x136 banners;
       discovery     #f5f5f5 band, 48px padding, h2 24px/700, 12px pill tabs,
                     5-column grid of white 227x318 cards (1px #dedee0 border,
                     radius 16, 16px padding, square picture radius 14, one
                     line of title, action row at the foot).
     The community block is left out, as asked. Content is ours: the five
     keyboards, no prices (Request Sourcing is the action), and the four
     feature banners are shortcuts to the four catalogue pages (2026-11-08:
     Game → Top ups, Top-Up → News, Gift Cards → Gift-cards; later that day the
     News banner became a pointer at a page that was then only a placeholder, so
     its eyebrow said Coming soon and it carried no art — the Douyin picture
     belonged to a card that moved to /top-ups/. 2026-11-08 evening /news/ filled
     up with the free-game cards, so the eyebrow reads Free games now; the banner
     still carries no art because the strip is built for cut-out PNGs and the
     news pictures are photographs of game art). This page is HAND-MAINTAINED —
     like /news/ and unlike /cdkeys/, /gift-cards/
     and /top-ups/, nothing regenerates it. Card ids, data-gallery sets, alt text (no commas:
     data-gallery splits on them) and data-name values are unchanged, so the
     homepage tiles, the lightbox and the live-chat hand-off all keep working.
     Layout and behaviour: docs/stylesheets/gear.css and docs/javascripts/
     gear.js (search box + brand pills filter the grid). -->

<!-- The hero box became a price request, not a search (2026-11-08, user:
     「这部分的意思应该是 用户输入商品链接，我为他通过异步的方式获取最低采购
     价」). So the headline says paste a link, the button says Get price, and the
     three steps describe that round trip: link in, lowest sourcing price
     looked up, the answer mailed back. gear.js tells a link from a word: a link
     opens the email dialog below and only a word filters the grid, because five
     cards is a shelf worth narrowing. -->

<!-- The shelf became RECENT QUOTES (2026-11-08, user: 「将 … Browse the gear …
     部分改成最近报价」, then 「你编一下价格」). The band still holds the same
     five keyboards — same ids, pictures, data-gallery sets and data-name
     values, so the lightbox, the /latest/ tiles and the chat hand-off keep
     working — but the heading, the hero chip and the grid's aria-label now say
     recent quotes, each card prints the lowest price found, and the action
     reads Get this price. data-price on the button makes sourcing.js put that
     number in the chat message, so a click asks about the price on screen.
     The quote line carries no date: the first cut printed "Lowest · Nov 7"
     under the price and the user dropped it (「类似Lowest · Nov 7的日期不需要」).

     Later that evening the band became POPULAR GEAR (2026-11-08, user:
     「Recent quotes 要改成热门装备，然后从网络上搜索它们的价格，并将价格降低70%后
     进行更新」). The heading, the hero chip, the grid's aria-label and the lead
     all say Popular gear now; the action still reads Get this price.

     THE PRICES ARE NO LONGER MADE UP. Each one is 70% of that product's US
     retail price — a 7折 price, 30% off — rounded to the dollar; that is the
     sourcing price this shop offers.
     They were looked up on 2026-11-08 from the makers' own stores and the big
     US retailers (MSRP where the maker lists one, the standing retail price
     otherwise); nothing on the page names a source, and no retail figure is
     shown. Keep each in step with data-price — the probe checks that the
     printed price and the chat number are the same. -->

<!-- A copy pass (2026-11-08, user: 「这个页面的文字需要优化一下，它主要提供
     顶级电竞装备的价格查询和代购」). The page now says what the shop is for in
     its first line: premium gaming gear, with both halves of the offer — the
     lowest sourcing price and the purchase on the customer's behalf. The
     headline, the meta row, the search aria-label, the third journey step, the
     dialog footnote, the shelf lead and both chat openers were rewritten; the
     price mechanics did not change, and the numbers were the placeholders the
     user asked for until the Popular gear pass replaced them with real retail
     prices set at 70% of retail. "Source" is the word used for 代购
     throughout — nothing here says "official store", and no supplier is
     named.

     The meta row first said "Any store", which read as "we will buy anywhere"
     (2026-11-08, user: 「这里要表达的是通过正品渠道进行低价采购，而不是 Any
     store」). It now reads "Genuine retail channels": the offer is a low price
     reached through authentic channels, not a free-for-all. Step 1 still
     accepts a link from anywhere — that is how a request arrives — so it says
     "Paste any product link" instead. -->

<div class="ab-sb" markdown="0">

  <section class="ab-sb-hero">
    <div class="ab-sb-hero__art" aria-hidden="true">
      <img src="/assets/gear/razer-blackwidow-v4-75/01.jpg" alt="" loading="eager" decoding="async">
    </div>
    <div class="ab-sb-hero__inner ab-sb-inner">
      <div class="ab-sb-hero__copy">
        <h1 class="ab-sb-hero__title">Premium gaming gear, priced and sourced for you</h1>
        <p class="ab-sb-hero__meta">Genuine retail channels &middot; Lowest sourcing price &middot; Bought and shipped for you</p>
        <form class="ab-sb-search" id="gear-search-form" role="search">
          <label class="ab-sb-search__field">
            <svg class="ab-sb-search__icon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">
              <circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/>
              <path d="m16 16 5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
            <input type="text" id="gear-search" name="q" autocomplete="off" placeholder="Paste a product link" aria-label="Paste a product link and we will look up its lowest sourcing price">
          </label>
          <button class="ab-sb-search__submit" type="submit">Get price</button>
        </form>
        <p class="ab-sb-search__note" id="gear-note" aria-live="polite" hidden></p>
        <div class="ab-sb-hero__tools">
          <a class="ab-sb-chip" href="#gear">Popular gear</a>
          <a class="ab-sb-chip" href="#how">How sourcing works</a>
          <button class="ab-sb-chip ab-crisp-open" type="button" data-crisp-msg="Hello, I'd like a sourcing price on some gaming gear.">Live chat</button>
        </div>
      </div>
    </div>
  </section>

  <!-- The email gate (2026-11-08, user: 「用户点 get price之后，需要弹出一个邮箱
       输入框，用于接收价格信息」). Get price no longer hands the link straight to
       the chat: it opens this dialog, because the price is answered asynchronously
       and needs somewhere to land. The address and the link both ride in the
       chat message — this site has no form backend, so the chat inbox is where a
       human picks the request up — and the note under the box repeats the
       address, so the reader can see what was sent. Nothing here promises a
       price, only where the lowest one we find will be sent. -->
  <div class="ab-sb-modal" id="price-modal" role="dialog" aria-modal="true"
       aria-labelledby="price-modal-title" hidden>
    <div class="ab-sb-modal__panel">
      <button class="ab-sb-modal__close" type="button" aria-label="Close">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">
          <path fill="currentColor" d="M18.3 5.7a1 1 0 0 0-1.4 0L12 10.6 7.1 5.7a1 1 0 0 0-1.4 1.4L10.6 12l-4.9 4.9a1 1 0 1 0 1.4 1.4L12 13.4l4.9 4.9a1 1 0 0 0 1.4-1.4L13.4 12l4.9-4.9a1 1 0 0 0 0-1.4z"/>
        </svg>
      </button>
      <h2 class="ab-sb-modal__title" id="price-modal-title">Where should we send the price?</h2>
      <p class="ab-sb-modal__lead">We will look up the lowest sourcing price for the link you pasted and email it to you.</p>
      <p class="ab-sb-modal__link" id="price-modal-link"></p>
      <form class="ab-sb-modal__form" id="price-form" novalidate>
        <label class="ab-sb-modal__label" for="price-email">Email address</label>
        <input class="ab-sb-modal__input" id="price-email" name="email" type="email"
               autocomplete="email" inputmode="email" spellcheck="false"
               placeholder="you@example.com" required>
        <p class="ab-sb-modal__error" id="price-error" role="alert" hidden></p>
        <button class="ab-sb-modal__submit" type="submit">Email me the price</button>
      </form>
      <p class="ab-sb-modal__foot">The lowest price we find goes to that address; reply in the live chat and we buy the gear for you.</p>
    </div>
  </div>

  <section class="ab-sb-journey" id="how">
    <div class="ab-sb-inner">
      <div class="ab-sb-journey__card">
        <ol class="ab-sb-journey__steps">
          <li class="ab-sb-step">
            <p class="ab-sb-step__title"><span class="ab-sb-step__num">1</span> Paste a link or pick a piece</p>
            <p class="ab-sb-step__text">Paste any product link, or pick one from the shelf below.</p>
          </li>
          <li class="ab-sb-step">
            <p class="ab-sb-step__title"><span class="ab-sb-step__num">2</span> Leave an email</p>
            <p class="ab-sb-step__text">We look up the lowest sourcing price and send it there.</p>
          </li>
          <li class="ab-sb-step">
            <p class="ab-sb-step__title"><span class="ab-sb-step__num">3</span> Confirm and we source it</p>
            <p class="ab-sb-step__text">Reply in the live chat; we buy and ship the gear.</p>
          </li>
        </ol>
        <div class="ab-sb-journey__track" aria-hidden="true">
          <span class="ab-sb-journey__dot"></span>
          <span class="ab-sb-journey__dot"></span>
          <span class="ab-sb-journey__dot"></span>
        </div>
      </div>
    </div>
  </section>

  <section class="ab-sb-features">
    <div class="ab-sb-inner">
      <div class="ab-sb-features__grid">
        <a class="ab-sb-feature ab-sb-feature--top-ups" href="/top-ups/">
          <span class="ab-sb-feature__text">
            <span class="ab-sb-feature__eyebrow">Catalogue</span>
            <span class="ab-sb-feature__title">Top-ups</span>
          </span>
          <span class="ab-sb-feature__art"><img src="/assets/digital/pubg-mobile-feed.png" alt="" loading="lazy" decoding="async"></span>
        </a>
        <a class="ab-sb-feature ab-sb-feature--gift" href="/gift-cards/">
          <span class="ab-sb-feature__text">
            <span class="ab-sb-feature__eyebrow">Catalogue</span>
            <span class="ab-sb-feature__title">Gift-cards</span>
          </span>
          <span class="ab-sb-feature__art"><img src="/assets/digital/amazon-gift-card-us-feed.png" alt="" loading="lazy" decoding="async"></span>
        </a>
        <a class="ab-sb-feature ab-sb-feature--cdkeys" href="/cdkeys/">
          <span class="ab-sb-feature__text">
            <span class="ab-sb-feature__eyebrow">Catalogue</span>
            <span class="ab-sb-feature__title">CDKeys</span>
          </span>
          <span class="ab-sb-feature__art"><img src="/assets/digital/fortnite-card-feed.png" alt="" loading="lazy" decoding="async"></span>
        </a>
        <a class="ab-sb-feature ab-sb-feature--news" href="/news/">
          <span class="ab-sb-feature__text">
            <span class="ab-sb-feature__eyebrow">Free games</span>
            <span class="ab-sb-feature__title">News</span>
          </span>
        </a>
      </div>
    </div>
  </section>

  <section class="ab-sb-discovery" id="gear">
    <div class="ab-sb-inner">
      <header class="ab-sb-discovery__head">
        <h2 class="ab-sb-discovery__title">Popular gear</h2>
        <button class="ab-sb-chat ab-crisp-open" type="button" data-crisp-msg="Hello, I'd like a sourcing price on some gaming gear.">Open live chat</button>
      </header>

      <p class="ab-sb-discovery__lead">The gear players ask about most, each with the price we can source it at.</p>

      <div class="ab-sb-pills" id="gear-pills">
        <button class="ab-sb-pill is-active" type="button" data-category="all" aria-pressed="true">All</button>
        <button class="ab-sb-pill" type="button" data-category="mouse" aria-pressed="false">Mice</button>
        <button class="ab-sb-pill" type="button" data-category="keyboard" aria-pressed="false">Keyboards</button>
        <button class="ab-sb-pill" type="button" data-category="mousepad" aria-pressed="false">Mousepads</button>
        <button class="ab-sb-pill" type="button" data-category="monitor" aria-pressed="false">Monitors</button>
        <button class="ab-sb-pill" type="button" data-category="headset" aria-pressed="false">Headsets</button>
        <button class="ab-sb-pill" type="button" data-category="chair" aria-pressed="false">Chairs</button>
      </div>

      <div class="ab-sb-grid" id="gear-grid" aria-label="Popular gear">

        <!-- Page one of five more review categories joined the shelf above the
             keyboards (2026-11-08, user: 「将 https://prosettings.net/reviews/type/
             keyboard/ …mousepad/ …monitor/ …headset/ …chair/ 这些页面的第1页商品
             也同样进行处理」). Each category page carries five "featured" reviews
             and a "More Reviews" list of five under them — four on the monitor
             page — and unlike the mouse page those two groups do not overlap, so
             page one is ten products per category, 49 in all. With the ten mice
             of the earlier batch the band holds 59 cards, newest review first —
             every one of them dated, so the order needs no tie-break.

             The five keyboards added on 2026-11-05 are gone (2026-11-08, user:
             「将非5小时内添加的商品删除」). The band keeps only what had been
             added in the last five hours, and by their covers' file dates the
             mice and these 49 were the only cards inside that window — the
             keyboards were three and a half days old. Their pictures are still
             on disk under /assets/gear/ (the cards were removed, the files were
             not, and the hero photo is one of them), and with both multi-photo
             cards gone nothing on the band opens a lightbox any more.

             Each card has one picture and no photo set, so none carries
             data-gallery. Covers are those reviews' own og:image uploads, cut to
             960x640 by _tmp_ocr/gear_cards_prep.py on the same rule as the mice:
             a 3:2 window sized off the product's longer side, because the card
             only shows the middle square. Sheets live at
             /assets/gear/<id>/01.jpg. Alt text carries no commas: data-gallery
             splits on them.

             The prices under these cards are the ones described in the block at
             the top of the page: 70% of the product's US retail, rounded to the
             dollar. Keep each in step with data-price — the probe checks that
             the printed price and the chat number agree.

             The pills filter by category now, not by brand: twenty-odd brands
             made a row nobody could read, while six categories stay on one line
             at 1440. gear.js reads data-category, on the card and on the pill. -->

        <article class="ab-sb-card" id="finalmouse-starlight-x" data-category="mouse" data-search="finalmouse starlight x mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/finalmouse-starlight-x/01.jpg" alt="A navy Finalmouse Starlight X seen from above on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Finalmouse Starlight X</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$125</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Finalmouse Starlight X" data-name="Finalmouse Starlight X" data-price="125">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="corsair-hs80-v2-max-wireless" data-category="headset" data-search="corsair hs80 v2 max wireless headset">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/corsair-hs80-v2-max-wireless/01.jpg" alt="Corsair HS80 v2 MAX Wireless on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Corsair HS80 v2 MAX Wireless</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$139</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Corsair HS80 v2 MAX Wireless" data-name="Corsair HS80 v2 MAX Wireless" data-price="139">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="logitech-g-pro-x2-rapid" data-category="keyboard" data-search="logitech g pro x2 rapid keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/logitech-g-pro-x2-rapid/01.jpg" alt="Logitech G Pro X2 RAPID on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Logitech G Pro X2 RAPID</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$160</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Logitech G Pro X2 RAPID" data-name="Logitech G Pro X2 RAPID" data-price="160">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="corsair-sabre-v3-pro" data-category="mouse" data-search="corsair sabre v3 pro mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/corsair-sabre-v3-pro/01.jpg" alt="A black Corsair Sabre V3 Pro seen from above on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Corsair Sabre V3 Pro</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$126</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Corsair Sabre V3 Pro" data-name="Corsair Sabre V3 Pro" data-price="126">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="logitech-g-pro-x3-lightspeed-headset" data-category="headset" data-search="logitech g pro x3 lightspeed headset headset">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/logitech-g-pro-x3-lightspeed-headset/01.jpg" alt="Logitech G Pro X3 LIGHTSPEED Headset on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Logitech G Pro X3 LIGHTSPEED Headset</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$174</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Logitech G Pro X3 LIGHTSPEED Headset" data-name="Logitech G Pro X3 LIGHTSPEED Headset" data-price="174">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="libernovo-omni-se" data-category="chair" data-search="libernovo omni se chair">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/libernovo-omni-se/01.jpg" alt="LiberNovo Omni SE on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">LiberNovo Omni SE</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$629</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for LiberNovo Omni SE" data-name="LiberNovo Omni SE" data-price="629">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="corsair-mm-glass" data-category="mousepad" data-search="corsair mm glass mousepad">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/corsair-mm-glass/01.jpg" alt="Corsair MM Glass on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Corsair MM Glass</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$70</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Corsair MM Glass" data-name="Corsair MM Glass" data-price="70">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="logitech-g-pro-x3-superstrike" data-category="mouse" data-search="logitech g pro x3 superstrike mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/logitech-g-pro-x3-superstrike/01.jpg" alt="A pink and black Logitech G Pro X3 SUPERSTRIKE seen from above on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Logitech G Pro X3 SUPERSTRIKE</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$140</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Logitech G Pro X3 SUPERSTRIKE" data-name="Logitech G Pro X3 SUPERSTRIKE" data-price="140">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="corsair-mm-anti-fray" data-category="mousepad" data-search="corsair mm anti-fray mousepad">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/corsair-mm-anti-fray/01.jpg" alt="Corsair MM Anti-fray on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Corsair MM Anti-fray</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$14</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Corsair MM Anti-fray" data-name="Corsair MM Anti-fray" data-price="14">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="vaxee-np-01-ergo" data-category="mouse" data-search="vaxee np-01 ergo mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/vaxee-np-01-ergo/01.jpg" alt="A green VAXEE NP-01 Ergo seen from above on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">VAXEE NP-01 Ergo</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$105</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for VAXEE NP-01 Ergo" data-name="VAXEE NP-01 Ergo" data-price="105">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="razer-huntsman-v3-pro-low-profile-tkl-8khz" data-category="keyboard" data-search="razer huntsman v3 pro low-profile tkl 8khz keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/razer-huntsman-v3-pro-low-profile-tkl-8khz/01.jpg" alt="Razer Huntsman V3 Pro Low-Profile TKL 8KHz on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Razer Huntsman V3 Pro Low-Profile TKL 8KHz</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$160</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Razer Huntsman V3 Pro Low-Profile TKL 8KHz" data-name="Razer Huntsman V3 Pro Low-Profile TKL 8KHz" data-price="160">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="secretlab-atlas" data-category="chair" data-search="secretlab atlas chair">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/secretlab-atlas/01.jpg" alt="Secretlab Atlas on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Secretlab Atlas</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$349</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Secretlab Atlas" data-name="Secretlab Atlas" data-price="349">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="corsair-nightsword-v2-wireless" data-category="mouse" data-search="corsair nightsword v2 wireless mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/corsair-nightsword-v2-wireless/01.jpg" alt="A black Corsair Nightsword V2 Wireless angled on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Corsair Nightsword V2 Wireless</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$91</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Corsair Nightsword V2 Wireless" data-name="Corsair Nightsword V2 Wireless" data-price="91">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="x-raypad-nod" data-category="mousepad" data-search="x-raypad nod mousepad">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/x-raypad-nod/01.jpg" alt="X-Raypad NOD on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">X-Raypad NOD</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$74</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for X-Raypad NOD" data-name="X-Raypad NOD" data-price="74">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="razer-huntsman-v3-magnetic-he-8khz" data-category="keyboard" data-search="razer huntsman v3 he magnetic 8khz keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/razer-huntsman-v3-magnetic-he-8khz/01.jpg" alt="Razer Huntsman V3 HE Magnetic 8KHz on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Razer Huntsman V3 HE Magnetic 8KHz</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$97</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Razer Huntsman V3 HE Magnetic 8KHz" data-name="Razer Huntsman V3 HE Magnetic 8KHz" data-price="97">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="epomaker-he75-v2-tmr" data-category="keyboard" data-search="epomaker he75 v2 tmr keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/epomaker-he75-v2-tmr/01.jpg" alt="EPOMAKER HE75 V2 TMR on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">EPOMAKER HE75 V2 TMR</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$90</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for EPOMAKER HE75 V2 TMR" data-name="EPOMAKER HE75 V2 TMR" data-price="90">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="zowie-xq2566-x" data-category="monitor" data-search="zowie xq2566x monitor">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/zowie-xq2566-x/01.jpg" alt="ZOWIE XQ2566X on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">ZOWIE XQ2566X</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$630</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for ZOWIE XQ2566X" data-name="ZOWIE XQ2566X" data-price="630">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="andaseat-kaiser-4-6d" data-category="chair" data-search="andaseat kaiser 4 6d chair">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/andaseat-kaiser-4-6d/01.jpg" alt="AndaSeat Kaiser 4 6D on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">AndaSeat Kaiser 4 6D</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$384</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for AndaSeat Kaiser 4 6D" data-name="AndaSeat Kaiser 4 6D" data-price="384">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="corsair-hs35-v3-wireless" data-category="headset" data-search="corsair hs35 v3 wireless headset">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/corsair-hs35-v3-wireless/01.jpg" alt="Corsair HS35 v3 Wireless on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Corsair HS35 v3 Wireless</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$55</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Corsair HS35 v3 Wireless" data-name="Corsair HS35 v3 Wireless" data-price="55">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="corsair-clipper-pro-mini-60" data-category="keyboard" data-search="corsair clipper pro mini 60 keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/corsair-clipper-pro-mini-60/01.jpg" alt="Corsair Clipper Pro Mini 60 on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Corsair Clipper Pro Mini 60</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$69</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Corsair Clipper Pro Mini 60" data-name="Corsair Clipper Pro Mini 60" data-price="69">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="pulsar-es-jupiter-pro" data-category="mousepad" data-search="pulsar es jupiter pro mousepad">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/pulsar-es-jupiter-pro/01.jpg" alt="Pulsar eS Jupiter Pro on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Pulsar eS Jupiter Pro</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$28</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Pulsar eS Jupiter Pro" data-name="Pulsar eS Jupiter Pro" data-price="28">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="razer-atlas-pro" data-category="mousepad" data-search="razer atlas pro mousepad">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/razer-atlas-pro/01.jpg" alt="Razer Atlas Pro on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Razer Atlas Pro</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$91</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Razer Atlas Pro" data-name="Razer Atlas Pro" data-price="91">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="melgeek-made68-ultra-v2" data-category="keyboard" data-search="melgeek made68 ultra v2 keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/melgeek-made68-ultra-v2/01.jpg" alt="MelGeek Made68 Ultra V2 on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">MelGeek Made68 Ultra V2</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$153</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for MelGeek Made68 Ultra V2" data-name="MelGeek Made68 Ultra V2" data-price="153">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="steelseries-arctis-nova-pro-omni" data-category="headset" data-search="steelseries arctis nova pro omni headset">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/steelseries-arctis-nova-pro-omni/01.jpg" alt="SteelSeries Arctis Nova Pro Omni on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">SteelSeries Arctis Nova Pro Omni</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$279</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for SteelSeries Arctis Nova Pro Omni" data-name="SteelSeries Arctis Nova Pro Omni" data-price="279">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="vaxee-np-01s-v3" data-category="mouse" data-search="vaxee np-01s v3 mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/vaxee-np-01s-v3/01.jpg" alt="A green VAXEE NP-01S V3 seen from above on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">VAXEE NP-01S V3</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$105</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for VAXEE NP-01S V3" data-name="VAXEE NP-01S V3" data-price="105">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="razer-gigantus-v2-pro" data-category="mousepad" data-search="razer gigantus v2 pro mousepad">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/razer-gigantus-v2-pro/01.jpg" alt="Razer Gigantus V2 Pro on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Razer Gigantus V2 Pro</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$35</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Razer Gigantus V2 Pro" data-name="Razer Gigantus V2 Pro" data-price="35">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="pulsar-es-pd170" data-category="mousepad" data-search="pulsar es pd170 mousepad">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/pulsar-es-pd170/01.jpg" alt="Pulsar eS PD170 laid flat on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Pulsar eS PD170</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$35</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Pulsar eS PD170" data-name="Pulsar eS PD170" data-price="35">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="steelseries-apex-pro-gen-3" data-category="keyboard" data-search="steelseries apex pro gen 3 keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/steelseries-apex-pro-gen-3/01.jpg" alt="SteelSeries Apex Pro Gen 3 on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">SteelSeries Apex Pro Gen 3</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$181</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for SteelSeries Apex Pro Gen 3" data-name="SteelSeries Apex Pro Gen 3" data-price="181">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="razer-viper-v4-pro" data-category="mouse" data-search="razer viper v4 pro mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/razer-viper-v4-pro/01.jpg" alt="A black Razer Viper V4 Pro seen from above on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Razer Viper V4 Pro</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$112</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Razer Viper V4 Pro" data-name="Razer Viper V4 Pro" data-price="112">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="pulsar-x2n-crazylight" data-category="mouse" data-search="pulsar x2n crazylight mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/pulsar-x2n-crazylight/01.jpg" alt="A grey Pulsar X2N Crazylight seen from above on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Pulsar X2N Crazylight</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$91</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Pulsar X2N Crazylight" data-name="Pulsar X2N Crazylight" data-price="91">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="razer-iskur-v2-newgen" data-category="chair" data-search="razer iskur v2 newgen chair">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/razer-iskur-v2-newgen/01.jpg" alt="Razer Iskur V2 NewGen on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Razer Iskur V2 NewGen</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$454</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Razer Iskur V2 NewGen" data-name="Razer Iskur V2 NewGen" data-price="454">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="pulsar-es-fs-1" data-category="mouse" data-search="pulsar es fs-1 mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/pulsar-es-fs-1/01.jpg" alt="A Pulsar eS FS-1 angled on a white field beside its USB dongle" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Pulsar eS FS-1</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$126</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Pulsar eS FS-1" data-name="Pulsar eS FS-1" data-price="126">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="corsair-galleon-100-sd" data-category="keyboard" data-search="corsair galleon 100 sd keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/corsair-galleon-100-sd/01.jpg" alt="Corsair Galleon 100 SD on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Corsair Galleon 100 SD</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$244</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Corsair Galleon 100 SD" data-name="Corsair Galleon 100 SD" data-price="244">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="logitech-g-pro-x2-superstrike" data-category="mouse" data-search="logitech g pro x2 superstrike mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/logitech-g-pro-x2-superstrike/01.jpg" alt="A white and black Logitech G Pro X2 SUPERSTRIKE seen from above on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Logitech G Pro X2 SUPERSTRIKE</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$126</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Logitech G Pro X2 SUPERSTRIKE" data-name="Logitech G Pro X2 SUPERSTRIKE" data-price="126">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="corsair-mm-pro" data-category="mousepad" data-search="corsair mm pro control mousepad">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/corsair-mm-pro/01.jpg" alt="Corsair MM Pro Control on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Corsair MM Pro Control</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$42</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Corsair MM Pro Control" data-name="Corsair MM Pro Control" data-price="42">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="esptiger-heavy-claw" data-category="mousepad" data-search="banks collection heavy claw by esptiger mousepad">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/esptiger-heavy-claw/01.jpg" alt="Banks Collection Heavy Claw by ESPTIGER on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Banks Collection Heavy Claw by ESPTIGER</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$31</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Banks Collection Heavy Claw by ESPTIGER" data-name="Banks Collection Heavy Claw by ESPTIGER" data-price="31">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="iqunix-ev63" data-category="keyboard" data-search="iqunix ev63 keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/iqunix-ev63/01.jpg" alt="IQUNIX EV63 on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">IQUNIX EV63</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$118</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for IQUNIX EV63" data-name="IQUNIX EV63" data-price="118">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="vaxee-pd140" data-category="mousepad" data-search="vaxee pd140 mousepad">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/vaxee-pd140/01.jpg" alt="VAXEE PD140 on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">VAXEE PD140</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$35</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for VAXEE PD140" data-name="VAXEE PD140" data-price="35">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="wooting-60he-v2" data-category="keyboard" data-search="wooting 60he v2 keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/wooting-60he-v2/01.jpg" alt="Wooting 60HE v2 on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Wooting 60HE v2</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$125</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Wooting 60HE v2" data-name="Wooting 60HE v2" data-price="125">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="blacklyte-kraken-pro" data-category="chair" data-search="blacklyte kraken pro chair">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/blacklyte-kraken-pro/01.jpg" alt="Blacklyte Kraken Pro on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Blacklyte Kraken Pro</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$454</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Blacklyte Kraken Pro" data-name="Blacklyte Kraken Pro" data-price="454">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="sony-inzone-h9-ii" data-category="headset" data-search="sony inzone h9 ii headset">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/sony-inzone-h9-ii/01.jpg" alt="SONY INZONE H9 II on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">SONY INZONE H9 II</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$244</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for SONY INZONE H9 II" data-name="SONY INZONE H9 II" data-price="244">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="razer-blackshark-v3-pro" data-category="headset" data-search="razer blackshark v3 pro headset">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/razer-blackshark-v3-pro/01.jpg" alt="Razer BlackShark V3 Pro on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Razer BlackShark V3 Pro</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$174</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Razer BlackShark V3 Pro" data-name="Razer BlackShark V3 Pro" data-price="174">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="sony-inzone-m10s" data-category="monitor" data-search="sony inzone m10s monitor">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/sony-inzone-m10s/01.jpg" alt="Sony INZONE M10S on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Sony INZONE M10S</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$629</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Sony INZONE M10S" data-name="Sony INZONE M10S" data-price="629">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="corsair-void-wireless-v2" data-category="headset" data-search="corsair void wireless v2 headset">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/corsair-void-wireless-v2/01.jpg" alt="Corsair VOID Wireless V2 on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Corsair VOID Wireless V2</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$83</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Corsair VOID Wireless V2" data-name="Corsair VOID Wireless V2" data-price="83">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="blacklyte-athena-pro" data-category="chair" data-search="blacklyte athena pro chair">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/blacklyte-athena-pro/01.jpg" alt="Blacklyte Athena Pro on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Blacklyte Athena Pro</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$349</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Blacklyte Athena Pro" data-name="Blacklyte Athena Pro" data-price="349">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="zowie-xl2586x" data-category="monitor" data-search="zowie xl2586x+ monitor">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/zowie-xl2586x/01.jpg" alt="ZOWIE XL2586X+ on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">ZOWIE XL2586X+</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$700</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for ZOWIE XL2586X+" data-name="ZOWIE XL2586X+" data-price="700">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="blacklyte-kraken" data-category="chair" data-search="blacklyte kraken chair">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/blacklyte-kraken/01.jpg" alt="Blacklyte Kraken on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Blacklyte Kraken</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$363</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Blacklyte Kraken" data-name="Blacklyte Kraken" data-price="363">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="razer-iskur-v2" data-category="chair" data-search="razer iskur v2 chair">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/razer-iskur-v2/01.jpg" alt="Razer Iskur V2 on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Razer Iskur V2</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$454</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Razer Iskur V2" data-name="Razer Iskur V2" data-price="454">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="zowie-xl2566x" data-category="monitor" data-search="zowie xl2566x+ monitor">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/zowie-xl2566x/01.jpg" alt="ZOWIE XL2566X+ on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">ZOWIE XL2566X+</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$454</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for ZOWIE XL2566X+" data-name="ZOWIE XL2566X+" data-price="454">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="nzxt-relay" data-category="headset" data-search="nzxt relay (+ switchmix) headset">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/nzxt-relay/01.jpg" alt="NZXT Relay (+ SwitchMix) on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">NZXT Relay (+ SwitchMix)</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$160</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for NZXT Relay (+ SwitchMix)" data-name="NZXT Relay (+ SwitchMix)" data-price="160">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="razer-blackshark-v2-pro" data-category="headset" data-search="razer blackshark v2 pro headset">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/razer-blackshark-v2-pro/01.jpg" alt="Razer BlackShark V2 Pro on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Razer BlackShark V2 Pro</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$139</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Razer BlackShark V2 Pro" data-name="Razer BlackShark V2 Pro" data-price="139">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="logitech-g-pro-x-2-lightspeed" data-category="headset" data-search="logitech g pro x 2 lightspeed headset headset">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/logitech-g-pro-x-2-lightspeed/01.jpg" alt="Logitech G Pro X 2 LIGHTSPEED Headset on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Logitech G Pro X 2 LIGHTSPEED Headset</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$160</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Logitech G Pro X 2 LIGHTSPEED Headset" data-name="Logitech G Pro X 2 LIGHTSPEED Headset" data-price="160">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="asus-rog-swift-pg27aqn" data-category="monitor" data-search="asus rog swift pg27aqn monitor">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/asus-rog-swift-pg27aqn/01.jpg" alt="ASUS ROG SWIFT PG27AQN on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">ASUS ROG SWIFT PG27AQN</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$419</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for ASUS ROG SWIFT PG27AQN" data-name="ASUS ROG SWIFT PG27AQN" data-price="419">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="zowie-xl-2566k" data-category="monitor" data-search="zowie xl2566k monitor">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/zowie-xl-2566k/01.jpg" alt="ZOWIE XL2566K on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">ZOWIE XL2566K</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$419</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for ZOWIE XL2566K" data-name="ZOWIE XL2566K" data-price="419">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="msi-oculux-nxg253r" data-category="monitor" data-search="msi oculux nxg253r monitor">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/msi-oculux-nxg253r/01.jpg" alt="MSI Oculux NXG253R on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">MSI Oculux NXG253R</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$350</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for MSI Oculux NXG253R" data-name="MSI Oculux NXG253R" data-price="350">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="secretlab-titan-evo-2022" data-category="chair" data-search="secretlab titan evo 2022 chair">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/secretlab-titan-evo-2022/01.jpg" alt="Secretlab Titan Evo 2022 on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Secretlab Titan Evo 2022</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$384</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Secretlab Titan Evo 2022" data-name="Secretlab Titan Evo 2022" data-price="384">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="herman-miller-logitech-embody" data-category="chair" data-search="herman miller x logitech g embody gaming chair chair">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/herman-miller-logitech-embody/01.jpg" alt="Herman Miller x Logitech G Embody Gaming Chair on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Herman Miller x Logitech G Embody Gaming Chair</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$1257</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Herman Miller x Logitech G Embody Gaming Chair" data-name="Herman Miller x Logitech G Embody Gaming Chair" data-price="1257">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="zowie-xl2546k" data-category="monitor" data-search="zowie xl2546k monitor">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/zowie-xl2546k/01.jpg" alt="Zowie XL2546K on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Zowie XL2546K</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$279</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Zowie XL2546K" data-name="Zowie XL2546K" data-price="279">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="zowie-xl2546" data-category="monitor" data-search="zowie xl2546 monitor">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/zowie-xl2546/01.jpg" alt="Zowie XL2546 on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Zowie XL2546</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$349</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Zowie XL2546" data-name="Zowie XL2546" data-price="349">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

      </div>

      <p class="ab-sb-empty" id="gear-empty" hidden>No quote here matches that search. Paste a product link above and we will check its lowest price in the live chat.</p>

    </div>
  </section>

</div>
