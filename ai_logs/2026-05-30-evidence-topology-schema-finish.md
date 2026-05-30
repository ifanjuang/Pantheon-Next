# Evidence Topology Schema Finish

Date: 2026-05-30

## Summary

Finished the Evidence Topology schema pass by adding a minimal read-only validation test and a changelog addendum.

This follows the Option B schema update that added optional Evidence Topology fields to:

- `schemas/task_contract.schema.yaml`;
- `schemas/evidence_pack.schema.yaml`.

## Added

- `tests/test_schema_examples.py`;
- `docs/governance/CHANGELOG_ADDENDUM_EVIDENCE_TOPOLOGY_SCHEMA_D2.md`.

## Test scope

`tests/test_schema_examples.py` validates the official examples against their schemas:

- `task_contract.example.yaml` against `task_contract.schema.yaml`;
- `evidence_pack.example.yaml` against `evidence_pack.schema.yaml`;
- `memory_candidate.example.yaml` against `memory_candidate.schema.yaml`;
- `role_signal.example.yaml` against `role_signal.schema.yaml`;
- `workflow_manifest.example.yaml` against `workflow_manifest.schema.yaml`;
- `skill_manifest.example.yaml` against `skill_manifest.schema.yaml`;
- `context_pack.example.yaml` against `context_pack.schema.yaml`.

It also checks that Evidence Topology fields remain documentary through boundary flags:

- `reasoning_topology` exists in Task Contract schema;
- `evidence_items`, `handoff_artifacts` and `reasoning_topology_record` exist in Evidence Pack schema;
- `topology_dispatch` remains `false`;
- `hidden_chain_of_thought_archive` remains `false`.

## Changelog handling

A dedicated addendum was created instead of rewriting the main `CHANGELOG.md` because the connector truncated long file reads during the pass.

The addendum records the D2 schema update without risking accidental changelog history loss.

## Boundary

This finish pass does not implement:

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
