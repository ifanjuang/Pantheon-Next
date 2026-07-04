# AI Log — Authority Index Decomposition Plan

Date: 2026-07-04

Repository: `ifanjuang/Pantheon-Next`

## Context

After several documentation additions, `docs/governance/AUTHORITY_INDEX.md` became increasingly long. The user asked whether it should be optimized or decomposed.

Assessment:

```text
AUTHORITY_INDEX.md should remain the authority interpreter.
It should not be removed or split abruptly.
Detailed rows may later move into sub-indexes if coverage behavior is preserved.
```

## Change made

Added:

```text
docs/governance/AUTHORITY_INDEX_DECOMPOSITION_PLAN.md
```

The document proposes a staged decomposition plan:

- keep `AUTHORITY_INDEX.md` as the master authority interpreter;
- move detailed rows later into optional sub-indexes;
- preserve promotion rule, placement test, terminology boundary, tool naming rule and protected-path summary in the master file;
- verify coverage checker behavior before moving rows;
- avoid a machine-readable YAML/JSON registry for now;
- start any future row migration with lower-risk groups such as external references or obsolete/absent items.

## Repo state

```text
Documented non-implemented.
```

No index rows were moved. No coverage script, schema, test, protected path, runtime or implementation artifact was changed.

## Decision classification

```text
Accepté:
- AUTHORITY_INDEX.md is too long for long-term maintainability.
- A decomposition plan is useful before any mechanical split.
- The master file should remain the authority interpreter.

Refusé:
- Removing AUTHORITY_INDEX.md.
- Creating competing authority sources.
- Moving rows before coverage behavior is verified.
- Converting immediately to a machine registry.

À vérifier:
- Behavior of `.github/scripts/check_index_coverage.py` with grouped rows and possible sub-indexes.
- Whether `docs/governance/authority/` is the right future directory.
- Whether the new validation-only plan needs explicit `AUTHORITY_INDEX.md` row coverage or can remain as a planning note until accepted.

À arbitrer:
- Exact number of sub-indexes.
- First migration group if the plan is accepted.
```

## Notion

The GitHub repository remains canonical. Notion should be updated if a PR is opened from this branch.
