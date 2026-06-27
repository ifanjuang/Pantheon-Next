/* Pantheon Control — hierarchy-driven deck app.
   Documenté non implémenté. Données fictives ; aucune action n'a d'effet réel.

   Règle UX actuelle :
   - chaque carte affiche son propre fil d'Ariane au-dessus du contenu ;
   - fil type : home / nom du projet / scène / sujet ;
   - liens du fil cliquables, nus, sans bordure ;
   - Swiper horizontal parent = profondeur hiérarchique ;
   - droite = descendre, gauche = remonter ;
   - Swipers verticaux imbriqués = cartes sœurs ;
   - haut / bas = changer de sibling ;
   - clic carte = recto / détail ;
   - bouton = fallback desktop/accessibilité, sans effet externe.
*/
(function(){
  'use strict';

  const CARD_TYPES = {
    project:{label:'Projet', className:'pc-card--project', bg:'PROJET', fields:['phase','scope','next']},
    scene:{label:'Scène', className:'pc-card--scene', bg:'SCÈNE', fields:['description','next']},
    subject:{label:'Sujet', className:'pc-card--subject', bg:'SUJET', fields:['scope','next']},
    run:{label:'Run', className:'pc-card--run', bg:'RUN', fields:['date','indice','output','next']},
    document:{label:'Document', className:'pc-card--document', bg:'DOC', fields:['source','freshness','next']},
    trace:{label:'Trace', className:'pc-card--trace', bg:'TRACE', fields:['event','impact','next']},
    status:{label:'Status', className:'pc-card--status', bg:'STATUS', fields:['open','blocked','next']},
    gate:{label:'Gate', className:'pc-card--gate', bg:'GATE', fields:['decision','reason','next']},
    knowledge:{label:'Connaissance', className:'pc-card--knowledge', bg:'KNOW', fields:['family','authority','freshness']},
    draft:{label:'Draft', className:'pc-card--draft', bg:'DRAFT', fields:['date','indice','version','output','next']},
    generic:{label:'Carte', className:'pc-card--generic', bg:'CARD', fields:['next']}
  };

  const CONFIG = window.PC_DECK_CONFIG || {
    root:{id:'root', type:'root', title:'Pantheon Control', scene:'runs', children:[
      {id:'project-general', type:'project', title:'Général / Corpus IFJ', scene:'knowledge', summary:'Corpus hors projet : connaissances, guides, lexiques, gates types et runs types.', phase:'Global', scope:'Hors projet', next:'Réutiliser comme référence, jamais comme preuve projet sans Evidence scopée.', chips:[['Corpus','blue'],['Non probant seul','yellow'],['Hors projet','muted']], children:[
        {id:'general-documents', type:'scene', title:'Documents', scene:'documents', summary:'Sources documentaires générales avant qualification.', description:'PLU, MAF, guides CCTP, lexiques et doctrine agence.', next:'Qualifier autorité, version et fraîcheur.', chips:[['Sources','yellow']], children:[
          {id:'general-maf', type:'subject', title:'MAF', scene:'documents', summary:'Recommandations et garde-fous assurance.', scope:'Corpus documentaire hors projet', next:'Créer ou vérifier les Connaissance Cards.', chips:[['À vérifier','yellow']], children:[
            {id:'know-maf-mission', type:'knowledge', title:'MAF — limites de mission', scene:'documents', summary:'Garde-fou de formulation pour demandes hors périmètre.', family:'Assurance / MAF', authority:'Version à vérifier.', freshness:'À qualifier avant usage externe.', chips:[['Candidate','blue'],['Responsabilité','red']]},
            {id:'know-maf-hors-mission', type:'knowledge', title:'MAF — réponse hors mission', scene:'documents', summary:'Réponse prudente si une demande sort de la prestation.', family:'Assurance / MAF', authority:'Doctrine candidate.', freshness:'À vérifier.', chips:[['Template lié','yellow']]}
          ]},
          {id:'general-plu', type:'subject', title:'PLU', scene:'documents', summary:'Règlements et extraits d’urbanisme.', scope:'Corpus documentaire hors projet', next:'Ne devient Evidence qu’une fois utilisé sur un dossier.', chips:[['Officiel à dater','yellow']], children:[
            {id:'know-plu-facades', type:'knowledge', title:'PLU — matériaux de façade', scene:'documents', summary:'Contrôle matériaux, teintes, modénatures et prescriptions locales.', family:'Urbanisme / PLU', authority:'Officiel si source datée.', freshness:'À vérifier commune par commune.', chips:[['Façade','blue']]},
            {id:'know-plu-emprise', type:'knowledge', title:'PLU — emprise et implantation', scene:'documents', summary:'Retraits, limites séparatives, emprise, hauteur et annexes.', family:'Urbanisme / PLU', authority:'Officiel si source datée.', freshness:'À vérifier.', chips:[['Implantation','blue']]}
          ]},
          {id:'general-cctp', type:'subject', title:'Guides CCTP', scene:'documents', summary:'Guides marché, interfaces lots et rédaction technique.', scope:'Corpus documentaire hors projet', next:'Distinguer guide, template et pièce projet.', chips:[['Marchés','yellow']], children:[
            {id:'know-cctp-interface', type:'knowledge', title:'CCTP — interfaces entre lots', scene:'documents', summary:'Éviter qu’une prestation soit placée au mauvais lot.', family:'CCTP / marchés', authority:'Doctrine agence candidate.', freshness:'À enrichir.', chips:[['Interfaces','orange']]}
          ]}
        ]},
        {id:'general-runs', type:'scene', title:'Runs types', scene:'runs', summary:'Méthodes de traitement réutilisables sans effet d’exécution.', description:'Scénarios types pour CR, factures, photos chantier et matériaux.', next:'Adapter à un projet réel.', chips:[['Non exécuté','muted']], children:[
          {id:'general-run-cr', type:'subject', title:'CR chantier', scene:'runs', summary:'Finaliser un CR depuis notes, photos, ancien CR et contraintes.', scope:'Méthode type', next:'Tester sur dossier réel.', chips:[['Run type','blue']], children:[
            {id:'run-type-cr-final', type:'run', title:'Finalisation CR', scene:'runs', summary:'Lire notes, comparer ancien CR, produire draft, ouvrir gates.', date:'2026-06-28', indice:'A', output:'Draft CR + mail candidat + gates.', next:'Ne pas envoyer sans gate.', chips:[['Gate externe','red'],['Indice A','blue']]},
            {id:'run-type-photo-doute', type:'run', title:'Photo doute chantier', scene:'runs', summary:'Analyser photo, rechercher contexte, demander autre angle si insuffisant.', date:'2026-06-28', indice:'B', output:'Observation candidate ou gap ciblé.', next:'Ne pas conclure sans source.', chips:[['Gap possible','orange'],['Indice B','blue']]}
          ]},
          {id:'general-run-facture', type:'subject', title:'Facture / devis', scene:'runs', summary:'Analyser facture, situation ou devis supplémentaire.', scope:'Méthode type', next:'Croiser marché, CCTP, assurance et avancement.', chips:[['Paiement','red']], children:[
            {id:'run-type-facture', type:'run', title:'Analyse facture', scene:'runs', summary:'Comparer facture, marché, CCTP, avancement et mission.', date:'2026-06-28', indice:'C', output:'Avis candidat + points à vérifier + gate paiement.', next:'Décision humaine obligatoire.', chips:[['Gate paiement','red'],['Indice C','blue']]},
            {id:'run-type-devis-sup', type:'run', title:'Devis supplémentaire', scene:'runs', summary:'Identifier hors marché, omission, aléa ou mauvaise affectation de lot.', date:'2026-06-28', indice:'D', output:'Analyse candidate + mail prudent.', next:'Vérifier responsabilité et mission.', chips:[['Hors mission possible','orange'],['Indice D','blue']]}
          ]}
        ]},
        {id:'general-gates', type:'scene', title:'Gates types', scene:'gates', summary:'Seuils de décision types.', description:'Envoi externe, mémoire validée, paiement, action Notion.', next:'Adapter au projet actif.', chips:[['Seuils','orange']], children:[
          {id:'gate-type-externe', type:'gate', title:'Gate type — effet externe', scene:'gates', summary:'Toute transmission externe doit être validée.', decision:'Envoyer / corriger / bloquer.', reason:'Effet hors cockpit.', next:'Validation humaine.', chips:[['Externe','orange']]}
        ]}
      ]},
      {id:'project-les-damps', type:'project', title:'Les Damps', scene:'runs', summary:'Projet actif : suivi chantier, CR, factures, documents et gates.', phase:'DET / chantier', scope:'Extension + rénovation énergétique', next:'Contrôler les gates ouverts avant transmission.', chips:[['Actif','green'],['Gates 4','red']], children:[
        {id:'damps-runs', type:'scene', title:'Runs', scene:'runs', summary:'Sessions de traitement et brouillons candidats.', description:'CR, factures, façade et production de sorties candidates.', next:'Ouvrir un sujet.', chips:[['Alertes 3','orange']], children:[
          {id:'damps-cr-runs', type:'subject', title:'CR chantier', scene:'runs', summary:'Comptes rendus chantier.', scope:'Projet Les Damps · Runs', next:'Valider le draft avant envoi.', chips:[['En cours','blue']], children:[
            {id:'run-cr-2026-06-27', type:'run', title:'CR chantier 27/06', scene:'runs', summary:'Brouillon CR prêt, 3 gates ouverts, 2 points à vérifier.', date:'2026-06-27', indice:'A', output:'Final Candidate v1.0 non transmis.', next:'Relire et décider.', chips:[['Candidate','blue'],['Gates 3','red']]},
            {id:'draft-cr-v1', type:'draft', title:'Draft CR', scene:'runs', summary:'Compte rendu candidat non envoyé.', date:'2026-06-27', indice:'B', version:'v1.0', output:'CR + mail candidat.', next:'Vérifier formulations hors mission.', chips:[['Non envoyé','red']]}
          ]},
          {id:'damps-factures-runs', type:'subject', title:'Factures', scene:'runs', summary:'Factures, situations et devis supplémentaires.', scope:'Projet Les Damps · Runs', next:'Croiser marché, CCTP et avancement.', chips:[['Paiement','red']], children:[
            {id:'run-facture-msb-01', type:'run', title:'Analyse facture MSB', scene:'runs', summary:'Comparer facture, AE, CCTP et avancement.', date:'2026-06-28', indice:'A', output:'Avis candidat : paiement à vérifier.', next:'Gate paiement requis.', chips:[['Gate paiement','red']]}
          ]},
          {id:'damps-facade-runs', type:'subject', title:'Façade', scene:'runs', summary:'Choix matériaux, PLU, échanges instruction et économie.', scope:'Projet Les Damps · Runs', next:'Croiser PLU et budget.', chips:[['PLU requis','yellow']], children:[
            {id:'run-facade-materials', type:'run', title:'Choix façade matériaux', scene:'runs', summary:'Comparer bardage, enduit, brique, coût et acceptabilité PLU.', date:'2026-06-28', indice:'A', output:'Pré-sélection candidate.', next:'Vérifier PLU et échanges antérieurs.', chips:[['Candidate','blue']]}
          ]}
        ]},
        {id:'damps-documents', type:'scene', title:'Documents', scene:'documents', summary:'Sources projet.', description:'Photos, CR, mails, plans, CCTP, AE, factures.', next:'Relier aux runs ou évidences.', chips:[['Sources','muted']], children:[
          {id:'damps-cr-docs', type:'subject', title:'CR chantier', scene:'documents', summary:'Documents du dernier CR.', scope:'Projet Les Damps · Documents', next:'Relier aux observations.', chips:[['Docs 4','blue']], children:[
            {id:'doc-cr-n-1', type:'document', title:'CR précédent n-1', scene:'documents', summary:'Source historique.', source:'PDF projet.', freshness:'Date à confirmer.', next:'Relier aux points maintenus.', chips:[['PDF','blue']]},
            {id:'doc-photo-support', type:'document', title:'Photo support escalier', scene:'documents', summary:'Photo à analyser avec prudence.', source:'Image chantier.', freshness:'Date fichier à confirmer.', next:'Demander autre angle si besoin.', chips:[['Photo','yellow']]}
          ]}
        ]},
        {id:'damps-gates', type:'scene', title:'Gates', scene:'gates', summary:'Décisions attendues.', description:'Envoi, paiement, Notion, mémoire.', next:'Décider ou reporter.', chips:[['Décision','orange']], children:[
          {id:'damps-cr-gates', type:'subject', title:'CR chantier', scene:'gates', summary:'Gates du compte rendu.', scope:'Projet Les Damps · Gates', next:'Traiter avant envoi.', chips:[['Gates 2','red']], children:[
            {id:'gate-envoi-cr', type:'gate', title:'Envoi CR chantier', scene:'gates', summary:'Transmission externe non validée.', decision:'Valider / corriger / garder brouillon.', reason:'Le CR engage l’agence.', next:'Décision humaine explicite.', chips:[['Ouvert','red'],['Effet externe','orange']]}
          ]}
        ]}
      ]},
      {id:'project-poussin', type:'project', title:'Poussin', scene:'status', summary:'Projet avec contexte contentieux / report. Exemple de projet à risque procédural.', phase:'PC accordé · recours / report', scope:'Surélévation + rénovation intérieure', next:'Conserver statut et limites avant toute relance.', chips:[['Contentieux','red']], children:[
        {id:'poussin-status', type:'scene', title:'Status', scene:'status', summary:'État général du dossier.', description:'Report, recours et limites de mission.', next:'Ne pas produire de réponse externe sans gate.', chips:[['Risque fort','red']], children:[
          {id:'poussin-recours', type:'subject', title:'Recours voisin', scene:'status', summary:'Sujet juridique/procédural sensible.', scope:'Projet Poussin · Status', next:'Qualifier avec pièces et conseil adapté.', chips:[['Procédure','orange']], children:[
            {id:'status-poussin-recours', type:'status', title:'État recours', scene:'status', summary:'Le projet est reporté ; aucune décision technique ne doit masquer le risque procédure.', open:'Recours / contentieux à suivre.', blocked:'Calendrier travaux suspendu.', next:'Conserver trace et décisions clients.', chips:[['Bloqué','red']]}
          ]}
        ]}
      ]}
    ]}
  };

  const state = { path:[0], activeLevel:0, depthSwiper:null, siblingSwipers:[] };

  function esc(value){ return String(value == null ? '' : value).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#039;'); }
  function typeConfig(type){ return CARD_TYPES[type] || CARD_TYPES.generic; }
  function nodeAtPath(path){ let node = CONFIG.root; path.forEach(index => { if(node && node.children && node.children[index]) node = node.children[index]; }); return node; }
  function siblingsForLevel(level){ const parent = nodeAtPath(state.path.slice(0, level)) || CONFIG.root; return parent.children || []; }
  function selectedNodeAtLevel(level){ const siblings = siblingsForLevel(level); return siblings[state.path[level] || 0]; }

  function visibleLevels(){
    const levels = [];
    let parent = CONFIG.root;
    let level = 0;
    while(parent && parent.children && parent.children.length){
      const siblings = parent.children;
      const selectedIndex = Math.min(state.path[level] || 0, siblings.length - 1);
      state.path[level] = selectedIndex;
      levels.push({level, parent, siblings, selectedIndex, selected:siblings[selectedIndex]});
      parent = siblings[selectedIndex];
      level += 1;
      if(level > 12) break;
    }
    state.path = state.path.slice(0, Math.max(1, levels.length));
    state.activeLevel = Math.min(state.activeLevel, Math.max(0, levels.length - 1));
    return levels;
  }

  function pathForCard(level, index){
    const path = state.path.slice(0, level + 1);
    path[level] = index;
    return path;
  }
  function crumbsForPath(path){
    const crumbs = [{title:'home', path:[0]}];
    for(let level=0; level<path.length; level++){
      const node = nodeAtPath(path.slice(0, level + 1));
      if(node) crumbs.push({title:node.title, path:path.slice(0, level + 1)});
    }
    return crumbs;
  }
  function renderCardBreadcrumb(level, index){
    return '<nav class="pc-card-breadcrumb">'+crumbsForPath(pathForCard(level, index)).map((crumb) => '<button data-card-crumb="'+esc(crumb.path.join(','))+'">'+esc(crumb.title)+'</button>').join('<span>/</span>')+'</nav>';
  }

  function renderChip(chip){ if(!chip) return ''; const label = Array.isArray(chip) ? chip[0] : chip; const tone = Array.isArray(chip) ? chip[1] : 'muted'; return '<span class="pc-chip pc-chip--'+esc(tone)+'">'+esc(label)+'</span>'; }
  function labelFor(key){ return ({phase:'Phase', scope:'Périmètre', next:'Prochaine action', description:'Description', output:'Sortie', source:'Source', freshness:'Fraîcheur', event:'Événement', impact:'Impact', open:'Ouvert', blocked:'Bloqué', decision:'Décision', reason:'Motif', family:'Famille', authority:'Autorité', version:'Version', date:'Date', indice:'Indice'})[key] || key; }
  function renderFields(node, cfg){ return (cfg.fields || []).filter(key => node[key]).map(key => '<p class="pc-card__field"><span>'+esc(labelFor(key))+'</span><b>'+esc(node[key])+'</b></p>').join(''); }

  function renderDetailRows(node, cfg){
    const children = node.children || [];
    const rows = [['ID', node.id || ''], ['Type', node.type || 'carte'], ['Statut', (node.chips || []).map(c => Array.isArray(c) ? c[0] : c).join(' · ')], ['Résumé', node.summary || '']];
    (cfg.fields || []).forEach(key => { if(node[key]) rows.push([labelFor(key), node[key]]); });
    rows.push(['Enfants', children.length ? children.map(c => c.title).join(' · ') : 'Aucun enfant configuré']);
    rows.push(['Effet', 'Détail consultatif uniquement. Aucune validation, mémoire ou action externe.']);
    return rows.filter(row => row[1]).map(row => '<p class="pc-detail-row"><span>'+esc(row[0])+'</span><b>'+esc(row[1])+'</b></p>').join('');
  }

  function renderCard(node, level, index){
    const cfg = typeConfig(node.type);
    const hasChildren = Array.isArray(node.children) && node.children.length > 0;
    const chips = (node.chips || []).map(renderChip).join('');
    const fields = renderFields(node, cfg);
    const detailRows = renderDetailRows(node, cfg);
    const sceneClass = node.scene ? ' scene-' + esc(node.scene) : '';
    const descend = hasChildren ? '<button class="pc-open-card" data-descend-level="'+level+'" data-descend-index="'+index+'">Descendre</button>' : '<button class="pc-open-card" data-detail-toggle="true">Détail</button>';
    const breadcrumb = renderCardBreadcrumb(level, index);
    return '<article class="pc-card '+esc(cfg.className)+sceneClass+'" data-card-level="'+level+'" data-card-index="'+index+'" data-node-id="'+esc(node.id || '')+'">'+breadcrumb+'<div class="pc-card__front"><div class="pc-card__bg-word">'+esc(node.bg || cfg.bg || cfg.label)+'</div><div class="pc-card__inner"><header class="pc-card__header"><span class="pc-card__eyebrow">'+esc(cfg.label)+' · '+esc(node.type || 'carte')+'</span><h3 class="pc-card__title">'+esc(node.title)+'</h3></header><p class="pc-card__summary">'+esc(node.summary || '')+'</p>'+(fields ? '<div class="pc-card__fields">'+fields+'</div>' : '')+'<footer class="pc-card__footer">'+chips+descend+'</footer></div></div><div class="pc-card__detail" aria-hidden="true"><div><span class="pc-card__eyebrow">Détail · '+esc(cfg.label)+'</span><h3 class="pc-card__detail-title">'+esc(node.title)+'</h3></div><div class="pc-detail-rows">'+detailRows+'</div><footer class="pc-card__footer"><button class="pc-open-card" data-detail-toggle="true">Retour carte</button>'+(hasChildren ? '<button class="pc-open-card" data-descend-level="'+level+'" data-descend-index="'+index+'">Descendre</button>' : '')+'</footer></div></article>';
  }

  function renderLevelSlide(info){
    return '<div class="swiper-slide pc-depth-slide scene-'+esc(info.selected.scene || 'runs')+'"><div class="swiper pc-level-swiper" data-level="'+info.level+'"><div class="swiper-wrapper">'+info.siblings.map((node, index) => '<div class="swiper-slide">'+renderCard(node, info.level, index)+'</div>').join('')+'</div><div class="swiper-pagination pc-level-pagination"></div></div></div>';
  }
  function renderApp(){
    ensureDeckStyles();
    const levels = visibleLevels();
    const active = levels[state.activeLevel] || levels[0];
    const body = '<section class="pc-deck-app scene-'+esc(active?.selected?.scene || 'runs')+'"><div class="pc-swipe-block"><div class="swiper pc-depth-swiper"><div class="swiper-wrapper">'+levels.map(renderLevelSlide).join('')+'</div><div class="swiper-pagination pc-depth-pagination"></div></div></div></section>';
    const page = document.getElementById('page');
    if(page) page.innerHTML = body;
    else { const shell = document.getElementById('shell'); if(shell) shell.innerHTML = body; }
    bindInteractions();
    initSwipers();
  }

  function toggleCardDetail(card){ if(!card) return; const isDetail = card.classList.toggle('is-detail'); const detail = card.querySelector('.pc-card__detail'); if(detail) detail.setAttribute('aria-hidden', isDetail ? 'false' : 'true'); }
  function changeSibling(level, index, rerender){ state.path[level] = index; state.path = state.path.slice(0, level + 1); state.activeLevel = level; if(rerender) renderApp(); }
  function descend(level, index){
    const node = siblingsForLevel(level)[index];
    if(!node || !node.children || !node.children.length){ toastIfAvailable('Carte feuille : aucun enfant configuré.', 'blue'); return; }
    state.path[level] = index;
    state.path = state.path.slice(0, level + 1);
    state.path[level + 1] = state.path[level + 1] || 0;
    state.activeLevel = level + 1;
    renderApp();
  }
  function goToCrumb(pathString){
    const path = pathString.split(',').map(v => Number(v)).filter(v => Number.isFinite(v));
    state.path = path.length ? path : [0];
    state.activeLevel = Math.max(0, state.path.length - 1);
    renderApp();
  }

  function bindInteractions(){
    document.querySelectorAll('.pc-card').forEach(card => card.addEventListener('click', event => { if(event.target.closest('button')) return; toggleCardDetail(card); }));
    document.querySelectorAll('[data-detail-toggle]').forEach(button => button.addEventListener('click', event => { event.stopPropagation(); toggleCardDetail(button.closest('.pc-card')); }));
    document.querySelectorAll('[data-descend-level]').forEach(button => button.addEventListener('click', event => { event.stopPropagation(); descend(Number(button.dataset.descendLevel), Number(button.dataset.descendIndex)); }));
    document.querySelectorAll('[data-card-crumb]').forEach(button => button.addEventListener('click', event => { event.stopPropagation(); goToCrumb(button.dataset.cardCrumb); }));
  }

  function initSwipers(){
    if(!window.Swiper) return;
    state.siblingSwipers = [];
    document.querySelectorAll('.pc-level-swiper').forEach(el => {
      const level = Number(el.dataset.level || 0);
      const swiper = new Swiper(el, {direction:'vertical', slidesPerView:1, spaceBetween:14, initialSlide:state.path[level] || 0, keyboard:false, pagination:{el:el.querySelector('.pc-level-pagination'), clickable:true}, resistanceRatio:.72, nested:true, mousewheel:false});
      swiper.on('slideChangeTransitionEnd', () => changeSibling(level, swiper.activeIndex, true));
      state.siblingSwipers.push(swiper);
    });
    const depthEl = document.querySelector('.pc-depth-swiper');
    if(!depthEl) return;
    state.depthSwiper = new Swiper(depthEl, {direction:'horizontal', slidesPerView:1, spaceBetween:0, initialSlide:state.activeLevel || 0, keyboard:{enabled:true, onlyInViewport:true}, pagination:{el:depthEl.querySelector('.pc-depth-pagination'), clickable:true}, resistanceRatio:.72, nested:false});
    state.depthSwiper.on('slideChangeTransitionEnd', () => { state.activeLevel = state.depthSwiper.activeIndex; renderApp(); });
  }

  function ensureDeckStyles(){
    if(document.getElementById('pc-deck-refine-style')) return;
    const style = document.createElement('style');
    style.id = 'pc-deck-refine-style';
    style.textContent = '.pc-deck-app{height:calc(100dvh - 72px);min-height:520px;display:flex;flex-direction:column;overflow:hidden}.pc-swipe-block{position:relative;flex:1 1 auto;min-height:0}.pc-depth-swiper,.pc-level-swiper{width:100%;height:100%}.pc-depth-slide{height:100%;display:flex}.pc-level-swiper .swiper-wrapper{height:100%!important}.pc-level-swiper .swiper-slide{height:100%!important;display:flex!important;align-items:stretch!important}.pc-card{border:0!important;box-shadow:0 28px 90px rgba(0,0,0,.36),inset 0 1px 0 rgba(255,255,255,.08)!important;background:linear-gradient(135deg,rgba(255,255,255,.06),rgba(255,255,255,.012)),#0d1016!important;isolation:isolate;display:flex;flex-direction:column;gap:12px}.pc-card-breadcrumb{position:relative;z-index:4;display:flex;align-items:center;gap:6px;flex-wrap:wrap;font-size:12px;line-height:1.1;color:rgba(244,242,238,.62);padding:2px 0 4px}.pc-card-breadcrumb button{border:0!important;background:transparent!important;box-shadow:none!important;border-radius:0!important;padding:0!important;margin:0!important;color:rgba(244,242,238,.72)!important;font-size:12px;line-height:1.1;text-transform:none;letter-spacing:.01em}.pc-card-breadcrumb button:hover{color:var(--fg)!important}.pc-card-breadcrumb span{color:rgba(244,242,238,.34)}.pc-card:after{content:"";position:absolute;inset:-24%;z-index:0;pointer-events:none;background:radial-gradient(circle at 18% 16%,color-mix(in srgb,var(--scene-accent) 58%,transparent),transparent 21%),radial-gradient(circle at 78% 12%,color-mix(in srgb,var(--scene-accent-2) 56%,transparent),transparent 24%),radial-gradient(circle at 58% 88%,rgba(255,255,255,.13),transparent 24%),conic-gradient(from 220deg at 50% 50%,rgba(255,255,255,.02),color-mix(in srgb,var(--scene-accent) 18%,transparent),rgba(255,255,255,.025),color-mix(in srgb,var(--scene-accent-2) 16%,transparent),rgba(255,255,255,.018)),repeating-linear-gradient(115deg,rgba(255,255,255,.035) 0 1px,transparent 1px 12px);filter:saturate(1.26) contrast(1.08);opacity:.88;background-size:120% 120%,130% 130%,140% 140%,160% 160%,auto;animation:pc-complex-gradient 18s ease-in-out infinite alternate}.pc-card__front,.pc-card__detail,.pc-card__inner{position:relative;z-index:2}.pc-card__front{min-height:0;display:block;flex:1}.pc-card__inner{height:100%;display:flex;flex-direction:column;gap:12px}.pc-card__detail{display:none;min-height:0;flex:1;flex-direction:column;gap:14px;position:relative;z-index:3}.pc-card.is-detail .pc-card__front{display:none}.pc-card.is-detail .pc-card__detail{display:flex}.pc-card__detail-title{margin:0;font-size:clamp(30px,8vw,64px);line-height:.9;letter-spacing:-.06em}.pc-detail-rows{display:grid;gap:8px}.pc-detail-row{margin:0;border-top:1px solid rgba(255,255,255,.08);padding-top:8px;display:grid;grid-template-columns:minmax(90px,180px) 1fr;gap:12px;color:var(--muted);font-size:13px}.pc-detail-row b{color:var(--fg);font-weight:600}.pc-open-card{touch-action:manipulation}@keyframes pc-complex-gradient{0%{transform:translate3d(-1%,0,0) scale(1);background-position:0% 35%,90% 20%,45% 95%,0% 50%,0 0}100%{transform:translate3d(1.5%,-1%,0) scale(1.035);background-position:82% 45%,10% 80%,75% 20%,100% 50%,24px 18px}}@media(max-width:720px){.pc-deck-app{height:calc(100dvh - 58px);min-height:480px}.pc-detail-row{display:block}.pc-detail-row b{display:block;margin-top:2px}.pc-card{border-radius:20px!important}}@media(prefers-reduced-motion:reduce){.pc-card:after{animation:none}}';
    document.head.appendChild(style);
  }

  function toastIfAvailable(message, tone){ if(typeof toast === 'function') toast(message, tone || 'blue'); }

  window.renderDeckApp = renderApp;
  document.addEventListener('DOMContentLoaded', renderApp);
})();
