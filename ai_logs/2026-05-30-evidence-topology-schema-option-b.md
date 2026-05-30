# Evidence Topology Schema Option B

Date: 2026-05-30

## Summary

Applied schema option B for Evidence Topology.

This pass modifies the two central governance schemas and their official examples:

- `schemas/task_contract.schema.yaml`;
- `schemas/evidence_pack.schema.yaml`;
- `schemas/examples/task_contract.example.yaml`;
- `schemas/examples/evidence_pack.example.yaml`;
- `schemas/README.md`.

## Changed

### Task Contract schema

Added optional `reasoning_topology` metadata.

Supported topology values:

- `single_primary_reasoning_context`;
- `fanout_extract_then_single_synthesis`;
- `parallel_independent_workers`;
- `router`;
- `sequential_handoff`;
- `persistent_role_team_handoff`;
- `bounded_hermes_swarm`.

The field validates governance metadata only.

It does not dispatch workers, route providers, schedule work, execute Hermes, create a graph runtime or approve anything.

### Evidence Pack schema

Added optional:

- `evidence_items`;
- `handoff_artifacts`;
- `reasoning_topology_record`.

These fields support structured proof-chain review, handoff artifact review and topology accountability.

They are not runtime traces, hidden chain-of-thought archives or approval mechanisms.

### Examples

Updated the official Task Contract and Evidence Pack examples to include the new optional fields.

The examples remain fictional and candidate-oriented.

### Schema README

Updated `schemas/README.md` with a Phase D2 section explaining Evidence Topology fields and boundaries.

## Boundary

This intervention does not implement:

- runtime behavior;
- topology dispatch;
- provider routing;
- scheduler;
- queue;
- graph runtime;
- Hermes execution;
- OpenWebUI plugin behavior;
- automatic approval;
- automatic memory promotion.

It does not modify:

- `workflow_manifest.schema.yaml`;
- tests;
- operations tooling;
- platform files;
- Docker files;
- environment files.

## Tests

No tests were added or modified in this pass.

A future protected pass should update schema validation tests if required.

## Changelog note

`CHANGELOG.md` was not updated in this pass because the file is long and the connector returned truncated reads. Avoiding a broad replacement was safer than risking history loss.

A future focused changelog patch should record this as a Phase D2 Evidence Topology schema update.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Core rule

```text
The unit of reasoning is not the agent.
The unit of reasoning is the proof chain.
```

## Files touched

- `schemas/task_contract.schema.yaml`
- `schemas/evidence_pack.schema.yaml`
- `schemas/examples/task_contract.example.yaml`
- `schemas/examples/evidence_pack.example.yaml`
- `schemas/README.md`
- `ai_logs/2026-05-30-evidence-topology-schema-option-b.md`
