/* Delta Force account cards — paginate by 20, load more on scroll/click. */
(function () {
  "use strict";

  function init() {
    var PAGE = 20;
    var container = document.getElementById("df-cards");
    if (!container) return;

    // 原始单元序列（卡片 + 分区标题，按 DOM 顺序）
    var allUnits = Array.prototype.slice.call(container.children).filter(function (el) {
      return el.classList.contains("mg-df-card") || el.classList.contains("mg-df-section");
    });
    if (!allUnits.length) return;

    var totalCards = allUnits.filter(function (el) {
      return el.classList.contains("mg-df-card");
    }).length;

    // 按每 PAGE 张卡片切分批次，标题归属其后卡片所在的批次
    var batches = [];
    var cur = [];
    var cardCount = 0;
    allUnits.forEach(function (el) {
      if (el.classList.contains("mg-df-section")) {
        if (cardCount >= PAGE && cur.length) {
          batches.push(cur);
          cur = [];
          cardCount = 0;
        }
        cur.push(el);
        return;
      }
      if (cardCount >= PAGE) {
        batches.push(cur);
        cur = [];
        cardCount = 0;
      }
      cur.push(el);
      cardCount++;
    });
    if (cur.length) batches.push(cur);

    var loadEl = document.getElementById("df-load-more");
    var batchIndex = 0;
    var shownCards = 0;
    var allLoaded = false;

    function renderLoad() {
      if (!loadEl) return;
      loadEl.textContent = allLoaded
        ? "已全部加载"
        : "加载更多（" + shownCards + " / " + totalCards + "）";
      loadEl.classList.toggle("is-end", allLoaded);
    }

    function showNext() {
      if (allLoaded || batchIndex >= batches.length) {
        allLoaded = true;
        renderLoad();
        return;
      }
      var batch = batches[batchIndex++];
      batch.forEach(function (el) {
        container.appendChild(el);
      });
      shownCards = Math.min(
        shownCards + batch.filter(function (el) {
          return el.classList.contains("mg-df-card");
        }).length,
        totalCards
      );
      if (batchIndex >= batches.length) allLoaded = true;
      renderLoad();
    }

    // 初始显示第一页
    showNext();

    // 滚动到底部加载更多
    var ticking = false;
    function onScroll() {
      if (allLoaded || ticking) return;
      ticking = true;
      window.requestAnimationFrame(function () {
        var rect = loadEl ? loadEl.getBoundingClientRect() : null;
        if (rect && rect.top <= window.innerHeight + 200) {
          showNext();
        }
        ticking = false;
      });
    }
    window.addEventListener("scroll", onScroll, { passive: true });

    // 点击"加载更多"手动加载
    if (loadEl) {
      loadEl.addEventListener("click", function () {
        showNext();
      });
    }

    // 初始时如果页面不满一屏，自动加载
    if (loadEl) {
      var r = loadEl.getBoundingClientRect();
      if (r.top <= window.innerHeight + 200) showNext();
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
