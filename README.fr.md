# Pantheon Next

> English version: [README.md](README.md)

> **L’IA ouvre les possibles. Les rôles organisent les tensions. La preuve contraint. L’humain décide. Le validé reste.**

<sub><strong>État actuel :</strong> Pantheon Next est un référentiel de méthode et de documentation en cours de structuration. Il est cohérent, mais partiel. Pour l’état d’implémentation faisant foi, lire <a href="docs/governance/STATUS.md">docs/governance/STATUS.md</a>.</sub>

Pantheon Next aide les professionnels à utiliser l’IA sur des dossiers sérieux sans laisser une réponse fluide devenir un acte professionnel risqué.

Le danger n’est pas seulement que l’IA invente.

Le danger est qu’elle produise une réponse claire, polie et convaincante qui transforme trop vite une hypothèse en décision, une source en preuve, un brouillon en livrable ou un message en validation implicite.

Pantheon garde le chemin visible : sources, doutes, contradictions, sorties candidates, validation humaine et mémoire bornée.

<details>
<summary>Sommaire</summary>

- [Pantheon en 60 secondes](#pantheon-en-60-secondes)
- [Le risque : l’IA répond bien, parfois trop bien](#le-risque--lia-répond-bien-parfois-trop-bien)
- [Quatre peurs, quatre réponses](#quatre-peurs-quatre-réponses)
- [Le mail qui engage trop](#le-mail-qui-engage-trop)
- [Quand une règle change, quels dossiers sont touchés ?](#quand-une-règle-change-quels-dossiers-sont-touchés-)
- [De l’IA brute au dossier maîtrisé](#de-lia-brute-au-dossier-maîtrisé)
- [Une source n’est pas une preuve](#une-source-nest-pas-une-preuve)
- [Désaccords utiles, décision humaine](#désaccords-utiles-décision-humaine)
- [Un brouillon n’est pas un livrable](#un-brouillon-nest-pas-un-livrable)
- [Aucune mémoire sans validation](#aucune-mémoire-sans-validation)
- [Cloud ou local : choisir selon le dossier](#cloud-ou-local--choisir-selon-le-dossier)
- [Dossiers déroulés : architecte, avocat, médecin](#dossiers-déroulés--architecte-avocat-médecin)
- [Sept regards, une décision humaine](#sept-regards-une-décision-humaine)
- [Pas un outil de plus : une méthode de dossier](#pas-un-outil-de-plus--une-méthode-de-dossier)
- [Le vocabulaire en clair](#le-vocabulaire-en-clair)
- [Ce que Pantheon n’est pas](#ce-que-pantheon-nest-pas)
- [En une formule](#en-une-formule)

</details>

## Pantheon en 60 secondes

Pantheon est une méthode professionnelle autour de l’IA.

Il fait cinq choses :

- il cadre la demande avant que l’IA n’agisse ;
- il garde visibles les sources, les doutes et les contradictions ;
- il marque les sorties comme candidates tant qu’elles ne sont pas revues ;
- il demande une décision humaine quand le risque dépasse l’arbitrage sûr ;
- il empêche la mémoire de devenir durable sans périmètre ni validation.

En langage simple :

```text
L’écran montre.
L’atelier prépare.
Pantheon cadre la méthode.
L’humain décide.
```

La doctrine interne reste :

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

## Le risque : l’IA répond bien, parfois trop bien

Une mauvaise réponse IA est facile à suspecter.

Une réponse fluide est plus dangereuse.

Elle peut sembler juste tout en cachant des sources manquantes, des contradictions non résolues, des hypothèses obsolètes ou des conséquences professionnelles.

Pantheon traite donc toute sortie IA comme candidate tant que le chemin du dossier n’est pas clair.

```text
Fluide ≠ sûr.
Utile ≠ validé.
Rapide ≠ prêt à envoyer.
```

## Quatre peurs, quatre réponses

| Peur professionnelle | Réponse Pantheon |
|---|---|
| Mes données vont-elles partir n’importe où ? | Les informations peuvent être minimisées, masquées ou traitées localement selon la sensibilité du dossier. |
| L’IA va-t-elle inventer ? | Les sources, hypothèses, contradictions et informations manquantes restent visibles. |
| Qui décide ? | L’IA propose. Le professionnel valide, rejette ou demande une reprise. |
| Que reste-t-il après coup ? | Seules les informations validées, bornées et reliées à un contexte peuvent devenir mémoire. |

## Le mail qui engage trop

Un risque professionnel courant n’est pas une mauvaise réponse.

C’est un mail bien écrit qui va trop loin.

Exemple :

```text
Prépare un mail au client pour valider ce devis de reprise.
```

Une IA générique peut rédiger un mail poli de validation.

Pantheon doit plutôt demander :

```text
Ce mail implique-t-il une validation technique, une acceptation, une réception, une approbation de périmètre ou un engagement externe ?
```

Si la réponse est incertaine, Pantheon ouvre un seuil de décision :

```text
Transmission bloquée en attente de décision.
Options :
1. mail neutre de clarification ;
2. note interne seulement ;
3. attente de la source manquante ;
4. deux variantes à relire.
```

Voir le premier démonstrateur : [`docs/examples/architecture_devis_reprise/`](docs/examples/architecture_devis_reprise/).

## Quand une règle change, quels dossiers sont touchés ?

Un professionnel doit aussi savoir quand une hypothèse d’hier devient fragile.

Une nouvelle réglementation, jurisprudence, doctrine officielle, norme technique ou recommandation peut affecter des dossiers en cours.

Pantheon ne doit pas les réécrire automatiquement.

Il doit produire une alerte de veille :

```text
Nouvelle source trouvée.
Hypothèse affectée possible.
Applicabilité non confirmée.
Dossiers à revoir.
Décision humaine requise avant mise à jour ou transmission.
```

Distinction clé :

```text
Information nouvelle ≠ règle applicable.
Alerte de veille ≠ mise à jour du dossier.
Réglementation retrouvée ≠ preuve.
Impact suspecté ≠ conclusion.
```

Voir le deuxième démonstrateur : [`docs/examples/regulatory_watch_conflict/`](docs/examples/regulatory_watch_conflict/).

## De l’IA brute au dossier maîtrisé

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg" width="100%" alt="Avant et après : une sortie IA brute devient un chemin de dossier professionnel maîtrisé">
  </a>
</p>

<p align="center"><strong>Avant / après.</strong><br><em>L’IA brute donne une réponse. Pantheon transforme le travail en chemin visible : mission, sources, preuve, sortie candidate et validation.</em></p>

L’IA seule peut répondre vite.

C’est utile, mais insuffisant pour un travail qui engage une responsabilité.

Pantheon ajoute le chemin du dossier :

```text
demande
→ fiche de mission
→ choix des sources et du périmètre
→ travail candidat
→ dossier de preuve
→ revue
→ décision humaine
→ mémoire bornée éventuelle
```

## Une source n’est pas une preuve

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/port_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/port_01_fr.jpg" width="100%" alt="Port des sources contrôlées : les informations externes entrent seulement après filtrage et statut de revue">
  </a>
</p>

<p align="center"><strong>Le port des sources.</strong><br><em>Pages web, fichiers, emails et connecteurs apportent de la matière. Pantheon marque ce qui est trouvé, utilisable, manquant ou encore à vérifier.</em></p>

Le web, les emails, les fichiers, les API, les messages et les Knowledge Bases peuvent fournir de la matière.

Cette matière n’est pas une preuve.

Pantheon sépare :

```text
Source trouvée ≠ preuve.
Document récupéré ≠ vérité.
Bibliothèque recherchable ≠ mémoire.
Réponse utile ≠ validation.
```

Une source ne devient utile que si son statut est clair : d’où elle vient, ce qu’elle soutient, ce qu’elle ne soutient pas, et si elle est encore actuelle.

## Désaccords utiles, décision humaine

Pantheon ne devient pas plus rigoureux en multipliant des agents autonomes.

Il sépare les responsabilités de jugement.

Les figures grecques sont des **Pantheon Roles** : des angles de revue et des magistratures de gouvernance. Ce ne sont pas des travailleurs autonomes. Leur valeur est de faire apparaître les désaccords utiles avant qu’un professionnel valide quoi que ce soit.

Exemples :

- Apollo peut rendre un message clair pendant que Themis bloque sa transmission parce que le risque reste trop élevé.
- Argos peut détecter une source manquante pendant qu’Hephaistos prépare quand même un brouillon.
- Zeus peut décider que la procédure sûre n’est pas la livraison, mais une décision humaine.

```text
Réponse fluide ≠ réponse sûre.
Artefact produit ≠ livrable.
Source retrouvée ≠ preuve.
Accord entre rôles ≠ approbation.
```

Voir [`docs/governance/GOVERNANCE_COLLEGE.md`](docs/governance/GOVERNANCE_COLLEGE.md) et [`docs/governance/USER_DECISION_GATE.md`](docs/governance/USER_DECISION_GATE.md).

## Un brouillon n’est pas un livrable

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/livrables_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/livrables_01_fr.jpg" width="100%" alt="Atelier des livrables candidats : notes, tableaux, courriers et rapports restent candidats jusqu’à validation">
  </a>
</p>

<p align="center"><strong>L’atelier des livrables.</strong><br><em>Pantheon aide à préparer notes, tableaux, courriers et rapports. Ils restent candidats tant que la revue et l’approbation ne sont pas terminées.</em></p>

Pantheon aide à produire de la matière utile : note, tableau, courrier, synthèse, schéma, rapport, checklist ou dossier d’export.

Mais le statut compte.

```text
Brouillon ≠ livrable.
Livrable candidat ≠ sortie validée.
Sortie validée ≠ mémoire.
Envoyé ≠ vrai.
```

Un livrable reste candidat tant que la revue et le chemin d’approbation nécessaires ne sont pas terminés.

## Aucune mémoire sans validation

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg" width="100%" alt="Mémoire compartimentée : sources, contexte, preuve et mémoire approuvée restent séparés">
  </a>
</p>

<p align="center"><strong>La mémoire compartimentée.</strong><br><em>Pantheon n’utilise pas un grand seau de vérité. Source, contexte, preuve, mémoire candidate et mémoire approuvée restent séparés.</em></p>

Pantheon n’utilise pas un grand seau de vérité unique.

```text
Raw Source       matière disponible
Knowledge        information de référence organisée
Context          information utile pour une tâche
Evidence         support sélectionné pour une affirmation ou une sortie
Memory Candidate information durable proposée
Canonical Memory mémoire approuvée, bornée et reliée aux preuves
Doctrine         couche de règles
Runtime State    état d’exécution externe, jamais mémoire canonique
```

Une sortie utile reste candidate jusqu’à ce que revue, preuve, périmètre et validation rendent sa conservation légitime.

## Cloud ou local : choisir selon le dossier

Pantheon n’impose pas une seule stratégie de modèle.

Une équipe peut utiliser des services IA externes comme ChatGPT, Claude ou Gemini lorsque le dossier le permet. Dans ce cas, Pantheon sert à réduire l’exposition avant que quelque chose ne sorte de l’environnement contrôlé : noms privés, adresses de projet, références client, identifiants contractuels ou extraits sensibles peuvent être masqués, minimisés ou retirés.

Une équipe peut aussi utiliser un modèle local, par exemple sur un poste avec GPU, une machine dédiée ou un NAS isolé avec Docker. Cette option garde davantage de données dans l’infrastructure du cabinet, mais demande du matériel, de la maintenance et une discipline d’exploitation.

Dans les deux cas :

```text
Le modèle propose.
Pantheon cadre la méthode.
Le professionnel valide.
```

## Dossiers déroulés : architecte, avocat, médecin

Les exemples sont fictifs et pédagogiques. Ils ne remplacent pas un avis professionnel.

Chemin de lecture recommandé :

1. [`architecture_devis_reprise/`](docs/examples/architecture_devis_reprise/) — devis de reprise et validation client dangereuse.
2. [`regulatory_watch_conflict/`](docs/examples/regulatory_watch_conflict/) — nouvelle règle externe contre hypothèses de dossiers actifs.
3. [`legal_note/`](docs/examples/legal_note/) — note de stratégie avec sources à vérifier.
4. [`medical_letter/`](docs/examples/medical_letter/) — courrier confrère avec exposition de données réduite.

L’idée n’est pas que Pantheon décide.

L’idée est que Pantheon rend le chemin de décision relisible.

## Sept regards, une décision humaine

Vous n’avez pas besoin de retenir ces noms. Ce sont des angles de revue internes, pas des agents autonomes.

| Rôle | Fonction simple |
|---|---|
| ATHENA | Organise le problème et prépare le plan. |
| ARGOS | Cherche les sources et vérifie la traçabilité. |
| THEMIS | Vérifie le risque, les règles et les limites d’approbation. |
| APOLLO | Relit la clarté, la complétude et la qualité de livraison. |
| ZEUS | Arbitre le statut et la prochaine procédure lorsque des options s’opposent. |
| IRIS | Reformule, clarifie et prépare la communication côté utilisateur. |
| HEPHAISTOS | Prépare les fichiers, les corrections candidates et les pistes d’implémentation. |

Les profils Hermes peuvent s’aligner sur ces rôles, mais ils restent des profils d’exécution limités. Ils n’approuvent pas, ne canonisent pas et ne promeuvent pas la mémoire.

## Pas un outil de plus : une méthode de dossier

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg" width="100%" alt="Méthode Pantheon autour des outils IA : l’écran, l’atelier et la gouvernance restent séparés">
  </a>
</p>

<p align="center"><strong>La méthode autour des outils.</strong><br><em>OpenWebUI montre le travail, Hermes prépare des candidats, Pantheon cadre ce qui est autorisé, revu, approuvé et mémorisé.</em></p>

Pour un lecteur non technique, Pantheon Next a trois parties :

| Vue simple | Nom technique | Sens |
|---|---|---|
| L’écran | OpenWebUI | L’interface de chat où le professionnel demande, lit, choisit les documents, voit les sources et valide. |
| L’atelier | Hermes Agent | Le travailleur externe qui peut chercher, extraire, comparer, convertir, rédiger et préparer des sorties candidates sous mission limitée. |
| La méthode | Pantheon Next | Les règles de travail : ce qui peut être utilisé, ce qui doit être vérifié, ce qui demande une preuve, ce qui demande validation et ce qui peut être gardé. |

Une réponse visible n’est pas automatiquement vraie.

Une tâche terminée n’est pas automatiquement approuvée.

Une sortie utile n’est pas automatiquement une mémoire.

## Le vocabulaire en clair

| Objet | Sens ordinaire |
|---|---|
| Task Contract | Une fiche de mission : quoi faire, avec quels documents, sous quelles limites et avec quelle sortie attendue. |
| Evidence Pack | Un dossier de preuve : sources utilisées, hypothèses, risques, contradictions, actions et état de revue. |
| Memory Candidate | Une information qui pourrait être utile plus tard, mais qui doit encore être revue avant d’être gardée. |
| Canonical Memory | Une mémoire validée, bornée et reliée à des preuves. |
| Context Pack | Le minimum de contexte utile envoyé à un travailleur pour une tâche donnée. |
| Pantheon Role | Un angle de revue : planifier, vérifier, contrôler le risque, améliorer la formulation, arbitrer ou préparer une correction. |
| Knowledge Base | Une bibliothèque documentaire. Elle aide à retrouver l’information, mais elle n’est pas une vérité en soi. |
| Approval | Une décision professionnelle visible, pas un clic technique caché. |

## Ce que Pantheon n’est pas

Pantheon Next n’est pas un chatbot, pas un travailleur IA autonome, pas une mémoire automatique et pas un substitut à la responsabilité professionnelle.

Il ne décide pas seul.

Il n’approuve pas ses propres sorties.

Il ne transforme pas chaque réponse en vérité.

```text
Pantheon Next cadre et contrôle l’exécution.
Il ne l’exécute pas.
```

<details>
<summary>État et structure du projet</summary>

Pantheon Next fournit aujourd’hui une base de gouvernance documentaire.

Implémenté ou documenté :

- doctrine de gouvernance ;
- doctrine de frontière runtime ;
- registre des Pantheon Roles ;
- doctrine du Governance College ;
- doctrine du User Decision Gate ;
- doctrine des Task Contracts ;
- doctrine des Evidence Packs ;
- doctrine des approvals ;
- doctrine mémoire ;
- politique des outils externes ;
- doctrine d’intégration OpenWebUI ;
- doctrine d’intégration Hermes ;
- taxonomie des connaissances et cadrage des scopes ;
- assets narratifs et visuels ;
- templates légers de profils Hermes.

Non implémenté dans ce projet :

- runtime autonome ;
- intégration runtime OpenWebUI ;
- intégration runtime Hermes ;
- génération automatique d’Evidence Packs ;
- interface de revue des Memory Candidates ;
- routage de fournisseurs IA ;
- gestionnaire libre de plugins ;
- réconciliation des schemas ;
- tests ;
- outillage read-only operations ;
- stack de déploiement.

Structure :

```text
docs/governance/     doctrine de gouvernance et documents de statut
docs/examples/       exemples professionnels fictifs
hermes/profiles/     templates légers de profils Hermes candidate-only
docs/assets/         références narratives et visuelles
ai_logs/             historique des interventions assistées par IA
legacy/              source historique Pantheon OS
schemas/             contrats déclaratifs attendus, non réconciliés
operations/          outillage read-only attendu, non implémenté
tests/               tests attendus, non implémentés
```

Points d’entrée principaux :

| Document | Fonction |
|---|---|
| [`docs/governance/STATUS.md`](docs/governance/STATUS.md) | État faisant foi du projet. |
| [`docs/governance/README.md`](docs/governance/README.md) | Index de gouvernance et ordre de lecture. |
| [`docs/governance/EDITORIAL_LANGUAGE.md`](docs/governance/EDITORIAL_LANGUAGE.md) | Guide de langage public et de vocabulaire. |
| [`docs/examples/README.md`](docs/examples/README.md) | Index des exemples professionnels. |
| [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) | Registre canonique des Pantheon Roles. |
| [`docs/governance/GOVERNANCE_COLLEGE.md`](docs/governance/GOVERNANCE_COLLEGE.md) | Séparation des rôles, tensions utiles et arbitrage procédural. |
| [`docs/governance/USER_DECISION_GATE.md`](docs/governance/USER_DECISION_GATE.md) | Escalade vers décision humaine quand la discorde dépasse l’arbitrage sûr. |
| [`docs/governance/TASK_CONTRACTS.md`](docs/governance/TASK_CONTRACTS.md) | Doctrine de cadrage des tâches. |
| [`docs/governance/EVIDENCE_PACK.md`](docs/governance/EVIDENCE_PACK.md) | Doctrine de preuve. |
| [`docs/governance/MEMORY.md`](docs/governance/MEMORY.md) | Doctrine de promotion mémoire. |
| [`docs/governance/APPROVALS.md`](docs/governance/APPROVALS.md) | Niveaux d’approbation. |
| [`docs/governance/HERMES_INTEGRATION.md`](docs/governance/HERMES_INTEGRATION.md) | Doctrine de frontière Hermes. |
| [`docs/governance/OPENWEBUI_INTEGRATION.md`](docs/governance/OPENWEBUI_INTEGRATION.md) | Doctrine de frontière OpenWebUI. |
| [`docs/governance/KNOWLEDGE_TAXONOMY.md`](docs/governance/KNOWLEDGE_TAXONOMY.md) | Vocabulaire source, connaissance, contexte, preuve et mémoire. |

Lorsque des documents se contredisent, traiter `STATUS.md` comme première référence de statut jusqu’à réconciliation.

</details>

## En une formule

```text
L’IA produit des possibles.
Pantheon cadre le chemin.
Hermes prépare le travail.
OpenWebUI montre le résultat.
L’humain décide.
Le validé reste.
```
