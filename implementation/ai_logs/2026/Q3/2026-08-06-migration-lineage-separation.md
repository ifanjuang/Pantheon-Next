# Migration name normalization — two lineages separated

Date: 2026-08-06
Scope: `mvp_vertical/sql/`
Axes: E3 certainty, V3 verification, K1 consequence, C0 approval (read-only reorganization, no schema change)

## What was found

`mvp_vertical/sql/` carried four duplicate numeric prefixes: `003`, `004`, `005`
and `010`. The cause was not carelessness. Two sequences had been numbering
independently into one directory — the Agency/Cockpit lineage and the Hermes
lineage, the latter a contiguous `003`–`007` block.

Extracting every cross-file `REFERENCES` dependency showed that **no ordering was
violated**: all eleven inter-file dependencies were satisfied by the prefix order
and also by the composed initializer's replay order, which differs from it in
seven of twelve positions. The defect was in naming alone — `sql/003_*` matched
two files, so the prefix no longer identified a migration.

One further gap surfaced from the same reading: `sql/*.sql` in
`[tool.setuptools.package-data]` would not have matched a subdirectory, and the
vendored provenance sidecars (`*.source.json`) and the two later pin files were
not packaged at all, so a built wheel shipped schemas with no recorded origin.

## What was decided

Human decision, this date: separate the lineages rather than renumber globally.

```text
sql/            Agency and Cockpit    001,002,003,004,005,008,009,010…017
sql/hermes/     Hermes execution      003…007
```

Three of the four collisions disappear without changing any number. The fourth
was internal to the Agency lineage and was resolved by moving
`source_intake_admission` from `010` to the free `009` — earlier in every
initializer that replays both, so no effective order changed.

A global renumbering to `001…020` was rejected: it would rename twenty files and
twenty constants to encode an order that does not exist, since eight distinct
entry points replay different subsets in different orders.

## Status

- implemented: directory separation, the `009` move, the `017` prefix for
  `paperless_source_bindings`, the packaging patterns.
- implemented: `tests/test_migration_naming.py` — duplicate prefix within a
  lineage, constant naming a missing file, `.sql` file no module replays. Each
  assertion was verified to fail against a deliberately reintroduced violation.
- documented: `mvp_vertical/sql/README.md`.
- unchanged: every effective replay order. Full suite `1192 passed`, no skips.

## Boundary

```text
migration prefix != replay order
directory        != schema
rename           != schema change
```

No migration content was edited. Nothing here executes, approves, promotes or
admits anything.
