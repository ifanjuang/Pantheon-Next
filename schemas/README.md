# Governance Schemas

Status: implemented validation baseline — D3 reconciliation pending

This directory contains declarative validation schemas for Pantheon Next governance objects.

Schemas define structure only.

They do not execute workflows, run tools, install Hermes profiles, route providers, schedule jobs, promote memory or mutate governance state.

The schema baseline can lag active doctrine while a reconciliation issue is open. Always verify `docs/governance/STATUS.md`, `docs/governance/AUTHORITY_INDEX.md` and related reconciliation issues before treating a schema as fully canonical for a newly stabilized doctrine cluster.

## Scope

Implemented schema files:

- `task_contract.schema.yaml`
- `task_contract_revision.schema.yaml`
- `evidence_pack.schema.yaml`
- `register_candidate.schema.yaml` (formerly `memory_candidate.schema.yaml`; certainty uses the E0–E4 axis)
- `register_link.schema.yaml` (typed, directed relation between register entries: depends_on, impacts, conflicts_with, supersedes…)
- `impact_review.schema.yaml` (cascade review opened when a register entry changes; records proposed consequences and human decisions)
- `shared_axes.schema.yaml` (the E/V/K/C axes, owned by GLOSSARY.md)
- `shared_defs.schema.yaml` (seed for shared schema vocabulary; currently defines `scope_type` and is not yet consumed by other schemas)
- `capability_passport.schema.yaml`
- `module_manifest.schema.yaml` (generic capability/module declaration; `skill_manifest` remains a narrower profile)
- `policy_decision.schema.yaml`
- `answer_status.schema.yaml`
- `architecture-proof-register/` (domain family: shared vocabularies, document_family, indexed_document_version, version_event, proof_entry, review_trigger — consequence on the K axis, approval on C)
- `architecture-project-understanding/` (candidate domain family. Belief contract: shared vocabularies, stable_object, attribute_claim, calibration, derivation, evidence, doubt, contradiction, human_override, canonization. Program & conformance: program, requirement, classification, classification_scheme, space_group, program_change, deviation. Project object model: spatial_node, object_identity, object_relation, object_group, property_set, instance_override, object_note, phase_state, analysis_context_candidate. Status/use vocabularies aligned with the proof register; the object model describes the project world and references the Pantheon registers. See `docs/governance/ARCHITECTURE_PROJECT_UNDERSTANDING.md`, `docs/governance/PROGRAM_AND_CONFORMANCE.md` and `docs/governance/ARCHITECTURE_PROJECT_OBJECT_MODEL.md`)
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
- Register Candidate structure in `MEMORY.md` and the Registre Probatoire vocabulary;
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

## Phase D3 partial reconciliation

This pass adds or confirms:

- `module_manifest.schema.yaml` as the generic module/capability declaration contract;
- `skill_manifest.schema.yaml` remains available as a narrower skill/watchlist profile;
- optional `evidence_items[].claim_status` for claim-ledger review posture (`supported`, `weak`, `unverified`, `contradicted`, `out_of_scope`), without replacing `confidence`;
- the broader scope vocabulary remains valid for repository and governance work;
- schema example validation dependencies are required by tests rather than silently skipped.

A follow-up seed adds `shared_defs.schema.yaml` as a non-consuming shared vocabulary file. It intentionally does not introduce `$ref` consumers until local reference resolution is handled in tests.

Further D3 factoring may still introduce shared definitions if that reduces duplication without changing doctrine.

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
