/* Pantheon Control — page Services & connexions.
   Candidate display only. No service, account, connector or route is changed. */

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
  return panel('Limite','<p>Les boutons préparent une demande. Ils ne changent aucun service, compte, connecteur, accès sécurisé ou routage dans cette maquette.</p>')+
    '<h3 class="chapter">Services internes / outils</h3>'+ 
    '<div class="toolbar"><select id="cat" onchange="renderServicesGrid()">'+cats.map(c=>'<option>'+c+'</option>').join('')+'</select></div>'+ 
    '<div id="grid" class="grid"></div>'+ 
    '<h3 class="chapter">Connexions externes</h3>'+ 
    '<div class="grid">'+EXTERNAL_CONNECTIONS.map(renderConnectionCard).join('')+'</div>'+ 
    '<h3 class="chapter">Accès sécurisé & routage</h3>'+ 
    '<div class="grid">'+ACCESS_CONNECTIONS.map(renderConnectionCard).join('')+'</div>'+ 
    panel('Demandes candidates','<pre id="out">Aucune demande.</pre>');
}
