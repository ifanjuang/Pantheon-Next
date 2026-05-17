# Pantheon Next

> English version: [README.md](README.md)

> Sources. Preuves. Mémoire. Validation.  
> Une couche de gouvernance pour le travail professionnel assisté par IA.

**État actuel :** Pantheon Next est un repository de gouvernance et de documentation en bootstrap contrôlé. Il est structurellement cohérent, mais partiel. Certains documents sont de la doctrine active. D’autres sont des stubs. Certaines zones d’implémentation sont encore absentes. Pour l’état faisant foi, lire [`docs/governance/STATUS.md`](docs/governance/STATUS.md).

Pantheon Next aide les professionnels à utiliser l’IA sur des dossiers sensibles sans perdre la maîtrise des sources, des hypothèses, des preuves, de la mémoire et de la validation.

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

En langage simple :

- **OpenWebUI** est l’application de chat IA visible : l’endroit où l’utilisateur parle à l’IA, dépose ou consulte des documents, voit les réponses et donne les validations. Elle peut être auto-hébergée et open source.
- **Hermes Agent** est l’atelier technique externe : la partie qui peut chercher, extraire, comparer, transcrire, préparer des fichiers ou produire des candidats.
- **Pantheon Next** est le cadre de contrôle : il dit ce qui est autorisé, ce qui doit être vérifié, ce qui demande une preuve, ce qui demande validation et ce qui peut devenir mémoire.

L’IA peut accélérer la lecture, la comparaison, la rédaction, l’extraction et la revue. Elle peut aussi mélanger les contextes, lisser les contradictions et transformer une hypothèse fragile en certitude apparente.

Pantheon Next sert à empêcher cette dérive.

Il cadre la tâche, sépare la source de la preuve, garde la mémoire candidate jusqu’à validation et rend la décision humaine explicite.

```text
L’IA ouvre les possibles.
Pantheon les organise.
L’humain décide.
Le validé reste.
```

---

## Ce que ce repository est

Pantheon Next est une **couche de gouvernance** pour les workflows professionnels assistés par IA.

Plus simplement : c’est un ensemble de règles, de méthodes et de documents de référence pour utiliser l’IA sur de vrais dossiers professionnels sans transformer chaque réponse en vérité.

Il définit :

| Zone | Fonction |
|---|---|
| Doctrine | Les règles de base du système. |
| Rôles | Des angles de revue : plan, preuve, risque, qualité, arbitrage, formulation et préparation d’implémentation. |
| Task Contracts | Des fiches de mission qui disent ce qui est demandé, avec quelles limites et quel résultat attendu. |
| Evidence Packs | Des dossiers de preuve qui montrent les sources, hypothèses, risques et éléments réellement utilisés. |
| Niveaux d’approbation | Les seuils de décision pour rédiger, modifier, transmettre, mémoriser ou rejeter. |
| Politique mémoire | La règle selon laquelle rien ne devient mémoire durable par accident. |
| Taxonomie des connaissances | La distinction entre source, référence utile, preuve, contexte et mémoire validée. |
| Politique des outils externes | Les règles pour la recherche, les emails, les fichiers, les connecteurs, les providers, les écritures et les données sensibles. |
| Frontières d’intégration | Ce que l’application de chat peut montrer et ce que l’atelier d’exécution peut faire. |

Pantheon Next ne remplace pas le jugement professionnel. Il structure les conditions dans lesquelles une sortie IA peut devenir un travail professionnel.

---

## Ce que ce repository n’est pas

Pantheon Next n’est pas :

- un chatbot ;
- un runtime agentique autonome ;
- un tool runtime ;
- un routeur de providers LLM ;
- un scheduler ;
- une queue ou un message bus ;
- un runtime LangGraph central ;
- un moteur de workflow caché ;
- un plugin manager libre ;
- un système de mémoire auto-promue ;
- un installateur automatique de skills ;
- un dashboard à surveiller toute la journée ;
- un remplacement de la responsabilité professionnelle.

