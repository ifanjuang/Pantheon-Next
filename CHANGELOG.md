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

It does not implement:

- OpenWebUI templates;
- OpenWebUI Functions;
- OpenWebUI Tools;
- OpenWebUI Pipes;
- OpenWebUI Filters;
- OpenWebUI Actions;
- OpenWebUI Pipelines;
- OpenWebUI native-mode governance runtime;
- module UI;
- module registry runtime;
- dependency graph runtime;
- plugin manager;
- skill installer;
- provider router;
- scheduler;
- queue;
- automatic approval;
- automatic memory promotion;
- schemas;
- tests;
- operations tooling.

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

### Changed

- `docs/governance/README.md` now indexes `MODULE_ACTIVATION.md`, `reference_reviews/README.md`, `reference_reviews/LANGGRAPH.md` and the LangGraph Hermes runtime candidate boundary;
- `docs/governance/STATUS.md` now tracks module activation doctrine, LangGraph reference review and the LangGraph Hermes runtime candidate template;
- `docs/governance/ROADMAP.md` now records module activation as support doctrine for future UI controls without implementing a module registry or plugin manager.

### Boundary clarification

Module activation follows this distinction:

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

This release documents governance support only.

It does not implement:

- LangGraph runtime;
- LangGraph installation;
- LangGraph OpenWebUI Function, Pipe, Tool or Pipeline;
- module UI;
- module registry runtime;
- module Effective Policy engine;
- automatic module detection monitor;
- automatic module activation;
- plugin manager;
- skill installer;
- provider router;
- scheduler;
- queue;
- automatic approval;
- automatic memory promotion;
- schemas;
- tests;
- operations tooling.

Central rule:

```text
Pantheon detects capabilities to apply policy.
It does not detect capabilities to execute them.
```

---

## 0.1.6 - 2026-05-26

External reference governance system.

### Added

- active support document `docs/governance/WATCHLIST.md` for general external reference observation;
- active support document `docs/governance/REFERENCE_BOUNDARIES.md` for allowed distillation and forbidden runtime import rules;
- active support document `docs/governance/ECOSYSTEM_MAP.md` for positioning external systems around OpenWebUI, Hermes Agent and Pantheon Next;
- active support document `docs/governance/DISTILLATION_REGISTRY.md` for recording extracted governance patterns;
- active support document `docs/governance/REJECTED_PATTERNS.md` for preserving explicit architectural refusals;
- active support document `docs/governance/EXTERNAL_METHOD_REVIEWS.md` for reviewing reasoning, prompting, evaluation and workflow methods;
- active support document `docs/governance/TENSIONS_AND_RISKS.md` for persistent governance tensions and risk categories.

### Changed

- `docs/governance/README.md` now indexes the external-reference governance system;
- `docs/governance/STATUS.md` now tracks external-reference support documents and explicitly marks related runtime/adoption mechanisms as not implemented;
- `docs/governance/ROADMAP.md` now adds the external-reference governance chain as support doctrine.

### Boundary clarification

The external-reference governance system follows this chain:

```text
observe      -> WATCHLIST.md and SKILL_WATCHLIST.md
understand   -> REFERENCE_BOUNDARIES.md and ECOSYSTEM_MAP.md
decide       -> DISTILLATION_REGISTRY.md, REJECTED_PATTERNS.md and EXTERNAL_METHOD_REVIEWS.md
preserve     -> TENSIONS_AND_RISKS.md
```

This release documents governance support only.

It does not implement:

- external reference adoption engine;
- automatic Watchlist monitor;
- dependency adoption automation;
- skill watch importer;
- reference scoring backend;
- external method runner;
- rejected-pattern enforcement runtime;
- tensions risk engine;
- LangGraph runtime;
- GraphRAG runtime;
- observability backend;
- MCP layer;
- skill marketplace;
- skill installer;
- provider router;
- scheduler;
- queue;
- automatic memory promotion;
- automatic approval.

Central rule:

```text
Pattern distillation is allowed.
Runtime migration is not.
```

---

## 0.1.5 - 2026-05-17

Context Pack doctrine integration.

### Added

- active `docs/governance/CONTEXT_PACKS.md` doctrine;
- governed context bundle concept for Claude Code, ChatGPT, OpenWebUI, Hermes Agent, external assistants and human reviewers;
- explicit distinction between Context Pack, Task Contract, Evidence Pack, Memory Candidate, Canonical Memory and runtime state;
- tool-specific adapter doctrine for `CLAUDE.md`, ChatGPT project instructions, OpenWebUI prompts/folders, Hermes profile notes and human checklists;
- central rule: `Context prepares action. Evidence supports review. Approval legitimizes change. Memory preserves what was validated.`;
- explicit rule that adapters are not canonical and cannot override Pantheon doctrine.

### Changed

- `docs/governance/README.md` now indexes `CONTEXT_PACKS.md` in the core read order and boundary sections;
- `docs/governance/STATUS.md` now tracks Context Packs as active governance doctrine and explicitly lists Context Pack runtime, automatic generator, importer, executor and context-to-memory promotion as not implemented.

### Boundary clarification

Context Packs are governed scoped context bundles.

They are not Canonical Memory, Evidence Packs, approval, runtime state, hidden prompt authority, hidden task launchers or substitutes for Task Contracts.

Claude Code `CLAUDE.md`, ChatGPT project instructions, OpenWebUI prompts/folders and Hermes notes are adapters only.

Pantheon doctrine remains canonical.

---

## 0.1.4 - 2026-05-17

Governance College, User Decision Gate, external agentic inspiration appendix, governed skill watchlist and README integration.

### Added

