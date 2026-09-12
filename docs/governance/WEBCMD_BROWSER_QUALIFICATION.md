# Webcmd browser qualification

Status: candidate qualification note — no selection, installation, activation or task authorization.

Tracking issue: #1051.

## Purpose

Qualify `agentrhq/webcmd` only as a replaceable Hermes-side browser-control implementation candidate when it demonstrates a concrete advantage over the currently reviewed Hermes native browser capability.

This note does not create a Pantheon browser runtime, browser-memory authority, MCP sequencing path or orchestration layer.

## Existing selection rule

```text
Hermes native capability sufficient
-> use it
-> no external binding required

capability gap demonstrated
-> compare one bounded external candidate
-> qualify it
-> select only if the demonstrated benefit justifies the added runtime surface
```

## Candidate responsibility

Webcmd combines live browser control with a local `site-memory` intended to retain useful navigation context such as observed pages, actions, workflows, endpoints and pitfalls.

For Pantheon/Hermes purposes:

```text
Webcmd site-memory
= runtime procedural/navigation memory
!= Pantheon Memory
!= Hindsight project/document memory
!= Knowledge
!= Evidence
!= source authority

Webcmd browser result
= runtime candidate/observation material
!= authorization
!= Evidence
!= professional validation
```

If selected later, Webcmd remains an external Hermes-side skill/runtime adapter. Pantheon continues to own only the existing governance boundary around scope, consequential effects, Evidence and approval.

## Adjacent capabilities

Keep the responsibilities distinct:

```text
Crawlberg / public-web evidence intake
!= interactive authenticated browser control

Hindsight / external runtime memory
!= navigation procedure memory

Hermes native browser capability
!= Webcmd adoption

Webcmd installed
!= Webcmd selected

Webcmd selected
!= Webcmd activated

Webcmd activated
!= browser action authorized
```

No Hindsight ingestion or Pantheon memory promotion is required for Webcmd `site-memory`.

## Qualification target

Compare the same bounded task corpus under the same model/profile/settings:

```text
A — Hermes native browser capability
B — Hermes + pinned Webcmd candidate
```

The qualification must record the exact Hermes and Webcmd artifacts used.

### Minimum corpus

Use synthetic/test accounts and non-sensitive data only for the first pass.

1. unfamiliar public site — read-only retrieval;
2. repeated navigation on the same site — measure second-run reuse;
3. authenticated synthetic/test account — read-only retrieval;
4. multi-step form/workflow stopping before consequential submission;
5. two concurrent isolated Sessions when practical.

### Minimum observations

Record:

- first-run success/failure;
- repeated-run success/failure;
- agent turns;
- token use where observable;
- elapsed time where observable;
- authenticated-session behavior;
- profile/session isolation;
- parallel-session isolation;
- timeout/error recovery;
- stale-navigation-memory behavior after a controlled page/state change;
- whether repeated execution materially reduces rediscovery.

A favorable upstream benchmark is not sufficient for selection.

## Privacy and runtime posture

Start from the narrowest local posture supported by the pinned Webcmd release:

```text
local execution only
Webcmd Cloud unused
global site-memory seed lookup disabled
candidate public-IP lookup disabled
isolated dedicated browser profile
explicit Sessions
no consequential browser mutation by default
no automatic external transmission
```

Re-check the exact upstream privacy/runtime behavior at qualification time rather than relying on this note as release documentation.

## Governance invariants

```text
reachable browser != authorized action
browser login != source admission
retrieved page != true
site-memory recall != current page state
site-memory recall != Evidence
successful browser run != professional validation
runtime success != authorization
runtime approval != Pantheon approval
profile cookie availability != permission to use every reachable account
```

Any consequential browser effect remains behind the existing Pantheon policy / human gate appropriate to that effect.

## Failure cases to exercise

At least one controlled failure must test each relevant class before selection:

- stale or changed page structure;
- expired or unavailable session;
- timeout or interrupted browser action;
- concurrent Session isolation;
- site-memory failure or unavailable learned context;
- exact outcome unknown after interruption when applicable.

The required behavior is bounded failure or explicit uncertainty, not silent widening or blind retry.

## Decision

Close #1051 with exactly one posture:

```text
preferred_candidate
fallback_candidate
watch
rejected
```

`preferred_candidate` is justified only when Webcmd materially improves representative repeated/authenticated workflows over Hermes native browser after considering reliability, cost, privacy, operational complexity and replacement cost.

If Hermes native browser is sufficient, keep Webcmd unselected.

## Non-goals

```text
no new Pantheon browser engine
no new Role / Rite / governed Space
no browser-specific authority owner
no second memory authority
no automatic Webcmd -> Hindsight promotion
no automatic Webcmd -> Pantheon Memory promotion
no new MCP server solely for Webcmd
no duplicate public-web evidence pipeline
no production/client-account rollout in the first qualification
no selection from upstream benchmark claims alone
```

## Exit criteria

- exact candidate artifacts recorded;
- local-only privacy posture verified;
- same-task A/B comparison completed;
- first-run versus repeated-run behavior measured;
- session/profile isolation observed;
- at least one stale-memory/failure case exercised;
- consequential actions remain governed through existing effect boundaries;
- no navigation memory promoted to governed memory/Evidence;
- one explicit selection posture recorded;
- no new governance abstraction introduced unless a residual failure proves the current owners insufficient.
