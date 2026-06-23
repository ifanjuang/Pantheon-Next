# Governance CI direct dependency pinning

Date: 2026-06-23

## Context

PR #209 centralized the read-only Governance CI Python dependencies in `.github/requirements/governance-ci.txt`.

The dependency set was still minimally constrained:

```text
jsonschema>=4.18
referencing
pyyaml
```

That shape was sufficient to unblock CI but still allowed resolver drift on direct dependencies.

## Change

This intervention pins the direct Governance CI dependencies:

```text
jsonschema==4.26.0
referencing==0.37.0
PyYAML==6.0.3
```

The selected versions were checked against PyPI on 2026-06-23.

## Scope

Changed files:

```text
.github/requirements/governance-ci.txt
ai_logs/2026-06-23-governance-ci-direct-dependency-pinning.md
```

## Governance classification

Status: implemented CI maintenance.

Authority: non-doctrinal adapter / CI support.

Decision Zeus: non applicable.

Repository state: implemented for direct CI dependency resolution only.

This does not change Pantheon doctrine, schemas, tests, runtime behavior, approval behavior, memory rules or execution boundaries.

## Risk and limitations

This is direct dependency pinning, not a full hash-locked transitive lockfile. Transitive dependencies may still drift unless a future pass introduces a generated lock or hash-checked requirements set.

No changes were made under `schemas/`, `tests/`, `pyproject.toml`, `operations/`, `platform/`, Docker or `.env`.
