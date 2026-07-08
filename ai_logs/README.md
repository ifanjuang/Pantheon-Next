# AI Logs

Status: active support note — AI log index — implemented as documentation.
Boundary profile: validation_only_trace.

This directory stores traceability logs for significant AI-assisted repository operations.

Use `ai_logs/LOG_FORMAT.md` for future logs unless a specific intervention needs a longer narrative.

## Purpose

AI logs provide:

- migration traceability;
- governance-change traceability;
- simplification traceability;
- architecture decision history;
- review references.

## Rules

A significant repository intervention should add an AI log.

AI logs must:

- describe what changed;
- describe why the change was made;
- describe risks or limitations;
- avoid claiming implementation when content is still a stub;
- avoid exposing secrets or private project data;
- avoid repeating full boundary and non-equivalence boilerplate when a boundary profile and local distinctions are enough.

## Naming convention

```text
YYYY-MM-DD-short-description.md
```

Example:

```text
2026-05-12-governance-md-bootstrap-reconcile.md
```
