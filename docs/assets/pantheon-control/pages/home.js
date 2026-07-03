/* Pantheon Control — page Accueil.
   Page module only. Candidate display, no runtime action. */

function renderHomeSummary(){
  const enLigne = SERVICES.filter(s=>s.etat[0]==='En ligne').length;
  const connexions = EXTERNAL_CONNECTIONS.filter(c=>c.etat[0]==='Connecté').length;
  const accesses = ACCESS_CONNECTIONS.filter(c=>c.etat[0]==='Connecté').length;
  const machinesOn = MACHINES.filter(m=>m.etat[0]==='Allumé').length;
  const instancesOn = LOCAL_INSTANCES.filter(i=>i.etat[0]==='En ligne').length;
  const skillsActifs = SKILLS.filter(s=>s.actif).length;
  const aExaminer = EVIDENCE.filter(e=>e.statut[0]!=='Référence').length;

  return '<div class="grid">' +
    card('Services & connexions', '<p>'+enLigne+'/'+SERVICES.length+' services en ligne</p><p>'+connexions+'/'+EXTERNAL_CONNECTIONS.length+' connexions actives</p><p>'+accesses+'/'+ACCESS_CONNECTIONS.length+' accès actifs</p>', 'services.html')+
    card('Machines & instances', '<p>'+machinesOn+'/'+MACHINES.length+' machines allumées</p><p>'+instancesOn+'/'+LOCAL_INSTANCES.length+' instances locales en ligne</p>', 'machines.html')+
    card('Observabilité', '<p>Langfuse : lien et santé uniquement</p>'+chip('Candidate','blue')+' '+chip('iframe refusée','muted'), 'observability.html')+
    card('Skills', '<p>'+skillsActifs+'/'+SKILLS.length+' actifs</p>', 'skills.html')+
    card('Preuves & sources', '<p>'+aExaminer+' à examiner</p><p><a href="evidence.html">Ouvrir</a> · <a href="evidence.html">Tester mobile</a></p>')+
    card('Fichiers', '<p>'+FICHIERS.length+' fichiers suivis</p>', 'files.html')+
  '</div>';
}

function renderStackChoicePanel(){
  return '<div class="panel">'+
    '<h3>Pourquoi OpenWebUI + Hermes + Pantheon ?</h3>'+
    '<p>Le choix de cette organisation vient d’un besoin très concret : utiliser l’IA dans un cadre professionnel sans mélanger l’espace de discussion, le travail préparatoire de l’assistant et la validation de ce qui pourra réellement être utilisé.</p>'+
    '<div class="grid three">'+
      '<div class="card"><h3>OpenWebUI, l’espace de travail visible</h3><p>OpenWebUI apporte une interface lisible pour dialoguer avec plusieurs IA, retrouver les documents, consulter des bases de connaissance, suivre les sources et afficher les cartes du cockpit. Sa force est de rendre le travail avec l’IA partageable et compréhensible par l’équipe, sans que l’interface devienne une autorité en elle-même.</p></div>'+
      '<div class="card"><h3>Hermes, la mémoire active et les skills</h3><p>Hermes est intéressant parce qu’il ne se limite pas à répondre dans une conversation. Il peut mobiliser des skills, c’est-à-dire des méthodes de travail réutilisables : relire un dossier, comparer des pièces, préparer une note, vérifier une procédure, organiser une recherche. Il peut conserver une mémoire de travail et documenter les étapes réalisées.</p></div>'+
      '<div class="card"><h3>Pantheon, le cadre qui évite la confusion</h3><p>Pantheon intervient là où le risque apparaît : croire une réponse trop vite, garder une mauvaise mémoire, utiliser une source insuffisante, envoyer une action sans validation, ou confondre une synthèse bien rédigée avec une décision professionnelle. Il qualifie les statuts, les preuves, le périmètre, la mémoire et les validations nécessaires.</p></div>'+
    '</div>'+
    '<div class="grid two" style="margin-top:12px">'+
      '<div class="card"><h3>Ce que permet OpenWebUI</h3><p>Dans un cabinet, il faut que l’IA reste visible et discutable. OpenWebUI sert à exposer les échanges, les documents, les sources, les fichiers et les décisions attendues dans un espace que l’équipe peut comprendre. C’est moins un moteur qu’un lieu de consultation et de pilotage.</p></div>'+
      '<div class="card"><h3>Ce que permet Hermes</h3><p>Hermes sert à porter le travail répétable et méthodique : des skills, une mémoire de travail, des vérifications, des traces et des tâches qui peuvent être préparées hors de l’interface. Ce qu’il produit peut être propre, structuré et utile, mais reste une proposition à contrôler avant usage.</p></div>'+
    '</div>'+
    '<p class="t" style="margin-top:12px">Le principe n’est donc pas de faire confiance à un outil unique. L’interface rend le travail lisible, Hermes prépare et documente, Pantheon qualifie ce qui peut être retenu, validé, mémorisé ou transmis.</p>'+
  '</div>';
}

