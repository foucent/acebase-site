/* The front page's link-to-price box and its category pills (2026-11-08, user:
   「将 http://127.0.0.1:8003/gear/ 页面模仿 https://www.superbuy.com/cn/page/
   homepage/…」, then 「这部分的意思应该是 用户输入商品链接，我为他通过异步的
   方式获取最低采购价」, then 「用户点 get price之后，需要弹出一个邮箱输入框，
   用于接收价格信息」).

   The hero box asks for a product link. Submitting one opens the live chat
   with the link already in the message (2026-11-11, user: 「这里不要通过邮件，
   而是直接打开聊天在线获取报价」 — the email dialog that stood here until then is
   gone). This site has no form backend, so the chat inbox is where a person
   picks the request up and answers with the price. The input keeps its value,
   so a typo can be fixed and sent again.

   Anything that is not a link is treated as a search of the shelf: the pills
   narrow by category, the box narrows by text, and the two stack. A shelf this
   long has seven kinds of thing to narrow by and two dozen brands, so the
   pills say Mice / Keyboards / Mousepads / Monitors / Headsets / Chairs /
   Top-ups (2026-11-08, when page one of five more review categories landed,
   and 2026-11-11, when the nineteen Top-ups products moved onto the shelf);
   before that they were brand pills. The copy never calls the box a search.

   The cards carry data-category and data-search (a lower-case string of the
   model plus its category) in index.md, so a card without data-search simply
   never matches. Only this page's markup is touched: everything below lives
   inside .ab-sb. */
(function () {
  "use strict";

  var root = document.querySelector(".ab-sb");
  if (!root) return;

  var grid = document.getElementById("gear-grid");
  var pills = document.getElementById("gear-pills");
  var form = document.getElementById("gear-search-form");
  var input = document.getElementById("gear-search");
  var empty = document.getElementById("gear-empty");
  if (!grid || !pills) return;

  var cards = Array.prototype.slice.call(grid.querySelectorAll(".ab-sb-card"));
  var category = "all";
  var query = "";

  function words(s) {
    return String(s || "")
      .toLowerCase()
      .split(/\s+/)
      .filter(Boolean);
  }

  /* A link is anything with a scheme, or a bare host with a dot in it
     ("shop.example.com/x"). A model name — "wooting 80he", "75%" — has no dot,
     so it falls through to the grid. */
  function looksLikeLink(v) {
    var s = String(v || "").trim();
    if (!s) return false;
    if (/^https?:\/\//i.test(s)) return true;
    return /^(www\.)?[a-z0-9-]+(\.[a-z0-9-]+)+([/?#]|$)/i.test(s);
  }

  function apply() {
    var terms = words(query);
    var shown = 0;

    cards.forEach(function (card) {
      var okCategory = category === "all" ||
        card.getAttribute("data-category") === category;
      var hay = card.getAttribute("data-search") || "";
      var okText = terms.every(function (t) {
        return hay.indexOf(t) !== -1;
      });
      var show = okCategory && okText;
      card.hidden = !show;
      if (show) shown += 1;
    });

    if (empty) empty.hidden = shown !== 0;
  }

  /* ---------- a link opens the live chat ---------- */

  /* The same request the shelf's cards send through sourcing.js — the link
     takes the place the card gives its name and price (2026-11-11, user:
     「输入链接的 get a quote 点击后的效果应该和下面的商品的 get a quote 的效果
     是一样的」). No note appears, for the same reason: a card click opens the
     chat and nothing else. */
  function sendToChat(link) {
    var msg =
      "Hello, I'd like a quote to buy this for me — from the brand supplier first, otherwise Pinduoduo, JD or Taobao:\n\n" +
      link +
      "\n\nPlease reply with the price and how I get it.";
    if (typeof window.abOpenCrisp === "function") {
      window.abOpenCrisp(msg);
    } else {
      /* crisp.js loads before this file, but a page that failed to load it
         must still queue the message rather than throw */
      window.$crisp = window.$crisp || [];
      window.$crisp.push(["set", "message:text", msg]);
      window.$crisp.push(["do", "chat:open"]);
    }
  }

  /* ---------- the shelf ---------- */

  pills.addEventListener("click", function (ev) {
    var pill = ev.target.closest(".ab-sb-pill");
    if (!pill) return;
    category = pill.getAttribute("data-category") || "all";
    Array.prototype.forEach.call(pills.querySelectorAll(".ab-sb-pill"), function (p) {
      var on = p === pill;
      p.classList.toggle("is-active", on);
      p.setAttribute("aria-pressed", on ? "true" : "false");
    });
    apply();
  });

  if (input) {
    input.addEventListener("input", function () {
      query = input.value;
      apply();
    });
  }

  if (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var value = input ? input.value.trim() : "";

      if (looksLikeLink(value)) {
        /* a link is not a filter: put the whole shelf back, then hand the link
           to the chat, where the quote is answered */
        query = "";
        apply();
        sendToChat(value);
        return;
      }

      query = value;
      apply();
      var disc = document.getElementById("gear");
      if (disc) disc.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  apply();
})();
