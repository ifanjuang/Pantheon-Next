# Capability Registry

Status: active support doctrine — governance declaration of capabilities, organized as a dependency graph for governed composition.

A capability registry is a governance declaration of *what capabilities exist*, *what each may and may not do*, and *which other capabilities each one depends on*. It is the index from which HÉPHAÏSTOS forges a Workflow Manifest candidate (`WORKFLOW_SCHEMA.md`).

It is not a runtime. It is not a skill installer. It is not a plugin manager. It is not a tool dispatch table. It does not execute, schedule, queue or route anything.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Core principle

A capability is declared by its governance metadata only.

The executable skill lives outside Pantheon, in the execution runtime.

Pantheon holds the declaration; the runtime holds the implementation.

```text
The registry declares.
The forge composes.
The runtime executes.
Pantheon governs eligibility, proof and status.
```

A capability declaration is a candidate until reviewed. Availability is not authorization.

## Capability declaration

A capability declaration should remain structurally small. Canonical fields:

```text
Identity        stable governance identifier and clear title
Purpose         the professional outcome it serves
Inputs          expected inputs
Outputs         allowed outputs
Forbidden       forbidden outputs and forbidden effects
Risk class      consequence if it goes wrong
Authority       what it may decide; what it must escalate
Dependencies    other capabilities it relies on
Domain scope    where it applies (domain pack, dossier, scope_id)
Evidence        the proof it is expected to produce
Provenance      where the declaration came from, and when
Status          candidate / reviewed / superseded
```

A declaration describes governance.

It does not describe scheduling, retries, provider routing or tool dispatch.

## Why a graph, not a list

Capabilities are declared with their dependencies, so the registry forms a graph,
not a flat list. This lets the forge retrieve a capability *and the capabilities it
structurally needs*, instead of matching free text.

```text
high-level capability   "prepare the project form"
  depends on
mid-level capabilities  "fetch form template", "resolve known field", "verify entity"
  depends on
low-level capabilities  "read scoped source", "render annotated document"
```

Retrieval starts from a small seed selected by declared purpose, then follows
declared dependencies to recover what is structurally required. The graph is a
governance map of dependency, not an execution graph.

## Metadata-first selection

Only the declaration is read during composition. The implementation is invoked
only after the forged manifest is found eligible and execution is authorized,
outside Pantheon. This keeps composition reviewable and cheap: a reviewer reads
declarations, not code, and the registry can hold many capabilities while a recipe
references only the few it needs.

```text
read the declaration to compose
invoke the implementation only when authorized, outside Pantheon
```

## Enrichment is governed

The registry may be enriched over time — new capabilities, new domain sources,
new declarations. Enrichment is a governed step.

```text
a new capability declaration enters as candidate
review promotes it
a superseded declaration is archived, not deleted (CHARON)
```

No capability self-registers as authority. No enrichment auto-promotes. The
registry must not become a marketplace, an automatic installer or a capability
runtime.

## Relationship to the forge

HÉPHAÏSTOS reads this registry to assemble a Workflow Manifest candidate. The
registry supplies the eligible capabilities and their dependencies; the forge
supplies the topology and the per-step signatures; Pantheon supplies the cap,
the gates and the status.

```text
registry   -> what capabilities exist and what they may do
forge      -> how they are composed for this cap
Pantheon   -> whether the recipe is eligible, proven and approved
runtime    -> execution, outside Pantheon
```

## Relationship to skills and modules

A capability declaration is the skill-governance declaration described in
`MODULES.md` (skill governance module), indexed for composition. It is not an
executable Hermes Skill. Hermes Skills or other runtime skills execute outside
Pantheon under Task Contract.

## Relationship to scope and memory

A capability declares its domain scope (`SCOPE_ISOLATION.md`, `CORE_RECORDS_MODEL.md`).
A capability that crosses scopes must say so and is governed accordingly. The
registry records declarations; it does not promote memory and it is not Canonical
Memory.

## Boundary

Documentation only. This registry is a governance declaration. It does not
implement a runtime, an installer, a scheduler, a queue, a provider router, tool
dispatch or automatic memory promotion. Execution remains external.

```text
The registry declares capabilities and their dependencies.
The forge composes them for a cap.
Pantheon governs eligibility, proof and status.
The execution runtime executes outside.
The human engages.
```
