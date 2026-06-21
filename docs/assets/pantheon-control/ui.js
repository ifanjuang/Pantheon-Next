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

function safeName(s){
  return String(s||'').replace(/'/g,'');
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

function depotLien(d){
  return d.indexOf('github.com')===0 ? '<a href="https://'+d+'" target="_blank" rel="noopener">'+d+'</a>' : d;
}

function renderServiceActions(s){
  const b=[];
  if(!s.installe){ b.push('<button class="primary" onclick="demanderService(this,\'Préparation ajout\',\''+s.nom+'\')">Préparer ajout</button>'); }
  if(s.installe && s.maj){ b.push('<button class="primary" onclick="demanderService(this,\'Préparation mise à jour\',\''+s.nom+'\')">Préparer MAJ ('+s.version+' → '+s.maj+')</button>'); }
  if(s.installe && !s.systeme){ b.push('<button onclick="demanderService(this,\'Préparation retrait\',\''+s.nom+'\')">Préparer retrait</button>'); }
  if(s.systeme){ b.push('<span class="chip muted">service système · pas de retrait</span>'); }
  return b.join('');
}

function renderServiceCard(s){
  return '<div class="card"><h3>'+s.nom+info(s.role)+' '+chip(s.etat[0],s.etat[1])+'</h3>'+
    kv('Catégorie', s.categorie)+
    kv('Port', s.port)+
    kv('Version', s.version+(s.maj?' '+chip('MAJ '+s.maj,'blue'):''))+
    kv('Dépôt', depotLien(s.depot))+
    kv('Dépendances', s.deps.join(', '))+
    '<p style="margin-top:10px">'+renderServiceActions(s)+'</p></div>';
}

function renderServicesGrid(){
  const c=document.getElementById('cat').value;
  document.getElementById('grid').innerHTML = SERVICES.filter(s=>c==='Toutes'||s.categorie===c).map(renderServiceCard).join('');
}

function demanderService(btn, quoi, nom){
  btn.textContent='Demande préparée ✓'; btn.disabled=true;
  document.getElementById('out').textContent = quoi+' de « '+nom+' » : demande candidate préparée. Aucun effet réel.\n\n'+document.getElementById('out').textContent;
  toast(quoi+' : '+nom,'blue');
}

function renderServicesPage(){
  const cats = ['Toutes'].concat([...new Set(SERVICES.map(s=>s.categorie))]);
  return panel('Limite','<p>Les boutons préparent une demande. Ils ne changent aucun service dans cette maquette.</p>')+
    '<div class="toolbar"><select id="cat" onchange="renderServicesGrid()">'+cats.map(c=>'<option>'+c+'</option>').join('')+'</select></div>'+
    '<div id="grid" class="grid"></div>'+
    panel('Demandes candidates','<pre id="out">Aucune demande.</pre>');
}

function renderMachineCard(m){
  const modeles = m.modeles.length ? m.modeles.map(x=>chip(x,'blue')).join('') : '<span class="chip muted">aucun modèle</span>';
  const wol = m.etat[0]==='Éteint' ? '<p><button onclick="reveillerMachine(this,\''+m.nom+'\')">Préparer le réveil</button></p>' : '';
  return '<div class="card"><h3>'+m.nom+' '+chip(m.etat[0],m.etat[1])+'</h3>'+
    kv('Adresse IP', m.ip)+kv('Carte graphique', m.gpu)+kv('Mémoire', m.ram)+kv('Processeur', m.cpu)+
    '<p style="margin-top:10px">Modèles hébergés</p>'+modeles+wol+'</div>';
}

function reveillerMachine(btn, nom){
  btn.textContent='Réveil demandé ✓'; btn.disabled=true;
  document.getElementById('out').textContent = 'Réveil de « '+nom+' » demandé.\n\n'+document.getElementById('out').textContent;
  toast('Réveil préparé : '+nom,'blue');
}

function renderMachinesPage(){
  return '<div class="grid">'+MACHINES.map(renderMachineCard).join('')+'</div>'+panel('Demandes','<pre id="out">Aucune demande.</pre>');
}

function renderProviderCard(p){
  const connecte = p.etat[0]==='Connecté';
  const btns = connecte
    ? '<button onclick="configProvider(this,\''+p.nom+'\')">Préparer configuration</button>'
    : '<button class="primary" onclick="configProvider(this,\''+p.nom+'\')">Préparer connexion</button><button onclick="configProvider(this,\''+p.nom+'\')">Préparer configuration</button>';
  return '<div class="card"><h3>'+p.nom+info(p.usage)+' '+chip(p.etat[0],p.etat[1])+'</h3>'+ 
    '<p>'+p.usage+'</p>'+kv('Type', p.type)+kv('Modèles', p.modeles)+'<p style="margin-top:10px">'+btns+'</p></div>';
}

function configProvider(btn, nom){
  document.getElementById('out').textContent = 'Demande candidate pour « '+nom+' » : clé API, modèles autorisés, coûts et périmètre à confirmer. Aucun changement réel.\n\n'+document.getElementById('out').textContent;
  toast('Demande candidate préparée : '+nom,'blue');
}

function renderIaPage(){
  const couts = AI_COSTS.map(c=>'<li><b>'+c.poste+'</b> '+chip(c.montant,'blue')+'<br><span class="t">'+c.detail+'</span></li>');
  return '<div class="grid">'+PROVIDERS.map(renderProviderCard).join('')+'</div>'+ 
    '<p class="hint">Les modèles locaux et leurs machines sont détaillés sur la page <a href="machines.html">Machines</a>.</p>'+ 
    '<div class="grid two">'+
      panel('Usage & coûts fictifs', queue(couts), 'Les tokens restent disponibles comme détail technique ; la vue cabinet privilégie coût par projet et fonction.')+
      panel('Configuration candidate','<pre id="out">Aucune demande préparée.</pre>')+
    '</div>';
}

function renderSkillCard(s){
  const etat = s.actif ? chip('Actif','green') : chip('Inactif','muted');
  const action = s.actif ? '' : '<p><button onclick="activerSkill(this,\''+s.nom+'\')">Activer</button></p>';
  return '<div class="card"><h3>'+s.nom+' '+etat+'</h3><p>'+s.usage+'</p>'+action+'</div>';
}

function activerSkill(btn, nom){
  confirmAct('Demander l\'activation du skill « '+nom+' » ?','Demander l\'activation',()=>{
    btn.textContent='Activation demandée ✓'; btn.disabled=true;
    toast('Demande préparée : '+nom,'blue');
  });
}

function renderSkillsPage(){
  return '<div class="grid">'+SKILLS.map(renderSkillCard).join('')+'</div>';
}

function renderFileCard(f){
  return '<div class="card"><h3>'+f.nom+'</h3>'+ '<p>'+f.type+' · '+f.projet+'</p>'+ chip(f.lecture[0],f.lecture[1])+' '+chip(f.statut[0],f.statut[1])+
    '<p style="margin-top:8px"><button onclick="proposerSource(this,\''+safeName(f.nom)+'\')">Utiliser comme source</button></p></div>';
}

function renderFilesGrid(){
  const q=(document.getElementById('q').value||'').toLowerCase();
  const p=document.getElementById('p').value;
  const rows=FICHIERS.filter(f=>(p==='Tous'||f.projet===p) && (f.nom+' '+f.type+' '+f.projet).toLowerCase().includes(q));
  document.getElementById('grid').innerHTML=rows.map(renderFileCard).join('');
}

function proposerSource(btn, nom){
  btn.textContent='Ajouté ✓'; btn.disabled=true;
  document.getElementById('out').textContent='« '+nom+' » proposé comme source.\n\n'+document.getElementById('out').textContent;
  toast('Source proposée : '+nom,'blue');
}

function renderFilesPage(){
  const projets = ['Tous'].concat([...new Set(FICHIERS.map(f=>f.projet))]);
  return '<div class="toolbar"><input id="q" placeholder="filtrer…" oninput="renderFilesGrid()">'+
    '<select id="p" onchange="renderFilesGrid()">'+projets.map(p=>'<option>'+p+'</option>').join('')+'</select></div>'+ 
    '<div id="grid" class="grid"></div>'+ 
    panel('Sources proposées','<pre id="out">Aucune.</pre>');
}

function renderBaseMemoryPage(){
  return '<div class="grid">'+BASE.map(b=>'<div class="card"><h3>'+b.nom+'</h3><p>'+b.role+'</p>'+chip(b.statut[0],b.statut[1])+'</div>').join('')+'</div>';
}

function renderSurveillancePage(){
  const controles = CONTROLES.map(c=>'<div class="card"><h3>'+c.label+'</h3>'+chip(c.resultat[0],c.resultat[1])+'</div>').join('');
  const journal = JOURNAL.map(j=>'<li><span class="t">'+j.t+'</span><br>'+j.msg+'</li>');
  return '<h3 class="chapter">Contrôles automatiques</h3><div class="grid">'+controles+'</div>'+panel('Journal d’activité', queue(journal));
}
