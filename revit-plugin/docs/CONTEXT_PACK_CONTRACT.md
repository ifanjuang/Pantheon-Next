# Context Pack Contract

Status: contract candidate — documented non-implemented.

A context pack is a structured snapshot for reasoning.

It is not proof by itself.

It is not approval.

## Minimal shape

```json
{
  "context_pack_id": "ctx_example",
  "timestamp": "2026-07-05T00:00:00+02:00",
  "document": {
    "title": "example.rvt",
    "path_hash": "redacted"
  },
  "active_view": {
    "id": 123,
    "name": "Level 0"
  },
  "selection": []
}
```
