# Governance CI dependency centralization

Date: 2026-06-23

## Context

PR #177 fixed a failing Governance CI check by installing `referencing` directly in two workflow steps.

That fix was correct, but it left the dependency set duplicated inline in `.github/workflows/governance-ci.yml`.

## Change

This intervention centralizes the read-only governance CI Python dependencies in:

```text
.github/requirements/governance-ci.txt
```

The workflow now installs that requirements file once before the jsonschema-based governance checks and runs a smoke import for:

```text
jsonschema
referencing
yaml
```

## Scope

Changed files:

```text
.github/requirements/governance-ci.txt
.github/workflows/governance-ci.yml
ai_logs/2026-06-23-governance-ci-dependency-centralization.md
```

## Governance classification

Status: implemented CI maintenance.

Authority: non-doctrinal adapter / CI support.

Decision Zeus: non applicable.

Repository state: implemented for CI dependency installation only.

This does not change Pantheon doctrine, schemas, tests, runtime behavior, approval behavior, memory rules or execution boundaries.

## Risk and limitations

The dependency versions remain minimally constrained rather than fully pinned. This is acceptable for lightweight CI maintenance, but a future stricter reproducibility pass could pin exact versions or move the dependency group into `pyproject.toml` after explicit approval.

No changes were made under `schemas/`, `tests/`, `pyproject.toml`, `operations/`, `platform/`, Docker or `.env`.
