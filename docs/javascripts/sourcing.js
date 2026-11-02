/* The Request Sourcing button — what the cart's "+ Add to cart" became.

   2026-11-02, at the user's request: 「将+Add to cart改为 Request Sourcing，
   全站都没有购物车」. The cart (localStorage lines, floating button, drawer,
   toast, "Confirm in live chat") is gone with cart.js. A button now asks the
   question for one piece instead of tallying a basket: it hands that piece to
   the live chat and a person answers with availability and the total.

   The button carries the same data-name / data-price hooks the cart used, and
   digital.js still rewrites them when a Spec dropdown changes, so the message
   names the exact option on screen. crisp.js loads before this file and owns
   window.abOpenCrisp. */
(function () {
  function money(n) {
    return "$" + (Math.round(n * 100) / 100).toFixed(n % 1 ? 2 : 0);
  }

  function buildMessage(btn) {
    var name = (btn.getAttribute("data-name") || "").trim();
    var price = parseFloat(btn.getAttribute("data-price"));
    if (!name) return "";
    var line = name + (isNaN(price) ? "" : " — " + money(price) + " each");
    return (
      "Hello, I'd like to request sourcing for:\n\n" +
      line +
      "\n\nPlease confirm availability and the final total."
    );
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

  function flash(btn) {
    btn.classList.add("ab-request--sent");
    setTimeout(function () {
      btn.classList.remove("ab-request--sent");
    }, 650);
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest ? e.target.closest(".ab-request") : null;
    if (!btn) return;
    e.preventDefault();
    var msg = buildMessage(btn);
    if (!msg) return;
    openChat(msg);
    flash(btn);
  });
})();
