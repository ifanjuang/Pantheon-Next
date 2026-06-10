# AI log — Open PR triage plan (9 open PRs)

Date: 2026-06-10.

## Intent

The maintainer asked for a triage plan for the 9 open pull requests. This log
records the analysis and the proposed sequence as a trace. It decides
nothing: every merge/close decision below is a recommendation for the
maintainer.

## Cross-cutting facts observed

- `CHANGELOG.md` was rotated on main (entries 0.1.12–0.1.41 archived), so PRs
  that add CHANGELOG entries (#87, #44) will conflict and need a rebase.
- The index files (`AUTHORITY_INDEX.md`, `MODULES.md`, `STATUS.md`) were
  reindexed by E5 on main; PRs that touch them (#71, #44) must be rebased and
  merged serially.
- The governance CI now guards against Registre Probatoire vocabulary
  regression (#92); older PR branches predate the sweep and may fail the lint
  until re-aligned.
- The GLOSSARY now owns four axes (E0–E4, V0–V4, K0–K4, C0–C5). PR #35 still
  uses `C0_administrative … C5_liability_safety_regulatory` as consequence
  levels, which now collides with the C-axis (approval ceiling); the
  consequence axis is K. PR #71's hardening already renamed its consequence
  levels C→K.
- The 2026-06-09 monorepo decision (`mcp-server/`, `dashboard/` in-repo)
  supersedes the `pantheon-control/…` layout referenced by #72 and #75.

## Proposed sequence (recommendation)

1. **#76** — vertical example (Maison Lierre). Lowest risk, no index files,
   includes two lint wording fixes. Merge first; it becomes the test object
   for the future proven vertical.
2. **#87 (E6)** — schema rename proposal. Rebase (CHANGELOG conflict), merge
   the proposal doc, then the maintainer walks the approval checklist; the
   protected-path rename itself lands in a separate follow-up PR.
3. **#71** — Answer Verification Gate. Rebase on main, align vocabulary with
   the post-E2/E5 state (GLOSSARY stays owner of V/K axes; no "Canonical
   Memory" phrasing), then merge as candidate. Unblocks E4 (bridge rule).
4. **#44** — Governed Form Filling. Rebase (CHANGELOG + index files);
   maintainer decides whether it enters as candidate rather than
   self-declared active support doctrine; vocabulary sweep; merge. It is the
   CERFA use case.
5. **#75** — MCP Policy Server development roadmap. Update the placement
   section from `pantheon-control/mcp-policy-server/` to `mcp-server/` per
   CLAUDE.md, then merge: it becomes the development roadmap for the bounded
   MCP module.
6. **#66** — module invocation / connectivity preflight. Merge as candidate;
   its MCP preflight and refusal tests feed the `mcp-server/` checks
   directly.
7. **#67 + #72** — Pantheon Control family (7 docs, ~2 700 lines + install
   boundary). Do not merge as-is: contradicts the sprawl pause (#41), the
   TARGET_ARCHITECTURE consolidation step and the monorepo decision.
   Recommendation: extract ONE slim boundary document (dashboard boundary +
   NAS/install posture, aligned to `dashboard/` in CLAUDE.md), then close
   both PRs referencing it.
8. **#35** — Architecture Proof Register JSON schemas. Hold. Protected path;
   gated by #37 (schema reconciliation) and E6. Rework before merge:
   consequence levels to the K axis, repo schema conventions (YAML,
   x-boundary, governance_refs, examples, test coverage).

## Issues to close in the same motion

- #90 (vocabulary sweep) closes once the rebased PRs pass the CI guard.
- #41 (sprawl pause) is honored by step 7's consolidation.

## Boundary

Analysis and trace only. No doctrine changed, no PR merged or closed by this
log, no protected path touched.
