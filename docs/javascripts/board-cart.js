(function () {
  "use strict";

  // AceBase mousepads cart.
  // Adapted from mygear-wiki price-cart.js: adds a "+" button to every row of a
  // .mg-price-table, a floating cart Fab + drawer, and checks out via Crisp
  // (window.abOpenCrisp) instead of WhatsApp.

  var STORAGE_KEY = "acebase-mousepads-cart-v1";
  var IS_MOUSEPADS = /\/mousepads\//.test(window.location.pathname);

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
    return "$" + (Math.round(n * 100) / 100).toFixed(n % 1 ? 2 : 0);
  }

  function loadCart() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      var data = raw ? JSON.parse(raw) : [];
      return Array.isArray(data) ? data : [];
    } catch (e) {
      return [];
    }
  }

  function saveCart(cart) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
  }

  function cartCount(cart) {
    return cart.reduce(function (sum, item) {
      return sum + (item.qty || 0);
    }, 0);
  }

  function cartTotal(cart) {
    return cart.reduce(function (sum, item) {
      return sum + (item.price || 0) * (item.qty || 0);
    }, 0);
  }

  function upsert(cart, name, price, image) {
    for (var i = 0; i < cart.length; i++) {
      if (cart[i].name === name) {
        cart[i].qty += 1;
        return { cart: cart, status: "updated" };
      }
    }
    cart.push({ name: name, price: price, qty: 1, image: image || "" });
    return { cart: cart, status: "added" };
  }

  function setQty(cart, name, qty) {
    qty = Math.max(0, parseInt(qty, 10) || 0);
    return cart
      .map(function (item) {
        if (item.name !== name) return item;
        return { name: item.name, price: item.price, qty: qty, image: item.image || "" };
      })
      .filter(function (item) {
        return item.qty > 0;
      });
  }

  function buildCrispMsg(cart) {
    var lines = ["你好，我想咨询以下鼠标垫：", ""];
    cart.forEach(function (item, i) {
      lines.push(
        (i + 1) + ". " + item.name + " × " + item.qty + " — US$" + money(item.price) + " /件"
      );
    });
    lines.push("");
    lines.push("请确认最新报价与库存，谢谢！");
    return lines.join("\n");
  }

  function openCrisp(cart) {
    var msg = buildCrispMsg(cart);
    if (typeof window.abOpenCrisp === "function") {
      window.abOpenCrisp(msg);
    } else if (window.$crisp) {
      window.$crisp.push(["set", "message:text", msg]);
      window.$crisp.push(["do", "chat:open"]);
    }
  }

  // ---- Snipcart instant checkout (v3) ----
  function isSnipcartConfigured() {
    var key = window.AB_SNIPCART_KEY || "";
    return !!key && key.indexOf("REPLACE_WITH_YOUR_SNIPCART") < 0;
  }

  function slugify(s) {
    return String(s || "")
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "")
      .slice(0, 48);
  }

  function loadSnipcart(cb) {
    if (window.Snipcart && window.Snipcart.api) {
      cb();
      return;
    }
    if (!isSnipcartConfigured()) {
      showToast("在线支付尚未配置，请通过在线客服确认");
      return;
    }
    window.SnipcartSettings = {
      publicApiKey: window.AB_SNIPCART_KEY,
      version: "3.0",
      currency: "usd",
      loadStrategy: "on-user-interaction",
      modalStyle: "side",
      timeoutDuration: 2000
    };
    // Snipcart v3 requires a #snipcart element carrying data-api-key.
    if (!document.getElementById("snipcart")) {
      var host = document.createElement("div");
      host.id = "snipcart";
      host.setAttribute("data-api-key", window.AB_SNIPCART_KEY);
      host.hidden = true;
      document.body.appendChild(host);
    }
    if (!document.getElementById("snipcart-script")) {
      var s = document.createElement("script");
      s.id = "snipcart-script";
      s.async = true;
      s.src = "https://cdn.snipcart.com/themes/v3.0/default/snipcart.js";
      document.head.appendChild(s);
    }
    var done = false;
    function go() {
      if (done) return;
      done = true;
      if (window.Snipcart && window.Snipcart.api) cb();
      else showToast("在线支付加载失败，请通过在线客服确认");
    }
    document.addEventListener("snipcart.ready", go);
    var tries = 0;
    var timer = setInterval(function () {
      tries += 1;
      if (window.Snipcart && window.Snipcart.api) go();
      else if (tries > 60) {
        clearInterval(timer);
        go();
      }
    }, 300);
  }

  function checkoutWithSnipcart(cart) {
    loadSnipcart(function () {
      // Snipcart v3 `items.add` accepts a single item object (or one at a time).
      // Passing an array is serialized as {"0": {...}} and fails validation.
      var queue = cart.map(function (it) {
        var item = {
          id: "mp-" + (it.id || slugify(it.name) || "item"),
          name: it.name,
          price: it.price,
          url: window.location.href,
          quantity: it.qty || 1
        };
        if (it.image) item.image = it.image;
        return item;
      });
      var index = 0;
      function addNext() {
        if (index >= queue.length) {
          if (
            Snipcart.api.theme &&
            typeof Snipcart.api.theme.cart.open === "function"
          ) {
            Snipcart.api.theme.cart.open();
          }
          window.location.hash = "/checkout";
          return;
        }
        Snipcart.api.cart.items
          .add(queue[index])
          .then(function () {
            index += 1;
            addNext();
          })
          .catch(function (err) {
            console.error("[AceBase] Snipcart add failed", err);
            showToast("加入支付失败，请通过在线客服确认");
          });
      }
      addNext();
    });
  }

  function enhanceTables() {
    $all(".mg-price-table table").forEach(function (table) {
      if (table.dataset.mgCartReady === "1") return;
      table.dataset.mgCartReady = "1";

      var headRow = table.querySelector("thead tr");
      if (headRow && !headRow.querySelector(".mg-cart-col")) {
        var th = document.createElement("th");
        th.className = "mg-cart-col";
        th.textContent = "";
        headRow.appendChild(th);
      }

      $all("tbody tr", table).forEach(function (tr) {
        if (tr.querySelector(".mg-cart-add")) return;
        var cells = tr.querySelectorAll("td");
        if (cells.length < 3) return;
        var name = (cells[1].textContent || "").trim();
        var priceCell = cells[2];
        var price = parsePrice(priceCell.textContent);
        if (!name || !(price >= 0)) return;

        var td = document.createElement("td");
        td.className = "mg-cart-col";
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "mg-cart-add";
        btn.setAttribute("aria-label", "Add " + name + " to cart");
        btn.setAttribute("data-name", name);
        btn.setAttribute("data-price", String(price));
        var rowImg = cells[0].querySelector("img");
        if (rowImg) {
          btn.setAttribute("data-image", rowImg.currentSrc || rowImg.src || "");
        }
        btn.innerHTML = "<span aria-hidden='true'>+</span>";
        td.appendChild(btn);
        tr.appendChild(td);
      });
    });
  }

  function ensureUi() {
    if ($("#mg-cart-root")) return;

    var root = document.createElement("div");
    root.id = "mg-cart-root";
    root.innerHTML =
      '<div class="mg-float-stack">' +
      '<button type="button" class="mg-cart-fab" id="mg-cart-fab" aria-label="Open cart" hidden>' +
      '  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 18c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm10 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zM7.2 14h9.45c.75 0 1.4-.41 1.73-1.07L21 6H6.2l-.94-2H1v2h2l3.6 7.59-1.35 2.44C4.52 16.37 5.48 18 7 18h12v-2H7.2l1-1.8z"/></svg>' +
      '  <span class="mg-cart-fab__count" id="mg-cart-count">0</span>' +
      "</button>" +
      "</div>" +
      '<div class="mg-cart-toast" id="mg-cart-toast" hidden role="status" aria-live="polite"></div>' +
      '<div class="mg-cart-drawer" id="mg-cart-drawer" hidden>' +
      '  <div class="mg-cart-drawer__backdrop" data-cart-close="1"></div>' +
      '  <div class="mg-cart-drawer__panel" role="dialog" aria-modal="true" aria-label="Cart">' +
      '    <div class="mg-cart-drawer__head">' +
      "      <strong>购物车</strong>" +
      '      <button type="button" class="mg-cart-drawer__x" data-cart-close="1" aria-label="Close">×</button>' +
      "    </div>" +
      '    <div class="mg-cart-drawer__body" id="mg-cart-items"></div>' +
      '    <div class="mg-cart-drawer__foot">' +
      '      <div class="mg-cart-drawer__total">小计 <span id="mg-cart-total">$0</span></div>' +
      '      <button type="button" class="mg-cart-drawer__wa" id="mg-cart-wa">通过在线客服确认</button>' +
      (IS_MOUSEPADS
        ? '      <button type="button" class="mg-cart-drawer__snipcart" id="mg-cart-snipcart">立即结帐</button>' +
          '      <p class="mg-cart-drawer__snipcart-hint">在线支付由 Snipcart 安全处理，支持信用卡 / 多种支付方式</p>'
        : "") +
      '      <button type="button" class="mg-cart-drawer__clear" id="mg-cart-clear">清空购物车</button>' +
      "    </div>" +
      "  </div>" +
      "</div>";
    document.body.appendChild(root);
  }

  var toastTimer = null;
  function showToast(message) {
    var toast = $("#mg-cart-toast");
    if (!toast) return;
    toast.textContent = message;
    toast.hidden = false;
    toast.classList.add("is-visible");
    if (toastTimer) clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toast.classList.remove("is-visible");
      toastTimer = setTimeout(function () {
        toast.hidden = true;
      }, 220);
    }, 1800);
  }

  function render(cart) {
    var fab = $("#mg-cart-fab");
    var countEl = $("#mg-cart-count");
    var itemsEl = $("#mg-cart-items");
    var totalEl = $("#mg-cart-total");
    var wa = $("#mg-cart-wa");
    var snip = $("#mg-cart-snipcart");
    var count = cartCount(cart);

    if (!fab || !itemsEl) return;

    fab.hidden = count === 0;
    countEl.textContent = String(count);
    totalEl.textContent = "$" + money(cartTotal(cart));

    if (!cart.length) {
      itemsEl.innerHTML = '<p class="mg-cart-empty">购物车是空的。点击商品右侧 + 号加入。</p>';
      wa.classList.add("is-disabled");
      wa.setAttribute("aria-disabled", "true");
      if (snip) {
        snip.classList.add("is-disabled");
        snip.setAttribute("aria-disabled", "true");
      }
    } else {
      itemsEl.innerHTML = cart
        .map(function (item) {
          return (
            '<div class="mg-cart-line" data-name="' +
            item.name.replace(/"/g, "&quot;") +
            '">' +
            '<div class="mg-cart-line__meta">' +
            '<div class="mg-cart-line__name">' +
            item.name +
            "</div>" +
            '<div class="mg-cart-line__price">US$' +
            money(item.price) +
            " each</div>" +
            "</div>" +
            '<div class="mg-cart-line__qty">' +
            '<button type="button" class="mg-cart-qty" data-delta="-1" aria-label="Decrease">−</button>' +
            "<span>" +
            item.qty +
            "</span>" +
            '<button type="button" class="mg-cart-qty" data-delta="1" aria-label="Increase">+</button>' +
            "</div>" +
            '<button type="button" class="mg-cart-remove" aria-label="Remove">×</button>' +
            "</div>"
          );
        })
        .join("");
      wa.classList.remove("is-disabled");
      wa.removeAttribute("aria-disabled");
      if (snip) {
        snip.classList.remove("is-disabled");
        snip.removeAttribute("aria-disabled");
      }
    }
  }

  function openDrawer(open) {
    var drawer = $("#mg-cart-drawer");
    if (!drawer) return;
    drawer.hidden = !open;
    document.body.classList.toggle("mg-cart-open", !!open);
  }

  function flashAdd(btn) {
    btn.classList.add("mg-cart-add--done");
    setTimeout(function () {
      btn.classList.remove("mg-cart-add--done");
    }, 650);
  }

  function init() {
    if (!$(".mg-price-table")) return;

    enhanceTables();
    ensureUi();

    var cart = loadCart();
    render(cart);

    document.addEventListener("click", function (e) {
      var add = e.target.closest(".mg-cart-add");
      if (add) {
        var name = add.getAttribute("data-name");
        var price = parseFloat(add.getAttribute("data-price"));
        var image = add.getAttribute("data-image") || "";
        var result = upsert(cart, name, price, image);
        cart = result.cart;
        saveCart(cart);
        render(cart);
        flashAdd(add);
        showToast(result.status === "updated" ? "已更新：" + name : "已加入：" + name);
        return;
      }

      if (e.target.closest("#mg-cart-fab")) {
        openDrawer(true);
        return;
      }

      if (e.target.closest("[data-cart-close]")) {
        openDrawer(false);
        return;
      }

      if (e.target.closest("#mg-cart-clear")) {
        cart = [];
        saveCart(cart);
        render(cart);
        return;
      }

      if (e.target.closest("#mg-cart-wa")) {
        if (!cart.length) return;
        openDrawer(false);
        openCrisp(cart);
        return;
      }

      if (e.target.closest("#mg-cart-snipcart")) {
        if (!cart.length) return;
        openDrawer(false);
        checkoutWithSnipcart(cart);
        return;
      }

      var line = e.target.closest(".mg-cart-line");
      if (!line) return;
      var lineName = line.getAttribute("data-name");
      var qtyBtn = e.target.closest(".mg-cart-qty");
      if (qtyBtn) {
        var delta = parseInt(qtyBtn.getAttribute("data-delta"), 10) || 0;
        var current = cart.find(function (x) {
          return x.name === lineName;
        });
        var next = current ? current.qty + delta : 0;
        cart = setQty(cart, lineName, next);
        saveCart(cart);
        render(cart);
        return;
      }
      if (e.target.closest(".mg-cart-remove")) {
        cart = setQty(cart, lineName, 0);
        saveCart(cart);
        render(cart);
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
