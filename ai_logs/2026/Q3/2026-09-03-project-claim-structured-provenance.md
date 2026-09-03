# 2026-09-03 — ProjectClaim structured provenance

## Objective

Close one observed provenance loss in the existing human-governed transition from a reviewed `ProjectClaimCandidate` to a separate append-only `ProjectClaim`.

The candidate already carries structured `basis_refs`, but the accepted Claim retained only the exact candidate/review identity plus an optional selected `backing_ref`. The complete reviewed basis array was therefore lost after Claim creation.

This slice preserves that array without creating a universal derivation object, provenance engine, Evidence admission path, conflict authority or identity resolver.

## Repository state checked

Initial P2 base after merged P1.5:

```text
61715aa1cea4171f0faede88daffda059d45299f
```

During implementation `main` advanced through #951 to:

```text
d3f0fab72f64714010e30abc3e03c001b441eb1b
```

That change concerns free episodic/runtime memory and is independent of ProjectClaim persistence. It was integrated before P2 review.

Relevant existing owners reviewed:

- `schemas/project_claim_candidate.schema.yaml`;
- `schemas/project_claim.schema.yaml`;
- `implementation/mvp_vertical/project_claim_candidates.py`;
- `implementation/mvp_vertical/agency_claims.py`;
- `implementation/mvp_vertical/sql/019_project_claim_candidates.sql`;
- Agency Data and composed Cockpit migration ordering;
- ProjectClaim projection and candidate SQL authority tests;
- APU `derivation` remains a distinct Project Anatomy concept and was not reused as a universal ProjectClaim provenance owner.

## Observed gap

Before this slice:

```text
ProjectClaimCandidate
  basis_refs = [A, B, ...]
       |
       | human accepted_for_claim
       v
ProjectClaim
  candidate_ref = exact candidate + review
  backing_ref   = optional one selected basis
  basis_refs    = lost
```

`backing_ref` and `basis_refs` have different semantics:

```text
backing_ref
= one selected governed semantic support used by Claim status qualification

basis_refs
= complete structured basis carried by the reviewed candidate
```

Keeping only `backing_ref` is therefore not equivalent provenance.

## Convergence decision

Extend the existing `ProjectClaim.provenance` owner.

Do not create:

```text
Universal Derivation
Provenance Authority
Lineage Engine
Conflict Engine
Identity Resolver
```

The P1.5 placement grammar applies directly:

```text
new provenance information
!= new governed Object

existing ProjectClaim provenance can carry it
-> extend existing owner
```

## Implementation

### Schema

`ProjectClaim.provenance` gains optional structured `basis_refs` using the same bounded entity-reference shape already present on `ProjectClaimCandidate`.

Compatibility rule:

- historical execution-backed Claims may expose `basis_refs: []` because the old creation path did not persist the array;
- in this slice, non-empty `basis_refs` are admitted only for `source_kind = execution_result`;
- other source kinds remain `[]` until a dedicated provenance path is demonstrated.

This avoids silently letting direct human or unrelated source paths invent structured basis lineage.

### Persistence

New additive migration:

```text
036_project_claim_provenance_basis.sql
```

It:

1. adds `agency_project_claims.basis_refs JSONB NOT NULL DEFAULT []`;
2. validates that the stored value is an array;
3. prevents non-execution source kinds from carrying non-empty structured bases in this slice;
4. adds one narrow trigger that compares a newly inserted execution-backed Claim's `basis_refs` with the exact candidate payload;
5. refreshes the existing Project Claim projection so `agency_projects.claim_refs` exposes the same provenance;
6. rebuilds stale existing projection caches with `basis_refs` present.

`019_project_claim_candidates.sql` is not modified. Its historical migration remains intact and continues to own candidate identity, reviewed disposition, value, unit, time and selected-backing checks.

The new trigger deliberately does not reimplement those checks.

### Python owner

`agency_claims.record_claim()` now normalizes and persists `basis_refs` and emits them in the governed Claim payload.

New execution-backed Claims require a non-empty structured basis at the Python owner boundary. Candidate creation passes the exact `payload["basis_refs"]` already reviewed.

The JSON Schema plus SQL constraint prevents non-execution paths from using non-empty basis provenance.

### Composition

Both persistence compositions execute the additive migration explicitly:

```text
Agency Data standalone:
002 -> 019 -> 036 -> 020

Composed Cockpit after execution owner exists:
... -> 010 -> 020 -> 019 -> 036 -> cross-family links
```

The second sequence is important because `019` may be replayed after Execution Result tables exist to install provenance foreign keys. `036` then restores the latest Claim projection definition with structured basis provenance.

## Tests added or strengthened

The slice now checks:

- composed migration order and packaging of `036`;
- migration idempotency and validation of the new constraints;
- exact `basis_refs` preserved from reviewed candidate to Claim;
- idempotent Claim replay preserves the same basis;
- Project cached `claim_refs` exposes the same basis;
- direct SQL cannot substitute the candidate basis array;
- selected `backing_ref` remains independently constrained to a candidate basis;
- non-execution Claim payloads cannot carry non-empty structured bases;
- historical execution-backed Claim payloads with an empty basis remain schema-valid.

Repository CI remains the final proof gate.

## Preserved distinctions

```text
basis_refs != Evidence
basis_refs != backing_ref
provenance != verification
candidate accepted != project truth
ProjectClaim != ProjectClaimCandidate
ProjectClaim != APU attribute_claim
ProjectClaim provenance != APU Derivation Record
runtime result != governed Claim
projection != persistence
```

## Scope deliberately excluded

- no generic derivation object;
- no machine derivation method/version carrier yet;
- no conflict detection;
- no entity resolution;
- no Evidence admission change;
- no authority-registry change;
- no PDP/PEP change;
- no ProjectClaim temporal change;
- no APU schema or runtime change.

## Relationship to next slices

This is the minimum structured-provenance foundation needed before P3 conflict detection.

A later provenance slice may add structured derivation lineage only when concrete ProjectClaim producers demonstrate information beyond `basis_refs` that cannot be represented without duplication. It must not collapse APU derivation and ProjectClaim semantics by default.

## Status

Implementation prepared on `feat/project-claim-structured-provenance`.

CI and PR review remain the merge gate.
