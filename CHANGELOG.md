# Changelog

## 0.1.27 - 2026-06-01

Core records model (cross-domain base for contacts, dossiers, documents, emails).

### Added

- `docs/governance/CORE_RECORDS_MODEL.md` as active support doctrine: the tool-agnostic, profession-agnostic record model shared by every domain (contact, organization, scope, document, message, event, decision, membership, party role) and the scope-keyed separation rule. Shapes only — the database, row-level scope enforcement and connectors are adapters outside Pantheon.
- `ai_logs/2026-06-01-core-records-model.md` as the intervention trace.

### Changed

- `docs/governance/MODULES.md` and `docs/governance/AUTHORITY_INDEX.md` now index the core records model. `STATUS.md` and `README.md` are being rewritten in PR #42 and should index it when that lands.

### Boundary clarification

Documentation only. It does not implement a database, schema, migration, connector, email intake, contact sync, OCR, vector index, runtime or executable artifact. Scope vocabulary remains owned by `SCOPE_ISOLATION.md`.

```text
The core records what every profession shares.
The scope keeps each dossier separate.
The domain pack adds the profession.
```

---

## 0.1.24 - 2026-06-01

AgentOS external reference review.

### Added

- `docs/governance/reference_reviews/AGENTOS.md` as an external reference review for runtime boundary vocabulary, memory review signals and claim review;
- `ai_logs/2026-06-01-agentos-reference-review.md` as the intervention trace.

### Boundary clarification

Documentation and reference review only.

It does not implement a runtime, generated capability execution, provider routing, scheduler, queue, OpenWebUI extension, Hermes skill, schema change, test, operations tooling, automatic approval or automatic memory promotion.

---

## 0.1.23 - 2026-05-31

