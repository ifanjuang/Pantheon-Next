# Parallel work is announced by file path, not by theme

Date: 2026-08-06
Scope: `docs/roadmaps/ADAPTIVE_PROJECT_LIFECYCLE_COCKPIT_PLAN.md` §19
Axes: E4 certainty, V4 verification, K2 consequence, C2 approval (human decision, recorded)

## What happened

Two agents work the A–J tranches in parallel. On 2026-08-06 both implemented the
same defect fix in `pantheon-mvp`, independently, within the same week: an upsert
in `add_document_link` recorded `document_link_added` for a call that was a
modification, so a role change entered the append-only history as a link creation
that never occurred.

Both implementations were correct. One used a preceding `SELECT`, the other
`RETURNING (xmax = 0)`.

The waste is not the point. The near-miss is: one side also carried an unrelated
correction — `occurred_at` moving from `CURRENT_TIMESTAMP` to `clock_timestamp()`,
without which two events written in one transaction cannot be ordered. Merging
the other side first and rebasing without reading would have dropped it silently,
and no test would have failed, because a passing suite does not exercise the
ordering the correction restores.

## Why the theme was not enough

The two chantiers were announced as "document link semantics" and "converge
Source, Information and EntityRef edges". Disjoint, by their names. Their files
were not:

```text
mvp_vertical/information_projection.py
mvp_vertical/knowledge_edit_variants.py
mvp_vertical/sql/013_information_card_projection.sql
tests/test_information_projection.py
```

One side additionally renamed `sql/012_information_card_projection.sql` to `013`,
which a theme cannot express at all.

## Decision

Human decision, this date: a chantier is announced by the files it will touch. A
rename counts as touching both names. Where two announcements intersect, the
intersection is settled before either starts.

An announcement is not a lock and grants nothing. It is the only artifact that
makes a collision visible while it is still cheap — at merge, the reconciler is
choosing between two finished implementations and is the only party positioned to
notice what is about to be lost.

## Status

- documented: §19 of the plan, beside the other coordination decisions.
- not implemented: nothing enforces this. It is a working agreement between the
  human and the agents, not a check. Recording it as implemented would be exactly
  the naming-without-verification failure this repository keeps finding.

## Boundary

```text
announcement != lock
intersection != conflict
theme        != file
```

No governance authority, schema or vocabulary is changed by this entry.