Plus simplement : Pantheon n’est pas la machine qui fait tout toute seule. C’est le cadre qui empêche la machine de faire la mauvaise chose silencieusement.

La règle est simple :

```text
Pantheon Next gouverne l’exécution.
Il ne l’exécute pas.
```

---

## Le modèle opératoire

Pantheon Next repose sur trois surfaces distinctes.

| Surface | Rôle simple | Frontière |
|---|---|---|
| Application de chat — OpenWebUI | Le cockpit visible. Le professionnel pose ses questions, apporte ses documents, voit les résultats et donne les validations. | Il peut afficher de l’information, mais l’affichage ne rend rien vrai. Il ne valide pas la mémoire tout seul. |
| Atelier d’exécution — Hermes Agent | Le travailleur externe. Il peut chercher, extraire, comparer, transcrire, rédiger, préparer des fichiers ou retourner des résultats candidats. | Il exécute sous règles. Il n’approuve pas son propre travail et ne décide pas de ce qui devient mémoire. |
| Cadre de gouvernance — Pantheon Next | Le livre de règles. Il définit les rôles, le cadrage des tâches, les preuves, les validations, les règles mémoire et les limites des outils. | Il gouverne la légitimité. Il ne devient pas un moteur d’exécution caché. |

La doctrine courte reste :

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

Un résultat visible dans le chat n’est pas automatiquement validé. Un travail terminé par un outil d’exécution n’est pas automatiquement approuvé. Un document trouvé par recherche n’est pas automatiquement une preuve. Une réponse utile n’est pas automatiquement une mémoire.

---

## Vocabulaire clé en mots ordinaires

| Terme Pantheon | Sens ordinaire |
|---|---|
| Task Contract | Une fiche de mission : quoi faire, avec quels documents, sous quelles limites et avec quelle sortie attendue. |
| Evidence Pack | Un dossier de preuve : sources utilisées, hypothèses, risques, contradictions, actions et état de revue. |
| Memory Candidate | Une information qui pourrait être utile plus tard, mais qui doit encore être revue avant d’être gardée. |
| Canonical Memory | Une mémoire validée, bornée et reliée à des preuves. |
| Context Pack | Le minimum de contexte utile envoyé à un travailleur pour une tâche donnée. |
| Pantheon Role | Un angle de revue : planifier, vérifier, contrôler le risque, améliorer la formulation, arbitrer ou préparer un patch. |
| Knowledge Base | Une bibliothèque documentaire. Elle aide à retrouver l’information, mais elle n’est pas une vérité en soi. |
| Approval | Une décision professionnelle visible, pas un clic technique caché dans le système. |

Ce vocabulaire est important parce que beaucoup de risques IA viennent de la confusion entre ces couches.

---

## Boucle professionnelle

Pantheon transforme une demande IA vague en chemin professionnel contrôlé.

```text
Demande utilisateur
→ fiche de mission
→ entrée des sources
→ sélection du périmètre et du contexte
→ stratégie de travail
→ exécution externe
→ dossier de preuve
→ revue humaine
→ sortie approuvée, sortie rejetée ou proposition mémoire
→ mémoire validée uniquement après approbation
```

La boucle doit rester continue lorsque le système peut travailler sans risque. Elle doit s’interrompre uniquement lorsque l’utilisateur doit valider, vérifier, choisir, fournir une information manquante ou accepter une action engageante.

C’est l’idée produit centrale : l’IA peut faire plus de travail entre les portes de validation, mais elle ne doit jamais franchir ces portes silencieusement.

---

## Pourquoi c’est utile

Un dossier professionnel n’est pas seulement un ensemble de documents. Il contient des obligations, des risques, des contradictions, des délais, des informations privées et des décisions qui peuvent engager la responsabilité.

Un dossier peut contenir contrats, plans, rapports, emails, devis, règlements, notes de réunion, PDF, sources web, images, tableurs et versions contradictoires.

