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

## Repository effect

- added `schemas/project_claim_candidate.schema.yaml` and example;
- admitted `project_claim_candidate` in the existing Execution Result envelope;
- extended `project_claim.schema.yaml` with certainty, effective date and exact
  candidate provenance;
- added contract tests;
- kept the general Project card composition doctrine unchanged after review;
  the transition is owned by the schemas and this decision record.

No runtime, persistence, Project mutation, Evidence admission, Decision, WorkIssue
or external effect is implemented by this contract change.
