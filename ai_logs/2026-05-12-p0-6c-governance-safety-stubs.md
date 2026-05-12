# P0.6C Governance Safety Stubs

Date: 2026-05-12

## Objective

Add the remaining governance safety stubs referenced by `docs/governance/STATUS.md` so the repository preserves canonical filenames before controlled migration from Pantheon-OS.

## Files created

- `docs/governance/TASK_CONTRACT_REVISIONS.md`
- `docs/governance/RUN_GRAPH.md`
- `docs/governance/EXECUTION_DISCIPLINE.md`
- `docs/governance/MODEL_ROUTING_POLICY.md`
- `docs/governance/ROUTING_FOUNDATION.md`

## Why these are stubs

Every file is a migration placeholder.

A stub:

- preserves the canonical filename;
- prevents broken references during bootstrap;
- is explicitly marked as non implemented;
- must be replaced by migrated Pantheon-OS doctrine under controlled review before it becomes canonical.

Each file carries the required header:

```text
Status: stub — Non implémenté — à migrer depuis Pantheon-OS
```

## These stubs are not migrated doctrine

The new files do not represent final Pantheon Next doctrine.

They define intended migration scope only.

Readers must check `docs/governance/STATUS.md` before treating any governance document as canonical implementation.

## Anti-runtime reminder

This pass introduces no runtime component.

It does not add:

- execution engine;
- autonomous agent loop;
- provider router;
- model gateway;
- scheduler;
- queue;
- message bus;
- workflow engine;
- LangGraph runtime;
- observability backend;
- Hermes installer;
- skill installer;
- auto-promoted memory.

## Out of scope

- migration of real Pantheon-OS content;
- changes to Hermes profiles;
- changes to `STATUS.md`, `ROADMAP.md`, `CHANGELOG.md`, root `README.md` or `docs/governance/README.md`;
- changes to `schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env` or `pyproject.toml`.

## Follow-up required after merge

After this PR is reviewed and merged, update `docs/governance/STATUS.md` and `docs/governance/README.md` so these five files move from `Absent` to `Stub present — non implemented`.
