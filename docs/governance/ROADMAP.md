# Pantheon Next Roadmap

Pantheon Next is a governance-first repository with minimal read-only tooling.

This roadmap defines controlled migration and stabilization phases. It must not be interpreted as a runtime implementation plan.

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next must not recreate an autonomous execution engine, agent runtime, tool runtime, scheduler, queue, provider router, hidden workflow runtime or automatic skill installer.

## Phase 0 — Clean repository bootstrap

Status: largely implemented.

Goals:

- initialize the repository baseline;
- add AI operating instructions;
- add repository hygiene files;
- add license, version and changelog;
- add bootstrap AI log;
- establish runtime boundary doctrine.

Implemented:

- `README.md`;
- `CLAUDE.md`;
- `.gitignore`;
- `pyproject.toml`;
- `LICENSE`;
- `VERSION`;
- `CHANGELOG.md`;
- `ai_logs/README.md`;
- `ai_logs/2026-05-12-pantheon-next-bootstrap.md`.

## Phase 1 — Canonical governance baseline

Status: partial.

Goals:

- migrate canonical governance Markdown from Pantheon-OS selectively;
- keep `docs/governance/AGENTS.md` as the single canonical Pantheon Role registry;
- avoid governance duplication in Hermes profile folders;
- add glossary and simplification plan;
- add STATUS and governance README index.

Implemented or stub-present:

- `docs/governance/README.md`;
- `docs/governance/STATUS.md`;
- `docs/governance/ROADMAP.md`;
- `docs/governance/AGENTS.md`;
- `docs/governance/ARCHITECTURE.md`;
- `docs/governance/APPROVALS.md`;
- `docs/governance/TASK_CONTRACTS.md`;
- `docs/governance/EVIDENCE_PACK.md`;
- `docs/governance/MEMORY.md`;
- `docs/governance/MEMORY_EVENT_SCHEMA.md`;
- `docs/governance/ROLE_SIGNALS.md`;
- `docs/governance/WORKFLOW_SCHEMA.md`;
- `docs/governance/WORKFLOW_ADAPTATION.md`;
- `docs/governance/SKILL_LIFECYCLE.md`;
- `docs/governance/GLOSSARY.md`;
- `docs/governance/REPOSITORY_SIMPLIFICATION_PLAN.md`;
- `docs/governance/EXTERNAL_AI_OPTION_REVIEWS.md`.

Still absent:

- `docs/governance/MODULES.md`;
- `docs/governance/TASK_CONTRACT_REVISIONS.md`;
- `docs/governance/RUN_GRAPH.md`;
- `docs/governance/EXECUTION_DISCIPLINE.md`;
- `docs/governance/MODEL_ROUTING_POLICY.md`;
- `docs/governance/ROUTING_FOUNDATION.md`;
- `docs/governance/HERMES_INTEGRATION.md`;
- `docs/governance/OPENWEBUI_INTEGRATION.md`;
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`;
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`;
- `docs/governance/KNOWLEDGE_TAXONOMY.md`.

## Phase 2 — Hermes profile templates

Status: partial.

Goals:

- add lightweight Hermes profile templates;
- keep profiles candidate-only;
- avoid per-profile `governance.md` files;
- avoid automatic Hermes installation;
- bind each profile to `docs/governance/AGENTS.md`.

Implemented:

- `athena`;
- `argos`;
- `themis`;
- `apollo`;
- `zeus`.

Remaining:

- `iris`;
- `hephaistos`.

## Phase 3 — Schemas and examples

Status: not implemented.

## Phase 4 — Read-only tooling

Status: not implemented.

## Phase 5 — Context packs and integration specs

Status: not implemented.

## Phase 6 — Optional read-only Domain API

Status: deferred.

The API must remain governance-only and read-only if ever implemented.

## Current risks

- governance migration remains incomplete;
- schemas are not yet migrated;
- tests are not yet present;
- Hermes profile coverage is incomplete;
- stubs must not be mistaken for canonical migrated doctrine.
