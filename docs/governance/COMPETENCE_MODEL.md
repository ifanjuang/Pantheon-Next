# Competence Model

Status: candidate support doctrine — governed competence vocabulary, source separation and execution projection model.

Runtime status: non-executable.

This document defines how Pantheon Next distinguishes professional knowledge, competence guides, competence resources, templates, runtime skills, tools, evidence, actions and gates.

It does not implement a runtime, competence engine, skill generator, repository generator, retrieval system, API client, PDF filler, OCR pipeline, d3.js/three.js generator, web search engine, template renderer, approval engine, memory engine, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Action, Hermes skill or external connector.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon needs a vocabulary that supports practical professional work without confusing:

```text
what is known;
how to do something;
what documentation teaches the doing;
what form is reused;
what is produced;
what is proved;
what is allowed.
```

The practical user-facing distinction is:

```text
La compétence sait faire.
La connaissance sait quoi mettre.
Le guide explique comment faire.
La ressource aide à faire.
Le template donne la forme.
L'Evidence justifie une valeur ou une assertion.
L'action produit.
Le Gate autorise ou bloque.
```

## Core vocabulary

### Connaissance

A Connaissance is professional, regulatory, contractual, project or dossier knowledge.

It informs the professional decision or supplies the content to be used in a task.

Examples:

```text
PLU
DTU
CCTP
CCAP
programme client
historique projet
pièces dossier
règlement ERP
surface taxable calculée
surface de plancher
référence cadastrale
montant marché
date de réception
doctrine agence validée
retour d'expérience validé
```

A Connaissance may support an Evidence item when selected for a specific assertion, value, decision or output with traceability.

A Connaissance is not a skill, guide, tool or template.

### Guide de compétence

A Guide de compétence explains a method for applying or learning a competence.

Examples:

```text
guide de remplissage PDF plat
guide OCR préalable
guide interrogation API
guide lecture documentation API
guide schéma d3.js
guide calcul surface taxable
guide réponse client prudente
guide extraction plan PDF
```

A Guide de compétence can live inside a competence folder.

Its location does not make it a Connaissance métier, Evidence or approved method.

### Ressource de compétence

A Ressource de compétence is material used by a competence.

It may be linked, embedded, mirrored, snapshotted, distilled or generated from examples.

Examples:

```text
documentation API
wiki d'outil
manuel PDF
lien vers une documentation officielle
exemple de formulaire
image test
PDF test
snippet
jeu de données
exemple de requête JSON
exemple de graphe d3.js
snapshot Markdown daté
distillation d'une documentation technique
```

A Ressource de compétence may explain or support execution.

It does not prove a professional claim by itself.

### Compétence

A Compétence is a governed reusable ability to do something under explicit boundaries.

It is tool-agnostic at the Pantheon level.

Examples:

```text
remplir un PDF avec ou sans champs
remplir un PDF scanné après OCR
interroger une API
produire un schéma d3.js ou three.js
faire une recherche internet sourcée
calculer une surface taxable
calculer une surface de plancher
vérifier un devis contre CCTP
préparer un visa EXE
rédiger une réponse client prudente
créer une chronologie probatoire
préparer un dossier de preuve
créer une compétence depuis une documentation
```

A Compétence may use:

```text
Connaissances
Guides de compétence
Ressources de compétence
Templates
Tools / Connectors
Hermes Skills
```

A Compétence produces candidates, not final truth, approval, memory or external action.

### Skill Hermes

A Skill Hermes is an execution-side projection of a Compétence.

It may operationalize a competence for Hermes or another external runtime.

A Hermes Skill is not Pantheon doctrine.

A Hermes Skill may produce:

```text
Result Candidate
Evidence Pack Candidate
Action Candidate
Capability Gap
Risk Escalation
Trace reference
```

It must not produce:

```text
validated truth
final approval
external-action authorization
Registre Probatoire entry
canonical memory
doctrine mutation
```

### Tool / Connector

A Tool or Connector is the actual means used to act, query, convert, render, extract, fill or search.

Examples:

```text
PDF library
OCR engine
API client
web browser
search provider
d3.js
three.js
Gmail connector
Drive connector
cadastre API
SIRENE API
```

Availability does not mean authorization.

### Template

A Template is a reusable form for producing something.

Examples:

