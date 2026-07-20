/**
 * Buy widget → multi-channel checkout (WhatsApp / Telegram / Crisp / Copy)
 * Config via data-* on .ab-buy-widget:
 *   data-whatsapp, data-telegram, data-product, data-region, data-max-qty
 */
(function () {
  var DEFAULT_WA = "8618627156285";

  function money(n) {
    return "US$ " + n.toFixed(2);
  }

  function openUrl(url) {
    var w = window.open(url, "_blank", "noopener,noreferrer");
    if (!w) window.location.href = url;
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text).then(function () {
        return true;
      }).catch(function () {
        return fallbackCopy(text);
      });
    }
    return Promise.resolve(fallbackCopy(text));
  }

  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try {
      ok = document.execCommand("copy");
    } catch (e) {
      ok = false;
    }
    document.body.removeChild(ta);
    return ok;
  }

  function flash(btn, label) {
    if (!btn) return;
    var prev = btn.getAttribute("data-label") || btn.textContent;
    btn.setAttribute("data-label", prev);
    btn.textContent = label;
    btn.classList.add("is-done");
    clearTimeout(btn._abFlash);
    btn._abFlash = setTimeout(function () {
      btn.textContent = btn.getAttribute("data-label") || prev;
      btn.classList.remove("is-done");
    }, 1800);
  }

  function openCrispChat(orderText, btn) {
    window.$crisp = window.$crisp || [];
    try {
      window.$crisp.push(["set", "message:text", [orderText]]);
      window.$crisp.push(["do", "chat:open"]);
      flash(btn, "Chat opened");
    } catch (e) {
      flash(btn, "Loading chat…");
      setTimeout(function () {
        try {
          window.$crisp.push(["set", "message:text", [orderText]]);
          window.$crisp.push(["do", "chat:open"]);
        } catch (err) {
          copyText(orderText).then(function () {
            flash(btn, "Copied — use bubble");
          });
        }
      }, 800);
    }
  }

  function initWidget(root) {
    var product = root.getAttribute("data-product") || "Product";
    var region = root.getAttribute("data-region") || "";
    var maxQty = parseInt(root.getAttribute("data-max-qty") || "50", 10);
    var wa = (root.getAttribute("data-whatsapp") || DEFAULT_WA).replace(/\D/g, "");
    var tg = (root.getAttribute("data-telegram") || "").replace(/^@/, "").trim();

    var options = root.querySelectorAll("[data-ab-option]");
    var qtyInput = root.querySelector("[data-ab-qty]");
    var qtyMinus = root.querySelector("[data-ab-qty-minus]");
    var qtyPlus = root.querySelector("[data-ab-qty-plus]");
    var priceEl = root.querySelector("[data-ab-price]");
    var channels = root.querySelector("[data-ab-channels]");
    var snipAdd = root.querySelector("[data-ab-snipcart-add]");

    var selected = root.querySelector("[data-ab-option].is-selected") || options[0];

    function getQty() {
      var q = parseInt(qtyInput.value, 10);
      if (isNaN(q) || q < 1) q = 1;
      if (q > maxQty) q = maxQty;
      qtyInput.value = String(q);
      return q;
    }

    function getUnit() {
      return parseFloat((selected && selected.getAttribute("data-price")) || "0");
    }

    function getFace() {
      return (selected && selected.getAttribute("data-face")) || "";
    }

    function getSnipId() {
      return (selected && selected.getAttribute("data-snip-id")) || "";
    }

    function buildOrder() {
      var qty = getQty();
      var unit = getUnit();
      var face = getFace();
      var total = unit * qty;
      var title = product + (region ? " (" + region + ")" : "");
      var lines = [
        "Hi, I'd like to buy:",
        "Product: " + title,
        "Denomination: " + face,
        "Qty: " + qty,
        "Unit price: " + money(unit),
        "Total: " + money(total),
      ];
      return {
        title: title,
        face: face,
        qty: qty,
        unit: unit,
        total: total,
        text: lines.join("\n"),
      };
    }

    function refresh() {
      var total = getUnit() * getQty();
      if (priceEl) priceEl.textContent = money(total);
    }

    function selectOption(el) {
      options.forEach(function (o) {
        o.classList.remove("is-selected");
        o.setAttribute("aria-pressed", "false");
      });
      el.classList.add("is-selected");
      el.setAttribute("aria-pressed", "true");
      selected = el;
      refresh();
    }

    options.forEach(function (el) {
      el.addEventListener("click", function () {
        selectOption(el);
      });
    });

    if (qtyMinus) {
      qtyMinus.addEventListener("click", function () {
        qtyInput.value = String(Math.max(1, getQty() - 1));
        refresh();
      });
    }
    if (qtyPlus) {
      qtyPlus.addEventListener("click", function () {
        qtyInput.value = String(Math.min(maxQty, getQty() + 1));
        refresh();
      });
    }
    if (qtyInput) {
      qtyInput.addEventListener("change", refresh);
      qtyInput.addEventListener("input", refresh);
    }

    if (snipAdd) {
      snipAdd.addEventListener("click", function (e) {
        e.preventDefault();
        var id = getSnipId();
        var qty = getQty();
        var catalogBtn = id
          ? root.querySelector(
              '.ab-snipcart-catalog .snipcart-add-item[data-item-id="' + id + '"]'
            )
          : null;
        if (!catalogBtn) {
          flash(snipAdd, "Item missing");
          return;
        }
        if (typeof window.LoadSnipcart === "function") {
          window.LoadSnipcart();
        }
        catalogBtn.setAttribute("data-item-url", productsValidateUrl());
        catalogBtn.setAttribute("data-item-quantity", String(qty));
        catalogBtn.click();
        flash(snipAdd, "Added ✓");
      });
    }

    if (channels) {
      channels.addEventListener("click", function (e) {
        var btn = e.target.closest("[data-ab-channel]");
        if (!btn || !channels.contains(btn)) return;
        e.preventDefault();
        var channel = btn.getAttribute("data-ab-channel");
        var order = buildOrder();

        if (channel === "whatsapp") {
          openUrl(
            "https://wa.me/" + wa + "?text=" + encodeURIComponent(order.text)
          );
          return;
        }

        if (channel === "telegram") {
          if (tg) {
            copyText(order.text).then(function () {
              flash(btn, "Copied — opening…");
              openUrl("https://t.me/" + encodeURIComponent(tg));
            });
          } else {
            openUrl(
              "https://t.me/share/url?url=" +
                encodeURIComponent(location.href.split("#")[0]) +
                "&text=" +
                encodeURIComponent(order.text)
            );
          }
          return;
        }

        if (channel === "chat") {
          openCrispChat(order.text, btn);
          return;
        }

        if (channel === "copy") {
          copyText(order.text).then(function (ok) {
            flash(btn, ok ? "Copied ✓" : "Copy failed");
          });
        }
      });
    }

    if (selected) selectOption(selected);
    else refresh();
  }

  function productsValidateUrl() {
    var u = window.__AB_SNIPCART_PRODUCTS_URL__;
    if (u && String(u).trim()) return String(u).trim();
    return location.origin + "/snipcart/products.json";
  }

  function syncSnipcartItemUrls() {
    // Snipcart's crawler runs on their servers — localhost/127.0.0.1 is unreachable.
    // Use a public products JSON URL (see mkdocs.yml snipcart_products_url).
    var url = productsValidateUrl();
    document.querySelectorAll(".snipcart-add-item[data-item-url]").forEach(function (btn) {
      btn.setAttribute("data-item-url", url);
    });
  }

  function boot() {
    syncSnipcartItemUrls();
    document.querySelectorAll(".ab-buy-widget").forEach(initWidget);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
