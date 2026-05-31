# Workflow Manifest Evidence Topology Finish

Date: 2026-05-30

## Summary

Finished the Workflow Manifest side of the Evidence Topology schema cycle.

The Workflow Manifest now declares optional governance requirements for topology, Evidence Items and Handoff Artifacts without adding runtime semantics.

## Files changed

- `schemas/workflow_manifest.schema.yaml`
- `schemas/examples/workflow_manifest.example.yaml`
- `tests/test_schema_examples.py`
- `schemas/README.md`
- `ai_logs/2026-05-30-workflow-manifest-evidence-topology-finish.md`

## Added to Workflow Manifest schema

Optional fields:

- `reasoning_topology_requirements`;
- `evidence_item_requirements`;
- `handoff_artifact_requirements`.

These fields let a governed workflow declare what it expects from topology selection, source-linked evidence and bounded handoff artifacts.

They do not execute anything.

## Example update

`schemas/examples/workflow_manifest.example.yaml` now includes:

- allowed topologies;
- default topology;
- topology selection policy;
- evidence policy;
- handoff policy;
- approval policy;
- memory policy;
- required governance references;
- Evidence Item requirements;
- Handoff Artifact requirements;
- explicit runtime-drift risks.

## Test update

`tests/test_schema_examples.py` now verifies that Workflow Manifest includes:

- `reasoning_topology_requirements`;
- `evidence_item_requirements`;
- `handoff_artifact_requirements`;
- `topology_dispatch: false`;
- `hidden_chain_of_thought_archive: false`.

## Boundary

This intervention does not implement:

- runtime behavior;
- workflow execution;
- topology dispatcher;
- provider routing;
- scheduler;
- queue;
- graph runtime;
- Hermes execution;
- OpenWebUI plugin behavior;
- automatic approval;
- automatic memory promotion.

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
