# 2026-09-09 — Boundary profile migration: final slice (templates/, hermes/profiles/, docs/roadmaps/)

Date: 2026-09-09

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

Migrated the last 7 documents restating the exposure/execution/governance
triad in prose onto declared `Boundary profile` lines, closing #996's
document migration. Profiles chosen by reading each document's own
`Status:` line and full content:

```text
4  non_executable_template   templates/architecture_probative_instruction/
                              pro_exe_responsibility_slice/README.md and
                              role_drift_early_warning_slice/README.md
                              (fill-in-the-blanks professional instruction
                              templates, not deployed); templates/
                              mcp_external_tool_review.md (a blank review
                              form); templates/context_handoff/
                              SESSION_HANDOFF.md (a numbered handoff
                              template) - applying the lesson from Codex's
                              PROMPTS.md correction on #1025: a template
                              document with concrete fill-in structure is
                              non_executable_template, not documentation_only
                              or candidate_support_note
3  candidate_support_note    hermes/profiles/PROFILE_CONSTITUTION.md (its
                              own "Status decisions" section still carries
                              open "To verify"/"To arbitrate" items - not
                              yet accepted doctrine, still a candidate
                              routing scheme); templates/prompt_templates/
                              README.md (self-declared "candidate support
                              note" on its own Status line); docs/roadmaps/
                              COCKPIT_CONSOLIDATION_ROADMAP.md (despite its
                              "validation-only roadmap" Status wording, its
                              content actively sequences and directs future
                              work across phases and issues with an
                              "Immediate work order" - the same
                              propose/direct shape that moved ROADMAP.md
                              and CORRECTIONS.md to candidate_support_note
                              on #1025, not the passive-record shape
                              validation_only_trace requires)
```

Two of the four `non_executable_template` files carried two locally
distinct lines beyond the generic triad, kept verbatim per the
#1017/#1022/#1024/#1025 exception precedent:
`pro_exe_responsibility_slice/README.md` keeps "The architect decides. /
The validated remains." (matching its own parent doctrine,
`PROBATIVE_INSTRUCTION.md`, exactly); `role_drift_early_warning_slice/
README.md` keeps "The architect reviews. / The human decides." The
roadmap's sole extra line ("The human decides.") was removed with the
rest of the block: unlike the paired cases above, this line stands alone
and duplicates ARCHITECTURE.md's own canonical doctrine (already
inherited by any declared profile), so it is not local content requiring
preservation - the same reasoning applied to `docs/assets/README.md` on
#1025.

None of the 7 were on `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES` (#995's
ratchet, verified by grep); that list is unchanged at 9 entries. None
matched `check_roles_rites_spaces_change.py`'s sensitive paths, so no
PR-body review-context sections were required this time.

## Why

Last slice of #996's document migration. `docs/audits/` (2 documents)
correctly remains outside scope - dated historical traces, an explicit
non-goal from #996's own text - so this closes the migration completely
rather than leaving a residual count.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: none — no `Status:` line changed beyond adding
`Boundary profile:` lines.
Schema/test/CI impact: none.
External action: none.
Memory behavior: none.

## Verification

- All 6 governance checks pass.
- `python3 -m pytest tests/ -q` — 678 passed.
- Fresh count on `main` before this change: 9 documents restate the triad
  with no profile. After: 2 — both in `docs/audits/`, both correctly out
  of #996's scope. No zone with in-scope documents remains.

## Local distinctions

```text
fill-in-the-blanks template != documentation explaining an idea
"validation-only" Status wording != validation_only_trace profile (content decides, not the word)
paired locally-distinct doctrine line != a lone line duplicating canonical inheritance
```

Closes #996: every in-scope document (112 originally counted, corrected
to varying totals as measurement methodology was refined across slices)
now declares a `Boundary profile` or, where a document names a concrete
surface, explicit boundary fields. The two open scope decisions (`docs/
assets/`, `mcp-server/docs/`) were resolved on #1025. `docs/audits/`
remains the one explicit, documented non-goal.
