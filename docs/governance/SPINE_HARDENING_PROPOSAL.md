# Spine Hardening Proposal (step 2)

Status: validation-only proposal — protected-path schema work. Requires explicit approval before any edit under `schemas/` or `tests/`.

This is step 2 of `TARGET_ARCHITECTURE.md`: make the governance spine machine-checkable enough to prove one vertical later. This file is a proposal only. It changes no protected path.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Boundary

This document modifies no protected path. It changes no file under `schemas/`, `tests/`, `operations/`, `platform/`, `pyproject.toml`, Docker or `.env`.

The shapes below are printed inside a governance note. They are not executable schema files. They may be applied only after explicit approval.

## Minimal canonical set proposed

After approval, the minimal protected-path set would be:

```text
shared_axes.schema.yaml        E0–E4 / V0–V4 / K0–K4 / C0–C5 owned once
capability_passport.schema.yaml promoted from templates/mcp_capability_passport.yaml
policy_decision.schema.yaml     gate decision object; data, not execution
answer_status.schema.yaml       Answer Verification Gate status, including K0–K4 consequence
register_candidate.schema.yaml  Registre Probatoire candidate, with E6/#87
```

Plus a read-only validator, called here Doctor checks.

## Axis addition

The proposal adopts `K0–K4` as the consequence axis. `K` is intentionally distinct from `C0–C5`, because `C` is approval clearance. `K` answers what could happen if the answer or capability is acted on. `C` answers who must approve action.

`GLOSSARY.md` owns the axis name and now records it next to E, V and C.

## Passport operation guardrail

The blocking review note on #97 is accepted.

The eventual `capability_passport.schema.yaml` must preserve the operation semantics inherited from `templates/mcp_capability_passport.yaml`. It must not silently collapse register operations, runtime memory behavior and code-capability behavior into one flag.

Apply-time mapping rule:

```text
private-data read flag                 keep
external-state write flag              keep
code-capability flag from the template  keep, or document a deliberate explicit mapping
external-party transfer flag            keep
modify-dossier flag                     rename to change-register
change-memory flag                      rename to promote-memory, distinct from change-register
professional-position flag              keep
```

The rule is:

```text
Registre != memory.
change-register != promote-memory.
The template's code-capability flag must not disappear silently.
```

This keeps the line between Registre Probatoire work, runtime memory behavior and code-capability behavior visible.

## Proposed schema intent, non-executable

The eventual passport schema should express the common envelope:

```text
Task Contract in
-> capability run outside Pantheon
-> Result Candidate + Evidence Pack Candidate out
-> policy decision as data
-> User Decision Gate when required
```

The eventual policy decision should return only a decision object such as allow, allow_with_gate, block, needs_revision, needs_evidence, needs_approval or not_applicable. The decision object must not run the capability, route providers, transmit externally, promote a register entry or validate truth by itself.

The eventual answer status should carry:

```text
verification_level  V0–V4
consequence_level   K0–K4
evidence_refs
register_refs
status
```

`register_candidate.schema.yaml` is specified by #87; apply both together.

## Read-only validator proposal

A later validator may check examples and candidates against the schemas and boundaries. It remains read-only.

Checks proposed:

```text
schema_valid
axes_consistent
passport_wellformed
operation_guarded
decision_is_data
evidence_linked
no_bypass
no_forbidden_tool
```

The validator validates. It does not run a capability, route a provider, schedule, transmit, approve or promote.

## Harness compatibility, apply-time mandatory

The existing schema tests impose constraints on every registered schema. Any future implementation PR must satisfy them:

```text
x-boundary present
runtime_execution: false present
governance_refs.default present and resolving
one validating example per schema
schemas/README.md boundary markers preserved
no forbidden canonical-agent spelling regression
```

These are not new policy. They are existing harness constraints inherited by any future protected-path change.

## Files to add only after approval

```text
schemas/shared_axes.schema.yaml
schemas/capability_passport.schema.yaml
schemas/policy_decision.schema.yaml
schemas/answer_status.schema.yaml
schemas/register_candidate.schema.yaml
schemas/examples/*.example.yaml
tests/test_governance_schemas.py
docs/governance/STATUS.md
schemas/README.md
```

## Approval checklist

```text
[ ] confirm shared E/V/K/C axes
[ ] confirm K0–K4 consequence vs C0–C5 approval
[ ] confirm read-only validator scope
[ ] confirm passport operation field set against the template
[ ] keep promote-memory distinct from change-register
[ ] keep the template's code-capability flag, or explicitly map it
[ ] require x-boundary, runtime_execution false and governance_refs.default in every new schema
[ ] authorize protected-path edits under schemas/ and tests/
[ ] apply with E6/#87 so register_candidate lands in the same set
[ ] add CHANGELOG and ai_log after applying
[ ] run schema tests after applying
```

## Current repo state

Documented non-implemented. No protected path changed. Apply is blocked until explicit approval of this proposal, correction of the passport operation guardrail, and #87 alignment.
