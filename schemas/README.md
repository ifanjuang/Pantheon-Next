# Governance Schemas

Status: implemented validation baseline — D3 reconciliation pending

This directory contains declarative validation schemas for Pantheon Next governance objects.

Schemas define structure only.

They do not execute workflows, run tools, install Hermes profiles, route providers, schedule jobs, promote memory or mutate governance state.

The schema baseline can lag active doctrine while a reconciliation issue is open. Always verify `docs/governance/STATUS.md`, `docs/governance/AUTHORITY_INDEX.md` and related reconciliation issues before treating a schema as fully canonical for a newly stabilized doctrine cluster.

## Scope

Implemented schema files:

- `document_knowledge_slice.schema.yaml` (transport-neutral validation contract for one source document, explicit parser observation, provenance-bearing chunks, Project Document Card, optional versioned Knowledge publication and optimistic-write events. Validation only; parsing, persistence, synchronization and editing remain in a separately reviewed external adapter.)
- `work_issue_slice.schema.yaml` (candidate validation contract for one Work Issue projection: issue, comments, external Hermes runs and material events. It carries the single business status, separate run status, normalized return, controlled transition shape and optimistic-version fields. Validation only; persistence and writes remain in a separately reviewed external adapter.)
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
- `mvp_governed_loop_objects.schema.yaml` (MVP vertical validation bundle: closed human-decision vocabulary; structured commitment and advisory grounding metadata; decision identity/integrity; separate retention authorization. Validation only; no gate runtime or consequence execution.)
- `architecture-proof-register/` (domain family: shared vocabularies, document_family, indexed_document_version, version_event, proof_entry, review_trigger — consequence on the K axis, approval on C)
- `architecture-project-understanding/` (candidate domain family. Belief contract: shared vocabularies, stable_object, attribute_claim, calibration, derivation, evidence, doubt, contradiction, human_override, canonization. Program & conformance: program, requirement, classification, classification_scheme, space_group, program_change, deviation. Project object model: spatial_node, object_identity, object_relation, object_group, property_set, instance_override, object_note, phase_state, analysis_context_candidate. Status/use vocabularies aligned with the proof register; the object model describes the project world and references the Pantheon registers. See `docs/domain-packs/architecture/PROJECT_UNDERSTANDING.md`, `docs/governance/PROGRAM_AND_CONFORMANCE.md` and `docs/domain-packs/architecture/PROJECT_OBJECT_MODEL.md`)
- `role_signal.schema.yaml`
- `workflow_manifest.schema.yaml`
- `skill_manifest.schema.yaml`
- `context_pack.schema.yaml`
- `install_verification_evidence.schema.yaml` (input contract for the read-only `verify_install` mcp-server tool: provided log / liveness / check evidence the tool classifies into a verdict. Documents the recommended shape; the permissive classifier reports missing signals as capability gaps rather than rejecting, so the schema is not enforced as a gate. See `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`)
- `observability_evidence.schema.yaml` (input contract for the read-only `verify_observability` mcp-server tool: provided signal-inventory / freshness / error evidence the tool classifies into an observability verdict. Same documented-not-enforced posture as the install evidence schema. See `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`)
- `backup_evidence.schema.yaml` (input contract for the read-only `verify_backup` mcp-server tool: provided backup-presence / freshness / restore evidence the tool classifies into a recoverability verdict. Same documented-not-enforced posture as the other evidence schemas. See `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`)
- `exposure_evidence.schema.yaml` (input contract for the read-only `verify_exposure` mcp-server tool: provided reach / auth / scope evidence the tool classifies into an exposure-surface safety verdict. Same documented-not-enforced posture as the other evidence schemas. See `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`)
- `update_evidence.schema.yaml` (input contract for the read-only `verify_update` mcp-server tool: a provided current version and latest available version the tool compares into an update-availability verdict. Same documented-not-enforced posture as the other evidence schemas. See `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`)
- `verification_preset.schema.yaml` (per-module declaration binding the read-only verification family — install / observability / backup / exposure / update — to a module: which verifications apply and the thresholds the evidence should meet. Structure only; it runs no verification, gathers no evidence and decides nothing. Read by the `load_verification_preset` mcp-server tool, which validates it and projects it into a verification plan as data. See `docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`)

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

