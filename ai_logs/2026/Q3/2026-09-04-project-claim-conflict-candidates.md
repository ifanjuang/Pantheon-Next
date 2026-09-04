# 2026-09-04 — ProjectClaim conflict candidates

## Objective

Add the first bounded P3 conflict-detection slice on top of temporal ProjectClaim
semantics and structured provenance.

```text
active scalar ProjectClaims
        ↓
deterministic pairwise tension detection
        ↓
ProjectClaimConflictCandidate
```

A conflict candidate is review material only. It does not resolve the conflict,
select a winning Claim, mutate Claim status, admit Evidence, create a Decision,
authorize an effect or merge identity.

## Repository state checked

Initial P3 work started from:

```text
4d5efa6374bd343a26c42caf082ad5242c17e7a1
```

The branch was repeatedly re-audited and rebuilt as `main` advanced. The final
exact baseline used for the current P3 candidate is:

```text
Pantheon-Next/main = 9714280f6dc03767cd24ab7b3d13ab81511291b6
```

Intervening work covers spatial/episodic qualification, qualification pin ordering,
Obsidian Headless qualification, completed MarkdownDB qualification provenance and
NoteMesh structural/scope qualification. None modifies the ProjectClaim/conflict
files owned by this slice.

No parallel open PR or issue was found implementing ProjectClaim conflict semantics
or governed entity resolution.

## Existing carriers reviewed

- `contradictory_review` remains a bounded Rite report tied to execution/review
  context; it is not a durable ProjectClaim conflict owner.
- `entity_relations.contradicts` remains a governed semantic relation with human
  canonization lifecycle; it is not raw detector output.
- `REVIEW_QUEUE.md` remains review guidance/presentation only; P3 does not create a
  universal queue.

## Placement

`ProjectClaimConflictCandidate` is a narrow carrier subordinate to the existing
`project_claim` authority envelope. No new system-ownership registry concept is
introduced.

The candidate has deterministic durable identity because a detected tension may
remain historically reviewable after one of its Claims is later superseded.
Persistence does not make the candidate an authority.

## Detection scope

Detector v1 compares only:

```text
same Project
+ same claim_type
+ active / unsuperseded / non-retired Claims
+ scalar claim field
```

Aggregated fields such as `parcelle` are excluded because multiple active values
are legitimate. Equal values produce no candidate.

## Governed unit decision

The ProjectClaim write owner derives unit from the governed `claim_type`, and
ProjectClaimCandidate admission rejects a proposed unit different from that
registered unit.

Therefore P3 does not define `unit_ambiguity`:

```text
same claim_type + different governed unit
= ProjectClaim integrity violation
!= business conflict candidate
```

Python and SQL fail closed if such a state is encountered.

## Temporal classification

P1 established that `effective_at` is only an explicit business-effective start.
No validity end is inferred.

```text
same explicit effective_at + different value
→ value_conflict_same_effective_start

both effective_at absent + different value
→ value_conflict_undated

different or partially missing effective_at
→ temporal_ambiguity
```

Even the strongest class remains review material, not a truth verdict.

## Provenance

P2 distinctions remain intact:

```text
basis_refs != backing_ref
```

The read projection compares `basis_relation` and `backing_relation` separately.
Neither signal selects a winner.

## Persistence convergence

The first P3 draft persisted both foreign keys to immutable ProjectClaims and a JSON
snapshot duplicating Claim values, certainty, time, backing and provenance.
Repository review rejected that duplication.

ProjectClaims are already append-only and protected from UPDATE/DELETE. P3 now
persists only:

```text
conflict_candidate_id
project_id
claim_type
left_claim_id
right_claim_id
classification
detector_id
detector_version
submitted_by
created_at
```

It does **not** persist:

```text
Claim value copies
Claim certainty copies
Claim time copies
backing_ref copies
basis_refs copies
candidate JSON payload
candidate digest
authority flags
resolution fields
Decision/Evidence links
```

The governed candidate is reconstructed from immutable Claim references when read.

```text
projection != persistence
reference != duplicated truth
```

This also removes the possibility that a direct SQL insert could bind real Claim
IDs while falsifying duplicated Claim content in a second payload.

## Contract

`schemas/project_claim_conflict_candidate.schema.yaml` defines the projected
review candidate. `claim_refs` contain only canonical Claim IDs.

Authority ceiling remains explicit in that contract:

```text
is_evidence           = false
is_decision           = false
resolves_conflict     = false
mutates_project_claim = false
authorizes_effect     = false
merges_identity       = false
```

The SQL table contains no authority-promotion columns.

## Detector and persistence

Implementation:

```text
implementation/mvp_vertical/project_claim_conflicts.py
implementation/mvp_vertical/sql/037_project_claim_conflict_candidates.sql
```

Detector identity:

```text
project_claim_pairwise_conflict / version 1
```

Candidate identity is deterministic from detector version, Project, claim type and
canonically ordered immutable Claim IDs.

Detection is public and read-only. P3 exposes no HTTP route and no public
persistence entry point.

Internal `_persist_candidate` exists only to qualify exact storage semantics. It:

1. validates the projected contract;
2. rebinds the two IDs to currently active immutable Claims;
3. recomputes the exact detector result;
4. refuses payload drift;
5. persists only the minimal detection record;
6. reconstructs the candidate from Claim refs on read.

PostgreSQL independently refuses:

- cross-Project pairs;
- cross-claim-type pairs;
- retired/superseded Claims at admission time;
- equal-value pairs;
- same-type unit-integrity violations;
- temporal classification drift;
- unqualified detector id/version;
- UPDATE/DELETE mutation.

The Claim pair is not UNIQUE because detector version participates in candidate
identity; a future detector can preserve a separate historical result.

## Transaction-test correction

The first CI attempt produced two PostgreSQL failures after expected refusal paths.
The guards themselves fired. Broad `conn.rollback()` calls then rolled back test
setup because psycopg reads had left an outer transaction open.

The corrected tests scope prohibited mutations in nested `with conn.transaction():`
blocks. These use savepoints when needed and roll back only the expected failing
mutation. Production transaction semantics are unchanged.

## Migration composition

```text
Agency Data:
002 → 019 → 036 → 037 → 020

Composed Cockpit:
... → 010 → 020 → 019 → 036 → 037 → cross-family links
```

## Preserved distinctions

```text
conflict detected != conflict resolved
conflict candidate != Decision
conflict candidate != Evidence
candidate persisted != Claim contested
same claim_type != identical professional scope
temporal change != contradiction
provenance difference != truth decision
basis_refs != backing_ref
certainty != authority
ProjectClaimConflictCandidate != contradictory Rite review
ProjectClaimConflictCandidate != canonical entity relation
projection != persistence
execution success != authorization
```

## Out of scope

- no automatic `ProjectClaim.status = contested`;
- no conflict-resolution lifecycle;
- no human resolution event;
- no generic review queue;
- no canonical `contradicts` relation creation;
- no entity resolution/merge;
- no fuzzy/vector/LLM conflict inference;
- no score or automatic winner;
- no API/Cockpit exposure;
- no Evidence/Decision/Register change;
- no authority-registry promotion;
- no P1 temporal redesign;
- no P2 provenance redesign.

## Status

Converged implementation candidate prepared on
`feat/project-claim-conflict-candidates`. Full repository CI on this exact current
baseline remains the merge gate.
