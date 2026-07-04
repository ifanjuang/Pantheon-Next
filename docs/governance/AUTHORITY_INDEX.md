# Pantheon Next — Authority Index

Status: active support doctrine — authority map, repository status vocabulary and sensitive-path guardrail.

This document is a governance index.

It does not implement a runtime, schema, test, operation, platform component, Docker configuration, environment setting, approval engine, memory engine, scheduler, queue, provider router, plugin manager or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Next already distinguishes doctrine, support doctrine, candidates, references, examples and implementation artifacts.

This index makes that distinction explicit so future work does not silently promote a draft, discussion, example, tool note, schema candidate or implementation artifact into authority.

It answers one practical question:

```text
What status does this repository item have, and what may it decide?
```

## Authority classes

### Canonical doctrine

Canonical doctrine defines binding Pantheon governance rules.

A document is canonical when it governs consequential decisions such as truth status, memory status, approval, evidence, scope, external action, role procedure or professional-domain boundaries.

Canonical doctrine overrides candidates, examples, discussions, comments, implementation notes and external references.

### Active support doctrine

Active support doctrine coordinates, clarifies or operationalizes canonical doctrine without replacing it.

It may define placement rules, indexes, checklists, interpretation guides, status maps, review methods, prompt placement rules, bridge boundaries, template discipline or activation semantics.

Support doctrine must remain compatible with canonical doctrine.

### Candidate / to verify

Candidate material proposes a useful orientation but is not yet promoted.

It may be referenced, reviewed or tested.

It must not be treated as binding doctrine until explicit review promotes it.

### Validation-only

Validation-only material tests coherence, audits a position or records a reconciliation.

It may support a decision.

It does not create doctrine by itself.

### External reference

External references describe tools, ecosystems, standards, architectural patterns or adjacent frameworks.

They may inform Pantheon.

They do not govern Pantheon.

### Implementation artifact

Implementation artifacts include executable or machine-checked material such as schemas, tests, code, platform components, operations procedures, Docker files and packaging files.

They may instantiate doctrine.

They must not silently redefine doctrine.

### Voluntarily absent

A voluntarily absent item is excluded by doctrine.

This is an active status, not a gap.

Examples include internal execution runtime, hidden scheduler, autonomous approval engine, automatic memory promotion engine or unrestricted plugin manager when such items would collapse governance into execution.

### Obsolete / refused

Obsolete or refused material has been superseded, rejected or moved outside scope.

It must not be reused as authority unless explicitly reinstated.

## Promotion rule — the referent (B-5)

A candidate does not become active doctrine by age or repetition. Promoting a
`candidate` to `active` (or `implemented`) requires a **referent** — at least one of:

- a schema that encodes it;
- a test that exercises it;
- an end-to-end example that runs it;
- a read-only verification surface (`mcp-server/`) that checks it;
- an explicit, dated human decision recorded in `ai_logs/`.

Without a referent, the material stays a note or a candidate; it is not promoted.
This keeps the doctrine growing only where it anchors to something executable or
explicitly decided (arbitration B-5). The rule governs promotion; it does not
demote existing entries by itself.

## Current authority map

