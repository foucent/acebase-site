(function () {
  "use strict";

  // Gift-card denomination dropdowns, added to the board-grid cards that
  // board-grid.js builds from the .mg-price-table--giftcards source table.
  // Loaded AFTER board-grid.js. Each product image carries
  //   data-denoms="LABEL:USD,LABEL:USD,..."
  //   data-discount="-16%"            (optional)
  // Picking a denomination updates the card price (in the header-selected
  // currency) and the "+ add to cart" button's data-name / data-price.

  function money(usd) {
    return window.AceBaseCurrency
      ? window.AceBaseCurrency.formatFromBase(usd)
      : "US$ " + (Math.round(usd * 100) / 100).toFixed(2);
  }

  function parseDenoms(img) {
    var raw = img && img.getAttribute("data-denoms");
    if (!raw) return [];
    return raw
      .split(",")
      .map(function (s) {
        var i = s.lastIndexOf(":");
        return { label: s.slice(0, i).trim(), usd: parseFloat(s.slice(i + 1)) };
      })
      .filter(function (p) {
        return !isNaN(p.usd);
      });
  }

  function renderPrice(priceEl, usd) {
    var discount = priceEl.dataset.discount || "";
    priceEl.textContent = money(usd);
    if (discount) {
      var tag = document.createElement("span");
      tag.className = "mg-gc-off";
      tag.textContent = discount;
      priceEl.appendChild(tag);
    }
  }

  function wireCard(card) {
    var img = card.querySelector(".mg-preowned-card__media img");
    var title = card.querySelector(".mg-preowned-card__title");
    var priceEl = card.querySelector(".mg-preowned-card__price");
    var btn = card.querySelector(".mg-cart-add");
    var pairs = parseDenoms(img);
    if (!title || !priceEl || pairs.length < 2) return;

    priceEl.dataset.discount = (img && img.getAttribute("data-discount")) || "";

    var wrap = document.createElement("div");
    wrap.className = "mg-preowned-card__opts";
    var label = document.createElement("label");
    label.className = "mg-preowned-card__opts-label";
    label.textContent = "面额";
    var sel = document.createElement("select");
    sel.className = "mg-preowned-card__opts-select";
    sel.setAttribute("aria-label", (title.textContent || "").trim() + " 面额");
    pairs.forEach(function (p) {
      var o = document.createElement("option");
      o.value = String(p.usd);
      o.textContent = p.label;
      sel.appendChild(o);
    });
    wrap.appendChild(label);
    wrap.appendChild(sel);
    title.insertAdjacentElement("afterend", wrap);

    function apply() {
      var usd = parseFloat(sel.value);
      if (isNaN(usd)) return;
      priceEl.dataset.usd = String(usd);
      renderPrice(priceEl, usd);
      if (btn) {
        btn.setAttribute("data-price", String(usd));
        var opt = sel.options[sel.selectedIndex];
        var full = (title.textContent || "").trim() + " · " + opt.textContent;
        btn.setAttribute("data-name", full);
        btn.setAttribute("aria-label", "Add " + full + " to cart");
      }
    }
    sel.addEventListener("change", apply);
    apply();

    // Keep the card price correct when the header currency changes.
    if (window.AceBaseCurrency && AceBaseCurrency.onChange) {
      AceBaseCurrency.onChange(function () {
        if (priceEl.dataset.usd) renderPrice(priceEl, parseFloat(priceEl.dataset.usd));
      });
    }
  }

  function init() {
    document
      .querySelectorAll(".mg-preowned-grid--giftcards .mg-preowned-card")
      .forEach(wireCard);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
