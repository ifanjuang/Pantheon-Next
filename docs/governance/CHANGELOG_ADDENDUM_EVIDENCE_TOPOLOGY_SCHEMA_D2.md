# Changelog Addendum — Evidence Topology Schema D2

Date: 2026-05-30

Status: changelog addendum.

This addendum records the protected schema pass for Evidence Topology.

It exists because the main `CHANGELOG.md` is long and connector reads were truncated during this pass. A broad replacement was avoided to prevent accidental history loss.

## Summary

Evidence Topology doctrine is now reflected in the two central governance schemas:

- `schemas/task_contract.schema.yaml`;
- `schemas/evidence_pack.schema.yaml`.

The official schema examples were updated accordingly.

## Added to Task Contract schema

Optional field:

```text
reasoning_topology
```

Supported topology values:

```text
single_primary_reasoning_context
fanout_extract_then_single_synthesis
parallel_independent_workers
router
sequential_handoff
persistent_role_team_handoff
bounded_hermes_swarm
```

Boundary:

```text
reasoning_topology is governance metadata.
It is not runtime dispatch.
```

## Added to Evidence Pack schema

Optional fields:

```text
evidence_items
handoff_artifacts
reasoning_topology_record
```

Boundary:

```text
Evidence Items support review.
Handoff Artifacts preserve continuity.
Topology Records preserve accountability.
None of them approve, dispatch, execute or promote memory.
```

## Examples updated

- `schemas/examples/task_contract.example.yaml`;
- `schemas/examples/evidence_pack.example.yaml`.

## Tests added

- `tests/test_schema_examples.py`.

The test validates schema examples and checks that Evidence Topology remains non-runtime through boundary flags:

```text
topology_dispatch: false
hidden_chain_of_thought_archive: false
```

## Explicitly not implemented

This pass does not implement:

- runtime behavior;
- topology dispatcher;
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
- operations tooling;
- platform files;
- Docker files;
- environment files.

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
