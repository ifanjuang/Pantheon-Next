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
| Travail | `evidence.html` | Points de contrôle : revue mobile compacte sans scroll de page, swipe horizontal pour les projets, swipe vertical pour les sujets, fiche structurée type compte rendu gouverné |
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
- La page `evidence.html` affiche désormais des **Points de contrôle** côté utilisateur. Côté système, ces points restent des candidats de preuve et de décision, non des vérités stabilisées.
- Chaque fiche suit la chaîne métier : source → constat → statut / risque → décideur attendu → actions recommandées → dépendances → action candidate Pantheon.
- La fiche distingue statut opérationnel et risque : `Contradictoire`, `Décision attendue`, `Bloquant`, `À vérifier`, `À faire`, etc. Le risque ne remplace pas le statut.
- Chaque fiche indique un décideur attendu : architecte, client, géomètre, BET, entreprise ou autre acteur selon le point traité.
- Les sources affichent leur type, force, statut, origine, date, fichier, indice, lien MD et lien PDF lorsqu’il existe. Une source `IA / extraction` doit rester visuellement candidate.
- Le constat distingue ce qui est établi et ce qui reste incertain. Une contradiction peut être affichée explicitement quand deux sources ou intentions divergent.
- Les actions recommandées sont structurées en trois niveaux : action immédiate, pièce ou information manquante, décision attendue.
- Le bloc `Dépendances` est nommé explicitement et calé en bas de la fiche, avant les actions. Les lignes Amont, Aval et Même niveau indiquent le numéro de carte à droite et peuvent naviguer vers cette carte si elle existe.
- Dans `evidence.html`, le geste gauche / droite change de projet ; le geste haut / bas change de sujet dans le projet actif.
- Le swipe vertical de la vue mono-carte est protégé contre le clic accidentel : une fiche ne passe en dézoom qu’après un vrai tap, pas après un drag.
- Un clic sur une fiche ouvre un mode dézoom du projet actif : grille de trois colonnes, scroll vertical libre, affichage réduit au titre et aux labels.
- En mode dézoom, le contour indique les relations vis-à-vis de la fiche sélectionnée : contour complet = sélectionnée, bord haut = ascendant, bord bas = descendant, bords haut et bas = même niveau. Cliquer la fiche déjà sélectionnée ferme le dézoom et revient à la fiche mono-carte.
- Les icônes de sujet sont des pictogrammes SVG blancs sur fond transparent, sans emoji.
- Le champ de note texte a été retiré de la fiche pour alléger l’écran et éviter les effets de zoom / focus sur iPhone.
- Le bouton `Recherche+` est contextualisé : il affiche les manques de la fiche, puis un workflow de recherche complémentaire avec base projet, courriels, corpus DTU / règles, sources contrôlées, résultat candidat et retour Pantheon.
- Les actions de bas de fiche sont formulées comme intentions à transmettre à Pantheon : valider, refuser, modifier, demander plus de détail / complément. Elles ne modifient pas de registre.
- La page `discussion.html` conserve les variantes refusées comme branches séparées pour éviter leur mélange silencieux avec une version retenue.
- La page `drafting.html` agit sur une sélection fictive ; aucune insertion réelle dans Google Docs, Sheets ou Office n’est implémentée.
- Un petit « i » au survol donne l’usage d’un module.

## Limite

Cette maquette ne crée pas de runtime, de connecteur, de chat engine, d’éditeur,
de Registre Probatoire, d’approbation, de mémoire canonique ou d’action externe.
