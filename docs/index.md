---
title: Premium gaming gear — we buy it in China and deliver it to your door
description: AceBase — premium gaming gear. Paste a product link from any shop and we buy it for you — from the brand supplier first, otherwise from Pinduoduo, JD or Taobao — then inspect it, assemble it where needed and deliver it to your door.
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
     news pictures are photographs of game art). 2026-11-11: the catalogue
     banners went one by one as their pages were emptied onto the shelf below —
     Top-ups first, then CDKeys and Gift-cards — so the strip was the News
     banner alone, full width, and it took the first news cover for its art
     rather than standing there as an empty purple bar. 2026-11-11 evening the
     user had that last one removed too (『将 首页的 Free games / News / The
     giveaways… 的内容去掉』), so there is no banner band at all now: the grey
     Popular gear band follows the journey card directly. The .ab-sb-features
     styles stay in gear.css, unused, in case a band comes back.
     This page is HAND-MAINTAINED — nothing regenerates it. Card ids, data-gallery sets, alt text (no commas:
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

<!-- THE OFFER CHANGED (2026-11-11, user: 「首页要表达的是获取硬件价格和购买
     链接，为用户提供验货及运转服务，而不提供产品采购」). The page used to sell
     a purchase: "bought and shipped for you", "confirm and we source it", a
     dialog that ended "reply in the live chat and we buy the gear for you".
     It now sells two things and says what it does not do:

       1. the lowest price we can find, and a link to buy it at — the headline,
          the meta row, the search button, the dialog and its footnote, the
          second step, the shelf lead and both chat openers all say "price and
          purchase link" instead of a price alone;
       2. inspection and forwarding — step 3 is where a visitor sees that they
          order at the link, the parcel comes to us first, and we check it and
          forward it;
       3. no procurement. The dialog footnote says it outright ("we don't buy
          products for you"), because the old wording promised the opposite
          and a footer is where a reader looks for the small print.

     "Source" is gone from the page's visible copy; the word still lives in
     sourcing.js, which the digital-goods catalogues share, so the shelf's
     cards get their purchase-link wording from a branch in that file scoped to
     .ab-sb rather than from a new button type. gear.js's message changed with
     the hero box. The prices themselves did not move.

     The 59 card actions changed with the rest: "Get this price" could not stay
     under a lead that promises a link as well. The first label was "Get price
     & link"; the user then asked for 获取购买链接或渠道, so the label reads "Get
     link or channel" and the aria-label "Get the purchase link or channel for
     <model>". "Channel" is the buying route when there is no single link —
     the reply may name one instead. At 390 the label steps down to 11px
     (gear.css, was 12) so the longer wording still sits on one line. Nothing
     else on the cards moved — ids, prices and data-price are as they were. -->

<!-- THE OFFER CHANGED BACK, AND FOR GOOD (2026-11-11 second pass, user: 「是的，
     首要也要改成 我们替你从品牌供应商或三大平台采购」的口径？」). The page is a
     buying service again, the same offer /first-order/ states: any shop's link
     in, the brand supplier first and Pinduoduo / JD / Taobao otherwise, we buy
     the item at the quoted price, inspect it, assemble it where needed and
     deliver it. Nothing on the page quotes a commission and nothing says
     "we don't buy products for you" any more; the dialog footnote now promises
     the opposite.

     What was rewritten: the title and description, the headline, the meta row,
     the paste box's aria-label and button (now Get a quote), both chat
     openers, the dialog's title / lead / submit / footnote, journey steps 2
     and 3, the shelf lead, and the 59 gear card actions — aria-label "Ask for
     a quote on <model> — we buy it for you", label "Get a quote". The 19
     top-up cards keep "Get channel coupons": a top-up is bought on its own
     channel and the user asked for that wording by name. sourcing.js's .ab-sb
     branch and gear.js's message and note moved with them; ids, pictures,
     prices and data-price did not. -->

<!-- NO MORE EMAIL GATE — THE QUOTE COMES BACK IN THE LIVE CHAT (2026-11-11,
     user: 「这里不要通过邮件，而是直接打开聊天在线获取报价」). The hero box used
     to open a dialog that collected an address because the price was answered
     out of band; now a submitted link goes straight into the chat and the
     answer arrives there. #price-modal, its CSS and gear.js's email handling
     are gone; the note under the box only confirms that the chat is open.

     The same message rewrote journey step 1's line ("Paste any product link,"
     — the shelf is no longer offered as the starting point) and step 2, which
     used to be "Leave an email, get a quote" and now names the chat as where
     the quote lands. /first-order/'s closing line changed with it so the two
     pages still describe one offer. -->

<!-- THE HERO ASKS THE SAME QUESTION AS A CARD (2026-11-11, user: 「输入链接的
     get a quote 点击后的效果应该和下面的商品的 get a quote 的效果是一样的」).
     The hero's hand-off now uses sourcing.js's own wording for the shelf's
     cards — "quote to buy this for me … Please reply with the price and how I
     get it" — with the pasted link in the place the card puts its name and
     price. The green note under the box is gone with it: a card click opens
     the chat and nothing else, so the hero does too.

     The shelf's heading no longer says "Popular gear" (user: 「Popular gear 要
     改成类似 最新热门商品价格」): it reads "Latest prices on hot gear", the
     grid's aria-label matches, and the hero chip that jumps there says "Hot
     gear". The "Open live chat" button beside that heading was removed — the
     hero already carries "Live chat". -->

