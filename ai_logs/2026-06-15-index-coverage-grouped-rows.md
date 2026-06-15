# AI Log — Index-coverage honors grouped rows (Lot A)

Date: 2026-06-15

## Trigger

Lot A of the governance-hygiene pass (map in
`GOVERNANCE_LINKAGE_RECONCILIATION.md`, #138). User decision: align the check to
honor grouped AUTHORITY_INDEX rows rather than index ~16 members individually.

## Doctrine read first (MD before code)

`.github/scripts/check_index_coverage.py` already encoded the sanctioned grouped
prefixes in `FUTURE_OR_GROUPED` (`docs/governance/reference_reviews/`,
`docs/governance/rites/`, `docs/governance/DATA_PLATFORM_*.md`, …) — but only the
*second* loop (validating that indexed paths resolve) honored them. The *first*
loop (candidate coverage) required each candidate's literal path string in the
index text, so members of an already-indexed group were flagged. The grouped
rows in `AUTHORITY_INDEX.md` clearly intend to index their members; the check
simply did not apply that intent consistently.

Per CLAUDE.md (code may expose a better implementation only after the doc is
updated), the convention was written into `AUTHORITY_INDEX.md` first: a row whose
path is a directory (`/`) or glob (`*`) is a grouped row that indexes every
governance doc it matches; coverage is visibility only and does not promote a
member's authority class.

## Change

- `AUTHORITY_INDEX.md`: added the grouped-row coverage convention above the map.
- `check_index_coverage.py`: the candidate-coverage loop now treats a candidate
  as indexed when its literal path is present **or** a grouped row matches it.
  Groups are derived from the index's own backticked paths (single source of
  truth), restricted to entries **under** `docs/governance/` and strictly deeper
  than the root.

### Notable decision

The bare governance root `docs/governance/` appears in index prose and is
captured by the path regex. An unrestricted directory-group rule made it match
every candidate, masking all 34 — including the 18 genuine top-level candidates
that Lot C must still index. The fix excludes the docs root (and any shallower
prefix) from grouping, so only real collection rows
(`reference_reviews/`, `rites/`, `DATA_PLATFORM_*.md`) cover their members.

## Boundary

Read-only check refinement + index documentation. No file is modified by the
check; no doctrine reclassified; the governance core gains no runtime. Coverage
is visibility only.

## Verification

- Absolute `candidate-not-indexed`: 34 → **18**. The 16 retired are the 11
  `reference_reviews/` notes, the 1 `rites/` catalogue and the 4
  `DATA_PLATFORM_*` docs. No grouped member remains flagged.
- The 18 remaining are all genuine top-level candidates — Lot C scope.
- All four read-only checks with `GOVERNANCE_BASE_REF=origin/main` → exit 0,
  zero new findings.
