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
| `docs/governance/MODULAR_DOMAIN_REORIENTATION.md` | active support doctrine | implemented as documentation | Reconciles modular capability placement and domain-pack projection. |
| `docs/governance/DOMAIN_PACK_SPEC.md` | active support doctrine | implemented as documentation | General specification for professional domain packs. |
| `docs/governance/REQUEST_LIFECYCLE.md` | active support doctrine | implemented as documentation | Request lifecycle: MÈTIS keeper of the cap (conditional), Zeus cap arbitration, Cerbère/Charon memory gates. MÈTIS/gates not yet in the canonical role registry. |
| `docs/governance/CAPABILITY_REGISTRY.md` | active support doctrine | implemented as documentation | Governance declaration of capabilities as a dependency graph; the index HÉPHAÏSTOS forges from. Declarative, no runtime. |
| `docs/governance/AUTHORITY_INDEX.md` | active support doctrine | implemented as documentation | Authority map and status vocabulary. |
| `docs/governance/ARCHITECTURE_AGENCY_DOMAIN_PACK.md` | candidate support doctrine | to verify | Candidate architecture domain pack until promoted. |
| `docs/governance/KNOWLEDGE_INGESTION_AND_MEMORY.md` | candidate support doctrine | to verify | Candidate until boundary review is resolved. |
| `docs/governance/WORKFLOW_LIFECYCLE.md` | candidate / to verify | to verify | Useful governance direction, pending reconciliation with workflow doctrine. |
| `docs/governance/DATA_PLATFORM_*.md` | candidate / to verify | to verify | Must not convert Pantheon into runtime, ERP, scheduler, queue, approval engine or memory engine. |
| `docs/governance/rites/` | active support doctrine | implemented as documentation | Rites coordinate recurring methodological tensions. They are not runtime workflows. |
| `docs/governance/reference_reviews/` | external reference / support review | to verify | Tool and ecosystem reviews. They do not become doctrine unless distilled. |
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

Any change touching those paths requires explicit confirmation.

## Review rule

Before promoting candidate material to doctrine:

1. Read the current governance documents, starting with `STATUS.md`.
2. Check related issues, pull requests, comments and review threads.
3. Classify discussion material as accepted, refused, to verify or to arbitrate.
4. Reconcile contradictions explicitly.
5. Update this authority index when authority status changes.
6. Add an `ai_logs/` entry after significant intervention.

## Status vocabulary

Use these repository-state labels consistently:

- implemented;
- documented non-implemented;
- partial;
- to verify;
- obsolete;
- non applicable.

Do not call a document implemented runtime when it is only documented doctrine.

Do not call a candidate canonical because it is useful.

Do not call an external reference governance because it is inspiring.
