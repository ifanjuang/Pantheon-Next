# Governance Schemas

Status: implemented — initial schema baseline

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

Examples are stored in `schemas/examples/`.

## Governance references

Each schema includes `x-governance_refs` to preserve traceability to the Markdown governance documents that define the doctrine for the object being validated.

A schema reference to a stub document does not make that document migrated doctrine.

Always check `docs/governance/STATUS.md` before treating any referenced governance document as canonical migrated content.

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
- execution gateways.
