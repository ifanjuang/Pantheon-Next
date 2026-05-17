# Pantheon Next Status

Status date: 2026-05-17

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

The repository baseline, governance structure, Hermes profile strategy, conceptual stabilization layer, memory doctrine, evidence doctrine, approval doctrine, role semantics, narrative layer, workflow vocabulary, integration boundary doctrine, external tools policy, knowledge taxonomy, scope isolation doctrine and Markdown dossier workflow doctrine are now stabilized at documentation level.

Migration from Pantheon-OS remains incomplete.

Future recovery from Pantheon-OS must use distillation, not bulk migration.

Default rule:

```text
do not migrate unless governance value is proven
```

## Implemented

### Repository baseline

- `README.md`;
- `README.fr.md`;
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
- evidence, memory, approval and role semantics stabilization logs;
- narrative and visual layer integration log;
- workflow language stabilization log when present;
- integration, knowledge taxonomy and scope isolation stabilization log when present;
- README front-door and visual reading path refactor log;
- Markdown dossier workflow governance proposal log when present.

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
- `docs/governance/APPROVALS.md`;
- `docs/governance/WORKFLOW_SCHEMA.md` (`Workflow Manifest`);
- `docs/governance/RUN_GRAPH.md` (`Run Trace View`);
- `docs/governance/REQUEST_ORCHESTRATION.md` (`Request Coordination`);
- `docs/governance/MARKDOWN_DOSSIER_WORKFLOW.md` (`Markdown Dossier Workflow`);
- `docs/governance/HERMES_INTEGRATION.md`;
- `docs/governance/OPENWEBUI_INTEGRATION.md`;
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`;
- `docs/governance/KNOWLEDGE_TAXONOMY.md`;
- `docs/governance/SCOPE_ISOLATION.md`.

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

## Workflow stabilization status

Workflow vocabulary is now active only as governance vocabulary.

`WORKFLOW_SCHEMA.md` defines a `Workflow Manifest`.

A Workflow Manifest is a reusable governance declaration.

It is not an execution graph, scheduler, queue definition or hidden orchestration layer.

`RUN_GRAPH.md` defines a `Run Trace View`.

A Run Trace View is a human-readable evidence and review trace.

It is not runtime state, a graph executor, an observability backend or a resume mechanism.

`REQUEST_ORCHESTRATION.md` defines `Request Coordination`.

Request Coordination is governance intake, review sequencing and escalation guidance.

It is not runtime orchestration, worker coordination, queue management or provider routing.

`MARKDOWN_DOSSIER_WORKFLOW.md` defines `Markdown Dossier Workflow`.

A Markdown Dossier Workflow is a governance proposal for progressively producing professional Markdown dossiers with inline comments, source discipline, selected-zone operations, coherence review, versioning and validation thresholds.

It is not a Markdown editor, OpenWebUI plugin, Hermes tool, workflow runtime, scheduler, queue, provider router or automatic memory system.

## Integration, knowledge and scope stabilization status

Integration vocabulary is now active only as governance vocabulary.

`HERMES_INTEGRATION.md` defines the external execution boundary.

Hermes Agent may execute under Task Contract and return Evidence Packs, Patch Candidates, outputs and Memory Candidates.

Hermes Agent does not canonize memory, approve itself or become Pantheon doctrine.

`OPENWEBUI_INTEGRATION.md` defines the cockpit and exposure boundary.

OpenWebUI may expose chat, Knowledge Bases, results, approvals, Evidence Packs and user actions.

OpenWebUI does not become Canonical Memory, a source of truth, a runtime or an approval authority.

`EXTERNAL_TOOLS_POLICY.md` defines external capability governance.

External tools are governed capabilities, not a plugin manager, hidden runtime or free execution layer.

`KNOWLEDGE_TAXONOMY.md` separates Raw Source, Knowledge Item, Retrieved Knowledge, Working Context, Evidence, Memory Candidate, Canonical Memory, Doctrine and Runtime State.

`SCOPE_ISOLATION.md` defines scope compartmentalization and the no-global-memory-by-default rule.

These documents are documentation-level governance doctrine.

They do not implement runtime integration, provider routing, plugin management, automatic memory promotion or runtime-enforced partitioning.

## Stub present — non implemented

The following files exist as governance placeholders only.

They are not migrated doctrine yet.

They must not be treated as canonical implementation.

### Governance doctrine stubs

- `docs/governance/ARCHITECTURE.md`;
- `docs/governance/MODULES.md`;
- `docs/governance/TASK_CONTRACT_REVISIONS.md`;
- `docs/governance/EXECUTION_DISCIPLINE.md`;
- `docs/governance/MODEL_ROUTING_POLICY.md`;
- `docs/governance/ROUTING_FOUNDATION.md`;
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`;
- `docs/governance/MEMORY_EVENT_SCHEMA.md`;
- `docs/governance/ROLE_SIGNALS.md`;
- `docs/governance/WORKFLOW_ADAPTATION.md`;
- `docs/governance/SKILL_LIFECYCLE.md`;
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
- Markdown editor runtime;
- OpenWebUI plugin implementation;
- Hermes tool implementation for Markdown dossiers;
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

### Markdown dossier workflow implementation

A future implementation path may be considered outside Pantheon runtime scope.

Allowed future posture:

- OpenWebUI exposes the document surface, selections, actions, comments, diffs and approvals;
- Hermes Agent or another external execution layer performs edits, source checks, coherence reviews and patch candidates under Task Contract;
- Pantheon governs annotations, evidence discipline, approval thresholds, versioning and memory proposal rules.

Forbidden future posture:

- Pantheon implements the editor runtime;
- Pantheon silently rewrites documents;
- Pantheon auto-promotes memory;
- OpenWebUI becomes source of truth;
- Hermes self-approves edits or memory.

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
- active integration documents may be mistaken for implemented integrations if documentation status is ignored;
- Markdown dossier workflow may be mistaken for an implemented editor or runtime;
- scope isolation may be mistaken for runtime-enforced partitioning;
- OpenWebUI folder scope or Notes may be mistaken for Canonical Memory;
- schemas are not reconciled here;
- tests are not implemented yet;
- read-only operations tooling is not migrated yet;
- future migrations may accidentally reintroduce runtime-oriented architecture;
- narrative metaphors may be misread as implementation semantics;
- workflow documents may still be misread as runtime documents if their canonical concepts are ignored.

## Next required action

Continue Phase S stabilization before further Pantheon-OS recovery:

- reconcile `ARCHITECTURE.md` as governance architecture, not runtime architecture;
- reconcile `MODULES.md` as governance module map, not implementation module registry;
- review `CODE_AUDIT_POST_PIVOT.md` against the post-pivot doctrine;
- then reconsider schemas under the protected-file rule;
- if Markdown dossier workflow is pursued, first design a governance-only example dossier and avoid implementing runtime behavior in Pantheon.
