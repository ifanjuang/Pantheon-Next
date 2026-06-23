/* Pantheon Control — registre des statuts.
   Pantheon ne porte pas la mémoire opérationnelle : elle relève d’Hermes ou d’un runtime équivalent.
   Ici, on affiche uniquement des statuts gouvernés et des copies non canoniques. */

const REGISTRY_STATUS = [
  {nom:'Registre de statut', role:'Suit le statut d’un objet : candidat, à vérifier, validé, refusé, obsolète, bloqué.', statut:['Référence','green']},
  {nom:'Registre des preuves', role:'Suit les preuves validées après qualification, décision humaine et rattachement à un dossier.', statut:['Référence','green']},
  {nom:'Registre des décisions', role:'Trace les décisions acceptées, refusées, à arbitrer ou à vérifier.', statut:['Référence','green']},
  {nom:'Brouillons candidats', role:'Objets proposés avant décision : texte, réponse, workflow, preuve ou action candidate.', statut:['À valider','yellow']},
  {nom:'Index de recherche', role:'Copie de travail pour retrouver par similarité. Ne valide rien et ne devient pas mémoire canonique.', statut:['Copie de travail','blue']},
  {nom:'Mémoire runtime externe', role:'Mémoire opérationnelle éventuelle côté Hermes ou runtime équivalent. Pantheon peut en gouverner le statut, pas l’exécuter.', statut:['Hors Pantheon','muted']},
  {nom:'Synchronisation', role:'État des copies et exports entre repo, cockpit, index, runtime ou tableau de pilotage.', statut:['À surveiller','orange']},
];

function renderRegistryCard(r){
  return '<div class="card"><h3>'+r.nom+'</h3><p>'+r.role+'</p>'+chip(r.statut[0],r.statut[1])+'</div>';
}

function renderBaseMemoryPage(){
  return panel(
    'Limite',
    '<p>Cette page ne stocke pas la mémoire agent. Elle expose les statuts que Pantheon doit gouverner. La mémoire opérationnelle appartient à Hermes ou à un runtime équivalent.</p>',
    'Le registre conserve le statut. La mémoire aide l’exécution. La preuve soutient une décision.'
  ) + '<div class="grid">'+REGISTRY_STATUS.map(renderRegistryCard).join('')+'</div>';
}
