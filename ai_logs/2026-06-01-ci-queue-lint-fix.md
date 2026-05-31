# AI Log — CI queue/scheduler lint false-positive fix

Date: 2026-06-01

## Scope

Fixed a false positive in the Governance CI "Governance files do not suggest
Pantheon executes" lint that turned `main` red.

The lint forbade the bare words `queue` and `scheduler` in `docs/governance/**`
outside a negation context. The legitimate governance concept **Review Queue**
(a queue of human decisions, surfaced by #29) uses the word "queue" affirmatively,
producing 19 false-positive failures across:

```text
REVIEW_QUEUE.md, ARCHITECTURE_PROOF_REGISTER.md, URGENT_REVIEW_TRIAGE.md,
ARCHITECTURE_INDEX_EFFECT_MATRIX.md, DATA_PLATFORM_RECONCILIATION.md,
DOCUMENT_INTELLIGENCE.md
```

Because those docs were pushed directly to `main` without a PR, the red CI did not
block them, and every subsequent PR (e.g. #35) inherited the red.

## Files changed

- `.github/workflows/governance-ci.yml` — the `FORBIDDEN` list now targets runtime
  queues/schedulers (`message queue`, `job queue`, `task queue`, `agent queue`,
  `queue runtime`, `queue system`, `internal scheduler`, `hidden scheduler`,
  `job scheduler`, `task scheduler`) instead of the bare words `queue`/`scheduler`.
  A comment documents why the bare words are excluded.
- `CHANGELOG.md` — 0.1.25 entry.
- `ai_logs/2026-06-01-ci-queue-lint-fix.md` — this trace.

## Why

The lint should forbid runtime constructs, not a vocabulary word. The bare-word
rule made Pantheon's own legitimate "Review Queue" concept incompatible with its CI.
Targeting runtime-specific phrases keeps the anti-runtime guard (aligned with
`CLAUDE.md`: internal scheduler, mandatory agent queue, message bus) while allowing
governance concepts such as a review/decision queue.

## Verification

Reproduced the lint locally with the new `FORBIDDEN` list over `docs/governance/**`:
0 failures (was 19). The guard still fires on genuine runtime phrases.

## Boundary

CI configuration only. No runtime, schema, test logic, or governance doctrine
changed. The anti-runtime intent of the check is preserved and made more precise.
