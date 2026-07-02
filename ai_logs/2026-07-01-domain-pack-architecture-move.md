# AI log — execute the architecture domain-pack move (B-4)

Date: 2026-07-01.

Actor: Claude Code.

## Intent

Arbitration B-4 (accepted; maintainer chose **prefix drop**). Move the 24
`docs/governance/ARCHITECTURE_*.md` documents into `docs/domain-packs/architecture/`
with the `ARCHITECTURE_` prefix dropped, generic rules staying in `docs/governance/`,
per the migration table delivered in #257.

## Change

- `git mv` the 24 files → `docs/domain-packs/architecture/<name>.md` (prefix dropped).
- Rewrote every live reference to the moved files:
  - full paths `docs/governance/ARCHITECTURE_X.md` -> `docs/domain-packs/architecture/X.md`
    across `docs/` and `README.md`;
  - bare `ARCHITECTURE_X.md` prose mentions -> `X.md`;
  - `schemas/` `governance_refs` and `templates/` references (required — the schema
    `governance_refs` resolution test would otherwise fail on the old paths).
  - `ai_logs/` are history and are left unchanged (not scanned by the link check).
- `AUTHORITY_INDEX.md` rows for the 24 files now point to the new paths (updated in
  place; individual rows kept, so coverage stays green).

## Validation (local, GOVERNANCE_BASE_REF=origin/main)

All governance CI checks pass: `check_internal_links`, `check_index_coverage`,
`check_status_headers`, `check_no_truncation`, `check_no_net_truncation`,
`check_axis_vocabulary`. `python3 -m pytest tests/` -> 12 passed (schema
`governance_refs` now resolve). Runtime-phrase guard green. Zero `ARCHITECTURE_`
reference remains outside `ai_logs/`.

## Boundary

Reference-complete move. Touches `schemas/` and `templates/` only to repoint
references to the moved docs (no schema semantics changed); this is a consequence of
the authorized B-4 move. No new doctrine, no runtime, no promotion. Generic rules
stay in `docs/governance/`.
