# An architecture assessment, measured rather than impressionistic

Date: 2026-09-06

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added: `docs/audits/2026-09-06-enforcement-and-exercised-authority.md` — a
  non-normative repository-truth assessment answering one question: is the
  governance architecture working, and if not, what is the smallest true
  statement of why.
- Regenerated: `ai_logs/INDEX.md` via `.github/scripts/generate_ai_logs_index.py`,
  the documented post-step for adding a log.
- Removed: nothing. No doctrine, schema, test, binding or status changed.

## Why here

`docs/audits/` already owns dated, non-normative repository assessments — ten of
them, most recently 2026-08-16 — so no new owner was created. `STATUS.md`,
`ARCHITECTURE.md`, `WHAT_RUNS.md` and `WATCHLIST.md` were checked first: each
states current posture and none of them is a place to record a critique of that
posture. `CLAUDE.md`'s rule against new governance documents applies to
`docs/governance/`, and an audit is precisely the artifact class it exempts.

An `ai_logs/` entry was considered and rejected as the primary home. The
assessment has an audience and a shelf life; a trace has neither.

## What the audit found

Three findings, in the order that matters:

```text
1  rules outpace the checks that make them true   6 instances in one session
2  declared authority is almost entirely unexercised   46% candidate, 0 connected
3  the blocker is a doctrine question, not engineering  K3 vs human-originated writes
```

Finding 1 is not six defects but one property: a rule is written, an owner is
named, and nothing is built that can fail when the rule is broken. Every case was
green; every one was invisible until read by hand.

Finding 3 is the one that decides the others. Five of six wired chokepoints are
refused by the real PDP because `K3` demands `task_contract_ref` and
`evidence_pack_candidate_ref` while the paths guard human-originated writes. So
the governance core cannot be connected, and therefore cannot be falsified, until
someone decides whether a Task Contract governs work a human does directly.

The audit names that question and deliberately does not answer it. Answering it
would be an assistant resolving doctrine, which is the reverse authority transfer
the repository forbids.

## The index step, and why it is in this entry

`ai_logs/INDEX.md` states it is generated and instructs running
`generate_ai_logs_index.py` after adding a log. Nothing enforces this:
`check_index_coverage.py` reads as though it would, and explicitly excludes
`ai_logs/`. 39 of 245 Q3 entries were unindexed, including all five entries this
session produced before this one.

Running the generator here indexes this entry and, by the generator's own design,
the stragglers with it. That closes the symptom, not the cause: nothing still
prevents the next log from being added without it. The cause belongs in a
separate change that puts the generator in CI, and this entry is not that change.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: none. The audit is non-normative, ratifies no candidate,
promotes nothing and resolves no open question.
Schema/test/CI impact: none. `ai_logs/INDEX.md` is regenerated output, not an
edited rule.
External action: none.
Memory behavior: none.

## Verification

```text
check_status_headers.py                   OK
check_internal_links.py                   OK
check_no_truncation.py                    OK
check_obsolete_authority_consistency.py   OK
tests/                                    675 passed
```

Every figure in the audit was measured on `main@2754625d` rather than recalled:
zone sizes, the authority distribution, the chokepoint states read from
`GOVERNANCE_STATUS.md`, and the six enforcement gaps each traced to their PR or
issue.

## Local distinctions

```text
assessment    != decision
audit         != doctrine
naming a gap  != authority to close it
generated     != enforced
```
