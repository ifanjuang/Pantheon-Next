# AI log — MVP vocabulary and invariants tightening

Date: 2026-07-08

Branch: `mvp-vocabulary-invariants-308`

Status: documentation-only vocabulary and invariant tightening.

## Purpose

Review the MVP vertical sequence and reduce ambiguous wording before any validator or CI work.

## Changes

```text
approve -> approve_for_internal_draft
ready_for_execution -> ready_for_governed_processing
memory_authorization: grant_register_candidate_only -> register_candidate_creation + memory_admission
```

Added:

```text
docs/governance/examples/mvp_vertical_fixture/GOVERNANCE_INVARIANTS.md
docs/governance/examples/mvp_vertical_fixture/VOCABULARY_TIGHTENING.md
```

## Boundary

No validator was added.
No command was added.
No CI was changed.
No runtime was added.
No database mapping was added.
No OpenWebUI feature was added.
No Hermes contract was added.
No approval engine or memory promotion was added.

## Preserved distinctions

```text
schema_valid != approved
schema_valid != evidence
reference_valid != truth
governance_invariant_pass != external_action_authorization
fixture_pass != runtime_success
register_candidate_creation != memory_admission
```
