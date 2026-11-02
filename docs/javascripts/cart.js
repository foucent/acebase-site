/* AceBase's cart — ported from mygear.top's price-cart.js (2026-10-31).

   What came over: the localStorage cart, the floating button, the drawer, the
   toast, and the checkout message. What did not: the price-table and listing
   scrapers (this site has neither), the GA4 add_to_cart/begin_checkout events
   (this site has no analytics at all), and the "unique" flag that marked
   one-off pre-owned items. A catalogue card writes its own button into the markup
   and takes a quantity like any other product.

   Checkout changed hands on 2026-11-01: it was a wa.me link, and at the user's
   request (「购物车的结账方式以及咨询也从 8003 复制过来」) it is now acebase.cc's
   method — the cart is handed to the live chat as one message, a person
   confirms the total there, and nothing is charged on this site. crisp.js
   provides window.abOpenCrisp; the $crisp queue is the fallback for the moment
   before it loads.

   The storage key kept its old spelling when the site was rebranded to AceBase
   (2026-11-01), so a cart already in a preview browser survives the rename; as
   localStorage is per-origin it cannot leak into acebase.cc on port 8003. */
(function () {
  var STORAGE_KEY = "sumei-cart-v1";

  function $(sel, root) {
    return (root || document).querySelector(sel);
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
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
    } catch (e) {}
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

  function upsert(cart, name, price) {
    for (var i = 0; i < cart.length; i++) {
      if (cart[i].name === name) {
        cart[i].qty += 1;
        return { cart: cart, status: "updated" };
      }
    }
    cart.push({ name: name, price: price, qty: 1 });
    return { cart: cart, status: "added" };
  }

  function setQty(cart, name, qty) {
    qty = Math.max(0, parseInt(qty, 10) || 0);
    return cart
      .map(function (item) {
        return item.name === name
          ? { name: item.name, price: item.price, qty: qty }
          : item;
      })
      .filter(function (item) {
        return item.qty > 0;
      });
  }

  // The whole cart in one message, on the model of acebase's board cart: the
  // person on the other side gets every line and the subtotal without asking
  // four questions back, and the total is theirs to confirm.
  function buildChatMsg(cart) {
    var lines = ["Hello, I'd like a quote for:", ""];
    cart.forEach(function (item, i) {
      lines.push(
        i + 1 + ". " + item.name + " × " + item.qty + " — " + money(item.price) + " each"
      );
    });
    lines.push("");
    lines.push("Subtotal " + money(cartTotal(cart)) + ".");
    lines.push("Please confirm the final total and how to pay. Thanks!");
    return lines.join("\n");
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

  function ensureUi() {
    if ($("#ab-cart-root")) return $("#ab-cart-root");

    var root = document.createElement("div");
    root.id = "ab-cart-root";
    root.innerHTML =
      '<div class="ab-float-stack">' +
      '  <button type="button" class="ab-cart-fab" id="ab-cart-fab" aria-label="Open cart" title="Your cart">' +
      '    <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 18c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm10 0c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zM7.2 14h9.45c.75 0 1.4-.41 1.73-1.07L21 6H6.2l-.94-2H1v2h2l3.6 7.59-1.35 2.44C4.52 16.37 5.48 18 7 18h12v-2H7.2l1-1.8z"/></svg>' +
      '    <span class="ab-cart-fab__count" id="ab-cart-fab-count" hidden>0</span>' +
      "  </button>" +
      "</div>" +
      '<div class="ab-cart-toast" id="ab-cart-toast" hidden role="status" aria-live="polite"></div>' +
      '<div class="ab-cart-drawer" id="ab-cart-drawer" hidden>' +
      '  <div class="ab-cart-drawer__backdrop" data-cart-close="1"></div>' +
      '  <div class="ab-cart-drawer__panel" role="dialog" aria-modal="true" aria-label="Cart">' +
      '    <div class="ab-cart-drawer__head">' +
      "      <strong>Cart</strong>" +
      '      <button type="button" class="ab-cart-drawer__x" data-cart-close="1" aria-label="Close">×</button>' +
      "    </div>" +
      '    <div class="ab-cart-drawer__body" id="ab-cart-items"></div>' +
      '    <div class="ab-cart-drawer__foot">' +
      '      <div class="ab-cart-drawer__total">Subtotal <span id="ab-cart-total">$0</span></div>' +
      '      <button type="button" class="ab-cart-drawer__chat" id="ab-cart-chat" aria-disabled="true">Confirm in live chat</button>' +
      '      <button type="button" class="ab-cart-drawer__clear" id="ab-cart-clear">Clear cart</button>' +
      "    </div>" +
      "  </div>" +
      "</div>";
    document.body.appendChild(root);
    return root;
  }

  var toastTimer = null;
  function showToast(message) {
    var toast = $("#ab-cart-toast");
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
    var fabEl = $("#ab-cart-fab-count");
    var itemsEl = $("#ab-cart-items");
    var totalEl = $("#ab-cart-total");
    var chat = $("#ab-cart-chat");
    var count = cartCount(cart);

    if (!itemsEl) return;

    // The badge stays hidden at zero, so an empty cart carries no "0" over it.
    if (fabEl) {
      fabEl.textContent = String(count);
      fabEl.hidden = count === 0;
    }
    totalEl.textContent = money(cartTotal(cart));

    if (!cart.length) {
      itemsEl.innerHTML = '<p class="ab-cart-empty">Cart is empty. Tap + on a product to add it.</p>';
      chat.setAttribute("aria-disabled", "true");
      chat.classList.add("is-disabled");
      return;
    }

    itemsEl.innerHTML = cart
      .map(function (item) {
        return (
          '<div class="ab-cart-line" data-name="' +
          item.name.replace(/"/g, "&quot;") +
          '">' +
          '<div class="ab-cart-line__meta">' +
          '<div class="ab-cart-line__name">' + item.name + "</div>" +
          '<div class="ab-cart-line__price">' + money(item.price) + " each</div>" +
          "</div>" +
          '<div class="ab-cart-line__qty">' +
          '<button type="button" class="ab-cart-qty" data-delta="-1" aria-label="Decrease">−</button>' +
          "<span>" + item.qty + "</span>" +
          '<button type="button" class="ab-cart-qty" data-delta="1" aria-label="Increase">+</button>' +
          "</div>" +
          '<button type="button" class="ab-cart-remove" aria-label="Remove">×</button>' +
          "</div>"
        );
      })
      .join("");
    chat.removeAttribute("aria-disabled");
    chat.classList.remove("is-disabled");
  }

  function openDrawer(open) {
    var drawer = $("#ab-cart-drawer");
    if (!drawer) return;
    drawer.hidden = !open;
    document.body.classList.toggle("ab-cart-open", !!open);
  }

  function flashAdd(btn) {
    btn.classList.add("ab-cart-add--done");
    setTimeout(function () {
      btn.classList.remove("ab-cart-add--done");
    }, 650);
  }

  function init() {
    // Every page, not just the ones selling something: the cart lives in
    // localStorage, so a reader who added a piece on /style/ can open it again
    // from a guide two pages away.
    ensureUi();

    var cart = loadCart();
    saveCart(cart);
    render(cart);

    document.addEventListener("click", function (e) {
      var add = e.target.closest(".ab-cart-add");
      if (add) {
        var name = add.getAttribute("data-name");
        var price = parseFloat(add.getAttribute("data-price"));
        var result = upsert(cart, name, price);
        cart = result.cart;
        saveCart(cart);
        render(cart);
        flashAdd(add);
        showToast(
          (result.status === "updated" ? "Updated: " : "Added to cart: ") + name
        );
        return;
      }

      if (e.target.closest("#ab-cart-fab")) {
        openDrawer(true);
        return;
      }

      if (e.target.closest("[data-cart-close]")) {
        openDrawer(false);
        return;
      }

      if (e.target.closest("#ab-cart-clear")) {
        cart = [];
        saveCart(cart);
        render(cart);
        return;
      }

      // The checkout: the drawer steps out of the way and the cart arrives in
      // the chat as one message, as on acebase.
      if (e.target.closest("#ab-cart-chat")) {
        if (!cart.length) return;
        openDrawer(false);
        openChat(buildChatMsg(cart));
        return;
      }

      var line = e.target.closest(".ab-cart-line");
      if (!line) return;
      var lineName = line.getAttribute("data-name");
      var qtyBtn = e.target.closest(".ab-cart-qty");
      if (qtyBtn) {
        var delta = parseInt(qtyBtn.getAttribute("data-delta"), 10) || 0;
        var current = cart.filter(function (x) {
          return x.name === lineName;
        })[0];
        cart = setQty(cart, lineName, current ? current.qty + delta : 0);
        saveCart(cart);
        render(cart);
        return;
      }
      if (e.target.closest(".ab-cart-remove")) {
        cart = setQty(cart, lineName, 0);
        saveCart(cart);
        render(cart);
      }
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") openDrawer(false);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
