# 2026-09-08 — Boundary profile migration: docs/assets/, and #996's two open scope decisions

## Change

Resolved both scope decisions #996 left open, per maintainer instruction
("on rend cohérent" — make it consistent):

### Decision 1: `docs/assets/` is in scope, not exempt

#996 asked whether illustrative/narrative assets should carry Boundary
profiles at all, or be legitimately out of scope. Decided: in scope.
Leaving them out would recreate the exact class of problem #996 exists to
eliminate — documents that still hand-roll the separation triad instead of
declaring it once. All 10 documents in `docs/assets/` that restated the
triad now declare a profile, chosen by reading each document's own
`Status:` line and content:

```text
7  documentation_only        pantheon-map/README.md, workflow-under-hood/
                              README.md, and 5 pantheon-rpg/ visual-
                              production files - explanatory support
                              material, proposing nothing
1  active_support_doctrine   docs/assets/README.md itself - it operationalizes
                              already-accepted placement rules (see
                              NEXT_MVP_REPOSITORY_PLACEMENT.md) for how
                              assets get labeled and classified, rather
                              than proposing new doctrine or just
                              explaining an idea
1  candidate_support_note    LANDING_STACK_REVISION.md - its own Status
                              line says "candidate editorial patch": it
                              proposes a concrete landing-page revision,
                              not yet accepted
1  validation_only_trace     distillation-note.md - a dated (2026-05-17)
                              record of a completed review of outside
                              inspiration material, extracting a pattern
                              and rejecting drift; not a candidate
                              proposal or a completed, version-pinned
                              external_reference_review (no source or
                              version is named - the same gap Codex
                              flagged on #1022's PROJECT_UNDERSTANDING_
                              EXTERNAL_REFERENCES.md, applied here
                              proactively rather than after correction)
```

Two files carried a locally meaningful second block beyond the generic
triad, kept verbatim: `pantheon-map/README.md` and `workflow-under-hood/
README.md` both keep "The Registre Probatoire proves. / The human
decides." (not covered by generic inheritance, per the #1017/#1022/#1024
exception precedent). `pantheon-rpg/README.md` keeps its "game-world
translation" block (interface/workshops/city language) since that
translation is the document's own local content, not boilerplate - only
the bare 3-line triad immediately above it was removed.

### Decision 2: `mcp-server/docs/HERMES_INTEGRATION_CONTRACT.md` needed explicit fields, not a profile line

This document names a concrete surface (`mcp-server/`) and states exactly
what it may and must not do. `BOUNDARY_PROFILES.md` is explicit that this
is not the inheritance case: *"A document that names a specific exposure,
execution, governance or approval surface is making a concrete claim
about that surface and must state it with the [boundary] fields."*
Replaced the generic 3-line triad with the `exposed_by / executed_by /
governed_by / approved_by / forbidden` fields the document already had
the content for (its own existing "It may" / "It must not" lists), rather
than reducing it to a `Boundary profile:` line that would misrepresent a
concrete claim as generic inheritance.

None of the 11 documents touched here were on `KNOWN_CANDIDATE_
OPENWEBUI_RESIDUES` (#995's ratchet, verified by grep); that list is
unchanged at 9 entries.

## Why

Both decisions were flagged in #996 and its follow-up comments but never
settled, leaving `docs/assets/` and `mcp-server/docs/` outside every
slice's plan. Settling them now closes both gaps rather than leaving them
as permanent exceptions with no stated rationale.

## Boundary

Documentation-only change. No Status line changed except the addition of
`Boundary profile:` lines (or, for the one concrete-surface document, the
boundary fields); no authority gained or lost, no schema, test logic or
CI workflow touched.

## Verification

- All 6 governance checks pass, plus `check_runtime_boundary_language.py`
  and `check_asset_references.py` (directly relevant to `docs/assets/`
  and `mcp-server/docs/`).
- `python3 -m pytest tests/ -q` — 678 passed.
- Fresh count on `main` before this change: 20 documents restate the
  triad with no profile. After: 9 — neither `docs/assets/` nor
  `mcp-server/docs/` appears in the remaining-work breakdown at all.

## Local distinctions

```text
narrative/illustrative asset != out of scope for boundary declaration
concrete surface claim != generic role separation (needs fields, not a profile line)
dated review record with no named source/version != a completed external_reference_review
```

Relates to #996 (does not close it — 9 of the original 112 documents
remain across `templates/` (5), `docs/audits/` (2, correctly staying —
dated historical traces, explicit non-goal), `hermes/profiles/` (1) and
`docs/roadmaps/` (1)).
