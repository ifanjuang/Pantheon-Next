# AI Log Format

Status: active support note — AI log format — documented non-implemented.
Boundary profile: validation_only_trace.

This file defines a compact format for future AI-assisted repository operation logs.

It does not create doctrine, runtime behavior, schema, test, CI workflow, approval engine, memory promotion, scheduler, queue, provider router or external action authorization.

## Purpose

AI logs should preserve traceability without repeating the same boundary and non-equivalence boilerplate in every file.

Use this format for future logs unless a specific intervention needs a longer narrative.

## Compact format

```md
# <short title>

Date: YYYY-MM-DD

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added:
- Updated:
- Removed:

## Why

Short explanation of the problem or repetition being addressed.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: yes/no.
Runtime impact: none / describe.
Authority impact: none / describe.
Schema/test/CI impact: none / describe.
External action: none / describe.
Memory behavior: none / describe.

## Local distinctions

Repeat only locally material distinctions, for example:

```text
trace != doctrine
schema_valid != approved
runtime_success != evidence
```
```

## Required fields

Every future AI log should include:

```text
Date
Status
Boundary profile
Change
Why
Boundary
Local distinctions
```

## Use of boundary profiles

For ordinary logs, use:

```text
Boundary profile: validation_only_trace.
```

Do not repeat the full non-runtime disclaimer unless the log itself concerns runtime, installation, external action, memory or approval behavior.

## Use of non-equivalence rules

Use `docs/governance/NON_EQUIVALENCE_RULES.md` as the canonical reference.

Repeat only the distinctions that matter locally.

## Longer logs

Longer logs remain acceptable when they record:

```text
migration sequence
schema or protected-path review
merge conflict resolution
failed approach
branch replacement
human decision
```

Even then, prefer the compact boundary block instead of repeating every forbidden capability.

## Forbidden claims

An AI log must not claim:

```text
implementation unless code or artifact exists
approval unless a human decision exists
memory admission unless a register admission exists
runtime health unless a runtime check exists
external action authorization unless explicitly granted
```
