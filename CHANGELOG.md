# Changelog

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

---

## 0.1.3 - 2026-05-17

README repositioning, product differentiation doctrine, Markdown dossier workflow governance proposal, governed OpenWebUI Knowledge handoff doctrine, RAG ingestion pipeline doctrine and external repository inspiration map.

### Added

#### Product differentiation

- active `docs/governance/PRODUCT_DIFFERENTIATION.md` product doctrine;
- clarified that Pantheon differentiates through governed configuration, evidence-first workflow and decision memory;
- explicit positioning that Pantheon does not replace OpenWebUI or Hermes;
- product promise around turning an AI stack into a governed professional method;
- Configuration Pack, Evidence-first and Decision Memory concepts;
- professional dossier mode direction;
- freshness/source aging statuses;
- responsibility statuses;
- contradiction ledger concept;
- Setup Doctor checklist concept;
- audit-ready export concept;
- AI usage register concept;
- adoption maturity levels.

#### Markdown dossier workflow

- active `docs/governance/MARKDOWN_DOSSIER_WORKFLOW.md` governance proposal;
- governed Markdown dossier production model;
- inline governance annotation vocabulary for source needs, citations, assumptions, contradictions, questions, variants, coherence risks, validation requirements and memory proposals;
- selected-zone operation model for paragraph, section, table, diagram, annex, introduction, conclusion or full dossier;
- coherence review checklist after meaningful modifications;
- update proposal model for summary, introduction, table of contents, diagrams, conclusion, source list, evidence notes and validation checklist;
- versioning expectations for professional dossier updates;
- OpenWebUI cockpit mapping for notes, selections, actions, comments, diffs and approvals;
- Hermes execution mapping for rewrite candidates, source checks, coherence reviews, patch candidates, version notes and diagram candidates.

#### Governed OpenWebUI Knowledge handoff

- explicit rule that OpenWebUI may organize user-side folders, files, Notes and Knowledge Bases, but this does not grant Hermes free access to OpenWebUI data;
- OpenWebUI Knowledge handoff doctrine added to `OPENWEBUI_INTEGRATION.md`;
- scoped OpenWebUI Knowledge consultation doctrine added to `HERMES_INTEGRATION.md`;
- Context Pack handoff identified as preferred MVP model;
- future read-only governed knowledge gateway identified as a possible target model;
- direct Hermes access to OpenWebUI database tables, Postgres, pgvector or internal storage marked as avoided for normal workflows;
- distinction preserved between available knowledge, selected knowledge, retrieved knowledge, evidence candidate, Memory Candidate and Canonical Memory.

#### RAG ingestion pipeline

- active `docs/governance/RAG_INGESTION_PIPELINE.md` governance proposal;
- doctrine for turning PDFs and documents into structured, traceable, reviewable RAG-ready sources;
- converter routing model for PyMuPDF4LLM, Docling, Marker and Unstructured as external candidate tools;
- required output structure: `document.md`, `chunks.jsonl`, `manifest.json`, `quality_report.md`, `assets/` and `tables/` when relevant;
- Markdown frontmatter and anchor expectations for page, source and chunk traceability;
- chunking policy based on professional structure rather than fixed character length;
- table and image preservation rules;
- quality doctor scoring and status vocabulary;
- candidate skill decomposition for PDF profiling, conversion, normalization, semantic chunking, manifest building, quality review, OpenWebUI packaging and Evidence Candidate linking;
- explicit distinction between Raw Source, Knowledge Item, Retrieved Knowledge, Evidence Candidate and Memory Candidate.

#### External repository inspiration map

- active support document `docs/governance/EXTERNAL_REPO_INSPIRATIONS.md`;
- inspiration map for RAGFlow, Onyx, AnythingLLM, Khoj, Dify, Flowise, Permify, Ory Keto, Casbin, TerminusDB, Dolt, Guardrails AI and Open Policy Agent;
- distinction between patterns to distill and platforms not to copy;
- mapping between external repository patterns and Pantheon concerns such as ingestion, retrieval, workspace UX, connectors, authorization, workflow visualization, versioning, validation and audit;
- MVP versus optional advanced path guidance;
- explicit anti-runtime guardrails for external inspirations.