```text
tableau de calcul surface taxable
mapping de champs CERFA
mail client prudent
fiche réserve chantier
fiche visa EXE
tableau comparatif devis
note analyse PLU
fiche Evidence
Gate Zeus
schéma d3.js
page HTML cockpit
rapport de synthèse
```

A Template structures a candidate output.

It does not validate its content.

### Evidence

Evidence is the reviewable support for an assertion or value in a specific case.

Examples:

```text
surface taxable candidate = 42,30 m² with calculation table and plan source
parcelle candidate = AB 123 with cadastre source
mail client received on a date
CCTP clause supporting a reserve
source PLU dated and scoped to the project zone
```

Evidence may be candidate, partial, contradicted, validated, obsolete or blocked.

### Action

An Action is a concrete produced or prepared effect.

Examples:

```text
PDF rempli candidat
mail candidat
note candidate
tableau candidat
schéma candidat
formulaire prérempli
requête API testée
fichier classé candidat
```

An Action may be internal, candidate-only or external-effect-bearing.

External-effect-bearing actions require approval when consequential.

### Gate

A Gate exposes the decision status.

It answers:

```text
Can this be used?
Can this be sent?
Can this be filed?
Can this be remembered?
Can this be treated as source-backed?
Must a human decide?
```

A Gate may authorize only a status or next procedure. It is not an execution engine.

## Boundary rules

### 1. Competence is not knowledge

```text
Remplir un PDF = Compétence.
Savoir quoi mettre dans le PDF = Connaissance.
La valeur du champ sensible = Evidence candidate.
Le PDF rempli = Action candidate.
La transmission = Gate / approval.
```

### 2. Documentation of a tool is not métier knowledge

A documentation API, d3.js guide, OCR manual, PDF library guide or internal wiki about how to operate a tool is not a Connaissance métier.

It is a Guide or Ressource de compétence.

### 3. A competence folder may contain documentation

A competence folder may contain:

```text
guides/
ressources/
templates/
examples/
procedures/
gates.md
```

But folder location does not change status.

A file inside `competences/.../ressources/` remains a Ressource de compétence, not Evidence or métier knowledge.

### 4. A template protects form, not truth

A good template may reduce risk.

It does not make a candidate output true, validated, deliverable or transmissible.

### 5. A calculated value is Evidence, not just data

Values that affect professional output must be treated as Evidence candidates when used.

Examples:

```text
surface taxable
surface de plancher
emprise au sol
classement ERP
effectif ERP
montant marché
délai
référence cadastrale
```

### 6. A skill executes only as projection

Pantheon may govern a Compétence.

Hermes may execute a Skill that projects the competence.

The execution remains outside Pantheon.

## Competence lifecycle

Recommended lifecycle:

```text
observed_need
reference_collected
competence_candidate
reviewed_candidate
sandbox_enabled
task_authorized
project_enabled
agency_enabled
suspended
rejected
obsolete
```

Interpretation:

| Status | Meaning |
|---|---|
| `observed_need` | recurring need or gap identified |
| `reference_collected` | guides/resources gathered, not distilled |
| `competence_candidate` | method drafted, not trusted |
| `reviewed_candidate` | reviewed for scope, risks and boundaries |
| `sandbox_enabled` | usable in tests only |
| `task_authorized` | allowed for a bounded Task Contract |
| `project_enabled` | allowed within a project/dossier scope |
| `agency_enabled` | accepted as agency-level competence |
| `suspended` | temporarily blocked |
| `rejected` | refused or out of scope |
| `obsolete` | superseded by a newer competence or method |

Activation is not execution.

Execution still requires the external runtime, tool or connector to be available and task-authorized.

## Competence card minimum fields

```text
competence_card:
  title:
  purpose:
  scope:
  status:
  not_for:
  inputs:
  outputs:
  required_connaissances:
  guides:
  ressources:
  templates:
  tools_or_connectors:
  possible_runtime_projection:
  risk_triggers:
  evidence_expectations:
  approval_ceiling:
  memory_impact:
  external_effect:
  test_cases:
  fallback:
  zeus_status:
  trace_refs:
```

## Guides and resources inside competence folders

Recommended folder structure:

```text
competences/
  competence-name/
    COMPETENCE.md
    guides/
    ressources/
      liens/
      fichiers/
      snapshots/
      distillations/
    templates/
    examples/
    gates.md
```

Allowed resource states:

```text
linked
embedded
mirrored
snapshotted
distilled
generated_example
```

