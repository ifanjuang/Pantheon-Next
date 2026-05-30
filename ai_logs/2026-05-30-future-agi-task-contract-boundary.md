# AI Log — Future AGI Task Contract Boundary Clarification

Date: 2026-05-30

## Scope

Resolved a pre-existing Governance CI false positive in
`docs/governance/reference_reviews/FUTURE_AGI.md` without changing the doctrine's
meaning.

## Problem

The "Governance files do not suggest Pantheon executes" scan flagged the words
`scheduler` and `queue` at `FUTURE_AGI.md:199`:

```text
- MCP, A2A, gateway, scheduler, queue or deployment surfaces.
```

This line is under the `## Task Contract requirement` header and lists surfaces
that, when touched, **require** a Task Contract — a gating constraint, not an
affirmative runtime claim. The scanner's negation detector did not recognize the
section context as exclusionary, so it failed.

This failure exists on `main` itself; every PR inherited it.

## Change made

Updated:

- `docs/governance/reference_reviews/FUTURE_AGI.md`.

Added:

- `ai_logs/2026-05-30-future-agi-task-contract-boundary.md`.

Added one boundary sentence at the top of the section:

```text
These surfaces stay outside Pantheon. Pantheon must never run, schedule, queue
or route them itself; a Task Contract only governs whether an external Future AGI
pass may touch them, under explicit approval.
```

This is a true restatement of existing doctrine (Future AGI is an external
reference; Pantheon does not execute), and it establishes the negation/exclusion
context the scanner expects.

## Verification

The governance scan now passes with **both** scanner versions:

- the widened-regex workflow on this branch;
- the original-regex workflow currently on `main`.

So the fix holds regardless of which workflow CI runs.

## Boundary

No runtime behavior added. No change to FUTURE_AGI evaluation/simulation scope.
The sentence only makes explicit that the listed surfaces stay outside Pantheon
and are governed, never executed, by it.
