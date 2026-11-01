/* Photo sets on the magazine cards.

   Ported from mygear.top's gallery-lightbox.js (2026-11-01), narrowed to what
   this site has: an <img data-gallery="a.jpg,b.jpg,…"> inside .ab-card__media.
   The mygear version also walked price tables, `.mg-gallery` link strips and
   the spec-sheet <template> panels; none of those exist here, so none came
   over. What it does keep is the count pill — the number of photos is written
   on the picture instead of a strip of thumbnails under it — and the lightbox
   itself: arrows, dots, arrow keys, Escape and swipe.

   Only images that name their own set opt in. A card without data-gallery is
   left completely alone, so dropping this file on every page cannot turn the
   other catalogue cards into one-photo lightboxes by accident.

   A data-gallery entry is a photo, optionally with its alt text after a "|":
   "/assets/foo/02.jpg|What that photo shows". Without one the entry takes the
   card image's own alt. */
(function () {
  var items = [];
  var index = 0;

  function ensureLightbox() {
    var root = document.getElementById("ab-lightbox");
    if (root) return root;

    root = document.createElement("div");
    root.id = "ab-lightbox";
    root.className = "ab-lightbox";
    root.hidden = true;
    root.setAttribute("role", "dialog");
    root.setAttribute("aria-modal", "true");
    root.setAttribute("aria-label", "Image preview");
    root.innerHTML =
      '<button type="button" class="ab-lightbox__close" aria-label="Close">×</button>' +
      '<button type="button" class="ab-lightbox__nav ab-lightbox__prev" aria-label="Previous">‹</button>' +
      '<button type="button" class="ab-lightbox__nav ab-lightbox__next" aria-label="Next">›</button>' +
      '<div class="ab-lightbox__stage">' +
      '  <img class="ab-lightbox__img" alt="">' +
      '  <div class="ab-lightbox__meta">' +
      '    <div class="ab-lightbox__counter" aria-live="polite"></div>' +
      '    <div class="ab-lightbox__hint">More photos — swipe or use arrows</div>' +
      "  </div>" +
      '  <div class="ab-lightbox__dots" aria-hidden="true"></div>' +
      "</div>";
    document.body.appendChild(root);

    var closeBtn = root.querySelector(".ab-lightbox__close");
    var prevBtn = root.querySelector(".ab-lightbox__prev");
    var nextBtn = root.querySelector(".ab-lightbox__next");
    var img = root.querySelector(".ab-lightbox__img");
    var counter = root.querySelector(".ab-lightbox__counter");
    var hint = root.querySelector(".ab-lightbox__hint");
    var dots = root.querySelector(".ab-lightbox__dots");

    function renderDots() {
      if (items.length <= 1) {
        dots.hidden = true;
        dots.innerHTML = "";
        return;
      }
      dots.hidden = false;
      dots.innerHTML = items
        .map(function (_, i) {
          return (
            '<button type="button" class="ab-lightbox__dot' +
            (i === index ? " is-active" : "") +
            '" data-index="' +
            i +
            '" aria-label="Photo ' +
            (i + 1) +
            '"></button>'
          );
        })
        .join("");
    }

    function show(i) {
      if (!items.length) return;
      index = (i + items.length) % items.length;
      var item = items[index];
      img.src = item.href;
      img.alt = item.alt || "";
      counter.textContent = index + 1 + " / " + items.length;
      var multi = items.length > 1;
      prevBtn.hidden = !multi;
      nextBtn.hidden = !multi;
      counter.hidden = !multi;
      hint.hidden = !multi;
      renderDots();
    }

    function close() {
      root.hidden = true;
      img.removeAttribute("src");
      items = [];
      document.body.classList.remove("ab-lightbox-open");
    }

    function open(list, start) {
      items = list;
      root.hidden = false;
      document.body.classList.add("ab-lightbox-open");
      show(start);
    }

    root.addEventListener("click", function (e) {
      if (e.target === root) close();
    });
    closeBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      close();
    });
    prevBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      show(index - 1);
    });
    nextBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      show(index + 1);
    });
    dots.addEventListener("click", function (e) {
      var dot = e.target.closest(".ab-lightbox__dot");
      if (!dot) return;
      e.stopPropagation();
      show(parseInt(dot.getAttribute("data-index"), 10) || 0);
    });

    var touchX = 0;
    var touchY = 0;
    var swiped = false;

    img.addEventListener("click", function (e) {
      e.stopPropagation();
      if (swiped) {
        swiped = false;
        return;
      }
      if (items.length > 1) show(index + 1);
    });
    document.addEventListener("keydown", function (e) {
      if (root.hidden) return;
      if (e.key === "Escape") close();
      else if (e.key === "ArrowLeft") show(index - 1);
      else if (e.key === "ArrowRight") show(index + 1);
    });

    root.addEventListener(
      "touchstart",
      function (e) {
        if (e.touches.length !== 1) return;
        touchX = e.touches[0].clientX;
        touchY = e.touches[0].clientY;
        swiped = false;
      },
      { passive: true }
    );
    root.addEventListener(
      "touchmove",
      function (e) {
        if (e.touches.length !== 1 || items.length <= 1) return;
        var dx = e.touches[0].clientX - touchX;
        var dy = e.touches[0].clientY - touchY;
        if (Math.abs(dx) > 12 && Math.abs(dx) > Math.abs(dy)) swiped = true;
      },
      { passive: true }
    );
    root.addEventListener(
      "touchend",
      function (e) {
        if (items.length <= 1 || e.changedTouches.length !== 1) return;
        var t = e.changedTouches[0];
        var dx = t.clientX - touchX;
        var dy = t.clientY - touchY;
        var absX = Math.abs(dx);
        var absY = Math.abs(dy);
        if (absX < 48 || absX < absY * 1.15) return;
        swiped = true;
        if (dx < 0) show(index + 1);
        else show(index - 1);
      },
      { passive: true }
    );

    root._open = open;
    return root;
  }

  function galleryEntry(entry, img) {
    var item = { href: "", alt: img.alt || "" };
    entry.split("|").forEach(function (field, i) {
      var value = field.trim();
      if (!value) return;
      if (i === 0) item.href = value;
      else item.alt = value;
    });
    return item;
  }

  function bindGalleries() {
    var root = ensureLightbox();

    document.querySelectorAll("img[data-gallery]").forEach(function (img) {
      if (img.dataset.abLightboxBound === "1") return;
      img.dataset.abLightboxBound = "1";

      var list = (img.getAttribute("data-gallery") || "")
        .split(",")
        .map(function (s) {
          return s.trim();
        })
        .filter(Boolean)
        .map(function (entry) {
          return galleryEntry(entry, img);
        });

      if (!list.length) return;

      // The count goes on the picture, in the same corner mygear put it. A bare
      // number reads as nothing to a screen reader, so the label carries the
      // words the pill no longer shows.
      var media = img.closest(".ab-card__media") || img.parentElement;
      if (media && list.length > 1 && !media.querySelector(".ab-card__count")) {
        var pill = document.createElement("span");
        pill.className = "ab-card__count";
        pill.textContent = String(list.length);
        pill.setAttribute("role", "img");
        pill.setAttribute("aria-label", list.length + " photos");
        media.appendChild(pill);
      }

      img.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        root._open(list, 0);
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindGalleries);
  } else {
    bindGalleries();
  }
})();
