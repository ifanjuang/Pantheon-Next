/* Pantheon Control — rendu Installations & bootstrap.
   Prépare des demandes candidates. Aucun changement système réel. */

function installLayerCard(l){
  return '<div class="card"><h3>'+l.id+' · '+l.titre+' '+chip(l.etat[0],l.etat[1])+'</h3>'+ 
    '<p>'+l.dependances+'</p>'+kv('Exécution', l.owner)+kv('Rôle Pantheon', l.pantheon)+kv('Prochaine action', l.next)+
    '<p style="margin-top:10px"><button onclick="prepareInstallStep(this,\''+safeName(l.id)+'\')">Préparer étape</button></p></div>';
}

function installProfileCard(p){
  const tone = p.score === 'Recommandé' ? 'green' : (p.score === 'À vérifier' || p.score === 'À prouver' ? 'yellow' : 'blue');
  return '<div class="card"><h3>'+p.nom+' '+chip(p.score,tone)+'</h3><p>'+p.role+'</p>'+kv('Risque', p.risque)+kv('Note', p.notes)+'</div>';
}

function prepareInstallStep(btn, id){
  btn.textContent = 'Demande préparée ✓'; btn.disabled = true;
  const out = document.getElementById('installOut');
  if(out) out.textContent = 'Étape '+id+' : plan candidat, preflight, rollback et décision humaine à préparer. Aucun changement réel.\n\n'+out.textContent;
  toast('Étape '+id+' préparée','blue');
}

function renderInstallationsPage(){
  return panel(
    'Limite',
    '<p>Cette page ne lance aucune installation. Elle rend visible la chaîne d’amorçage avant Hermes : dépendances, états, blocages, rôles et prochaines actions.</p>',
    'Avant Hermes, Pantheon ne peut pas demander à Hermes d’installer Hermes.'
  )+
  '<h3 class="chapter">Chaîne bootstrap</h3>'+ 
  '<div class="grid">'+INSTALL_LAYERS.map(installLayerCard).join('')+'</div>'+ 
  '<h3 class="chapter">Profils recommandés</h3>'+ 
  '<div class="grid">'+INSTALL_PROFILES.map(installProfileCard).join('')+'</div>'+ 
  panel('États possibles','<p>'+INSTALL_STATES.map(s=>chip(s,'muted')).join('')+'</p>')+
  panel('Demandes candidates','<pre id="installOut">Aucune demande.</pre>');
}
