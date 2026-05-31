# AI Log — Modular domain reorientation

Date: 2026-05-31

## Scope

Captured a reorientation as a single coordination artifact so that parallel work, including ChatGPT-assisted development, stays aligned on one model.

The reorientation consolidates decisions reached during review of recent changes:

1. Pantheon Next is a method and governance framework; the deliverable is the rules, not a product runtime.
2. The framework body stays tool-agnostic; product names live only in a bindings registry.
3. The non-negotiable prohibitions constrain the Pantheon repository, not the whole system.
4. New capability is added by manifest declaration plus a shared envelope, not by hardcoding.
5. A profession's methodology is defined once in Pantheon and projected into OpenWebUI display templates and Hermes skills.

## Files changed

Added:

- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`;
- `ai_logs/2026-05-31-modular-domain-reorientation.md`.

Updated:

- `CHANGELOG.md`.

## Why the change was made

Review surfaced a tension between using the strengths of OpenWebUI and Hermes and not over-coupling the framework to specific tools.

The reorientation resolves it: build freely in the tool layers, route only consequential decisions through Pantheon, and keep the methodology tool-agnostic with explicit projections.

It also records the complete module manifest shape and the domain-pack projection table so that parallel development does not reinvent divergent versions.

## Governance boundary

The document is a specification and coordination artifact.

It does not implement a runtime, a bridge, a plugin manager, a skill installer, a module registry runtime, a domain-pack worker, an OpenWebUI Function, a Hermes skill, an executable schema, automatic approval or automatic memory promotion.

The complete manifest is recorded as a shape only. A canonical executable schema under `schemas/` requires explicit approval before being added.

## Key doctrine preserved

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Abstract form, with tools named only in the bindings registry:

```text
The exposure surface exposes.
The execution runtime executes.
Pantheon governs.
```

## Risks and limitations

- Duplication risk if a domain pack's rules are restated inside tool templates instead of referenced; mitigated by the single-source discipline.
- Premature generalization risk across professions; mitigated by building the architecture pack first and proving it before generalizing.
- Fabricated methodology risk for liability-bearing professions; mitigated by the rule that domain content comes from the professional, structured by the framework, never invented.

## Explicit non-implementation

No files were touched under:

```text
schemas/
tests/
operations/
platform/
Docker
.env
pyproject.toml
CLAUDE.md
```

## Boundary phrase

```text
Pantheon defines the contract.
The tools carry the work.
The validated remains.
```