Sans gouvernance, l’IA produit surtout une réponse. Avec Pantheon, la cible est différente : un résultat qui peut être relu, contesté, limité, approuvé, rejeté ou mémorisé avec traçabilité.

| Sans Pantheon | Avec Pantheon |
|---|---|
| Une réponse utile, difficile à vérifier. | Une sortie relisible, liée aux sources et aux hypothèses. |
| Des sources dispersées entre les outils. | Des sources identifiées, bornées et enregistrées. |
| Des hypothèses qui peuvent devenir des faits cachés. | Des hypothèses visibles et discutables. |
| Une mémoire qui garde trop, ou mal. | Une mémoire qui reste candidate jusqu’à validation. |
| Des décisions difficiles à retracer. | Des preuves et un état d’approbation visibles. |
| Un usage IA fragmenté. | Un chemin de travail professionnel gouverné. |

---

## Premier scénario démontrable

Le premier scénario clair est la revue maîtrisée d’un dossier sensible.

```text
Dossier sensible
→ fiche de mission
→ exécution externe
→ dossier de preuve
→ revue humaine
→ sortie validée ou proposition mémoire
```

Entrées typiques :

- contrat ;
- CCTP ou descriptif technique ;
- devis ;
- rapport technique ;
- note juridique ;
- dossier projet ;
- fil d’emails ;
- transcription de réunion ;
- versions documentaires contradictoires.

Sorties typiques :

- synthèse des risques ;
- liste des obligations ;
- rapport de contradictions ;
- informations manquantes ;
- hypothèses à vérifier ;
- synthèse sourcée ;
- propositions mémoire ;
- checklist de validation finale.

Une démonstration réussie doit montrer ce qui a été demandé, quelles sources ont été utilisées, ce qui a été supposé, ce qui reste incertain, ce qui contredit quoi, ce qui demande validation, ce qui peut être transmis, ce qui peut devenir mémoire et ce qui doit être rejeté.

---

## Objets de gouvernance

| Objet | Rôle |
|---|---|
| Task Contract | Cadre l’intention, le périmètre, les sources, les contraintes, les sorties autorisées, les sorties interdites, le plafond d’approbation et les règles mémoire. |
| Evidence Pack | Conserve le dossier de preuve relisible : sources, hypothèses, actions, risques, sorties, revues, propositions mémoire et état d’approbation. |
| Approval Levels | Définissent les seuils de décision pour lecture, rédaction, actions réversibles, changements persistants, effets externes et actions critiques. |
| Memory Candidate | Information durable proposée. Elle n’est pas canonique par défaut. |
| Canonical Memory | Mémoire validée, bornée et reliée aux preuves. |
| Context Pack | Artefact de contexte borné pouvant être transmis à un runtime externe. |
| External Tools Policy | Gouverne les capacités qui lisent, transforment, écrivent, envoient, publient, configurent, exécutent ou influencent la mémoire. |
| AI Log | Trace les interventions significatives assistées par IA dans le repository. |

---

## Rôles Pantheon

Le fichier [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) conserve son nom historique, mais le concept canonique est **Pantheon Role**.

Les rôles sont des points de vue de gouvernance. Ce ne sont pas des agents runtime autonomes.

| Rôle | Fonction |
|---|---|
| ATHENA | Organise le problème et prépare le plan. |
| ARGOS | Cherche les sources et vérifie la traçabilité. |
| THEMIS | Vérifie le risque, les règles et les limites d’approbation. |
| APOLLO | Relit la clarté, la complétude et la qualité de livraison. |
| ZEUS | Arbitre lorsque plusieurs options entrent en conflit. |
| IRIS | Reformule, clarifie et prépare la communication côté utilisateur. |
| HEPHAISTOS | Prépare les builds, patch candidates et implementation candidates. |

