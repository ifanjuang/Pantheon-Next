/* Pantheon Control — page Registre déplacé.
   Informational page only; no register or memory is modified. */

function renderBaseMemoryPage(){
  return panel(
    'Nouvelle organisation',
    '<p>Le registre n’est pas une page autonome : il conserve le statut atteint par les sources, preuves, décisions et brouillons après qualification. L’examen et le registre vivent donc sur la même chaîne.</p><p><a class="primary-link" href="evidence.html">Ouvrir Preuves & statuts</a></p>',
    'La mémoire opérationnelle reste hors Pantheon : elle relève d’Hermes ou d’un runtime équivalent.'
  );
}
