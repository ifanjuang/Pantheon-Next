# 2026-08-31 — former pantheon-mvp retirement audit

Status: retirement/convergence trace; repository archive setting remains an operator action.

## Objective

Determine whether the former `ifanjuang/pantheon-mvp` repository still owns any active implementation responsibility that would block retirement after the history-preserving import into `Pantheon-Next/implementation/`.

## Frozen references

```text
Pantheon-Next/main = 3ffc583ac4232552aca9c34fa1407c11f388a59c
pantheon-mvp/main  = d960862dd0e23b7003a0f3e4ee0ea630ffc12af9
```

The former `main` is still exactly the source cutoff recorded in `implementation/IMPORT_PROVENANCE.md`.

## Branch audit method

The former repository still retains historical branches, several of which are Git-divergent from its final `main`. `ahead_by` was not treated as evidence of missing active work because stacked/rebased changes may have been merged later under different SHAs.

Each material branch family was therefore checked against current monorepo owners and tests.

Observed convergence included:

- Decision Requests: current `decision_requests.py`, APIs, SQL and Cockpit paths;
- Professional Documents: revision owner, source admission, comparison, currentness, inbox, impacts and tests;
- ProjectClaim candidates: current bounded candidate-to-claim owner and tests;
- storage retention: current implementation owner and canonical storage-object contract;
- Project Anatomy: current API/read/Cockpit projection owners and tests;
- APU cross-family: consolidated current owner and tests rather than the historical branch SQL shape;
- Tool Card exact binding: historical decorator intentionally retired; exact binding is projected by the canonical Cockpit projection;
- Cockpit nested collection/create behavior: current live collection adapter owns the converged path;
- EntityRelation migration coverage: current migration tests remain in the monorepo.

Some historical branches have no commits ahead of the former final `main`; others preserve superseded intermediate shapes. The conclusion is semantic convergence, not byte-for-byte equivalence of every historical branch commit.

## Issue reconciliation

The former repository had four open issues at audit start.

- #94 was verified complete in the current generic `child_collection.create_action` Cockpit path and closed completed.
- #165 had a real residual: review decisions remain online-only while request creation is queued. The residual scope was moved to `Pantheon-Next#906`; the former issue was closed duplicate.
- #227 was superseded by current real-environment qualification `Pantheon-Next#644` under `#607`; the former issue was closed duplicate.
- #338 was unrelated solicitation; it was closed and locked as spam.

The former repository had zero open issues after reconciliation.

## Retirement posture

The former repository README was replaced with an explicit historical-only notice. New implementation work there is forbidden and active development points to `Pantheon-Next/implementation/`.

The repository should be archived rather than deleted so original PR/issue URLs, branches and original commit identifiers remain available as provenance.

```text
retirement audit complete != GitHub archive toggle applied
archive != delete
historical provenance != active authority
```

No repository setting mutation was available through the connected GitHub tooling used for this audit, so the GitHub archive toggle remains an operator-side action.
