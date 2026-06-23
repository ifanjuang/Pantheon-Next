/* Pantheon Control — helpers de rendu partagés.
   Documenté non implémenté. Ces fonctions affichent des données candidates ; elles ne valident rien. */

function panel(title, body, hint){
  return '<div class="panel">'+
    '<h3>'+title+'</h3>'+
    body+
    (hint ? '<p class="hint">'+hint+'</p>' : '')+
  '</div>';
}

function card(title, body, href){
  return '<div class="card">'+
    '<h3>'+title+'</h3>'+
    body+
    (href ? '<p><a href="'+href+'">Ouvrir</a></p>' : '')+
  '</div>';
}

function kv(label, value){
  return '<div class="kv"><span>'+label+'</span><b>'+value+'</b></div>';
}

function queue(items){
  return '<ul class="queue">'+items.join('')+'</ul>';
}

function safeName(s){
  return String(s||'').replace(/'/g,'');
}

function depotLien(d){
  return d.indexOf('github.com')===0 ? '<a href="https://'+d+'" target="_blank" rel="noopener">'+d+'</a>' : d;
}
