# Persistent Role-Team Topology Update

Date: 2026-05-19

## Summary

Extended the Evidence Topology Gate doctrine and roadmap addendum to cover persistent role-team handoffs.

This was added after reviewing a 9-agent operational team example and the `Armandogith/langgraph-research-orchestrator` repository.

The update clarifies that multi-agent and role-team workflows can be useful when roles own distinct artifacts, surfaces or stages, but they still require governed evidence, handoff artifacts, approval gates and memory boundaries.

## Changed

Updated `docs/governance/EVIDENCE_TOPOLOGY_GATE.md` with:

- `persistent_role_team_handoff` as an allowed topology;
- examples such as `arch -> backend -> frontend -> review`, `research -> strategy -> writer -> editor -> SEO`, and `researcher -> critic -> human review -> writer`;
- allowed Handoff Artifacts such as API contracts, architectural decision notes, campaign briefs, draft articles, editorial review notes and evidence sufficiency notes;
- a Handoff Artifact example;
- a Task Contract expectation for role-team work;
- a topology matrix entry for persistent role teams;
- stronger rejection rules for role memory, team chat and visible canvas being mistaken for evidence, approval or Canonical Memory.

Updated `docs/governance/EVIDENCE_TOPOLOGY_ROADMAP.md` with:

- persistent role-team pattern distillation;
- LangGraph research orchestrator pattern distillation;
- explicit keep/reject lists;
- a revised example sequence before schema work.

## Patterns kept

From the 9-agent team example:

- explicit role ownership;
- stage-bound handoffs;
- visible conversation surface;
- persistent role context for voice, procedure or project continuity;
- reduced human copy-paste and dispatch burden.

From the LangGraph research orchestrator example:

- explicit graph edges;
- Researcher -> Critic -> Human Review -> Writer sequencing;
- critic loop before report writing;
- append-only evidence accumulation;
- human-in-the-loop interrupt before writer stage;
- structured state over informal handoff.

## Patterns rejected

- agent-to-agent chat as evidence;
- role memory as Canonical Memory;
- auto-captured Knowledge Base as doctrine;
- direct handoff as approval;
- visible canvas as governance validation;
- critic approval as final approval;
- in-memory checkpoint as Canonical Memory;
- runtime graph as Pantheon runtime.

## Doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Role-team and swarm execution remain Hermes-side or external runtime concerns.

Pantheon governs topology, evidence, approval, scope and memory status.

## Files touched

- `docs/governance/EVIDENCE_TOPOLOGY_GATE.md`
- `docs/governance/EVIDENCE_TOPOLOGY_ROADMAP.md`
- `ai_logs/2026-05-19-persistent-role-team-topology.md`
