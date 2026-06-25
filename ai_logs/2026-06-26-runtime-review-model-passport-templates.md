# AI Log — Runtime review and model passport templates

Date: 2026-06-26

## Request

Create human-fillable templates for the validation-only promotion path:

```text
templates/external_runtime_review_candidate.yaml
templates/model_capability_passport_candidate.yaml
```

## Source of truth read

Required governance documents reviewed:

```text
docs/governance/STATUS.md
docs/governance/MODULAR_DOMAIN_REORIENTATION.md
docs/governance/CAPABILITY_PLACEMENT.md
docs/governance/DOMAIN_PACK_SPEC.md
```

Additional documents/templates reviewed:

```text
docs/governance/RUNTIME_REVIEW_MODEL_PASSPORT_VALIDATION_PROMOTION.md
templates/mcp_capability_passport.yaml
templates/mcp_external_tool_review.md
```

## Files created

```text
templates/external_runtime_review_candidate.yaml
templates/model_capability_passport_candidate.yaml
```

## Decision classification

Accepted:

```text
Human-fillable template scaffolds before schema work.
Candidate-only boundary metadata in each template.
Validation level L0-L3 field in each template.
Gate recommendation field in each template.
Accepted / refused / to_verify / to_arbitrate sections in each template.
```

Refused:

```text
No schema.
No validator.
No test.
No mcp-server change.
No runtime.
No OpenWebUI configuration.
No Hermes skill.
No model router.
No provider selection.
No approval engine.
No memory promotion.
No external action.
```

To verify:

```text
Whether these templates should later become schema-backed contracts.
Whether the field vocabulary should be aligned with MCP capability-passport conventions.
Whether a validation report candidate template should be added next.
```

To arbitrate:

```text
Whether to proceed to schemas/.
Whether to proceed to tests/.
Whether to proceed to mcp-server read-only functions.
Whether validation is advisory or blocking before adapter use.
```

## Repo state

```text
Documented non-implemented.
Templates only.
No protected path changed.
No executable validation created.
```

## Note

The first attempted runtime-review template used overly operational host-control vocabulary and was blocked by the GitHub connector safety controls. The final template uses abstract governance categories.
