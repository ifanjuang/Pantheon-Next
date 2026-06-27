# Card Stack Knowledge Corpus Alignment

Status: candidate support note — card-stack terminology alignment for Connaissance as non-project documentary corpus.

This document is not canonical doctrine yet.

It does not implement a UI, dashboard, search engine, RAG pipeline, document ingestion engine, vector database, OCR pipeline, knowledge registry, evidence engine, memory engine, approval engine, OpenWebUI plugin, Hermes skill, connector or external action.

It reconciles `CARD_STACK_MODEL.md` with the intended meaning of `Connaissance` in the cockpit card deck.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The card-stack vocabulary must avoid confusing:

```text
project material;
source material;
evidence;
context;
validated memory;
professional documentary knowledge;
competence resources;
```

The term `Connaissance` should be reserved for the documentary corpus outside a specific project.

Examples:

```text
PLU / urbanism documents;
MAF recommendations;
CCTP guides;
professional lexicons;
agency doctrine;
regulatory notes;
insurance notes;
method guides;
technical reference dossiers;
standard details;
reference checklists;
professional doctrine distilled from reliable sources.
```

## Core correction

In the card stack:

```text
Connaissance = non-project documentary corpus, qualified or structured for professional reuse.
```

It is not:

```text
a project file;
a project-specific fact;
a raw source attached to one dossier;
a proof by itself;
a canonical memory;
a competence;
a template;
an action;
```

## Clean separation

| Object | Meaning | Example | Project-owned by default? |
|---|---|---|---|
| Document / Source | Raw or retrieved material. | PDF, mail, plan, photo, notice, PLU file, MAF PDF. | It depends on source. |
| Connaissance | Qualified documentary corpus outside projects. | PLU rule note, MAF recommendation digest, CCTP guide, lexicon. | No. |
| Context | Current project situation. | Phase APD, mission DET, commune, client, lot. | Yes. |
| Evidence | A source selected to support an assertion. | PLU article supporting a facade-material claim. | Scoped to assertion/project/subject. |
| Memory Candidate | Fact proposed for future retention. | “For project X, facade material A was rejected.” | Yes, until promoted. |
| Register Entry | Validated memory / proof register entry. | Human-validated scoped claim. | Scoped. |
| Competence | Reusable ability. | “Read a PLU and extract facade constraints.” | No. |
| Guide / Resource de competence | Material used to learn or operate a competence. | Tutorial, checklist, example file. | No. |
| Template | Reusable output structure. | Mail response, CR chantier, CCTP article skeleton. | No. |

## Working rule

```text
A project can use a Connaissance.
A Connaissance does not become project-owned because it was used.
A project-specific extraction from a Connaissance becomes Evidence, Context or Memory Candidate depending on its role.
```

Example:

```text
PLU of Rouen as documentary corpus -> Connaissance Card.
Article used to check a facade choice for project Poussin -> Evidence Card scoped to Poussin / facade.
Decision “zinc accepted for this project” -> Memory Candidate / Register after gate.
Ability “check PLU facade materials” -> Competence Card.
```

## Deck implications

### Documents / Sources Scene

This scene may show raw files or retrieved sources, including project documents and non-project documents.

Examples:

```text
uploaded CR chantier;
photo chantier;
client email;
CCTP project file;
PLU PDF;
MAF recommendation PDF;
lexicon page;
agency guide;
```

A raw document is not yet a Connaissance merely because it exists.

### Connaissances Scene

The Connaissances scene should be a documentary corpus scene, not a project working scene.

Candidate horizontal families:

```text
Urbanisme / PLU;
Assurance / MAF;
CCTP / marchés;
Réglementation;
Construction / chantier;
Lexiques;
Agence / doctrine interne;
Méthodes professionnelles;
Références techniques;
```

Candidate vertical order:

```text
Validated / accepted knowledge;
Candidate knowledge;
To verify;
Obsolete / superseded;
Gaps / needed knowledge;
Blank knowledge card;
```

