# AI Log — Internal-link reconciliation (Lot D)

Date: 2026-06-15

## Trigger

Lot D of the governance-hygiene pass (map in
`GOVERNANCE_LINKAGE_RECONCILIATION.md`, #138). Eight `check_internal_links.py`
findings, of four distinct natures. User decision: full repair by nature (8 → 0).

## Doctrine read first

Each flagged line was read in context before acting. This corrected one initial
diagnosis:

- **Not a typo.** `hermes/profiles/hephaestus/` in `GLOSSARY.md` sits under the
  heading **"Do not use as canonical spelling:"** — it is a deliberate
  counter-example. The canonical block directly above already uses
  `hephaistos/` (confirmed by `hermes/profiles/hephaistos/README.md`: "Canonical
  spelling … `hermes/profiles/hephaistos/`"; "`HEPHAESTUS` is not canonical").
  Editing it would have destroyed the glossary's point. Treated as a check false
  positive instead.

## Change

`check_internal_links.py`:
- `find_refs` now skips a path match immediately followed by `*`, so a
  glob/grouped row (`docs/governance/DATA_PLATFORM_*.md`) is not mis-read as the
  truncated reference `docs/governance/DATA_PLATFORM_`.
- `EXCLUDED_PATHS` gains five commented entries:
  - `hermes/profiles/hephaestus/` — deliberate non-canonical counter-example.
  - `docs/implementation/data-platform/`, `docs/adapters/data-platform/`,
    `schemas/evidence-memory/`, `docs/governance/PANTHEON_EVIDENCE_MEMORY.md` —
    forward-looking target paths named in planning/review notes, not yet created.

`PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md`:
- The "likely support sources" list pointed at `PANTHEON_CONTROL_DASHBOARD.md`
  and `PANTHEON_CONTROL_INSTALLATION.md`, both absorbed into and superseded by
  `PANTHEON_CONTROL_BOUNDARY.md` (per that doc, which supersedes the PR #67/#72
  drafts). The two stale lines are replaced by the single boundary doc.

## Boundary

Read-only check refinement + one documentation repoint. The check modifies no
files; no doctrine reclassified; no runtime added.

## Verification

- Absolute internal-link findings: 8 → **0**.
- All four read-only checks with `GOVERNANCE_BASE_REF=origin/main` → exit 0,
  zero new findings.
