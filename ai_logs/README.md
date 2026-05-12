# AI Logs

This directory stores traceability logs for significant AI-assisted repository operations.

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
- avoid exposing secrets or private project data.

## Naming convention

```text
YYYY-MM-DD-short-description.md
```

Example:

```text
2026-05-12-governance-md-bootstrap-reconcile.md
```
