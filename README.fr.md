# Pantheon Next

> English version: [README.md](README.md)

> **Une méthode de contrôle pour les dossiers professionnels : ce qui entre, ce qui est transmis, ce qui sort et ce qui reste.**

<sub><strong>État actuel :</strong> Pantheon Next est un référentiel de méthode et de documentation en cours de structuration. Il est cohérent, mais partiel. Pour l’état d’implémentation faisant foi, lire <a href="docs/governance/STATUS.md">docs/governance/STATUS.md</a>.</sub>

Pantheon Next garde visible et revisable ce qui engage votre responsabilité — sources, décisions, ce qui sort de votre cabinet, ce que vous conservez — du premier brouillon à votre signature.

Quand un outil d’IA entre dans le flux, il reste un outil. Vous restez responsable.

**Un exemple.** Un devis de reprise appelle un mail au client. La plupart des assistants vous renvoient un message poli qui dit *oui* — et vous engage au passage. Pantheon s’arrête sur la question qui compte : *ce mail valide-t-il, accepte-t-il, approuve-t-il un périmètre ou vous engage-t-il à l’externe ?* Si c’est incertain, il suspend la transmission et pose les options — une clarification neutre, une note interne, ou attendre une source manquante. Rien ne vous engage par accident.

## Pour qui

Les professionnels qui répondent de ce qu’ils envoient : architectes, avocats, médecins, experts-comptables, ingénieurs, consultants. Métiers régulés, responsabilité réelle, aucune place pour une réponse sûre d’elle qui se révèle fausse.

Aucune compétence technique requise. Vous gardez le contrôle des sources, des décisions et des signatures.

## Ce que vous y gagnez

- **Rien ne sort par accident.** Chaque sortie porte un statut. La transmission est une décision, pas un effet de bord.
- **Une traçabilité prête pour l’audit.** Sources, hypothèses, contradictions et approbations restent visibles et revisables.
- **Une mémoire fiable.** Seule une information validée, bornée et reliée à des preuves est conservée.

## Comment circule un dossier

<p align="center">
  <a href="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg">
    <img src="docs/assets/pantheon-rpg/references/before_after_01_fr.jpg" width="100%" alt="Avant et après : une réponse brute devient un chemin de dossier maîtrisé">
  </a>
</p>

<p align="center"><strong>Avant et après.</strong><br><em>Une réponse brute est rapide. Pantheon transforme le travail en un chemin de dossier visible.</em></p>

La vitesse est facile. Le contrôle est la partie difficile. Pantheon ajoute le chemin dont a besoin un travail à responsabilité :

```text
demande
→ fiche de mission
→ sélection des sources et du périmètre
→ contexte minimal nécessaire
→ travail candidat
→ dossier de preuve
→ revue
→ décision humaine
→ mémoire bornée optionnelle
```

Il n’expose jamais tout le dossier. Il prépare le minimum de contexte nécessaire — assez pour travailler, pas assez pour tout exposer. Quatre portes cadrent le flux :

| Porte | Question |
|---|---|
| Entrée | Quelles sources, documents ou faits peuvent entrer dans le périmètre de travail ? |
| Contexte | Quel est le plus petit contexte suffisant pour cette tâche ? |
| Sortie | Que peut-on produire, sous quel statut et pour quel destinataire ? |
| Mémoire | Que peut-il rester, sous quel périmètre, avec quelle preuve et quelle approbation ? |

Une carte interactive montre comment les pièces se connectent — l’écran, l’atelier, la méthode, les moteurs, les documents et la mémoire : [ouvrir la carte interactive](docs/assets/pantheon-map/pantheon_next_mindmap_d3_v3_animated.html). (GitHub ne l’affiche pas en ligne ; ouvrez-la par le lien.)

## Six distinctions honnêtes

Toute la méthode tient en six lignes :

```text
Réponse fluide   ≠ réponse sûre.
Source trouvée   ≠ preuve.
Brouillon        ≠ livrable.
Envoyé           ≠ vrai.
Fait répété      ≠ mémoire.
Accord des rôles ≠ approbation.
```

L’outil propose. Le professionnel valide, rejette ou demande une révision. Pantheon garde revisable le chemin entre les deux, et demande une décision humaine quand le risque dépasse l’arbitrage sûr.

## Cloud ou local : votre choix

Pantheon ne vous enferme pas dans un moteur unique. Utilisez un service externe comme ChatGPT, Claude ou Gemini, avec les noms privés, adresses, références clients ou extraits sensibles masqués ou minimisés avant tout envoi. Ou faites tourner un modèle local sur votre propre matériel pour plus de confinement, au prix de la maintenance et de la discipline.

Dans les deux cas : le moteur ne reçoit que le contexte nécessaire, Pantheon cadre la méthode, et le professionnel valide.

## Sur des dossiers réels

