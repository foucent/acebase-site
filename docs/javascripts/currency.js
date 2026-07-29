(function () {
  "use strict";

  var STORAGE_KEY = "acebase_currency";
  var DISPLAY = ["CNY", "USD", "TWD"];
  var TO_USD = { USD: 1, CNY: 1 / 7.25, TWD: 1 / 32, SGD: 1 / 1.35 };
  var FROM_USD = { USD: 1, CNY: 7.25, TWD: 32, SGD: 1.35 };
  var SYMBOLS = { CNY: "￥", USD: "US$", TWD: "NT$" };
  var NAMES_ZH = { CNY: "人民币", USD: "美元", TWD: "台币" };
  var NAMES_EN = { CNY: "CNY", USD: "USD", TWD: "TWD" };

  function pageLang() {
    var lang = (document.documentElement.lang || "zh").toLowerCase();
    return lang.indexOf("en") === 0 ? "en" : "zh";
  }

  function currencyNames() {
    return pageLang() === "en" ? NAMES_EN : NAMES_ZH;
  }

  var current = "CNY";
  var listeners = [];

  function load() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY);
      if (saved && DISPLAY.indexOf(saved) >= 0) current = saved;
    } catch (e) {}
  }

  function save(currency) {
    try {
      localStorage.setItem(STORAGE_KEY, currency);
    } catch (e) {}
  }

  function convert(amount, from, to) {
    var n = parseFloat(amount);
    if (isNaN(n)) return 0;
    if (from === to) return n;
    var usd = n * (TO_USD[from] || 1);
    return usd * (FROM_USD[to] || 1);
  }

  function formatNumber(n) {
    return n.toLocaleString("en-US", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    });
  }

  function formatFromBase(amount, base) {
    var val = convert(amount, base, current);
    return SYMBOLS[current] + " " + formatNumber(val);
  }

  function formatParts(amount, base) {
    var val = convert(amount, base, current);
    return {
      currency: current,
      symbol: SYMBOLS[current],
      amount: formatNumber(val),
      full: SYMBOLS[current] + " " + formatNumber(val),
    };
  }

  function get() {
    return current;
  }

  function set(currency) {
    if (DISPLAY.indexOf(currency) < 0) return;
    current = currency;
    save(currency);
    document.documentElement.setAttribute("data-ab-currency", currency);
    refreshAll();
    document.dispatchEvent(
      new CustomEvent("acebase:currency-change", { detail: { currency: currency } })
    );
    listeners.forEach(function (fn) {
      fn(currency);
    });
    updateSwitcherActive();
  }

  function onChange(fn) {
    listeners.push(fn);
    return function () {
      listeners = listeners.filter(function (f) {
        return f !== fn;
      });
    };
  }

  function refreshMoneyElements() {
    document.querySelectorAll(".ab-money[data-ab-amount]").forEach(function (el) {
      var amount = el.getAttribute("data-ab-amount");
      var base = el.getAttribute("data-ab-base") || "USD";
      el.textContent = formatFromBase(amount, base);
    });
  }

  function getBaseCurrency(el) {
    if (el.getAttribute("data-currency-base")) {
      return el.getAttribute("data-currency-base");
    }
    var root = el.closest("[data-currency-base]");
    return root ? root.getAttribute("data-currency-base") : "USD";
  }

  function refreshSkuPrices() {
    document.querySelectorAll(".bt-sku[data-price]").forEach(function (btn) {
      var base = getBaseCurrency(btn);
      var priceEl = btn.querySelector(".bt-sku__price");
      if (!priceEl) return;
      var price = btn.getAttribute("data-price");
      var was = btn.getAttribute("data-was");
      var nowHtml = formatFromBase(price, base);
      if (was) {
        priceEl.innerHTML =
          nowHtml +
          '<span class="bt-sku__was">' +
          formatFromBase(was, base) +
          "</span>";
      } else {
        priceEl.textContent = nowHtml;
      }
    });
  }

  function refreshCurrencyLabels() {
    var names = currencyNames();
    document.querySelectorAll(".ab-currency-label").forEach(function (el) {
      el.textContent = "(" + names[current] + ")";
    });
  }

  function refreshAll() {
    refreshMoneyElements();
    refreshSkuPrices();
    refreshCurrencyLabels();
  }

  function mountSwitcher() {
    var header = document.querySelector(".md-header__inner");
    if (!header || document.getElementById("ab-currency-switcher")) return;

    var wrap = document.createElement("div");
    wrap.id = "ab-currency-switcher";
    wrap.className = "ab-currency-switcher";
    wrap.setAttribute("role", "group");
    wrap.setAttribute("aria-label", pageLang() === "en" ? "Currency" : "货币切换");

    DISPLAY.forEach(function (code) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "ab-currency-switcher__btn";
      btn.setAttribute("data-currency", code);
      btn.setAttribute("title", currencyNames()[code]);
      btn.textContent = code === "CNY" ? "￥" : code === "USD" ? "$" : "NT$";
      btn.addEventListener("click", function () {
        set(code);
      });
      wrap.appendChild(btn);
    });

    var search = header.querySelector(".md-header__option");
    if (search) header.insertBefore(wrap, search);
    else header.appendChild(wrap);
    updateSwitcherActive();
  }

  function updateSwitcherActive() {
    document.querySelectorAll(".ab-currency-switcher__btn").forEach(function (btn) {
      var active = btn.getAttribute("data-currency") === current;
      btn.classList.toggle("is-active", active);
      btn.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  window.AceBaseCurrency = {
    get: get,
    set: set,
    convert: convert,
    formatFromBase: formatFromBase,
    formatParts: formatParts,
    onChange: onChange,
    refresh: refreshAll,
    SYMBOLS: SYMBOLS,
    NAMES: currencyNames,
  };

  load();
  document.documentElement.setAttribute("data-ab-currency", current);

  function init() {
    mountSwitcher();
    refreshAll();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
