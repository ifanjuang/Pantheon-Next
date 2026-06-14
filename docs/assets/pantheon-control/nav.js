/* Pantheon Control — coquille partagée (barre + drawer). Injecte le shell et
   marque la page active. Organisation par chapitres de fonction. */

const PAGES = [
  ['index.html',        'Accueil',              'Pilotage'],
  ['surveillance.html', 'Journal',              'Pilotage'],
  ['machines.html',     'Machines',             'Infrastructure'],
  ['services.html',     'Services & outils',    'Infrastructure'],
  ['ia.html',           'Modèles & IA',         'IA'],
  ['skills.html',       'Skills',               'IA'],
  ['discussion.html',   'Discussion',           'Travail'],
  ['drafting.html',     'Rédaction assistée',   'Travail'],
  ['evidence.html',     'Preuves & sources',    'Travail'],
  ['files.html',        'Fichiers',             'Travail'],
  ['base-memory.html',  'Base & mémoire',       'Travail'],
];

function currentPage(){
  const f = location.pathname.split('/').pop();
  return f && f.length ? f : 'index.html';
}

function renderShell(){
  const here = currentPage();
  const groups = {}, order = [];
  PAGES.forEach(([href,label,grp])=>{ if(!groups[grp]){groups[grp]=[];order.push(grp);} groups[grp].push([href,label]); });

  const links = order.map(grp =>
    '<div class="sep">'+grp+'</div>' +
    groups[grp].map(([href,label]) =>
      '<a href="'+href+'" class="'+(href===here?'active':'')+'">'+label+'</a>'
    ).join('')
  ).join('');

  document.getElementById('shell').innerHTML =
    '<div class="topbar">' +
      '<button class="burger" onclick="document.body.classList.toggle(\'nav-open\')">☰</button>' +
      '<h1>Pantheon Control</h1>' +
      '<div class="doctrine">documenté non implémenté · les boutons préparent des demandes</div>' +
    '</div>' +
    '<div class="layout">' +
      '<nav class="drawer">'+links+'</nav>' +
      '<div class="content"><div id="page"></div></div>' +
    '</div>';
}

/* Pose titre + sous-titre court + corps. */
function mountPage(title, lede, bodyHtml){
  let html = '<h2>'+title+'</h2>';
  if(lede) html += '<p class="lede">'+lede+'</p>';
  html += bodyHtml;
  document.getElementById('page').innerHTML = html;
}

renderShell();
