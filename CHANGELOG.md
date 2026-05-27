# Changelog

## 0.1.9 - 2026-05-27

Role, domain and skill activation doctrine.

### Added

- `docs/governance/ROLE_ACTIVATION.md` as support doctrine for Pantheon Role activation, professional domain packs and Hermes skill candidates;
- role statuses such as `active`, `standby`, `disabled_by_user`, `mandatory_for_risk`, `blocked` and `suspended`;
- domain statuses such as `candidate`, `sandbox_enabled`, `project_enabled`, `dossier_enabled`, `domain_enabled`, `suspended` and `rejected`;
- skill statuses such as `detected`, `candidate`, `sandbox_enabled`, `project_enabled`, `task_authorized`, `suspended` and `rejected`;
- Zeus Role Readiness Brief format;
- mandatory role reactivation triggers;
- architecture domain pack example;
- legal domain pack example;
- skill-domain eligibility model;
- cross-domain activation rule;
- draft-only professional domain rule.

### Changed

- `docs/governance/README.md` now indexes `ROLE_ACTIVATION.md` in the core read order and governance document list;
- `docs/governance/STATUS.md` now tracks role, domain and skill activation doctrine and explicitly marks role runtime, skill runtime, professional-domain authority, legal-agent authority and architecture-agent authority as not implemented;
- `docs/governance/ROADMAP.md` now records role/domain/skill activation as support doctrine for future UI controls and domain packs.

### Boundary clarification

Role, domain and skill activation follows this rule:

```text
Activate roles to reveal tensions.
Activate domains to constrain context.
Activate skills only as task-bound Hermes candidates.
Validate nothing by activation alone.
```

Architecture and legal domains are documented as draft-only professional domain packs.

They do not create professional validation, legal advice authority, architectural advice authority, autonomous domain agents or automatic external transmission.

This release documents governance support only.

It does not implement:

- autonomous role agents;
- role runtime;
- skill runtime;
- professional-domain authority engine;
- architecture agent authority;
- legal agent authority;
- automatic domain activation;
- automatic role execution;
- automatic skill installation;
- skill marketplace;
- OpenWebUI UI implementation;
- Hermes skill implementation;
- schemas;
- tests;
- operations tooling.

Central rule:

```text
A role can be inactive by default.
A risk can reactivate it.
A domain can constrain work.
A skill can execute only if Hermes is task-authorized.
```

---

## 0.1.8 - 2026-05-27

OpenWebUI cockpit template hierarchy and dependency blocking doctrine.

### Added

- `docs/governance/OPENWEBUI_TEMPLATES.md` as support doctrine for future OpenWebUI cockpit templates;
- parent-child dependency hierarchy for Task Contract, Knowledge, Evidence, Decision, Memory, Module Control and Runtime Candidate surfaces;
- disabled-parent behavior for dependent child functions;
- dependency state vocabulary such as `blocked_by_parent`, `blocked_by_scope`, `blocked_by_missing_evidence`, `suspended_by_risk` and `read_only_degraded`;
- mandatory blockers for missing Task Contract, Context Pack, evidence, approval level, memory policy, parent suspension and unresolved User Decision Gate;
- degraded mode for unavailable child templates;
- OpenWebUI cockpit template anatomy;
- LangGraph run status, Human Interrupt and Capability Gap exposure templates.

### Changed

- `docs/governance/README.md` now indexes `OPENWEBUI_TEMPLATES.md` in the core read order and governance document list;
- `docs/governance/STATUS.md` now tracks OpenWebUI template hierarchy doctrine and explicitly marks OpenWebUI template/function/tool/pipeline implementation as not implemented;
- `docs/governance/ROADMAP.md` now records future OpenWebUI cockpit-template hierarchy and dependency-graph semantics as support doctrine.

### Boundary clarification

OpenWebUI cockpit templates follow this rule:

```text
A disabled parent must make its children visibly unavailable.
A visible child must never imply its parent is satisfied.
```

This release documents governance support only.

It does not implement OpenWebUI templates, Functions, Tools, Pipes, Filters, Actions, Pipelines, native-mode governance runtime, module UI, dependency graph runtime, plugin manager, skill installer, provider router, scheduler, queue, automatic approval, automatic memory promotion, schemas, tests or operations tooling.

Central rule:

```text
OpenWebUI templates make governance visible.
They do not make governance true.
```

---

## 0.1.7 - 2026-05-27

LangGraph reference review, Hermes runtime candidate boundary and module activation doctrine.

### Added

- support review directory `docs/governance/reference_reviews/`;
- `docs/governance/reference_reviews/README.md` as the index for detailed external reference reviews;
- `docs/governance/reference_reviews/LANGGRAPH.md` as a LangGraph external runtime reference review;
- `hermes/profiles/_base/LANGGRAPH_RUNTIME_CANDIDATE.md` as a Hermes-side runtime candidate template;
- `docs/governance/MODULE_ACTIVATION.md` as support doctrine for detection, activation, task authorization and Effective Policy semantics.

### Boundary clarification

```text
Detected does not mean enabled.
Enabled does not mean authorized for a task.
Authorized for a task does not mean sovereign.
```

LangGraph is classified as:

```text
Pantheon   -> reference review and governance boundary only
Hermes     -> optional runtime candidate only, if task-authorized
OpenWebUI  -> cockpit exposure only, not runtime authority
```

---

## 0.1.6 - 2026-05-26

External reference governance system.

### Added

- `docs/governance/WATCHLIST.md`;
- `docs/governance/REFERENCE_BOUNDARIES.md`;
- `docs/governance/ECOSYSTEM_MAP.md`;
- `docs/governance/DISTILLATION_REGISTRY.md`;
- `docs/governance/REJECTED_PATTERNS.md`;
- `docs/governance/EXTERNAL_METHOD_REVIEWS.md`;
- `docs/governance/TENSIONS_AND_RISKS.md`.

