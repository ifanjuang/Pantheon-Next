/* Pantheon Control — manifeste d'accueil.
   Static prototype only. Overrides renderHomePage from home.js when loaded after it. */

function renderHomeManifestPanel(){
  return '<div class="panel">'+
    '<h3>Pourquoi ce projet existe</h3>'+
    '<p>L’IA change déjà la manière de préparer un dossier : elle reformule, classe, compare, synthétise et produit des documents qui peuvent paraître propres. Dans un métier à responsabilité, le problème n’est pas seulement de savoir si le texte est bien écrit. Il faut comprendre d’où viennent les informations, ce qui a été vérifié, quelle méthode a été suivie, ce qui peut être retenu en mémoire et ce qui reste une simple proposition.</p>'+
    '<p>Pantheon Control part de cette difficulté. Un résultat généré peut être utile sans être encore utilisable. Une note peut être claire sans être suffisamment sourcée. Une mémoire peut être pratique sans être fiable. Une action peut être préparée sans devoir être envoyée.</p>'+
  '</div>';
}

function renderHomeOrganizationPanel(){
  return '<div class="panel">'+
    '<h3>Pourquoi cette organisation</h3>'+
    '<p>Le projet distingue volontairement l’espace où l’on travaille avec l’IA, l’assistant qui prépare le travail, et le cadre qui qualifie ce qui peut être retenu. OpenWebUI apporte une surface lisible pour discuter, consulter les documents, voir les sources, suivre les cartes et partager un espace de travail. Hermes porte la partie plus active : skills, mémoire de travail, recherches, comparaisons, brouillons, vérifications et traces. Pantheon intervient pour empêcher la confusion entre une production utile et une décision professionnelle.</p>'+
    '<p>Cette séparation permet de profiter des outils sans leur donner un rôle qu’ils ne doivent pas avoir. OpenWebUI rend visible. Hermes prépare et documente. Pantheon qualifie les preuves, le périmètre, les statuts, la mémoire et les validations nécessaires.</p>'+
    '<p><a href="modules.html" class="primary-link">Voir le détail des modules et usages</a></p>'+
  '</div>';
}

function renderHomeRefusalPanel(){
  return '<div class="panel">'+
    '<h3>Ce que Pantheon refuse</h3>'+
    '<p>Pantheon ne remplace pas le professionnel. Il ne transforme pas automatiquement une réponse en vérité, une trace en preuve, une mémoire retrouvée en mémoire fiable, ou une action préparée en action autorisée. Il ne signe pas, ne valide pas seul, ne décide pas à la place de l’humain et ne transforme pas l’exécution technique en approbation.</p>'+
    '<p>Son rôle est plus strict : rendre visibles les risques de confusion, forcer la qualification, conserver les doutes utiles et maintenir une décision humaine lorsque le dossier touche à une vérité, une mémoire, un statut, une preuve ou un effet externe.</p>'+
  '</div>';
}

function renderHomePage(){
  const testMobile = panel(
    'Test rapide — revue mobile des preuves',
    '<p>Ouvrir directement la maquette Swiper.js : sujets en swipe horizontal, affaires en swipe vertical, options rondes sur appui long.</p><p><a href="evidence.html" class="primary-link">Tester la vue Preuves & sources mobile</a></p>',
    'Lien de test uniquement : les gestes préparent des intentions candidates, sans effet réel.'
  );
  const references = panel(
    'Références & doctrine candidate',
    '<p>RAG probatoire, références externes et suivis HTML sont regroupés dans une page dédiée du cockpit.</p><p><a href="references.html" class="primary-link">Ouvrir le centre de références</a> · <a href="../../rag-probatoire.html">Page RAG probatoire</a></p>',
    'Aucune référence affichée ici ne devient canonique sans qualification et décision humaine.'
  );
  return renderHomeManifestPanel() + renderHomeOrganizationPanel() + renderHomeRefusalPanel() + testMobile + references + renderHomeSummary() + renderWorkflowPanel() + renderPriorityPanels();
}
