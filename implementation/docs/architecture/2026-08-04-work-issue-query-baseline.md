# Work Issue projection SQL baseline

Date: 2026-08-04

Status: measured implementation baseline — non-authoritative.

## Scenario

The measurement creates three empty Work Issues for one exact `case_ref`, resets the SQL counter and executes:

```text
work_issue_read.list_issue_projections(connection, case_ref)
```

The probe uses a real PostgreSQL connection wrapped only to count `execute` calls. It does not replace owner reads, projection logic or governed schema validation.

## Baseline

Main commit before optimization: `5731b458fb6488674d406c40b0b7a6b1beeb1156`.

```json
{
  "issue_count": 3,
  "projection_count": 3,
  "sql_queries": 16,
  "expected_current_formula": "1 + 5N",
  "queries_per_issue_after_id_selection": 5.0
}
```

The current path performs:

```text
1 query  — ordered issue identities for the exact case_ref
N queries — Work Issue rows
N queries — comments
N queries — Hermes runs
N queries — events
N queries — Work Card metadata
```

For three issues:

```text
1 + (5 × 3) = 16 SQL executions
```

## Interpretation

This is a demonstrated N+1 read pattern in a Cockpit projection. It does not imply that Work Issue aggregates should lose their governed shape or that the single-item `get_issue` path should change.

## Target for the next PR

Batch the list projection only, preserving:

- exact `case_ref` scope;
- issue ordering and final status ordering;
- comments, runs and events ordering;
- Work Card metadata projection;
- one governed schema validation per aggregate;
- `work_activity` projection;
- single-item `get_issue` behavior.

Target query count:

```text
5 constant queries
issues + comments + runs + events + metadata
```

For three issues:

```text
16 -> 5 SQL executions (-68.75%)
```

## Non-equivalences

```text
batched read != broader scope
fewer queries != weaker validation
projection batching != aggregate mutation
query reduction != authorization
Cockpit read optimization != workflow engine
```
