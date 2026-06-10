# Evidence Topology Bridges

Status: active bridge note — documentation-level only.

Date: 2026-05-30

This document links Evidence Topology Gate doctrine to existing Pantheon governance documents.

It is not a replacement for those documents.

It is not a schema.

It is not runtime behavior.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

`EVIDENCE_TOPOLOGY_GATE.md` defines how Pantheon should classify the shape of a task before external execution.

This bridge note clarifies how that doctrine relates to:

- Task Contracts;
- Evidence Packs;
- Hermes integration;
- OpenWebUI exposure;
- memory governance;
- scope isolation;
- external tools;
- Governance College;
- User Decision Gate.

## Bridge to Task Contracts

Relevant document:

- `docs/governance/TASK_CONTRACTS.md`.

Task Contracts define the governed execution boundary for external runtime work.

Evidence Topology Gate adds a pre-execution question:

```text
What topology preserves the proof chain with the smallest safe complexity?
```

Task Contract implication:

- declare topology for non-trivial, evidence-sensitive or externally consequential work;
- explain why single context, fan-out, role-team or bounded swarm is justified;
- prohibit summary-only handoffs where proof-chain continuity matters;
- specify expected Evidence Items and Handoff Artifacts;
- state approval gaps before mutation, publication, transmission or memory impact.

Boundary:

```text
Task Contract topology is governance metadata.
It is not runtime dispatch.
```

## Bridge to Evidence Packs

Relevant document:

- `docs/governance/EVIDENCE_PACK.md`.

Evidence Packs explain what was done, on what basis, with which assumptions, risks and outputs.

Evidence Topology Gate adds topology accountability:

- why the topology was chosen;
- which topologies were rejected;
- what worker outputs were used as Evidence Items;
- what Handoff Artifacts were used between role-team stages;
- what summary-only handoffs were blocked;
- what contradictions remain unresolved;
- how the topology affects approval state.

Boundary:

```text
Evidence Pack records reviewable justification.
It must not become a runtime trace or hidden chain-of-thought archive.
```

## Bridge to Hermes Integration

Relevant document:

- `docs/governance/HERMES_INTEGRATION.md`.

Hermes executes externally under Task Contract.

Evidence Topology Gate clarifies permitted Hermes-side execution patterns:

- single worker with all authorized tools;
- fan-out extraction returning Evidence Items;
- persistent role-team handoff returning Handoff Artifacts;
- bounded swarm returning reviewable candidate outputs.

Hermes may choose internal operational means, but only within Task Contract boundaries.

Hermes must not:

- treat swarm output as approval;
- treat role-team memory as Pantheon memory;
- expand scope silently;
- hide worker traces when evidence is required;
- replace Pantheon Roles;
- bypass User Decision Gates.

Boundary:

```text
Hermes may multiply execution capacity.
It must not multiply authority.
```

## Bridge to OpenWebUI Integration

Relevant document:

- `docs/governance/OPENWEBUI_INTEGRATION.md`.

OpenWebUI exposes the cockpit surface.

Evidence Topology Gate clarifies what OpenWebUI may display:

- selected topology;
- topology reason;
- evidence state;
- worker checkpoints;
- Evidence Items;
- Handoff Artifacts;
- blocked handoffs;
- approval gaps;
- User Decision Gate prompts.

OpenWebUI may expose a visible canvas or conversation surface.

That visibility is useful, but it is not validation.

Boundary:

```text
OpenWebUI display is not governance authority.
A canvas is not an Evidence Pack by itself.
```

## Bridge to Memory

Relevant document:

- `docs/governance/MEMORY.md`.

Evidence Topology Gate reinforces that topology traces, worker summaries, runtime state, role memory, swarm state and repeated observations are not a Registre Probatoire entry.

A topology outcome may support a Register Candidate only if:

- evidence supports it;
- scope is explicit;
- contradictions are handled;
- approval level is satisfied;
- memory doctrine allows it.

Boundary:

```text
Role memory may help execution continuity.
It is not Pantheon Registre Probatoire entry.
```

## Bridge to Scope Isolation

Relevant document:

- `docs/governance/SCOPE_ISOLATION.md`.

Topology selection must preserve scope boundaries.

A worker, role-team or swarm must not broaden scope because it found adjacent material.

Scope expansion requires revised contract or User Decision Gate.

Boundary:

```text
Distributed work does not dissolve scope.
```

## Bridge to External Tools Policy

Relevant document:

- `docs/governance/EXTERNAL_TOOLS_POLICY.md`.

Topology does not authorize tools.

A fan-out or swarm pattern may make tool use more likely, but each external tool remains governed by scope, evidence and approval.

Boundary:

```text
Tool availability is not tool authorization.
Topology selection is not tool approval.
```

## Bridge to Governance College

Relevant document:

- `docs/governance/GOVERNANCE_COLLEGE.md`.

Evidence Topology Gate protects the difference between workers and roles.

Workers may collect, extract, check or produce candidates.

Pantheon Roles review tensions, risks, status and procedure.

Boundary:

```text
Governance College is not a multi-agent runtime.
Roles are not workers.
```

## Bridge to User Decision Gate

Relevant document:

- `docs/governance/USER_DECISION_GATE.md`.

Topology choice may trigger a User Decision Gate when it changes:

- scope;
- risk;
- cost;
- delivery timeline;
- external transmission;
- mutation;
- memory impact;
- evidence sufficiency.

Boundary:

```text
When topology choice affects stakes, expose the choice.
The human decides when procedure is insufficient.
```

## Bridge to examples

Relevant example folder:

- `docs/examples/evidence_topology/`.

The examples show:

- single primary reasoning context;
- fan-out extraction followed by single synthesis;
- persistent role-team handoff;
- Evidence Items;
- Handoff Artifacts;
- approval gaps;
- memory boundaries.

They are fictional and non-executable.

Boundary:

```text
Examples illustrate doctrine.
They do not implement execution.
```

## Rejected bridge mistakes

Reject:

```text
Task Contract topology as runtime dispatch
Evidence Pack as runtime trace
Hermes swarm as approval authority
OpenWebUI canvas as validation
role memory as a Registre Probatoire entry
worker summary as evidence
User Decision Gate as automatic approval
Governance College as hidden debate runtime
```

## Final bridge rule

```text
Task Contract declares the boundary.
Hermes executes within it.
Evidence Pack preserves reviewable proof.
OpenWebUI exposes the state.
Pantheon governs status, approval and memory.
```
