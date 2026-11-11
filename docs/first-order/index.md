---
title: First order
description: Your first order from China, step by step — paste a product link from any shop and we buy it for you from the brand supplier or from Pinduoduo, JD or Taobao, then inspect it, assemble it where needed and deliver it to your door.
icon: material/package-variant-closed
hide:
  - title
  - toc
---

<!-- 2026-11-11 (user: 「https://www.panli.com/helps/daigou 模仿这个页面
     新增一个页面，并在导航中展示」). The reference page's parts, in its order:
     a full-bleed hero with two buttons; a white card of five perks lifted over
     the hero's bottom edge; a six-step "how it works" section with a large
     step card; a "fees" band with the total beside the terms of a formula; a
     grid of restriction tiles; a closing call to action; a dark contact
     footer. The address is /first-order/, the nav label FIRST ORDER, and the
     reference site is not named anywhere — same rule as the rest of the repo.

     2026-11-11, after the first build (user: 「这里的意思要表达的是，用户提交任何
     网站的商品链接，我们会优先从品牌供应商，或中国的三大平台购物平台，拼多多，
     京东或淘宝为您采购并提供验货、组装及配送服务」): the page is a buying
     service after all. The hero says any shop's link, and the chain runs
     paste a link -> we source it from the brand supplier or Pinduoduo / JD /
     Taobao -> we buy it for you -> we receive, inspect and assemble -> we
     pack and deliver -> you receive it. The home page was aligned to the same
     offer later that day (its hero, dialog, steps and shelf lead all sell the
     purchase now), so the two pages say the same thing.

     The fee formula keeps the reference's shape but not its numbers: item
     price + shipping to us + delivery, with the price check free and no
     service percentage. Nothing here invents a fee or a delivery time.

     Markup is one .ab-fo wrapper styled by stylesheets/first-order.css; the
     page is checked by _tmp_ocr/first_order_probe.py. -->

