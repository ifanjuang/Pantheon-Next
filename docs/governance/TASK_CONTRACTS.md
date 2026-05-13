# Task Contracts

Status: active doctrine — conceptual stabilization.

A Task Contract defines the governed execution boundary for a task delegated to an external runtime.

A Task Contract is not a runtime task.

A Task Contract is not an execution graph.

A Task Contract is not a scheduler object.

Execution happens outside Pantheon Next.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

A Task Contract defines:

- intent;
- scope;
- constraints;
- approvals;
- expected evidence;
- allowed outputs;
- forbidden behaviors;
- memory expectations.

Pantheon Next defines what is legitimate.

Hermes Agent decides how to execute within its own runtime, under the contract boundary.

OpenWebUI may expose the contract, approval request, result and Evidence Pack to the user.

## Core principle

A Task Contract governs execution without owning execution.

Pantheon Next defines:

- what is authorized;
- what is forbidden;
- what evidence is required;
- what approvals are required;
- what memory behavior is allowed.

Pantheon Next never:

- executes;
- schedules;
- dispatches;
- retries;
- routes providers;
- spawns workers;
- orchestrates runtime state.

## Minimal structure

A Task Contract should remain structurally minimal.

Canonical components:

```text
Identity
Intent
Scope
Roles
Constraints
Approvals
Expected Evidence
Allowed Outputs
Forbidden Outputs
Memory Rules
Risk Notes
```

Anything beyond this requires justification.

## Identity

A Task Contract must define:

- stable identifier;
- owner role;
- creation source;
- revision linkage when applicable.

Identifiers are governance identifiers.

They are not runtime execution IDs.

## Intent

Intent defines the governed objective.

Intent must remain human-readable.

Bad intent:

```text
execute autonomous retrieval workflow
```

Good intent:

```text
review architectural consistency between quote and CCTP
```

## Scope

Scope defines boundaries.

It must define:

- included areas;
- excluded areas;
- authority limits;
- expected domain.

If scope is unclear, execution must not be considered governed.

## Roles

Roles are governance authorities.

Roles are not runtime agents.

Example:

```text
athena-agent
```

In Pantheon governance, this means:

```text
governance review authority
```

It does not mean:

```text
autonomous runtime worker
```

Hermes may map a Pantheon role to an execution profile externally.

Pantheon does not execute the role.

## Constraints

Constraints define non-negotiable limits.

Examples:

```text
human approval required before canonization
no external provider routing
no filesystem mutation
no deployment action
```

Constraints are governance rules.

They are not runtime configuration.

## Approvals

A Task Contract must define approval expectations.

Examples:

```text
C1
C2
C3
```

Approvals govern legitimacy.

They do not trigger execution automatically.

## Expected Evidence

Every governed execution must produce traceable evidence.

Canonical output:

```text
Evidence Pack
```

Expected evidence may include:

- assumptions;
- sources;
- risks;
- limitations;
- review notes;
- produced artifacts.

No execution should become canonical without evidence.

## Allowed Outputs

Allowed outputs define authorized artifact categories.

Examples:

```text
markdown review
risk assessment
schema proposal
evidence pack
context pack
```

Allowed outputs are not execution commands.

They are output categories.

## Forbidden Outputs

Forbidden outputs explicitly protect governance boundaries.

Examples:

```text
runtime orchestration
provider routing
automatic deployment
memory canonization
hidden workflow execution
```

If a requested output crosses these boundaries, the Task Contract must be revised or rejected.

## Memory Rules

Task Contracts must define memory behavior explicitly.

Default rule:

```text
outputs are not canonical memory
```

Canonical memory requires:

- review;
- approval;
- traceability;
- evidence linkage.

Retrieved knowledge is not memory.

Embeddings are not memory.

Agent repetition is not memory.

High confidence is not canonization.

## Risk Notes

Risk notes make uncertainty visible.

Examples:

```text
partial repository visibility
runtime assumptions not verified
migration doctrine incomplete
```

Governed systems must expose uncertainty explicitly.

## Forbidden drift

Task Contracts must never become:

- workflow graphs;
- execution DAGs;
- scheduler inputs;
- runtime queues;
- orchestration manifests;
- autonomous agent instructions.

If a Task Contract becomes executable by itself, governance drift has occurred.

## Relationship to Hermes Agent

Hermes Agent may interpret a Task Contract operationally.

Pantheon Next does not define how Hermes executes internally.

Hermes runtime behavior remains external.

Pantheon governs the contract boundary only.

## Relationship to OpenWebUI

OpenWebUI may expose:

- approvals;
- evidence;
- reviews;
- contracts;
- memory candidates.

OpenWebUI does not canonize governance automatically.

OpenWebUI does not become the source of truth.

## Relationship to schemas

The schema for Task Contracts validates structure.

It must not add runtime meaning.

The schema may validate required governance fields.

It must not define:

- execution order;
- retry behavior;
- worker assignment;
- provider choice;
- scheduling;
- dispatch semantics;
- tool execution.

## Final rule

A Task Contract exists to constrain execution.

Not to automate it.
