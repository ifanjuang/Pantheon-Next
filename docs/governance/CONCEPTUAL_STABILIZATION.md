# Conceptual Stabilization

Status: active doctrine — migration guardrail.

Pantheon Next must be stabilized conceptually before any further large migration from Pantheon-OS.

This document defines the migration filter.

It does not introduce a runtime, a scheduler, a provider router, an execution engine, a queue, a message bus, an automatic memory system or an autonomous agent layer.

## Core doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon Next is not a cleaned copy of Pantheon-OS.

Pantheon Next is a distilled governance kernel extracted from Pantheon-OS.

The default migration posture is:

```text
Do not migrate unless the element proves governance value.
```

## Purpose

The purpose of Pantheon Next is to make agentic systems governable, auditable, traceable and contextually constrained.

Pantheon Next owns doctrine, validation contracts, evidence structure, approval rules, memory governance and context governance.

Pantheon Next does not own execution.

## Minimal core

The irreducible Pantheon core is limited to the following primitives:

```text
Role
Policy
Contract
Evidence
Approval
Context
Register Candidate
```

These primitives are governance primitives.

They are not runtime objects.

A Workflow Manifest is permitted only as a derived declaration. It must never become an executable graph, a scheduler, a dispatcher or a hidden orchestration layer.

A Skill Manifest is permitted only as a governed capability declaration. It must never become a plugin manager, an installer or a runtime loader.

A Role Signal is permitted only as a governance communication artifact. It must never become a message bus.

## Layers

Pantheon Next distinguishes six layers.

```text
Doctrine explains.
Schemas constrain.
Evidence proves.
Context injects governed constraints.
Runtime executes elsewhere.
UI exposes elsewhere.
```

Pantheon Next owns:

```text
Doctrine
Schemas
Evidence
Context
```

Pantheon Next does not own:

```text
Runtime
UI
```

Hermes Agent owns execution runtime concerns.

OpenWebUI owns user-facing exposure concerns.

## Distillation rule

Pantheon-OS material must be classified before migration.

Allowed classifications:

```text
Keep
Rewrite
Split
Defer
Legacy
Reject
```

### Keep

Use only when the source material is already governance-first, non-runtime and conceptually stable.

### Rewrite

Use when the idea is strong but the source text carries runtime assumptions or legacy wording.

### Split

Use when one historical document mixes governance concepts with runtime concepts.

### Defer

Use when the idea may be useful but depends on missing doctrine, schemas or future operational context.

### Legacy

Use when the material is historically useful but should not become Pantheon Next doctrine.

### Reject

Use when the material contradicts the current doctrine.

## Migration filters

No Pantheon-OS element may be migrated unless it passes all filters below.

### Governance value

The element must define, constrain, validate, trace, approve, contextualize or classify.

If the element mainly executes, dispatches, schedules, routes, loads, installs or manages runtime state, it must not be migrated into canonical governance.

### Boundary safety

The element must not introduce:

```text
execution engine
agent runtime
tool runtime
provider router
scheduler
queue
message bus
central LangGraph runtime
automatic memory promotion
automatic skill installation
automatic Hermes profile installation
hidden workflow runtime
self-evolution auto-merge
runtime dashboard
plugin manager
```

### Semantic necessity

The element must use a necessary concept.

If the concept can be expressed by Role, Policy, Contract, Evidence, Approval, Context or Register Candidate, do not introduce a new primitive.

### Human auditability

The element must remain understandable as governance documentation.

If a reader needs a runtime interpreter to understand it, it is not Pantheon doctrine.

### Canonical memory safety

The element must not allow retrieved knowledge, embeddings, repeated observations or agent confidence to become canonical memory without review and approval.

## Vocabulary reduction

Pantheon Next should reduce inherited vocabulary from Pantheon-OS.

Historical terms must be treated carefully:

```text
module
capability
skill
authority
agent
workflow
signal
registry
manager
orchestrator
router
```

These terms are not forbidden, but they must not create new runtime semantics.

Preferred conceptual reductions:

```text
agent -> role when speaking about Pantheon governance
skill -> governed capability when speaking about declaration
workflow -> governed process declaration
registry -> index when read-only
memory -> candidate unless reviewed and approved
```

Do not rename widely referenced files yet if the rename cost is high.

Clarify semantics before renaming structures.

## Strong assets to preserve

The following ideas are strong and should be preserved during distillation:

```text
Evidence Pack
Approval levels
Task Contract
Task Contract Revision
Register Candidate versus canonical memory
Context Pack
Role responsibility
External tools policy
OpenWebUI / Hermes / Pantheon boundary
AI intervention logs
Status-driven governance
Read-only doctor concept
```

These ideas may be rewritten, simplified or split, but should not be lost.

## Default rejection patterns

The following patterns should normally be rejected or moved to legacy:

```text
runtime registry
execution orchestrator
workflow runner
provider routing
queue consumer
scheduler
plugin manager
automatic installer
auto-promoted memory
self-modifying workflow
agent spawning
hidden LangGraph execution
runtime dashboard
```

If one of these patterns appears useful, it belongs outside Pantheon Next unless explicitly reclassified as external runtime behavior under Hermes or another execution system.

## Migration workflow

Before migrating any Pantheon-OS document, create a short distillation note with:

```text
Source file
Target file
Classification
Kept concepts
Rejected concepts
Boundary risks
Rewrite strategy
Status impact
```

Do not bulk-copy doctrine.

Do not migrate a document because it exists.

Migrate only the concepts that survive the filters above.

## Relationship to schemas

Schemas are validation contracts for governance artifacts.

Schemas must not become runtime contracts.

A schema may define valid structure for a Task Contract, Evidence Pack, Register Candidate, Role Signal, Workflow Manifest or Skill Manifest.

A schema must not define execution order, retry policy, scheduler behavior, queue semantics, provider routing, runtime workers, tool dispatch or memory promotion logic.

## Relationship to operations

Operations tooling may be migrated only as read-only audit tooling.

Allowed:

```text
doctor checks
link checks
schema validation
status consistency checks
forbidden pattern detection
stub detection
read-only reporting
```

Forbidden:

```text
execution
mutation
runtime control
workflow start
tool dispatch
memory promotion
provider routing
scheduler control
queue control
```

## Relationship to domains

Domains may define vocabulary, policies, workflows, context packs and validation expectations.

Domains must not become plugin packs, autonomous agents or runtime modules.

A domain is a governance classification surface.

It is not an execution package.

## Final rule

Pantheon Next should become smaller, clearer and more authoritative than Pantheon-OS.

If a migration makes Pantheon Next larger but not clearer, reject or defer it.

If a migration adds execution power, reject it.

If a migration strengthens doctrine, evidence, approval, memory governance or context governance, keep it.