#### README commercial framing

- README and French README now emphasize professional trust rather than internal system mechanics;
- added plain-language explanation of OpenWebUI as the visible AI chat application, Hermes Agent as the external technical workshop and Pantheon Next as the control frame;
- reframed Pantheon as a method for using AI in serious professional dossiers without losing sources, assumptions, evidence, validation or memory control;
- visual reading path added around Player, Worldmap, Port, Citadel, Evidence, Livrables and Pantheon;
- missing Evidence and Livrables boards are explicitly marked as images to produce, not existing assets.

### Changed

- `docs/governance/README.md` now registers `PRODUCT_DIFFERENTIATION.md` as active product doctrine;
- `docs/governance/README.md` now registers `MARKDOWN_DOSSIER_WORKFLOW.md` as active governance documentation;
- `docs/governance/README.md` now registers `RAG_INGESTION_PIPELINE.md` as active governance documentation;
- `docs/governance/README.md` now registers `EXTERNAL_REPO_INSPIRATIONS.md` as inspiration/support doctrine, not runtime doctrine;
- `docs/governance/STATUS.md` now tracks product differentiation doctrine and explicitly lists configuration runtime, OpenWebUI auto-configuration, Hermes auto-configuration, Setup Doctor implementation and audit-ready export implementation as not implemented;
- `docs/governance/STATUS.md` now tracks Markdown dossier workflow doctrine and explicitly lists Markdown editor runtime, OpenWebUI plugin implementation and Hermes tool implementation as not implemented;
- `docs/governance/STATUS.md` now tracks governed OpenWebUI Knowledge handoff as documentation-level doctrine and explicitly lists OpenWebUI Knowledge gateway implementation and direct Hermes bridge to OpenWebUI database/vector store as not implemented;
- `docs/governance/STATUS.md` now tracks RAG ingestion pipeline doctrine and explicitly lists PDF parsing runtime, OCR runtime, ingestion scheduler, automatic OpenWebUI import pipeline, Postgres registry writer, automatic Evidence Candidate writer and automatic document-to-memory pipeline as not implemented;
- `docs/governance/STATUS.md` now tracks external repository inspiration as support doctrine and explicitly lists external RAG/search/authorization/versioning/validation dependencies as not implemented;
- the repository posture now states that product differentiation doctrine, Markdown dossier workflow doctrine, governed OpenWebUI Knowledge handoff doctrine, RAG ingestion pipeline doctrine and the external repository inspiration map are stabilized at documentation level;
- future product differentiation implementation is framed as configuration packs, checklists and export templates, not runtime behavior;
- future Markdown dossier implementation is framed as OpenWebUI exposure plus external execution under Task Contract, not Pantheon runtime behavior;
- future RAG ingestion implementation is framed as thin external skill wrappers plus governed status discipline, not Pantheon parsing or indexing runtime;
- future OpenWebUI Knowledge integration is framed as scoped Context Pack or read-only governed gateway, not direct database access;
- future external repository usage is framed as separate governed adoption of one pattern at a time, not import of a full platform.

### Explicitly not implemented

This release does not implement:

- product configuration runtime;
- OpenWebUI auto-configuration engine;
- Hermes auto-configuration engine;
- Setup Doctor implementation;
- audit-ready export implementation;
- Markdown editor runtime;
- PDF parsing runtime;
- OCR runtime;
- ingestion scheduler;
- automatic OpenWebUI import pipeline;
- OpenWebUI plugin;
- OpenWebUI Knowledge gateway;
- direct Hermes bridge to OpenWebUI database or vector store;
- Postgres registry writer;
- Hermes tool;
- automatic document rewriting;
- automatic source validation;
- automatic Evidence Candidate writing;
- automatic Knowledge-to-Memory promotion;
- automatic memory promotion;
- hidden workflow execution;
- provider routing;
- scheduler;
- queue;
- external RAG platform dependency;
- enterprise search dependency;
- authorization service dependency;
- versioned database dependency;
- validation library dependency.

