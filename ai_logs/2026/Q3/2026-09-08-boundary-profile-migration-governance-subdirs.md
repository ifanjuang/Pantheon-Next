# 2026-09-08 — Boundary profile migration: docs/governance/ subdirectories

## Change

Migrated the 13 documents in `docs/governance/examples/mvp_vertical_fixture/`,
`docs/governance/rites/` and `docs/governance/reference_reviews/` that still
restated the exposure/execution/governance triad in prose onto declared
`Boundary profile` lines, per #996's suggested slicing order (this is the
slice right after #1017's `docs/governance/` root pass).

Profiles chosen by reading each document's own `Status:` line and framing,
not by pattern-matching text:

```text
 9  candidate_support_note   the 9 mvp_vertical_fixture notes (each
                              proposes/frames a candidate direction)
 1  documentation_only       mvp_vertical_fixture/README.md (corrected from
                              an initial candidate_support_note choice per
                              Codex review on #1020: it only explains an
                              existing fictional fixture and is explicitly
                              non-normative, not a candidate direction -
                              grouping it with its siblings was exactly the
                              mistake BOUNDARY_PROFILES.md warns against:
                              classify what the document is and does, not
                              what it sits next to)
 2  candidate_support_note   EXTERNAL_REPO_QUALIFICATION_RITE.md,
                              RITE_TRIGGER_CATALOGUE.md (both explicitly
                              "candidate", proposing an unadopted procedure)
 1  external_reference_review MCP_SPEC_2026_07_28_REVIEW.md (a review of an
                              external spec release, matching the precedent
                              set by SPICE_REFERENCE_DISTILLATION.md in #1017)
```

All 13 carried the same `OpenWebUI exposes. / Hermes Agent executes. /
Pantheon Next governs.` fenced block, removed once the profile line was
added — the profile inherits the generic separation per
`BOUNDARY_PROFILES.md`'s "Inherited role separation" section (added in
#1005/#1017's precedent).

Dropped the same 13 paths from `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES` in
`tests/test_openwebui_integration_owner_retirement.py` (#995's ratchet):
22 -> 9 entries.

## Why

Next slice in #996's suggested order after the `docs/governance/` root
(#1017). No judgment beyond reading each document's stated status was
needed: none of the 13 has a local deviation beyond what its chosen profile
already means (no protected-path change, no schema/CI/runtime claim).

## Boundary

Documentation-only change. No Status line changed, no authority gained or
lost, no schema, test logic or CI workflow touched — only the ratchet's
allowlist shrank, as the ratchet itself requires.

## Verification

- All 6 governance checks pass.
- `python3 -m pytest tests/ -q` — 678 passed (ratchet test included; a
  shrink-only allowlist change cannot itself break the ratchet's own
  invariants, and the full suite confirms no other document referencing
  these 13 broke).
- Fresh count on `main` before this change: 65 documents restate the triad
  with no profile, 22 residue entries. After: 52 documents, 9 residue
  entries — `docs/governance/` no longer appears in the remaining-work
  breakdown at all.

## Local distinctions

```text
profile declared != local deviation waived
triad removed != role separation changed
ratchet shrinking != class of problem removed (that is #996's full scope)
```

Relates to #996 (does not close it — 52 of the original 112 documents
remain across `docs/domain-packs/`, `docs/examples/`, `docs/assets/`,
`templates/`, `hermes/profiles/`, `mcp-server/docs/` and `docs/roadmaps/`).
