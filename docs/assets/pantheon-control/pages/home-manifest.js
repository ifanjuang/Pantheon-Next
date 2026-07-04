/* Pantheon Control — manifeste d'accueil.
   Static prototype only. Overrides renderHomePage from home.js when loaded after it. */

function renderHomeManifestPanel(){
  return '<div class="panel">'+
    '<h3>Pourquoi ce projet existe</h3>'+
    '<p>L’IA produit vite des textes propres, des synthèses convaincantes et des dossiers bien rangés. Dans un métier à responsabilité, cela ne suffit pas. Il faut savoir d’où vient l’information, ce qui a été vérifié, quelle méthode a été suivie, ce qui peut être retenu et ce qui reste seulement proposé.</p>'+
    '<p>Pantheon Control part de ce point simple : un résultat peut être utile sans être encore utilisable. Une réponse bien écrite peut rester fragile. Une trace peut expliquer l’exécution sans valider le contenu. Une mémoire retrouvée peut aider sans devenir fiable.</p>'+
  '</div>';
}

function renderHomeOrganizationPanel(){
  return '<div class="panel">'+
    '<h3>Organisation</h3>'+
    '<p>OpenWebUI rend le travail visible. Hermes prépare, applique des skills, retrouve des éléments et produit des propositions. Pantheon qualifie les preuves, les statuts, la mémoire, le périmètre et les validations. Cette séparation permet d’utiliser les outils sans leur donner une autorité qu’ils ne doivent pas avoir.</p>'+
  '</div>';
}

function renderHomeRefusalPanel(){
  return '<div class="panel">'+
    '<h3>Ce que Pantheon refuse</h3>'+
    '<p>Pantheon ne signe pas, ne valide pas seul, ne transforme pas une réponse en vérité, une trace en preuve, une mémoire retrouvée en mémoire fiable ou une action préparée en action autorisée. Il rend visibles les seuils où l’humain doit décider.</p>'+
  '</div>';
}

function renderHomeEntryPanel(){
  return '<div class="panel">'+
    '<h3>Entrées utiles</h3>'+
    '<p class="t">Quatre portes suffisent pour lire le cockpit : preuve, décision, méthode, infrastructure.</p>'+
    '<div class="grid two">'+
      '<div class="card"><h3>Preuves & statuts</h3><p>Qualifier ce qui est source, indice, preuve candidate, blocage ou décision attendue.</p><p><a href="evidence.html" class="primary-link">Ouvrir</a></p></div>'+
      '<div class="card"><h3>Décisions</h3><p>Comparer des branches, conserver les refus utiles et rendre l’arbitrage humain visible.</p><p><a href="discussion.html" class="primary-link">Ouvrir</a></p></div>'+
      '<div class="card"><h3>Skills & mémoire</h3><p>Encadrer les méthodes réutilisables et éviter qu’une mémoire de travail devienne une vérité.</p><p><a href="skills.html" class="primary-link">Ouvrir</a></p></div>'+
      '<div class="card"><h3>Infrastructure</h3><p>Lire l’état des outils sans transformer le cockpit en console technique.</p><p><a href="infrastructure.html" class="primary-link">Ouvrir</a></p></div>'+
    '</div>'+
  '</div>';
}

function renderHomePage(){
  return renderHomeManifestPanel() + renderHomeOrganizationPanel() + renderHomeRefusalPanel() + renderHomeEntryPanel();
}
