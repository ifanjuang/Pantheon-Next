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
-> Pantheon grammar
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

## Pantheon grammar pass

A second repository reading was performed before expanding the Pantheon section. The page now follows the current owners rather than the older landing shorthand:

- `AGENTS.md` for the canonical seven Pantheon Roles;
- `GOVERNANCE_COLLEGE.md` for separated judgment, proportional activation and procedural arbitration;
- `rites/README.md` for the active shared recurring methods and their non-runtime boundary;
- `EVOLUTION_OF_ROLES_RITES_AND_SPACES.md` for the controlled distinction between Roles, Rites, governed Spaces and presentation structures;
- `NARRATIVE.md` for the explanatory city / gods metaphor and the clarification that Mnemosyne is not currently a canonical Role.

The public explanation now compresses the grammar as:

```text
Roles = distinct viewpoints of judgment
Rites = bounded methods for recurring methodological tensions
Spaces = durable distinctions between kinds of activity
Hermes/executor = performs admitted work
Pantheon = governs status, scope and consequences
Human = decides what is consequential
```

### Canonical roles explained

The page introduces only the seven roles currently registered in `AGENTS.md`:

- ATHENA — structure and decomposition;
- ARGOS — sources, versions and traceability;
- THEMIS — risk, limits and approval boundaries;
- APOLLO — clarity, completeness and delivery readiness;
- HEPHAISTOS — fabrication and implementation candidates;
- IRIS — formulation and transmission;
- ZEUS — status and next-procedure arbitration.

Each role is paired with a plain-language situation where its viewpoint becomes especially useful. The page explicitly says that roles are not seven autonomous agents and that the full college is not activated for every task.

Hermes Agent remains on the execution side. A Hermes profile may align with a Role viewpoint without inheriting Pantheon authority.

Mnemosyne is explained only as a possible visual memory figure; it is not promoted into the canonical role registry.

### Rites explained

The page introduces the five currently active shared rites through the symptom that makes each useful:

- controlled divergence when convergence happens too early;
- contradictory self-review when a polished first result is too easy to trust;
- source concordance when documents or versions may conflict;
- hidden premises when a plan depends on unstated assumptions;
- session refoundation when context has become polluted or mixed.

A sixth card deliberately explains that a simple task may need no rite at all. This preserves the proportionality and anti-ceremony rule from the Rite doctrine.

### Governed spaces explained

The page distinguishes:

- Governance Reference Space — reusable doctrine, rules and methods;
- Project Space — bounded project-specific sources, constraints, decisions and evidence candidates;
- Agora — visible deliberation when legitimate disagreement, professional preference or human arbitration remains.

The explanation states that a Space does not grant authority by itself and is not automatically a backend domain or UI screen.

### End-to-end example

The synthetic `LIA21` thread is replayed through the grammar:

```text
Project Space
-> Task Contract bounds the mission and names useful viewpoints
-> ATHENA checks structure
-> ARGOS checks sources and versions
-> Rite only if the observed tension justifies it
-> THEMIS / APOLLO / IRIS review consequence and delivery
-> ZEUS qualifies the next procedure
-> Agora only if a legitimate choice remains open
-> explicit question to the human
-> human decision
```

HEPHAISTOS is deliberately shown as unnecessary in this email example, demonstrating minimum-effective governance rather than ritual activation of every role.

## Schema convergence pass

A third read checked the public wording against the validation contracts and their current boundary notes before the final copy pass:

- `schemas/task_contract.schema.yaml`;
- `schemas/role_signal.schema.yaml`;
- `schemas/evidence_pack.schema.yaml`;
- `schemas/register_candidate.schema.yaml`;
- `schemas/context_pack.schema.yaml`;
- `schemas/document_knowledge_slice.schema.yaml`;
- `schemas/shared_axes.schema.yaml`;
- `schemas/decision_request.schema.yaml`;
- `schemas/workflow_manifest.schema.yaml`;
- `schemas/README.md`.

The page was adjusted without changing any schema:

- Role prose now emphasizes viewpoints of judgment rather than runtime workers;
- Task Contract now explicitly links mission scope, Role owner/viewpoints, constraints, approval, expected evidence, allowed/forbidden outputs and memory rules;
- HEPHAISTOS is described as qualifying fabrication / candidate composition while the executor performs the concrete production;
- Agency / Projects / Sandbox are consistently named working-memory domains, separate from governed Spaces and from canonical Task Contract scopes;
- the document path is now `original source -> extraction -> derived source-located structure -> provenance-bearing chunks`; Markdown is explained as either an original source or a derived working representation depending on how it was produced;
- `Evidence Item` and `Evidence Pack` are explained separately;
- a Register Candidate is shown as the review seam before a retained Probative Register entry;
- Decision Request is explained as an explicit human-attention question distinct from the resulting decision;
- the E / V / K / C axes are exposed only at second depth, keeping the first read simple;
- the page now states that Task Contracts, Role Signals, Evidence Packs and several other objects have validation schemas while Rites and governed Spaces remain primarily documented governance grammar rather than uniform machine objects.

No absence of a `rite.schema` or `governed_space.schema` is treated as a defect. The schema README explicitly treats schemas as validation contracts and allows doctrine/schema reconciliation to remain staged.

## Candidate posture preserved

The public page records:

- Hermes Agent as a replaceable candidate for the external executor role;
- Obsidian as a qualified candidate workspace around local Markdown notes;
- Hindsight as the first qualified bounded associative working-memory candidate;
- TencentDB Agent Memory as evaluated and currently deferred for the tested topology;
- Docling as the preferred document-structural-analysis candidate, with runtime integration still a separate qualification fact.

No candidate is described as a mandatory Pantheon dependency.

## Memory and document explanation

The page explains three working-memory domains without exposing private workspace names or project identities:

```text
Agence / Agency
Projets / Projects
Sandbox
```

These working-memory domains remain separate from the governed Space concept introduced later in the Pantheon grammar section.

It also explains:

- strict project/context/source classification;
- source-linked chunking;
- document and Markdown versioning;
- Markdown as portable plain text rather than source replacement;
- original source -> extraction -> derived source-located structure -> provenance-bearing chunks;
- Markdown as either source or derivative according to origin;
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

## Parallel landing discrepancy

Open PR #676 currently describes an eight-viewpoint grid by adding Mnemosyne as `Continuité / Continuity`. That conflicts with the seven-role registry used by `AGENTS.md`, `task_contract.schema.yaml` and `role_signal.schema.yaml`.

This branch does not modify #676's landing files. The required convergence is to keep Mnemosyne as a memory figure or explanatory metaphor without presenting it as an eighth canonical Pantheon Role, and to link the landing to `comprendre.html` / `understand.html` after the two branches are reconciled.

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

After #676 is resolved:

1. normalize its Role grid to the canonical seven roles, keeping Mnemosyne outside the Role registry;
2. add a small public navigation link from the landing to `comprendre.html` / `understand.html` rather than rebasing competing landing copy into this PR.