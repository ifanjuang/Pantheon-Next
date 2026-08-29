# Evidence Topology anti-pattern owner test

Date: 2026-08-29
Issue: #787
Base `main`: `870518c034d83f216ba224650a2d562649ad3209`
Branch: `codex/787-evidence-topology-owner`

## Objective

Continue the #787 current-authority baseline convergence without mechanically indexing every active-status Markdown file.

The post-#829/#825 diagnostic identified 38 current-authority documents outside the effective Authority Index. Six of those paths are the `docs/governance/evidence_topology_antipatterns/` collection.

## Owner test

`EVIDENCE_TOPOLOGY.md` was re-read on exact base `870518c034d83f216ba224650a2d562649ad3209`, together with the anti-pattern collection README and all five cards.

The parent doctrine already owns the relevant rules and explicitly names the same red flags:

```text
summary-only handoff for decision-critical work
swarm as judgment / authority
role memory as governed memory
conductor/router as Zeus
client canvas as validation / Evidence Pack
```

The cards therefore do not retain independent normative responsibility. Their useful function is explanatory: they illustrate failure shapes and corrective questions already governed by `EVIDENCE_TOPOLOGY.md` and the existing Evidence, memory, approval, Task Contract and Hermes owners.

## Decision

Keep the examples; remove their independent current-authority status.

- `evidence_topology_antipatterns/README.md` becomes `reference` and explicitly points to `EVIDENCE_TOPOLOGY.md` as the doctrine owner.
- the five cards become `reference` documents with unchanged examples/corrections.
- no new owner, schema, test, runtime, index family or authority vocabulary is introduced.
- `EVIDENCE_TOPOLOGY.md` remains current doctrine and remains part of the remaining #787 owner-index baseline for a later Evidence-family owner test/indexing slice.

## Net effect on #787 baseline

```text
post-#825 current-authority gaps: 38
this slice reclassifies:             6
expected remaining gaps:             32
```

This is a reduction in current-authority owners, not a loss of useful documentation.

## Preserved boundaries

```text
example card != authority
activity != Evidence
runtime topology != governance authority
memory != Evidence
projection != persistence
runtime success != authorization
```

## Validation

Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final PR head and reviews/threads/comments have been inspected.
