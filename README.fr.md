# Pantheon Next

> English version: [README.md](README.md)

> **L’IA ouvre les possibles. Pantheon les organise. L’humain décide. Le validé reste.**

<sub><strong>État actuel :</strong> Pantheon Next est un référentiel de méthode et de documentation en cours de structuration. Il est cohérent, mais partiel. Pour l’état d’implémentation faisant foi, lire <a href="docs/governance/STATUS.md">docs/governance/STATUS.md</a>.</sub>

Pantheon Next aide les professionnels à utiliser l’IA sur des dossiers sérieux sans perdre la maîtrise des sources, des hypothèses, des preuves, des livrables, de la mémoire et de la validation.

Pour les métiers libéraux, on peut le comprendre comme un **registre de déontologie et de méthode de travail pour l’IA**. Avant qu’une IA reçoive une demande et produise une réponse, Pantheon fixe le cadre : quelles informations peuvent être utilisées, ce qui doit être vérifié, ce qui doit être sourcé, ce qui demande validation et ce qui peut être conservé.

Ce n’est pas un outil IA de plus. C’est une méthode professionnelle pour garder le travail IA cadré, traçable et relisible.

<details>
<summary>Sommaire</summary>

- [Pantheon Next en 1 minute](#pantheon-next-en-1-minute)
- [Les quatre peurs que Pantheon traite](#les-quatre-peurs-que-pantheon-traite)
- [De l’IA brute au dossier maîtrisé](#de-lia-brute-au-dossier-maîtrisé)
- [Qui fait quoi ?](#qui-fait-quoi-)
- [Où tourne le modèle IA ?](#où-tourne-le-modèle-ia-)
- [Le chemin professionnel](#le-chemin-professionnel)
- [Exemples concrets : avocat et médecin généraliste](#exemples-concrets--avocat-et-médecin-généraliste)
- [Pour qui ?](#pour-qui-)
- [Objets de travail clés](#objets-de-travail-clés)
- [Rôles Pantheon](#rôles-pantheon)
- [Et maintenant ?](#et-maintenant-)

</details>

## Pantheon Next en 1 minute

- **Cadre la demande** avant que l’IA n’agisse — mission, sources et limites sont posées d’abord.
- **Garde les preuves visibles** — sources, hypothèses, contradictions et informations manquantes restent affichées.
- **Laisse la décision au professionnel** — l’IA propose, l’humain valide ou rejette.
- **Compartimente la mémoire** — rien ne devient durable sans revue, périmètre et validation.
- **Fonctionne avec ChatGPT, Claude, Gemini ou un modèle local** — la méthode s’adapte à la sensibilité du dossier.

En façade, les trois parties sont simples :

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

## Les quatre peurs que Pantheon traite

| Peur professionnelle | Réponse Pantheon |
|---|---|
| Mes données vont-elles partir n’importe où ? | Les informations peuvent être minimisées, brouillées ou traitées localement selon le niveau de sensibilité. |
| L’IA va-t-elle inventer ? | Les sources, hypothèses, contradictions et informations manquantes restent visibles. |
| Qui décide ? | L’IA propose. Le professionnel valide. |
| Que reste-t-il après coup ? | Seules les informations validées, bornées et reliées à un contexte peuvent devenir mémoire. |

## De l’IA brute au dossier maîtrisé

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg" width="100%" alt="Pantheon RPG avant après dossier maîtrisé">
  </a>
</p>

L’IA seule peut répondre vite. C’est utile, mais insuffisant pour un travail qui engage une responsabilité.

Pantheon cadre la demande, sépare les sources des preuves, rend l’incertitude visible, conserve les contradictions et laisse la validation au professionnel.

```text
Utiliser l’IA plus vite sans perdre la méthode du dossier.
```

## Qui fait quoi ?

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/ui_hermes_pantheon_01_fr.jpg" width="100%" alt="Pantheon RPG qui fait quoi">
  </a>
</p>

Pour un lecteur non technique, Pantheon Next se comprend en trois parties :

| Vue simple | Nom technique | Ce que ça veut dire |
|---|---|---|
| **L’écran** | OpenWebUI | L’application de chat IA locale et open source où le professionnel pose sa question, choisit ses documents, voit les sources et valide. |
| **L’atelier** | Hermes Agent | Le travailleur qui peut chercher, extraire, comparer, convertir, rédiger et préparer des sorties candidates dans une mission limitée. |
| **La méthode** | Pantheon Next | Les règles de travail : ce qui peut être utilisé, ce qui doit être vérifié, ce qui demande une preuve, ce qui demande validation et ce qui peut être gardé. |

Une réponse visible n’est pas automatiquement vraie. Une tâche terminée n’est pas automatiquement approuvée. Une sortie utile n’est pas automatiquement une mémoire.

## Où tourne le modèle IA ?

Pantheon n’impose pas une seule stratégie de modèle.

Une équipe peut utiliser des services IA externes comme ChatGPT, Claude ou Gemini lorsque le dossier le permet. Dans ce cas, Pantheon sert à réduire l’exposition avant que quelque chose ne sorte de l’environnement contrôlé : noms privés, adresses de projet, références client, identifiants contractuels ou extraits sensibles peuvent être remplacés, minimisés ou brouillés. La réponse reçue reste un candidat.

Une équipe peut aussi utiliser un modèle local. Dans ce cas, le modèle tourne dans un environnement maîtrisé : par exemple sur un poste équipé d’un **GPU** (carte graphique dédiée), sur une machine locale dédiée, ou sur un **NAS** (serveur de fichiers du cabinet) isolé avec **Docker** (conteneur logiciel). Cette option garde davantage de données dans l’infrastructure du cabinet, mais demande du matériel, de la maintenance et une discipline d’exploitation.

Dans les deux cas, la règle reste la même :

```text
Le modèle propose.
Pantheon cadre la méthode.
Le professionnel valide.
```

## Le chemin professionnel

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/player_journey_01_fr.jpg" width="100%" alt="Pantheon RPG parcours joueur demande livrable">
  </a>
</p>

Le joueur est l’utilisateur professionnel. Il apporte la question, le dossier, les contraintes, l’expertise et le jugement final.

Pantheon transforme une demande IA vague en chemin professionnel contrôlé :

```text
Demande utilisateur
→ fiche de mission
→ entrée des sources
→ sélection du périmètre et du contexte
→ stratégie de travail
→ exécution externe
→ dossier de preuve
→ livrable candidat
→ revue humaine
→ sortie approuvée, sortie rejetée ou proposition mémoire
→ mémoire validée uniquement après approbation
```

L’IA peut faire plus de travail entre les portes de validation, mais elle ne doit jamais franchir ces portes silencieusement.

## Exemples concrets : avocat et médecin généraliste

Deux scénarios métier qui montrent la différence entre une réponse IA brute et un livrable cadré par Pantheon.

### Cabinet d’avocats — préparer une audience de mise en état

> **Demande** : « À partir des conclusions adverses (52 pages), du contrat litigieux et de mes 8 pièces, prépare une note de stratégie pour l’audience de mise en état. »

**Sans Pantheon.** L’IA produit 4 pages bien tournées. Elles peuvent inclure une jurisprudence inexistante — cas déjà constaté devant des juridictions françaises — mélanger les pièces et lisser les contradictions. Le secret professionnel peut être engagé si les noms des parties partent dans un service grand public.

**Avec Pantheon.**

- **Fiche de mission** — périmètre : ce litige uniquement. Sources autorisées : les 10 pièces du dossier. Jurisprudence : à vérifier sur Légifrance avant citation. Sortie attendue : note de stratégie de 3 pages.
- **Minimisation avant envoi externe** — noms des parties, numéros RG et identifiants client remplacés par des étiquettes neutres.
- **Dossier de preuve** — 6 moyens identifiés (avec n° de pièce et page), 2 contradictions repérées entre les conclusions adverses et la pièce P-3, 3 hypothèses à confirmer, 1 référence jurisprudentielle marquée « à vérifier ».
- **Livrable candidat** — note de 3 pages, 11 citations sourcées, contradictions surlignées.
- **Validation** — l’avocat tranche, signe et archive. Rien n’est mémorisé tant qu’il ne le décide.

<details>
<summary>Extrait — fiche de mission (Task Contract)</summary>

```text
Mission        : Note de stratégie — audience de mise en état
Périmètre      : Dossier [RG-MASQUÉ], cabinet [ID-MASQUÉ]
Sources OK     : P-01 à P-08 (pièces client)
                 Conclusions adverses (PDF, 52 p.)
                 Contrat litigieux du [DATE-MASQUÉE]
                 Légifrance (vérification jurisprudence uniquement)
Sources KO     : autres dossiers du cabinet, base RH interne
Sortie         : note 3 pages — moyens, contradictions, hypothèses
Plafond        : transmission interne ; aucun envoi externe sans visa avocat
Mémoire        : rien ne devient mémoire du cabinet sans signature
```

</details>

<details>
<summary>Extrait — livrable candidat (note de stratégie)</summary>

```text
## Moyens identifiés

1. Inexécution contractuelle (art. 1217 C. civ.)
   Source       : pièce P-03, p. 4 (mise en demeure du [DATE])
   Renforcé par : pièce P-05 (échange email du [DATE])
   Statut       : à confirmer — manque la preuve de réception

2. Contradiction adverse / pièce P-03
   Adverse §17  : livraison alléguée le [DATE]
   Pièce P-03   : bon de livraison signé [DATE + 15 j]
   Statut       : pièce maîtresse pour l'audience

3. Cass. com., [DATE], n° [REF]
   Statut       : À VÉRIFIER sur Légifrance avant citation orale
```

Les marqueurs `[MASQUÉ]` correspondent aux champs ré-identifiés en local après revue ; ils ne quittent jamais le cabinet sous forme nominative.

</details>

### Médecin généraliste — courrier au confrère cardiologue

> **Demande** : « Prépare un courrier de correspondance au cardiologue à partir de ma consultation et des dernières analyses. »

**Sans Pantheon.** Tentation forte de coller le compte-rendu nominatif dans une IA grand public. Violation potentielle du secret médical (art. R.4127-4 CSP) et du RGPD si l’IA n’est pas hébergée en données de santé.

**Avec Pantheon.**

- **Fiche de mission** — périmètre : ce patient, cette correspondance. Sources : compte-rendu de consultation, biologie, ECG. Sortie attendue : lettre confrère d’1 page. IA externe autorisée uniquement sur version pseudonymisée.
- **Pseudonymisation préalable** — nom, date de naissance, NIR, adresse remplacés avant tout envoi.
- **Dossier de preuve** — 4 éléments cliniques cités (tension, fréquence, antécédents, traitement en cours), 2 résultats biologiques joints, 1 question explicite posée au confrère.
- **Livrable candidat** — courrier d’1 page, identifiants ré-injectés en local après revue.
- **Validation** — le médecin signe, archive dans le dossier patient. La donnée identifiante n’est jamais sortie du cabinet.

<details>
<summary>Extrait — fiche de mission (Task Contract)</summary>

```text
Mission        : Lettre de correspondance — cardiologie
Périmètre      : Patient [PSEUDO-A7], consultation du [DATE-MASQUÉE]
Sources OK     : compte-rendu du jour (pseudonymisé)
                 biologie du [DATE] (valeurs numériques uniquement)
                 ECG du [DATE]
                 antécédents pertinents (HTA, traitement en cours)
Sources KO     : autres dossiers patients, historique non lié
Sortie         : lettre confrère 1 page — ton clinique, question explicite
Plafond        : ré-identification en local uniquement ; envoi après signature
Mémoire        : archivage dans le dossier patient ; pas de mémoire IA durable
```

</details>

<details>
<summary>Extrait — livrable candidat (courrier au confrère)</summary>

```text
Cher confrère,

Je vous adresse mon patient [PSEUDO-A7], 58 ans, hypertendu traité par
[traitement-actuel], pour avis cardiologique.

Motif : palpitations intermittentes apparues il y a 3 semaines,
sans syncope ni douleur thoracique.

Éléments cliniques du jour :
  - TA  : 142/88 mmHg
  - FC  : 92/min, irrégulière à l'auscultation
  - ECG : extrasystoles ventriculaires (tracé joint)

Biologie du [DATE] :
  - kaliémie 3,9 mmol/L
  - TSH normale
  - troponine non dosée

Question : confirmation diagnostique et indication d'un Holter 24 h ?

Confraternellement,
Dr [NOM-MASQUÉ]
```

La version envoyée à l'IA externe reste pseudonymisée ; les identifiants (`[PSEUDO-A7]`, `[NOM-MASQUÉ]`, dates) sont ré-injectés sur le poste du médecin avant signature.

</details>

Dans les deux cas, le message est le même : **l’IA accélère, Pantheon cadre, le professionnel valide.**

## Pour qui ?

| Profession | Cas d’usage typique |
|---|---|
| Architecte, MOE, AMO | Relire un dossier technique, comparer devis, CCTP, échanges et risques avant décision. |
| Avocat ou juriste | Préparer une note sourcée, repérer obligations, contradictions et points à vérifier. |
| Notaire | Structurer les pièces d’un dossier, isoler les manques, tracer les hypothèses. |
| Expert-comptable ou consultant | Produire une synthèse exploitable à partir de documents, tableaux et échanges clients. |
| Médecin ou professionnel de santé | Organiser une analyse documentaire sans mélanger hypothèse, source et décision clinique. |
| DPO, expert judiciaire, dirigeant | Garder la trace des sources, validations, limites et responsabilités dans les usages IA. |

Le point commun : utiliser l’IA sans abandonner la méthode, la confidentialité et la responsabilité professionnelle.

## Une source n’est pas une preuve

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/port_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/port_01_fr.jpg" width="100%" alt="Pantheon RPG port des sources contrôlées">
  </a>
</p>

Le port représente les flux externes : web, emails, fichiers, API, messageries, dossiers locaux et connecteurs.

Pantheon définit ce qui peut entrer dans le dossier, ce qui reste temporaire, ce qui doit être rejeté et ce qui peut devenir preuve.

```text
Source trouvée ≠ preuve.
Document récupéré ≠ vérité.
Bibliothèque documentaire ≠ mémoire.
Réponse utile ≠ validation.
```

## La preuve avant la confiance

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/evidence_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/evidence_01_fr.jpg" width="100%" alt="Pantheon RPG atelier des preuves">
  </a>
</p>

Un dossier professionnel demande plus que des citations. Il demande des appuis relisibles.

Pantheon garde visibles :

| Élément | Pourquoi c’est important |
|---|---|
| Sources utilisées | L’utilisateur peut vérifier d’où vient la réponse. |
| Hypothèses | Le système ne cache pas ce qui reste supposé. |
| Contradictions | Les conflits restent visibles au lieu d’être lissés. |
| Informations manquantes | Le système peut s’arrêter et demander ce qui manque. |
| État de preuve | Une source ne devient preuve qu’après revue. |
| État de validation | Le professionnel décide ce qui peut être utilisé, transmis ou conservé. |

La preuve soutient la revue. Elle ne s’approuve pas elle-même.

## Du résultat candidat au livrable professionnel

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/livrables_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/livrables_01_fr.jpg" width="100%" alt="Pantheon RPG atelier de production des livrables">
  </a>
</p>

Pantheon ne sert pas seulement à répondre à une question. Le but est de produire quelque chose d’exploitable : une note, un tableau, un courrier, une synthèse, un schéma, un rapport, une checklist ou un dossier d’export.

Un livrable reste candidat tant que la revue et le chemin d’approbation nécessaires ne sont pas terminés.

```text
Brouillon ≠ livrable.
Livrable candidat ≠ sortie validée.
Sortie validée ≠ mémoire.
```

## La mémoire reste compartimentée

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/memory_compartment_01_fr.jpg" width="100%" alt="Pantheon RPG mémoire compartimentée">
  </a>
</p>

Pantheon n’utilise pas un grand seau de vérité unique.

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

La mémoire ne se promeut pas seule. Une sortie utile reste candidate jusqu’à ce que revue, preuve, périmètre et validation rendent sa conservation légitime.

## La ville du dossier maîtrisé

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/citadel_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/citadel_01_fr.jpg" width="100%" alt="Pantheon RPG citadelle dossier gouverné">
  </a>
</p>

La citadelle représente le dossier professionnel sous contrôle.

Les sources passent par des portes contrôlées. Les hypothèses restent visibles. Les sessions, les versions, les preuves et la mémoire restent bornées. Le professionnel décide ce qui demeure.

## Une méthode autour des outils IA

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/pantheon_system_summary_01_fr.jpg" width="100%" alt="Pantheon RPG résumé système gouvernance">
  </a>
</p>

Pantheon ne remplace pas l’écran ou l’atelier. Il rend leur configuration, leurs sorties, la discipline de preuve, les seuils de validation et la mémoire de décision relisibles.

C’est la différence entre un outillage IA puissant et une méthode de travail professionnelle.

## Le monde extérieur reste ouvert

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/worldmap_ai_internet_01_fr.jpg" width="100%" alt="Pantheon RPG carte IA Internet">
  </a>
</p>

L’IA, le web et les connaissances externes forment des mondes riches mais instables. Connaissances utiles, sources faibles, informations obsolètes, contradictions et découvertes inattendues coexistent.

Pantheon ne ferme pas ce monde. Il donne au professionnel une méthode pour le traverser sans confondre signal, source, preuve et mémoire.

## Ce que Pantheon n’est pas

Pantheon Next n’est pas un chatbot, pas un travailleur IA autonome, pas une mémoire automatique et pas un substitut à la responsabilité professionnelle.

Il ne décide pas seul. Il n’approuve pas ses propres sorties. Il ne transforme pas chaque réponse en vérité.

La frontière technique est :

```text
Pantheon Next cadre et contrôle l’exécution.
Il ne l’exécute pas.
```

## Objets de travail clés

| Objet | Sens ordinaire |
|---|---|
| Task Contract | Une fiche de mission : quoi faire, avec quels documents, sous quelles limites et avec quelle sortie attendue. |
| Evidence Pack | Un dossier de preuve : sources utilisées, hypothèses, risques, contradictions, actions et état de revue. |
| Memory Candidate | Une information qui pourrait être utile plus tard, mais qui doit encore être revue avant d’être gardée. |
| Canonical Memory | Une mémoire validée, bornée et reliée à des preuves. |
| Context Pack | Le minimum de contexte utile envoyé à un travailleur pour une tâche donnée. |
| Pantheon Role | Un angle de revue : planifier, vérifier, contrôler le risque, améliorer la formulation, arbitrer ou préparer une correction. |
| Knowledge Base | Une bibliothèque documentaire. Elle aide à retrouver l’information, mais elle n’est pas une vérité en soi. |
| Approval | Une décision professionnelle visible, pas un clic technique caché dans le système. |

## Rôles Pantheon

Vous n’avez pas besoin de retenir ces noms. Ce sont sept angles de revue utilisés en interne ; le professionnel les voit comme des modes de relecture, pas comme des agents autonomes.

Le fichier [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) conserve son nom historique, mais le concept canonique est **Pantheon Role**.

| Rôle | Fonction simple |
|---|---|
| ATHENA | Organise le problème et prépare le plan. |
| ARGOS | Cherche les sources et vérifie la traçabilité. |
| THEMIS | Vérifie le risque, les règles et les limites d’approbation. |
| APOLLO | Relit la clarté, la complétude et la qualité de livraison. |
| ZEUS | Arbitre lorsque plusieurs options entrent en conflit. |
| IRIS | Reformule, clarifie et prépare la communication côté utilisateur. |
| HEPHAISTOS | Prépare les fichiers techniques, les corrections proposées et les pistes d’implémentation. |

Les profils Hermes peuvent s’aligner sur ces rôles, mais ils restent des profils d’exécution limités. Ils n’approuvent pas, ne canonisent pas et ne promeuvent pas la mémoire.

<details>
<summary>État et structure du projet</summary>

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

</details>

## Et maintenant ?

### Pour le lecteur professionnel

- **Tester la doctrine sur un cas réel** — relire mentalement un dossier récent en se demandant : qu’aurais-je pu cadrer en fiche de mission ? Qu’aurait dû rester candidat ? Qu’est-ce qui n’aurait jamais dû devenir mémoire ?
- **Suivre le projet** — mettre ce dépôt en *Watch* sur GitHub pour suivre l’évolution de la méthode et des cas d’usage documentés.
- **Proposer un cas métier** — ouvrir une *issue* avec un cas réel anonymisé, pour qu’il soit étudié et intégré aux exemples publics.
- **Approfondir la doctrine** — lire [`docs/governance/STATUS.md`](docs/governance/STATUS.md) pour l’état faisant foi, puis [`docs/governance/README.md`](docs/governance/README.md) pour l’ordre de lecture.

### Pour les contributeurs et l’équipe projet

- construire un dossier de démonstration fictif complet ;
- fournir un exemple intégral de Task Contract et d’Evidence Pack ;
- documenter les premiers cas d’usage professionnels par métier ;
- préparer les exemples de handoff OpenWebUI ↔ Hermes.

## Principe final

```text
L’IA produit des possibles.
Pantheon cadre le chemin.
Hermes prépare le travail.
OpenWebUI montre le résultat.
L’humain décide.
Le validé reste.
```