<div class="ab-sb" markdown="0">

  <section class="ab-sb-hero">
    <div class="ab-sb-hero__art" aria-hidden="true">
      <img src="/assets/gear/razer-blackwidow-v4-75/01.jpg" alt="" loading="eager" decoding="async">
    </div>
    <div class="ab-sb-hero__inner ab-sb-inner">
      <div class="ab-sb-hero__copy">
        <h1 class="ab-sb-hero__title">Premium gaming gear &mdash; we buy it in China and deliver it to your door</h1>
        <p class="ab-sb-hero__meta">Bought for you &middot; Inspected &amp; assembled &middot; Delivered to your door</p>
        <form class="ab-sb-search" id="gear-search-form" role="search">
          <label class="ab-sb-search__field">
            <svg class="ab-sb-search__icon" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false">
              <circle cx="11" cy="11" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/>
              <path d="m16 16 5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
            <input type="text" id="gear-search" name="q" autocomplete="off" placeholder="Paste a product link" aria-label="Paste a product link from any shop and we will buy it for you — from the brand supplier first, otherwise from Pinduoduo, JD or Taobao — then inspect it and deliver it to your door">
          </label>
          <button class="ab-sb-search__submit" type="submit">Get a quote</button>
        </form>
        <!-- The three shops the price is checked on (2026-11-11, user: 「然后
             paste a product link 这里要放几个图标，京东，拼多多，淘宝」, then
             「Paste a link from 要改成从 这三个Logo的平台查询价格」). The marks
             are each shop's own front-door icon, cut to 66x66 by
             _tmp_ocr/platform_marks_prep.py; they are labels, not links — the
             row says where the price is looked up, it does not send the reader
             away from the page. -->
        <p class="ab-sb-search__from">
          <span class="ab-sb-search__from-label">Check prices on</span>
          <img class="ab-sb-search__shop" loading="eager" src="/assets/gear/platforms/jd.png" alt="JD.com" width="22" height="22" decoding="async">
          <img class="ab-sb-search__shop" loading="eager" src="/assets/gear/platforms/taobao.png" alt="Taobao" width="22" height="22" decoding="async">
          <img class="ab-sb-search__shop" loading="eager" src="/assets/gear/platforms/pinduoduo.png" alt="Pinduoduo" width="22" height="22" decoding="async">
        </p>
        <div class="ab-sb-hero__tools">
          <a class="ab-sb-chip" href="#gear">Hot gear</a>
          <a class="ab-sb-chip" href="#how">How it works</a>
          <button class="ab-sb-chip ab-crisp-open" type="button" data-crisp-msg="Hello, I'd like a quote to buy some gaming gear for me.">Live chat</button>
        </div>
      </div>
    </div>
  </section>

  <section class="ab-sb-journey" id="how">
    <div class="ab-sb-inner">
      <div class="ab-sb-journey__card">
        <ol class="ab-sb-journey__steps">
          <li class="ab-sb-step">
            <p class="ab-sb-step__title"><span class="ab-sb-step__num">1</span> Paste a link or pick a piece</p>
            <p class="ab-sb-step__text">Paste any product link.</p>
          </li>
          <li class="ab-sb-step">
            <p class="ab-sb-step__title"><span class="ab-sb-step__num">2</span> Get the quote in the live chat</p>
            <p class="ab-sb-step__text">We check the brand supplier first, then Pinduoduo, JD and Taobao, and reply with one price in the live chat.</p>
          </li>
          <li class="ab-sb-step">
            <p class="ab-sb-step__title"><span class="ab-sb-step__num">3</span> We buy, inspect and deliver</p>
            <p class="ab-sb-step__text">Approve the quote and we order the item, inspect it on arrival, assemble it where needed and deliver it to your door.</p>
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

  <section class="ab-sb-discovery" id="gear">
    <div class="ab-sb-inner">
      <header class="ab-sb-discovery__head">
        <h2 class="ab-sb-discovery__title">Latest prices on hot gear</h2>
      </header>

      <p class="ab-sb-discovery__lead">The gear players ask about most, plus top-ups, gift cards and game codes — ask on any card for a quote and we will buy it for you.</p>

      <div class="ab-sb-pills" id="gear-pills">
        <button class="ab-sb-pill is-active" type="button" data-category="all" aria-pressed="true">All</button>
        <button class="ab-sb-pill" type="button" data-category="mouse" aria-pressed="false">Mice</button>
        <button class="ab-sb-pill" type="button" data-category="keyboard" aria-pressed="false">Keyboards</button>
        <button class="ab-sb-pill" type="button" data-category="mousepad" aria-pressed="false">Mousepads</button>
        <button class="ab-sb-pill" type="button" data-category="monitor" aria-pressed="false">Monitors</button>
        <button class="ab-sb-pill" type="button" data-category="headset" aria-pressed="false">Headsets</button>
        <button class="ab-sb-pill" type="button" data-category="chair" aria-pressed="false">Chairs</button>
        <button class="ab-sb-pill" type="button" data-category="topup" aria-pressed="false">Top-ups</button>
        <button class="ab-sb-pill" type="button" data-category="cdkeys" aria-pressed="false">CDKeys</button>
        <button class="ab-sb-pill" type="button" data-category="giftcards" aria-pressed="false">Gift-cards</button>
      </div>

      <div class="ab-sb-grid" id="gear-grid" aria-label="Latest prices on hot gear">

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
             made a row nobody could read, while the categories stay on one line
             at 1440 — seven since the top-up cards joined at the bottom of the
             grid (2026-11-11). gear.js reads data-category, on the card and on
             the pill. -->

        <article class="ab-sb-card" id="finalmouse-starlight-x" data-category="mouse" data-search="finalmouse starlight x mouse">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/finalmouse-starlight-x/01.jpg" alt="A navy Finalmouse Starlight X seen from above on a white field" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Finalmouse Starlight X</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">$125</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Finalmouse Starlight X — we buy it for you" data-name="Finalmouse Starlight X" data-price="125">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Corsair HS80 v2 MAX Wireless — we buy it for you" data-name="Corsair HS80 v2 MAX Wireless" data-price="139">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Logitech G Pro X2 RAPID — we buy it for you" data-name="Logitech G Pro X2 RAPID" data-price="160">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Corsair Sabre V3 Pro — we buy it for you" data-name="Corsair Sabre V3 Pro" data-price="126">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Logitech G Pro X3 LIGHTSPEED Headset — we buy it for you" data-name="Logitech G Pro X3 LIGHTSPEED Headset" data-price="174">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on LiberNovo Omni SE — we buy it for you" data-name="LiberNovo Omni SE" data-price="629">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Corsair MM Glass — we buy it for you" data-name="Corsair MM Glass" data-price="70">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Logitech G Pro X3 SUPERSTRIKE — we buy it for you" data-name="Logitech G Pro X3 SUPERSTRIKE" data-price="140">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Corsair MM Anti-fray — we buy it for you" data-name="Corsair MM Anti-fray" data-price="14">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on VAXEE NP-01 Ergo — we buy it for you" data-name="VAXEE NP-01 Ergo" data-price="105">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Razer Huntsman V3 Pro Low-Profile TKL 8KHz — we buy it for you" data-name="Razer Huntsman V3 Pro Low-Profile TKL 8KHz" data-price="160">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Secretlab Atlas — we buy it for you" data-name="Secretlab Atlas" data-price="349">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Corsair Nightsword V2 Wireless — we buy it for you" data-name="Corsair Nightsword V2 Wireless" data-price="91">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on X-Raypad NOD — we buy it for you" data-name="X-Raypad NOD" data-price="74">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Razer Huntsman V3 HE Magnetic 8KHz — we buy it for you" data-name="Razer Huntsman V3 HE Magnetic 8KHz" data-price="97">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on EPOMAKER HE75 V2 TMR — we buy it for you" data-name="EPOMAKER HE75 V2 TMR" data-price="90">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on ZOWIE XQ2566X — we buy it for you" data-name="ZOWIE XQ2566X" data-price="630">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on AndaSeat Kaiser 4 6D — we buy it for you" data-name="AndaSeat Kaiser 4 6D" data-price="384">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Corsair HS35 v3 Wireless — we buy it for you" data-name="Corsair HS35 v3 Wireless" data-price="55">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Corsair Clipper Pro Mini 60 — we buy it for you" data-name="Corsair Clipper Pro Mini 60" data-price="69">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Pulsar eS Jupiter Pro — we buy it for you" data-name="Pulsar eS Jupiter Pro" data-price="28">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Razer Atlas Pro — we buy it for you" data-name="Razer Atlas Pro" data-price="91">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on MelGeek Made68 Ultra V2 — we buy it for you" data-name="MelGeek Made68 Ultra V2" data-price="153">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on SteelSeries Arctis Nova Pro Omni — we buy it for you" data-name="SteelSeries Arctis Nova Pro Omni" data-price="279">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on VAXEE NP-01S V3 — we buy it for you" data-name="VAXEE NP-01S V3" data-price="105">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Razer Gigantus V2 Pro — we buy it for you" data-name="Razer Gigantus V2 Pro" data-price="35">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Pulsar eS PD170 — we buy it for you" data-name="Pulsar eS PD170" data-price="35">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on SteelSeries Apex Pro Gen 3 — we buy it for you" data-name="SteelSeries Apex Pro Gen 3" data-price="181">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Razer Viper V4 Pro — we buy it for you" data-name="Razer Viper V4 Pro" data-price="112">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Pulsar X2N Crazylight — we buy it for you" data-name="Pulsar X2N Crazylight" data-price="91">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Razer Iskur V2 NewGen — we buy it for you" data-name="Razer Iskur V2 NewGen" data-price="454">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Pulsar eS FS-1 — we buy it for you" data-name="Pulsar eS FS-1" data-price="126">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Corsair Galleon 100 SD — we buy it for you" data-name="Corsair Galleon 100 SD" data-price="244">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Logitech G Pro X2 SUPERSTRIKE — we buy it for you" data-name="Logitech G Pro X2 SUPERSTRIKE" data-price="126">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Corsair MM Pro Control — we buy it for you" data-name="Corsair MM Pro Control" data-price="42">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Banks Collection Heavy Claw by ESPTIGER — we buy it for you" data-name="Banks Collection Heavy Claw by ESPTIGER" data-price="31">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on IQUNIX EV63 — we buy it for you" data-name="IQUNIX EV63" data-price="118">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on VAXEE PD140 — we buy it for you" data-name="VAXEE PD140" data-price="35">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Wooting 60HE v2 — we buy it for you" data-name="Wooting 60HE v2" data-price="125">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Blacklyte Kraken Pro — we buy it for you" data-name="Blacklyte Kraken Pro" data-price="454">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on SONY INZONE H9 II — we buy it for you" data-name="SONY INZONE H9 II" data-price="244">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Razer BlackShark V3 Pro — we buy it for you" data-name="Razer BlackShark V3 Pro" data-price="174">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Sony INZONE M10S — we buy it for you" data-name="Sony INZONE M10S" data-price="629">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Corsair VOID Wireless V2 — we buy it for you" data-name="Corsair VOID Wireless V2" data-price="83">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Blacklyte Athena Pro — we buy it for you" data-name="Blacklyte Athena Pro" data-price="349">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on ZOWIE XL2586X+ — we buy it for you" data-name="ZOWIE XL2586X+" data-price="700">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Blacklyte Kraken — we buy it for you" data-name="Blacklyte Kraken" data-price="363">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Razer Iskur V2 — we buy it for you" data-name="Razer Iskur V2" data-price="454">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on ZOWIE XL2566X+ — we buy it for you" data-name="ZOWIE XL2566X+" data-price="454">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on NZXT Relay (+ SwitchMix) — we buy it for you" data-name="NZXT Relay (+ SwitchMix)" data-price="160">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Razer BlackShark V2 Pro — we buy it for you" data-name="Razer BlackShark V2 Pro" data-price="139">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Logitech G Pro X 2 LIGHTSPEED Headset — we buy it for you" data-name="Logitech G Pro X 2 LIGHTSPEED Headset" data-price="160">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on ASUS ROG SWIFT PG27AQN — we buy it for you" data-name="ASUS ROG SWIFT PG27AQN" data-price="419">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on ZOWIE XL2566K — we buy it for you" data-name="ZOWIE XL2566K" data-price="419">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on MSI Oculux NXG253R — we buy it for you" data-name="MSI Oculux NXG253R" data-price="350">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Secretlab Titan Evo 2022 — we buy it for you" data-name="Secretlab Titan Evo 2022" data-price="384">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Herman Miller x Logitech G Embody Gaming Chair — we buy it for you" data-name="Herman Miller x Logitech G Embody Gaming Chair" data-price="1257">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Zowie XL2546K — we buy it for you" data-name="Zowie XL2546K" data-price="279">
              <span class="ab-sb-card__label">Get a quote</span>
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
            <button type="button" class="ab-request" aria-label="Ask for a quote on Zowie XL2546 — we buy it for you" data-name="Zowie XL2546" data-price="349">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <!-- TOP-UP CARDS BEGIN (generated by _tmp_ocr/gear_topup_cards_apply.py) -->

        <!-- The nineteen Top-ups products moved onto this shelf (2026-11-11,
             user: 「将 http://127.0.0.1:8003/top-ups/ 的商品移至
             http://127.0.0.1:8003/，商品只显示最低那一档的价格」), and on the
             three follow-up choices: they join Popular gear rather than a band
             of their own, /top-ups/ is deleted outright — no redirect — and
             the nav loses TOP-UPS — and the price reads "From $X".

             So each card shows one price, the entry tier's. The catalogue's
             Spec dropdown does not come along: the shelf is a list of things
             to ask about, and the exact amount is settled in the chat with the
             data-name below, which names the tier that price buys. The ids are
             the catalogue's, so /top-ups/pubg-mobile/'s "More from Top-ups"
             links land on /#pubg-gcoin and friends. Only the PUBG card links
             on — its title opens the one detail page the catalogue keeps
             (/top-ups/pubg-mobile/); every other card stays unlinked, as the
             gear cards above it are.

             Covers are the catalogue's transparent 1200x250 wordmarks cut to
             their alpha box and centred on a 960x960 ground of #f6f9fc — the
             media box's own colour — by _tmp_ocr/gear_topup_cards_prep.py, so
             the 1:1 frame needs no CSS of its own. Delta Force is the one mark
             whose name is white on transparency: it gets a dark ground, or its
             name would not read.

             data-search carries "topup top-up" as well as the title, so the
             hero box finds them and the Top-ups pill can stand alone.

             Later the same day the action became "Get channel coupons"
             (2026-11-11, user: 「将 top-ups的 Get link or channel 改成类似于
             获取渠道和优惠券」; 「Get channel & coupons 改成获取渠道优惠券」):
             the first pass wrote "Get channel & coupons", the second dropped
             the ampersand. A top-up is bought on its own channel and the
             channel's coupons are part of the answer, while the other cards
             kept "Get link or channel" until that day's second pass made
             them "Get a quote" (see the comment above the wrapper). Only the
             label and the aria-label change; data-name and data-price stay.

             The price line gained its tier the same day (user: 「类似 From
             $1.18 等这些价格，需要对应一个档位/规格」): "From $X" alone left
             the amount floating, so a small line under it names the entry
             tier the price buys — the first row of the catalogue's Spec
             dropdown, taken from data-name. -->

        <article class="ab-sb-card" id="douyin-top-up" data-category="topup" data-search="douyin live topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/douyin-top-up-square.png" alt="Douyin Live wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Douyin Live</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $1.17</span>
            <span class="ab-sb-card__tier">60 Diamonds</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Douyin Live — 60 Diamonds" data-name="Douyin Live — 60 Diamonds" data-price="1.17">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="telegram" data-category="topup" data-search="telegram topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/telegram-square.png" alt="Telegram wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Telegram</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $0.88</span>
            <span class="ab-sb-card__tier">50 Stars</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Telegram — 50 Stars" data-name="Telegram — 50 Stars" data-price="0.88">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="pubg-mobile" data-category="topup" data-search="pubg mobile uc topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/pubg-mobile-square.png" alt="PUBG Mobile UC wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title"><a href="/top-ups/pubg-mobile/">PUBG Mobile UC</a></h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $0.80</span>
            <span class="ab-sb-card__tier">60 UC</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for PUBG Mobile UC — 60 UC" data-name="PUBG Mobile UC — 60 UC" data-price="0.80">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="pubg-gcoin" data-category="topup" data-search="pubg g-coin topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/pubg-gcoin-square.png" alt="PUBG G-COIN wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">PUBG G-COIN</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $0.86</span>
            <span class="ab-sb-card__tier">100 G-COIN</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for PUBG G-COIN — 100 G-COIN" data-name="PUBG G-COIN — 100 G-COIN" data-price="0.86">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="hok" data-category="topup" data-search="honor of kings topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/hok-square.png" alt="Honor of Kings wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Honor of Kings</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $0.75</span>
            <span class="ab-sb-card__tier">80 Tokens</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Honor of Kings — 80 Tokens" data-name="Honor of Kings — 80 Tokens" data-price="0.75">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="arena-breakout" data-category="topup" data-search="arena breakout topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/arena-breakout-square.png" alt="Arena Breakout wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Arena Breakout</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $0.75</span>
            <span class="ab-sb-card__tier">60 + 6 Bonds</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Arena Breakout — 60 + 6 Bonds" data-name="Arena Breakout — 60 + 6 Bonds" data-price="0.75">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="pokemon-go" data-category="topup" data-search="pokémon go topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/pokemon-go-square.png" alt="Pokémon GO wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Pokémon GO</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $3.84</span>
            <span class="ab-sb-card__tier">550 PokéCoins</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Pokémon GO — 550 PokéCoins" data-name="Pokémon GO — 550 PokéCoins" data-price="3.84">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="mobile-legends" data-category="topup" data-search="mobile legends: bang bang topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/mobile-legends-square.png" alt="Mobile Legends: Bang Bang wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Mobile Legends: Bang Bang</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $1.27</span>
            <span class="ab-sb-card__tier">86 Diamonds</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Mobile Legends: Bang Bang — 86 Diamonds" data-name="Mobile Legends: Bang Bang — 86 Diamonds" data-price="1.27">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="honkai-star-rail" data-category="topup" data-search="honkai: star rail topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/honkai-star-rail-square.png" alt="Honkai: Star Rail wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Honkai: Star Rail</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $0.90</span>
            <span class="ab-sb-card__tier">60 Oneiric Shard</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Honkai: Star Rail — 60 Oneiric Shard" data-name="Honkai: Star Rail — 60 Oneiric Shard" data-price="0.90">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="genshin" data-category="topup" data-search="genshin impact topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/genshin-square.png" alt="Genshin Impact wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Genshin Impact</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $1.01</span>
            <span class="ab-sb-card__tier">60 Genesis Crystals</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Genshin Impact — 60 Genesis Crystals" data-name="Genshin Impact — 60 Genesis Crystals" data-price="1.01">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="clash-of-clans" data-category="topup" data-search="clash of clans topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/clash-of-clans-square.png" alt="Clash of Clans wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Clash of Clans</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $4.23</span>
            <span class="ab-sb-card__tier">500 Gems</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Clash of Clans — 500 Gems" data-name="Clash of Clans — 500 Gems" data-price="4.23">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="clash-royale" data-category="topup" data-search="clash royale topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/clash-royale-square.png" alt="Clash Royale wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Clash Royale</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $4.27</span>
            <span class="ab-sb-card__tier">500 Gems</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Clash Royale — 500 Gems" data-name="Clash Royale — 500 Gems" data-price="4.27">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="brawl-stars" data-category="topup" data-search="brawl stars topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/brawl-stars-square.png" alt="Brawl Stars wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Brawl Stars</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $1.74</span>
            <span class="ab-sb-card__tier">30 GEMS</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Brawl Stars — 30 GEMS" data-name="Brawl Stars — 30 GEMS" data-price="1.74">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="arena-of-valor" data-category="topup" data-search="arena of valor topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/arena-of-valor-square.png" alt="Arena of Valor wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Arena of Valor</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $0.46</span>
            <span class="ab-sb-card__tier">11 Coupons</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Arena of Valor — 11 Coupons" data-name="Arena of Valor — 11 Coupons" data-price="0.46">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="delta-force" data-category="topup" data-search="delta force topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/delta-force-square.png" alt="Delta Force wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Delta Force</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $0.40</span>
            <span class="ab-sb-card__tier">30 Coins</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Delta Force — 30 Coins" data-name="Delta Force — 30 Coins" data-price="0.40">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="valorant" data-category="topup" data-search="valorant topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/valorant-square.png" alt="VALORANT wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">VALORANT</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $3.15</span>
            <span class="ab-sb-card__tier">475 VP</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for VALORANT — 475 VP" data-name="VALORANT — 475 VP" data-price="3.15">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="diablo-iv" data-category="topup" data-search="diablo iv topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/diablo-iv-square.png" alt="Diablo IV wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Diablo IV</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $8.87</span>
            <span class="ab-sb-card__tier">1000 Platinum</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for Diablo IV — 1000 Platinum" data-name="Diablo IV — 1000 Platinum" data-price="8.87">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="lol-wild-rift" data-category="topup" data-search="league of legends: wild rift topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/lol-wild-rift-square.png" alt="League of Legends: Wild Rift wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">League of Legends: Wild Rift</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $3.10</span>
            <span class="ab-sb-card__tier">425 Cores</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for League of Legends: Wild Rift — 425 Cores" data-name="League of Legends: Wild Rift — 425 Cores" data-price="3.10">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="cs2" data-category="topup" data-search="cs2 skins &amp; credits topup top-up">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/cs2-square.png" alt="CS2 Skins &amp; Credits wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">CS2 Skins &amp; Credits</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $2.29</span>
            <span class="ab-sb-card__tier">CS2 Case Key</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Get channel coupons for CS2 Skins &amp; Credits — CS2 Case Key" data-name="CS2 Skins &amp; Credits — CS2 Case Key" data-price="2.29">
              <span class="ab-sb-card__label">Get channel coupons</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <!-- TOP-UP CARDS END -->

        <!-- CATALOGUE CARDS BEGIN (generated by _tmp_ocr/gear_catalog_cards_apply.py) -->

        <!-- The seventeen CDKeys and Gift-cards products moved onto this
             shelf too (2026-11-11, user: 「将 http://127.0.0.1:8003/cdkeys/
             和 http://127.0.0.1:8003/gift-cards/ 也同样处理」), on the same
             two choices the Top-ups block above records: they join Popular
             gear rather than a band of their own, and both pages are deleted
             outright — no redirect, nav down to HOME / NEWS / GUIDES — with
             the price reading "From $X".

             Eleven cards are CDKeys', six are Gift-cards', in the order the
             two pages had them. Each shows one price, the entry tier's; the
             Spec dropdown does not come along, because the shelf is a list of
             things to ask about and the exact amount is settled in the chat
             with the data-name below, which names the tier that price buys.
             The three cards the catalogue had no price for — Windows 11 Pro,
             Costco's Gold Star membership, Microsoft 365 — come along too and
             read "Price on request" (user: 「写 Price on request」): the
             button still opens the chat, and the quote is the answer. They
             have no data-price, so sourcing.js sends the name alone.

             Every priced card also names its entry tier under the price
             (user: 「类似 From $1.18 等这些价格，需要对应一个档位/规格」), the
             first row of the catalogue's Spec dropdown; the unpriced three
             never had a tier list, so they carry no tier line.

             Covers: the fourteen wordmarks are cut to their alpha box and
             centred on a 960x960 ground of #f6f9fc — the media box's own
             colour, as in the Top-ups block — by
             _tmp_ocr/gear_catalog_cards_prep.py. Fortnite's and Kammelna's
             names are white on transparency, so those two take the dark
             ground. The three unpriced cards keep the catalogue's photographs
             (/assets/gear/<id>/01.jpg), cropped 1:1 by the media box's
             object-fit; their data-gallery stays behind, since the shelf has
             no lightbox.

             data-search adds "cdkeys cdkey" or "giftcard gift-card" to the
             title, so the hero box and the two new pills find them. -->

        <article class="ab-sb-card" id="fortnite-card" data-category="cdkeys" data-search="fortnite v-bucks card cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/fortnite-card-square.png" alt="Fortnite V-Bucks Card wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Fortnite V-Bucks Card</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $9.99</span>
            <span class="ab-sb-card__tier">1000 V-Bucks (Austria)</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Fortnite V-Bucks Card — 1000 V-Bucks (Austria) — we buy it for you" data-name="Fortnite V-Bucks Card — 1000 V-Bucks (Austria)" data-price="9.99">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="apex-legends" data-category="cdkeys" data-search="apex legends coins cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/apex-legends-square.png" alt="Apex Legends Coins wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Apex Legends Coins</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $11.12</span>
            <span class="ab-sb-card__tier">1000 Coins</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Apex Legends Coins — 1000 Coins — we buy it for you" data-name="Apex Legends Coins — 1000 Coins" data-price="11.12">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="playstation" data-category="cdkeys" data-search="playstation network card cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/playstation-square.png" alt="PlayStation Network Card wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">PlayStation Network Card</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $1.18</span>
            <span class="ab-sb-card__tier">1 USD</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on PlayStation Network Card — 1 USD — we buy it for you" data-name="PlayStation Network Card — 1 USD" data-price="1.18">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="pubg-gcoins" data-category="cdkeys" data-search="pubg g-coin cdk cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/pubg-gcoins-square.png" alt="PUBG G-COIN CDK wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">PUBG G-COIN CDK</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $0.91</span>
            <span class="ab-sb-card__tier">100 coin</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on PUBG G-COIN CDK — 100 coin — we buy it for you" data-name="PUBG G-COIN CDK — 100 coin" data-price="0.91">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="ns-membership" data-category="cdkeys" data-search="nintendo switch online membership cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/ns-membership-square.png" alt="Nintendo Switch Online Membership wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Nintendo Switch Online Membership</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $3.82</span>
            <span class="ab-sb-card__tier">1 Month Subscription (HK)</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Nintendo Switch Online Membership — 1 Month Subscription (HK) — we buy it for you" data-name="Nintendo Switch Online Membership — 1 Month Subscription (HK)" data-price="3.82">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="nintendo-eshop" data-category="cdkeys" data-search="nintendo eshop gift card cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/nintendo-eshop-square.png" alt="Nintendo eShop Gift Card wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Nintendo eShop Gift Card</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $9.69</span>
            <span class="ab-sb-card__tier">10 USD</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Nintendo eShop Gift Card — 10 USD — we buy it for you" data-name="Nintendo eShop Gift Card — 10 USD" data-price="9.69">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="steam-wallet" data-category="cdkeys" data-search="steam wallet code cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/steam-wallet-square.png" alt="Steam Wallet Code wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Steam Wallet Code</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $1.42</span>
            <span class="ab-sb-card__tier">5 RM</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Steam Wallet Code — 5 RM — we buy it for you" data-name="Steam Wallet Code — 5 RM" data-price="1.42">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="gocash-card" data-category="cdkeys" data-search="gocash (global) cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/gocash-card-square.png" alt="GoCash (Global) wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">GoCash (Global)</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $4.79</span>
            <span class="ab-sb-card__tier">5 USD</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on GoCash (Global) — 5 USD — we buy it for you" data-name="GoCash (Global) — 5 USD" data-price="4.79">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="windows-11-pro" data-category="cdkeys" data-search="microsoft windows 11 pro cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/windows-11-pro/01.jpg" alt="The Windows 11 Pro box on a near-white field under a sticker reading activation code by email" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Microsoft Windows 11 Pro</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">Price on request</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Microsoft Windows 11 Pro — we buy it for you" data-name="Microsoft Windows 11 Pro">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="costco-gold-star-membership" data-category="cdkeys" data-search="costco 1-year gold star membership + $45 digital costco shop card cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/costco-gold-star-membership/01.jpg" alt="A couple carrying pizza boxes and two drinks at a warehouse snack counter" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Costco 1-Year Gold Star Membership + $45 Digital Costco Shop Card</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">Price on request</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Costco 1-Year Gold Star Membership + $45 Digital Costco Shop Card — we buy it for you" data-name="Costco 1-Year Gold Star Membership + $45 Digital Costco Shop Card">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="microsoft-365-1-year" data-category="cdkeys" data-search="microsoft 365: 1-year subscription cdkeys cdkey">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/gear/microsoft-365-1-year/01.jpg" alt="The Microsoft 365 Personal box with its year-one features listed on the front" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Microsoft 365: 1-Year Subscription</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">Price on request</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Microsoft 365: 1-Year Subscription — we buy it for you" data-name="Microsoft 365: 1-Year Subscription">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="amazon-gift-card-us" data-category="giftcards" data-search="amazon gift card (us) giftcards gift-card giftcard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/amazon-gift-card-us-square.png" alt="Amazon Gift Card (US) wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Amazon Gift Card (US)</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $4.95</span>
            <span class="ab-sb-card__tier">5 USD</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Amazon Gift Card (US) — 5 USD — we buy it for you" data-name="Amazon Gift Card (US) — 5 USD" data-price="4.95">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="apple-gift-card" data-category="giftcards" data-search="apple gift card giftcards gift-card giftcard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/apple-gift-card-square.png" alt="Apple Gift Card wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Apple Gift Card</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $4.50</span>
            <span class="ab-sb-card__tier">5 USD</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Apple Gift Card — 5 USD — we buy it for you" data-name="Apple Gift Card — 5 USD" data-price="4.50">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="google-play-gift-card" data-category="giftcards" data-search="google play gift card giftcards gift-card giftcard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/google-play-gift-card-square.png" alt="Google Play Gift Card wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Google Play Gift Card</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $4.95</span>
            <span class="ab-sb-card__tier">5 USD</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Google Play Gift Card — 5 USD — we buy it for you" data-name="Google Play Gift Card — 5 USD" data-price="4.95">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="netflix-gift-card-us" data-category="giftcards" data-search="netflix gift card (us) giftcards gift-card giftcard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/netflix-gift-card-us-square.png" alt="Netflix Gift Card (US) wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Netflix Gift Card (US)</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $20.25</span>
            <span class="ab-sb-card__tier">20 USD</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Netflix Gift Card (US) — 20 USD — we buy it for you" data-name="Netflix Gift Card (US) — 20 USD" data-price="20.25">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="xbox-gift-card" data-category="giftcards" data-search="xbox live gift card giftcards gift-card giftcard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/xbox-gift-card-square.png" alt="Xbox Live Gift Card wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Xbox Live Gift Card</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $4.59</span>
            <span class="ab-sb-card__tier">5 USD</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Xbox Live Gift Card — 5 USD — we buy it for you" data-name="Xbox Live Gift Card — 5 USD" data-price="4.59">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <article class="ab-sb-card" id="kammelna-gift-card" data-category="giftcards" data-search="kammelna gift card giftcards gift-card giftcard">
          <div class="ab-sb-card__media ab-card__media">
            <img src="/assets/digital/kammelna-gift-card-square.png" alt="Kammelna Gift Card wordmark" loading="lazy" decoding="async">
          </div>
          <h3 class="ab-sb-card__title">Kammelna Gift Card</h3>
          <p class="ab-sb-card__quote">
            <span class="ab-sb-card__price">From $8.09</span>
            <span class="ab-sb-card__tier">30 Days</span>
          </p>
          <div class="ab-sb-card__bottom">
            <button type="button" class="ab-request" aria-label="Ask for a quote on Kammelna Gift Card — 30 Days — we buy it for you" data-name="Kammelna Gift Card — 30 Days" data-price="8.09">
              <span class="ab-sb-card__label">Get a quote</span>
              <span class="ab-sb-card__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h13M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
            </button>
          </div>
        </article>

        <!-- CATALOGUE CARDS END -->

      </div>

      <p class="ab-sb-empty" id="gear-empty" hidden>No quote here matches that search. Paste a product link above and we will check its lowest price in the live chat.</p>

    </div>
  </section>

</div>
