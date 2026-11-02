---
title: Services
description: AceBase Services — live top-ups and gift cards, 8 titles, tiers from $0.88.
hide:
  - title
  - toc
---

<!-- 数字商品目录。款式与全部档位定价取自 acebase.cc 的 /topup/
     （只取 Douyin Live 与 Telegram）、/gift-cards/ 两页，以及
     docs/assets/games/prices.json。Accounts 一组于 2026-11-01 按用户
     要求整组移除；同日用户「商品不需要分类，直接都放在一起」，
     这里不再分 Top-up / Gift Cards 两段，8 款平铺一张网格。
     生成脚本：C:\1Work\_tmp_ocr\gen_digital_sumei.py（重跑覆盖本页）。
     卡片版式取自 acebase.cc 的 /gift-cards/（2026-11-01 用户：「按 /gift-cards/
     页的样式进行排版」）：--plate --wordmark 的 5:2 画框（品牌条 cover 裁进
     去）、左上角档数角标、价格跟在标题末尾、Spec 下拉。栅格是 --pricing 的
     三列（1024 起）。动作行是本站的 .ab-request（sourcing.js；2026-11-02 由
     + Add to cart 改写，同日按钮文案再改为 ORDER NOW，购物车已取消）：点一下
     把档位名与价格送进在线客服，不是 /gift-cards/ 的 Buy；下拉换档时由
     docs/javascripts/digital.js 同步价格、data-* 与无障碍名。
     品牌条图在 docs/assets/digital/<id>.png（1200x250，保留原画布留白）。 -->

<div class="ab-mag" markdown="0">

  <section class="ab-section">
    <div class="ab-list ab-list--pricing" aria-label="Services catalogue">

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="douyin-top-up" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">12 tiers</span>
          <img src="/assets/digital/douyin-top-up.png" alt="Douyin Live wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Douyin Live<span class="ab-card__price" data-digital-price>$1.17</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Douyin Live">
            <option data-name="Douyin Live — 60 Diamonds" data-price="1.17">60 Diamonds &mdash; $1.17</option>
            <option data-name="Douyin Live — 100 Diamonds" data-price="1.99">100 Diamonds &mdash; $1.99</option>
            <option data-name="Douyin Live — 200 Diamonds" data-price="3.11">200 Diamonds &mdash; $3.11</option>
            <option data-name="Douyin Live — 300 Diamonds" data-price="4.50">300 Diamonds &mdash; $4.50</option>
            <option data-name="Douyin Live — 500 Diamonds" data-price="7.49">500 Diamonds &mdash; $7.49</option>
            <option data-name="Douyin Live — 1000 Diamonds" data-price="15.71">1000 Diamonds &mdash; $15.71</option>
            <option data-name="Douyin Live — 2000 Diamonds" data-price="31.41">2000 Diamonds &mdash; $31.41</option>
            <option data-name="Douyin Live — 3000 Diamonds" data-price="47.12">3000 Diamonds &mdash; $47.12</option>
            <option data-name="Douyin Live — 5000 Diamonds" data-price="78.52">5000 Diamonds &mdash; $78.52</option>
            <option data-name="Douyin Live — 8000 Diamonds" data-price="127.65">8000 Diamonds &mdash; $127.65</option>
            <option data-name="Douyin Live — 10000 Diamonds" data-price="161.07">10000 Diamonds &mdash; $161.07</option>
            <option data-name="Douyin Live — 20000 Diamonds" data-price="324.12">20000 Diamonds &mdash; $324.12</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Douyin Live — 60 Diamonds" data-name="Douyin Live — 60 Diamonds" data-price="1.17">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="telegram" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">16 tiers</span>
          <img src="/assets/digital/telegram.png" alt="Telegram wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Telegram<span class="ab-card__price" data-digital-price>$0.88</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Telegram">
            <option data-name="Telegram — 50 Stars" data-price="0.88">50 Stars &mdash; $0.88</option>
            <option data-name="Telegram — 75 Stars" data-price="1.34">75 Stars &mdash; $1.34</option>
            <option data-name="Telegram — 100 Stars" data-price="1.76">100 Stars &mdash; $1.76</option>
            <option data-name="Telegram — 150 Stars" data-price="2.64">150 Stars &mdash; $2.64</option>
            <option data-name="Telegram — 250 Stars" data-price="4.40">250 Stars &mdash; $4.40</option>
            <option data-name="Telegram — 350 Stars" data-price="6.17">350 Stars &mdash; $6.17</option>
            <option data-name="Telegram — 500 Stars" data-price="8.79">500 Stars &mdash; $8.79</option>
            <option data-name="Telegram — 750 Stars" data-price="13.20">750 Stars &mdash; $13.20</option>
            <option data-name="Telegram — 1000 Stars" data-price="17.59">1000 Stars &mdash; $17.59</option>
            <option data-name="Telegram — 1500 Stars" data-price="26.39">1500 Stars &mdash; $26.39</option>
            <option data-name="Telegram — 2500 Stars" data-price="43.96">2500 Stars &mdash; $43.96</option>
            <option data-name="Telegram — 5000 Stars" data-price="87.96">5000 Stars &mdash; $87.96</option>
            <option data-name="Telegram — 10000 Stars" data-price="175.93">10000 Stars &mdash; $175.93</option>
            <option data-name="Telegram — Premium 3 Months" data-price="14.04">Premium 3 Months &mdash; $14.04</option>
            <option data-name="Telegram — Premium 6 Months" data-price="18.69">Premium 6 Months &mdash; $18.69</option>
            <option data-name="Telegram — Premium 12 Months" data-price="33.73">Premium 12 Months &mdash; $33.73</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Telegram — 50 Stars" data-name="Telegram — 50 Stars" data-price="0.88">ORDER NOW</button></p>
        </div>
      </article>

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
