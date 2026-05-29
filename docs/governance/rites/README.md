# Rites

Status: active doctrine - shared governance procedures.

Rites are bounded governance procedures used to coordinate Pantheon Roles around a recurring methodological tension.

They are not agents.

They are not Pantheon Roles.

They are not Hermes profiles.

They are not a runtime.

They are not a scheduler, queue, message bus, workflow engine, provider router, plugin manager, skill installer, MCP layer, observability backend or hidden debate system.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Core distinction

Pantheon Roles carry stable responsibilities of judgment.

Rites organize temporary procedures shared by several roles.

Task Contracts bound what may be done.

Evidence Packs make the result reviewable.

ZEUS arbitrates status and next procedure.

The human decides when procedural arbitration is insufficient.

```text
Roles judge.
Rites coordinate.
Task Contracts bound.
Evidence Packs prove.
ZEUS states procedure.
The human decides.
```

## Why rites exist

Some governance moves recur across multiple roles:

- divergent exploration before convergence;
- autocritique after a convincing draft;
- source concordance before delivery;
- premise extraction before planning;
- session refoundation when context is polluted.

Keeping these moves inside one role would create oversized roles and duplicated doctrine.

A rite makes the method explicit, reusable and reviewable without creating a new autonomous actor.

## Relationship to the Governance College

The Governance College separates responsibilities of judgment.

A rite may temporarily call several roles from the college, but it does not make them agents and does not create a runtime conversation.

A role keeps its responsibility.

A rite defines the order, trigger, outputs, anti-triggers and evidence expectations.

## Relationship to Agora

Agora is a visible deliberation space.

A rite is a bounded procedure.

Agora may receive the output of a rite, request a rite, or expose unresolved discord after a rite.

A rite must not replace Agora when human legitimacy, values, professional preference or explicit user arbitration are required.

Useful distinction:

```text
Agora deliberates.
Rites structure method.
ZEUS arbitrates status.
The human decides.
```

## Initial rite catalogue

- `RITE_DIVERGENCE_CONTROLEE.md` - widen options before convergence while separating generation from critique.
- `AUTOCRITIQUE_CONTRADICTOIRE.md` - review a draft or candidate as if it came from a third party.
- `CONCORDANCE_DES_SOURCES.md` - compare source support, freshness and contradictions before relying on a claim.
- `PREMISSES_CACHEES.md` - expose hidden assumptions before planning or deciding.
- `REFONDATION_DE_SESSION.md` - reset a polluted session into a new bounded Task Contract.

## External inspiration boundary

The first version of `RITE_DIVERGENCE_CONTROLEE.md` is inspired by the external divergent-ideation pattern from `uditakhourii/adhd`.

Pantheon distills the method only.

Pantheon does not import the package.

Pantheon does not adopt its name as public doctrine.

Pantheon does not install a skill, runtime, provider integration, scheduler or agent loop.

## Rite lifecycle

A rite may be:

```text
proposed
active
under_review
deprecated
rejected
superseded
```

A rite can become active doctrine only when it preserves the core boundary:

```text
method without runtime
coordination without agent multiplication
review without auto-approval
evidence without hidden chain-of-thought
memory candidate without automatic promotion
```

## Minimal rite structure

Each rite should define:

```text
id
status
purpose
triggers
anti-triggers
roles called
inputs
procedure
outputs
Evidence Pack impact
User Decision Gate impact
memory impact
failure modes
forbidden drift
```

## Forbidden drift

Rites must never become:

- autonomous workflows;
- hidden role debates;
- agent loops;
- tool dispatch plans;
- schedulers;
- queues;
- executable DAGs;
- LangGraph runtime substitutes;
- approval callbacks;
- memory promotion pipelines;
- OpenWebUI plugins;
- Hermes skill auto-installers.

If a rite becomes executable by Pantheon itself, governance drift has occurred.

## Final rule

A rite is a governed method.

It can organize roles.

It cannot execute work.

It cannot approve itself.

It cannot make memory canonical.
