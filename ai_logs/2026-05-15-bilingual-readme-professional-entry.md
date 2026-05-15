# AI Log — Bilingual README professional entry

Date: 2026-05-15

## Scope

Restructured the main README strategy into a bilingual public entry point:

- `README.md` is now the English primary GitHub entry point.
- `README.fr.md` is now the full French professional-facing version.

## Changes

- Preserved the professional onboarding structure centered on real dossiers, confidentiality, source control, memory and decision governance.
- Added cross-links between English and French README files.
- Kept the same conceptual structure across both languages to reduce drift.
- Preserved the central doctrine:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

French version keeps:

```text
OpenWebUI expose.
Hermes Agent exécute.
Pantheon Next gouverne.
```

## Boundary check

This intervention did not modify:

- `CLAUDE.md`;
- `pyproject.toml`;
- `schemas/`;
- `tests/`;
- `operations/`;
- `platform/`;
- Docker files;
- `.env`.

No runtime behavior was introduced.

No autonomous execution, scheduler, queue, provider router, auto-promoted memory or hidden workflow runtime was introduced.

## Follow-up

A later pass should reconcile `docs/governance/STATUS.md` with the current README and schema state.
