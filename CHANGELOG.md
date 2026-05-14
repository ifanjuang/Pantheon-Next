# Changelog

## 0.1.2 - 2026-05-14

Conceptual stabilization, narrative integration and workflow language stabilization.

### Added

#### Conceptual stabilization

- active `CONCEPTUAL_STABILIZATION.md` migration guardrail;
- governance-first distillation rule for Pantheon-OS recovery;
- explicit `do not migrate unless governance value is proven` posture;
- reduced conceptual core around Role, Policy, Contract, Evidence, Approval, Context and Memory Candidate.

#### Stabilized governance core

- active `TASK_CONTRACTS.md` doctrine;
- active `EVIDENCE_PACK.md` doctrine;
- active `MEMORY.md` doctrine;
- active short-form `APPROVALS.md` doctrine;
- clarified `AGENTS.md` role semantics;
- active `WORKFLOW_SCHEMA.md` doctrine as `Workflow Manifest`;
- active `RUN_GRAPH.md` doctrine as `Run Trace View`;
- active `REQUEST_ORCHESTRATION.md` doctrine as `Request Coordination`.

#### Narrative and visual layer

- `docs/governance/NARRATIVE.md`;
- `docs/governance/VISUAL_LANGUAGE.md`;
- README introduction using the city-game metaphor;
- governance index entries for narrative and visual documents.

### Changed

- `README.md` now presents Pantheon Next as both a governance kernel and a city-game of reliable decisions;
- `docs/governance/README.md` now distinguishes active doctrine, narrative support doctrine and stub placeholders;
- `docs/governance/STATUS.md` now reflects the active status of Task Contracts, Evidence Packs, Memory, Approvals, narrative doctrine and workflow doctrine;
- `AGENTS.md` now clarifies that the canonical concept is Pantheon Role, while the filename remains historical compatibility;
- workflow vocabulary is now explicitly governance-only.

### Narrative doctrine

The central narrative sentence is now:

```text
L'IA ouvre les possibles.
Pantheon les organise.
L'humain décide.
Le validé reste.
```

The narrative layer is explicitly non-runtime.

It must not redefine Pantheon Next as a game engine, execution engine, autonomous city, hidden workflow runner or agent runtime.

### Workflow doctrine

`WORKFLOW_SCHEMA.md` no longer defines runtime workflow semantics.

It defines a `Workflow Manifest`: a reusable governance declaration for a class of work.

`RUN_GRAPH.md` no longer defines executable graph semantics.

It defines a `Run Trace View`: a human-readable review and evidence trace.

`REQUEST_ORCHESTRATION.md` no longer defines runtime orchestration.

It defines `Request Coordination`: governance intake, review sequencing and escalation guidance.

These documents are explicitly non-runtime.

They must not define:

- execution;
- scheduling;
- queueing;
- provider routing;
- hidden orchestration;
- automatic memory promotion;
- autonomous agent plans.

### Boundary clarifications

- Iris is preferred as the narrative transmission figure to avoid confusion with Hermes Agent;
- Hermes Agent remains the external execution runtime;
- Mnemosyne may appear as a memory figure, but is not a canonical Pantheon Role unless `AGENTS.md` is explicitly updated;
- narrative companions produce candidate viewpoints and do not self-promote truth;
- workflow documents describe governance expectations, not runtime behavior.

### Current repository posture

Pantheon Next now has a stronger conceptual, narrative and workflow-governance baseline.

The next critical area is integration boundary stabilization, especially `HERMES_INTEGRATION.md`, `OPENWEBUI_INTEGRATION.md`, `EXTERNAL_TOOLS_POLICY.md` and `KNOWLEDGE_TAXONOMY.md`.

---

## 0.1.1 - 2026-05-12

Repository governance reconciliation and structural stabilization.

### Added

#### Governance bootstrap wave

- governance stub documents for architecture, approvals, task contracts, evidence packs and memory;
- governance stub documents for workflow schemas, workflow adaptation, role signals, memory event schema and skill lifecycle;
- explicit stub status headers for non migrated doctrine;
- governance-first repository status tracking.

#### Governance structure stabilization

- repository-wide distinction between implemented, stub-present and absent governance assets;
- governance README reconciliation with actual filesystem state;
- roadmap reconciliation with actual repository state;
- canonical anti-runtime boundary doctrine;
- preserved historical governance references from Pantheon-OS.

#### Hermes profile structure

- lightweight Hermes profile template structure;
- candidate-only execution doctrine for Hermes profiles;
- canonical naming alignment for `hephaistos-agent`;
- shared Hermes profile base rules.

### Changed

- `STATUS.md` rewritten as repository state registry;
- `README.md` governance index aligned with `CLAUDE.md` read order;
- `ROADMAP.md` aligned with actual implementation state;
- governance bootstrap now explicitly distinguishes:
  - implemented doctrine;
  - stub placeholders;
  - absent documents;
  - deferred features.

### Explicitly not implemented

The repository intentionally does not implement:

- autonomous runtime;
- hidden orchestration runtime;
- internal scheduler;
- queue system;
- provider router runtime;
- automatic Hermes installation;
- automatic skill installation;
- automatic memory promotion;
- hidden workflow execution;
- execution API endpoints.

### Current repository posture

Pantheon-Next is now structurally coherent but still under controlled migration from Pantheon-OS.

Governance structure and runtime boundaries are stabilized.

Schemas, tests, read-only tooling and migrated canonical doctrine remain incomplete.

---

## 0.1.0 - 2026-05-12

Initial Pantheon Next governance-first bootstrap.

### Added

- clean repository baseline;
- governance-first README;
- CLAUDE.md doctrine instructions;
- bootstrap AI logs;
- repository hygiene files;
- minimal Python project configuration;
- runtime boundary doctrine.

### Migration status

Pantheon-Next is under controlled migration from Pantheon-OS.

Only governance-relevant assets are migrated.

Runtime-oriented historical components remain excluded unless explicitly reviewed and approved.
