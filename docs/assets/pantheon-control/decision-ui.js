/* Pantheon Control — rendus des pages de décision candidate.
   Documenté non implémenté. Ces fonctions préparent des intentions visibles ; elles ne valident rien, ne transmettent rien et ne créent aucune mémoire canonique. */

function renderBranchCard(b){
  return '<div class="card">'+
    '<h3>'+b.id+' · '+b.titre+'</h3>'+
    chip(b.statut[0],b.statut[1])+' '+chip(b.risque[0],b.risque[1])+
    kv('Origine', b.origine)+
    '<p>'+b.note+'</p>'+
    '<p class="t">Sortie attendue : arbitrage humain ou demande de preuve complémentaire.</p>'+
  '</div>';
}

function decisionIntent(label,tone){
  toast('Décision candidate : '+label, tone || 'blue');
}

function accepterBranche(){
  confirmAct(
    'Préparer la décision retenue ?<br><span style="font-size:12.5px;color:#9aa2ad">Cette maquette ne valide rien et ne crée aucune mémoire canonique.</span>',
    'Préparer',
    ()=>toast('Décision candidate préparée','green')
  );
}

function renderDiscussionPage(){
  return panel(
    'Décisions visibles',
    '<p>Une branche de réponse n’est pas une décision. Cette page conserve les variantes utiles, les refus et les risques pour que l’arbitrage humain reste lisible.</p><p>'+chip('Statique','muted')+chip('Aucune exécution','yellow')+chip('Arbitrage humain','blue')+'</p>'
  )+
  '<div class="grid two">'+BRANCHES.map(renderBranchCard).join('')+'</div>'+
  panel(
    'Gate de décision',
    '<p>'+
      '<button onclick="decisionIntent(\'demander sources\')">Demander sources</button>'+
      '<button onclick="decisionIntent(\'demander révision\')">Demander révision</button>'+
      '<button onclick="decisionIntent(\'refuser\',\'orange\')">Refuser</button>'+
      '<button class="primary" onclick="accepterBranche()">Préparer décision retenue</button>'+
    '</p>',
    'Actions de maquette uniquement : aucune transmission, aucune validation, aucune mémoire canonique.'
  );
}

function renderDraftAnchor(d){
  return '<div class="card">'+
    '<h3>'+d.id+' · '+d.document+'</h3>'+
    chip(d.statut[0],d.statut[1])+' '+chip(d.risque[0],d.risque[1])+
    kv('Portée', d.scope)+
    '<div class="cascade"><span class="lbl">Sélection</span><p>'+d.selection+'</p></div>'+
    '<div class="cascade"><span class="lbl">Proposition</span><p>'+d.proposition+'</p></div>'+
    '<p class="t">Le remplacement reste candidat tant qu’il n’est pas relu et validé.</p>'+
  '</div>';
}

function preparerRemplacement(){
  confirmAct(
    'Préparer les remplacements candidats ?<br><span style="font-size:12.5px;color:#9aa2ad">Aucune insertion réelle dans cette maquette.</span>',
    'Préparer',
    ()=>toast('Remplacements candidats préparés','green')
  );
}

function actionMetier(label){
  toast('Intention de rédaction : '+label,'blue');
}

function renderDraftingPage(){
  return panel(
    'Rédaction candidate',
    '<p>La rédaction agit sur une sélection bornée. Chaque proposition reste un brouillon candidat : elle peut aider, mais ne modifie aucun document externe dans cette maquette.</p><p>'+chip('Sélection limitée','blue')+chip('Brouillon candidat','yellow')+chip('Aucune insertion réelle','muted')+'</p>'
  )+
  '<div class="grid two">'+DRAFT_ANCHORS.map(renderDraftAnchor).join('')+'</div>'+
  panel(
    'Actions de rédaction',
    '<p>'+
      '<button onclick="actionMetier(\'clarifier\')">Clarifier</button>'+
      '<button onclick="actionMetier(\'sécuriser responsabilité\')">Sécuriser</button>'+
      '<button onclick="actionMetier(\'préparer mail\')">Préparer mail</button>'+
      '<button class="primary" onclick="preparerRemplacement()">Préparer remplacements</button>'+
    '</p>',
    'Intentions de rédaction uniquement : pas d’envoi, pas d’écriture externe, pas de validation automatique.'
  );
}
