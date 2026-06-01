# AI Log — Autonomy and restraint in EXECUTION_MINIMALISM

Date: 2026-06-01

## Scope

Extended `docs/governance/EXECUTION_MINIMALISM.md` with an "Autonomy and restraint"
section. It loosens how much the doctrine dictates: govern the result and the cliffs,
not every step; default to autonomy; reserve control for consequence.

## Why

After several iterations the workflow doctrine had drifted toward dictating the path
(every field cited, every loop spelled out, everything candidate and gated). The user
asked to simplify and give the AI more freedom — more permissive autonomy — without
losing safety on consequential acts.

This is more faithful to existing doctrine, not less: it applies the placement test and
"use less than the tool makes possible" to autonomy itself.

## What the section adds

- Default autonomy, gate by consequence; reversibility decides the timing of control:
  reversible/low/semi-consequential -> act-then-notify, corrected via the Review Queue;
  irreversible/hard-cliff -> ask-before or never automatic.
- Govern outcomes, not procedures: contracts state the WHAT; step-by-step procedures in
  other docs are adaptable defaults, not mandates. This licenses other documents to stay
  light and reduces sprawl.
- Autonomy is earned via the lifecycle ladder.
- Reusable outputs: an autonomous capability returns a governed, scoped record reused by
  other requests (a retrieval done once serves many), answering the user's point that
  retrieving information must be reusable across request types.
- Artifacts scale with stakes: trivial tasks are just done; the full contract/evidence/
  gate is reserved for consequential work.

## Hard cliffs that stay strict

False truth stated as fact, unapproved external effect, sending/filing/signing,
canonical memory promotion, scope leakage, definitive legal/contractual claims.

## Governance boundary

Documentation only. No runtime, scheduler, queue, automatic approval or automatic
memory promotion is introduced. The section governs posture; it does not implement
behavior.

## Files changed

- `docs/governance/EXECUTION_MINIMALISM.md`;
- `CHANGELOG.md`;
- `ai_logs/2026-06-01-autonomy-and-restraint.md`.

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
Govern the destination and the cliffs, not every step of the path.
Reversible and logged: act, then review. Irreversible or external: review, then act.
```
