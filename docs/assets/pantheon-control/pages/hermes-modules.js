(function (global) {
  'use strict';

  function esc(value) {
    return String(value == null ? '' : value).replace(/[&<>"']/g, function (char) {
      return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char];
    });
  }
  function array(value) { return Array.isArray(value) ? value : []; }
  function bool(value) { return value === true ? 'oui' : value === false ? 'non' : 'inconnu'; }

  function state(label, value) {
    return '<div class="pm-state"><span>' + esc(label) + '</span><b>' + esc(value) + '</b></div>';
  }

  function card(item) {
    return '<article class="pm-module-card">' +
      '<h4>' + esc(item.name) + '</h4>' +
      '<p>' + esc(item.description || item.source || 'Élément observé.') + '</p>' +
      '<div class="pm-states">' +
        state('Détecté', bool(item.detected)) + state('Installé', bool(item.installed)) +
        state('Configuré', bool(item.configured)) + state('Hermes actif', bool(item.enabled)) +
        state('Santé', item.health || 'inconnue') + state('Usage tâche', 'non établi') +
      '</div></article>';
  }

  function normalize(data) {
    const p = data.payloads || {};
    const activeMemory = String((p.memory || {}).active || '').toLowerCase();
    const memory = array((p.memory || {}).providers).map(function (provider) {
      const name = provider.name || 'memory';
      return {name:name, description:provider.description, detected:provider.status !== 'missing', installed:provider.status !== 'missing', configured:provider.configured, enabled:String(name).toLowerCase() === activeMemory, health:'inconnue'};
    });
    const servers = new Map(array((p.servers || {}).servers).map(function (server) { return [String(server.name).toLowerCase(), server]; }));
    const mcps = array((p.catalog || {}).entries).map(function (entry) {
      const server = servers.get(String(entry.name).toLowerCase());
      return {name:entry.name, description:entry.description, source:entry.source, detected:Boolean(entry.installed || server), installed:Boolean(entry.installed || server), configured:array(entry.required_env).length ? null : Boolean(entry.installed || server), enabled:server ? server.enabled !== false : Boolean(entry.enabled), health:'inconnue'};
    });
    const plugins = array((p.hub || {}).plugins).map(function (plugin) {
      return {name:plugin.name, description:plugin.description, detected:true, installed:true, configured:null, enabled:plugin.runtime_status === 'enabled', health:'inconnue'};
    });
    const jobs = array(p.jobs).map(function (job) {
      const finite = Boolean(job.repeat && Number(job.repeat.times) > 0);
      return {name:job.name, description:'Planification native Hermes observée en lecture seule.', detected:true, installed:true, configured:finite, enabled:job.enabled !== false && job.state !== 'paused', health:job.last_status || 'jamais exécuté'};
    });
    return [{label:'Mémoire',items:memory},{label:'MCP & automatisation',items:mcps},{label:'Plugins Hermes',items:plugins},{label:'Opérations nocturnes',items:jobs}];
  }

  function render(data) {
    const meta = data.meta || {};
    const mode = meta.mode || 'unknown';
    const banner = '<div class="pm-source-banner"><div><strong>' + (meta.synthetic ? 'Démonstration — données fictives' : 'Hermes — données opérationnelles en lecture seule') + '</strong><p>' + esc(meta.notice || meta.source || '') + '</p></div><span class="pm-mode pm-mode-' + esc(mode) + '">' + esc(mode.toUpperCase()) + '</span></div>';
    const errors = array(data.errors).length ? '<div class="pm-error"><strong>Lecture partielle</strong><br>' + array(data.errors).map(esc).join('<br>') + '</div>' : '';
    const sections = normalize(data).map(function (section) {
      return '<section class="pm-section"><h3>' + esc(section.label) + '</h3><div class="pm-module-grid">' + (section.items.length ? section.items.map(card).join('') : '<p class="pm-empty">Aucun élément observé.</p>') + '</div></section>';
    }).join('');
    const toolbar = '<div class="pm-toolbar"><a href="?mode=demo">Forcer la démo</a><span class="hint">Le mode live ne peut être forcé que si le SDK Hermes est présent.</span></div>';
    return banner + errors + toolbar + sections + '<p class="pm-readonly">Cette page ne crée, n’active, ne désactive et ne déclenche rien. Hermes activé ≠ autorisation Pantheon.</p>';
  }

  async function start() {
    mountPage('Hermes Modules', 'Même interface et même contrat JSON : fixture synthétique sur GitHub Pages, lectures natives dans un hôte Hermes.', '<div class="panel"><p>Chargement de la source…</p></div>');
    try {
      const data = await global.PantheonHermesData.load();
      mountPage('Hermes Modules', 'Même interface et même contrat JSON : fixture synthétique sur GitHub Pages, lectures natives dans un hôte Hermes.', render(data));
    } catch (error) {
      mountPage('Hermes Modules', 'Source indisponible — aucun repli silencieux.', '<div class="pm-error"><strong>Impossible de charger les données.</strong><br>' + esc(error && error.message || error) + '</div>');
    }
  }

  global.renderHermesModulesPage = start;
})(window);
