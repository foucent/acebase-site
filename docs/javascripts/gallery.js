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
   card image's own alt.

   A set can also belong to a video: img[data-gallery-video="https://…"] makes
   the last photo in the set carry a play button that opens that link in a new
   tab, so the video the card sells is reachable from inside the lightbox
   instead of only from the action line under it. The button exists on the last
   frame alone — every other frame keeps the "more photos" hint.

   A hosted file on this site (an .mp4/.webm, 2026-11-03) is played in the
   lightbox instead of opening a tab: the button says "Watch the video" without
   the YouTube mark, and pressing it swaps the photo for a <video controls>
   playing the file. Moving to another frame, or closing, puts the photo back
   and stops the video. A YouTube link keeps the old behaviour — new tab. */
(function () {
  var items = [];
  var index = 0;
  var video = "";

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
      '  <video class="ab-lightbox__video" controls playsinline preload="metadata" hidden></video>' +
      '  <a class="ab-lightbox__play" href="#" target="_blank" rel="noopener" aria-label="Watch Details on YouTube" hidden>' +
      '    <svg class="ab-yt-mark" viewBox="0 0 28 20" aria-hidden="true" focusable="false">' +
      '      <rect width="28" height="20" rx="5" fill="#f00"/>' +
      '      <path d="M10.2 5.6v8.8L17.8 10z" fill="#fff"/>' +
      "    </svg>" +
      '    <span class="ab-lightbox__play-label">Watch Details on YouTube</span>' +
      "  </a>" +
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
    var play = root.querySelector(".ab-lightbox__play");
    var playLabel = root.querySelector(".ab-lightbox__play-label");
    var ytMark = root.querySelector(".ab-yt-mark");
    var stageVideo = root.querySelector(".ab-lightbox__video");

    // A file this site hosts plays here; anything else (a YouTube page) is a
    // link to open in a new tab.
    function isLocalVideo(url) {
      return /\.(mp4|webm|ogv|ogg|mov)([?#]|$)/i.test(url);
    }

    function stopVideo() {
      if (stageVideo.hidden) return;
      stageVideo.pause();
      stageVideo.removeAttribute("src");
      stageVideo.load();
      stageVideo.hidden = true;
      img.style.display = "";
    }

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
      stopVideo();
      // The play button belongs to the last photo of a set that names a video;
      // the hint is the only thing telling a reader what it will do.
      var playable = Boolean(video) && index === items.length - 1;
      var local = playable && isLocalVideo(video);
      play.hidden = !playable;
      if (playable) play.href = video;
      else play.removeAttribute("href");
      // A hosted file plays in place, so the button says so and drops the
      // YouTube mark rather than promising a tab that never opens.
      playLabel.textContent = local ? "Watch the video" : "Watch Details on YouTube";
      play.setAttribute("aria-label", local ? "Watch the video" : "Watch Details on YouTube");
      ytMark.style.display = local ? "none" : "";
      hint.textContent = playable
        ? "Last photo — press play to watch the video"
        : "More photos — swipe or use arrows";
      renderDots();
    }

    function close() {
      root.hidden = true;
      stopVideo();
      img.removeAttribute("src");
      items = [];
      video = "";
      document.body.classList.remove("ab-lightbox-open");
    }

    function open(list, start, videoUrl) {
      items = list;
      video = videoUrl || "";
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

    // A hosted file is played right here; a YouTube link keeps its new tab.
    play.addEventListener("click", function (e) {
      if (!isLocalVideo(video)) return;
      e.preventDefault();
      e.stopPropagation();
      stageVideo.src = video;
      stageVideo.hidden = false;
      img.style.display = "none";
      play.hidden = true;
      var started = stageVideo.play();
      if (started && started.catch) started.catch(function () {});
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

      var videoUrl = img.getAttribute("data-gallery-video") || "";

      img.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopPropagation();
        root._open(list, 0, videoUrl);
      });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bindGalleries);
  } else {
    bindGalleries();
  }
})();
