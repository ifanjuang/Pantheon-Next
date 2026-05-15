# Migration Playbook Canonical

Date: 2026-05-12

## Objective

Materialize the canonical `docs/governance/MIGRATION_PLAYBOOK.md` for Phase C, consolidating the arbitrated decisions D1 to D6 and the Pantheon-OS access channel choice recorded in issue #7.

## Source of arbitration

- Issue: `https://github.com/ifanjuang/Pantheon-Next/issues/7`
- Comment: ChatGPT arbitration on 2026-05-12T20:49:12Z

## Arbitrated decisions captured in the playbook

- D1 = OK. Better-than-Next OS content must first be proposed as a Pantheon-Next doctrine update; never silently integrated.
- D2 = a. Obsolete or contradictory OS content is not migrated by default; the stub is closed as `Voluntarily not migrated`.
- D3 = a. Oversized OS docs are condensed by default; split only if condensation destroys doctrine.
- D4 = b. Broken links to moved or removed files are fixed with a traceable migration note in the ai_log.
- D5 = a. Single OS SHA snapshot at start of Phase C. Later OS evolution handled as delta PRs after Phase C.
- D6 = defer. Diagrams and images go to Lot 8.

## Access channel captured in the playbook

C-1 chosen. Pantheon-OS to be added as a read-only repository to the Claude session permissions.

## Special rule captured in the playbook

GLOSSARY in Lot 1 is touched only if the OS diff carries a real terminological clarification missing from Next; otherwise a `no-op` decision is recorded in the migration ai_log.

## Coordination captured in the playbook

- Claude operates on `docs/governance/*.md` for Phase C.
- ChatGPT operates on `schemas/*` for Phase D (already started).
- No file overlap. Claude does not touch `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env*`, `pyproject.toml`, `CLAUDE.md`.
- ChatGPT does not touch `docs/governance/*.md` during Phase C migration PRs, except for post-merge reconciliation.

## Files created

- `docs/governance/MIGRATION_PLAYBOOK.md` (canonical Phase C doctrine).
- `ai_logs/2026-05-12-migration-playbook-canonical.md` (this file).

## Anti-runtime reminder

The playbook does not introduce a runtime, a scheduler, a queue, a message bus, a provider router, an installer, an endpoint, a Docker stack, a schema, a test or operations tooling. It defines documentation migration doctrine only.

## Pre-conditions before Phase C starts

- C-1 must be activated. Until then, no Phase C migration PR can begin.
- A single OS SHA snapshot must be recorded in `ai_logs/migration-mapping.md` at the start of Phase C, in the first migration PR.

## Out of scope for this PR

- No actual migration of any stub.
- No modification of any existing `docs/governance/*.md` stub.
- No modification of `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, root `README.md`, `docs/governance/README.md`.
- No modification of `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env*`, `pyproject.toml`.
- No modification of any Hermes profile.

## STATUS update reminder

After this PR is merged, the doctrine owner (ChatGPT) updates `docs/governance/STATUS.md` to add `MIGRATION_PLAYBOOK.md` under `Active governance documents`.

## Next required action

Owner enables C-1 (Pantheon-OS read access in Claude session). Then Claude opens the first Phase C migration PR for `ARCHITECTURE.md` as the Lot 1 gabarit.
