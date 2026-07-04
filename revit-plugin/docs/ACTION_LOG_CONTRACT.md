# Revit Action Log Contract — Skeleton

Status: contract candidate — documented non-implemented.

This file describes the intended local action log shape for a future Revit 2027 plugin. It is not a schema and does not implement logging.

## Purpose

The action log records what the plugin attempted or performed locally.

It is a trace candidate, not an Evidence Pack by itself.

```text
The log records.
The evidence supports.
The approval validates.
The human decides.
```

## Minimal JSONL entry

```json
{
  "action_id": "act_2026_000001",
  "session_id": "session_000001",
  "timestamp": "2026-07-04T00:00:00+02:00",
  "revit_version": "2027",
  "document_title": "example.rvt",
  "document_path_hash": "redacted_or_hash",
  "active_view_id": 123,
  "tool_id": "revit.create_text_note",
  "effect": "write_light",
  "status": "candidate_or_executed",
  "transaction_name": "Pantheon Revit Gate - Create Text Note",
  "selected_element_ids": [456],
  "created_element_ids": [789],
  "modified_element_ids": [],
  "warnings": [],
  "approval": {
    "required": true,
    "mode": "local_human_confirmation",
    "result": "accepted"
  }
}
```

## Rules

```text
Log document title before any action.
Log transaction name for any write_light action.
Log affected ElementIds where available.
Never log secrets.
Prefer path hashes or redacted paths.
Do not promote the log to proof automatically.
Do not treat a successful transaction as governance approval.
```

## First supported effects

```text
read_only
candidate_only
write_light
export
log
blocked_v0
```

## Excluded from first prototype

```text
write_model
external_effect
save
sync
delete
execute_generated_code
```
