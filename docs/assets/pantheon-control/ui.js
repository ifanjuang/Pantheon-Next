/* Pantheon Control — helpers de rendu partagés.
   Documenté non implémenté. Ces fonctions affichent des données candidates ; elles ne valident rien. */

function panel(title, body, hint){
  return '<div class="panel">'+
    '<h3>'+title+'</h3>'+
    body+
    (hint ? '<p class="hint">'+hint+'</p>' : '')+
  '</div>';
}

function card(title, body, href){
  return '<div class="card">'+
    '<h3>'+title+'</h3>'+
    body+
    (href ? '<p><a href="'+href+'">Ouvrir</a></p>' : '')+
  '</div>';
}

function kv(label, value){
  return '<div class="kv"><span>'+label+'</span><b>'+value+'</b></div>';
}

function queue(items){
  return '<ul class="queue">'+items.join('')+'</ul>';
}

function renderReferenceCards(){
  return REFERENCES.map(e =>
    '<div class="card">'+
      chip(e.status[0], e.status[1])+' '+chip(e.authority[0], e.authority[1])+' '+chip('Risque '+e.risk[0], e.risk[1])+
      '<h3>'+e.title+'</h3>'+
      '<p>'+e.summary+'</p>'+
      kv('Prochaine action', e.next)+
      '<p><a href="'+e.href+'" class="primary-link">Ouvrir</a></p>'+
    '</div>'
  ).join('');
}

function renderReferencesPage(){
  return panel(
    'Centre de références',
    '<p>Cette page expose des références, pages candidates et suivis. Elle ne valide rien, ne promeut aucune mémoire et ne déclenche aucune action externe.</p>',
    'Doctrine : retrieval proposes · evidence supports · governance qualifies · approval validates · the human decides.'
  ) + '<div class="grid">'+renderReferenceCards()+'</div>';
}

function renderHomeSummary(){
  const enLigne = SERVICES.filter(s=>s.etat[0]==='En ligne').length;
  const majDispo = SERVICES.filter(s=>s.maj).length;
  const machinesOn = MACHINES.filter(m=>m.etat[0]==='Allumé').length;
  const fournisseurs = PROVIDERS.filter(p=>p.etat[0]==='Connecté').length;
  const skillsActifs = SKILLS.filter(s=>s.actif).length;
  const aExaminer = EVIDENCE.filter(e=>e.statut[0]!=='Référence').length;

  return '<div class="grid">' +
    card('Services', '<p>'+enLigne+'/'+SERVICES.length+' en ligne</p>'+(majDispo?chip(majDispo+' mise(s) à jour','blue'):chip('à jour','green')), 'services.html')+
    card('Machines', '<p>'+machinesOn+'/'+MACHINES.length+' allumées</p>', 'machines.html')+
    card('Observabilité', '<p>Langfuse : lien et santé uniquement</p>'+chip('Candidate','blue')+' '+chip('iframe refusée','muted'), 'observability.html')+
    card('Modèles & IA', '<p>'+fournisseurs+' fournisseur(s) connecté(s)</p>', 'ia.html')+
    card('Skills', '<p>'+skillsActifs+'/'+SKILLS.length+' actifs</p>', 'skills.html')+
    card('Preuves & sources', '<p>'+aExaminer+' à examiner</p><p><a href="evidence.html">Ouvrir</a> · <a href="evidence.html">Tester mobile</a></p>')+
    card('Fichiers', '<p>'+FICHIERS.length+' fichiers suivis</p>', 'files.html')+
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
  return testMobile + references + renderHomeSummary() + renderWorkflowPanel() + renderPriorityPanels();
}
