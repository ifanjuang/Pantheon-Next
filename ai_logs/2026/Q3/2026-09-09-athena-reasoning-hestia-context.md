# 2026-09-09 — Athena reasoning and Hestia situated-context convergence

Date: 2026-09-09

Status: validation-only trace — documented semantic governance change.
Boundary profile: validation_only_trace.

## Change

- Updated `docs/governance/AGENTS.md` so canonical ATHENA owns reasoning structure, explicit hypotheses and bounded candidate projection of consequences, dependencies, scenarios and solution variants in addition to planning/decomposition.
- Clarified that canonical ATHENA role expansion does not itself expand the current `athena-agent` runtime profile or its output allowlist.
- Added proportional reasoning posture: intended conclusion level, phase, project complexity/interfaces, consequence magnitude, reversibility, temporal state, observation quality, source/competent-actor authority, audience/external effect and scope breadth may materially change the rigor required.
- Added baseline/alternative comparison and a stop rule: more available information is not a reason to widen context once remaining unknowns cannot materially change the permitted conclusion.
- Updated `docs/governance/CONTEXT_STACK.md` so candidate HESTIA watches situated referent grounding, bounded target scope and context sufficiency without becoming an identity resolver or new runtime owner.
- Reframed the ATHENA / Context Stack / other-role composition as a non-authoritative Context Stack example; `GOVERNANCE_COLLEGE.md` remains the owner of canonical inter-role interaction doctrine.
- Added explicit observation-state distinctions such as visible != measured, plan != installed state and opinion found != current/applicable opinion.
- Added no new Pantheon Role, Rite, governed Space, runtime agent, router, context engine, identity engine, graph, score, runtime mode, persistence owner or automatic project traversal.

## Why

Project questions are not limited to geometric modifications. A professional may refer to `cette porte` from a photo, `la salle de bain enfant` while drawings say `SDB A` / `SDB B`, ask whether a wall is acoustic, whether moving an office door remains acceptable, whether ERP/effectif/PPRI/ABF context matters, or whether a BET has already issued a more competent opinion.

The same wording can also require materially different rigor depending on whether the expected output is general orientation, a project-specific conclusion, an EXE/VISA response, a current chantier observation, a client/contractor transmission or another durable consequential effect.

The existing owners can cover these cases if their boundary is explicit:

```text
ATHENA -> what could materially change the reasoning; candidate consequences / scenarios / variants
Context Stack / HESTIA candidate -> are the situation, referent and corresponding context sufficiently established for the intended conclusion
ARGOS -> source identity / provenance / support / source authority
MNEMOSYNE -> prior naming, history, version, current-state framing and earlier opinions
THEMIS -> responsibility, competence, policy and approval boundary
ZEUS -> status/procedure arbitration only when materially unresolved
```

P2 / #986 remains a qualification of Hermes reasoning from admitted context, not a new Role or métier lens. The Pantheon-facing image may later use a clearer qualification name such as an Athena trial, but no new governed object is created by this change.

## Review convergence

Two PR review observations were accepted and resolved by simplification:

1. `AGENTS.md` no longer promises new `athena-agent` artifact outputs that are absent from the current profile contract. Canonical Role responsibility and runtime profile capability remain separate.
2. `CONTEXT_STACK.md` no longer presents an ATHENA -> HESTIA -> ARGOS/MNEMOSYNE -> ATHENA sequence as canonical interaction doctrine. It is explicitly an illustrative context composition only; `GOVERNANCE_COLLEGE.md` remains authoritative for role interaction.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no schema/runtime protected path; semantic Role owner surfaces are intentionally touched and require the Role/Rite/Space PR review context.
Runtime impact: none.
Authority impact: yes — canonical ATHENA jurisdiction is clarified/expanded within the existing Role; HESTIA remains candidate and is not canonized.
Schema/test/CI impact: no schema or runtime test logic; existing governance and Role/Rite/Space guards must pass.
External action: none.
Memory behavior: none.

## Local distinctions

```text
candidate projection != project fact
projection != persistence
possible risk != established non-compliance
bounded referent candidate set != merged identity
context sufficient != source true
visible != measured
plan != installed state
opinion found != current applicable opinion
more retrieval != more legitimacy
Role responsibility != runtime profile capability
P2 qualification != new Role
```