function renderWorkflowPanel(){
  const wf = WORKFLOW_PROPOSALS[0];
  return '<div class="panel"><h3>Workflow proposé</h3>'+
    chip(wf.risque[0],wf.risque[1])+' '+chip(wf.statut[0],wf.statut[1])+
    '<p><b>'+wf.titre+'</b></p>'+
    '<p>'+wf.demande+'</p>'+
    kv('Mission', wf.mission)+
    kv('Sortie', wf.sortie)+
    kv('Effet externe', wf.effet)+
    '<div class="cascade"><span class="lbl">Pièces manquantes</span><ul>'+wf.manques.map(m=>'<li>'+m+'</li>').join('')+'</ul></div>'+
    '<p style="margin-top:10px"><a href="discussion.html">Ouvrir la discussion</a> · <a href="evidence.html">Voir preuves & sources</a></p>'+
  '</div>';
}

function renderPriorityPanels(){
  const aExaminer = EVIDENCE.filter(e=>e.statut[0]!=='Référence').length;
  const impacts = IMPACTS.map(i=>
    '<li><b>'+i.declencheur+'</b> '+chip(i.gravite[0],i.gravite[1])+'<br><span class="t">touche : '+i.touche+'</span></li>'
  );
  const couts = AI_COSTS.map(c=>
    '<li><b>'+c.poste+'</b> '+chip(c.montant,'blue')+'<br><span class="t">'+c.detail+'</span></li>'
  );
  return '<div class="grid two">'+
    panel('À traiter en priorité', queue(impacts), aExaminer+' élément(s) de preuve ou source en attente d’examen.')+
    panel('Coûts IA — vue cabinet', queue(couts), 'Chiffres fictifs : les tokens restent un détail technique.')+
  '</div>';
}

function renderHomePage(){
  const testMobile = panel(
    'Test rapide — revue mobile des preuves',
    '<p>Ouvrir directement la maquette Swiper.js : sujets en swipe horizontal, affaires en swipe vertical, options rondes sur appui long.</p><p><a href="evidence.html" class="primary-link">Tester la vue Preuves & sources mobile</a></p>',
    'Lien de test uniquement : les gestes préparent des intentions candidates, sans effet réel.'
  );
  const references = panel(
    'Références & doctrine candidate',
    '<p>RAG probatoire, références externes et suivis HTML sont regroupés dans une page dédiée du cockpit.</p><p><a href="references.html" class="primary-link">Ouvrir le centre de références</a> · <a href="../../rag-probatoire.html">Page RAG probatoire</a></p>',
    'Aucune référence affichée ici ne devient canonique sans qualification et décision humaine.'
  );
  return renderStackChoicePanel() + testMobile + references + renderHomeSummary() + renderWorkflowPanel() + renderPriorityPanels();
}
