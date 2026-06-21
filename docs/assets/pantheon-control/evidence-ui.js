/* Pantheon Control — boot de la vue Preuves & sources.
   Documenté non implémenté. Cette couche monte le template mobile et lance le rendu candidat. */

function evidenceTemplateHtml(){
  return '<div class="app">'+
    '<header class="head">'+
      '<div><b id="barProject">Points de contrôle</b><small id="barPhase">Phase · —</small></div>'+ 
      '<button onclick="evidenceOpenAdd()">+ Fiche</button>'+ 
      '<button onclick="evidenceToggleInfo()">Infos</button>'+ 
    '</header>'+ 
    '<main class="stage"><div class="swiper pSw"><div class="swiper-wrapper">__PROJECTS__</div></div></main>'+ 
    '<aside id="inf" class="info"><p>Le header indique le projet, la phase et le nombre de fiches. Les exemples actifs incluent la sélection de sols, une clinique ABF et une rénovation chantier avec entreprise en procédure collective.</p></aside>'+ 
    '<aside id="panel" class="panel"><div class="ph"><div><h3 id="panelTitle">Fiche</h3><p>Transmission candidate Pantheon</p></div><button data-close="1">×</button></div><div id="panelBody" class="pb"></div><div class="pb"><button data-close="1">Fermer</button></div></aside>'+ 
    '<aside id="ov" class="ov"><div class="oh"><div><h3 id="ovTitle">Projet</h3><p id="ovSub">Mode dézoom</p></div><button data-close="1">×</button></div><div class="ob"><div id="ovGrid" class="grid"></div></div></aside>'+ 
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
    mountPage('Points de contrôle', '', '<div class="gap"><b>Données indisponibles.</b><br>' + escEv(err.message) + '<br>Manque : evidence_data.json. Sans effet sur le registre — aucune fiche candidate affichée.</div>');
  });
}
