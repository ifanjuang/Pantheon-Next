# 2026-09-12 — Hermes runtime-efficiency review hardening

Issue: #1047
PR: #1048

## Trigger

Automated PR review identified three ways the qualification harness could overstate efficiency:

- a non-complete run could look cheaper because it stopped early;
- source-recall comparability used only the number of checks, not their stable identities;
- non-finite elapsed-time values could enter deltas and JSON output.

## Decision

Harden the existing qualification lab only. Do not introduce a new owner, schema authority, runtime integration or SoL-derived component.

## Changes

- cost preference now requires both baseline and candidate `result_status == complete`;
- candidate `blocked`/`failed` remains a regression; other non-complete comparisons are inconclusive;
- observed source recall now requires stable opaque `source_recall_check_ids` with exact count agreement;
- A/B source-recall perimeter comparison uses those stable identities rather than count alone;
- non-finite `elapsed_seconds` values are rejected;
- JSON output uses `allow_nan=False`;
- targeted regression tests cover all three findings;
- lab documentation records the stricter contract.

## Preserved boundaries

```text
qualification harness != runtime integration
lower cost != better result
partial execution != equivalent execution
same check count != same source-recall perimeter
reduction != Evidence
runtime success != authorization
```

No Hermes runtime configuration, deployment, persistence, Evidence admission, Role, Rite, Capability Slot or Pantheon authority owner is changed.

## Completion condition

The review findings are complete only when the updated PR head passes the dedicated qualification workflow and the repository-wide governance, architecture and implementation checks.
