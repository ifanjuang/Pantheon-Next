# A body-driven check lived in a workflow that ignored body edits

Date: 2026-09-06

Status: implemented — `governance-ci.yml` now listens to the `edited`
pull-request event, so a check that reads `PR_BODY` can actually be
satisfied by correcting the body.
Boundary profile: validation_only.

## Change

- Updated: `.github/workflows/governance-ci.yml` — `pull_request:` gains
  `types: [opened, synchronize, reopened, edited]`.
- Removed: nothing. No job, step, script or check logic changed.

## Why

`check_roles_rites_spaces_change.py` reads the pull-request body:

```yaml
PR_BODY: ${{ github.event.pull_request.body || '' }}
```

It requires eight declared review-context sections whenever a Role, Rite or
governed-Space owner surface is touched. The correct remedy for its failure is
therefore to edit the PR body — and that remedy could not work:

```text
`pull_request:` with no `types:` filter
-> GitHub's defaults are opened / synchronize / reopened
-> editing a body fires `edited`, which triggered nothing

rerun_failed_jobs replays the ORIGINAL event payload
-> PR_BODY stays frozen at the body as it was when the PR opened
-> the re-run cannot see the correction either
```

Measured on #993, not inferred: the guard failed, the body was corrected, the
job was re-run, and the re-run's log printed the *old* body verbatim and failed
identically. Green was only reached by pushing a further commit to produce a
fresh `synchronize` payload.

So the repository held a check whose only sanctioned fix was structurally
unreachable, and whose workaround — commit something, anything — sits one step
away from the empty-commit-to-kick-CI practice the contribution rules forbid.

## Cost, stated plainly

Every PR title or body edit now re-runs all three jobs in this workflow.
Measured from #993's own runs, they complete in roughly 30s, 30s and 45s, in
parallel — well under two minutes of cheap CI. The alternative was leaving every
contributor who trips this guard to burn a cycle discovering the same thing.

A narrower design is possible (`if: github.event.action != 'edited'` on the two
jobs that do not read the body) and was deliberately not taken: two conditionals
to maintain in exchange for roughly one minute, in a workflow this small, is a
worse trade than the blunt fix.

## Boundary

Boundary profile applies: `validation_only`.

Protected paths touched: `.github/workflows/` — CI configuration only. No check
logic, threshold, allowlist or governance rule changed; only when the existing
checks run.
Runtime impact: none on the product. CI runs on one additional event type.
Authority impact: none. No check was weakened, and none was added.
Schema/test/CI impact: one trigger line; `tests/` 665 passed; the workflow YAML
was parsed to confirm the trigger list and job set are unchanged apart from the
added type.
External action: none.
Memory behavior: none.

## Local distinctions

```text
check implemented   != check satisfiable
re-run              != re-read
sanctioned remedy   != reachable remedy
```
