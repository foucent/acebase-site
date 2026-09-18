(function () {
  "use strict";

  // AceBase live-streaming top-up overview: fetch live-prices.json and fill each
  // .ab-ec-list[data-product] with that platform's tier ladder — one line per
  // tier, the same shape the GPU articles use. Values in live-prices.json are
  // USD, and USD is the only currency displayed.

  function $(sel, root) {
    return (root || document).querySelector(sel);
  }

  function $all(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function money(n) {
    return "$" + (Math.round(n * 100) / 100).toFixed(2);
  }

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  var T = {
    soon: "价格即将上线 — 请咨询在线客服获取最新报价。",
    err: "价格暂时不可用 — 请咨询在线客服获取最新报价。",
  };

  // The source lists a strike price beside the reference price on most tiers.
  // Quoting only the reference would leave the page's one discount signal
  // invisible, and printing both would double the width of every row — so the
  // saving rides as a pill on the entry tier, where it is largest and where
  // someone deciding whether to read further will actually see it.
  function offPill(entry) {
    if (!(entry.list > entry.ref)) return "";
    return (
      '<span class="ab-ec-off">省 ' +
      Math.round((1 - entry.ref / entry.list) * 100) +
      "%</span>"
    );
  }

  function renderList(wrap, product) {
    if (!product || !product.tiers || !product.tiers.length) {
      wrap.innerHTML = '<span class="ab-ec-loading">' + T.soon + "</span>";
      return;
    }
    // The generator already sorted these cheapest-first, so the entry tier is
    // the row the pill lands on. Nothing is re-sorted here.
    wrap.innerHTML = product.tiers
      .map(function (r, i) {
        return (
          '<span class="ab-ec-item">' +
          esc(r.title) +
          '<span class="ab-ec-sep">/</span>' +
          '<span class="ab-ec-price">' + money(r.ref) + "</span>" +
          (i === 0 ? offPill(r) : "") +
          ".</span>"
        );
      })
      .join("<br>");
  }

  function fail() {
    $all(".ab-ec-list[data-product]").forEach(function (wrap) {
      wrap.innerHTML = '<span class="ab-ec-loading">' + T.err + "</span>";
    });
  }

  function init() {
    var lists = $all(".ab-ec-list[data-product]");
    if (!lists.length) return;

    // The generator writes this page and the JSON in the same run, so the date
    // it stamps on the page is a cache key that cannot fall out of step with
    // the data — unlike a constant edited here by hand.
    var mag = $(".ab-mag[data-prices-ver]");
    var ver = (mag && mag.getAttribute("data-prices-ver")) || "1";

    fetch("/assets/games/live-prices.json?v=" + encodeURIComponent(ver))
      .then(function (r) {
        if (!r.ok) throw new Error("http " + r.status);
        return r.json();
      })
      .then(function (data) {
        var products = (data && data.products) || {};
        lists.forEach(function (wrap) {
          renderList(wrap, products[wrap.getAttribute("data-product")]);
        });
      })
      .catch(function (err) {
        console.warn("[AceBase] live-prices.json not loaded:", err.message);
        fail();
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
