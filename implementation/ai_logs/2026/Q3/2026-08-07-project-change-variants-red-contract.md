# Project change variants — executable selection and persistence

Date: 2026-08-07
Status: G1 validation and persistence implemented; runtime production binding remains separate.

## Objective

Implement the pantheon-mvp executable tranche for Project change variants after
the upstream G0 contract was merged through Pantheon-Next #571 at
`8227d1c78ca48e5aea04f825d80ecde159fa5434`.

The exact upstream schema is vendored with commit, blob and SHA-256 provenance.
Vendoring transfers no authority.

## Reused persistence owners

```text
execution_results
-> stores each immutable project_change_variant candidate.

execution_result_review_dispositions
-> stores the human selected_for_change_candidate disposition.

agency_change_candidates
-> remains the only persisted Project proposal and later human
   apply / reject / revision owner.
```

No persistent `VariantRequest`, `InformationBranch`, universal branch graph or
second ChangeCandidate store is introduced.

## Executable transition

```text
Hermes-shaped Execution Result
-> sibling project_change_variant items with one exact request scope
-> exact target Agency schema and mutable-field validation
-> human selected_for_change_candidate disposition
-> existing pending Project ChangeCandidate with exact source provenance
-> later existing human apply / reject / revision request
```

Selection creates no Project mutation, Decision, Evidence, memory promotion or
external effect. The selected candidate remains subject to the existing
ChangeCandidate review and optimistic Project revision gate.

## Deliberately red phase

The first head added only the vendored contract, provenance and behavioral tests.
CI failed exactly on the missing G1 behavior:

```text
6 new tests failed
1,251 existing tests passed
architecture audit passed
```

The failures were the absent result kind, selection disposition and bounded
transition module. This established the expected red contract without disturbing
existing behavior.

## Implementation

The green implementation extends existing owners only:

1. `project_change_variant` is admitted as an immutable Execution Result kind;
2. the vendored payload and canonical schema reference are validated at intake;
3. `selected_for_change_candidate` is human-only and valid only for that kind;
4. one execution lock serializes sibling selection checks;
5. siblings must share Project, base revision, target schema and request scope;
6. proposed fields must be mutable candidate fields in the exact current Agency
   Project schema;
7. ProjectClaim projections, unknown, immutable, system and other non-editable
   fields fail closed;
8. the selected alternative creates the existing pending ChangeCandidate with
   exact execution, result, disposition, request-scope and variant provenance;
9. unique result and request-scope indexes prevent duplicate or competing retained
   selections;
10. stale Project revision refuses selection without Project mutation.

The migration can install optional ChangeCandidate provenance when Agency Data is
present even if the Execution Result surface is mounted later. Foreign keys are
attached only when both existing owners are present.

## Reconciliation during green-up

The first implementation run exposed two compatibility seams rather than a model
defect:

- historical ChangeCandidate tests mounted Agency Data without the Execution Result
  migration, so optional provenance columns were not yet installed;
- one existing vocabulary contract still listed the pre-G result kinds and
  dispositions.

The Agency Data bootstrap now installs the bounded G migration, and the vocabulary
contract is aligned with the merged upstream enum. No historical test behavior was
weakened.

## Verified result

Final head validation completed with:

```text
Pantheon Architecture Audit: success
contract-tests: success
full PostgreSQL suite: success
```

The runtime production binding, selection API surface and Hermes 0.20.0 synthetic
run are deliberately outside this G1 persistence PR.

## Boundaries

```text
vendored contract != authority transfer
variant stored != variant selected
selection disposition != Decision
selection != Project application
ChangeCandidate created != Project mutated
source reference != Evidence
runtime success != retained truth
```

This tranche adds no parallel workflow engine, branch object, scheduler, queue,
provider router, automatic approval or automatic ProjectClaim/Evidence promotion.
