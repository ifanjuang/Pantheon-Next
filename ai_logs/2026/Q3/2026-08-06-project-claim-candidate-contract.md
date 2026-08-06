# ProjectClaim candidate contract

Date: 2026-08-06
Status: contract change proposed for tranche F

## Decision

Tranche F reuses the existing Execution Result and ProjectClaim authorities.
It adds one typed `project_claim_candidate` payload; it does not add a generic
Derivation, Consequence or runtime-specific Claim model.

```text
Execution Result item
→ human review
→ separate append-only ProjectClaim creation
```

The candidate carries project scope, proposed value, basis references, certainty,
rationale and limitations. Every authority flag remains false.

A Claim created from that candidate retains the exact execution/result identity,
its own certainty and optional business-effective date. The source result is not
promoted or mutated.

```text
candidate stored != Claim created
Claim created != Evidence admitted
certainty != status
observed_at != effective_at
```

## Accepted boundary

```text
ProjectClaim as governed knowledge unit       yes
ProjectClaim as universal reasoning unit      no
Derivation as a new generic object            no
Consequence as a generic attribute            no
Explicit transition from ResultCandidate      yes
Reuse DecisionRequest and WorkIssue            yes
```

A factual implication may become another governed ProjectClaim. Work to perform
remains a WorkIssue. A consequential choice remains a DecisionRequest followed by
a separate Decision where applicable. The candidate transition does not create
any of them automatically.

## Repository effect

- added `schemas/project_claim_candidate.schema.yaml` and example;
- admitted `project_claim_candidate` in the existing Execution Result envelope;
- extended `project_claim.schema.yaml` with certainty, effective date and exact
  candidate provenance;
- added contract tests;
- kept the general Project card composition doctrine unchanged after review;
  the transition is owned by the schemas and this decision record.

## Final review

The final diff contains only the candidate contract, the qualified Claim contract,
examples, tests and this journal. No general Cockpit or card-composition doctrine is
replaced or truncated.

No runtime, persistence, Project mutation, Evidence admission, Decision, WorkIssue
or external effect is implemented by this contract change.

## Validation continuation

On 2026-08-07, a journal-only commit retriggered the required repository checks
after the reviewed head had no materialized check runs. This entry changes no
contract, schema, authority or implementation boundary. Fusion remains conditional
on the four protected checks succeeding.
