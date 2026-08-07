# Project change variants — deliberately red executable contract

Date: 2026-08-07
Status: deliberately failing tests; implementation intentionally absent.

## Objective

Start the pantheon-mvp executable tranche for Project change variants only after
the upstream G0 contract was merged through Pantheon-Next #571 at
`8227d1c78ca48e5aea04f825d80ecde159fa5434`.

This commit vendors the exact upstream schema and defines the behavior that the
next implementation commits must satisfy. It does not add a migration, API,
selection module, Cockpit projection or runtime binding.

## Reused persistence owners

```text
execution_results
-> stores each immutable project_change_variant candidate.

execution_result_review_dispositions
-> will store the human selection disposition.

agency_change_candidates
-> remains the only persisted Project proposal and human application owner.
```

No persistent `VariantRequest`, `InformationBranch`, universal branch graph or
second ChangeCandidate store is introduced.

## Expected transition

```text
Hermes Execution Result
-> sibling project_change_variant items with one exact request scope
-> human selected_for_change_candidate disposition
-> existing pending Project ChangeCandidate with exact source provenance
-> later existing human apply / reject / revision request
```

Selection creates no Project mutation, Decision, Evidence or external effect.
The selected candidate remains subject to the existing ChangeCandidate review and
optimistic Project revision gate.

## Deliberately red assertions

The tests currently require behavior that main does not yet provide:

1. `project_change_variant` in the executable result-kind vocabulary and SQL check;
2. `selected_for_change_candidate` as a human-only review disposition;
3. persistence of sibling variants before selection;
4. a bounded `project_change_variants` transition module;
5. exact execution/result/disposition and request-scope provenance on the existing
   ChangeCandidate row;
6. at most one selected sibling per request scope;
7. refusal of ProjectClaim, system, immutable and non-editable target fields;
8. stale Project revision refusal without mutation.

The first DB-free vocabulary assertion guarantees the PR is red even when the
PostgreSQL suite is unavailable. PostgreSQL behavior tests then define the
transactional and persistence target.

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

The next commit may extend existing constraints and owners, but must not create a
parallel workflow engine, branch object, scheduler, queue, provider router,
automatic approval or automatic ProjectClaim/Evidence promotion.