### Boundary clarification

```text
observe      -> WATCHLIST.md and SKILL_WATCHLIST.md
understand   -> REFERENCE_BOUNDARIES.md and ECOSYSTEM_MAP.md
decide       -> DISTILLATION_REGISTRY.md, REJECTED_PATTERNS.md and EXTERNAL_METHOD_REVIEWS.md
preserve     -> TENSIONS_AND_RISKS.md
```

Central rule:

```text
Pattern distillation is allowed.
Runtime migration is not.
```

---

## 0.1.5 - 2026-05-17

Context Pack doctrine integration.

### Added

- `docs/governance/CONTEXT_PACKS.md` doctrine;
- governed context bundle concept for Claude Code, ChatGPT, OpenWebUI, Hermes Agent, external assistants and human reviewers;
- distinction between Context Pack, Task Contract, Evidence Pack, Memory Candidate, Canonical Memory and runtime state;
- adapter doctrine for `CLAUDE.md`, ChatGPT project instructions, OpenWebUI prompts/folders, Hermes profile notes and human checklists.

### Boundary clarification

Context Packs are governed scoped context bundles.

They are not Canonical Memory, Evidence Packs, approval, runtime state, hidden prompt authority, hidden task launchers or substitutes for Task Contracts.

---

## 0.1.4 - 2026-05-17

Governance College, User Decision Gate, external agentic inspiration appendix, governed skill watchlist and README integration.

### Added

- `docs/governance/GOVERNANCE_COLLEGE.md` doctrine;
- `docs/governance/USER_DECISION_GATE.md` doctrine;
- `docs/governance/EXTERNAL_AGENTIC_INSPIRATIONS.md` support document;
- `docs/governance/SKILL_WATCHLIST.md` support document;
- README and French README public-facing Governance College / User Decision Gate explanation.

### Boundary clarification

The Governance College is doctrine for separated review viewpoints.

It is not a runtime team of agents.

The User Decision Gate is doctrine for human escalation when discord exceeds safe procedural arbitration.

It is not an automatic approval callback.

External agentic systems and skill marketplaces are inspiration sources only.

They do not create dependencies, implementation commitments, plugin approvals, vendor choices or runtime adoption decisions.

---

## 0.1.3 - 2026-05-17

README repositioning, product differentiation doctrine, Markdown dossier workflow governance proposal, governed OpenWebUI Knowledge handoff doctrine, RAG ingestion pipeline doctrine and external repository inspiration map.

### Added

- `docs/governance/PRODUCT_DIFFERENTIATION.md` product doctrine;
- `docs/governance/MARKDOWN_DOSSIER_WORKFLOW.md` governance proposal;
- governed OpenWebUI Knowledge handoff doctrine in `OPENWEBUI_INTEGRATION.md` and `HERMES_INTEGRATION.md`;
- `docs/governance/RAG_INGESTION_PIPELINE.md` governance proposal;
- `docs/governance/EXTERNAL_REPO_INSPIRATIONS.md` support document;
- README and French README commercial framing around professional trust.

### Boundary clarification

These documents are governance and positioning proposals only.

They do not implement product configuration runtime, OpenWebUI auto-configuration, Hermes auto-configuration, Setup Doctor, audit export, Markdown editor runtime, PDF parsing, OCR, ingestion scheduler, OpenWebUI plugin, OpenWebUI Knowledge gateway, direct Hermes bridge to OpenWebUI database or vector store, Postgres registry writer, Hermes tool, automatic Evidence Candidate writing, automatic Knowledge-to-Memory promotion, provider routing, scheduler or queue.

---

## 0.1.2 - 2026-05-14

Conceptual stabilization, narrative integration, workflow language stabilization, integration boundary stabilization and knowledge-scope doctrine.

### Added

- `CONCEPTUAL_STABILIZATION.md` migration guardrail;
- active `TASK_CONTRACTS.md`, `EVIDENCE_PACK.md`, `MEMORY.md` and `APPROVALS.md` doctrine;
- workflow governance documents as `Workflow Manifest`, `Run Trace View` and `Request Coordination`;
- `HERMES_INTEGRATION.md` as external execution boundary;
- `OPENWEBUI_INTEGRATION.md` as cockpit and exposure boundary;
- `EXTERNAL_TOOLS_POLICY.md` as external capability governance;
- `KNOWLEDGE_TAXONOMY.md` and `SCOPE_ISOLATION.md`;
- `NARRATIVE.md` and `VISUAL_LANGUAGE.md`.

### Boundary clarification

Workflow and integration documents describe governance expectations and boundaries, not runtime behavior.

Scope isolation is documentation-level doctrine, not a runtime partitioning engine.

---

## 0.1.1 - 2026-05-12

Repository governance reconciliation and structural stabilization.

### Added

- governance stub documents for architecture, approvals, task contracts, evidence packs and memory;
- governance stub documents for workflow schemas, workflow adaptation, role signals, memory event schema and skill lifecycle;
- explicit stub status headers for non migrated doctrine;
- lightweight Hermes profile template structure;
- canonical naming alignment for `hephaistos-agent`;
- shared Hermes profile base rules.

### Changed

- `STATUS.md` rewritten as repository state registry;
- `README.md` governance index aligned with `CLAUDE.md` read order;
- `ROADMAP.md` aligned with actual implementation state.

### Boundary clarification

The repository intentionally does not implement autonomous runtime, hidden orchestration runtime, internal scheduler, queue system, provider router runtime, automatic Hermes installation, automatic skill installation, automatic memory promotion, hidden workflow execution or execution API endpoints.

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