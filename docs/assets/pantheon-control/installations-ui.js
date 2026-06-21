/* Pantheon Control — rendu Installations & bootstrap.
   Prépare des demandes candidates. Aucun changement système réel. */

let nasProfile = {...NAS_PROFILE_DEFAULT};

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

function nasFieldHtml(f){
  const [id,label,type,meta] = f;
  if(type === 'select'){
    return '<label>'+label+'<select id="nas_'+id+'" onchange="updateNasProfile()">'+meta.map(v=>'<option value="'+v+'">'+v+'</option>').join('')+'</select></label>';
  }
  return '<label>'+label+'<input id="nas_'+id+'" placeholder="'+meta+'" oninput="updateNasProfile()"></label>';
}

function scoreNasProfile(p){
  const unknowns = Object.keys(p).filter(k => !p[k] || p[k] === 'inconnu' || p[k] === 'inconnue').length;
  const hasGateway = p.reverse_proxy === 'oui' || p.vpn === 'oui';
  const hasSubstrate = p.containers === 'oui' || p.vm === 'oui';
  const hasGpu = p.gpu === 'GPU exploitable';
  const hasNpu = p.npu === 'oui';
  const hasBackup = p.backup === 'oui';
  const ramStrong = p.ram === '16 Go' || p.ram === '32 Go +';

  if(unknowns >= 5) return {profil:'NAS stockage + cockpit statique', statut:['Profil prudent','blue'], risque:'Faible', reco:'Trop d’inconnues. Utiliser le NAS comme stockage, documentation statique et éventuelle redirection privée.'};
  if(!hasBackup) return {profil:'Baseline à sécuriser', statut:['Bloqué sauvegarde','red'], risque:'Élevé', reco:'Clarifier backup/snapshot avant tout substrat ou runtime.'};
  if(hasGpu && hasSubstrate && ramStrong) return {profil:'NAS runtime GPU candidat', statut:['À prouver','yellow'], risque:'Élevé', reco:'Possible seulement après preuve drivers, visibilité container/VM, benchmark petit modèle et contrôle thermique.'};
  if((hasNpu || p.gpu === 'iGPU média') && hasSubstrate) return {profil:'NAS preprocessing candidat', statut:['À vérifier','yellow'], risque:'Moyen', reco:'Bon candidat OCR léger, vision ou média si le support runtime est prouvé. Pas runtime LLM par défaut.'};
  if(hasGateway && !hasSubstrate) return {profil:'NAS passerelle / redirection', statut:['Candidat','blue'], risque:'Moyen', reco:'Utiliser comme point d’entrée contrôlé vers une machine de calcul externe. Garder runtime interne.'};
  if(hasSubstrate && ramStrong) return {profil:'NAS runtime léger', statut:['À prouver','yellow'], risque:'Moyen', reco:'Possible pour cockpit, petits services, index léger. Calcul IA lourd à déléguer.'};
  if(hasGateway) return {profil:'NAS stockage + gateway', statut:['Recommandé','green'], risque:'Faible à moyen', reco:'Stockage, cockpit statique et redirection sécurisée. Calcul délégué.'};
  return {profil:'NAS stockage + cockpit statique', statut:['Recommandé','green'], risque:'Faible', reco:'Posture par défaut : stockage, sauvegarde, docs et cockpit statique.'};
}

function updateNasProfile(){
  NAS_PROFILE_FIELDS.forEach(([id])=>{
    const el = document.getElementById('nas_'+id);
    if(el) nasProfile[id] = el.value;
  });
  renderNasResult();
}

function renderNasResult(){
  const r = scoreNasProfile(nasProfile);
  const el = document.getElementById('nasResult');
  if(!el) return;
  el.innerHTML = '<h3>'+r.profil+' '+chip(r.statut[0],r.statut[1])+'</h3>'+kv('Risque', r.risque)+kv('Recommandation', r.reco)+
    '<p style="margin-top:10px"><button onclick="prepareNasProfile()">Préparer profil candidat</button></p>';
}

function prepareNasProfile(){
  const r = scoreNasProfile(nasProfile);
  const out = document.getElementById('installOut');
  const title = (nasProfile.vendor || 'NAS')+' '+(nasProfile.model || '').trim();
  if(out) out.textContent = 'Profil machine candidat — '+title.trim()+' : '+r.profil+' / '+r.risque+'. '+r.reco+' Aucun changement réel.\n\n'+out.textContent;
  toast('Profil NAS candidat préparé','blue');
}

function renderNasClassifier(){
  return '<div class="card wide"><h3>Fiche machine / NAS</h3><p>Renseigne ce qui est connu. Le résultat reste local à la page et sert uniquement à préparer un profil candidat.</p>'+ 
    '<div class="grid formgrid">'+NAS_PROFILE_FIELDS.map(nasFieldHtml).join('')+'</div>'+ 
    '<div id="nasResult" class="panel-mini"></div></div>';
}

function renderInstallationsPage(){
  const html = panel(
    'Limite',
    '<p>Cette page ne lance aucune installation. Elle rend visible la chaîne d’amorçage avant Hermes : dépendances, états, blocages, rôles et prochaines actions.</p>',
    'Avant Hermes, Pantheon ne peut pas demander à Hermes d’installer Hermes.'
  )+
  '<h3 class="chapter">Profil machine / NAS</h3>'+renderNasClassifier()+
  '<h3 class="chapter">Chaîne bootstrap</h3>'+ 
  '<div class="grid">'+INSTALL_LAYERS.map(installLayerCard).join('')+'</div>'+ 
  '<h3 class="chapter">Profils recommandés</h3>'+ 
  '<div class="grid">'+INSTALL_PROFILES.map(installProfileCard).join('')+'</div>'+ 
  panel('États possibles','<p>'+INSTALL_STATES.map(s=>chip(s,'muted')).join('')+'</p>')+
  panel('Demandes candidates','<pre id="installOut">Aucune demande.</pre>');
  setTimeout(renderNasResult, 0);
  return html;
}