### Boundary clarification

The product differentiation doctrine is a positioning and product-method document only.

Pantheon differentiates through governed configuration, evidence-first workflow and decision memory.

It does not replace OpenWebUI or Hermes.

It does not implement configuration packs, Setup Doctor, audit export, profession modes or runtime behavior.

The Markdown dossier workflow is a governance proposal only.

Pantheon defines what makes dossier editing governable.

OpenWebUI may expose the document surface.

Hermes or another external execution layer may execute bounded edits and reviews.

Pantheon does not execute the workflow.

The RAG ingestion pipeline is also a governance proposal only.

Pantheon defines what makes document ingestion governable.

Hermes or another external execution layer may execute thin skill wrappers for conversion, normalization, chunking and quality reporting.

OpenWebUI may expose upload, selection, quality reports and searchable Knowledge.

Pantheon does not parse PDFs, perform OCR, index documents or import Knowledge by itself.

The OpenWebUI Knowledge handoff is also governance doctrine only.

OpenWebUI organizes user knowledge.

Pantheon turns that organization into a bounded task scope.

Hermes consults only the authorized scope and returns candidates with evidence.

The external repository inspiration map is support doctrine only.

External repositories are inspirations, not dependencies, vendors, runtime components, plugin approvals or implementation decisions.

---

## 0.1.2 - 2026-05-14

Conceptual stabilization, narrative integration, workflow language stabilization, integration boundary stabilization and knowledge-scope doctrine.

### Added

#### Conceptual stabilization

- active `CONCEPTUAL_STABILIZATION.md` migration guardrail;
- governance-first distillation rule for Pantheon-OS recovery;
- explicit `do not migrate unless governance value is proven` posture;
- reduced conceptual core around Role, Policy, Contract, Evidence, Approval, Context and Memory Candidate.

#### Stabilized governance core

- active `TASK_CONTRACTS.md` doctrine;
- active `EVIDENCE_PACK.md` doctrine;
- active `MEMORY.md` doctrine;
- active short-form `APPROVALS.md` doctrine;
- clarified `AGENTS.md` role semantics;
- active `WORKFLOW_SCHEMA.md` doctrine as `Workflow Manifest`;
- active `RUN_GRAPH.md` doctrine as `Run Trace View`;
- active `REQUEST_ORCHESTRATION.md` doctrine as `Request Coordination`.

#### Integration, tools, knowledge and scope doctrine

- active `HERMES_INTEGRATION.md` doctrine as external execution boundary;
- active `OPENWEBUI_INTEGRATION.md` doctrine as cockpit and exposure boundary;
- active `EXTERNAL_TOOLS_POLICY.md` doctrine as external capability governance;
- active `KNOWLEDGE_TAXONOMY.md` doctrine separating sources, knowledge, context, evidence, memory, doctrine and runtime state;
- active `SCOPE_ISOLATION.md` doctrine for session, task, dossier, project, domain, user, organization, repository, governance and system scope;
- explicit no-global-memory-by-default rule;
- explicit rule that OpenWebUI folders may inform scope but do not become Canonical Memory.

#### Narrative and visual layer

- `docs/governance/NARRATIVE.md`;
- `docs/governance/VISUAL_LANGUAGE.md`;
- README introduction using the city-game metaphor;
- governance index entries for narrative and visual documents.

### Changed

- `README.md` now presents Pantheon Next as both a governance kernel and a city-game of reliable decisions;
- `docs/governance/README.md` now distinguishes active doctrine, narrative support doctrine and stub placeholders;
- `docs/governance/README.md` now lists integration, external tools, knowledge taxonomy and scope isolation as active governance doctrine;
- `docs/governance/STATUS.md` now reflects the active status of Task Contracts, Evidence Packs, Memory, Approvals, narrative doctrine, workflow doctrine, integration doctrine, knowledge taxonomy and scope isolation;
- `AGENTS.md` now clarifies that the canonical concept is Pantheon Role, while the filename remains historical compatibility;
- workflow vocabulary is now explicitly governance-only;
- integration vocabulary is now explicitly governance-only and documentation-level.

