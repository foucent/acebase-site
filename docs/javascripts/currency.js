(function () {
  "use strict";

  // Multi-currency (HKD / TWD) price renderer + header switcher.
  // All data-price / data-was / data-ab-amount values on the site are USD
  // (internal base); HKD and TWD are the only display currencies.
  // Rates come from open.er-api.com (free, no key), cached 24h; a fixed
  // fallback table keeps prices rendering if the API is unreachable.

  var STORAGE_KEY = "acebase_currency";
  var RATES_KEY = "acebase_fx_rates";
  var RATES_TTL = 24 * 60 * 60 * 1000; // 24 hours

  var CURRENCIES = ["HKD", "TWD"];
  var DEFAULT_RATES = { USD: 1, HKD: 7.8, TWD: 32.5 };
  var SYMBOLS = { HKD: "HK$", TWD: "NT$" };

  var current = "HKD";
  var rates = {};
  var listeners = [];

  function loadCurrency() {
    try {
      var saved = localStorage.getItem(STORAGE_KEY);
      if (saved && CURRENCIES.indexOf(saved) >= 0) current = saved;
    } catch (e) {}
  }

  function saveCurrency(code) {
    try {
      localStorage.setItem(STORAGE_KEY, code);
    } catch (e) {}
  }

  function loadRates() {
    // Start with the fallback table so prices render synchronously (no flash).
    rates = Object.assign({}, DEFAULT_RATES);
    try {
      var raw = localStorage.getItem(RATES_KEY);
      if (raw) {
        var data = JSON.parse(raw);
        if (
          data &&
          data.ts &&
          data.rates &&
          Date.now() - data.ts < RATES_TTL
        ) {
          var complete = CURRENCIES.every(function (c) {
            return data.rates[c] > 0;
          });
          if (complete) {
            rates = data.rates;
            return; // fresh cache — no refetch
          }
        }
      }
    } catch (e) {}
    fetchRates();
  }

  function fetchRates() {
    fetch("https://open.er-api.com/v6/latest/USD")
      .then(function (r) {
        if (!r.ok) throw new Error("http " + r.status);
        return r.json();
      })
      .then(function (data) {
        var src = data && data.rates;
        if (!src) return;
        var next = { USD: 1 };
        CURRENCIES.forEach(function (c) {
          if (src[c] > 0) next[c] = src[c];
        });
        rates = next;
        try {
          localStorage.setItem(
            RATES_KEY,
            JSON.stringify({ ts: Date.now(), rates: next })
          );
        } catch (e) {}
        emit(); // re-render prices with live rates
      })
      .catch(function () {
        /* keep fallback table */
      });
  }

  function formatNumber(n) {
    return n.toLocaleString("en-US", {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2,
    });
  }

  function convertFromUsd(usd) {
    var val = parseFloat(usd);
    if (isNaN(val)) return 0;
    return val * (rates[current] || 1);
  }

  function formatFromBase(amount) {
    // Base currency is always USD on this site; amount param kept for clarity.
    var val = convertFromUsd(amount);
    return (SYMBOLS[current] || current) + " " + formatNumber(val);
  }

  function symbol(code) {
    return SYMBOLS[code] || code;
  }

  function get() {
    return current;
  }

  function emit() {
    document.dispatchEvent(
      new CustomEvent("acebase:currency-change", {
        detail: { currency: current, rates: rates },
      })
    );
    listeners.forEach(function (fn) {
      try {
        fn(current, rates);
      } catch (e) {}
    });
    updateSwitcherActive();
    refreshAll();
  }

  function set(code) {
    if (CURRENCIES.indexOf(code) < 0) return;
    current = code;
    saveCurrency(code);
    emit();
  }

  function onChange(fn) {
    listeners.push(fn);
    return function () {
      listeners = listeners.filter(function (f) {
        return f !== fn;
      });
    };
  }

  // Legacy elements: .ab-money[data-ab-amount] and .bt-sku[data-price].
  function refreshMoneyElements() {
    document.querySelectorAll(".ab-money[data-ab-amount]").forEach(function (el) {
      var amount = el.getAttribute("data-ab-amount");
      el.textContent = formatFromBase(amount);
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

  function refreshAll() {
    refreshMoneyElements();
    refreshSkuPrices();
  }

  // --- Header currency dropdown (reuses Material's .md-select styles) ---
  function mountSwitcher() {
    var header = document.querySelector(".md-header__inner");
    if (!header || document.getElementById("ab-currency-select")) return;

    var langOpt = header.querySelector(".md-header__option");

    var wrap = document.createElement("div");
    wrap.id = "ab-currency-select";
    wrap.className = "md-header__option";

    var items = CURRENCIES.map(function (c) {
      return (
        '<li class="md-select__item">' +
        '<a href="#" data-currency="' +
        c +
        '" class="md-select__link">' +
        c +
        " · " +
        symbol(c) +
        "</a></li>"
      );
    }).join("");

    wrap.innerHTML =
      '<div class="md-select">' +
      '<button type="button" class="md-header__button ab-currency-btn" aria-label="Select currency" aria-haspopup="listbox">' +
      '<span class="ab-currency-btn__sym">' +
      symbol(current) +
      "</span>" +
      "</button>" +
      '<div class="md-select__inner">' +
      '<ul class="md-select__list" role="listbox">' +
      items +
      "</ul></div></div>";

    if (langOpt && langOpt.parentNode === header) {
      // Language switcher first, currency switcher after it.
      header.insertBefore(wrap, langOpt.nextSibling);
    } else {
      header.appendChild(wrap);
    }

    wrap.addEventListener("click", function (e) {
      var link = e.target.closest("[data-currency]");
      if (!link) return;
      e.preventDefault();
      set(link.getAttribute("data-currency"));
    });
  }

  function updateSwitcherActive() {
    var wrap = document.getElementById("ab-currency-select");
    if (!wrap) return;
    var sym = wrap.querySelector(".ab-currency-btn__sym");
    if (sym) sym.textContent = symbol(current);
    wrap.querySelectorAll("[data-currency]").forEach(function (link) {
      link.classList.toggle(
        "is-active",
        link.getAttribute("data-currency") === current
      );
    });
  }

  window.AceBaseCurrency = {
    get: get,
    set: set,
    onChange: onChange,
    symbol: symbol,
    formatFromBase: formatFromBase,
    refresh: refreshAll,
    CURRENCIES: CURRENCIES,
    SYMBOLS: SYMBOLS,
  };

  function init() {
    loadCurrency();
    loadRates();
    mountSwitcher();
    refreshAll();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
