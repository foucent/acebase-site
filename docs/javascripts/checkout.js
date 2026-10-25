/*
 * Checkout sheet for game top-ups, which are delivered to a Player ID.
 *
 * Every Buy on /games/ opens this sheet (and so does the copy of those cards
 * on the homepage); gift cards, top-up codes and accounts keep the direct
 * chat handoff, because they are not credited to an in-game ID.
 *
 * Two steps, because the order a manual payment needs is two things the card
 * cannot ask for: what to top up (ID + package) and how it will be paid.
 *
 *   1. Order    — Player ID / account and package. Nothing is sent yet.
 *   2. Payment  — a generated order reference, the amount, the method
 *                 (Wise transfer for larger orders, PayPal for smaller)
 *                 and what to do next.
 *
 * The method follows the amount: below PAYPAL_UNDER PayPal is preselected,
 * because a bank transfer costs the buyer more in fees than the order;
 * above it, the manual transfer. The sheet does not advertise the number —
 * the two cards just say larger / smaller orders. Either way the money does
 * not move here — the online payment link is sent by a person in chat, and
 * the Wise account details are printed from config (or handed over in chat
 * when they are not configured).
 *
 * Sending hands the whole order to Crisp in one message — order reference,
 * game, package, ID, amount, method — so support can match a payment to an
 * order without asking four questions back. The payment itself is confirmed
 * by a person, which is the point of the flow: no card is charged anywhere on
 * this site, and a wire that has landed cannot be charged back.
 *
 * Wise details live in mkdocs.yml under extra.payment.wise and are injected
 * as window.AB_PAYMENT by overrides/main.html. Left blank, step 2 says the
 * account details come from chat instead — never invent an account number in
 * this file.
 *
 * Opting a card in takes two attributes on its Buy (data-checkout="<prices.json
 * key>" + data-checkout-name) and removing ab-crisp-open — see the generated
 * rule in _tmp_ocr/games_checkout_enable.py. A new game is the same two
 * attributes, provided it really is credited to an in-game ID.
 *
 * Kept in ES5 on purpose: mkdocs minifies JS during the build.
 */
