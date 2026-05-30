# Evidence Topology Public README Index

Date: 2026-05-30

## Summary

Indexed the Evidence Topology Gate material in the public `README.md`.

This was done as the first safe part of the requested indexation pass.

## Changed

Updated `README.md` to include:

- Evidence Topology as a public-facing benefit;
- `evidence topology check` in the dossier flow;
- a plain-language explanation of Evidence Topology under the technical details section;
- `Evidence Topology Gate` in the vocabulary table;
- `EVIDENCE_TOPOLOGY_GATE.md` and `EVIDENCE_TOPOLOGY_CHECKLIST.md` in key entry points;
- Evidence Topology doctrine and checklist in the documented project status.

## Why

The Evidence Topology doctrine had already been documented through:

- `docs/governance/EVIDENCE_TOPOLOGY_GATE.md`;
- `docs/governance/EVIDENCE_TOPOLOGY_ROADMAP.md`;
- `docs/governance/EVIDENCE_TOPOLOGY_CHECKLIST.md`;
- `docs/governance/evidence_topology_antipatterns/`;
- `docs/examples/evidence_topology/`;
- `docs/examples/architecture_devis_reprise/EVIDENCE_TOPOLOGY_EXAMPLE.md`.

The public README now exposes the concept without claiming implementation.

## Boundary

This intervention did not modify:

- schemas;
- tests;
- operations tooling;
- platform files;
- Docker files;
- environment files;
- Hermes configuration;
- OpenWebUI configuration.

It does not implement runtime behavior, automatic topology dispatch, swarm control, worker scheduling, automatic approval or automatic memory promotion.

## Remaining index work

Still recommended in a later focused pass:

- `docs/governance/STATUS.md` indexing;
- `docs/governance/README.md` indexing;
- `CHANGELOG.md` entry;
- possible `README.fr.md` mirror.

Those were intentionally not replaced in this pass because the files are larger and the repository has had parallel movement.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```
