/* Pantheon Control — boot de la vue Preuves & statuts.
   Documenté non implémenté. Cette couche monte le template mobile et lance le rendu candidat. */

function evidenceTemplateHtml(){
  return '<div class="app">'+
    '<header class="head">'+
      '<div><b id="barProject">Preuves & statuts</b><small id="barPhase">Dossier · statut · date</small></div>'+ 
      '<button onclick="evidenceOpenAdd()">+ Fiche</button>'+ 
      '<button onclick="evidenceToggleInfo()">Filtres</button>'+ 
    '</header>'+ 
    '<main class="stage"><div class="swiper pSw"><div class="swiper-wrapper">__PROJECTS__</div></div></main>'+ 
    '<aside id="inf" class="info"><p>Cette page regroupe l’atelier probatoire et le registre des statuts. Les filtres cibles sont : dossier, statut, date, risque, type, phase et décision attendue. Dans cette maquette, le swipe par dossier/projet reste le mode principal.</p></aside>'+ 
    '<aside id="panel" class="panel"><div class="ph"><div><h3 id="panelTitle">Fiche</h3><p>Transmission candidate Pantheon</p></div><button data-close="1">×</button></div><div id="panelBody" class="pb"></div><div class="pb"><button data-close="1">Fermer</button></div></aside>'+ 
    '<aside id="ov" class="ov"><div class="oh"><div><h3 id="ovTitle">Projet</h3><p id="ovSub">Vue registre / dézoom</p></div><button data-close="1">×</button></div><div class="ob"><div id="ovGrid" class="grid"></div></div></aside>'+ 
    '<div id="to" class="toast"></div>'+ 
  '</div>';
}

function evidenceMountTemplate(){
  let tpl = document.getElementById('tpl');
  if(!tpl){
    tpl = document.createElement('template');
    tpl.id = 'tpl';
    document.body.appendChild(tpl);
  }
  tpl.innerHTML = evidenceTemplateHtml();
}

function evidenceBoot(){
  document.body.classList.add('ev');
  evidenceMountTemplate();
  evidenceRender().catch(err => {
    mountPage('Preuves & statuts', '', '<div class="gap"><b>Données indisponibles.</b><br>' + escEv(err.message) + '<br>Manque : evidence_data.json. Sans effet sur le registre — aucune fiche candidate affichée.</div>');
  });
}
