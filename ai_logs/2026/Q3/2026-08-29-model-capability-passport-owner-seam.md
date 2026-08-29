# AI log — Model Capability Passport owner seam

Date: 2026-08-29
Issue: #787
Original base: `dc2951fd341ecb85d1fcd4db149abef5ae1be95a`

## Objective

Converge `MODEL_CAPABILITY_PASSPORT.md` onto its distinct model-specific review responsibility without absorbing a useful specialization or creating executable schema semantics by documentation alone.

## Scope

Changed:

- `docs/governance/MODEL_CAPABILITY_PASSPORT.md`
- `templates/model_capability_passport_candidate.yaml`
- `docs/governance/RUNTIME_REVIEW_MODEL_PASSPORT_VALIDATION_PROMOTION.md`
- `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`
- `.github/scripts/truncation_ack.txt` — temporary deliberate-shrink acknowledgement required by the existing guard
- this ai_log

Not changed:

- `schemas/capability_passport.schema.yaml`
- `UNIFORM_CAPABILITY_GOVERNANCE.md`
- tests
- runtime, provider, binding, Cockpit or policy implementation
- governance checker logic

## Observed need

`MODEL_CAPABILITY_PASSPORT.md` is already an indexed active-support specialization, but it repeated substantial generic doctrine owned by the universal capability, Task Contract, Evidence, approval, memory and Hermes-integration owners.

The executable `schemas/capability_passport.schema.yaml` also currently has no `model` capability primitive and no model-specific fields such as model identity, modality, context limit, serving posture or failure-mode review.

The previous document correctly said its model shape was non-executable, but the surrounding wording could still be read as though the documentary block automatically extended the universal executable Capability Passport.

A late PR review then identified two real downstream inconsistencies that the initial exact-name search missed:

1. `templates/model_capability_passport_candidate.yaml` still exposed activation-like status values and task-family `allowed` semantics;
2. `RUNTIME_REVIEW_MODEL_PASSPORT_VALIDATION_PROMOTION.md` still declared the removed names mandatory, while `GOVERNANCE_AUTHORITY_INDEX.md` still described the owner as governing broader Evidence/approval responsibility.

The review was accepted and the dependent documentary artifacts were aligned in the same bounded slice.

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

Observed documentary consumers requiring alignment:

- governance README navigation — reference only; no change required;
- `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md` — owner description narrowed;
- `templates/model_capability_passport_candidate.yaml` — legacy filename retained, root contract aligned to `model_capability_review_candidate`;
- `docs/governance/RUNTIME_REVIEW_MODEL_PASSPORT_VALIDATION_PROMOTION.md` — validation proposal aligned to the review contract and universal-passport boundary;
- historical ai_log provenance — retained as history.

No executable schema, runtime or current non-document consumer was found for the removed documentary field names.

## Convergence

The model owner now:

1. declares `Boundary profile: active_support_doctrine`;
2. references generic owners instead of repeating their rules;
3. makes the current executable-schema mismatch explicit;
4. treats `model_capability_review` as documentary specialization, not executable schema input;
5. separates model `review_status` from scoped activation;
6. replaces `authorized_task_families` with `reviewed_task_families` so review is not confused with task authorization;
7. retains model-specific serving/data/task/failure-mode/comparison semantics;
8. keeps runtime and governed projection responsibilities external to this owner.

The dependent template now removes `sandbox`, `project_enabled` and `organization_enabled` review status values, removes per-task `allowed` authorization-like values and removes embedded approval/memory gate ownership. It instead records observational suitability plus references to the universal Capability Passport, activation and Task Contract where applicable.

The validation-only promotion document now validates a `Model Capability Review Candidate`, not a pseudo second Capability Passport. It preserves its legacy template path only for path compatibility and makes any future executable model-review schema a separate explicit decision.

The existing test `test_runtime_review_validation_status.py` protects the older proposal names `validate_model_capability_passport` and `classify_model_passport_gate` as proposal-only strings. Rather than modifying protected tests or pretending those functions exist, the validation note retains those two names explicitly as **legacy proposal aliases** while naming `validate_model_capability_review` / `classify_model_review_gate` as the preferred future proposal vocabulary. No MCP function is created.

The Governance Authority Index now describes the owner as model-specific review only; universal Capability Passport, activation, task/run legitimacy, Evidence and approval remain with their existing owners.

## Quantitative convergence

Initial model-owner reduction:

```text
MODEL_CAPABILITY_PASSPORT.md   365 -> 235 lines
Git diff                       +130 / -260
```

Net doctrine reduction: 130 lines.

The repository anti-truncation guard correctly rejected that deliberate shrink on the first exact HEAD. `.github/scripts/truncation_ack.txt` therefore carries exactly one temporary acknowledgement for this file. The guard itself is unchanged; the acknowledgement should be removed in the next bounded cleanup after the reduced file is merged into `main` baseline.

## Parallel-main check

While the review was being addressed, #818 merged to `main` as `7e10165567c675a3f21f573a935b1eaf82eee851`.

#818 changes only:

- `ADAPTERS_AND_BINDINGS.md`
- `REQUEST_LIFECYCLE.md`
- `SOURCE_NEED_AND_REGISTRY.md`
- `tests/test_source_document_owner_convergence.py`
- its ai_log

No file in this model-review slice overlaps #818. Final PR validation must still run against GitHub's current merge candidate before merge.

## Migration and rollback

Documentation/template convergence only. There is no executable model-review schema or runtime consumer to migrate.

The legacy template filename is deliberately retained to avoid unnecessary path churn; the current root record is `model_capability_review_candidate` and the validation proposal documents that compatibility fact.

The two legacy MCP proposal names are retained only as compatibility vocabulary for repository checks/history; they remain explicitly non-implemented.

If an executable model-specific contract is later required, it must be proposed explicitly under `schemas/` with migration and consumer review; this documentation change does not pre-authorize it.

Rollback is a normal Git revert.

## Role / Rite / Space

- Role: THEMIS for authority and authorization boundaries; MNEMOSYNE for owner/provenance continuity.
- Rite: Concordance des sources across exact main, #787, the universal Capability Passport schema, capability-governance owners and discovered documentary consumers.
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
proposal name != implemented MCP function
provider selected != authority transfer
runtime success != authorization
projection != persistence
PDP decision != PEP execution
```

## Verification

Before merge:

- inspect all exact PR patches, including the late-review corrections;
- confirm no executable schema/runtime/test/checker-logic change is present;
- confirm the Authority Index diff is limited to the model owner row;
- run Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency on the exact final HEAD/current merge candidate;
- reread reviews, review threads and PR comments after the final HEAD;
- resolve the two accepted late-review threads only after their corrections are visible;
- merge only with the expected final HEAD SHA.
