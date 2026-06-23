/* Pantheon Control — page Machines & instances.
   Candidate display only. No wake-on-LAN, runtime or model operation is executed. */

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

function renderMachinesPage(){
  return '<h3 class="chapter">Machines locales</h3>'+ 
    '<div class="grid">'+MACHINES.map(renderMachineCard).join('')+'</div>'+ 
    '<h3 class="chapter">Instances locales & modèles</h3>'+ 
    '<div class="grid">'+LOCAL_INSTANCES.map(renderLocalInstanceCard).join('')+'</div>'+ 
    panel('Demandes','<pre id="out">Aucune demande.</pre>');
}