Les exemples sont fictifs et pédagogiques. Ils ne remplacent pas un avis professionnel.

1. [`architecture_devis_reprise/`](docs/examples/architecture_devis_reprise/) — devis de reprise et validation client dangereuse.
2. [`architecture_legal_module_panel/`](docs/examples/architecture_legal_module_panel/) — futur panneau cockpit architecture + juridique, rôles actifs, blocages et éligibilité des skills.
3. [`regulatory_watch_conflict/`](docs/examples/regulatory_watch_conflict/) — nouvelle règle externe contre hypothèses d’un dossier actif.
4. [`evidence_topology/`](docs/examples/evidence_topology/) — exemples de topologie de contexte, extraction parallèle, transmission et Dossier de preuve.
5. [`understand_anything_structural_analysis/`](docs/examples/understand_anything_structural_analysis/) — analyse graphe externe cadrée comme preuve candidate, pas comme autorité.
6. [`legal_note/`](docs/examples/legal_note/) — note de stratégie juridique avec besoins de vérification des sources.
7. [`medical_letter/`](docs/examples/medical_letter/) — courrier d’adressage avec exposition de données minimisée.

Le but n’est pas que Pantheon décide. Le but est que le chemin de décision reste revisable.

<details>
<summary>Sous le capot (vocabulaire, rôles, architecture)</summary>

### Trois parties

| Élément | Rôle dans le dossier |
|---|---|
| **OpenWebUI (l’écran)** | L’endroit visible : demander, lire, sélectionner des documents, voir les sources, valider. |
| **Hermes Agent (l’atelier)** | L’endroit de préparation : chercher, extraire, comparer, convertir, rédiger, produire des candidats. |
| **Pantheon Next (la méthode)** | Le cadre : ce qui entre, le contexte minimal nécessaire, ce qui sort, ce qui reste. |

La doctrine interne :

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

### Sept regards, une décision humaine

Pas besoin de retenir ces noms. Ce sont des regards de revue internes, pas des agents autonomes.

| Rôle | Fonction en clair |
|---|---|
| ATHENA | Organise le problème et prépare le plan. |
| ARGOS | Cherche les sources et vérifie la traçabilité. |
| THEMIS | Vérifie le risque, les règles et les limites d’approbation. |
| APOLLO | Revoit la clarté, la complétude et la qualité de livraison. |
| ZEUS | Arbitre le statut et la procédure suivante quand les options s’opposent. |
| IRIS | Reformule, clarifie et prépare la communication vers l’utilisateur. |
| HEPHAISTOS | Prépare les fichiers, les candidats de correction et les chemins d’implémentation. |

Ces regards peuvent exposer un désaccord utile avant que le professionnel ne valide quoi que ce soit. Les profils Hermes peuvent s’y aligner, mais restent des profils d’exécution limités : ils n’approuvent pas, ne canonisent pas, ne promeuvent pas la mémoire. Voir [`docs/governance/GOVERNANCE_COLLEGE.md`](docs/governance/GOVERNANCE_COLLEGE.md) et [`docs/governance/USER_DECISION_GATE.md`](docs/governance/USER_DECISION_GATE.md).

### Mémoire compartimentée

Pantheon n’utilise pas un seul bac à vérité.

```text
Source brute      matière qui existe
Connaissance      matière de référence organisée
Contexte          information utile pour une tâche
Preuve            appui sélectionné pour une affirmation ou une sortie
Candidat mémoire  information proposée à la conservation
Mémoire canonique mémoire approuvée, avec périmètre et preuve
Doctrine          la couche des règles
État d’exécution  état d’exécution externe, jamais mémoire validée
```

### Le vocabulaire en clair

| Objet | Sens en clair |
|---|---|
| Contrat de tâche | Une fiche de mission : quoi faire, avec quels documents, sous quelles limites et avec quelle sortie attendue. |
| Pack de contexte | Le contexte minimal nécessaire transmis à un exécutant pour une tâche précise. |
| Dossier de preuve | Un dossier de preuves : sources utilisées, hypothèses, risques, contradictions, actions et état de revue. |
| Candidat mémoire | Quelque chose qui peut servir plus tard, mais qui doit être revu avant d’être conservé. |
| Mémoire canonique | Mémoire validée, bornée et reliée à des preuves. |
| Rôle Pantheon | Un angle de revue : planifier, vérifier, contrôler le risque, améliorer la formulation, arbitrer ou préparer une correction. |
| Base de connaissances | Une bibliothèque de documents. Elle aide à trouver, mais n’est pas la vérité en soi. |
| Approbation | Une décision professionnelle visible, pas un clic technique caché. |

### Ce que Pantheon n’est pas

Pantheon Next n’est pas un chatbot, pas un travailleur autonome, pas une mémoire automatique, et pas un substitut à la responsabilité professionnelle. Il ne décide pas seul, n’approuve pas ses propres sorties et ne transforme pas chaque réponse en vérité.

