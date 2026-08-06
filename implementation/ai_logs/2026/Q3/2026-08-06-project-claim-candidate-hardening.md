# ProjectClaim candidate transition hardening

Date: 2026-08-06
Status: implementation candidate validated on its final reviewed head
Scope: pantheon-mvp tranche F only

## Objective

Harden the existing transition without adding another authority:

```text
Execution Result project_claim_candidate
→ human accepted_for_claim disposition
→ separate append-only ProjectClaim
```

The Execution Result remains immutable and non-authoritative. The Claim remains a
separate Agency Data record. No Evidence, Decision, WorkIssue, Project mutation,
memory promotion or external effect is inferred.

## Upstream authority

The canonical contract was merged in Pantheon-Next through PR #565 at merge
commit:

```text
869afb153963d209d91f6c51d6e12b041ee633be
```

PR #559 was closed without fusion. The two vendored sidecars and their exact schema
blobs are pinned to the #565 merge commit.

## Observed defects

Review found concrete gaps in the first implementation candidate:

1. the disposition route used the read key although recording a review is a
   consequential write;
2. `accepted_for_claim` could be recorded for a non-Claim result or by a system
   reviewer at the persistence owner;
3. two concurrent Claim creations could both pass the replay lookup before the
   unique index arbitrated them;
4. a later review could race Claim creation without a single order between the
   two append-only events;
5. expanded CHECK constraints and provenance foreign keys could remain
   `NOT VALID`, and one migration guard identified a constraint by broad text
   rather than by its owner name;
6. a direct SQL insert could cite the accepted candidate while changing the
   Project, claim type, value, unit, dates or supporting basis;
7. normal Execution Result storage and review paths reloaded their response after
   their owned transaction ended, opening a new implicit transaction and allowing
   a following review to remain nested, uncommitted and row-locking;
8. legacy contract tests did not yet include `project_claim_candidate`,
   `accepted_for_claim` or the required Claim certainty.

These were implementation defects, not reasons to introduce a Derivation,
Consequence or parallel Claim model.

## Corrections

- review disposition writes require the editor key and an explicit human actor;
- the Execution Result owner admits `accepted_for_claim` only for a
  `project_claim_candidate` reviewed by a human;
- Python and SQL share the immutable result-row lock, establishing one order
  between review and Claim creation;
- Claim replay is checked after the lock with a fresh READ COMMITTED statement;
- migration constraints are found by exact owner name and validated when their
  catalog state is not validated;
- the SQL Claim trigger verifies the exact execution/result/review identity,
  Project scope, candidate kind, claim type, value, unit, observation/effective
  dates and selected basis reference;
- the first implementation remains bounded to Project and Information backing
  resolution while the upstream semantic schema stays open;
- response reloads now occur inside the transaction owned by storage and review,
  so the connection returns without an unintended implicit transaction snapshot;
- contract expectations include the new result kind, disposition and `E0`
  certainty for pre-existing asserted Claim fixtures.

The transaction correction changes no business authority and adds no commit beyond
the operation's existing transaction boundary.

## Validation added

The branch covers:

- read key refusal on the review route;
- system and wrong-kind `accepted_for_claim` refusal;
- absence of Claim creation without the latest human acceptance;
- deterministic replay under concurrent Claim creation;
- serialization of a later review against in-flight Claim creation;
- the inverse order where a rejection takes the lock first and the later Claim
  creation waits, observes the rejection and refuses;
- exact migration constraint presence, validation and replay;
- direct SQL refusal for false acceptance, changed candidate value and backing
  outside the candidate basis;
- acceptance of one exact, fully matching reviewed candidate identity;
- byte-for-byte vendored schemas and sidecars pinned to the #565 merge commit.

## Boundaries retained

```text
candidate stored != ProjectClaim created
accepted_for_claim != Decision
ProjectClaim created != Evidence admitted
runtime success != professional validation
certainty != status
observed_at != effective_at
read access != review authority
Project cache != Claim authority
```

No generic reasoning graph, scheduler, queue, runtime, automatic approval or
memory path is added.

## Verification status

The implementation and test corrections were validated on head:

```text
8ca0a399d5cd28e69ff0c6fd28a5a708cd6d1393
```

Results:

```text
Pantheon Architecture Audit -> success
Pantheon MVP CI / contract-tests -> success
Pantheon MVP CI / tests -> success
```

The journal amendment creates a later documentation-only head, which must receive
its own required checks before merge. No protection is bypassed and no earlier
check result is reused for a changed SHA.
