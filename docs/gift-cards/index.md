---
title: Gift-cards
description: AceBase Gift-cards — store gift cards, 6 cards, tiers from $4.50.
hide:
  - title
  - toc
---

<!-- 礼品卡目录。六款的款式与全部面值定价取自 acebase.cc 的
     /gift-cards/ 页，2026-11-01 随数字商品目录一起进来，一直是
     /services/ 网格的后半段。

     2026-11-08 用户「新增一个 Gift Cards 类目，同样将 /services/ 中的
     礼品卡移过去」：这六款单独成页 docs/gift-cards/，卡片 markup 与
     在 /services/ 时逐字相同（生成器同一个 card()），顺序照 SECTIONS
     的 Gift Cards 组，所以 Amazon 仍是第一张。外充 2 款与 /cdkeys/
     的十一张询价卡留在目录页 —— 询价卡是卡密/钱包码，不是礼品卡；那页
     同日改名 /top-up/（用户「将 services 类目改为 Top-Up」）。
     生成脚本：C:\1Work\_tmp_ocr\gen_digital_sumei.py（重跑覆盖本页）。
     2026-11-08 用户「/game/ 改名为 Top-ups，gift cards 改名为 gift-cards，
     /top-up/ 改名为 news」：外充那页成了 /news/（内容不动），游戏那页成了
     /top-ups/，礼品卡页只把标签改成 Gift-cards；旧地址 /top-up/ 与 /game/
     都 404，nav 顺序改成 HOME / TOP-UPS / CDKEYS / GIFT-CARDS / NEWS / GUIDES。
     同日晚些时候用户「将 news的商品移到 …/top-ups/，并将 top-ups/改名为
     Top ups」：外充 2 款并进 /top-ups/（排在 SECTIONS 的 Games 之前），
     这页改叫「Top ups」（nav 标签 TOP UPS，地址仍是 /top-ups/）。
     卡片版式取自 acebase.cc 早先的 /gift-cards/ 页（2026-11-01 用户：「按
     /gift-cards/ 页的样式进行排版」；本站同名页 2026-11-08 才建，用的就是
     这套卡）：--plate --wordmark 的 5:2 画框（品牌条 cover 裁进
     去）、左上角档数角标、价格跟在标题末尾、Spec 下拉。栅格是 --pricing 的
     三列（1024 起）。动作行是本站的 .ab-request（sourcing.js；2026-11-02 由
     + Add to cart 改写，同日按钮文案再改为 ORDER NOW，购物车已取消）：点一下
     把档位名与价格送进在线客服，不是那页的 Buy；下拉换档时由
     docs/javascripts/digital.js 同步价格、data-* 与无障碍名。
     品牌条图在 docs/assets/digital/<id>.png（1200x250，保留原画布留白）。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <div class="ab-list ab-list--pricing" aria-label="Gift-cards catalogue">

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="amazon-gift-card-us" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">6 tiers</span>
          <img src="/assets/digital/amazon-gift-card-us.png" alt="Amazon Gift Card (US) wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Amazon Gift Card (US)<span class="ab-card__price" data-digital-price>$4.95</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Amazon Gift Card (US)">
            <option data-name="Amazon Gift Card (US) — 5 USD" data-price="4.95">5 USD &mdash; $4.95</option>
            <option data-name="Amazon Gift Card (US) — 10 USD" data-price="9.90">10 USD &mdash; $9.90</option>
            <option data-name="Amazon Gift Card (US) — 20 USD" data-price="19.80">20 USD &mdash; $19.80</option>
            <option data-name="Amazon Gift Card (US) — 35 USD" data-price="34.65">35 USD &mdash; $34.65</option>
            <option data-name="Amazon Gift Card (US) — 50 USD" data-price="49.50">50 USD &mdash; $49.50</option>
            <option data-name="Amazon Gift Card (US) — 100 USD" data-price="99.00">100 USD &mdash; $99</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Amazon Gift Card (US) — 5 USD" data-name="Amazon Gift Card (US) — 5 USD" data-price="4.95">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="apple-gift-card" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">7 tiers</span>
          <img src="/assets/digital/apple-gift-card.png" alt="Apple Gift Card wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Apple Gift Card<span class="ab-card__price" data-digital-price>$4.50</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Apple Gift Card">
            <option data-name="Apple Gift Card — 5 USD" data-price="4.50">5 USD &mdash; $4.50</option>
            <option data-name="Apple Gift Card — 10 USD" data-price="9.00">10 USD &mdash; $9</option>
            <option data-name="Apple Gift Card — 20 USD" data-price="18.00">20 USD &mdash; $18</option>
            <option data-name="Apple Gift Card — 50 USD" data-price="45.00">50 USD &mdash; $45</option>
            <option data-name="Apple Gift Card — 100 USD" data-price="90.00">100 USD &mdash; $90</option>
            <option data-name="Apple Gift Card — 200 USD" data-price="181.80">200 USD &mdash; $181.80</option>
            <option data-name="Apple Gift Card — 500 USD" data-price="454.50">500 USD &mdash; $454.50</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Apple Gift Card — 5 USD" data-name="Apple Gift Card — 5 USD" data-price="4.50">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="google-play-gift-card" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">6 tiers</span>
          <img src="/assets/digital/google-play-gift-card.png" alt="Google Play Gift Card wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Google Play Gift Card<span class="ab-card__price" data-digital-price>$4.95</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Google Play Gift Card">
            <option data-name="Google Play Gift Card — 5 USD" data-price="4.95">5 USD &mdash; $4.95</option>
            <option data-name="Google Play Gift Card — 10 USD" data-price="9.90">10 USD &mdash; $9.90</option>
            <option data-name="Google Play Gift Card — 15 USD" data-price="14.85">15 USD &mdash; $14.85</option>
            <option data-name="Google Play Gift Card — 25 USD" data-price="24.75">25 USD &mdash; $24.75</option>
            <option data-name="Google Play Gift Card — 50 USD" data-price="49.50">50 USD &mdash; $49.50</option>
            <option data-name="Google Play Gift Card — 100 USD" data-price="99.00">100 USD &mdash; $99</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Google Play Gift Card — 5 USD" data-name="Google Play Gift Card — 5 USD" data-price="4.95">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="netflix-gift-card-us" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">6 tiers</span>
          <img src="/assets/digital/netflix-gift-card-us.png" alt="Netflix Gift Card (US) wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Netflix Gift Card (US)<span class="ab-card__price" data-digital-price>$20.25</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Netflix Gift Card (US)">
            <option data-name="Netflix Gift Card (US) — 20 USD" data-price="20.25">20 USD &mdash; $20.25</option>
            <option data-name="Netflix Gift Card (US) — 25 USD" data-price="25.20">25 USD &mdash; $25.20</option>
            <option data-name="Netflix Gift Card (US) — 30 USD" data-price="29.70">30 USD &mdash; $29.70</option>
            <option data-name="Netflix Gift Card (US) — 50 USD" data-price="49.50">50 USD &mdash; $49.50</option>
            <option data-name="Netflix Gift Card (US) — 60 USD" data-price="59.40">60 USD &mdash; $59.40</option>
            <option data-name="Netflix Gift Card (US) — 100 USD" data-price="94.50">100 USD &mdash; $94.50</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Netflix Gift Card (US) — 20 USD" data-name="Netflix Gift Card (US) — 20 USD" data-price="20.25">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="xbox-gift-card" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">7 tiers</span>
          <img src="/assets/digital/xbox-gift-card.png" alt="Xbox Live Gift Card wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Xbox Live Gift Card<span class="ab-card__price" data-digital-price>$4.59</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Xbox Live Gift Card">
            <option data-name="Xbox Live Gift Card — 5 USD" data-price="4.59">5 USD &mdash; $4.59</option>
            <option data-name="Xbox Live Gift Card — 10 USD" data-price="8.97">10 USD &mdash; $8.97</option>
            <option data-name="Xbox Live Gift Card — 15 USD" data-price="13.49">15 USD &mdash; $13.49</option>
            <option data-name="Xbox Live Gift Card — 20 USD" data-price="17.99">20 USD &mdash; $17.99</option>
            <option data-name="Xbox Live Gift Card — 25 USD" data-price="22.03">25 USD &mdash; $22.03</option>
            <option data-name="Xbox Live Gift Card — 50 USD" data-price="43.91">50 USD &mdash; $43.91</option>
            <option data-name="Xbox Live Gift Card — 100 USD" data-price="88.19">100 USD &mdash; $88.19</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Xbox Live Gift Card — 5 USD" data-name="Xbox Live Gift Card — 5 USD" data-price="4.59">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="kammelna-gift-card" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">9 tiers</span>
          <img src="/assets/digital/kammelna-gift-card.png" alt="Kammelna Gift Card wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Kammelna Gift Card<span class="ab-card__price" data-digital-price>$8.09</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Kammelna Gift Card">
            <option data-name="Kammelna Gift Card — 30 Days" data-price="8.09">30 Days &mdash; $8.09</option>
            <option data-name="Kammelna Gift Card — 90 Days" data-price="19.79">90 Days &mdash; $19.79</option>
            <option data-name="Kammelna Gift Card — 180 Days" data-price="36.89">180 Days &mdash; $36.89</option>
            <option data-name="Kammelna Gift Card — 365 Days" data-price="66.59">365 Days &mdash; $66.59</option>
            <option data-name="Kammelna Gift Card — 4,000 Gold" data-price="11.42">4,000 Gold &mdash; $11.42</option>
            <option data-name="Kammelna Gift Card — 12,000 Gold" data-price="26.21">12,000 Gold &mdash; $26.21</option>
            <option data-name="Kammelna Gift Card — 50,000 Gold" data-price="103.41">50,000 Gold &mdash; $103.41</option>
            <option data-name="Kammelna Gift Card — 100,000 Gold" data-price="199.71">100,000 Gold &mdash; $199.71</option>
            <option data-name="Kammelna Gift Card — 250,000 Gold" data-price="485.91">250,000 Gold &mdash; $485.91</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Kammelna Gift Card — 30 Days" data-name="Kammelna Gift Card — 30 Days" data-price="8.09">ORDER NOW</button></p>
        </div>
      </article>

    </div>
  </section>

</div>
