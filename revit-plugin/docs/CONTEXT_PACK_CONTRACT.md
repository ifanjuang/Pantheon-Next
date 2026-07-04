# Revit Context Pack Contract — Skeleton

Status: contract candidate — documented non-implemented.

This file describes the intended shape of a future Revit context pack. It is not a schema and does not implement validation.

## Purpose

A context pack is a structured snapshot of what Revit should expose to Hermes for reasoning.

It is not proof by itself.

It is not permission to modify the model.

```text
Context Pack Candidate -> Hermes reasoning -> Result Candidate -> preview / approval -> Revit transaction
```

## Minimal fields

```json
{
  "context_pack_id": "ctx_2026_000001",
  "timestamp": "2026-07-04T00:00:00+02:00",
  "revit": {
    "version": "2027",
    "build": "to_verify"
  },
  "document": {
    "title": "example.rvt",
    "path_hash": "redacted_or_hash",
    "is_workshared": false
  },
  "active_view": {
    "id": 123,
    "name": "Level 0",
    "type": "FloorPlan",
    "scale": 100
  },
  "selection": [
    {
      "element_id": 456,
      "category": "Walls",
      "name": "Basic Wall",
      "type_name": "Generic 200mm"
    }
  ],
  "visible_elements_summary": {
    "walls": 0,
    "doors": 0,
    "windows": 0,
    "rooms": 0
  },
  "image_refs": [
    {
      "kind": "active_view_capture",
      "path": "redacted/local/path.png",
      "width": 1920,
      "height": 1080
    }
  ],
  "warnings": [],
  "scope": {
    "source": "active_view_and_selection",
    "write_allowed": false
  }
}
```

## Rules

```text
Do not include raw private paths when a hash or redacted value is enough.
Do not include all parameters by default.
Do not include linked model data unless explicitly requested.
Do not treat visible geometry as complete model truth.
Do not authorize writes from context alone.
```

## Future validation

A later PR may add a machine-readable schema, but that would touch `schemas/` and requires explicit approval.
