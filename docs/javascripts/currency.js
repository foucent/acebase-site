(function () {
  "use strict";

  // Single-currency (USD) price renderer.
  // All data-price / data-was values on the site are USD.
  // Keeps the AceBaseCurrency API used by page scripts.

  function formatNumber(n) {
    return n.toLocaleString("en-US", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    });
  }

  function formatFromBase(amount) {
    var val = parseFloat(amount);
    if (isNaN(val)) return "US$ 0.00";
    return "US$ " + formatNumber(val);
  }

  function get() {
    return "USD";
  }

  function refreshMoneyElements() {
    document.querySelectorAll(".ab-money[data-ab-amount]").forEach(function (el) {
      var amount = el.getAttribute("data-ab-amount");
      el.textContent = formatFromBase(amount);
    });
  }

  function refreshSkuPrices() {
    document.querySelectorAll(".bt-sku[data-price]").forEach(function (btn) {
      var priceEl = btn.querySelector(".bt-sku__price");
      if (!priceEl) return;
      var price = btn.getAttribute("data-price");
      var was = btn.getAttribute("data-was");
      var nowHtml = formatFromBase(price);
      if (was) {
        priceEl.innerHTML =
          nowHtml +
          '<span class="bt-sku__was">' +
          formatFromBase(was) +
          "</span>";
      } else {
        priceEl.textContent = nowHtml;
      }
    });
  }

  function refreshAll() {
    refreshMoneyElements();
    refreshSkuPrices();
  }

  window.AceBaseCurrency = {
    get: get,
    formatFromBase: formatFromBase,
    refresh: refreshAll,
    SYMBOLS: { USD: "US$" },
  };

  function init() {
    refreshAll();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
