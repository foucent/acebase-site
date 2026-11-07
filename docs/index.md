---
title: Home
description: AceBase — paste a product link and we come back with the lowest sourcing price, by email and in the live chat.
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
     hero, the email dialog, the three steps, the four banners and the five
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
     feature banners are shortcuts to the four catalogue pages. This page is
     HAND-MAINTAINED — unlike /top-up/, /cdkeys/, /gift-cards/ and /game/,
     nothing regenerates it. Card ids, data-gallery sets, alt text (no commas:
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

     THE FIVE PRICES ARE PLACEHOLDERS the user asked to have made up
     (139 / 189 / 74 / 119 / 185 USD). Nothing measured them. They
     are here to show the band's shape; replace them with real quotes before
     anyone relies on them, and keep them in step with data-price — the probe
     checks that the printed price and the chat number are the same. -->

<div class="ab-sb" markdown="0">

  <section class="ab-sb-hero">
    <div class="ab-sb-hero__art" aria-hidden="true">
      <img src="/assets/gear/razer-blackwidow-v4-75/01.jpg" alt="" loading="eager" decoding="async">
    </div>
    <div class="ab-sb-hero__inner ab-sb-inner">
      <div class="ab-sb-hero__copy">
        <h1 class="ab-sb-hero__title">Paste a link, get the lowest price</h1>
        <p class="ab-sb-hero__meta">Any store &middot; Lowest sourcing price &middot; Emailed to you</p>
        <form class="ab-sb-search" id="gear-search-form" role="search">
          <label class="ab-sb-search__field">
            <svg class="ab-sb-search__icon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">
              <circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/>
              <path d="m16 16 5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
            <input type="text" id="gear-search" name="q" autocomplete="off" placeholder="Paste a product link" aria-label="Paste a product link and we will check its lowest sourcing price">
          </label>
          <button class="ab-sb-search__submit" type="submit">Get price</button>
        </form>
        <p class="ab-sb-search__note" id="gear-note" aria-live="polite" hidden></p>
        <div class="ab-sb-hero__tools">
          <a class="ab-sb-chip" href="#gear">Recent quotes</a>
          <a class="ab-sb-chip" href="#how">How sourcing works</a>
          <button class="ab-sb-chip ab-crisp-open" type="button" data-crisp-msg="Hello, I'd like to ask about the gear.">Live chat</button>
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
      <p class="ab-sb-modal__foot">The lowest price we find goes to that address, and the same thread stays open in the live chat.</p>
    </div>
  </div>

  <section class="ab-sb-journey" id="how">
    <div class="ab-sb-inner">
      <div class="ab-sb-journey__card">
        <ol class="ab-sb-journey__steps">
          <li class="ab-sb-step">
            <p class="ab-sb-step__title"><span class="ab-sb-step__num">1</span> Paste a link or pick a piece</p>
            <p class="ab-sb-step__text">Any store's product page, or one of the five here.</p>
          </li>
          <li class="ab-sb-step">
            <p class="ab-sb-step__title"><span class="ab-sb-step__num">2</span> Leave an email</p>
            <p class="ab-sb-step__text">The price needs somewhere to land while we look it up.</p>
          </li>
          <li class="ab-sb-step">
            <p class="ab-sb-step__title"><span class="ab-sb-step__num">3</span> The price arrives</p>
            <p class="ab-sb-step__text">The lowest source price and the total, by email.</p>
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
        <a class="ab-sb-feature ab-sb-feature--game" href="/game/">
          <span class="ab-sb-feature__text">
            <span class="ab-sb-feature__eyebrow">Catalogue</span>
            <span class="ab-sb-feature__title">Game</span>
          </span>
          <span class="ab-sb-feature__art"><img src="/assets/digital/pubg-mobile-feed.png" alt="" loading="lazy" decoding="async"></span>
        </a>
        <a class="ab-sb-feature ab-sb-feature--gift" href="/gift-cards/">
          <span class="ab-sb-feature__text">
            <span class="ab-sb-feature__eyebrow">Catalogue</span>
            <span class="ab-sb-feature__title">Gift Cards</span>
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
        <a class="ab-sb-feature ab-sb-feature--top-up" href="/top-up/">
          <span class="ab-sb-feature__text">
            <span class="ab-sb-feature__eyebrow">Catalogue</span>
            <span class="ab-sb-feature__title">Top-Up</span>
          </span>
          <span class="ab-sb-feature__art"><img src="/assets/digital/douyin-top-up-feed.png" alt="" loading="lazy" decoding="async"></span>
        </a>
      </div>
    </div>
  </section>

  <section class="ab-sb-discovery" id="gear">
    <div class="ab-sb-inner">
      <header class="ab-sb-discovery__head">
        <h2 class="ab-sb-discovery__title">Recent quotes</h2>
        <button class="ab-sb-chat ab-crisp-open" type="button" data-crisp-msg="Hello, I'd like to ask about the gear.">Open live chat</button>
      </header>

      <p class="ab-sb-discovery__lead">The lowest price we came back with for the last five requests, newest first.</p>

      <div class="ab-sb-pills" id="gear-pills">
        <button class="ab-sb-pill is-active" type="button" data-brand="all" aria-pressed="true">All</button>
        <button class="ab-sb-pill" type="button" data-brand="razer" aria-pressed="false">Razer</button>
        <button class="ab-sb-pill" type="button" data-brand="asus" aria-pressed="false">ASUS</button>
        <button class="ab-sb-pill" type="button" data-brand="keychron" aria-pressed="false">Keychron</button>
        <button class="ab-sb-pill" type="button" data-brand="glorious" aria-pressed="false">Glorious</button>
        <button class="ab-sb-pill" type="button" data-brand="wooting" aria-pressed="false">Wooting</button>
      </div>

      <div class="ab-sb-grid" id="gear-grid" aria-label="Recent quotes">

        <!-- Five mechanical keyboards added 2026-11-05 (user: 「将 … 这五款商品
             添加到 …/gear/」), at the top of the grid because that is where new
             cards go — the same place the three product cards took on /apps/
             the same day. Each card is the page's one layout: a picture that
             opens the lightbox, the name, and Request Sourcing. No price, no
             link out, no source named.

             Covers are the vendors' own pictures cut to the band's 3:2
             (960x640) by _tmp_ocr/keeb_cards_prep.py:
               - Razer, Keychron and Glorious are photographs on a desk or a
                 studio floor, so they are ordinary centred 3:2 crops;
               - ASUS published a transparent render against its own dark
                 key-visual gradient, so the render is laid whole on that
                 gradient instead of being cropped. Its square og image was not
                 used: it showed two keyboards and carried third-party award
                 badges;
               - Wooting's render is a wide flat-lay of the whole deck, so it
                 sits whole on a white field rather than losing keys to a crop.
             Alt text carries no commas: data-gallery splits on them. -->

        <article class="ab-sb-card" id="razer-blackwidow-v4-75" data-brand="razer" data-search="razer blackwidow v4 75% razer keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/razer-blackwidow-v4-75/01.jpg" alt="A Razer BlackWidow V4 75% on a glowing desk mat beside a Razer mouse" loading="lazy" decoding="async" data-gallery="/assets/gear/razer-blackwidow-v4-75/01.jpg|A Razer BlackWidow V4 75% on a glowing desk mat beside a Razer mouse,/assets/gear/razer-blackwidow-v4-75/02.jpg|The BlackWidow V4 75% from above with its RGB lit keys and wrist rest">
          </div>
          <h3 class="ab-sb-card__title">Razer BlackWidow V4 75%</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$139</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Razer BlackWidow V4 75%" data-name="Razer BlackWidow V4 75%" data-price="139">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="asus-rog-azoth" data-brand="asus" data-search="asus rog azoth keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/asus-rog-azoth/01.jpg" alt="The ROG Azoth angled in the dark with its RGB backlight on" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">ASUS ROG Azoth</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$189</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for ASUS ROG Azoth" data-name="ASUS ROG Azoth" data-price="189">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="keychron-v1-max" data-brand="keychron" data-search="keychron v1 max keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/keychron-v1-max/01.jpg" alt="A Keychron V1 Max with black and blue keycaps on a pale blue desk" loading="lazy" decoding="async" data-gallery="/assets/gear/keychron-v1-max/01.jpg|A Keychron V1 Max with black and blue keycaps on a pale blue desk,/assets/gear/keychron-v1-max/02.jpg|The V1 Max side on under a hard studio light with its red Escape key">
          </div>
          <h3 class="ab-sb-card__title">Keychron V1 Max</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$74</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Keychron V1 Max" data-name="Keychron V1 Max" data-price="74">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="glorious-gmmk-3-pro-75" data-brand="glorious" data-search="glorious gmmk 3 pro 75% keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/glorious-gmmk-3-pro-75/01.jpg" alt="A black GMMK 3 PRO 75% with rainbow-lit keys on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Glorious GMMK 3 PRO 75%</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$119</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Glorious GMMK 3 PRO 75%" data-name="Glorious GMMK 3 PRO 75%" data-price="119">
              <span class="ab-sb-card__label">Get this price</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="wooting-80he" data-brand="wooting" data-search="wooting 80he keyboard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/wooting-80he/01.jpg" alt="The Wooting 80HE from above in its black plastic case" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Wooting 80HE</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$185</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get this price for Wooting 80HE" data-name="Wooting 80HE" data-price="185">
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
