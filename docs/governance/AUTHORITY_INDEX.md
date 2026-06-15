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

## Current authority map

| Path or area | Authority class | Repo state | Notes |
|---|---|---|---|
| `docs/governance/STATUS.md` | canonical doctrine / active status index | implemented as documentation | Primary repository posture and active document index. |
| `docs/governance/README.md` | canonical navigation / support doctrine | to verify | Governance entry point. |
| `docs/governance/CAPABILITY_PLACEMENT.md` | active support doctrine | implemented as documentation | Defines capability placement and execution boundaries. |
| `docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md` | active support doctrine | implemented as documentation | Keystone: one rulebook, one passport per capability, no per-module rules; consequential effects route through an unbypassable gate (PDP/PEP). Unifies the passport, the two gates and the placement test; adds no runtime. |
| `docs/governance/MODULAR_DOMAIN_REORIENTATION.md` | active support doctrine | implemented as documentation | Reconciles modular capability placement and domain-pack projection. |
| `docs/governance/DOMAIN_PACK_SPEC.md` | active support doctrine | implemented as documentation | General specification for professional domain packs. |
| `docs/governance/REQUEST_LIFECYCLE.md` | active support doctrine | implemented as documentation | Request lifecycle: MÈTIS keeper of the cap (conditional), Zeus cap arbitration, Cerbère/Charon memory gates. MÈTIS/gates not yet in the canonical role registry. |
| `docs/governance/DOSSIER_SITUATION_INTAKE.md` | active support doctrine | documented non-implemented | Intake function before workflow forging: clarifies request, phase, geography, contract scope, sources, tensions and risk. Does not add a new canonical role or runtime. |
| `docs/governance/WORKFLOW_FORGING_PROTOCOL.md` | active support doctrine | documented non-implemented | Workflow Candidate forging protocol: workflows may be generated on the flow, but authority, launch mode and approval ceiling must be arbitrated before launch. No workflow engine. |
| `docs/governance/ANSWER_VERIFICATION_GATE.md` | candidate / to verify | documented non-implemented | Candidate central doctrine for memory-first answers, evidence escalation and consequential response status. Does not implement a classifier, COP, schema, approval engine or memory engine. |
| `docs/governance/DECISION_SURFACE_SPEC.md` | candidate support specification | documented non-implemented | OpenWebUI-facing decision review surface. Display/capture only; not runtime, approval engine, Evidence Pack, memory promotion, Hermes command or source of truth. |
| `docs/governance/SKILL_LIFECYCLE.md` | candidate support doctrine | to verify | Skill lifecycle states and gates; composes manifest, passport, admission guard and preflight. Written fresh by distillation; replaces the former stub. |
| `docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` | active support doctrine | documented non-implemented | Generic boundary for external runtime memory, checkpoint, graph recall and observability adapters. No memory backend, MCP server, checkpoint engine, observability backend or approval/memory engine implemented. |
| `docs/governance/GOVERNED_FORM_FILLING.md` | candidate support doctrine | to verify | Governed filling of any form/CERFA; field-as-claim, resolution loop, modular skills. Method only; connectors/PDF are adapters. Candidate until reviewed. |
| `docs/governance/AUTHORITY_INDEX.md` | active support doctrine | implemented as documentation | Authority map and status vocabulary. |
| `docs/governance/OPEN_PR_RECONCILIATION.md` | validation-only | implemented as documentation | Reconciliation trace for the recent merges and open PRs: classification, cross-cutting risks, maintainer decisions and proposed merge sequence. Records a position; promotes nothing. |
| `docs/governance/TARGET_ARCHITECTURE.md` | validation-only | implemented as documentation | Coherence compass: the system layers (PDP/PEP), the absorption map (which external pattern fills which slot), the coherence gaps and the sequence. Records a direction; adds no runtime. |
| `docs/governance/SPINE_HARDENING_PROPOSAL.md` | validation-only | documented non-implemented | Proposal for the minimal canonical schema set and read-only validator needed to harden the spine. Touches no protected path; apply remains blocked pending explicit approval and #87 alignment. |
| `docs/governance/MONOREPO_INTEGRATION_PROPOSAL.md` | validation-only | documented non-implemented | Proposal and `CLAUDE.md` amendment to host an MCP server (read-only connection to Hermes) and a thin install/liveness verification dashboard in-repo, behind a hard one-way module boundary (modules depend on the governance core, never the reverse). Adds no module code; apply blocked pending approval. |
| `docs/governance/REGISTER_LINK_CASCADE_SCHEMA_PROPOSAL.md` | validation-only | implemented as schemas | Proposal, applied after approval, for two schemas — `register_link` (typed relations between register entries) and `impact_review` (cascade) — formalizing the dependency/impact model in `EVIDENCE_MEMORY_CANONICALIZATION.md`. Declarative contract; no engine, no auto-resolution. Schemas live under `schemas/`. |
| `docs/governance/REPOSITORY_REVIEW_WATCHER.md` | candidate / to verify | documented non-implemented | Candidate workflow manifest for repository activity review. No cron, webhook, queue, dashboard integration, Hermes skill or automatic action implemented. |
| `docs/governance/ARCHITECTURE_AGENCY_DOMAIN_PACK.md` | candidate support doctrine | to verify | Candidate architecture domain pack until promoted. |
| `docs/governance/KNOWLEDGE_INGESTION_AND_MEMORY.md` | candidate support doctrine | to verify | Candidate until boundary review is resolved. |
| `docs/governance/WORKFLOW_LIFECYCLE.md` | candidate / to verify | to verify | Useful governance direction, pending reconciliation with workflow doctrine; now complemented by `WORKFLOW_FORGING_PROTOCOL.md`. |
| `docs/governance/HERMES_KANBAN_EXECUTION_PATTERNS.md` | candidate / to verify | documented non-implemented | Tool-specific Hermes Kanban execution-pattern note only. Coordinates runtime patterns only; does not grant approval, memory, scheduling or governance authority. |
| `docs/governance/MCP_POLICY_SERVER_CANDIDATE.md` | candidate / to verify | documented non-implemented | Candidate-only MCP policy plane for read-only governance resources, validation-only policy checks and MCP capability passporting. It does not create an MCP runtime, host, gateway, approval engine or memory engine. |
| `docs/governance/DATA_PLATFORM_*.md` | candidate / to verify | to verify | Must not convert Pantheon into runtime, ERP, scheduler, queue, approval engine or memory engine. |
| `docs/governance/rites/` | active support doctrine | implemented as documentation | Rites coordinate recurring methodological tensions. They are not runtime workflows. |
| `docs/governance/reference_reviews/` | external reference / support review | to verify | Tool and ecosystem reviews. They do not become doctrine unless distilled. |
| `docs/governance/SPICE_REFERENCE_DISTILLATION.md` | external reference / support review | documented non-implemented | Distills useful Spice decision-layer patterns while refusing Spice as Pantheon core, approval engine, memory engine, Hermes default orchestrator or source of truth. |
| `docs/governance/CAPABILITY_REGISTRY.md` | candidate / to verify | documented non-implemented | Capabilities declared by governance metadata only, as a dependency graph HÉPHAÏSTOS forges from. A declaration is a candidate until reviewed; it records nothing executable, promotes no memory and is not a Registre Probatoire entry. |
| `docs/governance/PADDLEOCR_DASHBOARD_INSTALL_CANDIDATE.md` | candidate / to verify | documented non-implemented | Dashboard-installable, Hermes-managed OCR placement note. Governs status, scope, evidence and memory boundaries only; no install, runtime, skill, MCP host, OCR pipeline, approval engine or memory promotion. |
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

Execution may live in the execution runtime.

Final truth, approval, memory and external-action status remain governed.

## External runtime memory adapter rule

External runtime memory may store, recall, rank, summarize, checkpoint or trace.

It may propose:

```text
Register Candidates
Evidence Pack Candidates
Trace References
Runtime State References
Review Queue signals
```

It must not produce:

```text
Registre Probatoire entries
validated truth
approval
scope decisions
external-action authorization
Pantheon runtime state
```

Any adapter or product-specific review remains documented non-implemented until a separate approved implementation exists outside Pantheon.

## Data platform rule

The data platform remains candidate unless explicitly promoted.

Principle:

```text
The database records.
The workflow proposes.
The evidence supports.
The approval validates.
The human decides.
```

A data platform must not turn Pantheon into an ERP, runtime, scheduler, queue, approval engine or memory engine.

## Sensitive-path guardrail

This index is allowed to live under `docs/governance/`.

It must not require modification of:

- `schemas/`;
- `tests/`;
- `pyproject.toml`;
- `operations/`;
- `platform/`;
- Docker files;
- `.env` files.

Those paths require explicit approval in their own work package.
