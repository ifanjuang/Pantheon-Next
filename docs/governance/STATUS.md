# Pantheon Next Status

Status date: 2026-05-14

Pantheon Next is under controlled bootstrap, conceptual stabilization and selective distillation from Pantheon-OS.

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

The repository baseline, governance structure, Hermes profile strategy, conceptual stabilization layer, memory doctrine, evidence doctrine, approval doctrine and narrative layer are now stabilized at documentation level.

Migration from Pantheon-OS remains incomplete.

Future recovery from Pantheon-OS must use distillation, not bulk migration.

Default rule:

```text
do not migrate unless governance value is proven
```

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
- `ai_logs/README.md`.

### AI intervention logs

Implemented logs include:

- bootstrap and governance reconciliation logs from 2026-05-12;
- conceptual stabilization guardrail log;
- task contract stabilization log when present;
- evidence, memory, approval and role semantics stabilization logs;
- narrative and visual layer integration log when present.

### Active governance documents

Canonical or active governance documents:

- `docs/governance/README.md`;
- `docs/governance/STATUS.md`;
- `docs/governance/ROADMAP.md`;
- `docs/governance/AGENTS.md`;
- `docs/governance/GLOSSARY.md`;
- `docs/governance/REPOSITORY_SIMPLIFICATION_PLAN.md`;
- `docs/governance/EXTERNAL_AI_OPTION_REVIEWS.md`;
- `docs/governance/CONCEPTUAL_STABILIZATION.md`;
- `docs/governance/TASK_CONTRACTS.md`;
- `docs/governance/EVIDENCE_PACK.md`;
- `docs/governance/MEMORY.md`;
- `docs/governance/APPROVALS.md`.

### Active narrative and visual support documents

These documents are active explanatory doctrine.

They do not define implementation or runtime behavior.

- `docs/governance/NARRATIVE.md`;
- `docs/governance/VISUAL_LANGUAGE.md`.

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

Hermes profiles remain candidate-only execution templates.

They are not installed, deployed or executed by Pantheon Next.

## Stub present — non implemented

The following files exist as governance placeholders only.

They are not migrated doctrine yet.

They must not be treated as canonical implementation.

### Governance doctrine stubs

- `docs/governance/ARCHITECTURE.md`;
- `docs/governance/MODULES.md`;
- `docs/governance/TASK_CONTRACT_REVISIONS.md`;
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

## Absent or not reconciled in this intervention

### Schemas

Schemas are not reconciled in this status pass.

Earlier repository search did not find schema files.

Required or expected schema area remains:

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

Read-only tooling is not migrated in this phase.

Required or expected area remains:

- `operations/doctor.md`;
- `operations/doctor.py`;
- `operations/validate_governance.py`.

### Tests

Tests are not implemented in this phase.

Required or expected area remains:

- `tests/test_doctor_readonly.py`;
- `tests/test_governance_schemas.py`.

## Voluntarily not implemented

The following are intentionally absent:

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

## Narrative status

The city-game metaphor is active as explanatory doctrine.

It must remain non-runtime.

It must not redefine Pantheon as a game engine, hidden workflow runner, autonomous city or agent runtime.

The preferred first-reading companion set is:

- Athena structures;
- Argos retrieves;
- Themis verifies;
- Apollo clarifies;
- Hephaistos fabricates;
- Iris transmits;
- Zeus arbitrates.

Iris is preferred for narrative transmission to avoid confusion with Hermes Agent, which remains the external execution runtime.

Mnemosyne may appear as a memory figure in visual language, but she is not a canonical Pantheon Role unless `AGENTS.md` is explicitly updated.

## Key risks

- governance migration remains incomplete;
- stubs may be mistaken for migrated doctrine;
- schemas are not reconciled here;
- tests are not implemented yet;
- read-only operations tooling is not migrated yet;
- future migrations may accidentally reintroduce runtime-oriented architecture;
- narrative metaphors may be misread as implementation semantics.

## Next required action

Continue Phase S stabilization before further Pantheon-OS recovery:

- stabilize workflow language without creating execution semantics;
- distinguish Workflow Manifest from runtime graph;
- review `RUN_GRAPH.md` and likely demote, rewrite or reject runtime semantics;
- then reconsider schemas under the protected-file rule.
