# AI Log — Coverage Check Tightening: Table Rows Only

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Context

User instruction "Ok améliore corrige et merge" on PR #287, following the
assessment that the decomposition's weakest point was substring-based
coverage: after the sub-index extension, a path mentioned anywhere in any
of seven files (prose included) counted as indexed.

## Change made

```text
.github/scripts/check_index_coverage.py: index_text() now returns only
Markdown table-row lines (lines starting with "|") from the master index
and the sub-indexes. Consequences:

- a candidate doc is indexed only by a deliberate table row (its own row,
  a mention inside a row, or a grouped row), never by a prose mention;
- grouped rows are likewise recognized only when declared in a table row;
- the missing-path validation now spans table rows only; prose path
  references remain validated by check_internal_links.py.

docs/governance/AUTHORITY_INDEX.md: the Sub-index map paragraph updated
to state the row-only rule.
```

## Verification

```text
Behavior tests (temp candidate doc, GOVERNANCE_BASE_REF=origin/main):
1. no mention anywhere            -> check fails (as before);
2. prose-only mention in sub-index -> check fails (new tightening);
3. table-row mention in sub-index  -> check passes.
Full local suite green: coverage, internal links, truncation,
net truncation, status headers, axis vocabulary, register instances,
vertical slice.
```

## Boundary

```text
Script change covered by the same in-session user approval as the
sub-index extension. No schema, test, operation, platform, Docker,
pyproject or .env change. No authority class or row moved.
```
