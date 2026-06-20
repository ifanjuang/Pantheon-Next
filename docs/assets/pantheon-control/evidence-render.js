// Pure markup builders for the points-de-controle card stack. No fetch, no
// state mutation — everything here takes data in and returns an HTML string.

function escEv(s) {
  return String(s ?? '').replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' }[m]));
}

const EVIDENCE_ICONS = {
  geo: '<circle cx="12" cy="12" r="7"/><path d="M12 3v18M3 12h18"/>',
  structure: '<path d="M4 20h16M6 20V9l6-5 6 5v11M9 20v-7h6v7"/>',
  budget: '<path d="M15 6c-5-2-9 1-9 6s4 8 9 6M4 10h10M4 14h10"/>',
  floor: '<path d="M4 6h16M4 12h16M4 18h16M8 6v12M16 6v12"/>',
  alert: '<path d="M12 4l9 16H3zM12 9v5M12 17h.01"/>',
  med: '<path d="M12 5v14M5 12h14"/><circle cx="12" cy="12" r="8"/>',
  cvc: '<path d="M4 12h16M8 8l-4 4 4 4M16 8l4 4-4 4"/>',
  heritage: '<path d="M4 20h16M6 20V9l6-5 6 5v11M8 12h8"/>',
  section: '<path d="M5 19L19 5M6 6h12v12H6z"/>',
  fire: '<path d="M12 21c4-2 5-5 3-8-1-2-3-3-3-6-3 3-6 6-3 11"/>',
  legal: '<path d="M12 4v16M6 8h12M8 8l-3 6h6zM16 8l-3 6h6z"/>',
  camera: '<path d="M4 8h5l1-2h4l1 2h5v10H4z"/><circle cx="12" cy="13" r="3"/>',
  plans: '<path d="M4 5h16v14H4zM8 5v14M4 10h16"/>',
  shield: '<path d="M12 3l7 3v5c0 5-3 8-7 10-4-2-7-5-7-10V6z"/>',
};

function evidenceIcon(k) {
  const d = EVIDENCE_ICONS[k] || '<circle cx="12" cy="12" r="7"/>';
  return '<span class="ico"><svg viewBox="0 0 24 24">' + d + '</svg></span>';
}

function evidenceChips(c) {
  return '<div class="chips">' + c.labels.map(x => '<span class="chip">' + escEv(x) + '</span>').join('') + '</div>';
}

function evidenceSources(c) {
  return c.src.map(s =>
    '<div class="src"><b>' + s[0] + ' · ' + escEv(s[3]) + '</b>' +
    '<span>' + escEv(s[1]) + ' · Date ' + s[2] + ' · Indice ' + escEv(s[4]) + '</span>' +
    '<span>Force ' + escEv(s[5]) + ' · Statut ' + escEv(s[6]) + '</span>' +
    '<code>MD ' + escEv(s[7]) + ' · PDF ' + escEv(s[8]) + '</code></div>'
  ).join('');
}

// relations: [{type, direction, target, label}]
function evidenceDeps(c) {
  const byDir = dir => c.relations.find(r => r.direction === dir);
  const rows = [
    ['Amont', byDir('upstream')],
    ['Aval', byDir('downstream')],
    ['Même', byDir('peer')],
  ];
  return rows.map(([titleLabel, r]) =>
    '<button class="dep" data-goto="' + escEv(r ? r.target : '') + '"><b>' + titleLabel + '</b>' +
    '<span>' + escEv(r ? r.label : '—') + '</span>' +
    '<code>' + escEv(r ? r.target : '—') + '</code></button>'
  ).join('');
}

function evidenceCard(c, pi, project) {
  return '<article class="swiper-slide sSlide"><div class="card ' + (c.risk === 'Critique' ? 'crit' : '') + '" data-p="' + pi + '" data-id="' + c.id + '">' +
    '<div class="top"><div class="meta">' + escEv(project.name.toUpperCase()) + ' · ' + escEv(c.id) + '<br><span class="phase">' + escEv(project.phase) + '</span><br>Date 16/06/2026</div>' +
    '<div class="risk">' + escEv(c.risk) + '<br><b>Butoir ' + escEv(c.due) + '</b></div></div>' +
    '<div class="title"><h3>' + escEv(c.title) + '</h3>' + evidenceIcon(c.ico) + '</div>' +
    evidenceChips(c) +
    '<div class="ops"><div class="op"><b>Statut</b>' + escEv(c.status) + '</div><div class="op"><b>Décideur attendu</b>' + escEv(c.decider) + '</div></div>' +
    '<div class="body"><section class="sec"><h4>Sources</h4>' + evidenceSources(c) + '</section>' +
    '<section class="sec"><h4>Constat</h4><p><b>Établi</b> · ' + escEv(c.est) + '</p><p><b>Incertain</b> · ' + escEv(c.inc) + '</p></section>' +
    '<section class="sec"><h4>Actions recommandées</h4><div class="line"><b>Action</b><span>' + escEv(c.act) + '</span></div>' +
    '<div class="line"><b>Manque</b><span>' + escEv(c.miss) + '</span></div>' +
    '<div class="line"><b>Décision</b><span>' + escEv(c.dec) + '</span></div></section></div>' +
    '<div class="deps"><h4>Dépendances</h4>' + evidenceDeps(c) + '</div>' +
    '<div class="actions"><button data-a="ok" data-id="' + c.id + '">Valider</button>' +
    '<button data-a="no" data-id="' + c.id + '">Refuser</button>' +
    '<button data-a="mod" data-id="' + c.id + '">Modifier</button>' +
    '<button data-a="more" data-id="' + c.id + '">Recherche+</button></div></div></article>';
}

function evidenceRenderProjects(projects) {
  return projects.map((p, pi) =>
    '<section class="swiper-slide pSlide"><div class="swiper sSw"><div class="swiper-wrapper">' +
    p.cards.map(c => evidenceCard(c, pi, p)).join('') +
    '</div></div></section>'
  ).join('');
}

function evidenceRelClass(c, selected, projects) {
  if (c.id === selected.id) return 'sel';
  const current = projects[selected.p].cards.find(x => x.id === selected.id);
  const rels = current ? current.relations : [];
  if (rels.some(r => r.direction === 'upstream' && r.target === c.id)) return 'up';
  if (rels.some(r => r.direction === 'downstream' && r.target === c.id)) return 'down';
  if (rels.some(r => r.direction === 'peer' && r.target === c.id)) return 'peer';
  return '';
}

function evidenceMiniCard(c, cls) {
  return '<button class="mini ' + cls + '" data-mini="' + c.id + '"><h4>' + escEv(c.title) + '</h4>' + evidenceChips(c) + '</button>';
}
