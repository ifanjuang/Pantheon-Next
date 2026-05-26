# Pantheon Next Status

Status date: 2026-05-27

Pantheon Next is under controlled bootstrap, conceptual stabilization and selective distillation from Pantheon-OS.

## Doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next is a governance-first repository.

Pantheon Next is not an execution runtime.

It does not implement an agent loop, tool runtime, provider router, scheduler, queue, message bus, hidden workflow runner, automatic approval system or automatic memory promotion.

## Current repository posture

Status: partial but structurally coherent.

The repository now contains:

- a public README and French README positioned around professional dossier flow;
- a governance Markdown baseline;
- migrated Pantheon-OS architecture, modules, post-pivot code audit, Task Contract revision, execution discipline and Role Signal doctrine;
- active conceptual doctrine for roles, approvals, evidence, memory, workflows, integrations, knowledge, scope isolation and governed context packaging;
- active module-activation support doctrine for detected, enabled and task-authorized capabilities;
- active support doctrine for narrative, product positioning, visual language and external inspirations;
- active external-reference governance support for watchlists, boundaries, ecosystem mapping, reference reviews, distillation, rejection memory, method review and persistent tensions;
- seven lightweight Hermes profile templates;
- one Hermes runtime candidate template for LangGraph;
- an initial schema baseline;
- fictional professional examples.

Migration from Pantheon-OS remains incomplete.

Future recovery from Pantheon-OS must use distillation, not bulk migration.

Default rule:

```text
do not migrate unless governance value is proven
```

## Migrated from Pantheon-OS

The following documents are migrated doctrine, not stubs:

- `docs/governance/ARCHITECTURE.md`;
- `docs/governance/MODULES.md`;
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`;
- `docs/governance/TASK_CONTRACT_REVISIONS.md`;
- `docs/governance/EXECUTION_DISCIPLINE.md`;
- `docs/governance/ROLE_SIGNALS.md`.

These documents describe governance structure, migration posture, audit discipline, contract lifecycle doctrine, contribution discipline and role-signal doctrine only.

They do not implement execution, provider routing, scheduling, queueing, Docker, endpoints, schemas, tests or operations tooling.

## Active governance documents

Canonical or active governance documents:

- `docs/governance/README.md`;
- `docs/governance/STATUS.md`;
- `docs/governance/ROADMAP.md`;
- `docs/governance/MIGRATION_PLAYBOOK.md`;
- `docs/governance/ARCHITECTURE.md`;
- `docs/governance/MODULES.md`;
- `docs/governance/MODULE_ACTIVATION.md`;
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`;
- `docs/governance/TASK_CONTRACT_REVISIONS.md`;
- `docs/governance/EXECUTION_DISCIPLINE.md`;
- `docs/governance/ROLE_SIGNALS.md`;
- `docs/governance/AGENTS.md`;
- `docs/governance/GOVERNANCE_COLLEGE.md`;
- `docs/governance/USER_DECISION_GATE.md`;
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
- `docs/governance/MARKDOWN_DOSSIER_WORKFLOW.md`;
- `docs/governance/RAG_INGESTION_PIPELINE.md`;
- `docs/governance/HERMES_INTEGRATION.md`;
- `docs/governance/OPENWEBUI_INTEGRATION.md`;
- `docs/governance/EXTERNAL_TOOLS_POLICY.md`;
- `docs/governance/KNOWLEDGE_TAXONOMY.md`;
- `docs/governance/SCOPE_ISOLATION.md`;
- `docs/governance/CONTEXT_PACKS.md`.

These documents are governance doctrine, conceptual stabilization, integration boundary doctrine or activation semantics.

They do not create runtime behavior by themselves.

### Module activation doctrine

`MODULE_ACTIVATION.md` defines detection, governance activation, task authorization, status vocabulary, activation scope, mandatory rules, optional rules and Effective Policy semantics.

It is support doctrine for a future UI that may enable, disable, suspend or review capability use.

It does not implement:

- UI;
- module registry;
- plugin loader;
- skill installer;
- runtime;
- scheduler;
- queue;
- provider router;
- approval engine;
- memory engine.

Core rule:

```text
Detected does not mean enabled.
Enabled does not mean authorized for a task.
Authorized for a task does not mean sovereign.
```

## Active support documents

Active product, editorial, narrative, visual, example, inspiration and external-reference support documents:

