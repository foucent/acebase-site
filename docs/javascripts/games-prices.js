(function () {
  "use strict";

  // AceBase games: fetch shared prices.json and render it into whichever of the
  // two shapes the page asks for — the full official-vs-AceBase comparison
  // table on each .mg-games__price-table[data-game] block, or the one-line-per-
  // tier ladder on each .ab-ec-list[data-game] block.

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
    // Prices in prices.json are already USD, which is the only currency the
    // site displays — so this is a straight format, not a conversion.
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

  // The one-line-per-tier price block. Lowest is the price that matters here:
  // the whole site's pitch is finding it. Rows keep their source order, which
  // groups tiers by product line rather than by price — re-sorting would break
  // that grouping.
  //
  // It has two shapes, and the markup differs enough that the container has to
  // pick one rather than a stylesheet adapting a single shape:
  //
  //   ladder — "100 G-COIN / $0.86." in a row, on the article and price-band
  //            pages that show the headline price rather than the full range.
  //            The name is bare text and the separator is its own span.
  //   card   — the same pair as the two cells of .ab-card--ec's label/price
  //            grid. There the row gives up its box (.ab-ec-item is
  //            `display: contents`) so the *label and price* are what the grid
  //            places: a bare text node would become an anonymous grid item and
  //            the "/" would take a column of its own.
  //
  // Both keep the trailing period, because the GPU pages bake it into their
  // static rows and a rendered row without one would be the only row on the
  // site that reads differently. Where it sits follows the same split: inside
  // .ab-ec-price on a card (as in "$419." there), outside it on the ladder.
  function renderEcList(gameKey, rows, updated) {
    var wrap = $('.ab-ec-list[data-game="' + gameKey + '"]');
    if (!wrap) return;

    var updEl = $("#" + gameKey + "-updated");
    if (updEl && updated) updEl.textContent = updated;

    // prices.json holds two row shapes. The official-vs-AceBase one carries no
    // `lowest`, and money(undefined) would print "$NaN" — so it is treated as
    // no data rather than rendered. No page lists one of those games today.
    if (!rows || !rows.length || rows[0].lowest == null) {
      wrap.innerHTML = '<span class="ab-ec-loading">' + T.emptySoon + "</span>";
      return;
    }

    var isCard = !!wrap.closest(".ab-card--ec");

    // Two sources, because the two kinds of saving are not the same thing. The
    // gift cards carry `data-discount`: the source's own list-price discount,
    // printed verbatim and never recomputed off the tier prices, because it
    // describes the whole card against a list price that is not in prices.json
    // at all (PSN's -40% is not the difference between any two numbers on its
    // card). The live-platform cards carry `off` on their entry row instead:
    // that saving *is* list against reference, it moves every time the FX is
    // re-run, and typing it onto the card would leave the page quoting a stale
    // number. Cards with neither get an empty string.
    var off = wrap.getAttribute("data-discount") || (rows[0] && rows[0].off) || "";

    wrap.innerHTML = rows
      .map(function (r, i) {
        var label = esc(r.title || T.topup);
        var price = money(r.lowest);
        // Entry tier only: a card holds one saving figure and sixteen of them
        // down the ladder is noise.
        //
        // It goes *inside* .ab-ec-price rather than beside it. In the card shape
        // .ab-ec-item is `display: contents`, so a third child would be placed
        // by the grid as a cell of its own and land in column one of the next
        // row; under 390px the row turns flex and it would crowd in there
        // instead. Nested here, the grid still sees exactly two cells.
        var pill = (i === 0 && off)
          ? '<span class="ab-ec-off">' + esc(off) + "</span>"
          : "";

        if (isCard) {
          return (
            '<span class="ab-ec-item">' +
            '<span class="ab-ec-label">' + label + "</span>" +
            '<span class="ab-ec-price">' + price + pill + ".</span>" +
            "</span>"
          );
        }

        return (
          '<span class="ab-ec-item">' +
          label +
          '<span class="ab-ec-sep">/</span>' +
          '<span class="ab-ec-price">' + price + pill + "</span>" +
          ".</span>"
        );
      })
      .join("<br>");
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
    var ecLists = $all(".ab-ec-list[data-game]");
    if (!tables.length && !ecLists.length) return;

    var games = {};
    var updated = "";
    var failed = false;

    function renderAll() {
      if (failed) {
        tables.forEach(function (t) {
          t.innerHTML = '<p class="mg-games__empty">' + T.emptyErr + "</p>";
        });
        ecLists.forEach(function (l) {
          l.innerHTML = '<span class="ab-ec-loading">' + T.emptyErr + "</span>";
        });
        return;
      }
      // The overview's own date, and every article's, come from the data file:
      // the page is hand-written, so a literal date would be stale the next
      // time prices.json is merged.
      if (updated) {
        $all(".js-prices-updated").forEach(function (el) {
          el.textContent = updated;
        });
      }
      tables.forEach(function (t) {
        var key = t.getAttribute("data-game");
        renderGame(key, games[key], updated);
      });
      ecLists.forEach(function (l) {
        var key = l.getAttribute("data-game");
        renderEcList(key, games[key], updated);
      });
    }

    // Cache-bust so a stale browser copy of prices.json can never show an old
    // schema (e.g. official/AceBase) after the site is rebuilt. Bump the
    // version to match prices.json "updated" when new data is merged — a stale
    // copy is served silently, so a bump missed here shows a returning reader
    // the *old* file, which for a newly added key means 价格即将上线 until their
    // cache happens to turn over.
    fetch("/assets/games/prices.json?v=" + (window.AceBasePricesVer || "20260921"))
      .then(function (r) {
        if (!r.ok) throw new Error("http " + r.status);
        return r.json();
      })
      .then(function (data) {
        games = (data && data.games) || {};
        updated = (data && data.updated) || "";
        renderAll();
      })
      .catch(function (err) {
        console.warn("[AceBase] prices.json not loaded:", err.message);
        failed = true;
        renderAll();
      });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
