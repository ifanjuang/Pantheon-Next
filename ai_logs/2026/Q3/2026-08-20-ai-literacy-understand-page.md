# AI literacy / Pantheon explainer page

Date: 2026-08-20

## Objective

Add one public pedagogical projection explaining modern AI concepts and their placement in Pantheon without creating new doctrine, runtime responsibility, memory ownership or binding adoption.

## Repository state checked first

- `main` at `b5a39b510968ce35e48a899b4148bdfc88a71e03`;
- recent document/Markdown convergence from #678 included in `main`;
- open landing PR #676 still owns `docs/index.html` and `docs/index-en.html`;
- open #679 records a newer SourceDown / Docling qualification checkpoint without changing public landing files;
- existing public `rag-probatoire.html`, `manifeste.html` / `manifesto.html`, landing pages and public map/prototype surfaces reviewed for overlap.

## Scope

Added only:

- `docs/comprendre.html`;
- `docs/understand.html`;
- `docs/assets/understand.css`;
- this intervention log.

The landing pages are deliberately not changed while #676 modifies them in parallel.

## Editorial model

The page uses a progressive first-read structure:

```text
Savoir / Know
-> Organiser / Organize
-> Agir / Act
-> Compter / Count
```

It explains the common AI mechanisms first, then maps them into Pantheon responsibilities.

First-read language uses functions rather than product bindings:

- model;
- context;
- RAG;
- memory;
- executor;
- tools / skills / agent / run / workflow;
- mission frame;
- provenance;
- Evidence;
- Registre Probatoire / Probative Register;
- human decision.

Concrete technologies appear only in a separate candidate section.

## Candidate posture preserved

The public page records:

- Hermes Agent as a replaceable candidate for the external executor role;
- Obsidian as a qualified candidate workspace around local Markdown notes;
- Hindsight as the first qualified bounded associative working-memory candidate;
- TencentDB Agent Memory as evaluated and currently deferred for the tested topology;
- Docling as the preferred document-structural-analysis candidate, with runtime integration still a separate qualification fact.

No candidate is described as a mandatory Pantheon dependency.

## Memory and document explanation

The page explains three working-memory spaces without exposing private workspace names or project identities:

```text
Agence / Agency
Projets / Projects
Sandbox
```

It also explains:

- strict project/context/source classification;
- source-linked chunking;
- document and Markdown versioning;
- Markdown as portable plain text rather than source replacement;
- source -> structured derivative -> chunks as a working path;
- the distinction between working recall and qualified Registre Probatoire material in prose rather than repeated non-equivalence notation.

## Privacy rule for public examples

No real project, client, address, agency or personal name is used.

Synthetic dossiers use a pronounceable three-letter code plus an attached number, e.g. `LIA21`, `SOL14`.

Synthetic people use civil title plus one initial, e.g. `Mme. C`, `Mr. H`.

## Local / cloud posture

The page explains that the architecture can be operated fully locally when selected components support it: documents, Markdown notes, extraction, retrieval, memory, databases and models may remain private/local. Cloud and hybrid capabilities remain explicit optional choices; the page does not claim that every Pantheon deployment is inherently offline.

## Subpage review

- `docs/rag-probatoire.html`: compatible with the new explanatory page; no real project names found in the reviewed public example text; retained as the deeper RAG page.
- `docs/manifeste.html` / `docs/manifesto.html`: compatible with the progressive explanation and replaceable-tool posture; retained as the philosophical/editorial deep link.
- `docs/index.html` / `docs/index-en.html`: not modified because #676 has active overlapping work.
- public prototype/map surfaces remain technical/prototype projections and are not made new authority sources by this page.

## Boundaries

This is static public documentation only.

It does not add or modify:

- a schema;
- a registry;
- a Capability Slot;
- a runtime;
- an executor;
- a scheduler or queue;
- a provider router;
- a memory engine;
- an automatic approval path;
- a Pantheon authority owner.

The page is a projection of existing repository concepts and candidate bindings.

## Follow-up

After #676 is resolved, add a small public navigation link from the landing to `comprendre.html` / `understand.html` rather than rebasing competing landing copy into this PR.
