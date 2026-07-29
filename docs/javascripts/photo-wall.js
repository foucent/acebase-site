(function () {
  function shuffle(node) {
    if (!node) return;
    var items = Array.prototype.slice.call(node.children);
    for (var i = items.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = items[i];
      items[i] = items[j];
      items[j] = tmp;
    }
    items.forEach(function (el) {
      node.appendChild(el);
    });
  }

  function parseGallery(tile) {
    var raw = tile.getAttribute("data-gallery");
    if (raw) {
      try {
        var list = JSON.parse(raw);
        if (Array.isArray(list) && list.length) return list;
      } catch (e) {}
    }
    var href = tile.getAttribute("href");
    return href ? [href] : [];
  }

  function todayStamp() {
    var d = new Date();
    return (
      d.getFullYear() +
      "-" +
      String(d.getMonth() + 1).padStart(2, "0") +
      "-" +
      String(d.getDate()).padStart(2, "0")
    );
  }

  function dismissStorageKey(lookId) {
    return "sc-buy-dismiss:" + todayStamp() + ":" + lookId;
  }

  function isBuyDismissed(lookId) {
    try {
      return localStorage.getItem(dismissStorageKey(lookId)) === "1";
    } catch (e) {
      return false;
    }
  }

  function dismissBuy(lookId) {
    try {
      localStorage.setItem(dismissStorageKey(lookId), "1");
    } catch (e) {}
  }

  function lookIdFromTile(tile, gallery) {
    return (
      tile.getAttribute("data-look") ||
      tile.getAttribute("href") ||
      (gallery && gallery[0]) ||
      tile.getAttribute("title") ||
      ""
    );
  }

  function waIcon() {
    return (
      '<svg class="sc-lightbox__buy-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">' +
      '<path fill="currentColor" d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>' +
      "</svg>"
    );
  }

  function createLightbox() {
    var root = document.createElement("div");
    root.className = "sc-lightbox";
    root.id = "sc-lightbox";
    root.hidden = true;
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-modal", "true");
    root.innerHTML =
      '<button type="button" class="sc-lightbox__close" aria-label="Close">&times;</button>' +
      '<button type="button" class="sc-lightbox__nav sc-lightbox__nav--prev" aria-label="Previous">‹</button>' +
      '<figure class="sc-lightbox__stage">' +
      '<div class="sc-lightbox__media">' +
      '<img class="sc-lightbox__img" alt="">' +
      '<div class="sc-lightbox__buy-wrap" hidden>' +
      '<a class="sc-lightbox__buy" href="/shop/how-to-order/" target="_blank" rel="noopener">' +
      waIcon() +
      "<span>WhatsApp / Order</span>" +
      "</a>" +
      '<button type="button" class="sc-lightbox__buy-dismiss" aria-label="Hide for today">&times;</button>' +
      "</div>" +
      "</div>" +
      '<figcaption class="sc-lightbox__cap"></figcaption>' +
      "</figure>" +
      '<button type="button" class="sc-lightbox__nav sc-lightbox__nav--next" aria-label="Next">›</button>';
    document.body.appendChild(root);
    return root;
  }

  function initLightbox(wall) {
    var tiles = Array.prototype.slice.call(wall.querySelectorAll(".sc-wall__tile"));
    if (!tiles.length) return;

    var box = createLightbox();
    var img = box.querySelector(".sc-lightbox__img");
    var cap = box.querySelector(".sc-lightbox__cap");
    var buyWrap = box.querySelector(".sc-lightbox__buy-wrap");
    var buy = box.querySelector(".sc-lightbox__buy");
    var buyDismiss = box.querySelector(".sc-lightbox__buy-dismiss");
    var gallery = [];
    var title = "";
    var lookId = "";
    var buyUrl = "/shop/";
    var idx = 0;
    var open = false;
    var buyTimer = null;
    var BUY_DWELL_MS = 5000;

    function clearBuyTimer() {
      if (buyTimer) {
        clearTimeout(buyTimer);
        buyTimer = null;
      }
    }

    function hideBuyCta() {
      clearBuyTimer();
      buyWrap.classList.remove("is-visible");
      buyWrap.hidden = true;
    }

    function armBuyCta() {
      hideBuyCta();
      if (!(gallery.length > 0 && buyUrl && !isBuyDismissed(lookId))) return;
      buyWrap.hidden = false;
      // force reflow so fade-in still runs if re-armed quickly
      void buyWrap.offsetWidth;
      buyTimer = setTimeout(function () {
        buyTimer = null;
        buyWrap.classList.add("is-visible");
      }, BUY_DWELL_MS);
    }

    function show(i) {
      if (!gallery.length) return;
      idx = (i + gallery.length) % gallery.length;
      img.src = gallery[idx];
      img.alt = title;
      cap.textContent =
        gallery.length > 1
          ? title + " · " + (idx + 1) + " / " + gallery.length
          : title;
      armBuyCta();
    }

    function openGallery(tile, start) {
      gallery = parseGallery(tile);
      title = tile.getAttribute("title") || "";
      lookId = lookIdFromTile(tile, gallery);
      buyUrl = tile.getAttribute("data-buy") || "/shop/";
      buy.href = buyUrl;
      show(typeof start === "number" ? start : 0);
      box.hidden = false;
      document.body.classList.add("sc-lightbox-open");
      open = true;
    }

    function close() {
      box.hidden = true;
      document.body.classList.remove("sc-lightbox-open");
      open = false;
      gallery = [];
      lookId = "";
      hideBuyCta();
      img.removeAttribute("src");
    }

    tiles.forEach(function (tile) {
      tile.addEventListener("click", function (e) {
        e.preventDefault();
        openGallery(tile, 0);
      });
    });

    buyDismiss.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      if (lookId) dismissBuy(lookId);
      hideBuyCta();
    });

    box.querySelector(".sc-lightbox__close").addEventListener("click", close);
    box.querySelector(".sc-lightbox__nav--prev").addEventListener("click", function () {
      show(idx - 1);
    });
    box.querySelector(".sc-lightbox__nav--next").addEventListener("click", function () {
      show(idx + 1);
    });

    box.addEventListener("click", function (e) {
      if (e.target === box) close();
    });

    document.addEventListener("keydown", function (e) {
      if (!open) return;
      if (e.key === "Escape") close();
      else if (e.key === "ArrowLeft") show(idx - 1);
      else if (e.key === "ArrowRight") show(idx + 1);
    });

    var touchX = null;
    box.addEventListener(
      "touchstart",
      function (e) {
        if (e.changedTouches && e.changedTouches[0]) {
          touchX = e.changedTouches[0].clientX;
        }
      },
      { passive: true }
    );
    box.addEventListener(
      "touchend",
      function (e) {
        if (touchX == null || !e.changedTouches || !e.changedTouches[0]) return;
        var dx = e.changedTouches[0].clientX - touchX;
        touchX = null;
        if (Math.abs(dx) < 40) return;
        if (dx > 0) show(idx - 1);
        else show(idx + 1);
      },
      { passive: true }
    );
  }

  function run() {
    var wall = document.getElementById("sc-wall");
    if (!wall) return;
    shuffle(wall);
    initLightbox(wall);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
