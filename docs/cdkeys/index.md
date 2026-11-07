---
title: CDKeys
description: AceBase CDKeys — game codes, wallet codes, licences and memberships, 11 cards, tiers from $0.91.
hide:
  - title
  - toc
---

<!-- CDKey 目录。十一张卡就是 2026-11-06 并页时从 /cdkeys/ 搬进
     /services/ 的那一组（那页 2026-11-05 由 /apps/ 改名而来），
     id、顺序、图片都与那时相同，图仍在 /assets/gear/ 下 ——
     资产目录是文件名，不是类目。

     2026-11-08 用户「新增 cdkeys 类目，将 /services/ 中符合 cdkeys 的
     商品移过去」：这十一张单独成页 docs/cdkeys/，卡片 markup 与在
     /services/ 时逐字相同（生成器的 sourcing_card()）。外充 2 款留在
     那一页（充进账号，不是给一串码；同日用户「将 services 类目改为
     Top-Up」，那页现在是 /top-up/）。

     同日用户「/cdkeys/ 的商品从 …/category/cdkeys 获取价格」：来源
     分类页上的八款改为标价卡（与 /game/、/gift-cards/ 同一个
     card()：品牌条、档数角标、标题末尾的价格、Spec 下拉、ORDER
     NOW），档位名与美元价原样取自来源 —— 页面出的是美元，价格不做
     汇率换算；同名档位带括号地区，如「1000 V-Bucks (Austria)」
     「3 Month Subscription (EU)」。数据由 _tmp_ocr/cdk_tl_prices.py
     抓成 cdkeys_prices.json，改价重跑它、再重跑生成器即可。来源
     分类页没有的三张（Windows 11 Pro、Costco、Microsoft 365）仍是
     band 卡 + Request Sourcing，价钱在在线客服里确认。
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
    <div class="ab-list ab-list--pricing" aria-label="CDKeys catalogue">

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="fortnite-card" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">28 tiers</span>
          <img src="/assets/digital/fortnite-card.png" alt="Fortnite V-Bucks Card wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Fortnite V-Bucks Card<span class="ab-card__price" data-digital-price>$9.99</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Fortnite V-Bucks Card">
            <option data-name="Fortnite V-Bucks Card — 1000 V-Bucks (Austria)" data-price="9.99">1000 V-Bucks (Austria) &mdash; $9.99</option>
            <option data-name="Fortnite V-Bucks Card — 1000 V-Bucks (Belgium)" data-price="9.99">1000 V-Bucks (Belgium) &mdash; $9.99</option>
            <option data-name="Fortnite V-Bucks Card — 1000 V-Bucks (France)" data-price="9.99">1000 V-Bucks (France) &mdash; $9.99</option>
            <option data-name="Fortnite V-Bucks Card — 1000 V-Bucks (Ireland)" data-price="9.99">1000 V-Bucks (Ireland) &mdash; $9.99</option>
            <option data-name="Fortnite V-Bucks Card — 1000 V-Bucks (Italy)" data-price="9.99">1000 V-Bucks (Italy) &mdash; $9.99</option>
            <option data-name="Fortnite V-Bucks Card — 1000 V-Bucks (Netherlands)" data-price="9.99">1000 V-Bucks (Netherlands) &mdash; $9.99</option>
            <option data-name="Fortnite V-Bucks Card — 1000 V-Bucks (Spain)" data-price="9.99">1000 V-Bucks (Spain) &mdash; $9.99</option>
            <option data-name="Fortnite V-Bucks Card — 2800 V-Bucks (Austria)" data-price="24.99">2800 V-Bucks (Austria) &mdash; $24.99</option>
            <option data-name="Fortnite V-Bucks Card — 2800 V-Bucks (Belgium)" data-price="24.99">2800 V-Bucks (Belgium) &mdash; $24.99</option>
            <option data-name="Fortnite V-Bucks Card — 2800 V-Bucks (France)" data-price="24.99">2800 V-Bucks (France) &mdash; $24.99</option>
            <option data-name="Fortnite V-Bucks Card — 2800 V-Bucks (Spain)" data-price="24.99">2800 V-Bucks (Spain) &mdash; $24.99</option>
            <option data-name="Fortnite V-Bucks Card — 2800 V-Bucks (Ireland)" data-price="29.99">2800 V-Bucks (Ireland) &mdash; $29.99</option>
            <option data-name="Fortnite V-Bucks Card — 2800 V-Bucks (Italy)" data-price="29.99">2800 V-Bucks (Italy) &mdash; $29.99</option>
            <option data-name="Fortnite V-Bucks Card — 2800 V-Bucks (Netherlands)" data-price="29.99">2800 V-Bucks (Netherlands) &mdash; $29.99</option>
            <option data-name="Fortnite V-Bucks Card — 5000 V-Bucks (Austria)" data-price="39.99">5000 V-Bucks (Austria) &mdash; $39.99</option>
            <option data-name="Fortnite V-Bucks Card — 5000 V-Bucks (Belgium)" data-price="39.99">5000 V-Bucks (Belgium) &mdash; $39.99</option>
            <option data-name="Fortnite V-Bucks Card — 5000 V-Bucks (Ireland)" data-price="39.99">5000 V-Bucks (Ireland) &mdash; $39.99</option>
            <option data-name="Fortnite V-Bucks Card — 5000 V-Bucks (Italy)" data-price="39.99">5000 V-Bucks (Italy) &mdash; $39.99</option>
            <option data-name="Fortnite V-Bucks Card — 5000 V-Bucks (Netherlands)" data-price="39.99">5000 V-Bucks (Netherlands) &mdash; $39.99</option>
            <option data-name="Fortnite V-Bucks Card — 5000 V-Bucks (Spain)" data-price="39.99">5000 V-Bucks (Spain) &mdash; $39.99</option>
            <option data-name="Fortnite V-Bucks Card — 5000 V-Bucks (France)" data-price="44.99">5000 V-Bucks (France) &mdash; $44.99</option>
            <option data-name="Fortnite V-Bucks Card — 13500 V-Bucks (Austria)" data-price="99.99">13500 V-Bucks (Austria) &mdash; $99.99</option>
            <option data-name="Fortnite V-Bucks Card — 13500 V-Bucks (Belgium)" data-price="99.99">13500 V-Bucks (Belgium) &mdash; $99.99</option>
            <option data-name="Fortnite V-Bucks Card — 13500 V-Bucks (France)" data-price="99.99">13500 V-Bucks (France) &mdash; $99.99</option>
            <option data-name="Fortnite V-Bucks Card — 13500 V-Bucks (Ireland)" data-price="99.99">13500 V-Bucks (Ireland) &mdash; $99.99</option>
            <option data-name="Fortnite V-Bucks Card — 13500 V-Bucks (Italy)" data-price="99.99">13500 V-Bucks (Italy) &mdash; $99.99</option>
            <option data-name="Fortnite V-Bucks Card — 13500 V-Bucks (Netherlands)" data-price="99.99">13500 V-Bucks (Netherlands) &mdash; $99.99</option>
            <option data-name="Fortnite V-Bucks Card — 13500 V-Bucks (Spain)" data-price="99.99">13500 V-Bucks (Spain) &mdash; $99.99</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Fortnite V-Bucks Card — 1000 V-Bucks (Austria)" data-name="Fortnite V-Bucks Card — 1000 V-Bucks (Austria)" data-price="9.99">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="apex-legends" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">5 tiers</span>
          <img src="/assets/digital/apex-legends.png" alt="Apex Legends Coins wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Apex Legends Coins<span class="ab-card__price" data-digital-price>$11.12</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Apex Legends Coins">
            <option data-name="Apex Legends Coins — 1000 Coins" data-price="11.12">1000 Coins &mdash; $11.12</option>
            <option data-name="Apex Legends Coins — 2150 Coins" data-price="22.43">2150 Coins &mdash; $22.43</option>
            <option data-name="Apex Legends Coins — 4350 Coins" data-price="37.27">4350 Coins &mdash; $37.27</option>
            <option data-name="Apex Legends Coins — 6700 Coins" data-price="55.29">6700 Coins &mdash; $55.29</option>
            <option data-name="Apex Legends Coins — 10500 Coins" data-price="112.68">10500 Coins &mdash; $112.68</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Apex Legends Coins — 1000 Coins" data-name="Apex Legends Coins — 1000 Coins" data-price="11.12">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="playstation" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">11 tiers</span>
          <img src="/assets/digital/playstation.png" alt="PlayStation Network Card wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">PlayStation Network Card<span class="ab-card__price" data-digital-price>$1.18</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for PlayStation Network Card">
            <option data-name="PlayStation Network Card — 1 USD" data-price="1.18">1 USD &mdash; $1.18</option>
            <option data-name="PlayStation Network Card — 2 USD" data-price="2.33">2 USD &mdash; $2.33</option>
            <option data-name="PlayStation Network Card — 3 USD" data-price="3.31">3 USD &mdash; $3.31</option>
            <option data-name="PlayStation Network Card — 4 USD" data-price="4.40">4 USD &mdash; $4.40</option>
            <option data-name="PlayStation Network Card — 10 USD" data-price="10.48">10 USD &mdash; $10.48</option>
            <option data-name="PlayStation Network Card — 25 USD" data-price="25.13">25 USD &mdash; $25.13</option>
            <option data-name="PlayStation Network Card — 50 USD" data-price="50.25">50 USD &mdash; $50.25</option>
            <option data-name="PlayStation Network Card — 75 USD" data-price="75.72">75 USD &mdash; $75.72</option>
            <option data-name="PlayStation Network Card — 100 USD" data-price="101.30">100 USD &mdash; $101.30</option>
            <option data-name="PlayStation Network Card — 150 USD" data-price="151.43">150 USD &mdash; $151.43</option>
            <option data-name="PlayStation Network Card — 200 USD" data-price="202.59">200 USD &mdash; $202.59</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — PlayStation Network Card — 1 USD" data-name="PlayStation Network Card — 1 USD" data-price="1.18">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="pubg-gcoins" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">6 tiers</span>
          <img src="/assets/digital/pubg-gcoins.png" alt="PUBG G-COIN CDK wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">PUBG G-COIN CDK<span class="ab-card__price" data-digital-price>$0.91</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for PUBG G-COIN CDK">
            <option data-name="PUBG G-COIN CDK — 100 coin" data-price="0.91">100 coin &mdash; $0.91</option>
            <option data-name="PUBG G-COIN CDK — 510 coin" data-price="4.56">510 coin &mdash; $4.56</option>
            <option data-name="PUBG G-COIN CDK — 1050 coin" data-price="8.93">1050 coin &mdash; $8.93</option>
            <option data-name="PUBG G-COIN CDK — 2700 coin" data-price="22.82">2700 coin &mdash; $22.82</option>
            <option data-name="PUBG G-COIN CDK — 5500 coin" data-price="44.65">5500 coin &mdash; $44.65</option>
            <option data-name="PUBG G-COIN CDK — 11200 coin" data-price="88.60">11200 coin &mdash; $88.60</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — PUBG G-COIN CDK — 100 coin" data-name="PUBG G-COIN CDK — 100 coin" data-price="0.91">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="ns-membership" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">10 tiers</span>
          <img src="/assets/digital/ns-membership.png" alt="Nintendo Switch Online Membership wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Nintendo Switch Online Membership<span class="ab-card__price" data-digital-price>$3.82</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Nintendo Switch Online Membership">
            <option data-name="Nintendo Switch Online Membership — 1 Month Subscription (HK)" data-price="3.82">1 Month Subscription (HK) &mdash; $3.82</option>
            <option data-name="Nintendo Switch Online Membership — 3 Month Subscription (US)" data-price="8.18">3 Month Subscription (US) &mdash; $8.18</option>
            <option data-name="Nintendo Switch Online Membership — 3 Month Subscription (JP)" data-price="8.24">3 Month Subscription (JP) &mdash; $8.24</option>
            <option data-name="Nintendo Switch Online Membership — 3 Month Subscription (EU)" data-price="9.49">3 Month Subscription (EU) &mdash; $9.49</option>
            <option data-name="Nintendo Switch Online Membership — 3 Month Subscription (UK)" data-price="10.44">3 Month Subscription (UK) &mdash; $10.44</option>
            <option data-name="Nintendo Switch Online Membership — 12 Month Subscription (EU)" data-price="21.06">12 Month Subscription (EU) &mdash; $21.06</option>
            <option data-name="Nintendo Switch Online Membership — 12 Month Subscription (HK)" data-price="21.07">12 Month Subscription (HK) &mdash; $21.07</option>
            <option data-name="Nintendo Switch Online Membership — 12 Month Subscription (US)" data-price="21.07">12 Month Subscription (US) &mdash; $21.07</option>
            <option data-name="Nintendo Switch Online Membership — 12 Month Subscription (JP)" data-price="22.63">12 Month Subscription (JP) &mdash; $22.63</option>
            <option data-name="Nintendo Switch Online Membership — 12 Month Subscription (UK)" data-price="26.00">12 Month Subscription (UK) &mdash; $26</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Nintendo Switch Online Membership — 1 Month Subscription (HK)" data-name="Nintendo Switch Online Membership — 1 Month Subscription (HK)" data-price="3.82">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="nintendo-eshop" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">21 tiers</span>
          <img src="/assets/digital/nintendo-eshop.png" alt="Nintendo eShop Gift Card wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Nintendo eShop Gift Card<span class="ab-card__price" data-digital-price>$9.69</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Nintendo eShop Gift Card">
            <option data-name="Nintendo eShop Gift Card — 10 USD" data-price="9.69">10 USD &mdash; $9.69</option>
            <option data-name="Nintendo eShop Gift Card — 50 BRL" data-price="9.88">50 BRL &mdash; $9.88</option>
            <option data-name="Nintendo eShop Gift Card — 100 HKD" data-price="12.99">100 HKD &mdash; $12.99</option>
            <option data-name="Nintendo eShop Gift Card — 15 EURO" data-price="16.79">15 EURO &mdash; $16.79</option>
            <option data-name="Nintendo eShop Gift Card — 20 USD" data-price="19.30">20 USD &mdash; $19.30</option>
            <option data-name="Nintendo eShop Gift Card — 100 BRL" data-price="19.90">100 BRL &mdash; $19.90</option>
            <option data-name="Nintendo eShop Gift Card — 15 GBP" data-price="20.95">15 GBP &mdash; $20.95</option>
            <option data-name="Nintendo eShop Gift Card — 25 EURO" data-price="27.87">25 EURO &mdash; $27.87</option>
            <option data-name="Nintendo eShop Gift Card — 150 BRL" data-price="28.65">150 BRL &mdash; $28.65</option>
            <option data-name="Nintendo eShop Gift Card — 35 USD" data-price="33.16">35 USD &mdash; $33.16</option>
            <option data-name="Nintendo eShop Gift Card — 25 GBP" data-price="34.91">25 GBP &mdash; $34.91</option>
            <option data-name="Nintendo eShop Gift Card — 300 HKD" data-price="39.30">300 HKD &mdash; $39.30</option>
            <option data-name="Nintendo eShop Gift Card — 50 USD" data-price="47.52">50 USD &mdash; $47.52</option>
            <option data-name="Nintendo eShop Gift Card — 250 BRL" data-price="50.18">250 BRL &mdash; $50.18</option>
            <option data-name="Nintendo eShop Gift Card — 50 EURO" data-price="55.76">50 EURO &mdash; $55.76</option>
            <option data-name="Nintendo eShop Gift Card — 300 BRL" data-price="59.11">300 BRL &mdash; $59.11</option>
            <option data-name="Nintendo eShop Gift Card — 500 HKD" data-price="64.23">500 HKD &mdash; $64.23</option>
            <option data-name="Nintendo eShop Gift Card — 50 GBP" data-price="68.67">50 GBP &mdash; $68.67</option>
            <option data-name="Nintendo eShop Gift Card — 75 GBP" data-price="101.34">75 GBP &mdash; $101.34</option>
            <option data-name="Nintendo eShop Gift Card — 100 EURO" data-price="111.72">100 EURO &mdash; $111.72</option>
            <option data-name="Nintendo eShop Gift Card — 100 GBP" data-price="134.79">100 GBP &mdash; $134.79</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Nintendo eShop Gift Card — 10 USD" data-name="Nintendo eShop Gift Card — 10 USD" data-price="9.69">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="steam-wallet" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">38 tiers</span>
          <img src="/assets/digital/steam-wallet.png" alt="Steam Wallet Code wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Steam Wallet Code<span class="ab-card__price" data-digital-price>$1.42</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for Steam Wallet Code">
            <option data-name="Steam Wallet Code — 5 RM" data-price="1.42">5 RM &mdash; $1.42</option>
            <option data-name="Steam Wallet Code — 8 RM" data-price="2.27">8 RM &mdash; $2.27</option>
            <option data-name="Steam Wallet Code — 10 RM" data-price="2.84">10 RM &mdash; $2.84</option>
            <option data-name="Steam Wallet Code — 100 TWD" data-price="3.54">100 TWD &mdash; $3.54</option>
            <option data-name="Steam Wallet Code — 16 RM" data-price="4.54">16 RM &mdash; $4.54</option>
            <option data-name="Steam Wallet Code — 150 TWD" data-price="5.28">150 TWD &mdash; $5.28</option>
            <option data-name="Steam Wallet Code — 40 HKD" data-price="5.45">40 HKD &mdash; $5.45</option>
            <option data-name="Steam Wallet Code — 20 RM" data-price="5.67">20 RM &mdash; $5.67</option>
            <option data-name="Steam Wallet Code — 5 USD" data-price="6.01">5 USD &mdash; $6.01</option>
            <option data-name="Steam Wallet Code — 24 RM" data-price="6.82">24 RM &mdash; $6.82</option>
            <option data-name="Steam Wallet Code — 50 HKD" data-price="6.87">50 HKD &mdash; $6.87</option>
            <option data-name="Steam Wallet Code — 200 TWD" data-price="7.05">200 TWD &mdash; $7.05</option>
            <option data-name="Steam Wallet Code — 300 TWD" data-price="10.46">300 TWD &mdash; $10.46</option>
            <option data-name="Steam Wallet Code — 80 HKD" data-price="11.13">80 HKD &mdash; $11.13</option>
            <option data-name="Steam Wallet Code — 10 USD" data-price="12.20">10 USD &mdash; $12.20</option>
            <option data-name="Steam Wallet Code — 48 RM" data-price="13.64">48 RM &mdash; $13.64</option>
            <option data-name="Steam Wallet Code — 100 HKD" data-price="13.68">100 HKD &mdash; $13.68</option>
            <option data-name="Steam Wallet Code — 50 RM" data-price="14.18">50 RM &mdash; $14.18</option>
            <option data-name="Steam Wallet Code — 120 HKD" data-price="17.02">120 HKD &mdash; $17.02</option>
            <option data-name="Steam Wallet Code — 500 TWD" data-price="17.57">500 TWD &mdash; $17.57</option>
            <option data-name="Steam Wallet Code — 160 HKD" data-price="22.69">160 HKD &mdash; $22.69</option>
            <option data-name="Steam Wallet Code — 80 RM" data-price="22.72">80 RM &mdash; $22.72</option>
            <option data-name="Steam Wallet Code — 650 TWD" data-price="22.74">650 TWD &mdash; $22.74</option>
            <option data-name="Steam Wallet Code — 20 USD" data-price="23.80">20 USD &mdash; $23.80</option>
            <option data-name="Steam Wallet Code — 200 HKD" data-price="27.43">200 HKD &mdash; $27.43</option>
            <option data-name="Steam Wallet Code — 800 TWD" data-price="27.81">800 TWD &mdash; $27.81</option>
            <option data-name="Steam Wallet Code — 100 RM" data-price="28.36">100 RM &mdash; $28.36</option>
            <option data-name="Steam Wallet Code — 25 USD" data-price="29.81">25 USD &mdash; $29.81</option>
            <option data-name="Steam Wallet Code — 240 HKD" data-price="33.37">240 HKD &mdash; $33.37</option>
            <option data-name="Steam Wallet Code — 1000 TWD" data-price="34.70">1000 TWD &mdash; $34.70</option>
            <option data-name="Steam Wallet Code — 30 USD" data-price="35.04">30 USD &mdash; $35.04</option>
            <option data-name="Steam Wallet Code — 300 HKD" data-price="41.15">300 HKD &mdash; $41.15</option>
            <option data-name="Steam Wallet Code — 400 HKD" data-price="54.84">400 HKD &mdash; $54.84</option>
            <option data-name="Steam Wallet Code — 200 RM" data-price="56.74">200 RM &mdash; $56.74</option>
            <option data-name="Steam Wallet Code — 50 USD" data-price="58.39">50 USD &mdash; $58.39</option>
            <option data-name="Steam Wallet Code — 500 HKD" data-price="68.54">500 HKD &mdash; $68.54</option>
            <option data-name="Steam Wallet Code — 100 USD" data-price="119.59">100 USD &mdash; $119.59</option>
            <option data-name="Steam Wallet Code — 1000 HKD" data-price="137.92">1000 HKD &mdash; $137.92</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — Steam Wallet Code — 5 RM" data-name="Steam Wallet Code — 5 RM" data-price="1.42">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--brand ab-card--plate ab-card--wordmark ab-card--picker" id="gocash-card" data-digital-card>
        <div class="ab-card__media">
          <span class="ab-card__badge">6 tiers</span>
          <img src="/assets/digital/gocash-card.png" alt="GoCash (Global) wordmark" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">GoCash (Global)<span class="ab-card__price" data-digital-price>$4.79</span></h3>
          <label class="ab-ec-pick">
            <span class="ab-ec-pick__label">Spec</span>
            <select class="ab-ec-pick__select" data-digital-pick aria-label="Choose an amount for GoCash (Global)">
            <option data-name="GoCash (Global) — 5 USD" data-price="4.79">5 USD &mdash; $4.79</option>
            <option data-name="GoCash (Global) — 10 USD" data-price="9.49">10 USD &mdash; $9.49</option>
            <option data-name="GoCash (Global) — 15 USD" data-price="14.99">15 USD &mdash; $14.99</option>
            <option data-name="GoCash (Global) — 20 USD" data-price="18.99">20 USD &mdash; $18.99</option>
            <option data-name="GoCash (Global) — 50 USD" data-price="47.99">50 USD &mdash; $47.99</option>
            <option data-name="GoCash (Global) — 100 USD" data-price="95.99">100 USD &mdash; $95.99</option>
            </select>
          </label>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="ORDER NOW — GoCash (Global) — 5 USD" data-name="GoCash (Global) — 5 USD" data-price="4.79">ORDER NOW</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--plate ab-card--band" id="windows-11-pro">
        <div class="ab-card__media">
          <img src="/assets/gear/windows-11-pro/01.jpg" alt="The Windows 11 Pro box on a near-white field under a sticker reading activation code by email" loading="lazy" decoding="async">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Microsoft Windows 11 Pro</h3>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="Request sourcing for Microsoft Windows 11 Pro" data-name="Microsoft Windows 11 Pro">Request Sourcing</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--plate ab-card--band" id="costco-gold-star-membership">
        <div class="ab-card__media">
          <img src="/assets/gear/costco-gold-star-membership/01.jpg" alt="A couple carrying pizza boxes and two drinks at a warehouse snack counter" loading="lazy" decoding="async" data-gallery="/assets/gear/costco-gold-star-membership/01.jpg|A couple carrying pizza boxes and two drinks at a warehouse snack counter,/assets/gear/costco-gold-star-membership/02.jpg|The front of a warehouse store under a border of holly leaves">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Costco 1-Year Gold Star Membership + $45 Digital Costco Shop Card</h3>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="Request sourcing for a Costco 1-Year Gold Star Membership with a $45 Digital Costco Shop Card" data-name="Costco 1-Year Gold Star Membership + $45 Digital Costco Shop Card">Request Sourcing</button></p>
        </div>
      </article>

      <article class="ab-card ab-card--plate ab-card--band" id="microsoft-365-1-year">
        <div class="ab-card__media">
          <img src="/assets/gear/microsoft-365-1-year/01.jpg" alt="The Microsoft 365 Personal box with its year-one features listed on the front" loading="lazy" decoding="async" data-gallery="/assets/gear/microsoft-365-1-year/01.jpg|The Microsoft 365 Personal box with its year-one features listed on the front,/assets/gear/microsoft-365-1-year/02.jpg|A laptop showing OneDrive folders above a line reading secure photo and file storage">
        </div>
        <div class="ab-card__copy">
          <h3 class="ab-card__title">Microsoft 365: 1-Year Subscription</h3>
          <p class="ab-card__more"><button type="button" class="ab-request" aria-label="Request sourcing for a Microsoft 365 one-year subscription" data-name="Microsoft 365: 1-Year Subscription">Request Sourcing</button></p>
        </div>
      </article>

    </div>
  </section>

</div>
