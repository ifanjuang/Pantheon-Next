# Glossary

Status: implemented — phase 1 terminology baseline.

This glossary clarifies Pantheon Next vocabulary. It also records the one governed rename in progress: "memory" is reserved to Hermès, and Pantheon governs the `Registre Probatoire` in place of "Canonical Memory" (see `REGISTRE_PROBATOIRE_DIRECTION.md`). This file is the owner of the three certainty and decision axes.

## Core doctrine

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Terms

### Pantheon Role

A canonical governance role defined in `docs/governance/AGENTS.md`.

A Pantheon Role may define authority, scope, escalation rules, approval boundaries and evidence requirements.

A Pantheon Role is not an executable runtime agent.

### Hermes Profile

A runtime-facing execution profile template under `hermes/profiles/<profile>/`.

A Hermes Profile may execute under Task Contract and produce candidates.

A Hermes Profile must not govern, approve, canonize, promote memory or merge code.

### Pantheon Skill

A governed capability contract defined by Pantheon policy.

A Pantheon Skill describes what may be done, under which constraints, with which evidence and approval requirements.

### Hermes Skill

An executable capability available to Hermes Agent.

A Hermes Skill executes only when allowed by Task Contract and governance policy.

### Task Contract

The execution contract that defines scope, inputs, limits, allowed capabilities, approval ceilings, evidence requirements and expected outputs.

### Evidence Pack

The structured proof bundle attached to a candidate output or operation.

It records sources, assumptions, commands, outputs, risks, rollback notes and validation state.

### Role Signal

A governed signal emitted by a role or profile to request review, escalate risk, report a capability gap or produce a candidate.

### Registre Probatoire

The governed evidence register: the rigorous, citeable record of evidence with certainty levels, exhibits (pièces), dates and citations. It replaces the former term "Canonical Memory".

It is the only basis Pantheon allows for a consequential decision. An entry is not binding until approved through the required path. Detailed in `REGISTRE_PROBATOIRE_DIRECTION.md` and `EVIDENCE_MEMORY_CANONICALIZATION.md`.

### Hermès memory

The execution runtime's own memory (mem0 or another system). It is free, self-evolving and ungoverned by Pantheon.

Hermès memory may propose and recall; it carries no authority. It is not a Registre Probatoire entry and may not be cited for a consequential decision.

### Register Candidate (formerly Memory Candidate)

A proposed entry for the Registre Probatoire: a sourced claim awaiting review.

It is not a Registre Probatoire entry until approved under Pantheon policy. "Memory Candidate" is the former name, retained where not yet migrated; the concept now feeds the register, not a Pantheon-owned memory.

### Candidate

A proposed output produced by Hermes or another execution surface.

A candidate is not canonical and not validated by default.

### Canonical

A validated source of truth governed by Pantheon policy.

Canonical status requires the appropriate approval path.

## Certainty and decision axes

These three axes answer three different questions. They are distinct and must not be conflated or merged into one scale. This file owns their names; the detailed levels are owned where noted.

### E0–E4 — probative certainty

"How trustworthy is this piece of evidence?" Owned here; carried by the Registre Probatoire.

```text
E0  no usable source — unsupported or rejected
E1  weak — a single unconfirmed or low-trust source
E2  plausible — sourced but not corroborated, or not fresh
E3  strong — corroborated, dated and attributed
E4  established — corroborated, fresh, attributed, and human-confirmed where consequential
```

A certainty level is not an approval and not an answer-verification level.

### V0–V4 — answer verification

"Is this answer verified?" The axis name is owned here; the detailed levels are owned by the Answer Verification Gate (candidate, see `ANSWER_VERIFICATION_GATE.md` when promoted) and reconciled against this glossary. The answer-verification axis must use `V`, never `C`, so it does not collide with the approval ceiling.

### C0–C5 — approval ceiling

"What clearance is required to act?" Owned by `APPROVALS.md`; used by the MCP capability passport. Not redefined here.

## Critical distinctions

Hermes done does not mean Pantheon validated.

Candidate does not mean canonical.

OpenWebUI Knowledge Base is not a Registre Probatoire entry.

Hermès memory (free runtime recall) is not a Registre Probatoire entry, and may not be cited for a consequential decision.

Probative certainty (E), answer verification (V) and approval ceiling (C) are three distinct axes.

A Hermes Profile does not replace a Pantheon Role.

## Canonical spelling

Use:

- `HEPHAISTOS`
- `hephaistos-agent`
- `hermes/profiles/hephaistos/`

Do not use as canonical spelling:

- `HEPHAESTUS`
- `hephaestus-agent`
- `hermes/profiles/hephaestus/`
