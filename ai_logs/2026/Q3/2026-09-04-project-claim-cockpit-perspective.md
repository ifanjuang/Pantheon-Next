# 2026-09-04 — ProjectClaim Cockpit perspective convergence

## Objective

Complete the bounded P5 ProjectClaim projection slice by exposing the temporal,
structured-provenance and conflict semantics that already exist in their canonical
owners without creating a new Claim, timeline, provenance or conflict backend.

## Repository state checked

Work started from current `Pantheon-Next/main`:

```text
0cc934071052d73b2a023a72e2536eb6a77c3b11
```

Open PRs/issues and current code were checked for parallel temporal/provenance/
conflict Cockpit work. No overlapping P5 implementation was found. The open Hermes
Desktop and Google Drive qualification PRs are unrelated to this slice.

## Existing owners reused

The audit found that P5 is presentation/composition work, not a new semantic owner:

- `agency_claims.project_claims_known_as_of()` owns knowledge-time reconstruction;
- `agency_claims.applicable_project_claims_as_of()` owns explicit business-time
  reconstruction, optionally bounded by knowledge time;
- ProjectClaim `provenance.basis_refs` owns structured support lineage;
- `project_claim_conflicts.detect_project_claim_conflicts()` owns current bounded
  conflict-candidate detection;
- `agency_claims.project_claim_projection()` owns the current Project-facing
  `claim_values` / `claim_refs` projection;
- `cockpit/project_claim_view_adapter.js` already owns the existing Project-card
  presentation seam for ProjectClaims.

No new persistence owner is required.

## Changes

### Current Claim read

`GET /agency/projects/{project_id}/claims` keeps its existing history and current
projection fields and now also exposes:

```text
projected_claims
perspective.mode = current
temporal_axes
conflict_candidates
conflict_projection
```

Conflict candidates are computed from the existing P3 detector. Detector refusal is
fail-soft for the base Claim read: Claims and their current projection remain
readable while `conflict_projection.status = unavailable` records that absence of
conflicts must not be inferred.

### Temporal read

A read-only endpoint is added:

```text
GET /agency/projects/{project_id}/claims/as-of
```

Supported perspectives:

```text
knowledge_time only
  -> project_claims_known_as_of

business_time only
  -> applicable_project_claims_as_of under current knowledge

business_time + knowledge_time
  -> applicable_project_claims_as_of under the bounded knowledge view
```

At least one cutoff is required.

P3 conflict candidates are deliberately not fabricated for these temporal views.
The current P3 contract is explicitly bounded to
`active_unsuperseded_scalar_claims`. Temporal responses therefore expose:

```text
conflict_candidates = []
conflict_projection.status = not_evaluated
absence_of_candidates_inferred = false
```

This avoids presenting a current-only detector as a historical contradiction engine.

### Cockpit projection

The existing ProjectClaim adapter now requests the enriched current Claim read and
projects, on the Project card back:

- current Claim value;
- observation time;
- explicit business-effective start, or an explicit note that business effectivity
  is undeclared;
- status/certainty/source provenance;
- structured `basis_refs`, collapsible for drill-down;
- current bounded conflict-candidate indicators by `claim_type`.

The existing `claim_values` / `claim_refs` stored Project cache remains a fallback if
the enriched read is unavailable. This avoids making the optional richer projection
a prerequisite for the basic Project card.

The UI creates no Claim card family and exposes no conflict-resolution action.

## Authority boundaries

```text
observed_at != effective_at
business time != knowledge time
as-of read != historical truth
basis_ref != Evidence
provenance != verification
conflict candidate != contradiction resolved
conflict detector unavailable != no conflict
Cockpit projection != persistence
current value displayed != authorization
```

The slice does not:

- mutate ProjectClaims;
- persist new conflict candidates;
- resolve or retire Claims;
- create Decisions;
- admit Evidence;
- promote memory;
- add a timeline store;
- create a new provenance engine;
- create a new visible Claim card family;
- add a temporal conflict detector beyond the existing P3 contract.

## Files

```text
implementation/mvp_vertical/agency_claims_api.py
implementation/mvp_vertical/cockpit/project_claim_view_adapter.js
implementation/tests/test_agency_claim_p5_read_api.py
implementation/tests/test_cockpit_back_interaction_and_claim_provenance.py
ai_logs/2026/Q3/2026-09-04-project-claim-cockpit-perspective.md
```

## Done criteria

- current ProjectClaim read keeps prior fields and gains bounded conflict metadata;
- detector refusal cannot hide the base current Claim projection;
- P1 temporal reconstruction is exposed through a read-only API;
- structured P2 basis provenance is visible from the Project card;
- P3 current conflict candidates are visible but never resolved by the projection;
- no migration or new authority owner is introduced;
- full repository CI is green before merge.

## Remaining limitation

Temporal conflict reconstruction is intentionally not implemented. If a real user
journey later requires conflict review "as known on K at business time B", that
requires a separately governed detector contract whose scan scope and candidate
identity include those temporal cutoffs. The current P3 candidate contract must not
be silently repurposed.

## Status

Implementation candidate prepared on `feat/cockpit-claim-perspective`. Full repository
CI and current-main reconciliation remain the merge gate.
