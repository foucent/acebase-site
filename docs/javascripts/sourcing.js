/* The Request Sourcing button — what the cart's "+ Add to cart" became.

   2026-11-02, at the user's request: 「将+Add to cart改为 Request Sourcing，
   全站都没有购物车」. The cart (localStorage lines, floating button, drawer,
   toast, "Confirm in live chat") is gone with cart.js. A button now asks the
   question for one piece instead of tallying a basket: it hands that piece to
   the live chat and a person answers with availability and the total.

   The button carries the same data-name / data-price hooks the cart used, and
   digital.js still rewrites them when a Spec dropdown changes, so the message
   names the exact option on screen. crisp.js loads before this file and owns
   window.abOpenCrisp. */
(function () {
  function money(n) {
    return "$" + (Math.round(n * 100) / 100).toFixed(n % 1 ? 2 : 0);
  }

  function buildMessage(btn) {
    var name = (btn.getAttribute("data-name") || "").trim();
    var price = parseFloat(btn.getAttribute("data-price"));
    if (!name) return "";
    var line = name + (isNaN(price) ? "" : " — " + money(price) + " each");

    /* The front page is a buying service (2026-11-11 second pass, user:
       「是的，首要也要改成 我们替你从品牌供应商或三大平台采购」): a card asks
       for a quote to buy the piece, not for a link to buy it at. Its cards sit
       inside .ab-sb. The one page left outside the shelf — /top-ups/pubg-mobile/
       — keeps the sourcing wording it has had since the cart was retired on
       2026-11-02. (It used to be said of the three catalogue pages too; they
       were emptied onto the shelf on 2026-11-11 and deleted.) */
    if (btn.closest && btn.closest(".ab-sb")) {
      /* A top-up is bought on its own channel and the channel's coupons are
         part of the answer, so its button says "Get channel coupons"
         (2026-11-11, user: 「将 top-ups的 Get link or channel 改成类似于
         获取渠道和优惠券」, then 「Get channel & coupons 改成获取渠道优惠券」). */
      if (btn.closest('[data-category="topup"]')) {
        return (
          "Hello, I'd like the channel coupons for:\n\n" +
          line +
          "\n\nPlease reply in the chat with which channel it is bought on, and any coupons that apply."
        );
      }
      return (
        "Hello, I'd like a quote to buy this for me — from the brand supplier first, otherwise Pinduoduo, JD or Taobao:\n\n" +
        line +
        "\n\nPlease reply with the price and how I get it."
      );
    }

    return (
      "Hello, I'd like to request sourcing for:\n\n" +
      line +
      "\n\nPlease confirm availability and the final total."
    );
  }

  // crisp.js is loaded first, but a page that fails to load it must still not
  // throw on the click: the $crisp queue is Crisp's own backlog.
  function openChat(msg) {
    if (typeof window.abOpenCrisp === "function") {
      window.abOpenCrisp(msg);
      return;
    }
    window.$crisp = window.$crisp || [];
    window.$crisp.push(["set", "message:text", msg]);
    window.$crisp.push(["do", "chat:open"]);
  }

  function flash(btn) {
    btn.classList.add("ab-request--sent");
    setTimeout(function () {
      btn.classList.remove("ab-request--sent");
    }, 650);
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest ? e.target.closest(".ab-request") : null;
    if (!btn) return;
    e.preventDefault();
    var msg = buildMessage(btn);
    if (!msg) return;
    openChat(msg);
    flash(btn);
  });
})();
