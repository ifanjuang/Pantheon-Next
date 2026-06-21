/* Pantheon Control — rendus des pages de décision candidate.
   Documenté non implémenté. Ces fonctions préparent des intentions visibles ; elles ne valident rien, ne transmettent rien et ne créent aucune mémoire canonique. */

function renderBranchCard(b){
  return '<div class="card">'+
    '<h3>'+b.id+' · '+b.titre+'</h3>'+ 
    chip(b.statut[0],b.statut[1])+' '+chip(b.risque[0],b.risque[1])+
    kv('Origine', b.origine)+
    '<p>'+b.note+'</p>'+ 
    '<p>'+ 
      '<button onclick="toast(\'Comparaison préparée : '+b.id+'\',\'blue\')">Comparer</button>'+ 
      '<button onclick="toast(\'Variante créée : '+b.id+'\',\'blue\')">Créer variante</button>'+ 
      '<button onclick="marquerRetenu(\''+b.id+'\')">Marquer comme retenue</button>'+ 
    '</p>'+ 
  '</div>';
}

function marquerRetenu(id){
  toast('Branche marquée comme retenue : '+id,'green');
}

function accepterBranche(){
  confirmAct(
    'Accepter la branche retenue ?<br><span style="font-size:12.5px;color:#9aa2ad">Cette action prépare une décision candidate. Elle ne crée aucune mémoire canonique.</span>',
    'Accepter',
    ()=>toast('Décision candidate préparée','green')
  );
}

function renderDiscussionPage(){
  return panel(
    'Conversation métier gouvernée',
    '<p>Cette page simule une discussion hiérarchique : chaque branche conserve son statut, son risque et ses sources. Une hypothèse refusée reste visible, mais ne doit pas contaminer la version retenue.</p><p>'+chip('Statique','muted')+chip('Aucune exécution','yellow')+chip('Décision humaine requise','blue')+'</p>'
  )+
  '<div class="grid two">'+BRANCHES.map(renderBranchCard).join('')+'</div>'+ 
  panel(
    'Décisions possibles',
    '<p>'+ 
      '<button onclick="toast(\'Sources affichées\',\'blue\')">Voir sources</button>'+ 
      '<button onclick="toast(\'Approfondissement préparé\',\'blue\')">Approfondir</button>'+ 
      '<button onclick="toast(\'Commentaire préparé\',\'blue\')">Éditer / commenter</button>'+ 
      '<button onclick="toast(\'Demande de modification préparée\',\'blue\')">Demander modification</button>'+ 
      '<button onclick="toast(\'Branche refusée\',\'orange\')">Refuser</button>'+ 
      '<button class="primary" onclick="accepterBranche()">Accepter la branche retenue</button>'+ 
    '</p>',
    'Ces boutons préparent une décision dans le mockup. Ils ne transmettent rien, ne valident rien et ne créent aucune mémoire canonique.'
  );
}

function renderDraftAnchor(d){
  return '<div class="card">'+
    '<h3>'+d.id+' · '+d.document+'</h3>'+ 
    chip(d.statut[0],d.statut[1])+' '+chip(d.risque[0],d.risque[1])+
    kv('Portée', d.scope)+
    '<div class="cascade"><span class="lbl">Sélection</span><p>'+d.selection+'</p></div>'+ 
    '<div class="cascade"><span class="lbl">Proposition</span><p>'+d.proposition+'</p></div>'+ 
    '<p>'+ 
      '<button class="primary" onclick="preparerRemplacement(\''+d.id+'\')">Préparer remplacement</button>'+ 
      '<button onclick="toast(\'Commentaire candidat inséré : '+d.id+'\',\'blue\')">Insérer en commentaire</button>'+ 
      '<button onclick="toast(\'Variante créée : '+d.id+'\',\'blue\')">Créer variante</button>'+ 
      '<button onclick="toast(\'Proposition refusée : '+d.id+'\',\'orange\')">Refuser</button>'+ 
    '</p>'+ 
  '</div>';
}

function preparerRemplacement(id){
  confirmAct(
    'Préparer le remplacement de la sélection « '+id+' » ?<br><span style="font-size:12.5px;color:#9aa2ad">Crée un brouillon candidat. Aucune insertion réelle dans cette maquette.</span>',
    'Préparer',
    ()=>toast('Remplacement candidat préparé : '+id,'green')
  );
}

function actionMetier(label){
  toast('Action préparée : '+label,'blue');
}

function renderDraftingPage(){
  return panel(
    'Assistant de rédaction contextuel',
    '<p>Le cockpit agit sur une sélection, pas forcément sur tout le document. Chaque proposition reste un brouillon candidat tant qu’un utilisateur ne l’a pas acceptée.</p><p>'+chip('Sélection limitée','blue')+chip('Brouillon candidat','yellow')+chip('Aucune insertion réelle','muted')+'</p>'
  )+
  '<div class="grid two">'+DRAFT_ANCHORS.map(renderDraftAnchor).join('')+'</div>'+ 
  panel(
    'Actions métier',
    '<p>'+ 
      '<button onclick="actionMetier(\'Clarifier\')">Clarifier</button>'+ 
      '<button onclick="actionMetier(\'Raccourcir\')">Raccourcir</button>'+ 
      '<button onclick="actionMetier(\'Développer\')">Développer</button>'+ 
      '<button onclick="actionMetier(\'Sécuriser responsabilité\')">Sécuriser responsabilité</button>'+ 
      '<button onclick="actionMetier(\'Ajouter limite de mission\')">Ajouter limite de mission</button>'+ 
      '<button onclick="actionMetier(\'Transformer en mail\')">Transformer en mail</button>'+ 
    '</p>',
    'Les actions affichées sont des intentions de rédaction. Elles ne modifient aucun document externe dans cette maquette.'
  );
}
