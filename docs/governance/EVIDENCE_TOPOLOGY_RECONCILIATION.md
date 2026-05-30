# Evidence Topology Reconciliation

Status: active reconciliation note — documentation-level only.

Date: 2026-05-30

This document reconciles the new Evidence Topology Gate material with the current governance corpus without replacing the main indexes in a risky bulk edit.

It is a lightweight bridge for `README.md`, `docs/governance/STATUS.md`, `CHANGELOG.md` and `docs/governance/README.md`.

It does not replace those documents.

It does not implement runtime behavior.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Why this reconciliation note exists

The Evidence Topology Gate doctrine was added after analysis of single-agent, multi-agent, swarm and persistent role-team patterns.

The doctrine adds an important rule:

```text
The unit of reasoning is not the agent.
The unit of reasoning is the proof chain.
```

The main governance indexes should eventually point to this doctrine, but large index replacements were avoided to reduce merge and SHA-conflict risk.

This note records the reconciliation target explicitly.

## Documents to index later

The following documents should be referenced in the main governance index during a focused reconciliation pass:

- `docs/governance/EVIDENCE_TOPOLOGY_GATE.md`;
- `docs/governance/EVIDENCE_TOPOLOGY_ROADMAP.md`;
- `docs/governance/EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md`;
- `docs/governance/EVIDENCE_TOPOLOGY_BRIDGES.md`;
- `docs/examples/evidence_topology/README.md`.

## Recommended placement

### `docs/governance/README.md`

Recommended additions:

- add `EVIDENCE_TOPOLOGY_GATE.md` to the core bootstrap read order after `EVIDENCE_PACK.md` or before `HERMES_INTEGRATION.md`;
- add `EVIDENCE_TOPOLOGY_ROADMAP.md`, `EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md` and `EVIDENCE_TOPOLOGY_BRIDGES.md` as support/reconciliation documents;
- add `docs/examples/evidence_topology/` to examples navigation.

### `docs/governance/STATUS.md`

Recommended status entry:

```text
Evidence Topology Gate is active doctrine for reasoning topology selection, proof-chain preservation, bounded Hermes swarm and persistent role-team handoff constraints.
```

Explicit non-implementation note:

```text
It does not add a runtime, worker dispatcher, scheduler, queue, graph engine, schema, test, operation, platform component, OpenWebUI plugin or Hermes configuration.
```

### `CHANGELOG.md`

Recommended future changelog item:

```text
Added Evidence Topology Gate doctrine, roadmap addendum, fictional examples, schema candidate note and doctrine bridges for single-context, fan-out extraction, persistent role-team handoff and bounded Hermes swarm governance.
```

### Root `README.md`

Recommended public-facing summary:

```text
Pantheon does not choose between single-agent and multi-agent as a slogan. It first asks what shape the proof has. When evidence must be connected across sources, Pantheon preserves a single primary reasoning context. When extraction can safely be distributed, workers return evidence items, not authority.
```

## Current active content

Current active doctrine already exists in:

- `docs/governance/EVIDENCE_TOPOLOGY_GATE.md`.

Current roadmap addendum exists in:

- `docs/governance/EVIDENCE_TOPOLOGY_ROADMAP.md`.

Current fictional examples exist in:

- `docs/examples/evidence_topology/`.

## Boundary

This reconciliation note is documentation-level only.

It does not:

- add or modify schemas;
- add tests;
- add operations tooling;
- modify platform files;
- modify Docker or environment configuration;
- execute Hermes;
- define an OpenWebUI plugin;
- create a LangGraph runtime;
- create a swarm controller;
- create a message bus;
- promote memory;
- approve external tools.

## Final rule

```text
Index the doctrine carefully.
Do not turn topology governance into topology execution.
```
