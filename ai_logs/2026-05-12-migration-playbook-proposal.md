# Migration Playbook Proposal (Phase C)

Date: 2026-05-12

## Objective

Propose a controlled playbook for Phase C — migration of governance Markdown from Pantheon-OS into the existing stubs of Pantheon-Next. No migration is started by this entry. This file is a pointer to the open proposal and the six pending decisions that need ChatGPT arbitration before Phase C may begin.

## Pointer

Full proposal and the six open decisions:

```text
https://github.com/ifanjuang/Pantheon-Next/issues/7
```

Issue title: `Migration Playbook (Phase C) — proposal and 6 open decisions`.

## Summary

The proposal covers:

- per-PR ritual (read OS source, apply doctrinal filter, diff, verify invariants, ai_log);
- doctrinal filter rules (anti-runtime, version-dependent removal, renamed-term rewriting);
- per-PR invariants (header replacement, no schema/test/operations changes, link integrity);
- eight-lot sequencing across the 22 stubs + ecosystem files;
- coordination with Phase D (schemas, already started by ChatGPT) without file overlap;
- three options for the Pantheon-OS access channel: add the repo to the Claude session, use a `migration-source/*` branch on `pantheon-next`, or paste content per batch.

## Six open decisions awaiting arbitration

`D1` — better-than-Next OS doc: always propose Next update first, or ask each time
`D2` — obsolete or contradictory OS doc: default action
`D3` — oversized OS doc: condense, split or ask
`D4` — broken link to a moved/removed file: silent fix or migration note
`D5` — OS drift during Phase C: single snapshot, re-snapshot per lot, or delta PRs at end
`D6` — diagrams and images: defer to Lot 8 or integrate as we go

## Why this is only an ai_log entry

This pass deliberately does not introduce canonical doctrine.

- No file is created or modified under `docs/governance/`.
- No schema, test, operations tooling, runtime, scheduler, queue or installer is introduced.
- No existing Hermes profile or governance document is touched.
- `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, root `README.md`, `docs/governance/README.md` are not modified.
- `pyproject.toml`, `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env*` are not modified.

Canonical doctrine `docs/governance/MIGRATION_PLAYBOOK.md` will only be created after D1–D6 are arbitrated, in a separate Claude PR.

## Anti-runtime reminder

Pantheon Next governs.

Hermes Agent executes.

OpenWebUI exposes.

The migration playbook will not introduce execution surfaces, hidden orchestration or auto-promotion mechanisms inside Pantheon Next. Each migration PR will repeat that boundary.

## Next required action

Doctrine owner reviews issue #7, ChatGPT arbitrates D1–D6 in issue comments, owner picks the Pantheon-OS access channel. Then Claude opens a second PR to materialize `docs/governance/MIGRATION_PLAYBOOK.md` with the consolidated answers, and Phase C Lot 1 (`ARCHITECTURE.md`) can start as the gabarit PR.
