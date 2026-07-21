# Changelog

## 0.1.63 - 2026-07-21

Repository-efficiency consolidation checkpoint. This heading records the
repository and MCP-package state after PRs #424 through #428. It is not a
published release: no `v0.1.63` tag is claimed.

### Added

- `pantheon-verify <family> <evidence>` as one static read-only CLI for install,
  observability, backup, exposure and update verification; the five historical
  command names remain compatible.
- Fail-closed duplicate-identifier detection for the Architecture Project
  Understanding dossier checker, with direct positive and negative tests.
- A current predecessor-independence guard that rejects active Pantheon-OS
  remotes, checkout paths, environment variables and vendored snapshots.
- A reusable runtime-boundary language guard extracted from GitHub Actions YAML.

### Changed

- The governance read path and roadmap now prioritize current status, ownership,
  blockers and exit criteria instead of repeating document inventories.
- `base_metier/architecte/` is explicitly qualified as an external professional
  corpus and adapter proving area, not an internal Pantheon RAG or runtime.
- Active governance documents use `Register Candidate` and `Registre Probatoire
  entry` where the governed record is meant, while Hermès retains runtime-memory
  ownership.
- AI intervention logs are limited to one durable trace per coherent material PR;
  mechanical corrections do not require an autonomous log.
- Governance CI no longer maintains completed-migration bookkeeping. It checks
  the present invariant that Pantheon Next is independent from its predecessor.
- `VERSION`, this changelog head and MCP package metadata advance together to
  `0.1.63`; the repository root remains deliberately non-distributable.

### Fixed

- Duplicate APU identifiers can no longer overwrite an earlier declaration
  silently in the dossier-wide reference index.
- Update evidence now uses the same schema-backed fail-closed validation path as
  install, observability, backup and exposure evidence.
- The large inline runtime-language program and two migration-era assertions were
  removed from the active workflow without removing current governance, APU, MCP,
  root-test or packaging checks.

### Validation posture

Each consolidation PR was refreshed onto the successive `main` state and passed
Governance CI plus Obsolete Authority Consistency before squash merge. The final
CI rewrite validated itself, including root tests, APU referential integrity,
MCP unit/end-to-end tests, wheel construction and clean-install metadata checks.

### Boundary clarification

No live runtime inventory, network probe, installer, scheduler, queue, provider
router, plugin manager, external action, update execution, automatic approval or
automatic register admission is introduced.

```text
installed != approved
healthy != safe
update_available != update_authorized
runtime_success != evidence
binding_selected != dependency_adopted
checkpoint recorded != tag published
```

### Earlier entries

- Versions `0.1.42` through `0.1.62` remain preserved in the immutable parent
  snapshot [`cc927ec:CHANGELOG.md`](https://github.com/ifanjuang/Pantheon-Next/blob/cc927ec93191e1fbbec148c1971714e89ba27488/CHANGELOG.md).
- Versions `0.1.12` through `0.1.41` remain in `CHANGELOG_ARCHIVE.md`.
