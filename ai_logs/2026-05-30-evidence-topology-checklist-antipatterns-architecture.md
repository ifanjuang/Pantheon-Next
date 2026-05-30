# Evidence Topology Checklist, Anti-patterns and Architecture Example

Date: 2026-05-30

## Summary

Added practical support material for the Evidence Topology Gate doctrine:

- a decision checklist;
- anti-pattern cards;
- a fictional architecture / maîtrise d’œuvre example.

The goal is to make the doctrine usable before any schema or runtime work.

## Files added

- `docs/governance/EVIDENCE_TOPOLOGY_CHECKLIST.md`
- `docs/governance/evidence_topology_antipatterns/README.md`
- `docs/governance/evidence_topology_antipatterns/ANTI_PATTERN_SUMMARY_ONLY_HANDOFF.md`
- `docs/governance/evidence_topology_antipatterns/ANTI_PATTERN_SWARM_AS_AUTHORITY.md`
- `docs/governance/evidence_topology_antipatterns/ANTI_PATTERN_ROLE_MEMORY_AS_CANONICAL_MEMORY.md`
- `docs/governance/evidence_topology_antipatterns/ANTI_PATTERN_CONDUCTOR_AS_ZEUS.md`
- `docs/governance/evidence_topology_antipatterns/ANTI_PATTERN_CANVAS_AS_EVIDENCE_PACK.md`
- `docs/examples/architecture_devis_reprise/EVIDENCE_TOPOLOGY_EXAMPLE.md`
- `ai_logs/2026-05-30-evidence-topology-checklist-antipatterns-architecture.md`

## Checklist

`EVIDENCE_TOPOLOGY_CHECKLIST.md` provides a fast decision table and twelve gating questions for choosing between:

- `single_primary_reasoning_context`;
- `fanout_extract_then_single_synthesis`;
- `parallel_independent_workers`;
- `router`;
- `sequential_handoff`;
- `persistent_role_team_handoff`;
- `bounded_hermes_swarm`.

## Anti-patterns

The anti-pattern cards identify common topology drifts:

- summary-only handoff;
- swarm as authority;
- role memory as Canonical Memory;
- conductor as ZEUS;
- canvas as Evidence Pack.

## Architecture example

The architecture / MOE example applies the rule to a fictional recovery quote dossier:

```text
recovery quote
+ CCTP excerpt
+ site report
+ client emails
+ photos
+ missing reception note
```

The selected topology is:

```text
fanout_extract_then_single_synthesis
```

The example makes explicit that workers may extract Evidence Items, but must not validate a quote, conclude reception status, produce a client-facing validation or promote memory.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Explicitly not implemented

This intervention does not implement:

- runtime behavior;
- schemas;
- tests;
- operations tooling;
- platform files;
- Docker changes;
- OpenWebUI plugin, Function, Tool, Pipe, Filter, Action or Pipeline;
- Hermes configuration;
- swarm runtime;
- automatic approval;
- automatic memory promotion.

## Tool note

The connector initially blocked a longer anti-pattern card. The card was reduced to a compact version and committed successfully.
