# Runtime Review + Model Passport Validation Promotion

Status: validation-only — promotion proposal for read-only validation. Documented non-implemented.

This document promotes the next governance step for:

```text
docs/governance/EXTERNAL_RUNTIME_THREAT_MODEL_REVIEW.md
docs/governance/MODEL_CAPABILITY_PASSPORT.md
```

It defines how those two support-doctrine objects may become validation-checkable without turning Pantheon Next into a runtime, model router, scanner, installer, provider gateway, scheduler, queue, approval engine or memory engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Decision summary

Accepted:

```text
Promote External Runtime Threat Model Review toward read-only validation.
Promote Model Capability Passport toward read-only validation.
Use the MCP Policy Server only as a read-only policy / validation surface if implementation is later approved.
Keep schemas and tests blocked until explicitly approved.
Keep all runtime execution outside Pantheon.
```

Refused:

```text
No runtime scanner.
No automatic sandbox.
No model router.
No benchmark runner.
No provider selection engine.
No OpenWebUI configuration.
No Hermes skill.
No automatic adapter installation.
No automatic approval.
No memory promotion.
No external action.
```

To verify:

```text
Whether existing MCP policy-server conventions are sufficient for these checks.
Whether schema-backed validation is needed immediately or later.
Whether Hermes adapters should carry these declarations as metadata.
Whether Pantheon Control should display validation status.
```

To arbitrate:

```text
Whether to modify schemas/.
Whether to modify tests/.
Whether to modify mcp-server/.
Whether to add templates for human-filled review records.
Whether validation should be soft advisory or blocking before adapter use.
```

## Promotion target

The target is not implementation.

The target is this governed capability:

```text
Given a Runtime Review Candidate or Model Passport Candidate,
Pantheon can classify whether the declaration is complete enough to be reviewed,
and whether it should be accepted, refused, sent to verification or sent to arbitration.
```

The expected output remains data:

```text
Validation Candidate
Completeness Report
Risk Classification
Missing Fields
Gate Recommendation
Human Decision Required
```

No validation check may produce:

```text
runtime execution
model selection
provider routing
external transmission
canonical approval
memory promotion
professional validation
```

## Validation levels

Use four levels:

```text
L0 — document exists
L1 — required fields present
L2 — field values are internally coherent
L3 — gate recommendation can be produced
```

Meaning:

| Level | Meaning | Allowed result |
|---|---|---|
| L0 | A review/passport record exists. | candidate only |
| L1 | Required fields are present. | completeness report |
| L2 | Values do not contradict declared scope, risk and effect. | to_verify / blocked / needs_review |
| L3 | A gate recommendation can be stated. | allow_read_only / candidate_only / needs_approval / block |

L3 is still not approval. It is a recommendation for a visible gate.

## Candidate object — runtime review

A Runtime Review Candidate is checkable when it declares at least:

```text
runtime_name
reviewed_ref
system_role
binding_status
exposure_posture
privileged_capabilities
data_access
external_effects
memory_effects
model_effects
scheduling_effects
host_control_surface
untrusted_content_paths
prompt_injection_posture
permission_granularity
auditability
pantheon_gate_required
approval_ceiling
evidence_expectation
safe_default
decision
repo_state
```

Validation may identify:

```text
missing mandatory field
unknown exposure posture
unclear host-control surface
unclear external effect
unclear memory effect
unclear approval ceiling
incompatible decision / risk posture
runtime power treated as normal skill
insufficient safe default
```

## Candidate object — model passport

A Model Passport Candidate is checkable when it declares at least:

```text
model_id
display_name
version_or_release
provider_or_runtime
processing_posture
serving_surface
status
modality
context_window
input_classes_allowed
input_classes_forbidden
output_classes_allowed
output_classes_forbidden
data_exposure
retention_or_training_unknowns
authorized_task_families
forbidden_task_families
professional_use_ceiling
evidence_expectation
known_failure_modes
uncertainty_behavior
comparison_required
approval_ceiling
memory_behavior
fallback_model_or_path
review_date
reviewed_by
decision
```

Validation may identify:

```text
missing mandatory field
unknown processing posture
sensitive data allowed without approval ceiling
professional-use ceiling too high for evidence expectation
task family allowed despite declared failure mode
memory behavior inconsistent with Memory doctrine
external model with unclear retention status
model treated as final validator
```

## Gate recommendation vocabulary

Read-only validation may return only these recommendations:

```text
allow_read_only
allow_candidate_only
needs_approval
needs_more_evidence
needs_human_review
needs_security_review
needs_adapter_review
block
```

The recommendation is not enforcement unless an approved external runtime honors it.

## MCP Policy Server promotion path

If implementation is later approved, the MCP Policy Server may expose read-only validation functions such as:

```text
validate_external_runtime_review
validate_model_capability_passport
classify_runtime_review_gate
classify_model_passport_gate
```

These names are proposal names only. They do not create MCP tools by themselves.

The functions, if later implemented, must:

```text
read candidate data
check required fields
check coherence rules
return a candidate report
never execute runtime work
never route providers
never select a model
never approve
never promote memory
never send externally
```

## Schema promotion path

Schema-backed validation is useful, but blocked until explicitly approved.

Allowed current state:

```text
proposal only
no schemas/ modification
no tests/ modification
no generated validator
```

If approved later, the schema work package should create separate declarative contracts for:

```text
external_runtime_review_candidate
model_capability_passport_candidate
validation_report_candidate
```

Any schema must include boundary metadata equivalent to:

```text
candidate_only: true
canonical_effect: false
runtime_effect: false
external_action: false
memory_promotion: false
```

## Template promotion path

Human-fillable templates may be added before schemas if useful.

Candidate templates:

```text
templates/external_runtime_review_candidate.yaml
templates/model_capability_passport_candidate.yaml
```

Templates are not schemas and not validators. They are scaffolds.

## Control / dashboard projection

Pantheon Control or any exposure surface may later display:

```text
review exists / missing
passport exists / missing
completeness level L0-L3
risk class
host-control surface
data exposure
approval ceiling
gate recommendation
human decision required
```

The display does not validate. It projects status.

## Repository state after this promotion

```text
Documented non-implemented.
Validation-only proposal.
No schema.
No tests.
No mcp-server change.
No runtime.
No OpenWebUI configuration.
No Hermes skill.
No external action.
No memory promotion.
```

## Required next explicit approvals

Before implementation, obtain explicit approval for any of:

```text
schemas/ changes
tests/ changes
mcp-server/ changes
operations/ changes
platform/ changes
Docker changes
.env changes
```

## Boundary phrase

```text
The passport declares.
The review qualifies.
The validator reports.
The gate recommends.
Zeus arbitrates status.
The human decides.
```