- `docs/governance/PRODUCT_DIFFERENTIATION.md`;
- `docs/governance/EDITORIAL_LANGUAGE.md`;
- `docs/governance/NARRATIVE.md`;
- `docs/governance/VISUAL_LANGUAGE.md`;
- `docs/governance/EXTERNAL_REPO_INSPIRATIONS.md`;
- `docs/governance/EXTERNAL_AGENTIC_INSPIRATIONS.md`;
- `docs/governance/reference_reviews/README.md`;
- `docs/governance/reference_reviews/LANGGRAPH.md`;
- `docs/governance/WATCHLIST.md`;
- `docs/governance/REFERENCE_BOUNDARIES.md`;
- `docs/governance/ECOSYSTEM_MAP.md`;
- `docs/governance/DISTILLATION_REGISTRY.md`;
- `docs/governance/REJECTED_PATTERNS.md`;
- `docs/governance/EXTERNAL_METHOD_REVIEWS.md`;
- `docs/governance/TENSIONS_AND_RISKS.md`;
- `docs/governance/SKILL_WATCHLIST.md`;
- `docs/examples/README.md`.

These documents support product explanation, practitioner readability, examples, visual language, external pattern distillation, reference boundary control, method review and risk memory.

They do not approve integrations, install skills, add dependencies, define a plugin registry, define a marketplace, authorize tools or implement runtime behavior.

### External-reference support chain

The external-reference support documents are organized as:

```text
observe      → WATCHLIST.md and SKILL_WATCHLIST.md
understand   → REFERENCE_BOUNDARIES.md, ECOSYSTEM_MAP.md and reference_reviews/
decide       → DISTILLATION_REGISTRY.md, REJECTED_PATTERNS.md and EXTERNAL_METHOD_REVIEWS.md
preserve     → TENSIONS_AND_RISKS.md
```

This chain is documentation-level governance only.

It does not create dependency adoption, vendor endorsement, runtime migration, automatic skill installation, MCP routing, observability backend, GraphRAG runtime, LangGraph runtime, automatic approval or automatic memory promotion.

## Hermes profile templates

Implemented candidate-only Hermes profile templates:

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
- `hermes/profiles/_base/base-soul-rules.md`;
- `hermes/profiles/_base/LANGGRAPH_RUNTIME_CANDIDATE.md`.

Hermes profiles and runtime candidate templates remain candidate-only execution documentation.

They are not installed, deployed or executed by Pantheon Next.

They do not approve, govern, promote memory or become canonical doctrine.

## Schema baseline

Status: initial schema baseline present, not yet backed by repository tests.

Implemented schema files:

- `schemas/README.md`;
- `schemas/task_contract.schema.yaml`;
- `schemas/task_contract_revision.schema.yaml`;
- `schemas/evidence_pack.schema.yaml`;
- `schemas/memory_candidate.schema.yaml`;
- `schemas/role_signal.schema.yaml`;
- `schemas/workflow_manifest.schema.yaml`;
- `schemas/skill_manifest.schema.yaml`;
- `schemas/examples/`.

Schemas are validation contracts only.

They do not execute workflows, run tools, install Hermes profiles, route providers, schedule jobs, promote memory or mutate governance state.

Remaining schema work:

- reconcile schema fields against the latest Markdown doctrine;
- verify all `governance_refs` resolve to active documents or explicit stubs;
- add read-only schema validation tests;
- keep schemas protected under the confirmation rule for future edits.

## Stub present - non implemented

The following files exist as governance placeholders or unreconciled migration targets.

They are not migrated doctrine yet.

They must not be treated as canonical implementation.

- `docs/governance/MODEL_ROUTING_POLICY.md`;
- `docs/governance/ROUTING_FOUNDATION.md`;
- `docs/governance/MEMORY_EVENT_SCHEMA.md`;
- `docs/governance/WORKFLOW_ADAPTATION.md`;
- `docs/governance/SKILL_LIFECYCLE.md`;
- `docs/governance/ROLE_SIGNAL_PROFILES.md`;
- `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`;
- `docs/governance/OPENWEBUI_PLUGIN_POLICY.md`;
- `docs/governance/EPISTEMIC_CONTROL.md`;
- `docs/governance/EPISTEMIC_CONTROL_PROPAGATION.md`;
- `docs/governance/EXTERNAL_RUNTIME_OPTIONS.md`;
- `docs/assets/README.md`.

## Absent implementation areas

### Operations

Read-only tooling is not implemented in Pantheon Next yet.

Expected area:

- `operations/doctor.md`;
- `operations/doctor.py`;
- `operations/validate_governance.py`.

### Tests

Tests are not implemented in Pantheon Next yet.

Expected area:

