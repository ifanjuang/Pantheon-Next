# Pantheon Control — maquette du tableau de bord

Statut : **documenté non implémenté**. Prototype HTML statique, données fictives.

Tableau de bord d’usage du cockpit : surveiller l’état, gérer machines, services
et modèles, suivre les preuves et fichiers du dossier, et préparer des workflows
professionnels avant décision humaine. Il informe sur **l’usage** ; les règles de
gouvernance vivent dans la documentation, pas à l’écran.

## Pages

| Chapitre | Page | Rôle |
|---|---|---|
| Pilotage | `index.html` | Accueil : synthèse, travail du jour, workflow proposé et coûts IA fictifs |
| Pilotage | `surveillance.html` | Journal : contrôles automatiques + historique |
| Infrastructure | `machines.html` | Postes/serveurs : IP, état, GPU/RAM, modèles hébergés |
| Infrastructure | `services.html` | Services & outils : version, MAJ, dépôt, dépendances, demandes candidates |
| Infrastructure | `observability.html` | Observabilité Langfuse : carte link-only / health-only, traces synthétiques uniquement |
| IA | `ia.html` | Modèles & fournisseurs (Ollama local + Claude, ChatGPT, Gemini, Mistral), coûts et configuration candidate |
| IA | `skills.html` | Skills actifs et leur usage |
| Travail | `discussion.html` | Discussion hiérarchique : branches, variantes et décisions humaines visibles |
| Travail | `drafting.html` | Rédaction assistée : sélection, proposition de remplacement et brouillon candidat |
| Travail | `evidence.html` | Preuves & sources : revue mobile compacte sans scroll de page, swipe horizontal pour les sujets, swipe vertical pour les affaires, actions Pantheon candidates, choix / variantes et cartes liées |
| Travail | `files.html` | Fichiers reçus et état de lecture |
| Travail | `base-memory.html` | Base & mémoire : référence vs copies de travail |

## Fichiers partagés

- `style.css` — thème, responsive (sans débordement mobile).
- `data.js` — données fictives + helpers `chip()` / `info()`.
- `nav.js` — coquille, navigation par chapitres, `mountPage()`.

## Notes

- Les modèles LLM sont inventoriés **par machine** (là où est le GPU), pas sur le serveur.
- Les boutons (préparer installation, préparer MAJ, préparer retrait, préparer connexion…) **préparent** une demande ; rien n’est exécuté directement par le tableau de bord.
- La page `observability.html` expose Langfuse en lien externe et health check opérationnel seulement : pas d’iframe, pas de clé frontend, pas de trace client, pas de preuve ni d’approbation automatique.
- La page `evidence.html` parle de **Preuves & sources** : une source récupérée reste candidate tant qu’elle n’est pas revue.
- La page `evidence.html` est une vue mobile compacte : la page ne scrolle pas, les cartes sont condensées, les risques sont alignés à droite avec date et butoir, les actions sont visibles, et le bouton `Infos` ouvre le contexte global en panneau replié.
- Dans `evidence.html`, `Source`, `Description`, `Recommandation Pantheon` et `Choix` sont dans le corps de la fiche, séparés par des lignes simples. Les choix / variantes remplacent temporairement le sous-contenu de la fiche, sans changer le titre, les labels ni les risques.
- La page affiche des cartes liées avant les actions : amont, aval et même niveau. Elles ouvrent un panneau de contexte sans produire d’effet probatoire.
- Les actions de bas de fiche sont formulées comme intentions à transmettre à Pantheon : valider, refuser, modifier, demander plus de détail / complément.
- La page `discussion.html` conserve les variantes refusées comme branches séparées pour éviter leur mélange silencieux avec une version retenue.
- La page `drafting.html` agit sur une sélection fictive ; aucune insertion réelle dans Google Docs, Sheets ou Office n’est implémentée.
- Un petit « i » au survol donne l’usage d’un module.

## Limite

Cette maquette ne crée pas de runtime, de connecteur, de chat engine, d’éditeur,
de Registre Probatoire, d’approbation, de mémoire canonique ou d’action externe.
