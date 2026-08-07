# AI log — Project Anatomy stable active artifact identities

Date: 2026-08-07
Scope: naming / authority-reference hygiene only
Base: `9cc6b7e7bb4e4631e5cb6bf6e33303dbba335023`

## Context

The cross-repository architecture-convergence guard requires active architecture artifacts to keep stable responsibility-based filenames. Contract generations and prior revisions belong in file content, metadata and Git history rather than in active filenames.

Project Anatomy had retained generation-named active artifacts after the V0.2 refactor and conceptual freeze. That conflicted with the already-established stable-artifact invariant and blocked `pantheon-mvp` H4c architecture audit.

## Changes

The active conceptual model is consolidated under one stable identity:

```text
docs/domain-packs/architecture/PROJECT_ANATOMY_MODEL.md
```

The former generation-named active documents are retired from the active tree:

```text
PROJECT_ANATOMY_V02_DESIGN_REVIEW.md
PROJECT_ANATOMY_V02_FROZEN_MODEL.md
```

Their historical content remains recoverable in Git history and prior PRs/ai_logs.

Active schema governance references are repointed to `PROJECT_ANATOMY_MODEL.md`. Validation shapes and semantic constraints are unchanged by those reference edits.

Two active contract-test files are also moved to stable responsibility-based identities:

```text
tests/test_apu_core_schemas.py
tests/test_apu_compatibility_registry.py
```

The test bodies are copied without behavioral changes; only the active filenames change.

## Protected paths

This slice deliberately touches `schemas/` and `tests/`, both protected areas, because the inconsistency itself lives in active schema governance refs and test artifact identities.

The protected-path changes are limited to:

- schema `governance_refs` / compatibility `authority_ref` path updates;
- test-file identity moves with unchanged test logic.

No schema validation rule, enum, required field, approval boundary, runtime behavior or executable effect is changed.

## Historical/versioned artifacts retained

Historical `ai_logs`, SQL migrations, external protocol releases and coexistence-required versioned imports remain generation/version named where that identity is part of their historical or compatibility role.

```text
historical record != active authority artifact
migration id != mutable active artifact identity
```

## Boundaries

```text
stable filename != frozen semantics forever
Git history != second authority
renamed test != changed validation
updated governance ref != schema implementation change
```

The Project Anatomy conceptual core and frozen boundaries remain unchanged. This slice exists only to make active artifact identity comply with repository convergence doctrine before executable H4c migration proceeds.
