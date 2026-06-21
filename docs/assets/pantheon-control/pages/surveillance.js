/* Pantheon Control — page Journal & contrôles.
   Static monitoring mockup; no scheduler or control engine is implemented. */

function renderSurveillancePage(){
  const controles = CONTROLES.map(c=>'<div class="card"><h3>'+c.label+'</h3>'+chip(c.resultat[0],c.resultat[1])+'</div>').join('');
  const journal = JOURNAL.map(j=>'<li><span class="t">'+j.t+'</span><br>'+j.msg+'</li>');
  return '<h3 class="chapter">Contrôles automatiques</h3><div class="grid">'+controles+'</div>'+panel('Journal d’activité', queue(journal));
}