Les profils Hermes peuvent s’aligner sur ces rôles, mais ils restent des profils d’exécution candidate-only. Ils n’approuvent pas, ne canonisent pas et ne promeuvent pas la mémoire.

---

## Connaissance, preuve et mémoire

Pantheon Next n’utilise pas un grand seau de vérité unique.

```text
Raw Source       matière disponible
Knowledge        information de référence organisée
Context          information bornée à la tâche
Evidence         support sélectionné pour une affirmation ou une sortie
Memory Candidate information durable proposée
Canonical Memory mémoire approuvée, bornée et reliée aux preuves
Doctrine         couche de règles
Runtime State    état d’exécution externe, jamais mémoire canonique
```

Une source n’est pas automatiquement une preuve.

Un document retrouvé n’est pas automatiquement une vérité.

Une Knowledge Base est une bibliothèque documentaire, pas une mémoire validée.

Une sortie modèle n’est pas une mémoire.

Une observation répétée n’est pas une mémoire.

La mémoire ne devient canonique qu’avec preuve, revue, périmètre et approbation.

---

## Les outils du quotidien comme entrées gouvernées

Pantheon Next ne remplace pas les outils professionnels. Il gouverne la manière dont leurs informations peuvent entrer dans un dossier.

| Canal | Rôle | État actuel |
|---|---|---|
| OpenWebUI | Application de chat IA auto-hébergeable où l’utilisateur interagit avec le système. | Doctrine de cockpit visée. |
| Hermes Agent | Atelier technique externe qui réalise le travail contrôlé. | Doctrine de runtime visée. |
| Fichiers locaux et PDF | Documents déjà présents dans le dossier professionnel. | Entrée visée. |
| Email, Gmail, Outlook | Messages et pièces jointes pouvant devenir sources. | Point d’entrée gouverné visé. |
| Google Drive, Docs, Sheets | Documents et tableaux partagés pouvant soutenir le travail. | Point d’entrée gouverné visé. |
| Documents Office | Fichiers professionnels et exports. | Point d’entrée gouverné visé. |
| Calendriers et notes | Échéances, rappels et notes de travail. | Point d’entrée gouverné visé. |
| Notion, Trello, Slack | Connaissance projet et échanges équipe. | Point d’entrée gouverné visé. |
| WhatsApp, Telegram | Messages, notes vocales et images. | Futur point d’entrée gouverné. |
| Recherche web | Découverte de sources externes. | Flux externe gouverné. |

Ces éléments ne sont pas des connecteurs Pantheon intégrés automatiquement, sauf implémentation séparée dans la couche d’exécution externe.

Les outils restent des canaux. Ils ne deviennent pas vérité.

---

## Parcours visuel

Pantheon utilise une métaphore de cité-jeu pour expliquer le modèle de gouvernance aux utilisateurs professionnels non techniques. La couche visuelle est une doctrine explicative. Elle ne redéfinit pas Pantheon comme moteur de jeu, cité autonome, workflow runner caché ou runtime.

La séquence visuelle suit maintenant l’histoire commerciale : pourquoi Pantheon existe, qui fait quoi, comment un dossier professionnel avance de la demande au résultat candidat, puis comment les sources, les preuves, la mémoire et l’information externe restent gouvernées.

Les planches actuelles sont principalement en français et utilisent des noms de fichiers stables. Leur inventaire est suivi dans [`docs/assets/pantheon-rpg/ASSET_REGISTER.md`](docs/assets/pantheon-rpg/ASSET_REGISTER.md).

### 0. Avant / Après — de l’IA brute au dossier gouverné

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg" width="100%" alt="Pantheon RPG avant après dossier gouverné">
  </a>
</p>

C’est la planche manifeste. Elle oppose l’IA brute au dossier professionnel gouverné. L’IA seule peut répondre, mais Pantheon cadre le travail, sépare les sources des preuves, rend l’incertitude visible et laisse la validation au professionnel.

Chemin image : `before_after_01_fr.jpg`.