### Workflow Scene

A Workflow Scene may include `Connaissances used` only when the treatment actually relies on the documentary corpus.

Do not include all relevant-looking knowledge by default.

### Evidence Scene

When a Connaissance supports a project assertion, it appears through an Evidence Card.

The Evidence Card must keep scope visible:

```text
Project:
Subject:
Assertion:
Connaissance used:
Source excerpt:
Status:
Freshness:
Gate:
```

### Competence Scene

A competence may use Connaissances, guides and resources.

But:

```text
Connaissance = professional content.
Competence = reusable ability.
Guide / Resource = support for operating or learning a competence.
```

A MAF recommendation digest is Connaissance.

A procedure for applying the MAF recommendation in a client email is a Competence or Template, depending on form.

## Connaissance Card

### Recto — five-second reading

```text
Title:
Family: PLU | MAF | CCTP | Lexique | Réglementation | Agence | Technique
Authority: official | professional | agency | external | candidate
Status: accepted | candidate | to_verify | obsolete | refused
Scope: non-project corpus
Freshness:
One-line use:
```

Examples:

```text
PLU Rouen — zones UB facade rules
Urbanisme / PLU · official · to_verify
Scope: non-project corpus
Use: facade material constraints for Rouen projects.
```

```text
MAF — limites de mission / responsabilité
Assurance / MAF · professional · candidate
Scope: non-project corpus
Use: wording guardrail for client / enterprise replies.
```

### Verso — detailed card

```text
source_document:
source_type:
authority_class:
version_or_date:
freshness_status:
content_summary:
usable_claims:
limitations:
related_competences:
related_templates:
related_evidence_cards:
related_projects_using_it:
review_status:
next_review_date:
```

## Relationship with project documents

Project-specific documents should not be reclassified as Connaissance by default.

Examples:

| Project item | Better card type |
|---|---|
| Client email | Document / Source Card |
| Uploaded photo | Document / Source Card |
| Previous CR for this chantier | Document / Source Card + Trace / Memory if validated |
| Project CCTP | Document / Source Card; Evidence when supporting claim |
| Project PLU excerpt used for a decision | Evidence Card scoped to project |
| Decision made from PLU | Memory Candidate / Register after gate |

## Relationship with external documentary corpus

External documentary corpus may become Connaissance when it is:

```text
qualified;
structured;
scope-marked;
authority-classed;
freshness-marked;
usable across projects;
not merely attached to one project;
```

Examples:

```text
PLU family summary;
MAF wording caution note;
CCTP article guide;
terminology lexicon;
ERP classification reference;
fire-safety reminder note;
agency standard detail commentary;
```

## Relationship with Evidence

Connaissance is not proof by itself.

A Connaissance becomes part of evidence only when it supports a scoped assertion.

```text
Connaissance Card -> used by Evidence Card -> supports Assertion -> may affect Gate.
```

## Relationship with Memory

Connaissance is reusable documentary material.

Memory is what was validated or decided in a specific scope.

Do not use Connaissance as a bypass around memory gates.

## Relationship with Templates

A template structures output.

A Connaissance informs content.

Example:

```text
Template: mail response hors mission.
Connaissance: MAF recommendation on responsibility boundary.
Evidence: specific mission contract clause for current project.
Gate: user approval before sending.
```

## Anti-patterns

```text
Do not classify every project note as Connaissance.
Do not let project-specific facts pollute the general knowledge corpus.
Do not treat PLU / MAF / CCTP guides as automatically current.
Do not treat Connaissance as Evidence without scoped assertion.
Do not treat Connaissance as canonical memory.
Do not let Connaissance become a competence.
Do not let competence resources become Connaissance unless they contain professional content.
```

## Final rule

```text
Documents are sources.
Connaissances are reusable documentary corpus outside projects.
Evidence is scoped support for an assertion.
Memory is validated retention.
Competence is reusable ability.
Template is reusable structure.
Gate is decision threshold.
The human decides.
```
