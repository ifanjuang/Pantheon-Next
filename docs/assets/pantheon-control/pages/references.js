/* Pantheon Control — page Références.
   References are displayed as candidate/support material only. */

function renderReferenceCards(){
  return REFERENCES.map(e =>
    '<div class="card">'+
      chip(e.status[0], e.status[1])+' '+chip(e.authority[0], e.authority[1])+' '+chip('Risque '+e.risk[0], e.risk[1])+
      '<h3>'+e.title+'</h3>'+
      '<p>'+e.summary+'</p>'+
      kv('Prochaine action', e.next)+
      '<p><a href="'+e.href+'" class="primary-link">Ouvrir</a></p>'+
    '</div>'
  ).join('');
}

function renderReferencesPage(){
  return panel(
    'Centre de références',
    '<p>Cette page expose des références, pages candidates et suivis. Elle ne valide rien, ne promeut aucune mémoire et ne déclenche aucune action externe.</p>',
    'Doctrine : retrieval proposes · evidence supports · governance qualifies · approval validates · the human decides.'
  ) + '<div class="grid">'+renderReferenceCards()+'</div>';
}
