/* Pantheon Control — page Skills.
   Activation requests are candidates only. */

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
