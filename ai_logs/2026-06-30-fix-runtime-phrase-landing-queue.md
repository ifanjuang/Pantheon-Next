# AI log — unblock CI: reword affirmative "landing queue"

Date: 2026-06-30.

Actor: Claude Code.

## Intent

`main` was red: the `runtime_phrases` governance guard (run both as the standalone
`Read-only governance checks` job and as a blocking check in the mcp-server doctor)
flagged two affirmative uses of the word `queue` in
`docs/governance/REPOSITORY_CONSOLIDATION_LANDING_PLAN.md`:

```text
217: ## Phase 3 — Branch and PR landing queue
540: Do after status spine and branch landing queue.
```

These are a branch/PR landing order, not a Pantheon runtime queue, but the guard
correctly forbids the affirmative runtime-suggesting word. The failure was
pre-existing on `main` and unrelated to PR #248 (authority-index alignment), which
only inherited the red.

## Change

- `docs/governance/REPOSITORY_CONSOLIDATION_LANDING_PLAN.md`: reworded the
  affirmative concept "landing queue" -> "landing sequence" (four occurrences:
  lines 33, 102, 217, 540). The line-14 negation ("does not create … a queue")
  is left intact, since the guard allows runtime terms in an explicit negation.
- `docs/governance/OPEN_BRANCH_LANDING_PLAN.md`: reworded the affirmative heading
  `## Current queue` -> `## Current landing sequence` (line 51). The line-9
  negation ("does not create … a queue") is left intact. This file surfaced after
  rebasing onto a fast-moving `main`; the fix was made comprehensive by running
  the guard's own `check_runtime_phrases` over the whole `docs/governance/` tree
  (result: 0 violations) rather than one file per CI round.

## Why reword rather than relax the guard

The guard does its job: governance files must not suggest Pantheon executes,
schedules, queues, routes providers or promotes memory. Aligning the document
with the guard preserves the boundary; weakening the guard would erode it. The
`ai_logs/2026-06-30-repository-consolidation-landing-plan.md` historical mention
of "landing queue" is left unchanged (ai_logs are a record, and the guard scans
only `docs/governance/`).

## Boundary

Documentation wording only. Semantics preserved; no doctrine authored or altered.
No schema, test, `mcp-server/`, runtime or other protected-path change.
