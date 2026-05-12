# Pantheon Next Status

Status date: 2026-05-12

Pantheon Next is under controlled bootstrap and migration from Pantheon-OS.

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next is a governance-first repository with minimal read-only tooling.

Pantheon Next is not an execution runtime.

## Current repository posture

Status: partial.

The repository has been initialized and is being built as a clean governance-first baseline.

Runtime-oriented historical components from Pantheon-OS are not migrated by default.

## Implemented

### Root repository baseline

- `README.md`: implemented;
- `CLAUDE.md`: implemented;
- `.gitignore`: implemented;
- `pyproject.toml`: implemented;
- `LICENSE`: implemented;
- `VERSION`: implemented;
- `CHANGELOG.md`: implemented;
- `legacy/README.md`: implemented;
- `ai_logs/2026-05-12-pantheon-next-bootstrap.md`: implemented.

### Governance documents

- `docs/governance/AGENTS.md`: implemented;
- `docs/governance/ROADMAP.md`: implemented.

### Hermes profile templates

- `hermes/README.md`: implemented;
- `hermes/profiles/README.md`: implemented;
- `hermes/profiles/_base/README.md`: implemented;
- `hermes/profiles/_base/base-soul-rules.md`: implemented;
- `hermes/profiles/athena/README.md`: implemented;
- `hermes/profiles/athena/profile.yaml`: implemented;
- `hermes/profiles/athena/soul.md`: implemented;
- `hermes/profiles/argos/README.md`: implemented;
- `hermes/profiles/argos/profile.yaml`: implemented;
- `hermes/profiles/argos/soul.md`: implemented;
- `hermes/profiles/themis/README.md`: implemented;
- `hermes/profiles/themis/profile.yaml`: implemented;
- `hermes/profiles/themis/soul.md`: implemented;
- `hermes/profiles/apollo/README.md`: implemented;
- `hermes/profiles/apollo/profile.yaml`: implemented;
- `hermes/profiles/apollo/soul.md`: implemented;
- `hermes/profiles/zeus/README.md`: implemented;
- `hermes/profiles/zeus/profile.yaml`: implemented;
- `hermes/profiles/zeus/soul.md`: implemented.

## Partially implemented

### Hermes profile coverage

The following role profiles remain incomplete:

- `iris`;
- `hephaistos`.

### Governance baseline

The governance baseline is not complete yet.

Required but not yet migrated:

- `docs/governance/README.md`;
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
- `docs/governance/REPOSITORY_SIMPLIFICATION_PLAN.md`.

## Non implemented

### Schemas

Schemas are not migrated yet.

Required:

- `schemas/README.md`;
- `schemas/task_contract.schema.yaml`;
- `schemas/task_contract_revision.schema.yaml`;
- `schemas/evidence_pack.schema.yaml`;
- `schemas/memory_candidate.schema.yaml`;
- `schemas/role_signal.schema.yaml`;
- `schemas/workflow_manifest.schema.yaml`;
- `schemas/skill_manifest.schema.yaml`;
- `schemas/examples/`.

### Operations

Read-only operations are not migrated yet.

Required:

- `operations/doctor.md`;
- `operations/doctor.py`;
- `operations/validate_governance.py`.

### Tests

Tests are not implemented yet.

Required:

- `tests/test_doctor_readonly.py`;
- `tests/test_governance_schemas.py`.

## Voluntarily not implemented

The following are intentionally absent in the current phase:

- autonomous execution runtime;
- agent runtime inside Pantheon Next;
- tool runtime;
- provider router;
- scheduler;
- queue;
- message bus;
- central LangGraph runtime;
- automatic Hermes profile installation;
- automatic skill installation;
- auto-promoted memory;
- hidden workflow runtime;
- Docker stack;
- FastAPI runtime endpoint.

## Deferred

### Read-only Domain API

A read-only Domain API is deferred.

It may be reconsidered later if it remains limited to governance exposure only.

Allowed future scope:

- governance snapshot;
- context pack export;
- role registry read;
- schema read;
- policy read.

Forbidden scope:

- execution;
- tool calling;
- workflow start;
- memory promotion;
- provider routing;
- scheduling;
- queueing.

## Canonical naming

Current canonical profile identifiers:

- `athena-agent`;
- `argos-agent`;
- `themis-agent`;
- `apollo-agent`;
- `zeus-agent`;
- `iris-agent`;
- `hephaistos-agent`.

The canonical spelling is `HEPHAISTOS` / `hephaistos-agent`.

The spelling `HEPHAESTUS` / `hephaestus-agent` is not canonical for Pantheon Next phase 1.

## Key risks

- Governance documents are still incomplete.
- Schemas are still absent.
- Schema `governance_refs` cannot be validated until governance docs and schemas are both migrated.
- Hermes profiles currently reference `docs/governance/AGENTS.md`, which now exists, but full role doctrine remains minimal.
- Read-only doctor and validator are not yet present.
- Tests are not yet present.

## Next required action

Complete Hermes profile coverage by adding:

- `hermes/profiles/iris/README.md`;
- `hermes/profiles/iris/profile.yaml`;
- `hermes/profiles/iris/soul.md`;
- `hermes/profiles/hephaistos/README.md`;
- `hermes/profiles/hephaistos/profile.yaml`;
- `hermes/profiles/hephaistos/soul.md`.
