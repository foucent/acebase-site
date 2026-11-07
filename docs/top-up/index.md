---
title: Top-Up
description: AceBase Top-Up — live top-ups, 2 products, tiers from $0.88.
hide:
  - title
  - toc
---

<!-- 数字商品目录。款式与全部档位定价取自 acebase.cc 的 /topup/
     （只取 Douyin Live 与 Telegram）、/gift-cards/ 两页，以及
     docs/assets/games/prices.json。Accounts 一组于 2026-11-01 按用户
     要求整组移除；同日用户「商品不需要分类，直接都放在一起」，
     这里不再分 Top-up / Gift Cards 两段，8 款平铺一张网格。

     2026-11-06 用户「将 https://acebase.cc/game/ 和
     https://acebase.cc/cdkeys/ 的商品都移至
     https://acebase.cc/services/」：/game/ 的十七款游戏代储与
     /cdkeys/ 的十一张卡一起并进这一张网格，两页随之删除、不留
     跳转（与 /gear/、/subs/、/apps/ 等的做法一致）。
     2026-11-08 用户「新增一个 Game 类目，将 /services/ 中的游戏
     移过去」：那十七款回到 docs/game/（见下面的 game 页），这一页
     只剩外充 2 款、礼品卡 6 款与 /cdkeys/ 的十一张询价卡 —— 询价卡
     是卡密/钱包码，不是游戏，跟着本页留下。
     同日用户「新增一个 Gift Cards 类目，同样将 /services/ 中的礼品卡
     移过去」：礼品卡 6 款也搬去 docs/gift-cards/（再下面一页），
     本页只剩外充 2 款 + 询价卡 11 张。
     同日用户又「新增 cdkeys 类目，将 /services/ 中符合 cdkeys 的商品
     移过去」：那十一张询价卡正是本站 2026-11-05 那版 /cdkeys/ 上的
     商品，整组搬去 docs/cdkeys/，本页只剩外充 2 款。
     同日用户「将 services 类目改为 Top-Up」：目录 docs/services/ →
     docs/top-up/、地址 /services/ → /top-up/，nav 标签、页面标题、
     description 与列表 aria-label 跟着改；旧地址直接 404，不留跳转
     （本站退役地址的做法，与 /gear/、/subs/、/apps/ 相同）。卡片、id、
     图片与价格一个字没动。
     2026-11-03 删掉的六款（ZZZ、Wuthering Waves、Marvel Rivals、
     NIKKE、Free Fire、Whiteout Survival）仍记在生成器的 DROP 里。
     生成脚本：C:\1Work\_tmp_ocr\gen_digital_sumei.py（重跑覆盖本页）。
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
    <div class="ab-list ab-list--pricing" aria-label="Top-Up catalogue">

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

    </div>
  </section>

</div>
