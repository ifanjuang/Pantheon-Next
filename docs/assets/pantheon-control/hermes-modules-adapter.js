/* One read-only data contract, two explicit sources.
   GitHub Pages loads a synthetic JSON fixture. A Hermes host exposing the
   audited dashboard SDK loads native data. Live failures never fall back to demo. */
(function (global) {
  'use strict';

  const API_CALLS = [
    ['memory', 'getMemory'],
    ['catalog', 'getMcpCatalog'],
    ['servers', 'getMcpServers'],
    ['hub', 'getPluginsHub'],
    ['jobs', 'getCronJobs', 'all'],
  ];

  function requestedMode() {
    const value = new URLSearchParams(global.location.search).get('mode');
    return value === 'demo' || value === 'live' ? value : 'auto';
  }

  function sdk() {
    return global.__HERMES_PLUGIN_SDK__ || null;
  }

  function resolveMode() {
    const requested = requestedMode();
    if (requested === 'demo') return 'demo';
    if (requested === 'live' && !sdk()) {
      throw new Error('Mode live demandé, mais le SDK Hermes est absent. Aucun repli vers les données de démonstration.');
    }
    return sdk() ? 'live' : 'demo';
  }

  function callHermes(name) {
    const current = sdk();
    const fn = current && current.api && current.api[name];
    if (typeof fn !== 'function') {
      return Promise.reject(new Error('Méthode Hermes indisponible : ' + name));
    }
    return Promise.resolve(fn.apply(current.api, Array.prototype.slice.call(arguments, 1)));
  }

  async function loadLive() {
    const results = await Promise.allSettled(API_CALLS.map(function (entry) {
      return callHermes.apply(null, [entry[1]].concat(entry.slice(2)));
    }));
    const payloads = {memory: {}, catalog: {}, servers: {}, hub: {}, jobs: []};
    const errors = [];
    results.forEach(function (result, index) {
      const key = API_CALLS[index][0];
      if (result.status === 'fulfilled') payloads[key] = result.value || payloads[key];
      else errors.push(key + ': ' + String(result.reason && result.reason.message || result.reason));
    });
    if (errors.length === API_CALLS.length) {
      throw new Error('Toutes les lectures Hermes ont échoué : ' + errors.join(' · '));
    }
    return {
      schema_version: 'pantheon.hermes-dashboard.v1',
      meta: {mode: errors.length ? 'live_partial' : 'live', synthetic: false, source: 'Hermes dashboard SDK'},
      payloads: payloads,
      errors: errors,
    };
  }

  async function loadDemo() {
    const response = await fetch('hermes-modules-demo.json', {cache: 'no-store'});
    if (!response.ok) throw new Error('Fixture de démonstration indisponible (' + response.status + ').');
    const data = await response.json();
    if (!data.meta || data.meta.synthetic !== true) {
      throw new Error('Fixture refusée : meta.synthetic doit être true.');
    }
    return data;
  }

  async function load() {
    const mode = resolveMode();
    return mode === 'live' ? loadLive() : loadDemo();
  }

  global.PantheonHermesData = Object.freeze({load: load, resolveMode: resolveMode});
})(window);