<div class="ab-fo" markdown="0">

  <section class="ab-fo-hero">
    <div class="ab-fo-inner ab-fo-hero__inner">
      <h1 class="ab-fo-hero__title">Your first order from China</h1>
      <p class="ab-fo-hero__lead">Paste a product link from any shop. We buy it for you &mdash; from the brand supplier first, otherwise from China's three big platforms, Pinduoduo, JD or Taobao &mdash; and handle inspection, assembly and delivery to your door. Here is how it runs, step by step.</p>
      <div class="ab-fo-hero__actions">
        <a class="ab-fo-btn" href="/#gear-search">Check a price</a>
        <a class="ab-fo-btn ab-fo-btn--ghost" href="/#gear">Browse popular gear</a>
      </div>
    </div>
  </section>

  <section class="ab-fo-perks">
    <div class="ab-fo-inner">
      <ul class="ab-fo-perks__row">
        <li class="ab-fo-perk">
          <span class="ab-fo-perk__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
          </span>
          <span class="ab-fo-perk__label">Any shop, one box</span>
          <span class="ab-fo-perk__note">A link from any site goes into the same box.</span>
        </li>
        <li class="ab-fo-perk">
          <span class="ab-fo-perk__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.59 13.41 13.42 20.58a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><circle cx="7" cy="7" r="1.2"/></svg>
          </span>
          <span class="ab-fo-perk__label">The price check is free</span>
          <span class="ab-fo-perk__note">You pay nothing to ask what an item costs in China.</span>
        </li>
        <li class="ab-fo-perk">
          <span class="ab-fo-perk__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>
          </span>
          <span class="ab-fo-perk__label">Sourced at the source</span>
          <span class="ab-fo-perk__note">The brand supplier first, then Pinduoduo, JD or Taobao.</span>
        </li>
        <li class="ab-fo-perk">
          <span class="ab-fo-perk__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m16.5 16.5 4 4"/><path d="M8.5 11h5"/><path d="M11 8.5v5"/></svg>
          </span>
          <span class="ab-fo-perk__label">Inspected and assembled</span>
          <span class="ab-fo-perk__note">Opened, checked against your order and assembled where it needs it.</span>
        </li>
        <li class="ab-fo-perk">
          <span class="ab-fo-perk__icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 3h14v13H1z"/><path d="M15 8h4l3 3v5h-7V8z"/><circle cx="5.5" cy="18.5" r="1.8"/><circle cx="17.5" cy="18.5" r="1.8"/></svg>
          </span>
          <span class="ab-fo-perk__label">Delivered worldwide</span>
          <span class="ab-fo-perk__note">Consolidated, repacked and tracked to your door.</span>
        </li>
      </ul>
    </div>
  </section>

  <section class="ab-fo-section ab-fo-how">
    <div class="ab-fo-inner">
      <h2 class="ab-fo-h2">How it works</h2>
      <p class="ab-fo-lead">Six steps from a link to a parcel at your door.</p>
      <ol class="ab-fo-steps">
        <li class="ab-fo-step">
          <span class="ab-fo-step__num">01</span>
          <h3 class="ab-fo-step__title">Paste a link</h3>
          <p class="ab-fo-step__text">Paste a product link from any shop &mdash; Pinduoduo, JD, Taobao or anywhere else &mdash; into the box on the home page. One link is enough.</p>
        </li>
        <li class="ab-fo-step">
          <span class="ab-fo-step__num">02</span>
          <h3 class="ab-fo-step__title">We find the best source</h3>
          <p class="ab-fo-step__text">We look for the item at the brand supplier first, then on Pinduoduo, JD and Taobao, and pick the seller that has it in stock at the lowest price.</p>
        </li>
        <li class="ab-fo-step">
          <span class="ab-fo-step__num">03</span>
          <h3 class="ab-fo-step__title">We buy it for you</h3>
          <p class="ab-fo-step__text">We place the order and pay the seller at the price we quoted you. The item price carries no margin from us.</p>
        </li>
        <li class="ab-fo-step">
          <span class="ab-fo-step__num">04</span>
          <h3 class="ab-fo-step__title">We receive and inspect</h3>
          <p class="ab-fo-step__text">When it reaches our warehouse we open it, check it against your order, photograph it and assemble anything that ships flat. If something is wrong, we tell you before it ships.</p>
        </li>
        <li class="ab-fo-step">
          <span class="ab-fo-step__num">05</span>
          <h3 class="ab-fo-step__title">We pack and deliver</h3>
          <p class="ab-fo-step__text">We consolidate your parcels, repack them and quote the delivery before anything leaves. You approve the amount first.</p>
        </li>
        <li class="ab-fo-step">
          <span class="ab-fo-step__num">06</span>
          <h3 class="ab-fo-step__title">You receive it</h3>
          <p class="ab-fo-step__text">You get the tracking number from our warehouse to your door, and we follow the parcel with you until it lands.</p>
        </li>
      </ol>
    </div>
  </section>

  <section class="ab-fo-section ab-fo-cost">
    <div class="ab-fo-inner">
      <h2 class="ab-fo-h2">What your total comes to</h2>
      <p class="ab-fo-lead">Three parts, and the price check costs nothing.</p>
      <div class="ab-fo-formula">
        <div class="ab-fo-term ab-fo-term--total">
          <span class="ab-fo-term__label">Total</span>
          <span class="ab-fo-term__note">what you pay</span>
        </div>
        <span class="ab-fo-op" aria-hidden="true">=</span>
        <div class="ab-fo-term">
          <span class="ab-fo-term__label">Item price</span>
          <span class="ab-fo-term__note">what the seller charges, quoted to you before we buy</span>
        </div>
        <span class="ab-fo-op" aria-hidden="true">+</span>
        <div class="ab-fo-term">
          <span class="ab-fo-term__label">Shipping to us</span>
          <span class="ab-fo-term__note">the shop's delivery inside China to our warehouse</span>
        </div>
        <span class="ab-fo-op" aria-hidden="true">+</span>
        <div class="ab-fo-term">
          <span class="ab-fo-term__label">Delivery</span>
          <span class="ab-fo-term__note">quoted per parcel by weight and destination, before it ships</span>
        </div>
      </div>
      <p class="ab-fo-cost__note">Delivery is quoted before your parcel leaves our warehouse, and nothing is charged until you approve it. Customs duty is not part of the total &mdash; it is charged in your country, to you.</p>
      <div class="ab-fo-cost__actions">
        <a class="ab-fo-btn" href="/#gear-search">Check a price</a>
      </div>
    </div>
  </section>

  <section class="ab-fo-section ab-fo-limits">
    <div class="ab-fo-inner">
      <h2 class="ab-fo-h2">What we can't send</h2>
      <p class="ab-fo-lead">Four things worth checking before you buy.</p>
      <div class="ab-fo-limits__grid">
        <article class="ab-fo-limit">
          <h3 class="ab-fo-limit__title">Prohibited goods</h3>
          <p class="ab-fo-limit__text">Customs bans these outright &mdash; weapons, drugs, counterfeit goods, fresh food, live plants. We can't take them into the warehouse or send them on.</p>
        </article>
        <article class="ab-fo-limit">
          <h3 class="ab-fo-limit__title">Restricted goods</h3>
          <p class="ab-fo-limit__text">Some items clear only with the right paperwork or a permit &mdash; batteries, liquids, branded goods. Ask us before you order and we will tell you what the destination needs.</p>
        </article>
        <article class="ab-fo-limit">
          <h3 class="ab-fo-limit__title">Oversized or heavy parcels</h3>
          <p class="ab-fo-limit__text">Delivery is charged on the greater of actual and volumetric weight, so a bulky parcel costs more than it weighs. Ask for a quote before you buy something large.</p>
        </article>
        <article class="ab-fo-limit">
          <h3 class="ab-fo-limit__title">Customs duty</h3>
          <p class="ab-fo-limit__text">Duty and tax charged in your country are yours to pay. We declare the parcel honestly and don't cover what customs charges.</p>
        </article>
      </div>
    </div>
  </section>

  <section class="ab-fo-cta">
    <div class="ab-fo-inner ab-fo-cta__inner">
      <h2 class="ab-fo-cta__title">Ready to start?</h2>
      <p class="ab-fo-cta__lead">Paste a link and we'll email you what it costs, where we'll source it and what delivery adds.</p>
      <div class="ab-fo-cta__actions">
        <a class="ab-fo-btn" href="/#gear-search">Get a quote</a>
        <button class="ab-fo-btn ab-fo-btn--ghost ab-crisp-open" type="button" data-crisp-msg="Hello, this is my first order — I have a question before I start.">Live chat</button>
      </div>
    </div>
  </section>

</div>
