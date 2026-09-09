# 2026-09-09 — Athena reasoning and Hestia situated-context convergence

Date: 2026-09-09

Status: validation-only trace — documented semantic governance change.
Boundary profile: validation_only_trace.

## Change

- Updated `docs/governance/AGENTS.md` so canonical ATHENA owns reasoning structure, explicit hypotheses and bounded candidate projection of consequences, dependencies, scenarios and solution variants in addition to planning/decomposition.
- Updated `docs/governance/CONTEXT_STACK.md` so candidate HESTIA watches situated referent grounding, bounded target scope and context sufficiency without becoming an identity resolver or new runtime owner.
- Documented the bounded ATHENA -> Context Stack / HESTIA -> ARGOS / MNEMOSYNE -> ATHENA reasoning-context loop, with THEMIS and ZEUS activated only when consequence requires them.
- Added no new Pantheon Role, runtime agent, router, context engine, identity engine, graph, persistence owner or automatic project traversal.

## Why

Project questions are not limited to geometric modifications. A professional may refer to `cette porte` from a photo, `la salle de bain enfant` while drawings say `SDB A` / `SDB B`, ask whether a wall is acoustic, whether moving an office door remains acceptable, whether ERP/effectif/PPRI/ABF context matters, or whether a BET has already issued a more competent opinion.

The existing owners can cover these cases if their boundary is explicit:

```text
ATHENA -> what could materially change the reasoning; candidate consequences / scenarios / variants
Context Stack / HESTIA candidate -> are the situation, referent and corresponding context sufficiently established
ARGOS -> source identity / provenance / support
MNEMOSYNE -> prior naming, history, version and earlier opinions
THEMIS -> responsibility, competence, policy and approval boundary
ZEUS -> status/procedure arbitration only when materially unresolved
```

P2 / #986 remains a qualification of Hermes reasoning from admitted context, not a new Role or métier lens.

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
Role responsibility != runtime agent
P2 qualification != new Role
```