### Narrative doctrine

The central narrative sentence is now:

```text
L'IA ouvre les possibles.
Pantheon les organise.
L'humain décide.
Le validé reste.
```

The narrative layer is explicitly non-runtime.

It must not redefine Pantheon Next as a game engine, execution engine, autonomous city, hidden workflow runner or agent runtime.

### Workflow doctrine

`WORKFLOW_SCHEMA.md` no longer defines runtime workflow semantics.

It defines a `Workflow Manifest`: a reusable governance declaration for a class of work.

`RUN_GRAPH.md` no longer defines executable graph semantics.

It defines a `Run Trace View`: a human-readable review and evidence trace.

`REQUEST_ORCHESTRATION.md` no longer defines runtime orchestration.

It defines `Request Coordination`: governance intake, review sequencing and escalation guidance.

These documents are explicitly non-runtime.

They must not define:

- execution;
- scheduling;
- queueing;
- provider routing;
- hidden orchestration;
- automatic memory promotion;
- autonomous agent plans.

### Integration doctrine

`HERMES_INTEGRATION.md` defines Hermes Agent as the external execution runtime boundary.

Hermes may execute under Task Contract and return Evidence Packs, Patch Candidates, outputs and Memory Candidates.

Hermes does not canonize memory, approve itself, bypass approvals or become Pantheon doctrine.

`OPENWEBUI_INTEGRATION.md` defines OpenWebUI as the cockpit boundary.

OpenWebUI may expose chat, Knowledge Bases, approvals, Evidence Packs and user-facing results.

OpenWebUI does not become Canonical Memory, source of truth, runtime or approval authority.

`EXTERNAL_TOOLS_POLICY.md` defines external tools as governed capabilities.

It does not define a plugin manager, hidden runtime, provider router or free execution layer.

### Knowledge and scope doctrine

`KNOWLEDGE_TAXONOMY.md` defines the distinction between Raw Source, Source Reference, Knowledge Item, Retrieved Knowledge, Working Context, Evidence Item, Evidence Pack, Output Candidate, Memory Candidate, Canonical Memory, Doctrine and Runtime State.

`SCOPE_ISOLATION.md` defines that every durable memory-like claim must have an explicit validity scope.

OpenWebUI folder scoping may be used as an interface signal, but it must be mapped into a Pantheon scope before it has governance value.

Scope expansion requires review.

Retrieved knowledge and indexed Knowledge Base content remain non-canonical unless selected as evidence or promoted through governed memory review.

### Boundary clarifications

- Iris is preferred as the narrative transmission figure to avoid confusion with Hermes Agent;
- Hermes Agent remains the external execution runtime;
- Mnemosyne may appear as a memory figure, but is not a canonical Pantheon Role unless `AGENTS.md` is explicitly updated;
- narrative companions produce candidate viewpoints and do not self-promote truth;
- workflow documents describe governance expectations, not runtime behavior;
- integration documents describe governance boundaries, not implemented runtime integration;
- scope isolation is documentation-level doctrine, not a runtime partitioning engine.

### Explicitly not implemented

This release still does not implement:

- runtime integration with Hermes Agent;
- runtime integration with OpenWebUI;
- provider routing;
- plugin management;
- automatic memory promotion;
- schemas;
- tests;
- read-only operations tooling.

### Current repository posture

Pantheon Next now has a stronger conceptual, narrative, workflow-governance, integration-boundary and knowledge-scope baseline.

The next critical areas are `ARCHITECTURE.md`, `MODULES.md` and `CODE_AUDIT_POST_PIVOT.md`, followed by schema reconsideration under the protected-file rule.

---

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
- governance README reconciliation with actual repository state;
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