## Governed composition fields

Workflow Manifest also supports an optional `governed_composition` object for a manifest forged on demand by HEPHAISTOS from declared capabilities (`docs/governance/CAPABILITY_REGISTRY.md`, "Governed composition" in `docs/governance/WORKFLOW_SCHEMA.md`).

It validates governance metadata only:

- `forged_by` (HEPHAISTOS) and `forge_status` (candidate by default — forging does not authorize);
- `composition_loop`: retrieve/reuse/revise/retain policies mapped to existing governance;
- `capability_steps`: per-step governance signatures (capability_id, optional `skill_manifest_ref` join to `skill_manifest.skill_id`, declared/forbidden scope, required Task Contract, evidence pack shape, `approval_ceiling` C0–C5, `register_behavior`, `risk_class` low/medium/high/critical, refusal tests, dependencies);
- `gates`: `pre_execution_eligibility` (arbiter ZEUS; `decision` allow / allow_with_gate / block / needs_revision / needs_evidence) and `post_execution_evidence` (`answer_verification` V0–V4, `probative_certainty` E0–E4, register rule).

These fields do not compose, dispatch, schedule or execute anything. The `x-boundary` block records `composition_dispatch: false` and `forge_execution: false`.

## Phase D3 partial reconciliation

This pass adds or confirms:

- `module_manifest.schema.yaml` as the generic module/capability declaration contract;
- `skill_manifest.schema.yaml` remains available as a narrower skill/watchlist profile;
- optional `evidence_items[].claim_status` for claim-ledger review posture (`supported`, `weak`, `unverified`, `contradicted`, `out_of_scope`), without replacing `confidence`;
- the broader scope vocabulary remains valid for repository and governance work;
- schema example validation dependencies are required by tests rather than silently skipped.

A follow-up seed adds `shared_defs.schema.yaml` as a non-consuming shared vocabulary file. It intentionally does not introduce `$ref` consumers until local reference resolution is handled in tests.

The `architecture-project-understanding/` family now factors its cross-cutting definitions into `architecture-project-understanding/shared.schema.yaml` and references them with cross-file `$ref: "shared.schema.yaml#/$defs/X"`. Validators (the two test suites and `.github/scripts/check_apu_referential_integrity.py`) resolve these through a small `referencing.Registry` that exposes that family's `shared.schema.yaml` under its bare filename. The core belief-contract schemas are factored; the program/conformance and object-model schemas still keep their schema-specific enums local and can be migrated incrementally (issue #169).

Further D3 factoring may still introduce shared definitions if that reduces duplication without changing doctrine.

A minimal schema example validation test exists in `tests/test_schema_examples.py`.

## MVP vertical reconciliation (#359)

The MVP bundle formalizes the following reviewed structures:

- the closed decision enum `approve`, `refuse`, `request_revision`, `request_more_evidence`;
- structured `commitment_flags[]` entries with `phrase` and `risk`;
- advisory-only `grounding_review` metadata;
- `decision_id`, `recorded_at`, optional supersession, SHA-256 content digests and honest identity assurance;
- a separate `retention_authorization` required on a Register Candidate.

The enum in `mvp_governed_loop_objects.schema.yaml#/$defs/decision_value` is the single vendorable machine-readable vocabulary. A candidate output may expose a subset as available choices, but it cannot define or widen the governed set.

`identity_assurance: declared` records an unverified human declaration. `identity_assurance: authenticated` requires an `authenticated_principal` supplied by the reviewed cockpit session. The schema validates the distinction; it performs no authentication.

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