```text
Pantheon Next cadre et contrôle l’exécution.
Il n’exécute pas.
```

</details>

<details>
<summary>État et structure du projet</summary>

Pantheon Next fournit actuellement une base de gouvernance au niveau documentaire.

Implémenté ou documenté :

- doctrine de gouvernance ;
- doctrine de frontière d’exécution ;
- registre des Rôles Pantheon ;
- doctrine du Collège de gouvernance ;
- doctrine des Rites ;
- doctrine de la Porte de décision utilisateur ;
- doctrine du Contrat de tâche ;
- doctrine du Dossier de preuve ;
- doctrine d’approbation ;
- doctrine de mémoire ;
- politique des outils externes ;
- doctrine d’intégration OpenWebUI ;
- doctrine d’intégration Hermes ;
- taxonomie de connaissance et cadrage de périmètre ;
- doctrine RAG d’ingestion et de frontière de preuve ;
- revues et frontières des références externes ;
- récits et ressources visuelles ;
- gabarits légers de profils Hermes ;
- baseline déclarative de schémas réconciliée ;
- premier test de validation de schémas en lecture seule.

Non implémenté dans ce projet :

- runtime autonome ;
- intégration runtime OpenWebUI ;
- intégration runtime Hermes ;
- génération automatique de Dossier de preuve ;
- interface de revue des Candidats mémoire ;
- routage de fournisseurs d’IA ;
- gestionnaire de plugins libre ;
- suite large de tests et couverture CI ;
- outillage d’opérations en lecture seule ;
- pile de déploiement.

Structure :

```text
docs/governance/     doctrine de gouvernance et documents de statut
docs/examples/       exemples professionnels fictifs
hermes/profiles/     gabarits de profils Hermes candidats seulement
docs/assets/         références narratives et visuelles
ai_logs/             historique des interventions assistées par IA
legacy/              matériel source historique de Pantheon OS
schemas/             contrats déclaratifs réconciliés, pas un runtime
operations/          outillage en lecture seule attendu, pas encore implémenté
tests/               premier test de schémas en lecture seule présent ; couverture plus large en attente
```

Points d’entrée clés :

| Document | Objet |
|---|---|
| [`docs/governance/STATUS.md`](docs/governance/STATUS.md) | Statut faisant foi du projet. |
| [`docs/governance/README.md`](docs/governance/README.md) | Index de gouvernance et ordre de lecture. |
| [`docs/governance/EDITORIAL_LANGUAGE.md`](docs/governance/EDITORIAL_LANGUAGE.md) | Guide du langage public et du vocabulaire. |
| [`docs/examples/README.md`](docs/examples/README.md) | Index des exemples professionnels. |
| [`docs/governance/AGENTS.md`](docs/governance/AGENTS.md) | Registre canonique des Rôles Pantheon. |
| [`docs/governance/GOVERNANCE_COLLEGE.md`](docs/governance/GOVERNANCE_COLLEGE.md) | Séparation des rôles, tensions utiles et arbitrage procédural. |
| [`docs/governance/USER_DECISION_GATE.md`](docs/governance/USER_DECISION_GATE.md) | Escalade vers décision humaine quand le désaccord dépasse l’arbitrage sûr. |
| [`docs/governance/TASK_CONTRACTS.md`](docs/governance/TASK_CONTRACTS.md) | Doctrine de cadrage de tâche. |
| [`docs/governance/EVIDENCE_PACK.md`](docs/governance/EVIDENCE_PACK.md) | Doctrine de preuve. |
| [`docs/governance/MEMORY.md`](docs/governance/MEMORY.md) | Doctrine de promotion mémoire. |
| [`docs/governance/APPROVALS.md`](docs/governance/APPROVALS.md) | Niveaux d’approbation. |
| [`docs/governance/HERMES_INTEGRATION.md`](docs/governance/HERMES_INTEGRATION.md) | Doctrine de frontière Hermes. |
| [`docs/governance/OPENWEBUI_INTEGRATION.md`](docs/governance/OPENWEBUI_INTEGRATION.md) | Doctrine de frontière OpenWebUI. |
| [`docs/governance/KNOWLEDGE_TAXONOMY.md`](docs/governance/KNOWLEDGE_TAXONOMY.md) | Vocabulaire source, connaissance, contexte, preuve et mémoire. |
| [`docs/governance/RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md`](docs/governance/RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md) | Doctrine RAG d’ingestion, retrieval et frontière de preuve. |

En cas de désaccord entre documents, traiter `STATUS.md` comme première référence de statut jusqu’à réconciliation.

</details>

## En une formule

```text
Pantheon cadre le flux.
Le moteur ne reçoit que le contexte nécessaire.
Hermes prépare les candidats.
OpenWebUI montre le résultat.
L’humain décide.
Seul le validé reste.
```
