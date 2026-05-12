# Glossary

Status: implemented — phase 1 terminology baseline.

This glossary clarifies Pantheon Next vocabulary without renaming existing concepts.

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

### Memory Candidate

A proposed memory item.

A Memory Candidate is not canonical memory until approved under Pantheon memory policy.

### Candidate

A proposed output produced by Hermes or another execution surface.

A candidate is not canonical and not validated by default.

### Canonical

A validated source of truth governed by Pantheon policy.

Canonical status requires the appropriate approval path.

## Critical distinctions

Hermes done does not mean Pantheon validated.

Candidate does not mean canonical.

OpenWebUI Knowledge Base does not mean canonical memory.

Hermes memory does not mean Pantheon canonical memory.

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
