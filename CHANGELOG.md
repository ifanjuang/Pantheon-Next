# Changelog

## 0.1.31 - 2026-06-07

External runtime memory adapter boundary.

### Added

- `docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` as active support doctrine for external runtime memory, checkpoint, graph recall, observability and loop-detection adapters.
- `ai_logs/2026-06-07-external-runtime-memory-adapters.md` as the intervention trace.

### Changed

- `docs/governance/AUTHORITY_INDEX.md`, `docs/governance/MODULES.md` and `docs/governance/README.md` now index the generic external runtime memory adapter boundary.

### Boundary clarification

Documentation only.

No runtime, memory backend, vector store, graph database, checkpoint engine, observability backend, MCP server, connector, schema, test, operations tooling, platform component, Docker change, approval engine or automatic memory promotion was implemented.

Core rule:

```text
External runtime memory may store, recall, rank, summarize, checkpoint or trace.
It may propose Memory Candidates and Evidence Pack Candidates.
It must not promote Canonical Memory, validate truth, approve action, decide scope or authorize external effects.
```

---

## 0.1.30 - 2026-06-01

Request lifecycle doctrine (MÈTIS, the cap, memory gates).

### Added

- `docs/governance/REQUEST_LIFECYCLE.md` as active support doctrine: the governed lifecycle of a request. MÈTIS is a situated-comprehension role activated conditionally (only on fuzzy/indirect/implicit/contradictory/vague-but-consequential demands; a light triage decides, MÈTIS may be convened mid-course) that establishes the real demand, the goal (the cap), the watch-points and the responsibility limit, and holds and re-reads the cap. The cap lives in the Task Contract; re-evaluation is a governed revision. Zeus arbitrates the cap (validated / back to MÈTIS to deepen / routed to human), with a bounded loop and framing-not-engagement separation. Cerbère and Charon are memory-threshold gates (filter what returns from the past; archive what must stop acting), not judges. Distinct natures: roles vs gates vs runtime vs human.
- `ai_logs/2026-06-01-request-lifecycle-metis.md` as the intervention trace.

### Changed

- `docs/governance/MODULES.md` and `docs/governance/AUTHORITY_INDEX.md` now index the request lifecycle.

### Boundary clarification

Documentation only — governance moments, not an execution pipeline. No runtime, scheduler, message bus, workflow engine, orchestration loop, automatic approval or automatic memory promotion. Promoting MÈTIS into the canonical role registry (`AGENTS.md`, `GOVERNANCE_COLLEGE.md`) and the gates into `MEMORY.md` / `CORE_RECORDS_MODEL.md` is a separate governed step.

```text
MÈTIS understands and holds the cap, when the demand is unclear.
ZEUS arbitrates the status, on evidence.
The human decides at the cliffs and engages.
```

---

## 0.1.26 - 2026-06-01

Optimize and de-duplicate the governance index files (STATUS.md and README.md).

### Changed

- `docs/governance/STATUS.md` reduced from 368 to ~75 lines. It no longer mirrors the full document listing, the read path or the per-doctrine summaries. It now records posture, the migration rule, a single boundary statement, and a `Live exceptions` table for candidate / to-verify items, with precedence rules pointing to the authoritative indexes.
- `docs/governance/README.md` reduced from 637 to ~150 lines. It is now the entry point and read path only. The two exhaustive document listings and the ~13 per-doctrine "boundary" sections were removed (each duplicated `STATUS.md`, `AUTHORITY_INDEX.md`, `MODULES.md` or the source doc itself). README now carries one consolidated boundary statement and a thematic read path, and delegates enumeration/classification with explicit precedence rules.

### Ownership (who owns what)

- `README.md` — entry point and read path.
- `STATUS.md` — posture and live exceptions.
- `AUTHORITY_INDEX.md` — authority class and status of each item.
- `MODULES.md` — module map per governance area.

### Boundary clarification

Documentation only. No doctrine removed in substance; redundant restatements consolidated and enumeration delegated. No runtime, schema, test or executable change. CI checks verified locally (no stub section; queue/scheduler lint clean on README, STATUS and AUTHORITY_INDEX).

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
