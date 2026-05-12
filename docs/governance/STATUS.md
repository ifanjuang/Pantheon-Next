# Pantheon Next Status

Status date: 2026-05-12

Pantheon Next is under controlled bootstrap and selective migration from Pantheon-OS.

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next is a governance-first repository.

Pantheon Next is not an execution runtime.

## Repository posture

Status: partial but structurally coherent.

The repository baseline, governance structure and Hermes profile strategy are now stabilized.

Migration from Pantheon-OS remains incomplete.

## Implemented

### Repository baseline

- `README.md`;
- `CLAUDE.md`;
- `.gitignore`;
- `pyproject.toml`;
- `LICENSE`;
- `VERSION`;
- `CHANGELOG.md`;
- `legacy/README.md`;
- `ai_logs/README.md`;
- `ai_logs/2026-05-12-pantheon-next-bootstrap.md`;
- `ai_logs/2026-05-12-governance-md-bootstrap-reconcile.md`;
- `ai_logs/2026-05-12-status-index-changelog-reconcile.md`;
- `ai_logs/2026-05-12-p0-6-read-order-stubs.md`;
- `ai_logs/2026-05-12-p0-7-hermes-iris-hephaistos.md`;
- `ai_logs/2026-05-12-p0-6c-governance-safety-stubs.md`;
- `ai_logs/2026-05-12-p0-6d-ecosystem-stubs.md`.

### Governance documents

Canonical or active governance documents:

- `docs/governance/README.md`;
- `docs/governance/STATUS.md`;
- `docs/governance/ROADMAP.md`;
- `docs/governance/AGENTS.md`;
- `docs/governance/GLOSSARY.md`;
- `docs/governance/REPOSITORY_SIMPLIFICATION_PLAN.md`;
- `docs/governance/EXTERNAL_AI_OPTION_REVIEWS.md`.

### Hermes profile templates

Implemented profiles:

- `athena-agent`;
- `argos-agent`;
- `themis-agent`;
- `apollo-agent`;
- `zeus-agent`;
- `iris-agent`;
- `hephaistos-agent`.

Implemented shared structure:

- `hermes/README.md`;
- `hermes/profiles/README.md`;
- `hermes/profiles/_base/README.md`;
- `hermes/profiles/_base/base-soul-rules.md`.

## Stub present — non implemented

The following files exist as governance placeholders only.

They are not migrated doctrine yet.

They must not be treated as canonical implementation.

### Governance doctrine stubs

- `docs/governance/ARCHITECTURE.md`;
- `docs/governance/MODULES.md`;
- `docs/governance/APPROVALS.md`;
- `docs/governance/TASK_CONTRACTS.md`;
- `docs/governance/TASK_CONTRACT_REVISIONS.md`;
- `docs/governance/EVIDENCE_PACK.md`;
- `docs/governance/MEMORY.md`;
- `docs/governance/RUN_GRAPH.md`;
- `docs/governance/EXECUTION_DISCIPLINE.md`;
- `docs/governance/MODEL_ROUTING_POLICY.md`;
- `docs/governance/ROUTING_FOUNDATION.md`;
- `docs/governance/HERMES_INTEGRATION.md`;
- `docs/governance/OPENWEBUI_INTEGRATION.md`;
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`;
- `docs/governance/KNOWLEDGE_TAXONOMY.md`;
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`;
- `docs/governance/MEMORY_EVENT_SCHEMA.md`;
- `docs/governance/ROLE_SIGNALS.md`;
- `docs/governance/WORKFLOW_SCHEMA.md`;
- `docs/governance/WORKFLOW_ADAPTATION.md`;
- `docs/governance/SKILL_LIFECYCLE.md`;
- `docs/governance/REQUEST_ORCHESTRATION.md`;
- `docs/governance/ROLE_SIGNAL_PROFILES.md`;
- `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`;
- `docs/governance/OPENWEBUI_PLUGIN_POLICY.md`;
- `docs/governance/EPISTEMIC_CONTROL.md`;
- `docs/governance/EPISTEMIC_CONTROL_PROPAGATION.md`;
- `docs/governance/EXTERNAL_RUNTIME_OPTIONS.md`;
- `docs/assets/README.md`.

## Absent

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

Read-only tooling is not migrated yet.

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

The following are intentionally absent in phase 1:

- autonomous execution runtime;
- internal Pantheon agent runtime;
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
- Docker runtime stack;
- FastAPI execution endpoint.

## Deferred

### Optional read-only Domain API

A governance-only read API may be reconsidered later.

Allowed future scope:

- governance snapshot;
- context-pack export;
- role registry read;
- schema read;
- policy read.

Forbidden scope:

- execution;
- workflow start;
- tool runtime;
- provider routing;
- memory promotion;
- scheduling;
- queueing.

## Canonical naming

Canonical identifiers:

- `athena-agent`;
- `argos-agent`;
- `themis-agent`;
- `apollo-agent`;
- `zeus-agent`;
- `iris-agent`;
- `hephaistos-agent`.

Canonical spelling:

```text
HEPHAISTOS
hephaistos-agent
```

Non canonical spelling:

```text
HEPHAESTUS
hephaestus-agent
```

## Key risks

- governance migration remains incomplete;
- stubs may be mistaken for migrated doctrine;
- schemas are not migrated yet;
- tests are not implemented yet;
- read-only operations tooling is not migrated yet;
- future migrations may accidentally reintroduce runtime-oriented architecture.

## Next required action

Prepare controlled migration from Pantheon-OS:

- migrate schemas under review;
- migrate read-only operations tooling under review;
- add tests for schemas and doctor tooling.
