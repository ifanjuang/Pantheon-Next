# Governance CI lockfile

Date: 2026-06-23

## Context

PR #209 centralized Governance CI dependencies.

PR #210 pinned direct Governance CI dependencies.

The remaining limitation was that transitive dependencies could still drift between GitHub Actions runs.

## Change

This intervention adds a lightweight lockfile structure under `.github/requirements/`:

```text
governance-ci.in       direct dependency intent
governance-ci.lock.txt direct + transitive dependency set
governance-ci.txt      stable workflow entry point delegating to the lockfile
README.md              maintenance rule
```

The workflow keeps its existing stable install path:

```text
.github/requirements/governance-ci.txt
```

That file now delegates to:

```text
.github/requirements/governance-ci.lock.txt
```

## Locked dependency set

```text
attrs==26.1.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
PyYAML==6.0.3
referencing==0.37.0
rpds-py==2026.5.1
typing-extensions==4.15.0
```

## Governance classification

Status: implemented CI maintenance.

Authority: non-doctrinal adapter / CI support.

Decision Zeus: non applicable.

Repository state: implemented for Governance CI dependency reproducibility only.

This does not change Pantheon doctrine, schemas, tests, runtime behavior, approval behavior, memory rules or execution boundaries.

## Risk and limitations

This is a lightweight lockfile without hashes. It improves reproducibility by freezing direct and transitive package versions, but it is not a full supply-chain hardening mechanism.

A future hash-locked requirements file or `pylock.toml` should be treated as a separate decision because it changes the CI dependency policy more strongly.

No changes were made under `schemas/`, `tests/`, `pyproject.toml`, `operations/`, `platform/`, Docker or `.env`.
