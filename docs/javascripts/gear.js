/* The front page's link-to-price box and its category pills (2026-11-08, user:
   「将 http://127.0.0.1:8003/gear/ 页面模仿 https://www.superbuy.com/cn/page/
   homepage/…」, then 「这部分的意思应该是 用户输入商品链接，我为他通过异步的
   方式获取最低采购价」, then 「用户点 get price之后，需要弹出一个邮箱输入框，
   用于接收价格信息」).

   The hero box asks for a product link. Submitting one opens the email dialog
   (#price-modal) rather than sending anything: the price is looked up out of
   band, so it needs an address to land at. On submit, the link and the address
   go into one Crisp message — this site has no form backend, so the chat inbox
   is where the request is actually picked up — and the note under the box says
   where the answer will go. The input keeps its value, so a typo can be fixed
   and sent again.

   Anything that is not a link is treated as a search of the shelf: the pills
   narrow by category, the box narrows by text, and the two stack. A shelf this
   long has six kinds of thing to narrow by and two dozen brands, so the pills
   say Mice / Keyboards / Mousepads / Monitors / Headsets / Chairs (2026-11-08,
   when page one of five more review categories landed); before that they were
   brand pills. The copy never calls the box a search.

   The cards carry data-category and data-search (a lower-case string of the
   model plus its category) in index.md, so a card without data-search simply
   never matches. Only this page's markup is touched: everything below lives
   inside .ab-sb. */
(function () {
  "use strict";

  var root = document.querySelector(".ab-sb");
  if (!root) return;

  var grid = document.getElementById("gear-grid");
  var pills = document.getElementById("gear-pills");
  var form = document.getElementById("gear-search-form");
  var input = document.getElementById("gear-search");
  var note = document.getElementById("gear-note");
  var empty = document.getElementById("gear-empty");
  var modal = document.getElementById("price-modal");
  if (!grid || !pills) return;

  var cards = Array.prototype.slice.call(grid.querySelectorAll(".ab-sb-card"));
  var category = "all";
  var query = "";

  function words(s) {
    return String(s || "")
      .toLowerCase()
      .split(/\s+/)
      .filter(Boolean);
  }

  /* A link is anything with a scheme, or a bare host with a dot in it
     ("shop.example.com/x"). A model name — "wooting 80he", "75%" — has no dot,
     so it falls through to the grid. */
  function looksLikeLink(v) {
    var s = String(v || "").trim();
    if (!s) return false;
    if (/^https?:\/\//i.test(s)) return true;
    return /^(www\.)?[a-z0-9-]+(\.[a-z0-9-]+)+([/?#]|$)/i.test(s);
  }

  /* Deliberately loose: something@something.tld and no spaces. Anything
     stricter rejects addresses that are perfectly deliverable. */
  function looksLikeEmail(v) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(v || "").trim());
  }

  function apply() {
    var terms = words(query);
    var shown = 0;

    cards.forEach(function (card) {
      var okCategory = category === "all" ||
        card.getAttribute("data-category") === category;
      var hay = card.getAttribute("data-search") || "";
      var okText = terms.every(function (t) {
        return hay.indexOf(t) !== -1;
      });
      var show = okCategory && okText;
      card.hidden = !show;
      if (show) shown += 1;
    });

    if (empty) empty.hidden = shown !== 0;
  }

  /* ---------- the email gate ---------- */

  var priceModal = modal && modal.querySelector(".ab-sb-modal__panel") ? modal : null;
  var emailForm = priceModal && priceModal.querySelector("#price-form");
  var emailInput = priceModal && priceModal.querySelector("#price-email");
  var emailError = priceModal && priceModal.querySelector("#price-error");
  var linkEcho = priceModal && priceModal.querySelector("#price-modal-link");
  var pendingLink = "";
  var lastFocus = null;

  function setError(msg) {
    if (!emailInput) return;
    if (msg) {
      emailInput.setAttribute("aria-invalid", "true");
      if (emailError) {
        emailError.textContent = msg;
        emailError.hidden = false;
      }
    } else {
      emailInput.removeAttribute("aria-invalid");
      if (emailError) {
        emailError.textContent = "";
        emailError.hidden = true;
      }
    }
  }

  function openModal(link) {
    if (!priceModal) return;
    pendingLink = link;
    setError("");
    if (linkEcho) linkEcho.textContent = link;
    if (emailInput) emailInput.value = "";
    lastFocus = document.activeElement;
    priceModal.hidden = false;
    document.body.style.overflow = "hidden";
    if (emailInput) emailInput.focus();
  }

  function closeModal() {
    if (!priceModal || priceModal.hidden) return;
    priceModal.hidden = true;
    document.body.style.overflow = "";
    setError("");
    if (lastFocus && lastFocus.focus) lastFocus.focus();
    lastFocus = null;
  }

  function send(link, email) {
    var msg =
      "Hello, I'd like the lowest sourcing price for this link:\n\n" +
      link +
      "\n\nPlease email the price to: " +
      email;
    if (typeof window.abOpenCrisp === "function") {
      window.abOpenCrisp(msg);
    } else {
      /* crisp.js loads before this file, but a page that failed to load it
         must still queue the message rather than throw */
      window.$crisp = window.$crisp || [];
      window.$crisp.push(["set", "message:text", msg]);
      window.$crisp.push(["do", "chat:open"]);
    }
    if (note) {
      note.textContent =
        "Request sent — the lowest price goes to " + email + ".";
      note.hidden = false;
    }
  }

  if (priceModal) {
    priceModal.addEventListener("click", function (ev) {
      /* the backdrop closes; a click inside the panel does not */
      if (ev.target === priceModal) closeModal();
    });
    var closeBtn = priceModal.querySelector(".ab-sb-modal__close");
    if (closeBtn) closeBtn.addEventListener("click", closeModal);
    document.addEventListener("keydown", function (ev) {
      if (ev.key === "Escape" && !priceModal.hidden) {
        ev.preventDefault();
        closeModal();
      }
    });
  }

  if (emailForm && emailInput) {
    emailInput.addEventListener("input", function () {
      if (emailInput.getAttribute("aria-invalid") === "true") setError("");
    });
    emailForm.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var email = emailInput.value.trim();
      if (!email) {
        setError("Enter an email address so we can send the price.");
        emailInput.focus();
        return;
      }
      if (!looksLikeEmail(email)) {
        setError("That does not look like an email address — check it and try again.");
        emailInput.focus();
        return;
      }
      send(pendingLink || (input ? input.value.trim() : ""), email);
      closeModal();
    });
  }

  /* ---------- the shelf ---------- */

  pills.addEventListener("click", function (ev) {
    var pill = ev.target.closest(".ab-sb-pill");
    if (!pill) return;
    category = pill.getAttribute("data-category") || "all";
    Array.prototype.forEach.call(pills.querySelectorAll(".ab-sb-pill"), function (p) {
      var on = p === pill;
      p.classList.toggle("is-active", on);
      p.setAttribute("aria-pressed", on ? "true" : "false");
    });
    apply();
  });

  if (input) {
    input.addEventListener("input", function () {
      query = input.value;
      if (note) note.hidden = true;
      apply();
    });
  }

  if (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var value = input ? input.value.trim() : "";

      if (looksLikeLink(value)) {
        /* a link is not a filter: put the whole shelf back, then ask where to
           send the price */
        query = "";
        apply();
        openModal(value);
        return;
      }

      if (note) note.hidden = true;
      query = value;
      apply();
      var disc = document.getElementById("gear");
      if (disc) disc.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  apply();
})();
