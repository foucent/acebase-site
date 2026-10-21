/*
 * Unified boosting configurator for /boosting/.
 *
 * The whole game list, rank ladders and services live in
 * docs/assets/boosting/boosting.json. Adding a game means editing that file
 * only. Bump the ?v= literal below whenever the JSON changes so browsers do
 * not serve a cached copy.
 *
 * Kept in ES5 on purpose: mkdocs minifies JS during the build.
 */
(function () {
  "use strict";

  var root = document.querySelector("[data-boost-root]");
  if (!root) {
    return;
  }

  var DATA_URL = "/assets/boosting/boosting.json?v=20261021";

  var T = {
    from: "From $9.9",
    fallback: "Tell us your game, rank and server in chat and we will quote you.",
    defaultMsg: "Hi, I'd like a quote for game boosting. From $9.9.",
    hint: "Pick a desired rank above your current one, or tell us the climb in chat.",
    server: "Server"
  };

  var UNITS = {
    wins: "wins",
    hours: "hours",
    levels: "levels",
    credits: "credits",
    marks: "marks",
    tanks: "tanks",
    camos: "camos"
  };

  var ui = {
    games: root.querySelector("[data-boost-games]"),
    services: root.querySelector("[data-boost-services]"),
    fields: root.querySelector("[data-boost-fields]"),
    server: root.querySelector("[data-boost-server]"),
    options: root.querySelector("[data-boost-options]"),
    summary: root.querySelector("[data-boost-summary]"),
    hint: root.querySelector("[data-boost-hint]"),
    cta: root.querySelector("[data-boost-cta]"),
    note: root.querySelector("[data-boost-note]")
  };

  var state = {
    game: null,
    service: null,
    values: {},
    checks: {}
  };

  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) {
      node.className = cls;
    }
    if (text !== undefined && text !== null) {
      node.appendChild(document.createTextNode(String(text)));
    }
    return node;
  }

  function setRadio(box, value) {
    if (!box) {
      return;
    }
    var inputs = box.querySelectorAll("input[type=radio]");
    for (var i = 0; i < inputs.length; i++) {
      if (inputs[i].value === value) {
        inputs[i].checked = true;
        return;
      }
    }
  }

  function one(items, key, value) {
    for (var i = 0; i < items.length; i++) {
      if (items[i][key] === value) {
        return items[i];
      }
    }
    return null;
  }

  function fieldOptions(field) {
    if (!field) {
      return [];
    }
    if (field.options === "ranks") {
      return (state.game && state.game.ranks) || [];
    }
    return field.options || [];
  }

  function indexOfValue(list, value) {
    for (var i = 0; i < list.length; i++) {
      if (String(list[i]) === String(value)) {
        return i;
      }
    }
    return -1;
  }

  /* ---------------------------------------------------------------- chips */

  function renderGames() {
    if (!ui.games) {
      return;
    }
    ui.games.innerHTML = "";
    var games = state.data.games;
    for (var i = 0; i < games.length; i++) {
      (function (game) {
        var label = el("label", "ab-boost__chip");
        var input = document.createElement("input");
        input.type = "radio";
        input.name = "boost-game";
        input.value = game.key;
        input.addEventListener("change", function () {
          if (input.checked) {
            selectGame(game);
          }
        });
        label.appendChild(input);
        label.appendChild(el("span", "ab-boost__chip-text", game.name));
        ui.games.appendChild(label);
      }(games[i]));
    }
    if (games.length) {
      selectGame(games[0]);
    }
  }

  function renderServices() {
    if (!ui.services) {
      return;
    }
    ui.services.innerHTML = "";
    var services = (state.game && state.game.services) || [];
    for (var i = 0; i < services.length; i++) {
      (function (service) {
        var label = el("label", "ab-boost__chip");
        var input = document.createElement("input");
        input.type = "radio";
        input.name = "boost-service";
        input.value = service.key;
        input.addEventListener("change", function () {
          if (input.checked) {
            selectService(service);
          }
        });
        label.appendChild(input);
        label.appendChild(el("span", "ab-boost__chip-text", service.name));
        ui.services.appendChild(label);
      }(services[i]));
    }
    if (services.length) {
      selectService(services[0]);
    }
  }

  /* --------------------------------------------------------------- fields */

  function renderFields() {
    if (!ui.fields) {
      return;
    }
    ui.fields.innerHTML = "";
    state.values = {};
    var fields = (state.service && state.service.fields) || [];
    for (var i = 0; i < fields.length; i++) {
      var field = fields[i];
      var options = fieldOptions(field);
      if (!options.length) {
        continue;
      }
      var label = el("label", "ab-boost__field");
      label.appendChild(el("span", "ab-boost__field-label", field.label));
      var select = document.createElement("select");
      select.setAttribute("data-boost-field", field.key);
      for (var j = 0; j < options.length; j++) {
        var option = document.createElement("option");
        option.value = String(options[j]);
        option.appendChild(document.createTextNode(String(options[j])));
        select.appendChild(option);
      }
      var start = 0;
      if (field.key === "to" && options.length > 1) {
        start = Math.floor(options.length / 2);
      }
      select.selectedIndex = start;
      state.values[field.key] = select.value;
      select.addEventListener("change", function (key) {
        return function (event) {
          state.values[key] = event.target.value;
          update();
        };
      }(field.key));
      label.appendChild(select);
      ui.fields.appendChild(label);
    }
    renderServer();
  }

  function renderServer() {
    if (!ui.server) {
      return;
    }
    ui.server.innerHTML = "";
    state.values.server = "";
    var servers = (state.game && state.game.servers) || [];
    if (!servers.length) {
      return;
    }
    var label = el("label", "ab-boost__field");
    label.appendChild(el("span", "ab-boost__field-label", T.server));
    var select = document.createElement("select");
    select.setAttribute("data-boost-field", "server");
    for (var i = 0; i < servers.length; i++) {
      var option = document.createElement("option");
      option.value = servers[i];
      option.appendChild(document.createTextNode(servers[i]));
      select.appendChild(option);
    }
    state.values.server = select.value;
    select.addEventListener("change", function (event) {
      state.values.server = event.target.value;
      update();
    });
    label.appendChild(select);
    ui.server.appendChild(label);
  }

  function renderOptions() {
    if (!ui.options) {
      return;
    }
    ui.options.innerHTML = "";
    state.checks = {};
    var options = (state.service && state.service.options) || [];
    for (var i = 0; i < options.length; i++) {
      (function (value) {
        var label = el("label", "ab-boost__opt");
        var input = document.createElement("input");
        input.type = "checkbox";
        input.value = value;
        input.addEventListener("change", function () {
          state.checks[value] = !!input.checked;
          update();
        });
        label.appendChild(input);
        label.appendChild(el("span", "ab-boost__opt-text", value));
        ui.options.appendChild(label);
      }(options[i]));
    }
  }

  /* ------------------------------------------------------------ selection */

  function selectGame(game) {
    state.game = game;
    setRadio(ui.games, game.key);
    renderServices();
  }

  function selectService(service) {
    state.service = service;
    setRadio(ui.services, service.key);
    renderFields();
    renderOptions();
    update();
  }

  /* ---------------------------------------------------------------- paint */

  function update() {
    if (!state.game || !state.service) {
      return;
    }

    var bits = [];
    var parts = [state.game.name, state.service.name];
    var fromField = null;
    var toField = null;
    var fields = state.service.fields || [];

    for (var i = 0; i < fields.length; i++) {
      if (fields[i].key === "from") {
        fromField = fields[i];
      } else if (fields[i].key === "to") {
        toField = fields[i];
      }
    }

    if (fromField && toField) {
      var fromValue = state.values.from;
      var toValue = state.values.to;
      if (fromValue && toValue) {
        bits.push(fromValue + " to " + toValue);
        parts.push(fromValue + " → " + toValue);
      }
    } else if (fromField && state.values.from) {
      bits.push(state.values.from);
      parts.push(state.values.from);
    }

    for (var j = 0; j < fields.length; j++) {
      var field = fields[j];
      if (field.key === "from" || field.key === "to") {
        continue;
      }
      var value = state.values[field.key];
      if (value === undefined || value === "") {
        continue;
      }
      var text = UNITS[field.key] ? value + " " + UNITS[field.key] : String(value);
      bits.push(text);
      parts.push(text);
    }

    if (state.values.server) {
      bits.push("server " + state.values.server);
      parts.push(state.values.server);
    }

    var options = (state.service.options) || [];
    for (var k = 0; k < options.length; k++) {
      if (state.checks[options[k]]) {
        bits.push(options[k]);
        parts.push(options[k]);
      }
    }

    if (ui.summary) {
      ui.summary.textContent = parts.join(" · ") + " · " + T.from;
    }
    if (ui.note) {
      ui.note.textContent = state.game.note || "";
    }

    var message = "Hi, I'd like a quote for " + state.game.name + " " +
      state.service.name + ": " + bits.join(", ") + ". From $9.9.";

    var blocked = false;
    if (fromField && toField && state.values.from && state.values.to) {
      var ladder = fieldOptions(fromField);
      var fromIndex = indexOfValue(ladder, state.values.from);
      var toIndex = indexOfValue(fieldOptions(toField), state.values.to);
      blocked = fromIndex >= 0 && toIndex >= 0 && toIndex <= fromIndex;
    }

    if (ui.hint) {
      ui.hint.textContent = blocked ? T.hint : "";
    }
    if (ui.cta) {
      ui.cta.setAttribute("data-crisp-msg", message);
      if (blocked) {
        ui.cta.classList.remove("ab-crisp-open");
        ui.cta.setAttribute("aria-disabled", "true");
      } else {
        ui.cta.classList.add("ab-crisp-open");
        ui.cta.removeAttribute("aria-disabled");
      }
    }
  }

  /* ------------------------------------------------------------- fallback */

  function fallback() {
    if (ui.games) {
      ui.games.innerHTML = "";
    }
    if (ui.services) {
      ui.services.innerHTML = "";
    }
    if (ui.fields) {
      ui.fields.innerHTML = "";
    }
    if (ui.server) {
      ui.server.innerHTML = "";
    }
    if (ui.options) {
      ui.options.innerHTML = "";
    }
    if (ui.summary) {
      ui.summary.textContent = T.fallback;
    }
    if (ui.hint) {
      ui.hint.textContent = "";
    }
    if (ui.note) {
      ui.note.textContent = "";
    }
    if (ui.cta) {
      ui.cta.setAttribute("data-crisp-msg", T.defaultMsg);
      ui.cta.classList.add("ab-crisp-open");
      ui.cta.removeAttribute("aria-disabled");
    }
  }

  /* ----------------------------------------------------------------- boot */

  function boot(doc) {
    var games = (doc && doc.games) || [];
    if (!games.length) {
      fallback();
      return;
    }
    state.data = doc;
    renderGames();
  }

  if (typeof fetch !== "function") {
    fallback();
    return;
  }

  fetch(DATA_URL)
    .then(function (response) {
      if (!response.ok) {
        throw new Error("boosting.json " + response.status);
      }
      return response.json();
    })
    .then(boot)
    .catch(fallback);
}());
