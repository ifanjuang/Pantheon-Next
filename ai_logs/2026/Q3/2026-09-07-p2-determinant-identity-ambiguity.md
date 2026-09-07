# P2 determinant identity ambiguity qualification

Date: 2026-09-07

Status: validation-only trace — repository qualification candidate.
Boundary profile: validation_only_trace.

## Change

- Added: `implementation/tests/test_p2_identity_ambiguity_context.py`.
- Added: one PostgreSQL-backed P2 case with two equally plausible, explicitly admitted `stable_object` identities for the same existing wall-move question.
- Updated: no runtime, schema, owner, persistence path, prompt policy or identity-resolution behavior.
- Removed: nothing.

## Why

P2 already qualifies a local-context variant A and a composed-context variant B. The next question is whether Pantheon can preserve determinant identity ambiguity instead of silently resolving it before Hermes sees the bounded context.

This repository test exercises only that structural half. Two distinct synthetic partitions have the same display name and the same source-backed thickness. Both are explicitly selected for the same task. The expected repository behavior is to keep both identities distinct and readable, with no implicit scope widening, global search, relation traversal, neighbour materialization or preferred target.

The test does not claim that live Hermes asks the user for clarification. That cognitive behavior remains a live qualification under #986 / H5.9b.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none; test-only qualification.
Authority impact: none; no identity is promoted, merged or selected by this trace.
Schema/test/CI impact: adds one PostgreSQL-backed qualification test; no existing test weakened, skipped or removed.
External action: none.
Memory behavior: none.

## Verification

On PR #1016 head `5cfc9012b9302eb39e670a6237852a58387387f8`, the new ambiguity test passed inside the implementation PostgreSQL suite. The pytest phase reported 900 passed and 4 skipped. Architecture Audit, Governance CI and Obsolete Authority also passed. The overall implementation workflow failed only because this required AI intervention log had not yet been added.

The remaining live acceptance is intentionally separate:

```text
if the ambiguity materially affects the answer
-> Hermes asks which object is intended, or explicitly refuses to conclude
-> Hermes must not silently select one candidate
```

## Local distinctions

```text
candidate match != governed identity
two admitted candidates != one selected target
repository qualification != live cognitive qualification
identity clarification != attribute confirmation
Hermes interpretation != Project truth
```
