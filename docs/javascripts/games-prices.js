(function () {
  "use strict";

  // AceBase games hub: fetch shared prices.json and render the official-vs-AceBase
  // comparison table on each .mg-games__price-table[data-game] block.

  function $(sel, root) {
    return (root || document).querySelector(sel);
  }

  function $all(sel, root) {
    return Array.prototype.slice.call((root || document).querySelectorAll(sel));
  }

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

  function offPct(official, acebase) {
    if (!(official > 0)) return "";
    var pct = Math.round((1 - acebase / official) * 100);
    if (pct <= 0) return "";
    return pct + "% OFF";
  }

  function renderGame(gameKey, rows, updated) {
    var wrap = $('.mg-games__price-table[data-game="' + gameKey + '"]');
    if (!wrap) return;

    var updEl = $("#" + gameKey + "-updated");
    if (updEl && updated) updEl.textContent = updated;

    if (!rows || !rows.length) {
      wrap.innerHTML =
        '<p class="mg-games__empty">Prices coming soon — ask our chat for the latest quote.</p>';
      return;
    }

    // Price-range schema: rows have {title, lowest, highest, average} ->
    // 4-column table (Amount / Lowest / Highest / Average).
    // Official-vs-AceBase schema: rows have {title, official, acebase} ->
    // 3-column table (Amount / Official / AceBase / Discount).
    var isRange = rows.some(function (r) {
      return r.lowest != null && r.highest != null && r.average != null;
    });

    var html;
    if (isRange) {
      html =
        '<table class="mg-games__table">' +
        "<thead><tr>" +
        "<th>Amount</th><th>Lowest</th><th>Highest</th><th>Average</th>" +
        "</tr></thead><tbody>";
      rows.forEach(function (r) {
        var title = esc(r.title || "Top-Up");
        html +=
          "<tr>" +
          "<td>" + title + "</td>" +
          '<td class="mg-games__td-lowest">' + money(r.lowest) + "</td>" +
          '<td class="mg-games__td-highest">' + money(r.highest) + "</td>" +
          '<td class="mg-games__td-average">' + money(r.average) + "</td>" +
          "</tr>";
      });
      html += "</tbody></table>";
      wrap.innerHTML = html;
      return;
    }

    html =
      '<table class="mg-games__table">' +
      "<thead><tr>" +
      "<th>Amount</th><th>Official</th><th>AceBase</th><th>Discount</th>" +
      "</tr></thead><tbody>";
    rows.forEach(function (r) {
      var title = esc(r.title || "Top-Up");
      var official = money(r.official);
      var acebase = money(r.acebase);
      var off = esc(offPct(r.official, r.acebase));
      html +=
        "<tr>" +
        "<td>" + title + "</td>" +
        '<td class="mg-games__td-official">' + official + "</td>" +
        '<td class="mg-games__td-acebase">' + acebase + "</td>" +
        '<td class="mg-games__td-off">' + off + "</td>" +
        "</tr>";
    });
    html += "</tbody></table>";
    wrap.innerHTML = html;
  }

  function init() {
    var tables = $all(".mg-games__price-table[data-game]");
    if (!tables.length) return;

    fetch("/assets/games/prices.json")
      .then(function (r) {
        if (!r.ok) throw new Error("http " + r.status);
        return r.json();
      })
      .then(function (data) {
        var games = (data && data.games) || {};
        var updated = (data && data.updated) || "";
        tables.forEach(function (t) {
          var key = t.getAttribute("data-game");
          renderGame(key, games[key], updated);
        });
      })
      .catch(function (err) {
        console.warn("[AceBase] prices.json not loaded:", err.message);
        tables.forEach(function (t) {
          t.innerHTML =
            '<p class="mg-games__empty">Prices temporarily unavailable — ask our chat for the latest quote.</p>';
        });
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
