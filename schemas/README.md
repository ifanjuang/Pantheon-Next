# Governance Schemas

Status: implemented — reconciled schema baseline

This directory contains declarative validation schemas for Pantheon Next governance objects.

Schemas define structure only.

They do not execute workflows, run tools, install Hermes profiles, route providers, schedule jobs, promote memory or mutate governance state.

## Scope

Implemented schema files:

- `task_contract.schema.yaml`
- `task_contract_revision.schema.yaml`
- `evidence_pack.schema.yaml`
- `memory_candidate.schema.yaml`
- `role_signal.schema.yaml`
- `workflow_manifest.schema.yaml`
- `skill_manifest.schema.yaml`
- `context_pack.schema.yaml`

Examples are stored in `schemas/examples/`.

## Governance references

Each schema includes `governance_refs` defaults to preserve traceability to the Markdown governance documents that define the doctrine for the object being validated.

A schema reference to a stub document does not make that document migrated doctrine.

Always check `docs/governance/STATUS.md` before treating any referenced governance document as canonical migrated content.

## Phase D1 reconciliation

This baseline aligns schema vocabulary with active doctrine for:

- canonical Pantheon Role names in `AGENTS.md`;
- C0-C5 approval levels in `APPROVALS.md`;
- scope categories in `SCOPE_ISOLATION.md`;
- Task Contract boundaries in `TASK_CONTRACTS.md`;
- Evidence Pack structure in `EVIDENCE_PACK.md`;
- Memory Candidate structure in `MEMORY.md`;
- Role Signal vocabulary in `ROLE_SIGNALS.md`;
- Workflow Manifest doctrine in `WORKFLOW_SCHEMA.md`;
- Skill Watchlist and candidate skill boundaries in `SKILL_WATCHLIST.md`;
- Context Pack boundaries in `CONTEXT_PACKS.md`.

## Phase D2 evidence topology fields

This baseline also includes optional Evidence Topology fields for Task Contracts, Evidence Packs and Workflow Manifests.

Task Contract now supports optional:

- `reasoning_topology`.

Evidence Pack now supports optional:

- `evidence_items`;
- `handoff_artifacts`;
- `reasoning_topology_record`.

Workflow Manifest now supports optional:

- `reasoning_topology_requirements`;
- `evidence_item_requirements`;
- `handoff_artifact_requirements`.

These fields validate governance metadata only.

They do not dispatch workers, route providers, schedule tasks, create a graph runtime, run Hermes, approve outputs or promote memory.

A minimal schema example validation test exists in `tests/test_schema_examples.py`.

## Boundary rule

Schemas are validation contracts.

They are not:

- runtime components;
- provider routers;
- approval engines;
- memory promotion engines;
- workflow engines;
- Hermes installers;
- OpenWebUI plugins;
- execution gateways;
- tool routers;
- topology dispatchers;
- schedulers;
- queues.
