# Pantheon Control — maquette du tableau de bord

Statut : **documenté non implémenté**. Prototype HTML statique, données fictives.

Tableau de bord d’usage du cockpit : surveiller l’état, gérer machines, services
et modèles, suivre les preuves, documents du dossier et workflows professionnels
avant décision humaine. Il informe sur **l’usage** ; les règles de gouvernance
vivent dans la documentation, pas à l’écran.

## Pages

| Chapitre | Page | Rôle |
|---|---|---|
| Pilotage | `index.html` | Accueil : synthèse, travail du jour, workflow proposé et coûts IA fictifs |
| Pilotage | `surveillance.html` | Journal : contrôles automatiques + historique |
| Infrastructure | `machines.html` | Postes/serveurs : IP, état, GPU/RAM, modèles hébergés |
| Infrastructure | `services.html` | Services & outils : version, MAJ, dépôt, dépendances, demandes candidates |
| IA | `ia.html` | Modèles & fournisseurs (Ollama local + Claude, ChatGPT, Gemini, Mistral), coûts et configuration candidate |
| IA | `skills.html` | Skills actifs et leur usage |
| Travail | `discussion.html` | Discussion hiérarchique : branches, variantes et décisions humaines visibles |
| Travail | `drafting.html` | Rédaction assistée : sélection, proposition de remplacement et brouillon candidat |
| Travail | `files.html` | Documents projet : dossiers actifs, versions, archives, sync Knowledge et utilisabilité IA |
| Travail | `evidence.html` | Preuves & sources : sources, propositions, gate humain simulé et conséquences |
| Travail | `base-memory.html` | Base & mémoire : référence vs copies de travail |

## Fichiers partagés

- `style.css` — thème, responsive (sans débordement mobile).
- `data.js` — données fictives + helpers `chip()` / `info()`.
- `nav.js` — coquille, navigation par chapitres, `mountPage()`.

## Notes

- Les modèles LLM sont inventoriés **par machine** (là où est le GPU), pas sur le serveur.
- Les boutons (préparer installation, préparer MAJ, préparer retrait, préparer connexion…) **préparent** une demande ; rien n’est exécuté directement par le tableau de bord.
- La page `files.html` reprend une logique GED / boîte à plans : dossiers, versions, archives, statut IA, sync Knowledge et demandes candidates.
- Les productions IA restent dans les discussions et branches ; la base documentaire contient des sources, pas des brouillons produits.
- La page `evidence.html` parle de **Preuves & sources** : une source récupérée reste candidate tant qu’elle n’est pas revue.
- La page `discussion.html` conserve les variantes refusées comme branches séparées pour éviter leur mélange silencieux avec une version retenue.
- La page `drafting.html` agit sur une sélection fictive ; aucune insertion réelle dans Google Docs, Sheets ou Office n’est implémentée.
- Un petit « i » au survol donne l’usage d’un module.

## Limite

Cette maquette ne crée pas de runtime, de connecteur, de chat engine, d’éditeur,
de Registre Probatoire, d’approbation, de mémoire canonique ou d’action externe.
