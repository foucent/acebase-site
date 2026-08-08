/**
 * Steam Game Account rental — two-stage selector (eldorado-style).
 * Stage 1: pick a game from the grid. Stage 2: show that game's offer.
 */
(function () {
  var GAMES = [
    { name: "Solo Leveling: ARISE OVERDRIVE", icon: "Solo-leveling_-arise-overdrive.png", price: 14.90 },
    { name: "DayZ", icon: "DayZ.png", price: 11.50 },
    { name: "Rust", icon: "Rust.png", price: 5.75 },
    { name: "Dispatch", icon: "Dispatch.png", price: 1.98 },
    { name: "Escape From Duckov", icon: "Escape-From-Duckov.png", price: 5.55 },
    { name: "RV There Yet?", icon: "RV-There-Yet.png", price: 2.90 },
    { name: "Baldur's Gate 3", icon: "Baldur's-Gate-3.png", price: 2.00 },
    { name: "Don't Starve Together", icon: "Don't-Starve-Together.png", price: 0.50 },
    { name: "Dead By Daylight", icon: "Dead-by-Daylight.png", price: 3.92 },
    { name: "The Outer Worlds 2", icon: "The-Outer-Worlds-2.png", price: 29.13 },
    { name: "Arc Raiders", icon: "Arc-Raiders.png", price: 19.82 },
    { name: "Call of Duty: Black Ops 7", icon: "Call-of-Duty-BO7.png", price: 25.27 },
    { name: "Anno 117: Pax Romana", icon: "Anno-117-pax-romana.png", price: 19.90 },
    { name: "Constance", icon: "Constance.png", price: 6.50 },
    { name: "Of Ash and Steel", icon: "Of-ash-and-steel.png", price: 7.39 },
    { name: "SpongeBob SquarePants: Titans of the Tide", icon: "Spongebob-squarepants-titans-of-the-tide.png", price: 15.89 },
    { name: "TORMENTOR", icon: "tormentor.png", price: 4.85 },
    { name: "Escape from Tarkov", icon: "Escape-From-Tarkov.png", price: 12.39 },
    { name: "EA FC 26", icon: "FC-25.png", price: 3.54 },
    { name: "Sea of Thieves", icon: "Sea-of-Thieves.png", price: 4.50 },
    { name: "Battlefield 6", icon: "Battlefield-6.png", price: 11.50 },
    { name: "Ready or Not", icon: "Ready-or-Not.png", price: 5.00 },
    { name: "Cyberpunk 2077", icon: "Cyberpunk-2077.png", price: 1.89 },
    { name: "Stardew Valley", icon: "Stardew-Valley.png", price: 2.24 },
    { name: "Peak", icon: "PEAK.png", price: 1.70 },
    { name: "Counter-Strike 2 - Active Prime", icon: "cs-2-prime.png", price: 10.49 },
    { name: "Euro Truck Simulator 2", icon: "ets2.png", price: 1.45 },
    { name: "Path of Exile 2", icon: "poe2.png", price: 13.15 },
    { name: "Diablo IV", icon: "diablo4.png", price: 12.49 },
    { name: "Nioh 3", icon: "Nioh-3.png", price: 30.99 },
    { name: "Resident Evil Requiem", icon: "RE.png", price: 9.99 },
    { name: "Crimson Desert", icon: "Crmsondsrt.png", price: 16.99 },
  ];

  function money(n) {
    // Prices are USD; format via the header currency switcher.
    return window.AceBaseCurrency
      ? window.AceBaseCurrency.formatFromBase(n)
      : "$" + (Math.round(n * 100) / 100).toFixed(n % 1 ? 2 : 0);
  }

  function esc(s) {
    return String(s || "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  var PAGE_SIZE = 8;
  var currentPage = 0;

  var LANG = (document.documentElement.lang || "en").toLowerCase();
  var isZh = LANG.indexOf("zh") === 0;
  var SUB_LABEL = isZh ? "Steam 游戏账号" : "Steam Game Account";

  function buildGrid() {
    var grid = document.getElementById("steam-game-grid");
    if (!grid) return;
    renderList();
  }

  function renderList() {
    var grid = document.getElementById("steam-game-grid");
    if (!grid) return;

    var totalPages = Math.ceil(GAMES.length / PAGE_SIZE);
    if (currentPage >= totalPages) currentPage = totalPages - 1;
    if (currentPage < 0) currentPage = 0;

    var start = currentPage * PAGE_SIZE;
    var end = Math.min(start + PAGE_SIZE, GAMES.length);
    var pageGames = GAMES.slice(start, end);

    grid.innerHTML = pageGames.map(function (g) {
      return (
        '<div class="mg-games__game-row">' +
        '<span class="mg-games__game-icon"><img src="/assets/games/steam/' + g.icon + '" alt="' + esc(g.name) + '" width="36" height="36" loading="lazy"></span>' +
        '<span class="mg-games__game-meta">' +
        '<span class="mg-games__game-name">' + esc(g.name) + '</span>' +
        '<span class="mg-games__game-sub">' + SUB_LABEL + "</span>" +
        "</span>" +
        '<span class="mg-games__game-price">' + money(g.price) + '</span>' +
        "</div>"
      );
    }).join("");

    renderPager(totalPages);
  }

  function renderPager(totalPages) {
    var pager = document.getElementById("steam-game-pager");
    if (!pager) return;

    if (totalPages <= 1) {
      pager.innerHTML = "";
      return;
    }

    var html = '<div class="mg-games__pager">';
    html +=
      '<button type="button" class="mg-games__pager-btn" data-page="' + (currentPage - 1) + '"' +
      (currentPage === 0 ? " disabled" : "") + ">&lsaquo;</button>";

    for (var p = 0; p < totalPages; p++) {
      html +=
        '<button type="button" class="mg-games__pager-btn' + (p === currentPage ? " is-active" : "") + '" data-page="' + p + '">' +
        (p + 1) + "</button>";
    }

    html +=
      '<button type="button" class="mg-games__pager-btn" data-page="' + (currentPage + 1) + '"' +
      (currentPage >= totalPages - 1 ? " disabled" : "") + ">&rsaquo;</button>";
    html += "</div>";

    pager.innerHTML = html;

    pager.querySelectorAll(".mg-games__pager-btn").forEach(function (btn) {
      if (btn.disabled) return;
      btn.addEventListener("click", function () {
        var target = parseInt(btn.getAttribute("data-page"), 10);
        if (target >= 0 && target < totalPages) {
          currentPage = target;
          renderList();
        }
      });
    });
  }

  function bind() {
    buildGrid();
    // Re-render prices when the header currency switcher changes.
    if (window.AceBaseCurrency && window.AceBaseCurrency.onChange) {
      window.AceBaseCurrency.onChange(function () {
        renderList();
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bind);
  } else {
    bind();
  }
})();
