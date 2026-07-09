# Pantheon MPV

Status: external executable candidate — not adopted by Pantheon Next.

This repository is intended to host the executable MVP vertical slice for a governed Pantheon task loop.

It is external to Pantheon Next.

It may execute deterministic proof-loop code, tests and local fixtures.

It must not govern, approve, validate professional truth, promote memory, send external messages, schedule work, route providers or become Pantheon Next.

```text
Pantheon Next governs.
Hermes-side execution occupies the runtime seat.
OpenWebUI or another cockpit exposes the review surface.
The human decides.
```

## Current repository status

```text
repo: ifanjuang/pantheon-mpv
status: initialized / awaiting external MVP vertical code
adoption: not adopted
activation: not activated
production use: forbidden
```

The code that lands here must remain classified as an external executable candidate until reviewed against Pantheon Next governance.

## Expected vertical-slice shape

The candidate MVP vertical may include:

```text
bounded Task Contract loading
bounded source ingestion
scoped retrieval
result candidate production
evidence-pack candidate production
forbidden-operation refusal
human decision gate stand-in
signed decision trace
acceptance tests
```

## Required boundaries

The repository must preserve these distinctions:

```text
external_repo != Pantheon runtime
stand_in_runner != Hermes Agent
terminal_gate != OpenWebUI cockpit
runtime_success != evidence
result_candidate != approved_result
evidence_pack_candidate != validated_evidence
draft != external_send_authorization
test_pass != adoption
```

## Before adoption

Before Pantheon Next may classify this binding as adoptable, this repository must provide:

```text
schema-aligned Task Contract fixture
source path boundary checks
explicit stand-in naming or headers
human-gate decision semantics
CI-visible test run
GOVERNANCE_STATUS.md
human approval for adoption
```
