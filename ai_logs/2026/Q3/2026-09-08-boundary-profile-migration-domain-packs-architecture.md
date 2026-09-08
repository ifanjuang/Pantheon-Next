# 2026-09-08 — Boundary profile migration: docs/domain-packs/architecture/

## Change

Migrated the 19 documents in `docs/domain-packs/architecture/` that still
restated the exposure/execution/governance triad in prose onto declared
`Boundary profile` lines, per #996's suggested slicing order (next slice
after `docs/governance/` root and subdirectories, #1017/#1020).

Profiles chosen by reading each document's own `Status:` line and content,
not by pattern-matching text:

```text
18  candidate_support_note    all candidate/to-verify/implementation-candidate
                               documents that propose, explore or frame a
                               direction not yet accepted, including
                               PROJECT_UNDERSTANDING_EXTERNAL_REFERENCES.md
                               (corrected from an initial external_reference_
                               review choice per Codex review on #1022: that
                               profile requires a completed, version-pinned
                               review, and this document explicitly says
                               every entry is still awaiting audit - listing
                               external things is not itself a completed
                               review of them)
 1  candidate_support_note    PROBATIVE_INSTRUCTION.md, with a documented
                               local exception: its triad block carried two
                               extra distinct lines ("The architect decides."
                               / "The validated remains.") beyond the
                               generic three - kept verbatim, only the
                               generic three lines removed, following the
                               precedent set by WORK_ISSUE_AND_DELEGATED_
                               MERGE_MODEL.md in #1017
```

Three of the 19 (`ROLE_ACTIVATION_MODEL.md`, `ROLE_FACETS.md`,
`ROLE_REFLEX_COORDINATION.md`) carry the `ROLE_` filename prefix and
triggered `.github/scripts/check_roles_rites_spaces_change.py`'s
Role/Rite/Space review-context guard. The PR body declares the required
eight sections (Change level: editorial; Observed need; Existing owners
checked; Overlap analysis; Affected consumers; Migration and rollback;
Authority impact; Runtime impact).

Two documents (`INDEX_EFFECT_MATRIX.md`, `PROOF_REGISTER.md`) also carried
a second, abstractly-worded restatement of the same triad ("In abstract
form: / The exposure surface exposes. / The execution runtime executes. /
Pantheon governs.") immediately after the standard one. Read both in full
first: this abstract block feeds nothing in the document's own analysis
that follows (a separate, unrelated "Core rule" / index-taxonomy section) -
it is pure duplicate boilerplate in different words, not local content, so
both blocks were removed.

None of the 19 were on `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES` (#995's
ratchet); that list is unchanged at 9 entries.

## Why

Next slice in #996's suggested order, now that all of `docs/governance/`
is done. No judgment beyond reading each document's stated status and
content was needed, except the abstract-triad and PROBATIVE_INSTRUCTION.md
cases above, both resolved by reading the surrounding text rather than
assuming.

## Boundary

Documentation-only change. No Status line changed, no authority gained or
lost, no schema, test logic or CI workflow touched.

## Verification

- All 6 governance checks pass.
- `python3 -m pytest tests/ -q` — 678 passed.
- Fresh count on `main` before this change: 52 documents restate the triad
  with no profile. After: 33 documents — `docs/domain-packs/` no longer
  appears in the remaining-work breakdown at all.
- Confirmed none of the 19 paths appear in
  `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES` before or after (grep, not assumed).

## Local distinctions

```text
profile declared != local deviation waived
abstract restatement of the triad != local content specific to the document
triad removed != role separation changed
```

Relates to #996 (does not close it — 33 of the original 112 documents
remain across `docs/examples/`, `docs/assets/`, `templates/`,
`hermes/profiles/`, `mcp-server/docs/` and `docs/roadmaps/`).
