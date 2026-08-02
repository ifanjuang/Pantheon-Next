# CLAUDE.md runtime-policy human-decision line — governance record

Date: 2026-08-02

Status: applied doc alignment — non-authoritative over the governance corpus, non-runtime.

## Purpose

Align the `CLAUDE.md` Runtime policy actor list with the reader-facing README
system-boundary surface reconciled in PR #504, which restored the human
decision as an explicit final actor.

## Change

Add one line to the Runtime policy actor list in `CLAUDE.md`:

```text
The human decides what is consequential.
```

placed after `Pantheon Next is the governance source of truth.`

## What this is not

- It does not abstract or remove the named-actor triptych
  (OpenWebUI exposes / Hermes executes / Pantheon governs); that separation
  remains the load-bearing boundary and is unchanged.
- It does not change any invariant, schema, gate, route, runtime behavior or
  authority class.
- It does not promote the README to authority; `CLAUDE.md` and the governance
  corpus remain authoritative over reader-facing surfaces.

## Boundary

```text
doc alignment != doctrine change
human decision restated != new gate
README surface != authority source
```
