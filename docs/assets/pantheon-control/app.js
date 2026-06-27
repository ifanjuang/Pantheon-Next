/* Pantheon Control — hierarchy-driven deck app.
   Documenté non implémenté. Données fictives ; aucune action n'a d'effet réel.

   Règle UX :
   - swipe horizontal = cartes sœurs du niveau actif ;
   - swipe haut = descendre dans la carte active ;
   - swipe bas = remonter au parent ;
   - clic carte = recto / détail ;
   - bouton = fallback desktop, sans effet externe.
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
    draft:{label:'Draft', className:'pc-card--draft', bg:'DRAFT', fields:['version','output','next']},
    action:{label:'Action', className:'pc-card--action', bg:'ACTION', fields:['effect','tool','next']},
    generic:{label:'Carte', className:'pc-card--generic', bg:'CARD', fields:['next']}
  };

  const PC_DECK_CONFIG = window.PC_DECK_CONFIG || {
    levels:[
      {key:'project', label:'Projet'},
      {key:'scene', label:'Scène'},
      {key:'subject', label:'Sujet'},
      {key:'card', label:'Carte'}
    ],
    root:{id:'root', type:'root', title:'Pantheon Control', scene:'runs', children:[
      {
        id:'project-general', type:'project', title:'Général / Corpus IFJ', scene:'knowledge',
        summary:'Corpus hors projet : connaissances, guides, lexiques, gates types et runs types.',
        phase:'Global', scope:'Hors projet', next:'Réutiliser comme référence, jamais comme preuve projet sans Evidence scopée.',
        chips:[['Corpus','blue'],['Non probant seul','yellow'],['Hors projet','muted']],
        children:[
          {id:'general-documents', type:'scene', title:'Documents', scene:'documents', summary:'Sources documentaires générales avant qualification.', description:'PLU, MAF, guides CCTP, lexiques et doctrine agence.', next:'Qualifier autorité, version et fraîcheur.', chips:[['Scène','yellow'],['Sources','muted']], children:[
            {id:'general-maf', type:'subject', title:'MAF', scene:'documents', summary:'Recommandations et garde-fous assurance.', scope:'Corpus documentaire hors projet', next:'Créer ou vérifier les Connaissance Cards.', chips:[['Sujet','blue'],['À vérifier','yellow']], children:[
              {id:'know-maf-mission', type:'knowledge', title:'MAF — limites de mission', scene:'documents', summary:'Garde-fou de formulation pour demandes hors périmètre.', family:'Assurance / MAF', authority:'Professionnel · version à vérifier.', freshness:'À qualifier avant usage externe.', chips:[['Candidate','blue'],['Responsabilité','red']]},
              {id:'know-maf-devoir-conseil', type:'knowledge', title:'MAF — devoir de conseil', scene:'documents', summary:'Distinguer conseil dû, mission signée et responsabilité engagée.', family:'Assurance / MAF', authority:'Professionnel · à sourcer.', freshness:'À vérifier.', chips:[['To verify','yellow'],['Conseil','blue']]},
              {id:'know-maf-hors-mission', type:'knowledge', title:'MAF — réponse hors mission', scene:'documents', summary:'Réponse prudente si une demande sort de la prestation.', family:'Assurance / MAF', authority:'Doctrine candidate.', freshness:'À vérifier.', chips:[['Candidate','blue'],['Template lié','yellow']]}
            ]},
            {id:'general-plu', type:'subject', title:'PLU', scene:'documents', summary:'Règlements et extraits d’urbanisme.', scope:'Corpus documentaire hors projet', next:'Ne devient Evidence qu’une fois utilisé sur un dossier.', chips:[['Sujet','blue'],['Officiel à dater','yellow']], children:[
              {id:'know-plu-facades', type:'knowledge', title:'PLU — matériaux de façade', scene:'documents', summary:'Contrôle des matériaux, teintes, modénatures et prescriptions locales.', family:'Urbanisme / PLU', authority:'Officiel si source datée.', freshness:'À vérifier commune par commune.', chips:[['To verify','yellow'],['Façade','blue']]},
              {id:'know-plu-emprise', type:'knowledge', title:'PLU — emprise et implantation', scene:'documents', summary:'Retraits, limites séparatives, emprise, hauteur et annexes.', family:'Urbanisme / PLU', authority:'Officiel si source datée.', freshness:'À vérifier.', chips:[['To verify','yellow'],['Implantation','blue']]}
            ]},
            {id:'general-cctp', type:'subject', title:'Guides CCTP', scene:'documents', summary:'Guides marché, interfaces lots et rédaction technique.', scope:'Corpus documentaire hors projet', next:'Distinguer guide, template et pièce projet.', chips:[['Sujet','blue'],['Marchés','yellow']], children:[
              {id:'know-cctp-interface', type:'knowledge', title:'CCTP — interfaces entre lots', scene:'documents', summary:'Éviter qu’une prestation soit placée au mauvais lot.', family:'CCTP / marchés', authority:'Doctrine agence candidate.', freshness:'À enrichir.', chips:[['Candidate','blue'],['Interfaces','orange']]},
              {id:'know-cctp-decennale', type:'knowledge', title:'CCTP — assurance décennale', scene:'documents', summary:'Vérifier l’activité précise assurée face à la prestation demandée.', family:'Assurance / marchés', authority:'À vérifier juridiquement.', freshness:'À vérifier.', chips:[['To verify','yellow'],['Décennale','red']]}
            ]}
          ]},
          {id:'general-runs', type:'scene', title:'Runs types', scene:'runs', summary:'Méthodes de traitement réutilisables sans effet d’exécution.', description:'Scénarios types pour CR, factures, photos chantier et matériaux.', next:'Adapter à un projet réel.', chips:[['Scène','blue'],['Non exécuté','muted']], children:[
            {id:'general-run-cr', type:'subject', title:'CR chantier', scene:'runs', summary:'Finaliser un CR depuis notes, photos, ancien CR et contraintes.', scope:'Méthode type', next:'Tester sur dossier réel.', chips:[['Run type','blue']], children:[
              {id:'run-type-cr-final', type:'run', title:'Run type — finalisation CR', scene:'runs', summary:'Lire notes, comparer ancien CR, produire draft, ouvrir gates.', output:'Draft CR + mail candidat + gates.', next:'Ne pas envoyer sans gate.', chips:[['Type','blue'],['Gate externe','red']]},
              {id:'run-type-photo-doute', type:'run', title:'Run type — photo doute chantier', scene:'runs', summary:'Analyser photo, rechercher contexte, demander autre angle si insuffisant.', output:'Observation candidate ou gap ciblé.', next:'Ne pas conclure sans source.', chips:[['Image','yellow'],['Gap possible','orange']]}
            ]},
            {id:'general-run-facture', type:'subject', title:'Facture / devis', scene:'runs', summary:'Analyser facture, situation ou devis supplémentaire.', scope:'Méthode type', next:'Croiser marché, CCTP, assurance et avancement.', chips:[['Run type','blue'],['Paiement','red']], children:[
              {id:'run-type-facture', type:'run', title:'Run type — analyse facture', scene:'runs', summary:'Comparer facture, marché, CCTP, avancement et mission.', output:'Avis candidat + points à vérifier + gate paiement.', next:'Décision humaine obligatoire.', chips:[['Type','blue'],['Gate paiement','red']]},
              {id:'run-type-devis-sup', type:'run', title:'Run type — devis supplémentaire', scene:'runs', summary:'Identifier hors marché, omission, aléa ou mauvaise affectation de lot.', output:'Analyse candidate + mail prudent.', next:'Vérifier responsabilité et mission.', chips:[['Type','blue'],['Hors mission possible','orange']]}
            ]}
          ]},
          {id:'general-gates', type:'scene', title:'Gates types', scene:'gates', summary:'Seuils de décision types.', description:'Envoi externe, mémoire validée, paiement, action Notion.', next:'Adapter au projet actif.', chips:[['Scène','red'],['Seuils','orange']], children:[
            {id:'gate-type-externe', type:'gate', title:'Gate type — effet externe', scene:'gates', summary:'Toute transmission externe doit être validée.', decision:'Envoyer / corriger / bloquer.', reason:'Effet hors cockpit.', next:'Validation humaine.', chips:[['Type','red'],['Externe','orange']]},
            {id:'gate-type-memoire', type:'gate', title:'Gate type — mémoire', scene:'gates', summary:'Promotion en registre ou mémoire stable.', decision:'Promouvoir / refuser / garder candidat.', reason:'Risque de fausse vérité durable.', next:'Preuve et portée obligatoires.', chips:[['Type','red'],['Mémoire','blue']]}
          ]}
        ]
      },
      {
        id:'project-les-damps', type:'project', title:'Les Damps', scene:'runs',
        summary:'Projet actif : suivi chantier, CR, factures, documents et gates.',
        phase:'DET / chantier', scope:'Extension + rénovation énergétique', next:'Contrôler les gates ouverts avant transmission.',
        chips:[['Actif','green'],['Risque moyen','yellow'],['Gates 4','red']],
        children:[
          {id:'damps-runs', type:'scene', title:'Runs', scene:'runs', summary:'Sessions de traitement et brouillons candidats.', description:'CR, factures, façade et production de sorties candidates.', next:'Ouvrir un sujet.', chips:[['Scène','blue'],['Alertes 3','orange']], children:[
            {id:'damps-cr-runs', type:'subject', title:'CR chantier', scene:'runs', summary:'Comptes rendus chantier.', scope:'Projet Les Damps · Runs', next:'Valider le draft avant envoi.', chips:[['En cours','blue'],['Risque moyen','yellow']], children:[
              {id:'run-cr-2026-06-27', type:'run', title:'CR chantier — 27/06', scene:'runs', summary:'Brouillon CR prêt, 3 gates ouverts, 2 points à vérifier.', output:'Final Candidate v1.0 non transmis.', next:'Relire et décider.', chips:[['Candidate','blue'],['Docs 5','muted'],['Gates 3','red']]},
              {id:'draft-cr-v1', type:'draft', title:'Draft CR — v1.0', scene:'runs', summary:'Compte rendu candidat non envoyé.', version:'v1.0', output:'CR + mail candidat.', next:'Vérifier formulations hors mission.', chips:[['Draft','blue'],['Non envoyé','red']]},
              {id:'run-cr-2026-06-20', type:'run', title:'CR chantier — 20/06', scene:'runs', summary:'Run précédent, source historique.', output:'Draft v0.3 archivé.', next:'Comparer les points maintenus.', chips:[['Trace','muted'],['Clos','green']]}
            ]},
            {id:'damps-factures-runs', type:'subject', title:'Factures', scene:'runs', summary:'Factures, situations et devis supplémentaires.', scope:'Projet Les Damps · Runs', next:'Croiser marché, CCTP et avancement.', chips:[['À faire','yellow'],['Paiement','red']], children:[
              {id:'run-facture-msb-01', type:'run', title:'Analyse facture MSB — situation 01', scene:'runs', summary:'Comparer facture, AE, CCTP et avancement.', output:'Avis candidat : paiement à vérifier.', next:'Gate paiement requis.', chips:[['Candidate','blue'],['Gate paiement','red']]},
              {id:'run-devis-sup-couv', type:'run', title:'Devis sup — couverture', scene:'runs', summary:'Vérifier si la prestation relève du lot ou d’un hors marché.', output:'Analyse candidate + question entreprise.', next:'Contrôler CCTP et assurance.', chips:[['To verify','yellow'],['Interface lot','orange']]}
            ]},
            {id:'damps-facade-runs', type:'subject', title:'Façade', scene:'runs', summary:'Choix matériaux, PLU, échanges instruction et économie.', scope:'Projet Les Damps · Runs', next:'Croiser PLU et budget.', chips:[['Préparation','blue']], children:[
              {id:'run-facade-materials', type:'run', title:'Choix façade — matériaux', scene:'runs', summary:'Comparer bardage, enduit, brique, coût et acceptabilité PLU.', output:'Pré-sélection candidate.', next:'Vérifier PLU et échanges antérieurs.', chips:[['Candidate','blue'],['PLU requis','yellow']]}
            ]}
          ]},
          {id:'damps-documents', type:'scene', title:'Documents', scene:'documents', summary:'Sources projet.', description:'Photos, CR, mails, plans, CCTP, AE, factures.', next:'Relier aux runs ou évidences.', chips:[['Scène','yellow'],['Sources','muted']], children:[
            {id:'damps-cr-docs', type:'subject', title:'CR chantier', scene:'documents', summary:'Documents du dernier CR.', scope:'Projet Les Damps · Documents', next:'Relier aux observations.', chips:[['Docs 4','blue']], children:[
              {id:'doc-cr-n-1', type:'document', title:'CR précédent n-1', scene:'documents', summary:'Source historique.', source:'PDF projet.', freshness:'Date à confirmer.', next:'Relier aux points maintenus.', chips:[['PDF','blue'],['Source','muted']]},
              {id:'doc-photo-support', type:'document', title:'Photo support escalier', scene:'documents', summary:'Photo à analyser avec prudence.', source:'Image chantier.', freshness:'Date fichier à confirmer.', next:'Demander autre angle si besoin.', chips:[['Photo','yellow'],['Gap possible','orange']]},
              {id:'doc-audio-reunion', type:'document', title:'Audio réunion chantier', scene:'documents', summary:'Support de transcription non probant seul.', source:'Audio utilisateur.', freshness:'À transcrire.', next:'Extraire points candidats.', chips:[['Audio','blue'],['Non probant','yellow']]},
              {id:'doc-mail-retard', type:'document', title:'Mail entreprise — retard support', scene:'documents', summary:'Échange à vérifier avant formulation.', source:'Mail projet.', freshness:'Date à confirmer.', next:'Relier à Trace ou Evidence.', chips:[['Mail','blue'],['À vérifier','yellow']]}
            ]},
            {id:'damps-factures-docs', type:'subject', title:'Factures', scene:'documents', summary:'Pièces marché pour analyse facture.', scope:'Projet Les Damps · Documents', next:'Croiser facture, AE, CCTP, assurance.', chips:[['Docs 4','blue']], children:[
              {id:'doc-facture-msb', type:'document', title:'Facture MSB — situation 01', scene:'documents', summary:'Facture à analyser.', source:'PDF facture.', freshness:'Version reçue à dater.', next:'Comparer au marché.', chips:[['Facture','yellow'],['Paiement','red']]},
              {id:'doc-ae-msb', type:'document', title:'Acte d’engagement MSB', scene:'documents', summary:'Pièce contractuelle de comparaison.', source:'Marché signé.', freshness:'Version à confirmer.', next:'Contrôler montant et périmètre.', chips:[['Marché','blue'],['Source forte','green']]},
              {id:'doc-cctp-go', type:'document', title:'CCTP gros œuvre', scene:'documents', summary:'Contrôle du périmètre de prestation.', source:'CCTP projet.', freshness:'Indice à vérifier.', next:'Identifier lot concerné.', chips:[['CCTP','blue'],['Lot','yellow']]},
              {id:'doc-assurance-msb', type:'document', title:'Assurance MSB', scene:'documents', summary:'Vérifier activité précise assurée.', source:'Attestation entreprise.', freshness:'Validité à contrôler.', next:'Comparer activité/prestation.', chips:[['Décennale','red'],['À vérifier','yellow']]}
            ]}
          ]},
          {id:'damps-traces', type:'scene', title:'Traces', scene:'traces', summary:'Historique de travail et contraintes.', description:'Ledger non canonique.', next:'Utiliser pour relire le run.', chips:[['Scène','muted'],['Ledger','blue']], children:[
            {id:'damps-cr-traces', type:'subject', title:'CR chantier', scene:'traces', summary:'Contraintes du CR.', scope:'Projet Les Damps · Traces', next:'Maintenir avant finalisation.', chips:[['Traces 3','muted']], children:[
              {id:'trace-no-opc', type:'trace', title:'Pas de posture OPC', scene:'traces', summary:'Les délais doivent rester alerte, pas pilotage.', event:'Correction utilisateur.', impact:'Formulations délai.', next:'Maintenir.', chips:[['Retenue','green'],['Responsabilité','red']]},
              {id:'trace-photo-gap', type:'trace', title:'Gap photo', scene:'traces', summary:'Localisation de la photo incertaine.', event:'Analyse image insuffisante.', impact:'Bloque observation ferme.', next:'Demander autre angle.', chips:[['Gap','yellow'],['Image','blue']]},
              {id:'trace-hors-mission', type:'trace', title:'Hors mission', scene:'traces', summary:'Rappeler limite de responsabilité si nécessaire.', event:'Règle utilisateur.', impact:'Mails et CR.', next:'Maintenir.', chips:[['Retenue','green'],['Mission','red']]}
            ]}
          ]},
          {id:'damps-status', type:'scene', title:'Status', scene:'status', summary:'Synthèse par sujet.', description:'État, blocages et prochaine action.', next:'Lire avant action.', chips:[['Scène','green'],['Synthèse','blue']], children:[
            {id:'damps-cr-status', type:'subject', title:'CR chantier', scene:'status', summary:'État du CR chantier.', scope:'Projet Les Damps · Status', next:'Relire gates.', chips:[['À valider','yellow']], children:[
              {id:'status-cr', type:'status', title:'État CR chantier', scene:'status', summary:'Version candidate prête mais non transmissible.', open:'2 points ouverts, 1 clôture candidate.', blocked:'Envoi bloqué par gate externe.', next:'Relire points à vérifier.', chips:[['À valider','yellow'],['Gates 3','red']]}
            ]},
            {id:'damps-fact-status', type:'subject', title:'Factures', scene:'status', summary:'État analyse factures.', scope:'Projet Les Damps · Status', next:'Vérifier pièces marché.', chips:[['Bloqué','red']], children:[
              {id:'status-factures', type:'status', title:'État factures', scene:'status', summary:'Non finalisable sans AE/CCTP/avancement.', open:'1 facture, 1 devis sup.', blocked:'Assurance et lot à vérifier.', next:'Ouvrir gate paiement.', chips:[['Bloqué','red'],['Pièces manquantes','yellow']]}
            ]}
          ]},
          {id:'damps-gates', type:'scene', title:'Gates', scene:'gates', summary:'Décisions attendues.', description:'Envoi, paiement, Notion, mémoire.', next:'Décider ou reporter.', chips:[['Scène','red'],['Décision','orange']], children:[
            {id:'damps-cr-gates', type:'subject', title:'CR chantier', scene:'gates', summary:'Gates du compte rendu.', scope:'Projet Les Damps · Gates', next:'Traiter avant envoi.', chips:[['Gates 2','red']], children:[
              {id:'gate-envoi-cr', type:'gate', title:'Envoi CR chantier', scene:'gates', summary:'Transmission externe non validée.', decision:'Valider / corriger / garder brouillon.', reason:'Le CR engage l’agence.', next:'Décision humaine explicite.', chips:[['Ouvert','red'],['Effet externe','orange']]},
              {id:'gate-notion-cr', type:'gate', title:'Écriture Notion', scene:'gates', summary:'Inscription d’observations dans le suivi.', decision:'Écrire / reporter / refuser.', reason:'Trace projet persistante.', next:'Valider contenu.', chips:[['Ouvert','red'],['Mémoire projet','blue']]}
            ]},
            {id:'damps-fact-gates', type:'subject', title:'Factures', scene:'gates', summary:'Gates paiement et réserve.', scope:'Projet Les Damps · Gates', next:'Décider après analyse.', chips:[['Gates 2','red']], children:[
              {id:'gate-paiement-msb', type:'gate', title:'Paiement facture MSB', scene:'gates', summary:'Aucun avis favorable sans validation.', decision:'Valider / réserver / refuser.', reason:'Impact financier.', next:'Contrôler pièces.', chips:[['Paiement','red'],['Client','orange']]},
              {id:'gate-reponse-devis-sup', type:'gate', title:'Réponse devis supplémentaire', scene:'gates', summary:'Réponse à cadrer hors validation technique si hors mission.', decision:'Répondre / demander pièces / refuser de se prononcer.', reason:'Responsabilité agence.', next:'Choisir posture.', chips:[['Responsabilité','red'],['Hors mission possible','orange']]}
            ]}
          ]}
        ]
      },
      {id:'project-poussin', type:'project', title:'Poussin', scene:'status', summary:'Projet avec contexte contentieux / report. Exemple de projet à risque procédural.', phase:'PC accordé · recours / report', scope:'Surélévation + rénovation intérieure', next:'Conserver statut et limites avant toute relance.', chips:[['À surveiller','yellow'],['Contentieux','red']], children:[
        {id:'poussin-status', type:'scene', title:'Status', scene:'status', summary:'État général du dossier.', description:'Report, recours et limites de mission.', next:'Ne pas produire de réponse externe sans gate.', chips:[['Scène','green']], children:[
          {id:'poussin-recours', type:'subject', title:'Recours voisin', scene:'status', summary:'Sujet juridique/procédural sensible.', scope:'Projet Poussin · Status', next:'Qualifier avec pièces et conseil adapté.', chips:[['Risque fort','red']], children:[
            {id:'status-poussin-recours', type:'status', title:'État recours', scene:'status', summary:'Le projet est reporté ; aucune décision technique ne doit masquer le risque procédure.', open:'Recours / contentieux à suivre.', blocked:'Calendrier travaux suspendu.', next:'Conserver trace et décisions clients.', chips:[['Bloqué','red'],['Procédure','orange']]}
          ]}
        ]},
        {id:'poussin-documents', type:'scene', title:'Documents', scene:'documents', summary:'Pièces du dossier.', description:'PC, échanges mairie, ABF, recours, notes client.', next:'Qualifier avant usage.', chips:[['Scène','yellow']], children:[
          {id:'poussin-pc', type:'subject', title:'Permis', scene:'documents', summary:'Documents administratifs du PC.', scope:'Projet Poussin · Documents', next:'Vérifier version et décision.', chips:[['Permis','blue']], children:[
            {id:'doc-poussin-pc', type:'document', title:'Arrêté PC accordé', scene:'documents', summary:'Pièce administrative principale.', source:'Mairie / instruction.', freshness:'Version à confirmer.', next:'Lier au status projet.', chips:[['Source forte','green'],['PC','blue']]}
          ]}
        ]}
      ]}
    ]}
  };

  const state = { path:[0] };

  function esc(value){ return String(value == null ? '' : value).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#039;'); }
  function typeConfig(type){ return PC_CARD_TYPES[type] || PC_CARD_TYPES.generic; }
  function nodeAtPath(path){ let node = PC_DECK_CONFIG.root; path.forEach(index => { if(node && node.children && node.children[index]) node = node.children[index]; }); return node; }
  function currentNode(){ return nodeAtPath(state.path) || (PC_DECK_CONFIG.root.children || [])[0]; }
  function parentNode(){ return nodeAtPath(state.path.slice(0,-1)) || PC_DECK_CONFIG.root; }
  function currentSiblings(){ return (parentNode().children || []); }
  function activeIndex(){ return state.path[state.path.length - 1] || 0; }
  function breadcrumb(){ const parts = [{title:PC_DECK_CONFIG.root.title, path:[0]}]; let node = PC_DECK_CONFIG.root; state.path.forEach((index, depth) => { node = node.children[index]; parts.push({title:node.title, path:state.path.slice(0, depth + 1)}); }); return parts; }
  function renderChip(chip){ if(!chip) return ''; const label = Array.isArray(chip) ? chip[0] : chip; const tone = Array.isArray(chip) ? chip[1] : 'muted'; return '<span class="pc-chip pc-chip--'+esc(tone)+'">'+esc(label)+'</span>'; }
  function labelFor(key){ return ({phase:'Phase', scope:'Périmètre', next:'Prochaine action', description:'Description', output:'Sortie', source:'Source', freshness:'Fraîcheur', event:'Événement', impact:'Impact', open:'Ouvert', blocked:'Bloqué', decision:'Décision', reason:'Motif', family:'Famille', authority:'Autorité', version:'Version', effect:'Effet', tool:'Outil'})[key] || key; }
  function renderFields(node, cfg){ return (cfg.fields || []).filter(key => node[key]).map(key => '<p class="pc-card__field"><span>'+esc(labelFor(key))+'</span><b>'+esc(node[key])+'</b></p>').join(''); }
  function renderDetailRows(node, cfg){
    const children = node.children || [];
    const rows = [['ID', node.id || ''], ['Type', node.type || 'carte'], ['Statut', (node.chips || []).map(c => Array.isArray(c) ? c[0] : c).join(' · ')], ['Résumé', node.summary || '']];
    (cfg.fields || []).forEach(key => { if(node[key]) rows.push([labelFor(key), node[key]]); });
    rows.push(['Enfants', children.length ? children.map(c => c.title).join(' · ') : 'Aucun enfant configuré']);
    rows.push(['Effet', 'Détail consultatif uniquement. Aucune validation, mémoire ou action externe.']);
    return rows.filter(row => row[1]).map(row => '<p class="pc-detail-row"><span>'+esc(row[0])+'</span><b>'+esc(row[1])+'</b></p>').join('');
  }

  function renderCard(node, index){
    const cfg = typeConfig(node.type);
    const hasChildren = Array.isArray(node.children) && node.children.length > 0;
    const chips = (node.chips || []).map(renderChip).join('');
    const fields = renderFields(node, cfg);
    const detailRows = renderDetailRows(node, cfg);
    const sceneClass = node.scene ? ' scene-' + esc(node.scene) : '';
    const descend = hasChildren ? '<button class="pc-open-card" data-descend-index="'+index+'">Descendre</button>' : '<button class="pc-open-card" data-detail-toggle="true">Détail</button>';
    return '<article class="pc-card '+esc(cfg.className)+sceneClass+'" data-card-index="'+index+'" data-node-id="'+esc(node.id || '')+'">'+
      '<div class="pc-card__front"><div class="pc-card__bg-word">'+esc(node.bg || cfg.bg || cfg.label)+'</div><div class="pc-card__inner"><header class="pc-card__header"><span class="pc-card__eyebrow">'+esc(cfg.label)+' · '+esc(node.type || 'carte')+'</span><h3 class="pc-card__title">'+esc(node.title)+'</h3></header><p class="pc-card__summary">'+esc(node.summary || '')+'</p>'+(fields ? '<div class="pc-card__fields">'+fields+'</div>' : '')+'<footer class="pc-card__footer">'+chips+descend+'</footer></div></div>'+
      '<div class="pc-card__detail" aria-hidden="true"><div><span class="pc-card__eyebrow">Détail · '+esc(cfg.label)+'</span><h3 class="pc-card__detail-title">'+esc(node.title)+'</h3></div><div class="pc-detail-rows">'+detailRows+'</div><footer class="pc-card__footer"><button class="pc-open-card" data-detail-toggle="true">Retour carte</button>'+(hasChildren ? '<button class="pc-open-card" data-descend-index="'+index+'">Descendre</button>' : '')+'</footer></div>'+ 
    '</article>';
  }

  function renderSiblingRail(){
    const children = currentSiblings();
    const active = activeIndex();
    if(!children.length) return '';
    return '<nav class="pc-sibling-rail" aria-label="Cartes sœurs">'+children.map((child, index) => '<button class="pc-sibling '+(index===active?'is-active':'')+'" data-sibling="'+index+'">'+esc(child.title)+'</button>').join('')+'</nav>';
  }
  function renderMiniNav(){
    const crumbs = breadcrumb();
    return '<section class="pc-deck-nav"><nav class="pc-breadcrumb">'+crumbs.map((c,i)=>'<button data-crumb="'+i+'">'+(i===0?'⌂':esc(c.title))+'</button>').join('<span>›</span>')+'</nav>'+renderSiblingRail()+'</section>';
  }
  function renderSiblingDeck(){
    const children = currentSiblings();
    if(!children.length) return '<section class="pc-empty"><b>Aucune carte sœur.</b><p>Rien à afficher pour ce niveau.</p></section>';
    return '<section class="pc-deck-frame pc-axis-horizontal"><div class="swiper pc-card-swiper" data-axis="horizontal"><div class="swiper-wrapper">'+children.map((child, index) => '<div class="swiper-slide">'+renderCard(child, index)+'</div>').join('')+'</div><div class="swiper-pagination"></div></div></section>';
  }

  function renderApp(){
    ensureDetailStyles();
    const node = currentNode();
    const body = '<section class="pc-deck-app scene-'+esc(node.scene || 'runs')+'">'+renderSiblingDeck()+renderMiniNav()+'</section>';
    const page = document.getElementById('page');
    if(page) page.innerHTML = body;
    else { const shell = document.getElementById('shell'); if(shell) shell.innerHTML = body; }
    bindInteractions();
    initSwiper();
  }

  function descendFromIndex(index){
    const siblings = currentSiblings();
    const node = siblings[index];
    if(!node || !node.children || !node.children.length){ toastIfAvailable('Carte feuille : aucun enfant configuré.', 'blue'); return; }
    state.path[state.path.length - 1] = index;
    state.path.push(0);
    renderApp();
  }
  function ascend(){
    if(state.path.length <= 1){ toastIfAvailable('Niveau racine : aucun parent supérieur.', 'blue'); return; }
    state.path.pop();
    renderApp();
  }
  function toggleCardDetail(card){
    if(!card) return;
    const isDetail = card.classList.toggle('is-detail');
    const detail = card.querySelector('.pc-card__detail');
    if(detail) detail.setAttribute('aria-hidden', isDetail ? 'false' : 'true');
  }

  function bindInteractions(){
    document.querySelectorAll('.pc-card').forEach(card => {
      card.addEventListener('click', event => { if(event.target.closest('button')) return; toggleCardDetail(card); });
    });
    document.querySelectorAll('[data-detail-toggle]').forEach(button => {
      button.addEventListener('click', event => { event.stopPropagation(); toggleCardDetail(button.closest('.pc-card')); });
    });
    document.querySelectorAll('[data-descend-index]').forEach(button => {
      button.addEventListener('click', event => { event.stopPropagation(); descendFromIndex(Number(button.getAttribute('data-descend-index'))); });
    });
    document.querySelectorAll('[data-sibling]').forEach(button => {
      button.addEventListener('click', () => { state.path[state.path.length - 1] = Number(button.getAttribute('data-sibling')); renderApp(); });
    });
    document.querySelectorAll('[data-crumb]').forEach(button => {
      button.addEventListener('click', () => { const index = Number(button.getAttribute('data-crumb')); state.path = breadcrumb()[index].path.slice(); renderApp(); });
    });
  }

  function updateActiveRail(index){
    document.querySelectorAll('[data-sibling]').forEach(btn => btn.classList.toggle('is-active', Number(btn.getAttribute('data-sibling')) === index));
  }
  function bindVerticalDepthGesture(swiperEl){
    let startX = 0, startY = 0;
    swiperEl.addEventListener('touchstart', event => {
      const t = event.changedTouches[0]; startX = t.clientX; startY = t.clientY;
    }, {passive:true});
    swiperEl.addEventListener('touchend', event => {
      const t = event.changedTouches[0];
      const dx = t.clientX - startX;
      const dy = t.clientY - startY;
      if(Math.abs(dy) < 70 || Math.abs(dy) < Math.abs(dx) * 1.25) return;
      if(dy < 0) descendFromIndex(activeIndex());
      else ascend();
    }, {passive:true});
  }

  function initSwiper(){
    if(!window.Swiper) return;
    const swiperEl = document.querySelector('.pc-card-swiper');
    if(!swiperEl) return;
    const swiper = new Swiper(swiperEl, {
      direction:'horizontal', slidesPerView:1, spaceBetween:14, keyboard:true,
      pagination:{el:'.swiper-pagination', clickable:true}, initialSlide:activeIndex(), resistanceRatio:.7
    });
    swiper.on('slideChange', () => {
      state.path[state.path.length - 1] = swiper.activeIndex;
      updateActiveRail(swiper.activeIndex);
    });
    bindVerticalDepthGesture(swiperEl);
    document.addEventListener('keydown', event => {
      if(event.key === 'ArrowUp') descendFromIndex(activeIndex());
      if(event.key === 'ArrowDown') ascend();
    }, {once:true});
  }

  function ensureDetailStyles(){
    if(document.getElementById('pc-detail-style')) return;
    const style = document.createElement('style');
    style.id = 'pc-detail-style';
    style.textContent = '.pc-card__front{min-height:100%;display:block}.pc-card__detail{display:none;position:relative;z-index:3;min-height:100%;flex-direction:column;gap:14px}.pc-card.is-detail .pc-card__front{display:none}.pc-card.is-detail .pc-card__detail{display:flex}.pc-card__detail-title{margin:0;font-size:clamp(30px,8vw,64px);line-height:.9;letter-spacing:-.06em}.pc-detail-rows{display:grid;gap:8px}.pc-detail-row{margin:0;border-top:1px solid rgba(255,255,255,.08);padding-top:8px;display:grid;grid-template-columns:minmax(90px,180px) 1fr;gap:12px;color:var(--muted);font-size:13px}.pc-detail-row b{color:var(--fg);font-weight:600}.pc-deck-nav{margin-top:8px}.pc-open-card{touch-action:manipulation}@media(max-width:720px){.pc-detail-row{display:block}.pc-detail-row b{display:block;margin-top:2px}}';
    document.head.appendChild(style);
  }
  function toastIfAvailable(message, tone){ if(typeof toast === 'function') toast(message, tone || 'blue'); }

  window.renderDeckApp = renderApp;
  document.addEventListener('DOMContentLoaded', renderApp);
})();
