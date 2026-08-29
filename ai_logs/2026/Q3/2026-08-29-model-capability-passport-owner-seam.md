# AI log — Model Capability Passport owner seam

Date: 2026-08-29
Issue: #787
Base: `dc2951fd341ecb85d1fcd4db149abef5ae1be95a`

## Objective

Converge `MODEL_CAPABILITY_PASSPORT.md` onto its distinct model-specific review responsibility without absorbing a useful specialization or creating executable schema semantics by documentation alone.

## Scope

Changed:

- `docs/governance/MODEL_CAPABILITY_PASSPORT.md`
- this ai_log

Not changed:

- `schemas/capability_passport.schema.yaml`
- `UNIFORM_CAPABILITY_GOVERNANCE.md`
- authority indexes
- runtime, provider, binding, Cockpit or policy implementation

## Observed need

`MODEL_CAPABILITY_PASSPORT.md` is already an indexed active-support specialization, but it repeated substantial generic doctrine owned by the universal capability, Task Contract, Evidence, approval, memory and Hermes-integration owners.

The executable `schemas/capability_passport.schema.yaml` also currently has no `model` capability primitive and no model-specific fields such as model identity, modality, context limit, serving posture or failure-mode review.

The previous document correctly said its model shape was non-executable, but the surrounding wording could still be read as though the documentary block automatically extended the universal executable Capability Passport.

## Overlap analysis

Existing owners remain authoritative:

- `UNIFORM_CAPABILITY_GOVERNANCE.md` — one universal capability law and passport path;
- `schemas/capability_passport.schema.yaml` — current executable universal Capability Passport shape;
- `MODULE_ACTIVATION.md` — scoped capability activation;
- `TASK_CONTRACTS.md` / Execution Admission owners — task/run legitimacy;
- `EVIDENCE_PACK.md` — Evidence packaging;
- `APPROVALS.md` — approval requirements;
- `MEMORY.md` — governed retention;
- `HERMES_INTEGRATION.md` — runtime/client/PDP/PEP/Cockpit placement.

The retained model owner now covers only model-specific review data and interpretation: exact model/release, serving posture, data exposure, retention/training posture, modalities, reviewed task families, professional-use ceiling, known failure modes, comparison triggers and safe fallback.

## Affected consumers

Current exact-file search found only:

- governance README navigation;
- Governance Authority Index placement;
- historical ai_log provenance.

No executable schema, runtime or current non-document consumer depends on the removed prose or documentary field names.

## Convergence

The document now:

1. declares `Boundary profile: active_support_doctrine`;
2. references generic owners instead of repeating their rules;
3. makes the current schema mismatch explicit;
4. treats `model_capability_review` as documentary specialization, not executable schema input;
5. separates model `review_status` from scoped activation;
6. replaces `authorized_task_families` with `reviewed_task_families` so review is not confused with task authorization;
7. retains model-specific serving/data/task/failure-mode/comparison semantics;
8. keeps runtime and governed projection responsibilities external to this owner.

Pre-log compare:

```text
MODEL_CAPABILITY_PASSPORT.md   +130 / -260
```

Net doctrine reduction: 130 lines.

## Migration and rollback

Documentation-only convergence. There is no executable model-passport schema or consumer to migrate.

If an executable model-specific contract is later required, it must be proposed explicitly under `schemas/` with migration and consumer review; this documentation change does not pre-authorize it.

Rollback is a normal Git revert.

## Role / Rite / Space

- Role: THEMIS for authority and authorization boundaries; MNEMOSYNE for owner/provenance continuity.
- Rite: Concordance des sources across exact main, #787, the universal Capability Passport schema and capability-governance owners.
- Space: Pantheon Next governance repository.

## Authority impact

No authority promotion, transfer or new gate.

The model-specific review constrains suitability only. It does not activate a capability, authorize a task, select a provider, lower approval, admit Evidence or validate an output.

## Runtime impact

None. No model router, provider router, model registry, serving process, benchmark runner, client, Hermes skill, scheduler, queue, policy implementation or external action is created or changed.

## Preserved invariants

```text
model available != model reviewed
model reviewed != model activated
model selected != task authorized
model confidence != Evidence
reviewed task family != task authorization
documentary specialization != executable schema
provider selected != authority transfer
runtime success != authorization
projection != persistence
PDP decision != PEP execution
```

## Verification

Before merge:

- inspect the exact PR patch;
- confirm no schema/runtime/index change is present;
- run Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency on the exact final HEAD;
- read reviews, review threads and PR comments;
- merge only with the expected final HEAD SHA.