- `tests/test_doctor_readonly.py`;
- `tests/test_governance_schemas.py`.

## Voluntarily not implemented

The following remain intentionally absent from Pantheon Next:

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
- skill marketplace;
- plugin manager;
- MCP server layer;
- observability backend;
- GraphRAG runtime;
- auto-promoted memory;
- hidden workflow runtime;
- autonomous debate runtime;
- automatic approval system;
- modular UI implementation;
- module registry runtime;
- module Effective Policy engine;
- automatic module detection monitor;
- automatic module activation;
- module plugin loader;
- Markdown editor runtime;
- OpenWebUI plugin implementation;
- OpenWebUI Knowledge gateway implementation;
- direct Hermes bridge to OpenWebUI database or vector store;
- Hermes tool implementation for Markdown dossiers;
- Docker runtime stack;
- FastAPI execution endpoint;
- PDF parsing runtime;
- OCR runtime;
- ingestion scheduler;
- automatic OpenWebUI import pipeline;
- Postgres registry writer;
- automatic Evidence Candidate writer;
- automatic document-to-memory pipeline;
- product configuration runtime;
- OpenWebUI auto-configuration engine;
- Hermes auto-configuration engine;
- Context Pack runtime;
- automatic Context Pack generator;
- automatic Context Pack importer;
- hidden Context Pack prompt authority;
- Context Pack executor;
- automatic context-to-memory promotion;
- external reference adoption engine;
- automatic Watchlist monitor;
- dependency adoption automation;
- skill watch importer;
- reference scoring backend;
- external method runner;
- rejected-pattern enforcement runtime;
- tensions risk engine;
- Setup Doctor implementation;
- audit-ready export implementation.

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

Non-canonical spelling:

```text
HEPHAESTUS
hephaestus-agent
```

## Key risks

- governance migration remains incomplete;
- stubs may be mistaken for migrated doctrine;
- active integration documents may be mistaken for implemented integrations;
- schema presence may be mistaken for tested validation coverage;
- examples may be mistaken for professional advice or implemented workflows;
- Governance College doctrine may be mistaken for a multi-agent runtime;
- User Decision Gate doctrine may be mistaken for an automatic approval loop;
- Task Contract revision doctrine may be mistaken for automatic workflow resume;
- Execution discipline may be mistaken for an internal execution engine;
- Role Signals may be mistaken for an agent message bus or hidden debate runtime;
- Context Packs may be mistaken for Canonical Memory, Evidence Packs, approvals, Task Contracts or runtime state;
- Module Activation doctrine may be mistaken for an implemented UI, plugin manager, module registry or runtime policy engine;
- Effective Policy examples may be mistaken for executable policy enforcement;
- tool-specific adapters such as `CLAUDE.md`, ChatGPT project instructions, OpenWebUI prompts or Hermes notes may be mistaken for canonical doctrine;
- external-reference support documents may be mistaken for dependency adoption, framework endorsement or runtime migration;
- Watchlist may be mistaken for an implementation backlog;
- Distillation Registry may be mistaken for approval to implement;
- Rejected Patterns may be mistaken for an automatic enforcement engine;
- External Method Reviews may be mistaken for hidden method orchestration;
- Tensions and Risks may be mistaken for a risk-scoring backend;
- Skill Watchlist may be mistaken for a skill marketplace or approval list;
- Markdown dossier workflow may be mistaken for an implemented editor or runtime;
- RAG ingestion pipeline may be mistaken for an implemented parser, importer or indexing runtime;
- governed OpenWebUI Knowledge handoff may be mistaken for an implemented gateway;
- Hermes may be accidentally granted broad OpenWebUI Knowledge or database access in future implementation;
- scope isolation may be mistaken for runtime-enforced partitioning;
- read-only operations tooling and tests are not implemented yet;
- future migrations may accidentally reintroduce runtime-oriented architecture.

## Next required action

Continue from the reconciled state:

1. continue controlled migration one file at a time under `MIGRATION_PLAYBOOK.md`;
2. reconcile schemas against the active Markdown doctrine under the protected-file rule;
3. add read-only operations tooling only after the governance targets are stable;
4. add tests for schema validation and read-only Doctor behavior;
5. keep OpenWebUI exposure, Hermes execution and Pantheon governance separated in every future implementation proposal;
6. use the external-reference support chain to observe, bound, distill, reject or preserve external inspirations without importing runtime responsibility;
7. use `MODULE_ACTIVATION.md` when designing future UI controls for detected, enabled or task-authorized capabilities.