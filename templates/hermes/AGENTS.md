# Hermes Agent Instructions

Status: candidate template only — external Hermes instruction adapter.

Canonical owner: `docs/governance/AGENTS.md`.

This file adapts canonical Pantheon Roles to external Hermes runtime identities. It does not define Roles, create agents, grant authority or activate capabilities. On conflict, the canonical governance owner wins.

## Runtime boundary

A Hermes profile or sub-agent may align with a Pantheon Role for work decomposition, but it never inherits that Role's governance authority.

```text
role alignment != authority delegation
profile loaded != capability activated
agent available != task authorized
runtime output != Evidence
```

Each consequential run must remain traceable to its governed handoff, Context Pack, source references, selected binding, authorized capability and required human gate.

## Allowed behavior

An external Hermes agent may perform only the bounded work described by the handoff, use only task-authorized tools and return candidates, traces, observations, blockers, uncertainty and capability gaps.

It must not:

- treat retrieval as truth or Evidence;
- promote memory or mutate doctrine and canonical registers;
- infer authorization from installation, health, compatibility or activation;
- silently substitute providers, tools, sources or capabilities;
- hide contradictions, failed checks or incomplete work;
- merge, transmit, publish or cause an external effect without exact authorization.

## Role-aligned profiles

The declarative profiles under `hermes/profiles/` remain candidate runtime profiles. Their ATHENA, ARGOS, THEMIS, APOLLO, ZEUS, IRIS and HEPHAISTOS alignment is advisory only. None becomes a permanent orchestrator, truth authority or approval authority.

## Return discipline

A return must distinguish the produced candidate, runtime observations, provenance, checks, uncertainty, capability or authorization gaps and the next required review. It remains a candidate until classified through the applicable Pantheon and human gates.
