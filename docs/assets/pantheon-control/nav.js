/* Pantheon Control — coquille partagée (barre + drawer). Injecte le shell et
   marque la page active. Organisation par chapitres de fonction. */

const PAGES = [
  ['index.html',        'Accueil',                  'Pilotage'],
  ['surveillance.html', 'Journal',                  'Pilotage'],
  ['services.html',     'Services & connexions',    'Infrastructure'],
  ['machines.html',     'Machines & instances',     'Infrastructure'],
  ['observability.html','Observabilité',            'Infrastructure'],
  ['skills.html',       'Skills',                   'Travail'],
  ['discussion.html',   'Discussion',               'Travail'],
  ['drafting.html',     'Rédaction assistée',       'Travail'],
  ['evidence.html',     'Preuves & sources',        'Travail'],
  ['references.html',   'Références',               'Travail'],
  ['files.html',        'Fichiers',                 'Travail'],
  ['base-memory.html',  'Base & mémoire',           'Travail'],
];

function currentPage(){
  const f = location.pathname.split('/').pop();
  return f && f.length ? f : 'index.html';
}

function closeNav(){
  document.body.classList.remove('nav-open');
}

function toggleNav(){
  document.body.classList.toggle('nav-open');
}

function renderShell(){
  const here = currentPage();
  const groups = {}, order = [];
  PAGES.forEach(([href,label,grp])=>{ if(!groups[grp]){groups[grp]=[];order.push(grp);} groups[grp].push([href,label]); });

  const links = order.map(grp =>
    '<div class="sep">'+grp+'</div>' +
    groups[grp].map(([href,label]) =>
      '<a href="'+href+'" class="'+(href===here?'active':'')+'" onclick="closeNav()">'+label+'</a>'
    ).join('')
  ).join('');

  document.getElementById('shell').innerHTML =
    '<div class="topbar">' +
      '<button class="burger" aria-label="Ouvrir le menu" onclick="toggleNav()">☰</button>' +
      '<h1>Pantheon Control</h1>' +
      '<div class="doctrine">documenté non implémenté · les boutons préparent des demandes</div>' +
    '</div>' +
    '<div class="layout">' +
      '<div class="nav-backdrop" aria-hidden="true" onclick="closeNav()"></div>' +
      '<nav class="drawer" aria-label="Navigation">'+links+'</nav>' +
      '<div class="content"><div id="page"></div></div>' +
    '</div>';
}

/* Pose titre + breadcrumb + sous-titre court + corps. */
function mountPage(title, lede, bodyHtml){
  const here = currentPage();
  const p = PAGES.find(([href])=>href===here);
  const grp = p ? p[2] : null;
  const bc = grp
    ? '<nav class="bc" aria-label="Fil d\'Ariane"><span class="bc-g">'+grp+'</span><span class="bc-sep" aria-hidden="true">›</span><span>'+title+'</span></nav>'
    : '';
  let html = bc+'<h2>'+title+'</h2>';
  if(lede) html += '<p class="lede">'+lede+'</p>';
  html += bodyHtml;
  document.getElementById('page').innerHTML = html;
}

/* ---- Toast de feedback ---- */
function toast(msg, tone){
  tone = tone||'green';
  const el = document.createElement('div');
  el.className = 'pc-toast t-'+tone;
  el.setAttribute('role','status');
  el.setAttribute('aria-live','polite');
  el.textContent = msg;
  document.body.appendChild(el);
  requestAnimationFrame(()=>el.classList.add('show'));
  setTimeout(()=>{ el.classList.remove('show'); setTimeout(()=>el.remove(), 300); }, 3000);
}

/* ---- Dialog de confirmation ---- */
function confirmAct(msg, label, onOk){
  const ov = document.createElement('div');
  ov.className = 'overlay';
  ov.setAttribute('role','dialog');
  ov.setAttribute('aria-modal','true');
  ov.innerHTML =
    '<div class="dialog">'+
      '<p>'+msg+'</p>'+
      '<div class="dbtn">'+
        '<button class="primary" id="_dok">'+label+'</button>'+
        '<button id="_dcancel">Annuler</button>'+
      '</div>'+
    '</div>';
  document.body.appendChild(ov);
  ov.querySelector('#_dok').onclick = ()=>{ ov.remove(); onOk(); };
  ov.querySelector('#_dcancel').onclick = ()=>ov.remove();
  ov.addEventListener('click', e=>{ if(e.target===ov) ov.remove(); });
  ov.querySelector('#_dok').focus();
}

renderShell();