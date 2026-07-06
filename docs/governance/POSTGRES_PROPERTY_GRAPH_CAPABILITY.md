# PostgreSQL Property Graph Capability

Status: candidate support doctrine — documented non-implemented.

Scope: governance graph / evidence graph / capability graph.

Dependency: PostgreSQL 19+ to verify.

Activation: disabled by default.

This document is a candidate capability note for using PostgreSQL Property Graph as an optional read layer over Pantheon governance tables.

It does not implement PostgreSQL 19, SQL/PGQ, schema migrations, runtime behavior, graph algorithms, approval behavior, memory promotion or external actions.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## 1. Intention

PostgreSQL Property Graph may be useful as a readable graph projection over the existing relational governance model.

The purpose is not to turn Pantheon into a graph engine.

The purpose is to make governed relationships easier to inspect:

- cards;
- decisions;
- evidence;
- gates;
- statuses;
- actions;
- dependencies;
- capabilities;
- Hermes bindings;
- runtime health;
- human approvals.

Pantheon remains a governance frame.

Hermes remains the execution runtime.

OpenWebUI remains the exposure surface.

The human remains the decision-maker.

## 2. Architectural position

PostgreSQL remains the primary relational store where applicable.

A property graph, if ever adopted, must remain a declarative read layer over governed tables.

It may help answer bounded relationship questions such as:

- which evidence supports which decision;
- which action is blocked by which gate;
- which capability is proposed but not approved;
- which binding is installed but not activated;
- which runtime is healthy but not qualified safe;
- which cards are in conflict on the same subject;
- which decision lacks sufficient evidence.

The graph does not execute.

The graph does not approve.

The graph does not promote memory.

The graph does not replace gates.

## 3. What Pantheon governs

Pantheon governs:

- statuses;
- status transitions;
- gates;
- approvals;
- evidence / decision / action relationships;
- card dependencies;
- capability / binding / runtime relationships;
- distinctions between signal, proof, status and action;
- qualification of Hermes results;
- traceability of human arbitration.

Pantheon may declare and query a governance graph.

Pantheon must not become the execution engine of that graph.

## 4. What Hermes executes

Hermes executes:

- probes;
- runtime checks;
- installations;
- updates;
- external actions;
- tool calls;
- technical operations;
- bounded workflows after approval.

Hermes may produce runtime outputs that populate governed records.

A runtime output does not become evidence by itself.

```text
runtime_success ≠ evidence
healthy ≠ safe
installed ≠ approved
update_available ≠ update_authorized
binding_selected ≠ dependency_adopted
```

## 5. What OpenWebUI exposes

OpenWebUI exposes:

- cards;
- statuses;
- qualified logs;
- dependency graphs;
- conflicts;
- gates;
- possible actions;
- limits;
- Hermes proposals;
- human approval requests.

OpenWebUI does not decide.

OpenWebUI does not validate.

OpenWebUI does not turn a detected relation into truth.

## 6. What the human must approve

The human must approve:

- adoption of a Hermes binding;
- installation of an external component;
- activation of a capability;
- authorization of an update;
- migration to PostgreSQL 19;
- change to the governance schema;
- qualification of critical evidence;
- consequential external action;
- consequential project-status transition.

## 7. What remains forbidden

Pantheon must not become:

- a graph engine;
- a runtime;
- an installer;
- a scheduler;
- a queue;
- a provider router;
- an MCP host;
- a plugin manager;
- a memory engine;
- an automatic approval system.

The following distinctions remain binding:

```text
relation_detected ≠ evidence
runtime_success ≠ evidence
installed ≠ approved
healthy ≠ safe
update_available ≠ update_authorized
```

## 8. Capability slot

Abstract capability:

Query Pantheon governance relationships as a readable graph.

Candidate binding:

PostgreSQL 19 SQL/PGQ Property Graph.

Installation status:

To verify.

Health:

To verify on the Pantheon / Hermes runtime environment.

Update:

Not applicable at this stage.

Activation:

Disabled by default.

Fallbacks:

- SQL views;
- relational joins;
- recursive CTEs;
- adjacency tables;
- JSON exports for visualization.

Pantheon gates:

- technical schema review;
- PostgreSQL version check;
- migration compatibility check;
- performance check;
- human validation before activation.

## 9. Recommended use

Recommended:

- dependency audits;
- card relationship inspection;
- evidence / decision visualization;
- gate-blocker detection;
- capability / binding / runtime mapping;
- status-incoherence checks;
- conflict diagnosis.

Not recommended:

- unbounded deep propagation;
- shortest-path computation;
- inference engine behavior;
- workflow execution;
- approval behavior;
- long-term memory;
- Hermes orchestration.

For deep recursive traversal, prefer recursive CTEs, bounded Hermes-side analysis under governance, or a separately reviewed external graph adapter.

## 10. Example governed question

Question:

Which action is proposed by Hermes, linked to an installed capability, but blocked because it is not human-approved?

Conceptual model:

```text
Project -> Card -> Action -> Capability -> Binding -> Runtime
Action -> Gate -> Human Approval
Action -> Evidence
```

Expected behavior:

Pantheon displays the governed situation.

Hermes does not execute until the gate is validated.

OpenWebUI makes the status readable.

The human decides.

## 11. Repository classification

This document is:

```text
candidate support doctrine
documented non-implemented
optional capability slot
```

It is not:

```text
canonical doctrine
active runtime
schema migration
PostgreSQL dependency
Hermes install instruction
OpenWebUI feature commitment
approval shortcut
memory mechanism
```

## 12. Doctrine position

PostgreSQL Property Graph is a useful candidate read capability.

It must remain:

- optional;
- reversible;
- readable;
- bounded;
- governed;
- non-critical for system bootstrap.

It may improve auditability and graph readability.

It must not become a central dependency.

```text
Pantheon does not become the engine.
Pantheon becomes the governed dashboard of the engine.
The human decides.
```
