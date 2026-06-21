/* Pantheon Control — connexions externes et instances locales.
   Documenté non implémenté. Remplace l’onglet IA autonome par :
   Services & connexions = API cloud / comptes / connecteurs Internet / accès distant.
   Machines & instances = matériel local / Ollama / modèles par machine. */

function renderConnectionCard(c){
  const connected = c.etat[0] === 'Connecté';
  const btn = connected ? 'Préparer configuration' : 'Préparer connexion';
  return '<div class="card"><h3>'+c.nom+info(c.usage)+' '+chip(c.etat[0],c.etat[1])+'</h3>'+ 
    '<p>'+c.usage+'</p>'+kv('Type', c.type)+kv('Identité', c.identite)+
    '<p style="margin-top:10px"><button class="'+(connected?'':'primary')+'" onclick="prepareConnection(this,\''+btn+'\',\''+safeName(c.nom)+'\')">'+btn+'</button></p></div>';
}

function prepareConnection(btn, action, nom){
  btn.textContent='Demande préparée ✓'; btn.disabled=true;
  const out = document.getElementById('out');
  if(out) out.textContent = action+' — '+nom+' : scope, compte, coût, preuve et approval à confirmer. Aucun changement réel.\n\n'+out.textContent;
  toast(action+' : '+nom,'blue');
}

function renderLocalInstanceCard(i){
  const modeles = i.modeles.length ? i.modeles.map(x=>chip(x,'blue')).join('') : '<span class="chip muted">aucun modèle</span>';
  const btn = i.etat[0] === 'Éteint' ? 'Préparer réveil' : 'Préparer configuration';
  return '<div class="card"><h3>'+i.nom+' '+chip(i.etat[0],i.etat[1])+'</h3>'+ 
    '<p>'+i.usage+'</p>'+kv('Machine', i.machine)+kv('Service', i.service)+kv('Port', i.port)+
    '<p style="margin-top:10px">Modèles disponibles</p>'+modeles+
    '<p style="margin-top:10px"><button onclick="prepareLocalInstance(this,\''+btn+'\',\''+safeName(i.nom)+'\')">'+btn+'</button></p></div>';
}

function prepareLocalInstance(btn, action, nom){
  btn.textContent='Demande préparée ✓'; btn.disabled=true;
  const out = document.getElementById('out');
  if(out) out.textContent = action+' — '+nom+' : demande candidate locale. Aucun changement réel.\n\n'+out.textContent;
  toast(action+' : '+nom,'blue');
}

function renderServicesPage(){
  const cats = ['Toutes'].concat([...new Set(SERVICES.map(s=>s.categorie))]);
  return panel('Limite','<p>Les boutons préparent une demande. Ils ne changent aucun service, compte, connecteur, VPN ou routage dans cette maquette.</p>')+
    '<h3 class="chapter">Services internes / outils</h3>'+ 
    '<div class="toolbar"><select id="cat" onchange="renderServicesGrid()">'+cats.map(c=>'<option>'+c+'</option>').join('')+'</select></div>'+ 
    '<div id="grid" class="grid"></div>'+ 
    '<h3 class="chapter">Connexions externes</h3>'+ 
    '<div class="grid">'+EXTERNAL_CONNECTIONS.map(renderConnectionCard).join('')+'</div>'+ 
    '<h3 class="chapter">Accès distant & routage</h3>'+ 
    '<div class="grid">'+ACCESS_CONNECTIONS.map(renderConnectionCard).join('')+'</div>'+ 
    panel('Demandes candidates','<pre id="out">Aucune demande.</pre>');
}

function renderMachinesPage(){
  return '<h3 class="chapter">Machines locales</h3>'+ 
    '<div class="grid">'+MACHINES.map(renderMachineCard).join('')+'</div>'+ 
    '<h3 class="chapter">Instances locales & modèles</h3>'+ 
    '<div class="grid">'+LOCAL_INSTANCES.map(renderLocalInstanceCard).join('')+'</div>'+ 
    panel('Demandes','<pre id="out">Aucune demande.</pre>');
}

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

function renderIaMovedPage(){
  return panel('Onglet IA retiré','<p>Les comptes IA cloud sont maintenant dans <a href="services.html">Services & connexions</a>. Les modèles locaux sont configurés par machine dans <a href="machines.html">Machines & instances</a>.</p>','L’IA n’est pas un domaine séparé : c’est soit une connexion externe, soit une capacité locale exécutée sur une machine.');
}