A row whose path is a directory (ending in `/`) or a glob (containing `*`) is a **grouped row**: it indexes every governance document it matches, so individual members are covered without a separate row. The read-only coverage check honors these grouped rows — a candidate under `docs/governance/reference_reviews/`, `docs/governance/rites/` or matching `docs/governance/DATA_PLATFORM_*.md` is considered indexed by its group. Coverage is visibility only; it does not promote a member's authority class.

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `docs/governance/STATUS.md` | canonical doctrine / active status index | implemented as documentation | Primary repository posture and active document index. |
| `docs/governance/README.md` | canonical navigation / support doctrine | to verify | Governance entry point. |
| `docs/governance/CAPABILITY_PLACEMENT.md` | active support doctrine | implemented as documentation | Defines capability placement and execution boundaries. |
| `docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md` | active support doctrine | implemented as documentation | Keystone: one rulebook, one passport per capability, no per-module rules; consequential effects route through an unbypassable gate (PDP/PEP). Unifies the passport, the two gates and the placement test; adds no runtime. |
| `docs/governance/MODULAR_DOMAIN_REORIENTATION.md` | active support doctrine | implemented as documentation | Reconciles modular capability placement and domain-pack projection. |
| `docs/governance/DOMAIN_PACK_SPEC.md` | active support doctrine | implemented as documentation | General specification for professional domain packs. |
| `docs/governance/TERMINOLOGY_BOUNDARIES.md` | active support doctrine | implemented as documentation | Controlled vocabulary, reserved runtime terms, public aliases and progressive cleanup rules. It adds no schema rename, runtime, linter or migration by itself. |
| `docs/governance/COMPETENCE_MODEL.md` | candidate support doctrine | documented non-implemented | Candidate model separating Connaissance, Guide/Ressource de compétence, Compétence, Template, Hermes Skill, Tool/Connector, Evidence, Action and Gate. No competence engine, skill generator, API client, PDF filler, OCR pipeline, diagram generator, web search engine, UI, approval engine or memory engine. |
| `docs/governance/REASONING_MODES_LIBRARY.md` | candidate support doctrine | documented non-implemented | Governance frame for a candidate Guide de compétence on reasoning modes (`templates/competence/reasoning_modes_guide_candidate.json`, moved out of `schemas/`). The Métis `selector`/`controls` are an advisory description, not a router/agent/executor; any runnable selector lives Hermes-side. No reasoning engine, selector runtime, orchestrator, approval engine or memory engine. |
| `docs/governance/CARD_STACK_MODEL.md` | candidate support doctrine | documented non-implemented | Candidate cockpit card-stack grammar for cards, scenes, decks, constellation, navigation, gates, competences, evidence and actions. UX/governance only; no UI, renderer, state machine, approval engine, memory engine, OpenWebUI plugin or Hermes skill. |
| `docs/governance/METHOD_CARD_MODEL.md` | candidate support doctrine | documented non-implemented | Generic Method Card grammar and Method Proposal Candidate model for governed AI use: cockpit-facing cards that name a method without executing it. Documentation only; no UI, renderer, method engine, approval engine, memory engine, OpenWebUI plugin or Hermes skill. |
| `docs/domain-packs/architecture/METHOD_DECK.md` | candidate support doctrine | documented non-implemented | Architecture-domain professional Method Cards (the agency method deck) built on `METHOD_CARD_MODEL.md`. Documentation only; no UI, runtime, approval engine, memory engine, OpenWebUI plugin, Hermes skill or external action. |
| `docs/domain-packs/architecture/METHOD_RUN_TESTS.md` | candidate support examples | documented non-implemented | Compact architecture-domain run tests for Method Cards, Hermes handoff and cockpit density. Documentation only; no UI, runtime, executable test, schema, approval engine, memory engine, Hermes skill or external action. |
| `docs/governance/CARD_STACK_ROLE_QUALITY_ALIGNMENT.md` | candidate support note | documented non-implemented | Reconciles `CARD_STACK_MODEL.md` with role-quality vocabulary: Role / God cards show useful quality expressions, not activated agents. No UI, gesture engine, graph view, approval engine, memory engine or runtime. |
| `docs/governance/ITERATIVE_DELIBERATION_LIFECYCLE.md` | candidate support doctrine | documented non-implemented | How multi-turn AI deliberation (many corrections, a draft CR, then finalization) maps onto governed candidates without making every message a governance event: trace=event log, candidate=projection, ledger=reduced state, gate=command, register=commit. Defines the three persistences (fungible deliberation, pinned constraint/decision ledger, canon) and optimization invariants (shift-left, gate-the-contract, diff-everything, idempotent-finalize). Method/vocabulary only; no conversation engine, chat memory, summarizer, workflow engine, approval engine or memory engine. |
| `docs/governance/REQUEST_LIFECYCLE.md` | active support doctrine | implemented as documentation | Request lifecycle: MÈTIS keeper of the cap (conditional), Zeus cap arbitration, Cerbère/Charon memory gates. MÈTIS/gates not yet in the canonical role registry. |
| `docs/governance/DOSSIER_SITUATION_INTAKE.md` | active support doctrine | documented non-implemented | Intake function before workflow forging: clarifies request, phase, geography, contract scope, sources, tensions and risk. Does not add a new canonical role or runtime. |
| `docs/governance/WORKFLOW_FORGING_PROTOCOL.md` | active support doctrine | documented non-implemented | Workflow Candidate forging protocol: workflows may be generated on the flow, but authority, launch mode and approval ceiling must be arbitrated before launch. No workflow engine. |
| `docs/governance/CONTEXT_STACK.md` | candidate support doctrine | documented non-implemented | Dynamic cockpit-facing context-card stack, Context Stack Change Candidate and HESTIA candidate context-watch role. It does not create a UI, context engine, runtime state, retrieval engine, approval engine, memory engine or canonical role promotion. |
| `docs/governance/ANSWER_VERIFICATION_GATE.md` | candidate / to verify | documented non-implemented | Candidate central doctrine for memory-first answers, evidence escalation and consequential response status. Does not implement a classifier, COP, schema, approval engine or memory engine. |
| `docs/governance/DECISION_SURFACE_SPEC.md` | candidate support specification | documented non-implemented | OpenWebUI-facing decision review surface. Display/capture only; not runtime, approval engine, Evidence Pack, memory promotion, Hermes command or source of truth. |
| `docs/governance/SKILL_LIFECYCLE.md` | candidate support doctrine | to verify | Skill lifecycle states and gates; composes manifest, passport, admission guard and preflight. Written fresh by distillation; replaces the former stub. |
| `docs/governance/EXTERNAL_RUNTIME_THREAT_MODEL_REVIEW.md` | active support doctrine | documented non-implemented | Review method for external runtimes, mixed AI workspaces and privileged capability surfaces. Classifies exposure, host-control, untrusted content, evidence and gates. No scanner, sandbox, runtime, adapter, operation or implementation. |
| `docs/governance/MODEL_CAPABILITY_PASSPORT.md` | active support doctrine | documented non-implemented | Model-specific passport specialization under the uniform capability rule. Governs model admissibility, processing posture, data exposure, task-family suitability, evidence and approval ceiling. No model router, serving, benchmark, provider selection or runtime. |
| `docs/governance/RUNTIME_REVIEW_MODEL_PASSPORT_VALIDATION_PROMOTION.md` | validation-only | documented non-implemented | Promotion proposal for read-only validation of runtime reviews and model passports. Blocks schemas/, tests/ and mcp-server changes pending explicit approval. Creates no validator, MCP tool, schema, test, runtime or external action. |
| `docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` | active support doctrine | documented non-implemented | Generic boundary for external runtime memory, checkpoint, graph recall and observability adapters. No memory backend, MCP server, checkpoint engine, observability backend or approval/memory engine implemented. |
| `docs/governance/GOVERNED_FORM_FILLING.md` | candidate support doctrine | to verify | Governed filling of any form/CERFA; field-as-claim, resolution loop, modular skills. Method only; connectors/PDF are adapters. Candidate until reviewed. |
| `docs/governance/AUTHORITY_INDEX.md` | active support doctrine | implemented as documentation | Authority map and status vocabulary. |
| `docs/governance/OPEN_PR_RECONCILIATION.md` | validation-only | implemented as documentation | Reconciliation trace for the recent merges and open PRs: classification, cross-cutting risks, maintainer decisions and proposed merge sequence. Records a position; promotes nothing. |
| `docs/governance/TARGET_ARCHITECTURE.md` | validation-only | implemented as documentation | Coherence compass: the system layers (PDP/PEP), the absorption map (which external pattern fills which slot), the coherence gaps and the sequence. Records a direction; adds no runtime. |
| `docs/governance/SPINE_HARDENING_PROPOSAL.md` | validation-only | documented non-implemented | Proposal for the minimal canonical schema set and read-only validator needed to harden the spine. Touches no protected path; apply remains blocked pending explicit approval and #87 alignment. |
| `docs/governance/MONOREPO_INTEGRATION_PROPOSAL.md` | validation-only | documented non-implemented | Proposal and `CLAUDE.md` amendment to host an MCP server (read-only connection to Hermes) and a thin install/liveness verification dashboard in-repo, behind a hard one-way module boundary (modules depend on the governance core, never the reverse). Adds no module code; apply blocked pending approval. |
| `docs/governance/REGISTER_LINK_CASCADE_SCHEMA_PROPOSAL.md` | validation-only | implemented as schemas | Proposal, applied after approval, for two schemas — `register_link` (typed relations between register entries) and `impact_review` (cascade) — formalizing the dependency/impact model in `EVIDENCE_MEMORY_CANONICALIZATION.md`. Declarative contract; no engine, no auto-resolution. Schemas live under `schemas/`. |
| `docs/governance/REPOSITORY_REVIEW_WATCHER.md` | candidate / to verify | documented non-implemented | Candidate workflow manifest for repository activity review. No cron, webhook, queue, dashboard integration, Hermes skill or automatic action implemented. |
| `docs/domain-packs/architecture/AGENCY_DOMAIN_PACK.md` | candidate support doctrine | to verify | Candidate architecture domain pack until promoted. |
| `docs/domain-packs/architecture/SOURCE_POLICY.md` | candidate support doctrine | documented non-implemented | Architecture-fr source treatment policy: source states, authority classes, freshness, project-source priority, Evidence Pack Candidate expectations and output status discipline. No runtime, retrieval engine, source validator, OpenWebUI config or Hermes skill. |
| `docs/governance/KNOWLEDGE_INGESTION_AND_MEMORY.md` | candidate support doctrine | to verify | Candidate until boundary review is resolved. |
| `docs/governance/WORKFLOW_LIFECYCLE.md` | candidate / to verify | to verify | Useful governance direction, pending reconciliation with workflow doctrine; now complemented by `WORKFLOW_FORGING_PROTOCOL.md`. |
| `docs/governance/HERMES_KANBAN_EXECUTION_PATTERNS.md` | candidate / to verify | documented non-implemented | Tool-specific Hermes Kanban execution-pattern note only. Coordinates runtime patterns only; does not grant approval, memory, scheduling or governance authority. |
| `docs/governance/HERMES_PAGE_AGENT_INTEGRATION.md` | active support doctrine | documented non-implemented | Hermes-side Page-Agent / Chrome / MCP browser-control adapter framing. Raw Page-Agent commands are not exposed; P0 is status + observe only; final effects require explicit human gates. No Page-Agent dependency, Chrome extension, Hermes skill, MCP service, browser automation, approval engine, memory engine or external action is implemented. |
| `docs/governance/MCP_POLICY_SERVER_CANDIDATE.md` | candidate / to verify | documented non-implemented | Candidate-only MCP policy plane for read-only governance resources, validation-only policy checks and MCP capability passporting. It does not create an MCP runtime, host, gateway, approval engine or memory engine. |
| `docs/governance/TRIPARTITE_INTERFACE_SPEC.md` | candidate support doctrine | documented non-implemented | Interface grammar for exposure surface, execution runtime, Pantheon governance and optional MCP policy surface. Defines data objects and trace spine only; no API, endpoint, queue, scheduler, OpenWebUI extension, Hermes skill, MCP tool, approval engine, memory engine or external action. |
| `docs/governance/MCP_PANTHEON_MINIMAL_V0.md` | candidate support doctrine | documented non-implemented | Minimal MCP Pantheon posture: read-only resources, validation-only tools, candidate skeletons and reports. Refuses runtime, connector gateway, provider router, scheduler, queue, approval engine, memory promotion and external action server. |
| `docs/governance/REFUSAL_FIXTURES.md` | candidate support doctrine | documented non-implemented | Refusal fixture catalog for future MCP, Hermes adapter and OpenWebUI gate tests. Documentation only; no tests, CI, runtime behavior, MCP tools, OpenWebUI actions, Hermes skills, external actions, approval behavior or memory promotion. |
| `docs/domain-packs/architecture/DOCUMENT_REVIEW.md` | candidate support doctrine | to verify | Architecture-domain document-review slice applying `DOMAIN_PACK_SPEC.md` and `DOCUMENT_INTELLIGENCE.md`. Documentation only. |
| `docs/domain-packs/architecture/INDEX_EFFECT_MATRIX.md` | candidate support doctrine | to verify | Candidate matrix for interpreting document indices and versions in architecture practice. Documentation only. |
| `docs/domain-packs/architecture/KNOWLEDGE_REGISTRY_BLUEPRINT.md` | candidate support doctrine | documented non-implemented | Pantheon-side blueprint for the architecture knowledge registry (regulations, agency standards, details, lessons learned, supplier data, precedents) reusing the proof-register authority/status vocabulary. Resolves OS_RECONCILIATION item C: blueprint in Pantheon, runnable mapping outside. No runtime. |
| `docs/domain-packs/architecture/PROJECT_OBJECT_MODEL.md` | candidate support doctrine | documented non-implemented | Candidate project object model: spatial hierarchy, transversal zones, typed relations, internal nomenclature, semi-structured property sets with per-instance overrides, phase states and non-normative analysis contexts. Describes the project world and references the Pantheon registers; no runtime. |
| `docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md` | candidate support doctrine | documented non-implemented | Candidate belief contract turning heterogeneous sources into provenance-bearing project beliefs. Documentation + validation schemas only; no runtime, extraction, OCR, vision or Revit plugin. |
| `docs/domain-packs/architecture/PROJECT_UNDERSTANDING_ADAPTER_CONTRACT.md` | candidate support doctrine | documented non-implemented | Binding an external APU adapter (PDF/IFC/image/Revit reader) must respect: Task Contract in -> Result Candidate + Evidence Pack Candidate out, candidate-only, per-attribute provenance, E0-E4 certainty, no canonization. Specializes BRIDGE_CONTRACT/ADAPTERS_AND_BINDINGS; runtime lives outside Pantheon. |
| `docs/governance/PANTHEON_REVIT_GATE.md` | candidate support doctrine | documented non-implemented | Framing dossier for a local Revit architecture plugin governed by Pantheon. Current arbitration accepts V0 Free Exploration Mode as sandbox / exploration only: architecture-only, offline/local-first, permissive on test copies with mandatory minimal traces. It is not production policy and implements no plugin/runtime. The conservative read-first/control-matrix posture remains the later regulated target in `PANTHEON_REVIT_GATE_DEVELOPER_DOSSIER.md`. |
| `docs/governance/PANTHEON_REVIT_GATE_2027_PROTOTYPE_PLAN.md` | candidate support doctrine | documented non-implemented | Revit 2027 prototype planning slice for Pantheon Revit Gate: targets Revit 2027 / .NET 10, treats the Revit Public MCP Server as an adapter signal rather than the first dependency, and narrows the first proof loop to context pack, light write actions and logs. Documentation only; no plugin code, add-in, MCP server, schema, test, Docker or operations change. |
| `docs/domain-packs/architecture/PROOF_REGISTER.md` | candidate support doctrine | to verify | Candidate proof register for architecture practice. Documentation only; records nothing executable. |
| `docs/domain-packs/architecture/PROOF_REGISTER_IMPLEMENTATION_SPEC.md` | candidate / to verify | documented non-implemented | Implementation candidate for the architecture proof register and indexed document-version model. Specification only; no runtime. |
| `docs/domain-packs/architecture/PROJECT_UNDERSTANDING_EXTERNAL_REFERENCES.md` | external reference | documented non-implemented | Candidate-only register of external standards, libraries, tools, datasets and research that may inspire Architecture Project Understanding adapters/examples/benchmarks. Non-canonical; no runtime, schema or dependency. |
| `docs/governance/PROGRAM_AND_CONFORMANCE.md` | candidate support doctrine | documented non-implemented | Program-as-source and conformance extension of the project-understanding contract: typed/layered/versioned programs, requirements, multi-scheme classification, composite multi-level groups, deviations with bidirectional resolution. Documentation + validation schemas only; no runtime. |
| `docs/domain-packs/architecture/TARGET_WORKFLOWS.md` | candidate support doctrine | documented non-implemented | Consolidates the architecture-agency workflow examples into one target model. No runtime, connector, OpenWebUI action, Hermes skill, sender, listener, generator, exporter or memory engine. |
| `docs/domain-packs/architecture/REFLEX_OPERATING_MODEL.md` | candidate support doctrine | documented non-implemented | Common operating grammar for architecture-domain reflexes: Request -> Depth -> Context -> Reflexes -> Candidate -> Gate. Keeps reflexes compact and composable; adds no router, workflow engine, UI, connector, memory engine, approval engine or automatic action. |
| `docs/domain-packs/architecture/METHOD_TAXONOMY.md` | candidate support doctrine | documented non-implemented | Architecture-domain vocabulary for methods, approaches, disciplines, strategies, procedures, tactics and reflexes. Keeps reflex narrow; no runtime, workflow engine, generator, checker, sender or external action. |
| `docs/domain-packs/architecture/ROLE_REFLEX_COORDINATION.md` | candidate support doctrine | documented non-implemented | Coordination model for role-owned reflexes, consultations, rites and Zeus arbitration inside architecture-domain approaches. No agent loop, workflow runtime, role executor, rite runner, approval engine or external action. |
| `docs/domain-packs/architecture/ROLE_FACETS.md` | candidate support doctrine | documented non-implemented | Candidate architecture role-quality model: roles guard jurisdictions; facets are qualities such as sensitivities, reflexes, orientations, tactics, consultation habits, prudence modes, thresholds and limits. No agent, role executor, approval engine, sender or memory engine. |
| `docs/domain-packs/architecture/ROLE_ACTIVATION_MODEL.md` | candidate support doctrine | documented non-implemented | Historical filename for the current Architecture Role Expression Model: roles are permanent guardians; qualities/facets express contextually. No role activation module, scoring engine, agent loop, UI, approval engine or runtime. |
| `docs/domain-packs/architecture/MISSION_RESPONSIBILITY_BOUNDARY_REFLEX.md` | candidate support doctrine | documented non-implemented | Architecture-domain guardrail for mission scope and responsibility boundaries. Warns before outputs that may imply validation, instruction, visa, OPC, financial approval, insurance confirmation, fault recognition or mission extension. No legal review, email sending, Notion write or runtime. |
| `docs/governance/PANTHEON_REVIT_GATE_DEVELOPER_DOSSIER.md` | candidate support doctrine | documented non-implemented | Developer dossier for the future Pantheon Revit Gate, a local Revit add-in that would turn a governed Action Contract into a controlled Revit transaction under human validation. Documentation only; no runtime, no Revit plugin code, no schema, no test and no Docker/operations change. Pantheon governs rights; the add-in would execute locally inside Revit, outside Pantheon, and the human validates. No claim that the plugin exists. |
| `docs/governance/DOCUMENT_INTELLIGENCE.md` | candidate support doctrine | to verify | Frames governed document intelligence and the evidence chain without becoming a document-processing runtime, OCR pipeline, vector database, graph runtime, scheduler or queue. Documentation only. |
| `docs/governance/EVIDENCE_MEMORY_CANONICALIZATION.md` | candidate support doctrine | documented non-implemented | Central note for the `Registre Probatoire` (evidence register). Intended model for scoped, versioned, dated, cited entries; certainty on the `E0–E4` scale owned by `GLOSSARY.md`. No memory engine. (issue #68) |
| `docs/governance/EVIDENCE_MEMORY_DEV_PLAN.md` | candidate support doctrine | documented non-implemented | Development plan companion to `EVIDENCE_MEMORY_CANONICALIZATION.md`. Documentation only. (issue #68) |
| `docs/governance/MODULE_INVOCATION_PREFLIGHT.md` | candidate / to verify | documented non-implemented | Proposed doctrine for invoking roles, rites, places and external connections before a module is used. No UI, gateway, MCP server, connector runtime, scheduler, queue, executor or approval system. |
| `docs/governance/NANGO_HERMES_CONNECTOR_GATEWAY.md` | candidate support doctrine | documented non-implemented | How Nango may be considered a bounded Hermes-side connector gateway for third-party APIs. Does not install Nango; no runtime. |
| `docs/governance/PADDLEOCR_HERMES_SKILL_NOTE.md` | candidate / to verify | documented non-implemented | Placement note for PaddleOCR as a possible document-extraction adapter. Does not implement PaddleOCR. |
| `docs/governance/PANTHEON_COCKPIT_UX_SPEC.md` | candidate / to verify | documented non-implemented | Product and governance UX candidate for the future Pantheon-facing cockpit, discussion and drafting surface. No UI, runtime, chat engine, editor, router, scheduler, queue, approval engine, memory engine, OpenWebUI Function or Hermes skill. |
| `docs/governance/PANTHEON_CONTROL_BOUNDARY.md` | candidate support doctrine | to verify | Single boundary reference for the verification surface `CLAUDE.md` names `dashboard/`. Supersedes the larger Pantheon Control drafts in PR #67 and PR #72. Candidate until reviewed. |
| `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` | candidate / to verify | documented non-implemented | Development sequence for a future Pantheon MCP Policy Server. No MCP server, Docker service, installer, dashboard, gateway, connector runtime, scheduler, queue, approval engine, memory engine, router or plugin manager. Partially superseded by the implemented read-only `mcp-server/` artifact; remains useful as development history and must not contradict `WHAT_RUNS.md` or `MODULES.md`. |
| `mcp-server/` | implementation artifact / read-only verification surface | implemented read-only / partial / protected path | Bounded read-only MCP policy / verification surface (capability-passport validation and the install / observability / backup / exposure / update verifiers). Validates structure and status and returns status data only; must not execute, approve, send, schedule, queue, route providers, install, update, write external systems or promote memory. Implementation artifact, not authority; broader server coverage remains to verify. Changes are a protected path. |
| `docs/assets/pantheon-control/` | implementation artifact / static prototype | static prototype / partial read-only mirror / to verify | Static Pantheon Control prototype (the surface `CLAUDE.md` names `dashboard/`). Some logic mirrors read-only verification behaviour (including the update verifier after PR #239); it is not a live cockpit, approval engine, memory engine, runtime, sender, scheduler or provider router. Static prototype, not authority. |
| `base_metier/architecte/` | external professional corpus / to verify | documented non-implemented | Architecture professional RAG corpus (knowledge / skills / prompts / workflows). Candidate corpus, **not authority and not proof**. Source PDFs are kept out of git (`.gitignore`) with a reconstructible manifest at `knowledge/sources/SOURCES.manifest.yaml`; licence is to verify per source (MAF / Ordre des Architectes material is copyrighted). The two ingestion skills execute (PyMuPDF) and belong Hermes-side. Frozen pending the B-2 licence decision; do not ground a vertical slice on it until qualified. |
| `docs/governance/RAW_DERIVED_GOVERNED_RECORDS.md` | candidate support doctrine | documented non-implemented | Separation between raw, derived and governed records, retrieval and provenance objects, evidence and approvals. Non-executable. |
| `docs/governance/REVIEW_QUEUE.md` | candidate support doctrine | documented non-implemented | Governance rule for a review queue surfacing doubtful, conflicting, stale, low-confidence or consequential items to a human decision. Documentation only; no queue runtime. |
| `docs/governance/UNDERSTAND_ANYTHING_HERMES_ADAPTER.md` | candidate support doctrine | documented non-implemented | How Understand-Anything may be considered a bounded Hermes-side structural-analysis capability. Does not install it; no runtime. |
| `docs/governance/URGENT_REVIEW_TRIAGE.md` | candidate support doctrine | documented non-implemented | Urgency-qualification rule for fiches before they enter or move inside a review queue. Documentation only. |
| `docs/governance/DATA_PLATFORM_*.md` | candidate / to verify | to verify | Must not convert Pantheon into runtime, ERP, scheduler, queue, approval engine or memory engine. |
| `docs/governance/rites/` | active support doctrine | implemented as documentation | Rites coordinate recurring methodological tensions. They are not runtime workflows. |
| `docs/governance/reference_reviews/` | external reference / support review | to verify | Tool and ecosystem reviews. They do not become doctrine unless distilled. |
| `docs/governance/SPICE_REFERENCE_DISTILLATION.md` | external reference / support review | documented non-implemented | Distills useful Spice decision-layer patterns while refusing Spice as Pantheon core, approval engine, memory engine, Hermes default orchestrator or source of truth. |
| `docs/governance/CAPABILITY_REGISTRY.md` | candidate / to verify | documented non-implemented | Capabilities declared by governance metadata only, as a dependency graph HÉPHAÏSTOS forges from. A declaration is a candidate until reviewed; it records nothing executable, promotes no memory and is not a Registre Probatoire entry. |
| `docs/governance/PADDLEOCR_DASHBOARD_INSTALL_CANDIDATE.md` | candidate / to verify | documented non-implemented | Dashboard-installable, Hermes-managed OCR placement note. Governs status, scope, evidence and memory boundaries only; no install, runtime, skill, MCP host, OCR pipeline, approval engine or memory promotion. |
| `docs/domain-packs/architecture/PROBATIVE_INSTRUCTION.md` | candidate support doctrine | documented non-implemented | Architecture-domain instruction method: how Pantheon frames questions that need source retrieval, professional qualification, responsibility review and human decision. Method only; not a RAG engine, graph runtime, agent, checker, scheduler, queue, approval engine, memory engine, OpenWebUI extension, Hermes skill or schema. |
| `docs/governance/ARCHITECTURAL_PROJECT_GRAPH.md` | candidate orientation | documented non-implemented | Architecture domain graph, visualization and boundary note. Orientation only; no graph database, BIM runtime, IFC parser, GraphRAG runtime, vector database, memory engine, approval engine, evidence register or external action. |
| `docs/governance/BOOTSTRAP_INSTALLATION_LADDER.md` | candidate orientation | documented non-implemented | Cold-start installation sequence and dependency ladder. Orientation only; no Docker configuration, compose file, install script, service, scheduler, queue, memory engine or runtime. |
| `docs/governance/NAS_INSTALLATION_PROFILES.md` | candidate orientation | documented non-implemented | NAS installation profiles, acceleration classes and redirection patterns. Orientation only; no Docker configuration, runtime service, scheduler, queue, memory engine or connector. |
| `docs/governance/PANTHEON_CONTROL_INTENT_LOG.md` | candidate / to verify | documented non-implemented | Intent log for Pantheon Control (issue #192). Record only; decides nothing, promotes no memory and adds no runtime. |
| `docs/governance/ROLE_DIALOGUE_TRACE.md` | candidate orientation | documented non-implemented | Observable workflow trace, role dialogue and cockpit log. Orientation only; no workflow runtime, agent loop, hidden recorder, scheduler, queue, approval engine or memory engine. |
| `templates/` | support material / candidates | to verify | Non-executable scaffolds. Templates instantiate doctrine; they do not govern. |
| `examples/` | illustrative material | to verify | Fictional examples. They do not override doctrine. |
| `ai_logs/` | validation-only / trace | to verify | Intervention trace, not canonical doctrine. |
| `schemas/` | implementation artifact | protected path | Do not modify without explicit confirmation. |
| `tests/` | implementation artifact | protected path | Do not modify without explicit confirmation. |
| `operations/` | implementation / operational artifact | protected path | Spec first; no operations file before validated governing documentation. |
| `platform/` | implementation artifact | protected path | Do not modify without explicit confirmation. |
| `pyproject.toml` | packaging / implementation artifact | protected path | Do not modify without explicit confirmation. |
| `Docker*` | infrastructure / runtime artifact | protected path | Do not modify without explicit confirmation. |
| `.env*` | environment / secret boundary | protected path | Do not modify. |
| Historical bootstrap stubs formerly listed in roadmap/status materials, including `MODEL_ROUTING_POLICY.md`, `MEMORY_EVENT_SCHEMA.md`, `EPISTEMIC_CONTROL.md` and equivalent declared stubs | candidate / stub reference | documented non-implemented | Not canonical, not implemented and not active support doctrine unless a future row in this index promotes a concrete file. Roadmap mentions are historical signals, not authority. |

## Bootstrap stub rule

Historical bootstrap stubs may appear in roadmap, migration or discussion material before a concrete governed document exists.

They remain:

```text
candidate / stub reference
repo state: documented non-implemented
```

until this authority index explicitly promotes a concrete path.

A roadmap mention, filename placeholder or removed `STATUS.md` stub list does not make the item canonical, implemented, active support doctrine or voluntarily absent.

## Placement test

For any capability, module, template, skill, connector, workflow or data platform component, ask:

```text
If this goes wrong, can it produce a false truth,
an unapproved external effect,
a wrong memory,
an invalid approval,
an illegitimate scope expansion,
or an unauthorized action?
```

If the answer is no, it is a feature and belongs in the appropriate tool or runtime.

If the answer is yes, Pantheon governs the decision through rules, status, evidence, memory, approval and scope.

Execution remains outside Pantheon unless a separately approved implementation artifact exists.

```text
Governing is not implementing.
```

## Tool naming rule

Generic governance documents should use abstract roles:

- exposure surface;
- execution runtime;
- observability layer;
- connector gateway;
- data registry;
- administration cockpit.

Specific product names belong in bindings, adapters, integration notes, reference reviews or other non-generic documents whose subject is the tool relationship.

## Terminology boundary rule

`TERMINOLOGY_BOUNDARIES.md` defines controlled terms, reserved runtime words, public aliases and progressive cleanup rules.

New governance writing should prefer:

```text
Case / Affaire
Situation
Method / Méthode
Approach / Démarche
Contract / Contrat
Scope / Périmètre
Corpus
Source
Connaissance
Context / Contexte
Capability / Capacité
Competence / Compétence
Guide de compétence
Ressource de compétence
Template
Assertion
Evidence / Preuve
Gate / Seuil
Approval / Approbation
Register / Registre
Recall / Rappel
Trace
Role / Rôle
Handoff / Relais
Surface
```

Runtime and host-system words remain reserved unless explicitly qualified:

```text
Runtime
Workflow
Skill
Tool
Plugin
Job
Action
State
Run
Node
Edge
Checkpoint
Thread
Queue
Scheduler
Worker
```

This terminology rule does not rename schemas or existing fields by itself. It governs future language and progressive cleanup proposals.

## Domain pack rule

A domain pack is a governed professional method.

It does not advise, validate, approve, execute, send or memorize by itself.

Common envelope:

```text
Task Contract in
-> module
-> Result Candidate + Evidence Pack Candidate out
```

The method lives in Pantheon.

Display may live in the exposure surface.
Execution may live in Hermes.
Pantheon governs status.
