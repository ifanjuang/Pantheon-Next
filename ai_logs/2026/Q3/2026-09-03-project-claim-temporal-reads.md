# ProjectClaim temporal reads — knowledge time and business time stay distinct

Date: 2026-09-03

Status: implemented on candidate branch — CI/review pending.
Boundary profile: bounded_implementation_change.

## Objective

Add the smallest executable temporal slice to the existing ProjectClaim owner so
Pantheon can reconstruct historical claim state without introducing a temporal
engine, universal Fact table, mutable validity columns or a second Claim owner.

## Base

```text
main = de46bdfcdb738440b73f005ce85849f7abd6cc97
```

This base already contains:

- merged #943 direct-human policy-gate convergence;
- merged #945 authority topology revision 4;
- merged #946 Architecture Audit repin to the accepted topology.

No open parallel PR was found for ProjectClaim temporal semantics before this
slice.

## Observed existing model

ProjectClaim already had the necessary temporal ingredients:

```text
observed_at
  semantic observation time

effective_at
  optional business-effective time

created_at
  PostgreSQL recording/system time

supersedes
  append-only lineage
```

`agency_project_claims` is already protected by PostgreSQL triggers that reject
UPDATE and DELETE. A later Claim supersedes a prior Claim by inserting a new row;
the predecessor is never rewritten.

Therefore a stored `valid_until` would be the wrong first move: closing the old
row would either violate append-only history or require a second mutable temporal
store.

## Change

### Existing owner extended

Temporal reads are implemented in `agency_claims.py`; no new module or authority
was created.

Added:

```text
project_claims_known_as_of(project_id, knowledge_time)
applicable_project_claims_as_of(project_id, business_time, knowledge_time=None)
```

### Knowledge/system-time read

`project_claims_known_as_of` uses PostgreSQL `created_at` as the system recording
axis and reconstructs supersession only from rows recorded by the requested
knowledge cutoff.

A later correction cannot rewrite what Pantheon could have known earlier.

### Business/world-time read

`applicable_project_claims_as_of` uses only explicit `effective_at` values.

```text
effective_at = null
!= observed_at
!= created_at
```

A Claim with no explicit business-effective time remains available to normal
Claim/current-state reads, but it is not silently inserted into a business-time
view.

When `knowledge_time` is supplied, the business-time view is constrained to what
was already recorded at that system time. When omitted, the function gives the
current retrospective view of that business time.

### Supersession

Supersession is evaluated after both temporal cutoffs.

A superseding Claim displaces its predecessor only if that superseding Claim is
itself:

- already recorded by the requested knowledge time, when a knowledge cutoff is
  supplied; and
- explicitly effective by the requested business time, for a business-time view.

No predecessor row is mutated and no `valid_until` is persisted.

## Canonical schema clarification

`schemas/project_claim.schema.yaml` keeps the same shape. Only descriptions were
strengthened:

- observation time is distinct from recording time and applicability;
- null `effective_at` establishes no business applicability start;
- readers must not substitute observation/recording time;
- `supersedes` is append-only lineage, not an in-place validity mutation.

The implementation `created_at` field intentionally remains outside the semantic
ProjectClaim payload, so persistence metadata does not become a new Claim field by
accident.

## Proof case

The PostgreSQL test creates:

```text
Claim A
  value = 350000
  effective = 2026-01-01
  recorded first

knowledge cutoff K

Claim B
  value = 375000
  effective = 2026-02-01
  recorded after K
  supersedes A
```

Expected reconstruction:

```text
known at K
  -> A

applicable on 2026-03-01 using knowledge at K
  -> A

what we know now about 2026-03-01
  -> B

what we know now about 2026-01-15
  -> A
```

A second test records a Claim with `observed_at` but no `effective_at` and proves
that it is present in the knowledge-time view while absent from the business-time
view.

## Deliberately absent

- no SQL migration;
- no stored `valid_until`;
- no mutable temporal closure;
- no global temporal engine;
- no generic Fact table;
- no automatic conflict resolution;
- no change to Evidence, approval or identity authority;
- no new Cockpit/API temporal endpoint yet.

## Boundaries

```text
observed_at != effective_at
observed_at != recorded/system time
recorded != true
applicable != verified
superseded != deleted
retrospective knowledge != historical knowledge
projection != persistence
```

## Next

After this slice is accepted, P2 remains structured derivation provenance for
ProjectClaim. That work should reuse existing candidate/result/basis identities and
APU derivation patterns rather than invent a second provenance owner.
