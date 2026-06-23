/* Pantheon Control — page Fichiers.
   Source proposals are candidates only. */

function renderFileCard(f){
  return '<div class="card"><h3>'+f.nom+'</h3>'+ '<p>'+f.type+' · '+f.projet+'</p>'+ chip(f.lecture[0],f.lecture[1])+' '+chip(f.statut[0],f.statut[1])+
    '<p style="margin-top:8px"><button onclick="proposerSource(this,\''+safeName(f.nom)+'\')">Utiliser comme source</button></p></div>';
}

function renderFilesGrid(){
  const q=(document.getElementById('q').value||'').toLowerCase();
  const p=document.getElementById('p').value;
  const rows=FICHIERS.filter(f=>(p==='Tous'||f.projet===p) && (f.nom+' '+f.type+' '+f.projet).toLowerCase().includes(q));
  document.getElementById('grid').innerHTML=rows.map(renderFileCard).join('');
}

function proposerSource(btn, nom){
  btn.textContent='Ajouté ✓'; btn.disabled=true;
  document.getElementById('out').textContent='« '+nom+' » proposé comme source.\n\n'+document.getElementById('out').textContent;
  toast('Source proposée : '+nom,'blue');
}

function renderFilesPage(){
  const projets = ['Tous'].concat([...new Set(FICHIERS.map(f=>f.projet))]);
  return '<div class="toolbar"><input id="q" placeholder="filtrer…" oninput="renderFilesGrid()">'+
    '<select id="p" onchange="renderFilesGrid()">'+projets.map(p=>'<option>'+p+'</option>').join('')+'</select></div>'+ 
    '<div id="grid" class="grid"></div>'+ 
    panel('Sources proposées','<pre id="out">Aucune.</pre>');
}
