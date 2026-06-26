# AI Log — Competence model vocabulary

Date: 2026-06-27

## Change

Created `docs/governance/COMPETENCE_MODEL.md` as candidate support doctrine.

Updated:

- `docs/governance/TERMINOLOGY_BOUNDARIES.md` — corrected the former ambiguity where `Competence` was reserved only for human professional skill. The document now distinguishes abstract `Capability`, governed reusable `Competence`, execution-side `Skill`, host `Plugin`, and quantity/load `Capacity`.
- `docs/governance/README.md` — added `COMPETENCE_MODEL.md` to the short read path and core bootstrap path, and expanded the terminology section.
- `docs/governance/AUTHORITY_INDEX.md` — indexed `COMPETENCE_MODEL.md` as `candidate support doctrine`, repo state `documented non-implemented`, and expanded the terminology preferred list.

## Model captured

The new vocabulary separates:

```text
Connaissance
Guide de compétence
Ressource de compétence
Compétence
Skill Hermes
Tool / Connector
Template
Evidence
Action
Gate
```

Core rule:

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

## Examples included

- filling PDFs with or without fields;
- API querying;
- d3.js / three.js diagrams;
- taxable surface calculation;
- architecture-practice anti-errors.

## Boundary

Documentation only.

No runtime, competence engine, skill generator, repository generator, retrieval system, API client, PDF filler, OCR pipeline, d3.js/three.js generator, web search engine, template renderer, approval engine, memory engine, OpenWebUI Function, OpenWebUI Tool, OpenWebUI Pipe, OpenWebUI Action, Hermes skill or external connector was implemented.

No protected paths were modified.

## Repo state

Documented non-implemented.

## Follow-up

- Reconcile `GOVERNED_FORM_FILLING.md` and `SKILL_LIFECYCLE.md` wording with the new competence model.
- Decide whether `Compétence` becomes the preferred UX/public label while `Capability` remains the kernel abstraction.
- Formalize `Competence Card` inside a future `CARD_STACK_MODEL.md`.
- Decide whether Hermes skill creation from guides/resources requires a dedicated Competence-to-Skill Gate.
