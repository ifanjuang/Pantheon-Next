# Evidence Topology ACB Reconciliation

Date: 2026-05-30

## Summary

Applied the requested A/C/B sequence after the Evidence Topology Gate examples:

- A: lightweight documentary reconciliation;
- C: non-executable schema candidate note;
- B: doctrine bridge note.

The work was done through dedicated files to avoid risky bulk replacements of `README.md`, `docs/governance/STATUS.md`, `CHANGELOG.md` or `docs/governance/README.md` while the repository was moving in parallel.

## Files added

- `docs/governance/EVIDENCE_TOPOLOGY_RECONCILIATION.md`
- `docs/governance/EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md`
- `docs/governance/EVIDENCE_TOPOLOGY_BRIDGES.md`
- `ai_logs/2026-05-30-evidence-topology-acb-reconciliation.md`

## A — Reconciliation note

`EVIDENCE_TOPOLOGY_RECONCILIATION.md` records how the Evidence Topology material should later be indexed in:

- root `README.md`;
- `docs/governance/README.md`;
- `docs/governance/STATUS.md`;
- `CHANGELOG.md`.

It avoids bulk edits and preserves a safe reconciliation target.

## C — Schema candidate note

`EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md` proposes possible future fields such as:

- `reasoning_topology`;
- `Evidence Item` shape;
- `Handoff Artifact` shape;
- Evidence Pack topology record.

It explicitly states that these are not schemas and do not modify `schemas/`.

Any future schema work remains protected and requires separate confirmation.

## B — Doctrine bridges

`EVIDENCE_TOPOLOGY_BRIDGES.md` connects the doctrine to:

- Task Contracts;
- Evidence Packs;
- Hermes Integration;
- OpenWebUI Integration;
- Memory;
- Scope Isolation;
- External Tools Policy;
- Governance College;
- User Decision Gate;
- fictional examples.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Explicitly not implemented

This intervention does not implement:

- runtime behavior;
- schema changes;
- tests;
- operations tooling;
- platform files;
- Docker changes;
- OpenWebUI plugin, Function, Tool, Pipe, Filter, Action or Pipeline;
- Hermes configuration;
- LangGraph runtime;
- swarm controller;
- scheduler;
- queue;
- message bus;
- automatic approval;
- automatic memory promotion.

## Risk note

The repository had parallel movement around PRs and unrelated documentation commits.

To avoid collateral edits, this pass used additive reconciliation files rather than replacing large index documents.

## Next suggested step

After the repository settles, perform a small focused index pass to add links from:

- `docs/governance/README.md`;
- `docs/governance/STATUS.md`;
- `CHANGELOG.md`;
- root `README.md` if public-facing explanation is desired.
