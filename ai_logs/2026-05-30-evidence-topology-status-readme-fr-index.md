# Evidence Topology Status and Bilingual README Indexing

Date: 2026-05-30

## Summary

Indexed Evidence Topology Gate doctrine in:

- `README.md`;
- `README.fr.md`;
- `docs/governance/STATUS.md`.

This follows the earlier Evidence Topology doctrine, checklist, anti-pattern and examples work.

## Changed

### `README.md`

Added public-facing references to:

- the right work shape before execution;
- `evidence topology check` in the dossier flow;
- Evidence Topology as the decision between one context, fan-out extraction, role-team handoff or bounded swarm;
- `Evidence Topology Gate` in the vocabulary table;
- `EVIDENCE_TOPOLOGY_GATE.md` and `EVIDENCE_TOPOLOGY_CHECKLIST.md` in key entry points.

### `README.fr.md`

Mirrored the public-facing Evidence Topology explanation in French:

- `vérification de topologie de preuve` in the dossier flow;
- `Topologie de preuve` section;
- `Porte de topologie de preuve` in the vocabulary table;
- key entry points to `EVIDENCE_TOPOLOGY_GATE.md` and `EVIDENCE_TOPOLOGY_CHECKLIST.md`.

### `docs/governance/STATUS.md`

Recorded Evidence Topology as active governance doctrine and indexed:

- `docs/governance/EVIDENCE_TOPOLOGY_GATE.md`;
- `docs/governance/EVIDENCE_TOPOLOGY_ROADMAP.md`;
- `docs/governance/EVIDENCE_TOPOLOGY_RECONCILIATION.md`;
- `docs/governance/EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md`;
- `docs/governance/EVIDENCE_TOPOLOGY_BRIDGES.md`;
- `docs/governance/EVIDENCE_TOPOLOGY_CHECKLIST.md`;
- `docs/governance/evidence_topology_antipatterns/README.md`.

Added a status section explaining that Evidence Topology doctrine does not implement topology routing, scheduling, queues, worker dispatch, graph runtime, swarm control, OpenWebUI plugin behavior, Hermes configuration, automatic approval or automatic memory promotion.

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
- topology dispatcher;
- swarm controller;
- automatic approval;
- automatic memory promotion.

## Remaining indexing work

Still recommended in a later focused pass:

- `docs/governance/README.md` read order and document list update;
- `CHANGELOG.md` entry.

Those two files were intentionally left untouched in this pass to avoid broad replacement risk while repository state is moving.

## Files touched

- `README.md`
- `README.fr.md`
- `docs/governance/STATUS.md`
- `ai_logs/2026-05-30-evidence-topology-public-readme-index.md`
- `ai_logs/2026-05-30-evidence-topology-status-readme-fr-index.md`
