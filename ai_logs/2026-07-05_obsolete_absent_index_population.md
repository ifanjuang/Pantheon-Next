# AI Log — Obsolete and Absent Index Population (first migration group)

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Context

Continuation explicitly requested by the user ("merge et continue") after
PR #281 (sub-index skeletons, plan step PR B) was merged. This executes
the first migration group of `AUTHORITY_INDEX_DECOMPOSITION_PLAN.md`
(step PR D, group obsolete/absent), the group both the plan and the #276
review recommended starting with.

## Finding that reshaped the step

The Current authority map contains no obsolete, refused or voluntarily
absent rows: the coverage check only forces candidate docs into the
index, so obsolete material was simply never indexed. The "migration"
is therefore almost entirely **additive**: the sub-index records
decisions that were previously scattered in per-file Status headers,
`STUB_RESOLUTION_PLAN.md` and `CLAUDE.md`, rather than moving rows out
of the master. Exactly one master row migrates.

## Changes made

```text
docs/governance/authority/OBSOLETE_AND_ABSENT_INDEX.md (populated):
- 17 obsolete documents (evidence topology corpus, resolved stubs,
  merged OpenWebUI/role/workflow notes), each mirroring its own
  per-file Status: obsolete header, which stays the source of truth;
- the dashboard/ voluntary absence (doctrine in CLAUDE.md);
- the "historical bootstrap stubs" row, migrated verbatim from the
  master map (its three named files are now Status: obsolete);
- status raised from skeleton to "populated; awaiting review",
  keeping the candidate family.

docs/governance/AUTHORITY_INDEX.md:
- removed the migrated historical-stubs row from the Current
  authority map (the only row moved);
- Bootstrap stub rule now points to the sub-index for the records
  while the rule itself stays in the master;
- grouped row and Sub-index map prose updated: obsolete/absent map
  populated, other sub-indexes remain skeletons.
```

## Coverage safety

```text
None of the 17 obsolete docs has "candidate" in its Status header, so
none requires master-index coverage; the migrated stub row's backticked
names carry no docs/ prefix and are not indexed paths. No change to
check_index_coverage.py or any checker was needed — as predicted for
this group during the #276 review.
```

## Boundary

```text
No promotion, no reinstatement, no deletion of any file.
No change to .github/scripts, schemas/, tests/, operations/,
platform/, Docker files, pyproject.toml or .env files.
The master index remains the sole authority interpreter.
```

## Repo state

```text
Obsolete/absent sub-index: implemented as documentation (candidate,
awaiting review). Remaining sub-indexes: skeletons. Next groups
(external references, architecture, runtime adapters) blocked on
PR C coverage decision for candidate-status rows.
```
