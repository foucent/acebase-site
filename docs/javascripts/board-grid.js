(function () {
  "use strict";

  // AceBase mousepads: convert the .mg-price-table source table into a
  // card grid (adapted from mygear-wiki preowned-grid.js buildShopGrid).
  // Each card: media image (zoom-in), stock badge, title, price, add-to-cart.

  function $(sel, root) {
    return (root || document).querySelector(sel);
  }

  function $all(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

  function parsePrice(text) {
    var m = String(text || "").replace(/,/g, "").match(/([0-9]+(?:\.[0-9]+)?)/);
    return m ? parseFloat(m[1]) : NaN;
  }

  function money(n) {
    return window.AceBaseCurrency
      ? window.AceBaseCurrency.formatFromBase(n)
      : "$" + (Math.round(n * 100) / 100).toFixed(n % 1 ? 2 : 0);
  }

  function buildShopGrid() {
    // Process every .mg-price-table (gift cards + cdkeys sections share the page).
    $all(".mg-price-table").forEach(function (wrap) {
      if (wrap.dataset.mgGridReady === "1") return;
      var table = wrap.querySelector("table");
      if (!table) return;
      wrap.dataset.mgGridReady = "1";

      var isEn = (document.documentElement.lang || "").toLowerCase().indexOf("en") === 0;
    // Gift cards: stock badge + a --giftcards grid so gift-cards.js can add
    // the denomination dropdown to each card (mirrors mygear rubbers).
    var isGift = wrap.classList.contains("mg-price-table--giftcards");
    var addLabel = isEn ? "Add to cart" : "加入购物车";
    var badgeLabel = isGift
      ? isEn ? "In stock" : "在售"
      : isEn ? "Proxy" : "代购";
    var badgeCls = isGift
      ? "mg-preowned-card__badge--stock"
      : "mg-preowned-card__badge--proxy";
    var cardCls = isGift
      ? "mg-preowned-card mg-preowned-card--stock"
      : "mg-preowned-card mg-preowned-card--proxy";

    var grid = document.createElement("div");
    grid.className =
      "mg-preowned-grid mg-preowned-grid--shop" +
      (isGift ? " mg-preowned-grid--giftcards" : "");
    grid.setAttribute("role", "list");

    $all("tbody tr", table).forEach(function (tr) {
      var cells = tr.querySelectorAll("td");
      if (cells.length < 3) return;
      var img = cells[0].querySelector("img");
      var name = (cells[1].textContent || "").trim();
      var priceCell = cells[2];
      var price = parsePrice(priceCell.textContent);
      if (!name || !(price >= 0)) return;

      var card = document.createElement("article");
      card.className = cardCls;
      card.setAttribute("role", "listitem");
      card.dataset.name = name;
      card.dataset.price = String(price);

      var media = document.createElement("div");
      media.className = "mg-preowned-card__media";
      if (img) {
        img.alt = name;
        img.removeAttribute("loading");
        media.appendChild(img);
      }
      var badge = document.createElement("span");
      badge.className = "mg-preowned-card__badge " + badgeCls;
      badge.textContent = badgeLabel;
      media.appendChild(badge);

      var title = document.createElement("h3");
      title.className = "mg-preowned-card__title";
      title.textContent = name;

      var priceEl = document.createElement("p");
      priceEl.className = "mg-preowned-card__price";
      priceEl.textContent = money(price);

      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "mg-cart-add mg-preowned-card__cart";
      btn.setAttribute("aria-label", "Add " + name + " to cart");
      btn.setAttribute("data-name", name);
      btn.setAttribute("data-price", String(price));
      btn.innerHTML = "<span aria-hidden='true'>+</span><span>" + addLabel + "</span>";

      card.appendChild(media);
      card.appendChild(title);
      card.appendChild(priceEl);
      card.appendChild(btn);
      grid.appendChild(card);
    });

    wrap.appendChild(grid);

    // Remove the source table so the grid is the only view.
    var tableShell = table.closest(".md-typeset__table") || table.parentElement;
    if (tableShell && tableShell !== wrap && tableShell.contains(table)) {
      tableShell.remove();
    } else {
      table.remove();
    }

      var meta = $(".mg-rubbers-showing");
      if (meta) {
        meta.textContent = isEn
          ? "Showing " + grid.children.length + " results"
          : "共 " + grid.children.length + " 款";
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", buildShopGrid);
  } else {
    buildShopGrid();
  }
})();
