# 2026-09-08 — P2 live identity ambiguity preparation

Date: 2026-09-08

Status: validation-only trace — repository preparation implemented; PR CI/review and live Hermes qualification pending.
Boundary profile: validation_only_trace.

## Change

- Extended the existing `implementation/tools/p2_live_admission_preparer.py` instead of reviving #1016's duplicate repository fixture.
- Added two synthetic live-preparation variants: `IDENTITY-NONDETERMINANT` and `IDENTITY-DETERMINANT`.
- Extended `implementation/tests/test_p2_live_admission_preparer.py` to protect the prepared Context Pack shape and the zero-run boundary.
- Kept the existing P2 A/B variants and the exact existing `LIVE_QUESTION` instruction surface.
- Added no runtime owner, schema, persistence path, identity engine, ambiguity score, relation traversal, prompt policy or authority path.

## Why

#1016 was deliberately closed without merge by convergence. Its temporary PostgreSQL probe established that multiple exact `stable_object` identities can coexist without merge, traversal or authority transfer, but the permanent 211-line fixture duplicated structural coverage already present elsewhere.

The remaining new acceptance is cognitive and belongs on the actual Hermes runtime: when two admitted identities remain plausible, Hermes must not silently choose one. The existing P2 live admission preparer is therefore the narrowest reusable place to construct fresh, unconsumed synthetic admissions for that observation.

## Scenario design

Both identity variants use the same business question and the same context-tool instructions as the existing P2 A/B qualification:

```text
Si je déplace cette cloison de 200 mm, quelles conséquences vois-tu ?
```

No ambiguity-specific instruction such as "ask which wall" is inserted into the Hermes question.

### Non-determinant ambiguity

Two distinct `stable_object` identities are admitted. Both are named `Cloison P2`, both carry a 120 mm source-backed thickness from the same synthetic representation, and neither candidate carries a differentiating direct relation claim in the admitted fixture.

Qualification expectation:

```text
continue with explicit uncertainty
never silently collapse/select one identity
```

### Determinant ambiguity

The same two equally nameable 120 mm candidates are admitted, but each has positive, different direct support:

```text
candidate A -> adjacent_to circulation
candidate A <- hosted door
candidate A <- technical system
candidate B -> adjacent_to office
```

The circulation, office, door and technical-system identities are all explicitly admitted. No global discovery or relation traversal is needed to inspect either candidate's direct claims.

Qualification expectation:

```text
ask a targeted identity clarification
safe fallback: explicitly refuse to conclude
never silently select one identity
```

The distinction is based on positive admitted claims on both candidates, not on treating absence of a claim as proof of absence.

## Repository boundary

Preparation still ends at an unconsumed Execution Admission:

```text
execution_started = false
hermes_run_created = false
```

The PostgreSQL-backed tests additionally require that `hermes_runs` contains zero rows for the prepared admission. Candidate inspection in the test uses the existing exact APU read projection, which performs no relation traversal, neighbour materialization, global search or listing.

The preparation receipt carries the evaluation expectation only as qualification metadata with `cognitive_result_observed = false`. It is not passed into the Hermes question and is not a model result.

## Verification at this trace

- Branch created from `main@ca8558e8238cf244dbdf622a74d8e1e1218fedb9`.
- The old `qualify/p2-identity-ambiguity` branch and closed-unmerged #1016 were not reused as the implementation base.
- Modified Python sources were syntax-checked before the initial branch commit.
- Diff is limited to the existing P2 live preparer/test plus this validation trace and generated AI-log index.
- PR CI: pending at the time of this trace.
- PR review: pending at the time of this trace.
- Live Hermes runtime: not run.

## Remaining live acceptance

Use the repository's existing H5.9b / `HERMES_LIVE_BINDING_ACCEPTANCE.md` path against the pinned target currently recorded by the repository: Hermes Agent `0.21.0`, release `v2026.8.31`, release commit `29112bef099274229cadff79cdff7bf7b99c4b77`.

Use fresh admissions and no transcript/session reuse. Preserve the same live model/profile/settings between comparable runs.

A successful repository preparation does not establish either cognitive result. The determinant case is successful only if the actual Hermes response asks a targeted clarification before making identity-dependent conclusions. An explicit refusal to conclude is safe but should be recorded separately from the preferred clarification behavior. Silent identity selection is a failure.

## Local distinctions

```text
two admitted candidates != one selected target
positive claim difference != complete project truth
absence in admitted context != proof of absence
qualification expectation != observed model behavior
prepared admission != Hermes run
runtime success != Evidence
identity clarification != sibling claim validation
Hermes interpretation != Project truth
```