(function () {
  "use strict";

  var TRIGGERS = "[data-checkout]";
  // Games on /games/ hand over an identifier in one of three shapes: digits
  // (PUBG, Genshin, Free Fire…), a name#tag (VALORANT, Diablo IV), or digits
  // with the server in brackets (Mobile Legends). Letters, digits and the
  // separators those three use are accepted; everything else is refused
  // before it reaches the chat.
  var ID_RE = /^[A-Za-z0-9#()_.\- ]{3,40}$/;

  function validId(v) {
    return ID_RE.test(v) && (v.match(/[A-Za-z0-9]/g) || []).length >= 4;
  }
  // No I, L, O, U: a reference is read aloud in chat and typed into a bank
  // field, and those four are the pairs people get wrong.
  var REF_ABC = "23456789ABCDEFGHJKMNPQRSTUVWXYZ";

  var T = {
    kicker: "Checkout",
    step1: "Order",
    step2: "Payment",
    playerId: "Player ID / account",
    placeholder: "e.g. 51234567890 or Name#TAG",
    uidHint:
      "Copy it exactly as the game shows it. If the game gives an ID and a " +
      "server separately, paste both — 12345678(1234).",
    pkg: "Package",
    reference: "Reference price",
    pending: "Confirmed in chat",
    note1:
      "The final price is confirmed in chat before you pay. The top-up goes to " +
      "the ID above, so double-check it — a completed top-up cannot be reversed.",
    help: "Where do I find my Player ID?",
    steps: [
      "Open the game and go to your profile — the avatar in the lobby, or your account page.",
      "Copy the ID shown under your name: digits, or name#tag where the game uses one.",
      "Type or paste it above exactly, including the # tag or a (server) part."
    ],
    next: "Continue to payment",
    method: "Payment method",
    wiseT: "Wise / bank transfer",
    wiseN: "For larger orders · manual transfer, checked by a person.",
    paypalT: "PayPal",
    paypalN: "For smaller orders · we send an online payment link in chat.",
    ref: "Order reference",
    amount: "Amount",
    uidRow: "Player ID / account",
    pkgRow: "Package",
    account: "Transfer to",
    accountPaypal: "Where to pay",
    accountPending: "Account details come in chat — wait for them before transferring.",
    accountPaypalPending: "We send the online payment link in chat — pay only through it.",
    howTitle: "How it works",
    howWise: [
      "Transfer the amount we confirm in chat, and put the order reference in the transfer's reference field.",
      "Send us the Wise transaction ID, or a screenshot of the transfer, in chat.",
      "We check the transfer by hand, then the UC is credited to your Player ID."
    ],
    howPaypal: [
      "Send the order with the button below — it reaches us with your order reference and Player ID.",
      "We confirm the amount and send you an online PayPal payment link in chat.",
      "Once the payment clears, the UC is credited to your Player ID."
    ],
    note2: "Nothing is charged on this page. Every payment is checked by a person before we credit the UC.",
    back: "Back",
    send: "Send order in chat",
    copy: "Copy",
    copied: "Copied",
    close: "Close",
    badUid:
      "Enter the Player ID exactly as the game shows it — digits, or name#tag " +
      "where that is the format."
  };

  var dialog = null;
  var trigger = null;
  var ui = {};
  var tierPrices = [];
  var order = { ref: "", method: "wise", step: 1, picked: false };

  // Under this, PayPal is the suggested method: a bank transfer costs the
  // buyer more in fees than the order itself. The sheet only preselects the
  // radio — either way the payment happens in chat (Wise details, or a
  // payment link sent by hand), so a wrong preselection costs one click.
  var PAYPAL_UNDER = 10;

  /* ---------------------------------------------------------------- util */

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

  function trim(s) {
    return String(s == null ? "" : s).replace(/^\s+|\s+$/g, "");
  }

  function rowsFor(key) {
    var all = window.AceBaseGameRows || {};
    return all[key] || [];
  }

  function wiseConf() {
    var p = window.AB_PAYMENT || {};
    return p.wise || {};
  }

  function makeRef() {
    var d = new Date();
    var pad = function (n) { return (n < 10 ? "0" : "") + n; };
    var head = String(d.getFullYear()).slice(2) + pad(d.getMonth() + 1) + pad(d.getDate());
    var tail = "";
    for (var i = 0; i < 6; i++) {
      tail += REF_ABC.charAt(Math.floor(Math.random() * REF_ABC.length));
    }
    return "AB-" + head + "-" + tail;
  }

  function copyText(text, btn) {
    var settle = function () {
      var was = btn.textContent;
      btn.textContent = T.copied;
      btn.classList.add("is-copied");
      setTimeout(function () {
        btn.textContent = was;
        btn.classList.remove("is-copied");
      }, 1600);
    };
    var legacy = function () {
      var ta = document.createElement("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed";
      ta.style.top = "-1000px";
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand("copy"); } catch (e) {}
      document.body.removeChild(ta);
    };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(settle, function () {
        legacy();
        settle();
      });
    } else {
      legacy();
      settle();
    }
  }

  /* --------------------------------------------------------------- build */

  function row(key, label, value, extra) {
    return '<span class="ab-checkout__sum-k">' + esc(label) + "</span>" +
      '<span class="ab-checkout__sum-v' + (extra || "") + '" data-row="' + key +
      '">' + value + "</span>";
  }

  function build() {
    dialog = document.createElement("dialog");
    dialog.className = "ab-checkout";
    dialog.setAttribute("aria-labelledby", "ab-checkout-title");
    dialog.innerHTML =
      '<form class="ab-checkout__panel" novalidate>' +
      '  <header class="ab-checkout__head">' +
      '    <p class="ab-checkout__kicker">' + T.kicker + "</p>" +
      '    <h2 class="ab-checkout__title" id="ab-checkout-title"></h2>' +
      '    <button type="button" class="ab-checkout__close" aria-label="' +
             T.close + '">&times;</button>' +
      '    <ol class="ab-checkout__steps" aria-label="Progress">' +
      '      <li data-step-mark="1">' + T.step1 + "</li>" +
      '      <li data-step-mark="2">' + T.step2 + "</li>" +
      "    </ol>" +
      "  </header>" +
      '  <div class="ab-checkout__body">' +

      '    <div class="ab-checkout__step" data-step="1">' +
      '      <label class="ab-checkout__field">' +
      '        <span class="ab-checkout__label">' + T.playerId + "</span>" +
      '        <input class="ab-checkout__input" type="text" inputmode="numeric"' +
               ' autocomplete="off" autocapitalize="off" spellcheck="false"' +
               ' placeholder="' + T.placeholder + '"' +
               ' aria-describedby="ab-checkout-uid-hint">' +
      '        <span class="ab-checkout__hint" id="ab-checkout-uid-hint">' +
               T.uidHint + "</span>" +
      "      </label>" +
      '      <p class="ab-checkout__error" role="alert" hidden></p>' +
      '      <label class="ab-checkout__field ab-checkout__field--pkg">' +
      '        <span class="ab-checkout__label">' + T.pkg + "</span>" +
      '        <select class="ab-checkout__select"></select>' +
      "      </label>" +
      '      <div class="ab-checkout__summary">' +
      row("pkg", T.pkg, '<span data-sum-pkg></span>') +
      row("price", T.reference, '<span data-sum-price></span>',
          " ab-checkout__sum-v--price") +
      "      </div>" +
      '      <p class="ab-checkout__note">' + T.note1 + "</p>" +
      '      <details class="ab-checkout__help">' +
      "        <summary>" + T.help + "</summary><ol>" +
      T.steps.map(function (s) { return "<li>" + s + "</li>"; }).join("") +
      "</ol></details>" +
      "    </div>" +

      '    <div class="ab-checkout__step" data-step="2" hidden>' +
      '      <fieldset class="ab-checkout__methods">' +
      '        <legend class="ab-checkout__label">' + T.method + "</legend>" +
      '        <label class="ab-checkout__method">' +
      '          <input type="radio" name="ab-pay-method" value="wise" checked>' +
      '          <span class="ab-checkout__method-t">' + T.wiseT + "</span>" +
      '          <span class="ab-checkout__method-n">' + T.wiseN + "</span>" +
      "        </label>" +
      '        <label class="ab-checkout__method">' +
      '          <input type="radio" name="ab-pay-method" value="paypal">' +
      '          <span class="ab-checkout__method-t">' + T.paypalT + "</span>" +
      '          <span class="ab-checkout__method-n">' + T.paypalN + "</span>" +
      "        </label>" +
      "      </fieldset>" +

      '      <div class="ab-checkout__summary">' +
      '        <span class="ab-checkout__sum-k">' + T.ref + "</span>" +
      '        <span class="ab-checkout__sum-v ab-checkout__sum-v--ref" data-row="ref">' +
      '          <span class="ab-checkout__ref" data-ref></span>' +
      '          <button type="button" class="ab-checkout__copy" data-copy-ref>' +
                 T.copy + "</button></span>" +
      row("amount", T.amount, '<span data-sum-amount></span>', " ab-checkout__sum-v--price") +
      row("uid", T.uidRow, '<span data-sum-uid></span>') +
      row("tier", T.pkgRow, '<span data-sum-tier></span>') +
      // Built by hand rather than with row(): its key changes with the method
      // ("Transfer to" vs "Where to pay"), and row() escapes what it is given.
      '        <span class="ab-checkout__sum-k" data-acct-key>' + T.account + "</span>" +
      '        <span class="ab-checkout__sum-v ab-checkout__sum-v--stack" data-row="wise">' +
                 '<span data-sum-account></span></span>' +
      "      </div>" +

      '      <div class="ab-checkout__how">' +
      '        <p class="ab-checkout__label">' + T.howTitle + "</p>" +
      "        <ol data-how></ol></div>" +
      '      <p class="ab-checkout__note">' + T.note2 + "</p>" +
      "    </div>" +

      "  </div>" +
      '  <footer class="ab-checkout__foot">' +
      '    <button type="button" class="ab-checkout__back" data-act="back" hidden>' +
             T.back + "</button>" +
      '    <button type="submit" class="ab-checkout__cta" data-act="next">' +
             T.next + "</button>" +
      "  </footer>" +
      "</form>";
    document.body.appendChild(dialog);

    ui.form = dialog.querySelector(".ab-checkout__panel");
    ui.title = dialog.querySelector(".ab-checkout__title");
    ui.body = dialog.querySelector(".ab-checkout__body");
    ui.input = dialog.querySelector(".ab-checkout__input");
    ui.select = dialog.querySelector(".ab-checkout__select");
    ui.pkgField = dialog.querySelector(".ab-checkout__field--pkg");
    ui.err = dialog.querySelector(".ab-checkout__error");
    ui.sumPkg = dialog.querySelector("[data-sum-pkg]");
    ui.sumPrice = dialog.querySelector("[data-sum-price]");
    ui.step1 = dialog.querySelector('[data-step="1"]');
    ui.step2 = dialog.querySelector('[data-step="2"]');
    ui.marks = dialog.querySelectorAll("[data-step-mark]");
    ui.cta = dialog.querySelector(".ab-checkout__cta");
    ui.back = dialog.querySelector(".ab-checkout__back");
    ui.ref = dialog.querySelector("[data-ref]");
    ui.sumAmount = dialog.querySelector("[data-sum-amount]");
    ui.sumUid = dialog.querySelector("[data-sum-uid]");
    ui.sumTier = dialog.querySelector("[data-sum-tier]");
    ui.sumAccount = dialog.querySelector("[data-sum-account]");
    ui.acctKey = dialog.querySelector("[data-acct-key]");
    ui.how = dialog.querySelector("[data-how]");

    dialog.querySelector(".ab-checkout__close").addEventListener("click", function () {
      dialog.close();
    });
    // The dialog element itself is only hit outside the panel: everything the
    // reader can see is inside .ab-checkout__panel, so a click on the element
    // is a click on the backdrop.
    dialog.addEventListener("click", function (e) {
      if (e.target === dialog) dialog.close();
    });
    dialog.addEventListener("close", function () {
      document.body.classList.remove("ab-checkout-open");
      trigger = null;
    });
    dialog.querySelector("[data-copy-ref]").addEventListener("click", function (e) {
      copyText(order.ref, e.currentTarget);
    });
    ui.select.addEventListener("change", syncSummary);
    ui.step2.addEventListener("change", function (e) {
      if (e.target.name === "ab-pay-method") {
        order.method = e.target.value;
        order.picked = true;
        renderPayment();
      }
    });
    ui.step2.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-copy]");
      if (btn) copyText(btn.getAttribute("data-copy"), btn);
    });
    ui.back.addEventListener("click", function () {
      setStep(1);
      ui.input.focus();
    });
    ui.form.addEventListener("submit", submit);
    ui.input.addEventListener("input", function () {
      if (!ui.err.hidden) {
        ui.err.hidden = true;
        ui.input.removeAttribute("aria-invalid");
      }
    });
  }

  /* ---------------------------------------------------------------- steps */

  function setStep(n) {
    order.step = n;
    ui.step1.hidden = n !== 1;
    ui.step2.hidden = n !== 2;
    ui.back.hidden = n !== 2;
    ui.cta.setAttribute("data-act", n === 1 ? "next" : "send");
    ui.cta.textContent = n === 1 ? T.next : T.send;
    Array.prototype.forEach.call(ui.marks, function (li) {
      var on = Number(li.getAttribute("data-step-mark")) === n;
      li.classList.toggle("is-current", on);
      if (on) li.setAttribute("aria-current", "step");
      else li.removeAttribute("aria-current");
    });
    ui.body.scrollTop = 0;
    if (n === 2) {
      recommend();
      renderPayment();
    }
  }

  function syncSummary() {
    var i = ui.select.selectedIndex;
    var tier = ui.select.options.length ? ui.select.options[i].text : "";
    ui.sumPkg.textContent = tier || "—";
    ui.sumPrice.textContent =
      tierPrices[i] == null ? T.pending : money(tierPrices[i]);
    if (order.step === 2) {
      // The tier moved the amount across or under the PayPal line.
      recommend();
      renderPayment();
    }
  }

  function currentTier() {
    return ui.select.options.length
      ? ui.select.options[ui.select.selectedIndex].text
      : "";
  }

  function currentPrice() {
    var p = tierPrices[ui.select.selectedIndex];
    return p == null ? null : p;
  }

  // The account row is the one part that must never be guessed: it prints
  // what extra.payment.wise holds, and when that is empty it says out loud
  // that the details come from chat.
  function accountHtml() {
    // Both fallbacks are sentences, so they take the prose span rather than
    // the bold value weight the account numbers use.
    var note = function (s) {
      return '<span class="ab-checkout__acct-note">' + esc(s) + "</span>";
    };
    if (order.method !== "wise") return note(T.accountPaypalPending);
    var w = wiseConf();
    var lines = [];
    if (w.email) {
      lines.push('<span class="ab-checkout__acct">' + esc(w.email) +
        '<button type="button" class="ab-checkout__copy" data-copy="' +
        esc(w.email) + '">' + T.copy + "</button></span>");
    }
    if (w.iban) {
      lines.push('<span class="ab-checkout__acct">' + esc(w.iban) +
        '<button type="button" class="ab-checkout__copy" data-copy="' +
        esc(w.iban) + '">' + T.copy + "</button></span>");
    }
    if (!lines.length) return note(T.accountPending);
    if (w.name) lines.unshift('<span class="ab-checkout__acct-name">' + esc(w.name) + "</span>");
    return lines.join("");
  }

  function renderPayment() {
    if (!order.ref) order.ref = makeRef();
    var wise = order.method === "wise";
    ui.ref.textContent = order.ref;
    var price = currentPrice();
    ui.sumAmount.textContent = price == null ? T.pending : money(price);
    ui.sumUid.textContent = trim(ui.input.value) || "—";
    ui.sumTier.textContent = currentTier() || "—";
    ui.acctKey.textContent = wise ? T.account : T.accountPaypal;
    ui.sumAccount.innerHTML = accountHtml();
    ui.how.innerHTML = (wise ? T.howWise : T.howPaypal)
      .map(function (s) { return "<li>" + esc(s) + "</li>"; })
      .join("");
  }

  // Suggest the method that suits the amount: below PAYPAL_UNDER a bank
  // transfer makes little sense, above it the manual transfer does. A
  // choice the reader made by hand wins until the sheet is reopened.
  function recommend() {
    if (order.picked) return;
    var price = currentPrice();
    var next = price != null && price < PAYPAL_UNDER ? "paypal" : "wise";
    order.method = next;
    var input = ui.step2.querySelector('input[name="ab-pay-method"][value="' + next + '"]');
    if (input) input.checked = true;
  }

  /* ----------------------------------------------------------------- open */

  // Split out of open() so a sheet opened in the moment before prices.json
  // landed can be filled in when it does (see the price listener in init).
  function fillTiers(btn) {
    var rows = rowsFor(btn.getAttribute("data-checkout"));
    var card = btn.closest(".ab-card");
    var cardSel = card && card.querySelector(".ab-ec-pick__select");

    if (rows.length) {
      tierPrices = rows.map(function (r) { return r.lowest; });
      ui.select.innerHTML = rows
        .map(function (r) { return "<option>" + esc(r.title || T.pkg) + "</option>"; })
        .join("");
      ui.select.selectedIndex =
        cardSel && cardSel.selectedIndex < rows.length ? cardSel.selectedIndex : 0;
      ui.pkgField.hidden = false;
    } else {
      // prices.json did not arrive: keep the sheet (the UID still matters),
      // drop the package row rather than offer an empty select, and let the
      // chat ask which package.
      tierPrices = [];
      ui.select.innerHTML = "";
      ui.pkgField.hidden = true;
    }
    // The summary is package + reference price, so it goes with the package.
    ui.sumPkg.parentNode.parentNode.hidden = !rows.length;
    syncSummary();
  }

  function open(btn) {
    if (!dialog) build();
    trigger = btn;

    ui.title.textContent =
      btn.getAttribute("data-checkout-name") || btn.textContent.trim();
    ui.err.hidden = true;
    ui.input.removeAttribute("aria-invalid");
    ui.input.value = "";
    order.ref = "";
    order.method = "wise";
    order.picked = false;
    ui.step2.querySelector('input[value="wise"]').checked = true;
    fillTiers(btn);
    setStep(1);

    document.body.classList.add("ab-checkout-open");
    if (!dialog.open) dialog.showModal();
    ui.input.focus();
  }

  /* --------------------------------------------------------------- submit */

  function submit(e) {
    e.preventDefault();
    if (!trigger) return;

    var uid = trim(ui.input.value);
    if (!validId(uid)) {
      setStep(1);
      ui.err.textContent = T.badUid;
      ui.err.hidden = false;
      ui.input.setAttribute("aria-invalid", "true");
      ui.input.focus();
      return;
    }
    if (order.step === 1) {
      setStep(2);
      return;
    }

    // The tier in the sheet wins over the card's own, since the reader may
    // have changed either one. The base sentence comes from the markup, where
    // games-prices.js already keeps the card's own handoff message.
    var tier = currentTier();
    var price = currentPrice();
    var base = (
      trigger.getAttribute("data-crisp-base") ||
      trigger.getAttribute("data-crisp-msg") ||
      ""
    ).replace(/[.。]\s*$/, "");

    var msg = base + (tier ? ", spec " + tier : "") +
      ". Player ID / account: " + uid +
      ". Order " + order.ref + ", paying by " +
      (order.method === "wise"
        ? "Wise transfer"
        : "PayPal — please send the online payment link") +
      "." +
      (price == null ? "" : " Reference price " + money(price) + ".");

    if (typeof window.abOpenCrisp === "function") {
      window.abOpenCrisp(msg);
    } else if (window.$crisp && window.$crisp.push) {
      window.$crisp.push(["set", "message:text", msg]);
      window.$crisp.push(["do", "chat:open"]);
    }

    dialog.close();
  }

  /* ----------------------------------------------------------------- wire */

  function init() {
    var nodes = Array.prototype.slice.call(document.querySelectorAll(TRIGGERS));
    if (!nodes.length) return;

    // A reader on a slow connection can tap Buy before prices.json has been
    // dealt with; games-prices.js announces the rows when they arrive, and an
    // already-open sheet picks them up rather than sending the order without
    // a package.
    document.addEventListener("acebase:prices", function () {
      if (dialog && dialog.open && trigger && ui.pkgField.hidden) {
        fillTiers(trigger);
      }
    });

    nodes.forEach(function (btn) {
      // markup drift guard: a data-checkout trigger must not also be a
      // .ab-crisp-open one, or crisp.js's own capture listener opens the chat
      // on the same click and the reader gets both.
      btn.classList.remove("ab-crisp-open");
      btn.addEventListener("click", function (e) {
        e.preventDefault();
        open(btn);
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