### 1. Qui fait quoi ? — OpenWebUI, Hermes et Pantheon

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg" width="100%" alt="Pantheon RPG qui fait quoi">
  </a>
</p>

Cette planche clarifie le modèle opératoire. OpenWebUI est le cockpit visible. Hermes est l’atelier d’exécution. Pantheon est le cadre de gouvernance qui fixe les règles, le périmètre, les attentes de preuve, la validation et le statut mémoire.

Chemin image : `ui_hermes_pantheon_01_fr.jpg`.

### 2. Parcours joueur — de la demande au livrable candidat

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg" width="100%" alt="Pantheon RPG parcours joueur demande livrable">
  </a>
</p>

Le joueur est l’utilisateur professionnel. Il apporte la question, le dossier, les contraintes, l’expertise et le jugement final. Pantheon structure le passage de la demande vers une sortie candidate. L’IA accélère certaines tâches, mais la responsabilité reste humaine.

Chemin image : `player_journey_01_fr.jpg`.

### 3. Port — les sources entrent sous contrôle

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/port_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/port_01_fr.jpg" width="100%" alt="Pantheon RPG port des sources contrôlées">
  </a>
</p>

Le port représente les flux externes : web, emails, fichiers, API, messageries et connecteurs. Pantheon gouverne ce qui peut entrer dans le dossier, ce qui doit rester temporaire, ce qui doit être rejeté et ce qui peut devenir preuve. Les outils restent des canaux. Ils ne deviennent pas vérité.

Chemin image : `port_01_fr.jpg`.

### 4. Evidence — la preuve avant la confiance

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/evidence_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/evidence_01_fr.jpg" width="100%" alt="Pantheon RPG atelier des preuves">
  </a>
</p>

Cette planche montre l’atelier des preuves. Les sources sélectionnées, les hypothèses, les contradictions et les tables de revue deviennent visibles avant qu’un livrable soit considéré comme fiable. La preuve soutient la revue. Elle ne s’approuve pas elle-même.

Chemin image : `evidence_01_fr.jpg`.

### 5. Citadel — la ville du dossier gouverné

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/citadel_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/citadel_01_fr.jpg" width="100%" alt="Pantheon RPG citadelle dossier gouverné">
  </a>
</p>

La citadelle représente le dossier professionnel gouverné. Les sources passent par des portes contrôlées. Les hypothèses restent visibles. Le professionnel décide ce qui demeure.

Chemin image : `citadel_01_fr.jpg`.

### 6. Mémoire — compartimentée, pas un grand vrac

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg" width="100%" alt="Pantheon RPG mémoire compartimentée">
  </a>
</p>

La mémoire n’est pas un grand vrac. Mémoire projet, mémoire système, sessions, versions et décisions validées doivent rester bornées. La mémoire ne se promeut pas seule. Une sortie utile reste candidate jusqu’à ce que revue, preuve, périmètre et validation rendent sa conservation légitime.

Chemin image : `memory_compartment_01_fr.jpg`.

### 7. Pantheon — résumé système et cadre de gouvernance

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg" width="100%" alt="Pantheon RPG résumé système gouvernance">
  </a>
</p>

Pantheon est la couche de gouvernance autour de la stack. Il ne remplace pas OpenWebUI ou Hermes. Il rend leur configuration, leurs sorties, la discipline de preuve, les seuils de validation et la mémoire de décision relisibles.

Chemin image : `pantheon_system_summary_01_fr.jpg`.

### 8. Worldmap — l’IA et Internet restent des mondes externes

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg" width="100%" alt="Pantheon RPG carte IA Internet">
  </a>
</p>

L’IA, le web et les connaissances externes forment des mondes riches mais instables. Connaissances utiles, sources faibles, informations obsolètes, contradictions et découvertes inattendues coexistent. Pantheon ne ferme pas ce monde. Il donne au professionnel une méthode pour le traverser sans confondre signal, source, preuve et mémoire.