Modular domain reorientation reconciliation (#25) and governance indexing.

### Changed

- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md` now uses abstract role names in the body, tables and diagram, confines product names to the bindings registry (with an explicit bindings/adapters exception), reconciles the module manifest `status` with `MODULE_ACTIVATION.md` (status, activation and task authorization as three separate axes), adds a hierarchy note that it reconciles rather than replaces existing doctrine, and clarifies that a domain pack is a governed methodology configuration, not an executable runtime module;
- `docs/governance/ADAPTERS_AND_BINDINGS.md` now records that it is part of the bindings and adapters naming exception;
- `docs/governance/STATUS.md`, `docs/governance/README.md`, `docs/governance/MODULES.md` and `docs/governance/CORE_CONCEPTS_MAP.md` now index `MODULAR_DOMAIN_REORIENTATION.md`, `ADAPTERS_AND_BINDINGS.md`, `CAPABILITY_PLACEMENT.md`, `ARCHITECTURE_AGENCY_DOMAIN_PACK.md`, `KNOWLEDGE_INGESTION_AND_MEMORY.md` and `WORKFLOW_LIFECYCLE.md` in the read path.

### Added

- `ai_logs/2026-05-31-modular-domain-reorientation-reconciliation.md` as the intervention trace;
- `ai_logs/2026-05-31-data-platform-boundary-review.md` as the data-platform boundary-review trace.

### To verify

- `DATA_PLATFORM_ARCHITECTURE.md`, `DATA_PLATFORM_INDEX.md` and `DATA_PLATFORM_STATUS.md` are indexed with a `to verify` status, pending a boundary review against `CLAUDE.md`. Indexing does not endorse them as canonical; a data platform must not become a Pantheon runtime.

### Data platform boundary review (#30)

- `DATA_PLATFORM_ARCHITECTURE.md`: `Directus exposes and controls` → `Directus exposes controlled records`; the deployment section is reframed as `Candidate deployment profiles outside Pantheon` with a no-authorization disclaimer; table families are marked conceptual registry families, not approved schema; an adapter/binding status note is added.
- `ARCHITECTURE_AGENCY_DOMAIN_PACK.md`, `KNOWLEDGE_INGESTION_AND_MEMORY.md` and `WORKFLOW_LIFECYCLE.md` are realigned to `candidate / to verify` in `STATUS.md`, `README.md` and `MODULES.md` to match their own headers and the #30 boundary review.
- `DATA_PLATFORM_RECONCILIATION.md` (added to `main` as candidate reconciliation doctrine) is indexed in `STATUS.md`, `README.md` and `MODULES.md`.

### Not included

AgentOS distillation (Issue #27) is intentionally out of scope and left to its own change.

### Boundary clarification

Documentation and indexing only.

It does not implement a runtime, a bridge, a plugin manager, a skill installer, a module registry runtime, an executable schema, automatic approval or automatic memory promotion.

Central rule:

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```

---

## 0.1.22 - 2026-05-31

Adapters and bindings support doctrine.

### Added

- `docs/governance/ADAPTERS_AND_BINDINGS.md` as active support doctrine for the blueprint-in-Pantheon and adapter-outside model, defining where tool-specific templates and configurations live (OpenWebUI, Hermes, Langfuse and others) and the four disciplines that keep them adapted to Pantheon without coupling Pantheon to any tool;
- `ai_logs/2026-05-31-adapters-and-bindings.md` as the intervention trace.

### Boundary clarification

This release documents a configuration-placement model only.

It does not implement a configuration, an OpenWebUI Function, a Hermes skill, a Langfuse project, a runtime, a bridge or any executable artifact.

Central rule:

```text
The blueprint lives in Pantheon.
The adapter lives in the tool.
The dependency always points to Pantheon.
The validated remains.
```

---

## 0.1.21 - 2026-05-31

Modular domain reorientation coordination artifact.

### Added

- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md` as active support doctrine for tool-agnostic placement, the modular capability contract (manifest plus envelope) and the domain-pack projection model, including a bindings registry, the placement test, the complete module manifest shape, the domain-pack section-to-layer table and a Mermaid diagram;
- `ai_logs/2026-05-31-modular-domain-reorientation.md` as the intervention trace.

### Boundary clarification

This release documents a coordination and placement model only.

It does not implement a runtime, a bridge, a plugin manager, a skill installer, a module registry runtime, a domain-pack worker, an OpenWebUI Function, a Hermes skill, an executable schema, automatic approval or automatic memory promotion.

The complete manifest is recorded as a shape only. A canonical executable schema under `schemas/` requires explicit approval before being added.

Central rule:

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```

---

## 0.1.20 - 2026-05-31

SOUL.md Hermes profile identity boundary review and integration.

### Added

- `docs/governance/reference_reviews/SOUL_MD_HERMES_PROFILE.md` as a support review and pattern card for SOUL-like identity layers in Hermes profiles;
- `Profile identity layer` entry in `docs/governance/DISTILLATION_REGISTRY.md` with status `hermes_candidate_constraint`.

### Changed

- `docs/governance/HERMES_INTEGRATION.md` now defines the allowed and forbidden use of SOUL-like Hermes profile identity layers;
- `docs/governance/reference_reviews/README.md` now indexes the SOUL.md review.

### Boundary clarification

This release documents profile identity governance only.

It does not install `SOUL.md`, modify Hermes runtime behavior, deploy profiles, create Pantheon Roles, authorize tool use, approve outputs, promote memory, create a profile marketplace, add a plugin manager or create runtime behavior inside Pantheon Next.

Central rule:

```text
A SOUL-like file may stabilize how Hermes executes.
It must never decide what Pantheon validates.
```

---

## 0.1.19 - 2026-05-30

Evidence Topology doctrine, examples and index reconciliation.

### Added

- `docs/governance/EVIDENCE_TOPOLOGY_GATE.md` as active doctrine for reasoning topology selection, proof-chain preservation, persistent role-team handoff and bounded Hermes swarm constraints;
- `docs/governance/EVIDENCE_TOPOLOGY_ROADMAP.md` as a roadmap addendum for single-context, fan-out extraction, role-team handoff and swarm boundaries;
- `docs/governance/EVIDENCE_TOPOLOGY_RECONCILIATION.md` as a safe reconciliation note for index and status alignment;
- `docs/governance/EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md` as a non-executable schema candidate note, without modifying `schemas/`;
- `docs/governance/EVIDENCE_TOPOLOGY_BRIDGES.md` to link the doctrine to Task Contracts, Evidence Packs, Hermes, OpenWebUI, memory, scope, tools, Governance College and User Decision Gate;
- `docs/governance/EVIDENCE_TOPOLOGY_CHECKLIST.md` as a practical checklist for selecting topology;
- `docs/governance/evidence_topology_antipatterns/` with support cards for summary-only handoff, swarm as authority, role memory as Canonical Memory, conductor as ZEUS and canvas as Evidence Pack;
- `docs/examples/evidence_topology/` with fictional Task Contract and Evidence Pack examples;
- `docs/examples/architecture_devis_reprise/EVIDENCE_TOPOLOGY_EXAMPLE.md` as a fictional architecture / MOE topology example.

### Changed

- `README.md` and `README.fr.md` now explain Evidence Topology in public-facing language and link to the gate and checklist;
- `docs/governance/STATUS.md` now records Evidence Topology as active doctrine;
- `docs/governance/README.md` now indexes Evidence Topology in the read order, document lists and boundary section;
- `docs/examples/README.md` now indexes the `evidence_topology/` example folder.

### Boundary clarification

This release documents governance and examples only.

It does not implement a topology router, scheduler, queue, worker dispatcher, graph runtime, swarm controller, OpenWebUI plugin, Hermes configuration, automatic approval, automatic memory promotion, schemas, tests, operations tooling, platform files, Docker changes or environment configuration.

Central rule:

```text
The unit of reasoning is not the agent.
The unit of reasoning is the proof chain.
```

Operational boundary:

```text
Swarm for collection.
Role-team handoff for bounded artifact stages.
Single context for inference when evidence must connect.
Governance College for review.
User Decision Gate for unresolved stakes.
Human decision for consequential approval.
```

---

## 0.1.18 - 2026-05-30

Core concepts map and doctrine navigation consolidation.

### Added

- `docs/governance/CORE_CONCEPTS_MAP.md` as active navigation doctrine for Pantheon core concepts and relationships;
- compact object map for Task Contracts, Context Packs, Evidence Packs, approvals, memory, roles, rites, domain packs, skill candidates, modules, Effective Policy, OpenWebUI Templates, User Decision Gates, external tools and reference reviews;
- authority ladder separating source, evidence, approval, Memory Candidate and Canonical Memory;
- execution ladder separating Task Contract, Context Pack, Hermes execution, candidate return, Pantheon review and OpenWebUI exposure;
- high-risk shortcut list to reject concept collapses such as `retrieved = evidence`, `schema valid = approved`, `Nango connection = authorized external action` or `OpenWebUI Function = Pantheon runtime`.

### Changed

- `docs/governance/README.md` now indexes `CORE_CONCEPTS_MAP.md`, adds a short stable reading path and records the core concepts boundary;
- `README.md` now links to `CORE_CONCEPTS_MAP.md` from the public vocabulary section and key entry points;
- `docs/governance/STATUS.md` now tracks the core concepts map as active navigation doctrine and records the associated non-runtime boundary and risk.

### Boundary clarification

This release documents navigation support only.

It does not implement a schema, runtime model, workflow engine, module registry, plugin manager, approval engine, memory engine, OpenWebUI UI, Hermes integration, tests, operations tooling, automatic approval or automatic memory promotion.

Central rule:

```text
Every concept has one job.
Every promotion requires governance.
Every external action requires a boundary.
Every unresolved tension must remain visible.
```

---

## 0.1.17 - 2026-05-30

Public and governance index reconciliation.

### Changed

- `README.md` now reflects the reconciled declarative schema baseline, first read-only schema validation test, RAG evidence-boundary doctrine and current fictional example set;
- `README.fr.md` now mirrors the same public status and example updates in French;
- `docs/governance/README.md` now indexes Nango, Future AGI and the connector gateway boundary, and no longer states that tests are entirely absent;
- `docs/governance/STATUS.md` now records Nango support doctrine, Future AGI support doctrine, connector/reliability non-implementation boundaries and related risks;
- `docs/governance/ROADMAP.md` now records Nango/Future AGI support doctrine, current examples, first read-only schema test coverage and future connector/reliability read-only consistency checks.

### Clarification

The historical `0.1.11` entry remains accurate for the moment it was written: the Phase D1 schema baseline was not yet backed by tests at that time.

The current repository state is later than that entry and now includes a first read-only schema validation test file.

### Boundary clarification

This release documents public-index and governance-index reconciliation only.

It does not implement connector runtime, credential storage, OAuth provider configuration, Future AGI installation, observability backend, simulation runtime, provider gateway, broad test suite, CI coverage, read-only operations tooling, automatic approval or automatic memory promotion.

Central rule:

```text
Indexes describe the current doctrine surface.
They do not install, execute, validate or approve anything by themselves.
```

---

## 0.1.16 - 2026-05-29

Understand-Anything graph authority boundary lock.

### Changed

- `docs/governance/UNDERSTAND_ANYTHING_HERMES_ADAPTER.md` now links to the fictional structural-analysis examples;
- `docs/governance/REJECTED_PATTERNS.md` now explicitly rejects generated repository graphs as architecture truth;
- `docs/governance/TENSIONS_AND_RISKS.md` now records repository radiography vs graph authority as a persistent governance tension.

### Boundary clarification

This release documents rejection memory and tension preservation only.

It does not implement graph analysis, GraphRAG runtime, repository graph validation, automatic enforcement, runtime blocking, OpenWebUI plugin behavior, Hermes skill installation, repository automation, tests or operations tooling.

Central rule:

```text
A graph may reveal structure.
It does not validate structure.
It does not approve architecture.
It does not create memory.
```

---

## 0.1.15 - 2026-05-29

RAG evidence-boundary reconciliation across status, roadmap and ingestion doctrine.

### Changed

- `docs/governance/STATUS.md` now indexes `RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md`, records RAG evidence-boundary doctrine and explicitly marks RAG runtime, retrieval runtime, chunking runtime, benchmark runner, scoring backend and OpenWebUI Knowledge mutation as not implemented;
- `docs/governance/ROADMAP.md` now lists `RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` in active doctrine, adds a RAG evidence-boundary section and includes future read-only RAG evidence-boundary consistency checks;
- `docs/governance/RAG_INGESTION_PIPELINE.md` now aligns its doctrine chain with `RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` by adding `Ingestion Candidate`, `Chunk / Retrieval Unit` and `Context Sufficiency Check`.

### Boundary clarification

This release documents reconciliation only.

It does not implement RAG runtime, retrieval runtime, chunking runtime, benchmark runner, scoring backend, OpenWebUI Knowledge mutation, Hermes ingestion worker, tests, operations tooling, automatic approval or automatic memory promotion.

Central rule:

```text
RAG ingestion can prepare sources.
RAG evidence boundaries decide what the preparation means.
Neither creates proof, approval or memory by itself.
```

---

## 0.1.14 - 2026-05-29

Understand-Anything structural-analysis fictional examples.

### Added

- `docs/examples/understand_anything_structural_analysis/README.md` as a non-executable example index;
- `docs/examples/understand_anything_structural_analysis/TASK_CONTRACT_STRUCTURAL_ANALYSIS.md` as a fictional `STRUCTURAL_ANALYSIS` Task Contract example;
- `docs/examples/understand_anything_structural_analysis/EVIDENCE_PACK_CANDIDATE.md` as a fictional Evidence Pack Candidate example for external structural-analysis output.

### Changed

- `docs/examples/README.md` now indexes the Understand-Anything structural-analysis example.

### Boundary clarification

These examples are fictional and educational only.

They do not implement Understand-Anything, install Hermes skills, create command syntax, create repository hooks, commit generated graph artifacts, approve graph output, create GraphRAG runtime, create Canonical Memory or authorize repository mutation.

Central rule:

```text
The graph may help review the repository.
It does not decide what the repository is.
It does not approve what should change.
It does not remember anything by itself.
```

---

## 0.1.13 - 2026-05-29

Rites governance layer.

### Added

- `docs/governance/rites/README.md` as the index for shared governance rites;
- `docs/governance/rites/_TEMPLATE_RITE.md` as a rite documentation template;
- `docs/governance/rites/RITE_DIVERGENCE_CONTROLEE.md` for divergent option exploration before convergence;
- `docs/governance/rites/AUTOCRITIQUE_CONTRADICTOIRE.md` for structured post-draft contradiction;
- `docs/governance/rites/CONCORDANCE_DES_SOURCES.md` for source comparison and claim support review;
- `docs/governance/rites/PREMISSES_CACHEES.md` for implicit assumption extraction;
- `docs/governance/rites/REFONDATION_DE_SESSION.md` for controlled reset when session context becomes polluted.

### Changed

- `docs/governance/README.md` now indexes the Rites layer and active rite documents;
- `ai_logs/2026-05-29-rites-governance-layer.md` records the intervention, rationale, boundary and limitations.

### Boundary clarification

Rites are documentation-level governance procedures.

They do not implement a runtime, scheduler, queue, provider router, tool runtime, hidden debate system, OpenWebUI plugin, Hermes skill installation, automatic approval or automatic memory promotion.

Central rule:

```text
Roles judge.
Rites coordinate.
Task Contracts bound.
Evidence Packs prove.
ZEUS states procedure.
The human decides.
```

---

## 0.1.12 - 2026-05-29

Understand-Anything external reference review and Hermes Skill Candidate boundary.

### Added

- `docs/governance/reference_reviews/UNDERSTAND_ANYTHING.md` as an external reference review for Understand-Anything, Hermes Agent and Hermes Desktop boundary classification;
- `docs/governance/UNDERSTAND_ANYTHING_HERMES_ADAPTER.md` as support doctrine for a non-implemented Hermes-side structural analysis skill candidate;
- Understand-Anything watch record in `docs/governance/SKILL_WATCHLIST.md`;
- Understand-Anything reference review index entry in `docs/governance/reference_reviews/README.md`.

### Changed

- `docs/governance/README.md` now indexes the Understand-Anything reference review and Hermes adapter support doctrine;
- `docs/governance/STATUS.md` now tracks Understand-Anything support doctrine, Hermes Desktop non-adoption and the explicitly absent implementation areas.

### Boundary clarification

This release documents governance support only.
