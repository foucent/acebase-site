(function () {
  "use strict";

  // /digital/ only: a card sells one game but many amounts, so the Add button
  // has to carry whichever spec the reader picked.
  //
  // cart.js reads data-name and data-price on the click itself, not at load, so
  // rewriting them from the <select> is all this needs to do — no second copy of
  // the price list, and no change to the cart. The name carries the spec because
  // the cart keys lines by name: "PUBG Mobile UC — 60 UC" and the same game at
  // another amount are two lines, as they should be.
  //
  // Options hold their own data-name/data-price (written by the generator from
  // prices.json); selectedIndex is what picks the row, the option's text is only
  // what the row is called.

  // Same spelling as cart.js's own money(): whole dollars drop the cents.
  function money(n) {
    n = Math.round(n * 100) / 100;
    return "$" + n.toFixed(n % 1 ? 2 : 0);
  }

  function sync(card) {
    var sel = card.querySelector("[data-digital-pick]");
    var add = card.querySelector(".ab-cart-add");
    if (!sel || !add) return;

    var opt = sel.options[sel.selectedIndex];
    if (!opt) return;

    var name = opt.getAttribute("data-name");
    var price = parseFloat(opt.getAttribute("data-price"));
    if (!name || isNaN(price)) return;

    add.setAttribute("data-name", name);
    add.setAttribute("data-price", String(price));
    add.setAttribute("aria-label", "Add " + name + " to cart");

    var shown = card.querySelector("[data-digital-price]");
    if (shown) shown.textContent = money(price);

    // A spec switch is not the add that just flashed green; let the button go
    // back to its resting look rather than keep a stale confirmation.
    add.classList.remove("ab-cart-add--done");
  }

  var cards = Array.prototype.slice.call(
    document.querySelectorAll("[data-digital-card]")
  );

  cards.forEach(function (card) {
    var sel = card.querySelector("[data-digital-pick]");
    if (!sel) return;
    sel.addEventListener("change", function () {
      sync(card);
    });
    sync(card);
  });
})();
