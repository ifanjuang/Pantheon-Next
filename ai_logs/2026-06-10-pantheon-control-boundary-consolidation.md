# AI log — Pantheon Control consolidation into one boundary document

Date: 2026-06-10.

## Intent

Execute step 7 of the open-PR triage plan (see
`ai_logs/2026-06-10-open-pr-triage-plan.md`): the Pantheon Control family
proposed in PR #67 (seven documents, ~2 700 lines) and PR #72 (installation
boundary) contradicted the sprawl pause (issue #41), the consolidation step
of `TARGET_ARCHITECTURE.md` and the 2026-06-09 monorepo decision
(`dashboard/` + `mcp-server/` as the bounded modules).

## Work performed

- Added `docs/governance/PANTHEON_CONTROL_BOUNDARY.md` as a single slim
  candidate boundary note: what the `dashboard/` surface is, what it is not,
  the installed/connected/authorized/validated distinction, the NAS and
  read-only mount posture, forbidden behavior, and the absorption note for
  the former drafts.
- PR #67 and PR #72 are closed referencing this note; their feature-level
  material (document/media stack, observability and voice, mobile-first UX,
  implementation phasing) may return later as individually scoped governed
  candidates.

## Boundary

Documentation only. Candidate until reviewed. No dashboard code, installer,
Docker stack, `.env`, schema, test, scheduler, queue, approval engine or
memory engine is implemented. No protected path touched.

## Repo state

Documented non-implemented.