#### Governance College

- active `docs/governance/GOVERNANCE_COLLEGE.md` doctrine;
- clarified that Pantheon Roles are governance roles, magistratures and controlled viewpoints, not autonomous agents;
- formalized the role college as separated responsibilities of judgment rather than multi-agent execution;
- introduced governed tensions as explicit disagreements between legitimate requirements;
- introduced role biases and risks if unchecked;
- introduced negative powers for roles: propose, challenge, block or escalate;
- introduced dissent statuses such as `ok_with_reserve`, `source_insufficient`, `contradiction_detected`, `delivery_premature`, `transmission_blocked`, `memory_forbidden` and `approval_required`;
- introduced activation proportionality: use more role viewpoints only when risk, external effect or memory impact justifies it;
- clarified ZEUS as procedural arbitrator of status and next procedure, not autonomous truth judge;
- introduced contradiction ledger expectations;
- introduced an economy of doubt: source, version, scope, calculation, professional, recipient, memory and freshness doubts must change the next procedure;
- clarified production versus delivery: produced artifact, draft, deliverable, validated output and memory are distinct states.

#### User Decision Gate

- active `docs/governance/USER_DECISION_GATE.md` doctrine;
- defined when Pantheon must stop procedural arbitration, expose discord and ask for human decision;
- added trigger categories for source conflict, scope conflict, professional risk, external effect, delivery ambiguity, memory risk, approval uncertainty and role conflict;
- added three escalation levels: reserve, clarification and decision required;
- added decision statuses such as `human_decision_required`, `user_clarification_required`, `source_required`, `scope_decision_required`, `transmission_blocked_pending_decision`, `memory_blocked_pending_decision` and `delivery_blocked_pending_decision`;
- added a user-facing discord format with object of conflict, role positions, tension type, severity, options, recommended procedure and decision effects;
- clarified that User Decision Gates may be exposed by OpenWebUI and reported by Hermes, but do not grant approval automatically.

#### External agentic inspirations

- active support document `docs/governance/EXTERNAL_AGENTIC_INSPIRATIONS.md`;
- added distillation grid for external agentic patterns;
- classified LangGraph as external runtime reference, not Pantheon runtime;
- classified LangSmith as observability/eval inspiration, not approval or evidence authority;
- classified Langfuse as self-hostable observability inspiration, not Canonical Memory or approval authority;
- classified GraphRAG and graph-based RAG as corpus-structure inspiration, not proof or memory;
- classified GenAI_Agents as broad pattern catalog, not architecture target;
- classified Shokunin as skill lifecycle inspiration, not memory/MCP/auto-save/scheduler pattern to import.

#### Skill Watchlist

- active support document `docs/governance/SKILL_WATCHLIST.md`;
- added governed watchlist doctrine for external `SKILL.md` ecosystems such as Agensi;
- defined watched skills as signals, not approved Pantheon Skills;
- added watchlist record format;
- added statuses such as `watch`, `pattern_candidate`, `distill_into_doctrine`, `distill_into_hermes_candidate`, `reject_runtime_drift`, `reject_memory_drift`, `reject_external_effect_risk` and `archive`;
- added six-axis scoring lens: governance value, evidence value, professional relevance, runtime drift risk, memory drift risk and external effect risk;
- blocked treating popularity, price, rating, install count or marketplace availability as approval.

#### README integration

- README and French README now include a public-facing Governance College / User Decision Gate explanation;
- README now states that Pantheon does not gain rigor by multiplying autonomous agents, but by separating responsibilities of judgment;
- README now links to `GOVERNANCE_COLLEGE.md` and `USER_DECISION_GATE.md`;
- project status detail lists Governance College and User Decision Gate as documented doctrine.

### Changed

- `docs/governance/AGENTS.md` now links Pantheon Roles to the Governance College model;
- `docs/governance/AGENTS.md` now clarifies that role disagreement is review material, not autonomous runtime chatter;
- `docs/governance/AGENTS.md` now clarifies that ZEUS arbitrates status, risk posture and next procedure, not truth by itself;
- `docs/governance/README.md` now indexes `GOVERNANCE_COLLEGE.md`, `USER_DECISION_GATE.md`, `EXTERNAL_AGENTIC_INSPIRATIONS.md` and `SKILL_WATCHLIST.md`;
- `docs/governance/STATUS.md` now tracks Governance College, User Decision Gate, external agentic inspiration and skill watchlist doctrine;
- `docs/governance/STATUS.md` now explicitly lists autonomous role agents, role message bus, hidden debate runtime, automatic approval loop, skill marketplace, MCP layer, observability backend, GraphRAG runtime and LangGraph runtime as not implemented.

### Explicitly not implemented

This release does not implement:

- autonomous Pantheon role agents;
- multi-agent runtime;
- role message bus;
- autonomous debate runtime;
- ZEUS truth engine;
- automatic User Decision Gate approval;
- OpenWebUI runtime decision-gate UI;
- Hermes runtime role execution;
- LangGraph runtime;
- GraphRAG runtime;
- Langfuse or LangSmith observability backend;
- MCP server layer;
- skill marketplace;
- skill importer;
- skill installer;
- automatic skill updates;
- automatic memory promotion;
- schemas;
- tests;
- operations tooling.

### Boundary clarification

The Governance College is doctrine for separated review viewpoints.

It is not a runtime team of agents.

The User Decision Gate is doctrine for human escalation when discord exceeds safe procedural arbitration.

It is not an automatic approval callback.

External agentic systems and skill marketplaces are inspiration sources only.

They do not create dependencies, implementation commitments, plugin approvals, vendor choices or runtime adoption decisions.