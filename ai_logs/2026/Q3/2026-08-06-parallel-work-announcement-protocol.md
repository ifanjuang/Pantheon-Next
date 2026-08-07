# Parallel work is announced by file path, not by theme

Date: 2026-08-06
Status: working agreement documented; no automated enforcement.
Scope: repository-wide work rule in `CLAUDE.md`.

## What happened

Two agents implemented the same `pantheon-mvp` defect fix independently. Both
were correct, but one branch also carried an unrelated correction from
`CURRENT_TIMESTAMP` to `clock_timestamp()` that could have been lost during a
superficial rebase without causing the existing tests to fail.

The two chantiers had different thematic names, but touched the same files:

```text
mvp_vertical/information_projection.py
mvp_vertical/knowledge_edit_variants.py
mvp_vertical/sql/013_information_card_projection.sql
tests/test_information_projection.py
```

One side also renamed `sql/012_information_card_projection.sql` to `013`; a theme
name cannot express that collision.

## Decision

Before significant parallel work, announce the repository paths that may be
changed. A rename announces both the old and new path. When two active
announcements overlap, divide or sequence the shared paths before modification.

```text
announcement != lock
intersection != conflict
theme != file scope
```

The announcement grants no authority, reserves no responsibility and does not
replace review, tests or merge reconciliation.

## Placement

The concise working rule is in `CLAUDE.md` under `Work rules`, because it applies
to every significant repository change rather than one product roadmap.

The temporary addition to
`docs/roadmaps/ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md` was removed. That
roadmap remains the authority for the adaptive project lifecycle and Cockpit
sequence, not repository coordination procedure.

## Verification posture

No check, lock service or reservation mechanism is added. The rule remains a
human-agent working agreement and must not be described as implemented
enforcement.

No schema, runtime, authority vocabulary, product behavior or external effect is
changed by this entry.

## Final rebase verification

The branch was rebased onto the final `main` after the accepted ProjectClaim,
Revit, Project Anatomy, Hermes preparation, retrieval coverage and landing-diagram
changes were merged. A backup of the pre-rebase head was retained at:

```text
backup/pr-553-before-rebase-20260807
```

The product roadmap is unchanged from `main`. The final diff is limited to this
journal, the concise `CLAUDE.md` work rule and the generated AI-log index.
