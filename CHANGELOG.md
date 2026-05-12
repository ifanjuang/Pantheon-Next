# Changelog

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
