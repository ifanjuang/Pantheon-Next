# AI Log — Request Lifecycle (MÈTIS, cap, memory gates)

Date: 2026-06-01

## Scope

Added `docs/governance/REQUEST_LIFECYCLE.md`: the governed lifecycle of a request, from
situated comprehension to human engagement. It connects the Governance College, the
Task Contract, the rites and the autonomy doctrine into one lifecycle.

This formalizes a model developed with the user across several exchanges, answering:
understand the real demand, hold the goal (the cap), re-evaluate it as answers arrive,
arbitrate, execute outside, let the human engage.

## The model

- **MÈTIS** — a role of situated, adaptive comprehension, activated conditionally (only
  on fuzzy / indirect / implicit / contradictory / vague-but-consequential demands; a
  light triage decides, and MÈTIS may be convened mid-course). She establishes the four
  métier things (real demand, goal/cap, watch-points, responsibility limit) and holds
  and re-reads the cap. She proposes; she does not arbitrate or engage.
- **The cap** lives in the Task Contract; re-evaluation is a governed revision
  (`TASK_CONTRACT_REVISIONS.md`). Minor within-scope adjustments are autonomous; a
  material change of destination requires a revision.
- **ZEUS** arbitrates the cap: validated / insufficient -> back to MÈTIS to deepen /
  touches engagement -> human. The loop is bounded; ZEUS validates framing quality, not
  engagement; ZEUS arbitrates, he does not re-comprehend.
- **CERBÈRE / CHARON** — memory-threshold gates (not judges): Cerbère filters what
  returns from the past, Charon ferries what must stop acting into the archive.
- **Distinct natures**: roles (MÈTIS, ZEUS, College) vs gates (Cerbère, Charon) vs
  runtime (external execution) vs human.

## Why

The user emphasized that the real value is understanding, per the métier, the real
demand, the goal, the watch-points and the responsibility limit — and that the goal may
be re-evaluated as answers come in. This lifecycle makes that the front of every request
without adding ceremony to direct requests (conditional MÈTIS) and without drift
(governed cap revision).

## Boundary

Documentation only. These are governance moments, not an execution pipeline. No runtime,
scheduler, message bus, workflow engine, orchestration loop, automatic approval or
automatic memory promotion. Execution stays external.

Promoting MÈTIS into the canonical role registry (`AGENTS.md`, `GOVERNANCE_COLLEGE.md`)
and the gates into `MEMORY.md` / `CORE_RECORDS_MODEL.md` is a separate governed step;
this document is active support doctrine describing the lifecycle.

## Files changed

- `docs/governance/REQUEST_LIFECYCLE.md`;
- `CHANGELOG.md`;
- `docs/governance/MODULES.md`, `docs/governance/AUTHORITY_INDEX.md` (indexing);
- `ai_logs/2026-06-01-request-lifecycle-metis.md`.

## Explicit non-implementation

No files were touched under:

```text
schemas/
tests/
operations/
platform/
Docker
.env
pyproject.toml
CLAUDE.md
```

## Boundary phrase

```text
MÈTIS understands and holds the cap, when the demand is unclear.
ZEUS arbitrates the status, on evidence.
The human decides at the cliffs and engages.
```
