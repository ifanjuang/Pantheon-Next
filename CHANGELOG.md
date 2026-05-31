# Changelog

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