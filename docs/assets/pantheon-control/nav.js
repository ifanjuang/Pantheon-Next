/* Pantheon Control — coquille partagée (barre + drawer). Injecte le shell et
   marque la page active. Organisation par chapitres de fonction. */

const PAGES = [
  ['index.html',        'Accueil',                  'Pilotage'],
  ['surveillance.html', 'Journal & contrôles',      'Pilotage'],
  ['services.html',     'Services & connexions',    'Infrastructure'],
  ['machines.html',     'Machines & instances',     'Infrastructure'],
  ['installations.html','Installations & bootstrap','Infrastructure'],
  ['observability.html','Observabilité',            'Infrastructure'],
  ['modules.html',      'Modules & usages',         'Infrastructure'],
  ['deck.html',         'Decks gouvernés',          'Travail'],
  ['skills.html',       'Skills',                   'Travail'],
  ['discussion.html',   'Branches de décision',     'Travail'],
  ['drafting.html',     'Rédaction candidate',      'Travail'],
  ['evidence.html',     'Preuves & statuts',        'Travail'],
  ['references.html',   'Références',               'Travail'],
  ['files.html',        'Fichiers',                 'Travail'],
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

  const topbarStyle = 'min-height:42px;padding:0 0 0 14px;gap:10px;align-items:stretch';
  const titleStyle = 'display:flex;align-items:center;font-size:15px;line-height:1;margin:0';
  const doctrineStyle = 'display:flex;align-items:center;margin-left:auto;color:var(--muted);font-size:11px;text-align:right';
  const burgerStyle = 'order:3;align-self:stretch;margin:0;border:0;background:transparent;border-radius:0;padding:0 15px;color:var(--fg);font-size:18px;box-shadow:none';
  const deckAxisFix = '<style id="pc-deck-axis-fix">.pc-deck-topnav .pc-sibling-rail{display:none!important}.pc-level-swiper .swiper-wrapper{height:100%!important}.pc-level-swiper .swiper-slide{height:100%!important;display:flex!important;align-items:stretch!important}.pc-depth-swiper>.swiper-wrapper>.swiper-slide{width:100%!important}.pc-deck-topnav .pc-breadcrumb{margin:0!important}.pc-deck-app,.pc-swipe-block,.pc-depth-swiper,.pc-level-swiper,.pc-depth-slide{background:#090a0d!important;background-image:none!important}.pc-deck-app .pc-card{background:#10131a!important;background-image:none!important;filter:none!important;animation:none!important}.pc-deck-app .pc-card:before,.pc-deck-app .pc-card:after,.pc-card--scene:before{content:none!important;display:none!important;background:none!important;background-image:none!important;animation:none!important}.pc-deck-app .pc-card__bg-word{color:rgba(255,255,255,.035)!important}.pc-card.pc-card--subject{border:5px solid var(--scene-accent)!important;box-shadow:0 18px 50px rgba(0,0,0,.28)!important}.pc-card.pc-card--scene .pc-card__title{font-weight:1000!important;color:var(--scene-accent)!important;font-size:clamp(64px,16vw,152px)!important;line-height:.78!important;letter-spacing:-.105em!important;text-shadow:none!important}.pc-card.pc-card--scene .pc-card__eyebrow{color:var(--scene-accent)!important;font-weight:900!important}</style>';

  document.getElementById('shell').innerHTML =
    deckAxisFix +
    '<div class="topbar" style="'+topbarStyle+'">' +
      '<h1 style="'+titleStyle+'">Pantheon Control</h1>' +
      '<div class="doctrine" style="'+doctrineStyle+'">documenté non implémenté · les boutons préparent des demandes</div>' +
      '<button class="burger" style="'+burgerStyle+'" aria-label="Ouvrir le menu" onclick="toggleNav()">☰</button>' +
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
