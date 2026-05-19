# Evidence Topology Gate Doctrine

Date: 2026-05-19

## Summary

Added `docs/governance/EVIDENCE_TOPOLOGY_GATE.md` as active governance doctrine for reasoning topology, evidence preservation and Hermes swarm constraints.

The doctrine was added after review of single-agent versus multi-agent failure modes, external multi-agent frameworks and Hermes Workspace swarm patterns.

## Changed

Created a new governance document defining:

- the proof chain as the unit of reasoning;
- single primary reasoning context as the default when decisive evidence must be connected across sources;
- fan-out extraction followed by single synthesis;
- parallel independent workers only for genuinely independent tasks;
- routers for classification, not truth decisions;
- sequential handoffs only when each handoff carries traceable evidence;
- bounded Hermes swarm as distributed execution capacity, not decision authority;
- a forbidden topology for summary-only specialist-agent handoffs followed by supervisor synthesis;
- Evidence Item expectations for worker outputs;
- future Task Contract topology expectations without changing schemas;
- relationship to Hermes, Governance College, Evidence Packs, OpenWebUI, memory and external inspirations.

## Core rule

```text
The unit of reasoning is not the agent.
The unit of reasoning is the proof chain.
```

## Hermes swarm constraint

```text
Hermes Swarm may multiply execution capacity, not decision authority.
```

Hermes may swarm for evidence collection, bounded source inspection, independent checks, Patch Candidates, Evidence Items and review notes.

Hermes swarm must not approve, canonize memory, expand scope silently, replace Pantheon Roles, produce final authority, hide worker traces, rely on summary-only handoffs or bypass User Decision Gates.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

The new document does not implement runtime behavior.

It does not add schemas.

It does not modify tests, operations, platform files, Docker, protected areas or environment configuration.

## Follow-up needed

- Link `EVIDENCE_TOPOLOGY_GATE.md` from `docs/governance/README.md` and `STATUS.md` when the connector permits safe focused updates.
- Add a roadmap entry when a non-volumetric patch is available.
- Later, consider example-only Task Contract and Evidence Pack samples before any schema change.

## Tool limitation

A full `ROADMAP.md` replacement update was attempted but blocked by the connector safety layer.

No roadmap file change was applied in that blocked attempt.

## Files touched

- `docs/governance/EVIDENCE_TOPOLOGY_GATE.md`
- `ai_logs/2026-05-19-evidence-topology-gate.md`
