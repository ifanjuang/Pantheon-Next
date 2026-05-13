# Migrate ARCHITECTURE — Phase C Lot 1 gabarit

Date: 2026-05-12

## Objective

First Phase C migration PR. Replaces the `Status: stub` `docs/governance/ARCHITECTURE.md` placeholder with content migrated from the Pantheon-OS snapshot. Acts as the gabarit for the remaining 21+ migration PRs.

## Snapshot

```text
Source archive : legacy/Pantheon-OS-main.zip
Captured in    : Pantheon-Next commit 9c2354b
Source file    : Pantheon-OS-main/docs/governance/ARCHITECTURE.md
Source length  : 509 lines
```

Phase C snapshot SHA is referenced through the Pantheon-Next commit `9c2354b` because the live Pantheon-OS repository is not reachable from this Claude session.

## Files in this PR

- `docs/governance/ARCHITECTURE.md`: stub replaced with migrated condensed content (~250 lines), `Status:` header rewritten to `migrated from Pantheon-OS snapshot ...`.
- `ai_logs/migration-mapping.md`: new — initializes the Phase C mapping table with one migrated row (`ARCHITECTURE.md`), 21 pending rows and a list of OS-only files awaiting arbitration.
- `ai_logs/2026-05-12-migrate-architecture.md`: this file.

No other files touched.

## Doctrinal transformations applied

- Renamed `Pantheon OS` to `Pantheon Next` throughout the document.
- Removed OS-specific domain identifiers (`architecture_fr`, `software`) from canonical body. Domain registration deferred to `MODULES.md`.
- Condensed or removed runtime detail: NAS, Portainer, FastAPI applications, Docker tags, scheduler reference, Hermes context export paths.
- Condensed OS sections 8 (skill XP and lifecycle implementation), 14 (runtime security execution detail), 15 (Hermes context exports) and 17 (installation operations) into governance references.
- Replaced OS `Pantheon defines and canonizes. Hermes executes. OpenWebUI exposes.` with the Pantheon Next canonical positioning `OpenWebUI exposes. Hermes Agent executes. Pantheon Next governs.`.
- Enforced HEPHAISTOS canonical spelling. No occurrence of HEPHAESTUS in the migrated document.
- Reduced 509 source lines to under 300 lines per playbook rule D3=a. No content split into multiple files.
- All cross-references resolve to existing Pantheon Next governance documents or active stubs.

## Invariant check

- [x] `Status: stub …` header removed; replaced by `Status: migrated from Pantheon-OS snapshot …`.
- [x] No Python, YAML schema, Dockerfile, environment file or installation script added.
- [x] No file added or modified under `schemas/`, `tests/`, `operations/`, `platform/`, repository root, `pyproject.toml`, `.env*`, `docker*`.
- [x] No modification of `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, root `README.md`, `docs/governance/README.md`.
- [x] No existing Hermes profile touched.
- [x] All Markdown references in the migrated document resolve to existing files (active docs or stubs present in `docs/governance/`).
- [x] Document length under 300 lines.
- [x] HEPHAISTOS spelling enforced.
- [x] Single governance file migrated; single ai_log; mapping file initialized.

## Out of scope for this PR

- Migration of `MODULES.md` and any Lot 2+ file (handled in dedicated PRs).
- `GLOSSARY.md` comparison: OS snapshot does not contain `docs/governance/GLOSSARY.md`; the playbook special rule applies and `GLOSSARY.md` will be marked `no-op` in its own dedicated PR.
- Migration of any OS file not bound to a Pantheon-Next stub (awaiting arbitration; listed in `ai_logs/migration-mapping.md`).
- Reconciliation of `STATUS.md`, `docs/governance/README.md` and `CHANGELOG.md` (handled by ChatGPT after merge).
- Phase D schema work; Phase E operations tooling; Phase F tests.

## STATUS update reminder

After merge, the doctrine owner (ChatGPT) updates `docs/governance/STATUS.md`:

- move `docs/governance/ARCHITECTURE.md` from `Stub present — non implemented` to `Migrated from Pantheon-OS`;
- if no `Migrated from Pantheon-OS` section exists yet, create one.

## Anti-runtime reminder

This PR migrates a governance document.

It does not introduce an execution runtime, a scheduler, a queue, a message bus, a provider router, an installer, an endpoint, a Docker stack, a schema, a test or operations tooling.

OpenWebUI exposes.

Hermes Agent executes.

Pantheon Next governs.

## Next required action

After merge, open the second Phase C migration PR for `docs/governance/MODULES.md` using this PR as gabarit.
