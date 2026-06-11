# AI log — Lot 1 read-only governance checks

Date: 2026-06-10.

## Context

After #100 was merged, the maintainer chose option B: stabilize the repository with read-only CI checks before resuming the protected schema work around #87 / #97.

The partial E6 schema branch created during the previous attempt is intentionally not used in this lot.

## Work performed

Added read-only governance check scripts under `.github/scripts/`:

- `check_status_headers.py`
- `check_internal_links.py`
- `check_index_coverage.py`
- `check_axis_vocabulary.py`

Extended `.github/workflows/governance-ci.yml` to run these scripts in the existing Governance CI job, without replacing the existing checks.

## Boundary

Read-only CI checks only.

No schema file, schema example, test file, runtime, MCP server, dashboard module, platform component, Docker file, pyproject file or environment file was changed.

The scripts report violations and exit non-zero. They do not edit files.

## Repo state

Implemented as CI checks.

No doctrine was promoted.

No protected schema apply was performed.
