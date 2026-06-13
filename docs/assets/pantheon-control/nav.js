/* Pantheon Control — coquille partagée (barre + drawer + bandeau de règles).
   Injecte le shell dans #shell et marque la page active. */

const PAGES = [
  ['index.html',        'Accueil / Liveness', 'Cockpit'],
  ['evidence.html',     'Evidence → Mémoire', 'Gouvernance'],
  ['files.html',        'Files',              'Gouvernance'],
  ['base-memory.html',  'Base & Mémoire',     'Gouvernance'],
  ['surveillance.html', 'Surveillance',       'Gouvernance'],
  ['infra.html',        'Infrastructure',     'Infrastructure'],
];

const RULES = [
  'Installed ≠ Authorized',
  'Latest ≠ Stable',
  'Runtime success ≠ Approval',
  'Evidence candidate ≠ Proof',
];

function currentPage(){
  const f = location.pathname.split('/').pop();
  return f && f.length ? f : 'index.html';
}

function renderShell(){
  const here = currentPage();
  let groups = {}, order = [];
  PAGES.forEach(([href,label,grp])=>{ if(!groups[grp]){groups[grp]=[];order.push(grp);} groups[grp].push([href,label]); });

  const links = order.map(grp =>
    '<div class="sep">'+grp+'</div>' +
    groups[grp].map(([href,label]) =>
      '<a href="'+href+'" class="'+(href===here?'active':'')+'">'+label+'</a>'
    ).join('')
  ).join('');

  const rules = RULES.map(r=>'<span class="rule">'+r+'</span>').join('');

  document.getElementById('shell').innerHTML =
    '<div class="topbar">' +
      '<button class="burger" onclick="document.body.classList.toggle(\'nav-open\')">☰</button>' +
      '<h1>Pantheon Control</h1>' +
      '<div class="doctrine">OpenWebUI expose · Hermes exécute · Pantheon gouverne · l’humain décide</div>' +
    '</div>' +
    '<div class="layout">' +
      '<nav class="drawer">'+links+'</nav>' +
      '<div class="content">' +
        '<div class="rules">'+rules+'</div>' +
        '<div id="page"></div>' +
      '</div>' +
    '</div>';
}

/* À appeler par chaque page : pose le titre, le rappel doctrinal et le corps. */
function mountPage(title, lede, guard, bodyHtml){
  let html = '<h2>'+title+'</h2>';
  if(lede)  html += '<p class="lede">'+lede+'</p>';
  if(guard) html += '<div class="guard">'+guard+'</div>';
  html += bodyHtml;
  document.getElementById('page').innerHTML = html;
}

renderShell();
