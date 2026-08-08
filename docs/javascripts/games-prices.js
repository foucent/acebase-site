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

  var LANG = (document.documentElement.lang || "en").toLowerCase();
  var isZh = LANG.indexOf("zh") === 0;
  var T = {
    amount: isZh ? "档位" : "Amount",
    lowest: isZh ? "最低" : "Lowest",
    highest: isZh ? "最高" : "Highest",
    average: isZh ? "平均" : "Average",
    official: isZh ? "官方" : "Official",
    acebase: "AceBase",
    discount: isZh ? "折扣" : "Discount",
    topup: isZh ? "充值" : "Top-Up",
    emptySoon: isZh
      ? "价格即将上线 — 请咨询在线客服获取最新报价。"
      : "Prices coming soon — ask our chat for the latest quote.",
    emptyErr: isZh
      ? "价格暂时不可用 — 请咨询在线客服获取最新报价。"
      : "Prices temporarily unavailable — ask our chat for the latest quote.",
  };

  function money(n) {
    // Prices in prices.json are USD; format via the header currency switcher.
    return window.AceBaseCurrency
      ? window.AceBaseCurrency.formatFromBase(n)
      : "$" + (Math.round(n * 100) / 100).toFixed(2);
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
      wrap.innerHTML = '<p class="mg-games__empty">' + T.emptySoon + "</p>";
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
        "<th>" + T.amount + "</th><th>" + T.lowest + "</th><th>" + T.highest + "</th><th>" + T.average + "</th>" +
        "</tr></thead><tbody>";
      rows.forEach(function (r) {
        var title = esc(r.title || T.topup);
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
      "<th>" + T.amount + "</th><th>" + T.official + "</th><th>" + T.acebase + "</th><th>" + T.discount + "</th>" +
      "</tr></thead><tbody>";
    rows.forEach(function (r) {
      var title = esc(r.title || T.topup);
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

    var games = {};
    var updated = "";
    var failed = false;
    var loaded = false;

    function renderAll() {
      if (failed) {
        tables.forEach(function (t) {
          t.innerHTML = '<p class="mg-games__empty">' + T.emptyErr + "</p>";
        });
        return;
      }
      tables.forEach(function (t) {
        var key = t.getAttribute("data-game");
        renderGame(key, games[key], updated);
      });
    }

    fetch("/assets/games/prices.json")
      .then(function (r) {
        if (!r.ok) throw new Error("http " + r.status);
        return r.json();
      })
      .then(function (data) {
        games = (data && data.games) || {};
        updated = (data && data.updated) || "";
        loaded = true;
        renderAll();
      })
      .catch(function (err) {
        console.warn("[AceBase] prices.json not loaded:", err.message);
        failed = true;
        renderAll();
      });

    // Re-render prices when the header currency switcher changes.
    if (window.AceBaseCurrency && window.AceBaseCurrency.onChange) {
      window.AceBaseCurrency.onChange(function () {
        if (loaded) renderAll();
      });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