Chemin image : `worldmap_ai_internet_01_fr.jpg`.

### 9. Livrables — les sorties candidates avant transmission

Image à produire : `docs/assets/pantheon-rpg/references/livrables_01_fr.jpg`.

Cette planche doit montrer rapports, tableaux, courriers, diagrammes, présentations et dossiers d’export quittant les ateliers uniquement après revue. Un livrable reste candidat tant que le chemin d’approbation requis n’est pas complet.

---

## État d’implémentation actuel

Pantheon Next fournit aujourd’hui une base de gouvernance documentaire.

Implémenté ou documenté :

- doctrine de gouvernance ;
- doctrine de frontière runtime ;
- registre des Pantheon Roles ;
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

Non implémenté dans ce repository :

- runtime autonome ;
- intégration runtime OpenWebUI ;
- intégration runtime Hermes ;
- génération automatique d’Evidence Packs ;
- interface de revue des Memory Candidates ;
- provider routing ;
- plugin management ;
- réconciliation des schemas ;
- tests ;
- outillage read-only operations ;
- stack de déploiement.

L’état doit être vérifié capacité par capacité dans [`docs/governance/STATUS.md`](docs/governance/STATUS.md).

---

## Structure du repository

```text
docs/governance/     doctrine de gouvernance et documents de statut
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
| [`docs/governance/STATUS.md`](docs/governance/STATUS.md) | État faisant foi du repository. |
| [`docs/governance/README.md`](docs/governance/README.md) | Index de gouvernance et ordre de lecture. |
| [`docs/governance/ARCHITECTURE.md`](docs/governance/ARCHITECTURE.md) | Anatomie de gouvernance et modèle de frontière. |
| [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) | Registre canonique des Pantheon Roles. |
| [`docs/governance/TASK_CONTRACTS.md`](docs/governance/TASK_CONTRACTS.md) | Doctrine de cadrage des tâches. |
| [`docs/governance/EVIDENCE_PACK.md`](docs/governance/EVIDENCE_PACK.md) | Doctrine de preuve. |
| [`docs/governance/MEMORY.md`](docs/governance/MEMORY.md) | Doctrine de promotion mémoire. |
| [`docs/governance/APPROVALS.md`](docs/governance/APPROVALS.md) | Niveaux d’approbation. |
| [`docs/governance/HERMES_INTEGRATION.md`](docs/governance/HERMES_INTEGRATION.md) | Doctrine de frontière Hermes. |
| [`docs/governance/OPENWEBUI_INTEGRATION.md`](docs/governance/OPENWEBUI_INTEGRATION.md) | Doctrine de frontière OpenWebUI. |
| [`docs/governance/EXTERNAL_TOOLS_POLICY.md`](docs/governance/EXTERNAL_TOOLS_POLICY.md) | Gouvernance des capacités externes. |
| [`docs/governance/KNOWLEDGE_TAXONOMY.md`](docs/governance/KNOWLEDGE_TAXONOMY.md) | Vocabulaire source, connaissance, contexte, preuve et mémoire. |

Lorsque des documents se contredisent, traiter `STATUS.md` comme première référence de statut jusqu’à réconciliation.

---

## Priorités proches

- construire un dossier de démonstration fictif ;
- fournir un exemple de Task Contract ;
- fournir un exemple d’Evidence Pack ;
- produire la planche manquante `livrables_01_fr.jpg` ;
- clarifier l’état d’implémentation par capacité ;
- documenter les premiers packs de cas d’usage professionnels ;
- préparer des exemples de handoff OpenWebUI et Hermes ;
- reconsidérer les schemas sous règle de fichier protégé ;
- ajouter un outillage de validation read-only uniquement s’il préserve la frontière de gouvernance.

---

## Principe final

```text
L’IA produit des possibles.
Pantheon gouverne le chemin.
Hermes exécute le travail.
OpenWebUI expose le résultat.
L’humain décide.
Le validé reste.
```