Recommended resource manifest:

```text
resource:
  title:
  type: api_doc | wiki | guide | library_doc | tool_manual | example | dataset | snippet | file | link | snapshot | distillation
  source:
  version:
  retrieved_at:
  license:
  scope:
  status: active | candidate | stale | obsolete | linked_only
  used_by_competence:
  not_authoritative_for:
  update_policy:
```

A Markdown file may be:

```text
reference index
resource manifest
distillation
procedure
template
example
```

It is not automatically the source of truth.

## Example — PDF filling

```text
Compétence:
Remplir un PDF.

Guides:
Détecter les champs PDF.
Remplir un PDF plat.
Demander OCR préalable.
Remplir en surimpression.

Ressources:
Documentation outil PDF.
Guide AcroForm.
PDF exemple.
Image scan exemple.

Connaissances:
Nom du demandeur.
Adresse du terrain.
Référence cadastrale.
Surface taxable.
Surface de plancher.
Destination du projet.

Template:
Mapping de champs CERFA.

Evidence:
Surface taxable candidate = 42,30 m², source tableau de calcul.

Action:
PDF rempli candidat.

Gate:
Validation humaine requise avant dépôt ou transmission.
```

## Example — API query

```text
Compétence:
Interroger une API.

Guides:
Construire une requête.
Tester l'appel.
Gérer erreurs, pagination, auth, quotas.
Vérifier provenance et fraîcheur.

Ressources:
Documentation API.
Exemple endpoint.
Exemple réponse JSON.

Connaissances:
Adresse, SIRET, parcelle ou autre donnée métier utilisée comme entrée.

Template:
Fiche résultat API.

Evidence:
Résultat API candidat, daté, avec endpoint et paramètres.

Action:
Note ou tableau candidat.

Gate:
Usable for review only until source/state is checked when consequential.
```

## Example — d3.js / three.js diagram

```text
Compétence:
Produire un schéma interactif.

Guides:
Guide graphe d3.js.
Guide scène three.js.
Guide lisibilité mobile.

Ressources:
Documentation d3.js.
Documentation three.js.
Exemples de graphes.
Snippets.

Connaissances:
Cartes, statuts, liens, risques, Evidence, Gates à représenter.

Template:
Constellation de cartes.
Timeline.
Graphe de dépendances.

Evidence:
The displayed data points and links are source-backed or candidate-labeled.

Action:
HTML/SVG/JS candidate.

Gate:
Pedagogical unless linked sources and evidence status are visible.
```

## Example — surface taxable

```text
Compétence:
Calculer une surface taxable.

Connaissances:
Règles fiscales applicables.
Projet.
Plans.
Niveaux.
Surfaces closes et couvertes.
Hauteurs.
Déductions.
Cas particuliers.

Guides:
Méthode de calcul par niveau.
Distinction surface taxable / surface de plancher / emprise.
Méthode de restitution.

Templates:
Tableau de calcul.
Note de contrôle.

Evidence:
Surface taxable candidate.

Action:
Note, tableau ou champ CERFA.

Gate:
Validation humaine before filing, declaration or external transmission.
```

## Architecture-practice anti-errors

```text
filled does not mean validated;
clear does not mean verified;
calculated does not mean approved;
retrieved does not mean evidence;
template-protected does not mean safe to send;
project-specific does not mean agency-general;
Hermes done does not mean Pantheon validated.
```

## Relationship to existing doctrine

This model complements:

```text
CAPABILITY_PLACEMENT.md
MODULAR_DOMAIN_REORIENTATION.md
DOMAIN_PACK_SPEC.md
SKILL_LIFECYCLE.md
CONTEXT_STACK.md
TASK_CONTRACTS.md
EVIDENCE_PACK.md
USER_DECISION_GATE.md
TERMINOLOGY_BOUNDARIES.md
```

It does not replace Capability Placement.

It refines the vocabulary for the class of governed reusable abilities that may be projected into runtime skills, tools, connectors, templates or cockpit cards.

## Open questions

```text
Should `Compétence` become the preferred public/UX label while `Capability` remains the kernel abstraction?
Should competence folder structure be standardized under `templates/` before any actual competence directory is created?
Should `Competence Card` be formalized inside CARD_STACK_MODEL.md later?
Should Hermes skill creation from guides/resources require a dedicated Competence-to-Skill Gate?
```
