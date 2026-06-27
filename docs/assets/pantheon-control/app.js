/* Pantheon Control — hierarchy-driven deck app.
   Documenté non implémenté. Données fictives ; aucune action n'a d'effet réel.

   Le moteur ne connaît pas une hiérarchie fixe.
   Il lit PC_DECK_CONFIG.levels et PC_DECK_CONFIG.root.
   Modifier la hiérarchie = modifier la configuration, pas le renderer.
*/
(function(){
  'use strict';

  const PC_CARD_TYPES = {
    project:{label:'Projet', className:'pc-card--project', bg:'PROJET', fields:['phase','scope','next']},
    scene:{label:'Scène', className:'pc-card--scene', bg:'SCÈNE', fields:['description','next']},
    subject:{label:'Sujet', className:'pc-card--subject', bg:'SUJET', fields:['scope','next']},
    run:{label:'Run', className:'pc-card--run', bg:'RUN', fields:['output','next']},
    document:{label:'Document', className:'pc-card--document', bg:'DOC', fields:['source','freshness','next']},
    trace:{label:'Trace', className:'pc-card--trace', bg:'TRACE', fields:['event','impact','next']},
    status:{label:'Status', className:'pc-card--status', bg:'STATUS', fields:['open','blocked','next']},
    gate:{label:'Gate', className:'pc-card--gate', bg:'GATE', fields:['decision','reason','next']},
    knowledge:{label:'Connaissance', className:'pc-card--knowledge', bg:'KNOW', fields:['family','authority','freshness']},
    generic:{label:'Carte', className:'pc-card--generic', bg:'CARD', fields:['next']}
  };

  const PC_DECK_CONFIG = window.PC_DECK_CONFIG || {
    levels:[
      {key:'project', label:'Projet'},
      {key:'scene', label:'Scène'},
      {key:'subject', label:'Sujet'},
      {key:'card', label:'Carte'}
    ],
    root:{
      id:'root', type:'root', title:'Pantheon Control', children:[
        {
          id:'project-general', type:'project', title:'Général / Corpus IFJ', scene:'knowledge',
          summary:'Espace hors projet : corpus documentaire, connaissances, modèles et runs types.',
          phase:'Global', scope:'Corpus non projet', next:'Utiliser comme référence, pas comme preuve projet.',
          chips:[['Hors projet','blue'],['Non probant seul','yellow']],
          children:[
            {
              id:'general-documents', type:'scene', title:'Documents', scene:'documents',
              summary:'Documents généraux, guides, PDF, lexiques et références brutes.',
              description:'Sources documentaires avant qualification en Connaissance.', next:'Qualifier version, autorité et fraîcheur.',
              chips:[['Scène','blue'],['Sources','yellow']],
              children:[
                {
                  id:'general-maf', type:'subject', title:'MAF', scene:'documents',
                  summary:'Recommandations et garde-fous assurance.', scope:'Corpus documentaire hors projet', next:'Créer des Connaissance Cards qualifiées.',
                  chips:[['Sujet','blue'],['À vérifier','yellow']],
                  children:[
                    {id:'know-maf-mission', type:'knowledge', title:'MAF — limites de mission', scene:'documents', summary:'Corpus documentaire utilisé comme garde-fou de formulation.', family:'Assurance / MAF', authority:'Professionnel · version à vérifier.', freshness:'À qualifier avant usage probatoire.', chips:[['Candidate','blue'],['Hors projet','muted']]},
                    {id:'know-maf-hors-mission', type:'knowledge', title:'MAF — réponse hors mission', scene:'documents', summary:'Aide à formuler une réponse prudente quand la demande sort du périmètre.', family:'Assurance / MAF', authority:'Professionnel · candidate.', freshness:'À vérifier.', chips:[['Candidate','blue'],['Template lié','yellow']]}
                  ]
                },
                {
                  id:'general-plu', type:'subject', title:'PLU', scene:'documents',
                  summary:'Documents d’urbanisme et extraits qualifiés.', scope:'Corpus documentaire hors projet', next:'Ne devient Evidence qu’une fois utilisé sur un projet.',
                  chips:[['Sujet','blue'],['Officiel à dater','yellow']],
                  children:[
                    {id:'know-plu-facades', type:'knowledge', title:'PLU — matériaux de façade', scene:'documents', summary:'Note type pour analyser les matériaux de façade.', family:'Urbanisme / PLU', authority:'Officiel si source datée.', freshness:'À vérifier commune par commune.', chips:[['To verify','yellow'],['Usage façade','blue']]}
                  ]
                }
              ]
            },
            {
              id:'general-runs', type:'scene', title:'Runs types', scene:'runs',
              summary:'Méthodes de traitement réutilisables sans effet d’exécution.',
              description:'Exemples de runs théoriques pour tester les decks.', next:'Ne pas confondre run type et run réel.',
              chips:[['Scène','blue'],['Documenté non implémenté','muted']],
              children:[
                {id:'run-type-cr', type:'run', title:'Run type — CR chantier', scene:'runs', summary:'Scénario générique de finalisation de compte rendu.', output:'Brouillon candidat + gates.', next:'Tester sur un dossier réel.', chips:[['Type','blue'],['Non exécuté','muted']]}
              ]
            }
          ]
        },
        {
          id:'project-les-damps', type:'project', title:'Les Damps', scene:'runs',
          summary:'Projet actif · suivi chantier et décisions de production.',
          phase:'DET / chantier', scope:'Extension + rénovation énergétique', next:'Contrôler les gates ouverts avant transmission.',
          chips:[['Actif','green'],['Risque moyen','yellow'],['Gates 3','red']],
          children:[
            {
              id:'damps-runs', type:'scene', title:'Runs', scene:'runs',
              summary:'Sessions de traitement et brouillons candidats.', description:'Brouillons, corrections, versions et sorties préparées.', next:'Ouvrir un sujet puis un run.',
              chips:[['Scène','blue'],['Alertes 2','orange']],
              children:[
                {
                  id:'damps-cr-runs', type:'subject', title:'CR chantier', scene:'runs',
                  summary:'Sujet de production récurrent pour les comptes rendus.', scope:'Projet Les Damps · scène Runs', next:'Ouvrir le dernier run ou créer un brouillon.',
                  chips:[['En cours','blue'],['Risque moyen','yellow']],
                  children:[
                    {id:'run-cr-2026-06-27', type:'run', title:'CR chantier — 27/06', scene:'runs', summary:'Brouillon CR prêt, 3 gates ouverts, 2 points à vérifier.', output:'Final Candidate v1.0 non transmis.', next:'Valider le diff avant toute action externe.', chips:[['Candidate','blue'],['Docs 5','muted'],['Traces 12','muted'],['Gates 3','red']]},
                    {id:'run-cr-2026-06-20', type:'run', title:'CR chantier — 20/06', scene:'runs', summary:'Run précédent ; points maintenus et contraintes de formulation.', output:'Draft Candidate v0.3 archivé.', next:'Utilisé comme source historique.', chips:[['Trace','muted'],['Gates 0','green']]}
                  ]
                },
                {
                  id:'damps-factures-runs', type:'subject', title:'Factures', scene:'runs',
                  summary:'Analyse de factures, situations et devis supplémentaires.', scope:'Projet Les Damps · scène Runs', next:'Préparer un run facture.',
                  chips:[['À faire','yellow']], children:[]
                }
              ]
            },
            {
              id:'damps-documents', type:'scene', title:'Documents', scene:'documents',
              summary:'Sources projet liées aux sujets actifs.', description:'Photos, CR, mails, plans et PDF projet.', next:'Ne pas confondre source et preuve.',
              chips:[['Scène','yellow'],['Sources','muted']],
              children:[
                {
                  id:'damps-cr-documents', type:'subject', title:'CR chantier', scene:'documents',
                  summary:'Documents utilisés pour le dernier compte rendu.', scope:'Projet Les Damps · scène Documents', next:'Lier les sources aux runs ou évidences.',
                  chips:[['Documents 2','blue']],
                  children:[
                    {id:'doc-cr-n-1', type:'document', title:'CR précédent n-1', scene:'documents', summary:'Source historique pour éviter les doublons.', source:'PDF projet · compte rendu antérieur.', freshness:'Version datée à confirmer.', next:'Relier aux points maintenus.', chips:[['Source à valider','yellow'],['PDF','blue']]},
                    {id:'doc-photo-support', type:'document', title:'Photo support escalier', scene:'documents', summary:'Photo associée au point support à vérifier.', source:'Image chantier transmise pendant le run.', freshness:'Date fichier à confirmer.', next:'Demander localisation si nécessaire.', chips:[['Candidate','blue'],['Photo','yellow']]}
                  ]
                }
              ]
            },
            {
              id:'damps-traces', type:'scene', title:'Traces', scene:'traces',
              summary:'Historique de travail, contraintes et corrections.', description:'Trace conversationnelle non canonique.', next:'Promouvoir uniquement après gate si nécessaire.',
              chips:[['Scène','muted'],['Ledger','blue']],
              children:[
                {id:'damps-cr-traces', type:'subject', title:'CR chantier', scene:'traces', summary:'Traces du run CR chantier.', scope:'Projet Les Damps · scène Traces', next:'Relire les contraintes avant finalisation.', chips:[['Traces 1','muted']], children:[
                  {id:'trace-constraint-no-opc', type:'trace', title:'Contrainte : pas de posture OPC', scene:'traces', summary:'La formulation délai doit rester une alerte, pas un pilotage.', event:'Correction utilisateur intégrée au ledger de travail.', impact:'Affecte les formulations délai du CR.', next:'Maintenir dans les prochains drafts.', chips:[['Retenue','green'],['Utilisateur','blue'],['v0.2','muted']]}
                ]}
              ]
            },
            {
              id:'damps-status', type:'scene', title:'Status', scene:'status',
              summary:'État synthétique du projet ou du sujet.', description:'Synthèse de blocage, risque et prochaine action.', next:'Lire avant action externe.',
              chips:[['Scène','green'],['Synthèse','blue']],
              children:[
                {id:'damps-cr-status', type:'subject', title:'CR chantier', scene:'status', summary:'État du CR chantier.', scope:'Projet Les Damps · scène Status', next:'Relire gates et points à vérifier.', chips:[['À valider','yellow']], children:[
                  {id:'status-cr', type:'status', title:'État CR chantier', scene:'status', summary:'Version candidate prête mais non transmissible sans décision.', open:'2 points ouverts, 1 clôture candidate.', blocked:'Envoi bloqué par gate externe.', next:'Relire gates et points à vérifier.', chips:[['À valider','yellow'],['Risque moyen','yellow'],['Gates 3','red']]}
                ]}
              ]
            },
            {
              id:'damps-gates', type:'scene', title:'Gates', scene:'gates',
              summary:'Arbitrages attendus et décisions humaines.', description:'Aucune transmission sans validation explicite.', next:'Décider, reporter ou corriger.',
              chips:[['Scène','red'],['Décision','orange']],
              children:[
                {id:'damps-cr-gates', type:'subject', title:'CR chantier', scene:'gates', summary:'Gates du compte rendu chantier.', scope:'Projet Les Damps · scène Gates', next:'Traiter le gate d’envoi avant toute transmission.', chips:[['Gates 1','red']], children:[
                  {id:'gate-envoi-cr', type:'gate', title:'Envoi CR chantier', scene:'gates', summary:'Transmission externe non validée.', decision:'Valider, corriger ou garder en brouillon.', reason:'Le CR engage l’agence vis-à-vis du client et des entreprises.', next:'Décision humaine explicite requise.', chips:[['Ouvert','red'],['Risque fort','red'],['Effet externe','orange']]}
                ]}
              ]
            }
          ]
        }
      ]
    }
  };

  const state = { path:[0] };

  function esc(value){
    return String(value == null ? '' : value)
      .replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')
      .replace(/"/g,'&quot;').replace(/'/g,'&#039;');
  }

  function typeConfig(type){ return PC_CARD_TYPES[type] || PC_CARD_TYPES.generic; }

  function currentNode(){
    let node = PC_DECK_CONFIG.root;
    state.path.forEach(index => {
      if(node && node.children && node.children[index]) node = node.children[index];
    });
    return node || PC_DECK_CONFIG.root;
  }

  function nodeAtPath(path){
    let node = PC_DECK_CONFIG.root;
    path.forEach(index => {
      if(node && node.children && node.children[index]) node = node.children[index];
    });
    return node;
  }

  function breadcrumb(){
    const parts = [{title:PC_DECK_CONFIG.root.title, path:[]}];
    let node = PC_DECK_CONFIG.root;
    state.path.forEach((index, depth) => {
      node = node.children[index];
      parts.push({title:node.title, path:state.path.slice(0, depth + 1)});
    });
    return parts;
  }

  function levelLabel(depth){
    const level = PC_DECK_CONFIG.levels[depth];
    return level ? level.label : 'Niveau';
  }

  function renderChip(chip){
    if(!chip) return '';
    const label = Array.isArray(chip) ? chip[0] : chip;
    const tone = Array.isArray(chip) ? chip[1] : 'muted';
    return '<span class="pc-chip pc-chip--'+esc(tone)+'">'+esc(label)+'</span>';
  }

  function renderFields(node, cfg){
    return (cfg.fields || [])
      .filter(key => node[key])
      .map(key => '<p class="pc-card__field"><span>'+esc(labelFor(key))+'</span><b>'+esc(node[key])+'</b></p>')
      .join('');
  }

  function labelFor(key){
    return ({phase:'Phase', scope:'Périmètre', next:'Prochaine action', description:'Description', output:'Sortie', source:'Source', freshness:'Fraîcheur', event:'Événement', impact:'Impact', open:'Ouvert', blocked:'Bloqué', decision:'Décision', reason:'Motif', family:'Famille', authority:'Autorité'})[key] || key;
  }

  function renderCard(node, index){
    const cfg = typeConfig(node.type);
    const hasChildren = Array.isArray(node.children) && node.children.length > 0;
    const chips = (node.chips || []).map(renderChip).join('');
    const fields = renderFields(node, cfg);
    const sceneClass = node.scene ? ' scene-' + esc(node.scene) : '';
    const action = hasChildren ? '<button class="pc-open-card" data-index="'+index+'">Ouvrir</button>' : '<button class="pc-open-card" data-leaf="true">Détail</button>';

    return ''+
      '<article class="pc-card '+esc(cfg.className)+sceneClass+'" data-index="'+index+'" data-node-id="'+esc(node.id || '')+'">'+
        '<div class="pc-card__bg-word">'+esc(node.bg || cfg.bg || cfg.label)+'</div>'+
        '<div class="pc-card__inner">'+
          '<header class="pc-card__header">'+
            '<span class="pc-card__eyebrow">'+esc(cfg.label)+' · '+esc(node.type || 'carte')+'</span>'+
            '<h3 class="pc-card__title">'+esc(node.title)+'</h3>'+
          '</header>'+
          '<p class="pc-card__summary">'+esc(node.summary || '')+'</p>'+
          (fields ? '<div class="pc-card__fields">'+fields+'</div>' : '')+
          '<footer class="pc-card__footer">'+chips+action+'</footer>'+
        '</div>'+
      '</article>';
  }

  function renderSiblingRail(){
    const parentPath = state.path.slice(0, -1);
    const parent = nodeAtPath(parentPath) || PC_DECK_CONFIG.root;
    const active = state.path[state.path.length - 1];
    const children = parent.children || [];
    if(!children.length) return '';
    return '<nav class="pc-sibling-rail" aria-label="Cartes sœurs">'+
      children.map((child, index) => '<button class="pc-sibling '+(index===active?'is-active':'')+'" data-sibling="'+index+'">'+esc(child.title)+'</button>').join('')+
      '</nav>';
  }

  function renderChildrenDeck(node){
    const children = node.children || [];
    if(!children.length){
      return '<section class="pc-empty"><b>Carte feuille.</b><p>Aucun enfant configuré. Le détail reste candidat et sans effet.</p></section>';
    }
    return '<section class="pc-deck-frame"><div class="swiper pc-card-swiper"><div class="swiper-wrapper">'+
      children.map((child, index) => '<div class="swiper-slide">'+renderCard(child, index)+'</div>').join('')+
      '</div><div class="swiper-pagination"></div></div></section>';
  }

  function renderApp(){
    const node = currentNode();
    const crumbs = breadcrumb();
    const depth = state.path.length;
    const body = ''+
      '<section class="pc-deck-app scene-'+esc(node.scene || 'runs')+'">'+
        '<div class="pc-deck-head">'+
          '<p class="pc-kicker">Documenté non implémenté · structure générée depuis JSON</p>'+
          '<h2>'+esc(node.title || 'Decks Pantheon')+'</h2>'+
          '<p class="lede">Le moteur lit la hiérarchie configurée. Ajouter un niveau, une scène ou un type de carte ne doit pas imposer de recoder le rendu.</p>'+
          '<nav class="pc-breadcrumb">'+crumbs.map((c,i)=>'<button data-crumb="'+i+'">'+esc(c.title)+'</button>').join('<span>›</span>')+'</nav>'+
          '<div class="pc-contextbar"><span>Niveau : '+esc(levelLabel(depth - 1))+'</span><span>Enfants : '+((node.children||[]).length)+'</span><span>Type : '+esc(node.type || 'root')+'</span></div>'+
        '</div>'+
        renderSiblingRail()+
        renderChildrenDeck(node)+
      '</section>';

    if(typeof mountPage === 'function'){
      mountPage('Decks gouvernés', 'Prototype : la navigation et les cartes sont générées depuis une structure hiérarchique.', body);
    } else {
      const shell = document.getElementById('shell');
      if(shell) shell.innerHTML = body;
    }
    bindInteractions();
    initSwiper();
  }

  function bindInteractions(){
    document.querySelectorAll('[data-index]').forEach(button => {
      button.addEventListener('click', event => {
        event.stopPropagation();
        const index = Number(button.getAttribute('data-index'));
        const node = currentNode();
        if(node.children && node.children[index] && node.children[index].children){
          state.path.push(index);
          renderApp();
        } else {
          toastIfAvailable('Carte feuille : aucun effet, détail candidat seulement.', 'blue');
        }
      });
    });
    document.querySelectorAll('[data-sibling]').forEach(button => {
      button.addEventListener('click', () => {
        state.path[state.path.length - 1] = Number(button.getAttribute('data-sibling'));
        renderApp();
      });
    });
    document.querySelectorAll('[data-crumb]').forEach(button => {
      button.addEventListener('click', () => {
        const index = Number(button.getAttribute('data-crumb'));
        state.path = breadcrumb()[index].path.slice();
        if(!state.path.length) state.path = [0];
        renderApp();
      });
    });
  }

  function initSwiper(){
    if(!window.Swiper) return;
    new Swiper('.pc-card-swiper', {
      direction:'vertical',
      slidesPerView:1,
      spaceBetween:14,
      mousewheel:true,
      keyboard:true,
      pagination:{el:'.swiper-pagination', clickable:true}
    });
  }

  function toastIfAvailable(message, tone){
    if(typeof toast === 'function') toast(message, tone || 'blue');
  }

  window.renderDeckApp = renderApp;
  document.addEventListener('DOMContentLoaded', renderApp);
})();
