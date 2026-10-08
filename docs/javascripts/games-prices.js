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
    spec: isZh ? "规格" : "Spec",
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

  // The third shape is the spec picker, on the /cdkeys/ cards that carry
  // ab-card--picker. It is built where the ladder would have been: one labelled
  // <select>, one option per tier, on the model of mygear.top's /rubbers/ card.
  //
  // One thing does not carry over. rubbers' options are colours and share a
  // single price, so its title price never moves; these tiers are priced one
  // by one, which is the whole reason the page exists, so the title's inline
  // price is the *chosen* tier's and follows the select. The quote message
  // follows it too — a reader who has picked a denomination should not have to
  // repeat it to the chat.
  //
  // The original message is copied into data-crisp-base on the first pass, so
  // switching tiers twice cannot append the spec twice. crisp.js reads
  // data-crisp-msg at click time rather than at load, which is what lets it be
  // rewritten here at all.
  function renderPicker(wrap, card, rows) {
    var head = card.querySelector(".ab-card__title .ab-card__price");
    var buy = card.querySelector(".ab-fold__buy");
    if (buy && !buy.getAttribute("data-crisp-base")) {
      buy.setAttribute("data-crisp-base", buy.getAttribute("data-crisp-msg") || "");
    }
    var base = buy ? buy.getAttribute("data-crisp-base") : "";

    wrap.innerHTML =
      '<label class="ab-ec-pick">' +
      '<span class="ab-ec-pick__label">' + esc(T.spec) + "</span>" +
      '<select class="ab-ec-pick__select">' +
      rows
        .map(function (r) {
          return "<option>" + esc(r.title || T.topup) + "</option>";
        })
        .join("") +
      "</select></label>";

    var sel = wrap.querySelector("select");

    // selectedIndex rather than the option's text: the rows are the source of
    // truth and the label is only what they are called.
    function sync() {
      var r = rows[sel.selectedIndex] || rows[0];
      if (head) head.textContent = money(r.lowest);
      if (buy && base) {
        buy.setAttribute(
          "data-crisp-msg",
          base.replace(/[。.]\s*$/, "") + "，规格 " + r.title + "。"
        );
      }
    }

    sel.addEventListener("change", sync);
    sync();
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

    // The entry price again, inline at the end of the card's title. It has to be
    // scripted: the title's hypothetical width is the whole line, so the CSS
    // route would push the price onto a line of its own rather than into the
    // end of the title, and the plate cards are the ones that show it. Filled
    // here rather than in renderAll so the no-data branch above — which returns
    // before this point — is what keeps money(undefined)'s "$NaN" off the
    // title. `rows[0].lowest`, not a minimum over the rows: on every key in
    // prices.json they are the same number, and rows[0] is the tier the ladder
    // paints red, so the two figures are guaranteed to agree.
    //
    // On failure the fetch callback never gets here, the span stays empty, and
    // :empty in uncrate.css keeps it out of the layout.
    var card = wrap.closest(".ab-card");
    var head = card && card.querySelector(".ab-card__title .ab-card__price");
    if (head) head.textContent = money(rows[0].lowest);

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

    // The saving belongs on the corner badge, and on the live-platform cards
    // the badge is the only place it can be written — the markup has no
    // `data-discount` to copy, so the channel tag it ships with stands in until
    // the number exists. Filled here rather than in the markup for the same
    // reason the entry price is, and only when the badge is not already wearing
    // the saving: `--off` is the flag uncrate.css paints green, and the nine
    // hand-written badges carry it from the start.
    var badge = card && card.querySelector(".ab-card__badge");
    if (badge && off && !badge.classList.contains("ab-card__badge--off")) {
      badge.textContent = off;
      badge.classList.add("ab-card__badge--off");
    }

    // /cdkeys/ draws a picker where the other price pages draw a ladder. Taken
    // after the badge, not before the title price, so the saving still lands on
    // a card whose own markup has no data-discount to copy — returning early
    // from above would leave those cards wearing their channel tag with the
    // number already in hand.
    if (card && card.classList.contains("ab-card--picker")) {
      renderPicker(wrap, card, rows);
      return;
    }

    // /figures/ draws neither picker nor ladder: each card is one piece at one
    // price, and that price is the entry figure already written into the title
    // by the block above. The block is emptied rather than left holding its
    // 「正在加载最新价格…」 placeholder — a card that ships a loading line and
    // is never given rows of its own would read as a page that failed to load.
    //
    // It is a branch of its own rather than a reuse of --picker because the two
    // answer different questions: the picker has rows a reader chooses between
    // (denominations, specs), and these have exactly one. `return` before the
    // ladder, and after the badge, so an --figure card with a data-discount
    // would still get its corner tag.
    if (card && card.classList.contains("ab-card--figure")) {
      wrap.innerHTML = "";
      return;
    }

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
        //
        // On the plate cards uncrate.css hides it — the badge above carries the
        // same number, and at three columns the 74px pill was what pushed the
        // entry row onto a second line. It is kept in the markup rather than
        // dropped so a ladder that is not a plate still gets it, and so the
        // badge's takeover stays one `display: none` to reverse.
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
    fetch("/assets/games/prices.json?v=" + (window.AceBasePricesVer || "20261009"))
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
