# AI Log — Governance scan: allow governed review/decision queue

Date: 2026-05-31

## Scope

Refined the governance phrase scan so it stops failing on the word "queue" when
it means a governed review/decision queue, while still blocking a runtime
message/task queue.

## Problem

The "Governance files do not suggest Pantheon executes" step lists "queue" as a
forbidden runtime-suggesting phrase. Recently added governance docs use "queue"
in the human-decision sense — a *review queue* / *decision queue* that surfaces
doubtful, conflicting, stale or consequential items to a human:

- `REVIEW_QUEUE.md`, `URGENT_REVIEW_TRIAGE.md`,
- `ARCHITECTURE_PROOF_REGISTER.md`, `ARCHITECTURE_INDEX_EFFECT_MATRIX.md`,
- `DOCUMENT_INTELLIGENCE.md`, `DATA_PLATFORM_RECONCILIATION.md`.

19 occurrences were flagged, turning `main` (and every PR) red. This is the
governed-decision sense, not the forbidden runtime "mandatory agent queue".

## Change made

Updated:

- `.github/workflows/governance-ci.yml`.

Added:

- `ai_logs/2026-05-31-governance-scan-review-queue.md`.

For the "queue" phrase only, an occurrence is now allowed when a governed
review/decision-queue framing is present on the line, in its section context, or
in the document title:

```text
review queue | decision queue | queue of governed decisions |
governed (review|decision) queue
```

Decided by the user: refine the scanner, leave the docs intact.

## Why this is safe

The scanner's intent is preserved. A bare runtime queue with no review/decision
framing still fails — verified with a negative test:

```text
"Pantheon runs a message queue and a task queue." -> still FAIL
```

The allowance is the narrowest that covers the governed sense: it keys on the
explicit "review queue" / "decision queue" / "governed decisions" wording, not
on a blanket exemption of the word "queue" or of specific files.

## Verification

- full `docs/governance/` tree: PASS (0 occurrences);
- negative test (runtime queue): FAIL as expected;
- `CLAUDE.md` boundary unchanged: the forbidden "mandatory agent queue" remains
  forbidden; only the human review/decision queue sense is recognized.

## Explicit non-implementation

CI doctrine guard only. No runtime, no governance doctrine edited, no files
touched under `schemas/`, `tests/`, `hermes/`, `operations/`, `pyproject.toml`,
or `CLAUDE.md`.
