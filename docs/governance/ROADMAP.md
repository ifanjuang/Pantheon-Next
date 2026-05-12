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

Status: partial.

Goals:

- initialize the repository baseline;
- add AI operating instructions;
- add repository hygiene files;
- add license, version and changelog;
- add bootstrap AI log;
- establish runtime boundary doctrine.

Current status:

- `README.md`: implemented;
- `CLAUDE.md`: implemented;
- `.gitignore`: implemented;
- `pyproject.toml`: implemented;
- `LICENSE`: implemented;
- `VERSION`: implemented;
- `CHANGELOG.md`: implemented;
- `ai_logs/2026-05-12-pantheon-next-bootstrap.md`: implemented.

## Phase 1 — Canonical governance baseline

Status: partial.

Goals:

- migrate canonical governance Markdown from Pantheon-OS selectively;
- keep `docs/governance/AGENTS.md` as the single canonical Pantheon Role registry;
- avoid governance duplication in Hermes profile folders;
- add glossary and simplification plan;
- add STATUS and governance README index.

Required files:

- `docs/governance/AGENTS.md`;
- `docs/governance/ARCHITECTURE.md`;
- `docs/governance/MODULES.md`;
- `docs/governance/APPROVALS.md`;
- `docs/governance/TASK_CONTRACTS.md`;
- `docs/governance/TASK_CONTRACT_REVISIONS.md`;
- `docs/governance/EVIDENCE_PACK.md`;
- `docs/governance/MEMORY.md`;
- `docs/governance/MEMORY_EVENT_SCHEMA.md`;
- `docs/governance/ROLE_SIGNALS.md`;
- `docs/governance/WORKFLOW_SCHEMA.md`;
- `docs/governance/WORKFLOW_ADAPTATION.md`;
- `docs/governance/SKILL_LIFECYCLE.md`;
- `docs/governance/RUN_GRAPH.md`;
- `docs/governance/EXECUTION_DISCIPLINE.md`;
- `docs/governance/MODEL_ROUTING_POLICY.md`;
- `docs/governance/ROUTING_FOUNDATION.md`;
- `docs/governance/HERMES_INTEGRATION.md`;
- `docs/governance/OPENWEBUI_INTEGRATION.md`;
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`;
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`;
- `docs/governance/GLOSSARY.md`;
- `docs/governance/REPOSITORY_SIMPLIFICATION_PLAN.md`;
- `docs/governance/STATUS.md`;
- `docs/governance/README.md`.

## Phase 2 — Hermes profile templates

Status: partial.

Goals:

- add lightweight Hermes profile templates;
- keep profiles candidate-only;
- avoid per-profile `governance.md` files;
- avoid automatic Hermes installation;
- bind each profile to `docs/governance/AGENTS.md`.

Profile structure:

```text
hermes/profiles/<profile>/
  README.md
  profile.yaml
  soul.md
```

Profiles:

- `athena`;
- `argos`;
- `themis`;
- `apollo`;
- `zeus`;
- `iris`;
- `hephaistos`.

## Phase 3 — Schemas and examples

Status: not implemented.

Goals:

- migrate schema files;
- migrate schema examples;
- ensure every `governance_refs` entry resolves to an existing governance document;
- keep schemas aligned with canonical Markdown.

Core schemas:

- `task_contract.schema.yaml`;
- `task_contract_revision.schema.yaml`;
- `evidence_pack.schema.yaml`;
- `memory_candidate.schema.yaml`;
- `role_signal.schema.yaml`;
- `workflow_manifest.schema.yaml`;
- `skill_manifest.schema.yaml`.

## Phase 4 — Read-only tooling

Status: not implemented.

Goals:

- migrate read-only doctor checks;
- migrate governance validators;
- add fast standalone tests;
- avoid FastAPI, DB, queues, schedulers or runtime endpoints in this phase.

Allowed:

- `operations/doctor.py`;
- `operations/doctor.md`;
- `operations/validate_governance.py`;
- `tests/test_doctor_readonly.py`;
- `tests/test_governance_schemas.py`.

Not allowed in this phase:

- execution endpoints;
- provider routing runtime;
- hidden workflow execution;
- automatic profile installation;
- memory promotion automation.

## Phase 5 — Context packs and integration specs

Status: not implemented.

Goals:

- define Hermes context pack verification;
- define OpenWebUI display/action boundaries;
- keep all integration specs governance-only unless explicitly approved.

Allowed:

- context-pack specifications;
- OpenWebUI action display specifications;
- Hermes Task Contract bridge specifications.

Not allowed:

- OpenWebUI as canonical memory;
- OpenWebUI as runtime;
- Pantheon as execution backend;
- Hermes bypassing Pantheon approvals.

## Phase 6 — Optional read-only Domain API

Status: deferred.

A read-only Domain API may be reconsidered later.

Allowed scope if approved:

- governance snapshot;
- context pack export;
- role registry read;
- schema read;
- policy read.

Forbidden scope:

- `/run`;
- `/execute`;
- `/agent`;
- `/workflow/start`;
- `/tool`;
- `/memory/promote`;
- provider routing;
- scheduling;
- queueing.

## Migration policy

Pantheon-OS remains the historical source repository.

Pantheon-Next migrates selectively:

- governance Markdown;
- schemas;
- schema examples;
- AI logs;
- read-only validation tooling;
- governance tests;
- context-pack specifications.

Pantheon-Next does not bulk-copy runtime-oriented folders from Pantheon-OS.

## Current risks

- `STATUS.md` is not yet present;
- governance documents are still incomplete;
- schemas are not yet migrated;
- tests are not yet present;
- Hermes profile coverage is still incomplete;
- `AGENTS.md` must remain aligned with every `profile.yaml`.
