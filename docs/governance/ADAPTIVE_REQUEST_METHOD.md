# Adaptive Request Method

Status: active support doctrine — adaptive governance method for any request — documented non-implemented.
Boundary profile: active_support_doctrine.

This document defines how Pantheon Next handles a user request proportionally, from light direct handling to governed context expansion, source need, evidence review, output gating and human decision.

It is a method, not a workflow.

Runtime/client boundary: see `HERMES_INTEGRATION.md`. This method governs proportional handling and candidate status only; execution remains external and client or runtime success transfers no Pantheon authority.

## Core thesis

Every request starts simple.

It becomes more governed only when the request, context, source dependency, evidence need, output consequence, external effect or memory effect requires it.

```text
The request opens a Situation.
MÈTIS qualifies the cap.
HESTIA qualifies expected context.
ARGOS qualifies sources.
THEMIS qualifies risk.
The College works the path.
ZEUS arbitrates status.
The human decides at consequential cliffs.
```

This method extends `REQUEST_LIFECYCLE.md` and consumes context/source owners without replacing them.

## Why this exists

A request should not be treated as a fixed workflow.

The same input can support different outputs.

The same output can require different input authority depending on audience, risk and consequence.

A missing source does not authorize guessing.

A registered source does not automatically become evidence.

A model answer does not become professional truth.

## Activation principle

Use proportional activation.

```text
simple, clear, low-consequence request -> light handling
a request with unclear cap -> MÈTIS
a request with context dependency -> context-sufficiency review
a request with source dependency -> source-need / ARGOS review
a request with liability / external effect -> THEMIS + ZEUS / human gate
a request with memory effect -> memory gates + ZEUS / human gate
a request with candidate output -> evidence and approval posture
```

The method must not impose a heavy ritual on every request.

It becomes stricter when the situation demands it.

## Request decomposition

A request is decomposed into separate candidates:

```text
Request Candidate           -> what the user asked, as received
Cap Candidate               -> what MÈTIS understands as the real aim
Expected Context Profile    -> context expected to safely proceed
Input Admission Candidate   -> what was supplied, retrieved, recalled or is absent
Source Need Candidate       -> what source is missing and why it matters
Output Intent Candidate     -> what kind of output is expected and under what status
Situated Approach Candidate -> what motifs are composed to handle this situation
Result Candidate            -> output produced by a role, runtime or adapter
Evidence Pack Candidate     -> review material supporting or contradicting assertions
Gate / Decision             -> accepted, refused, to_verify, to_arbitrate or blocked
```

These are governance objects. They do not execute.

The specific contracts and status rules of Context Stack, source need, Evidence, approval and memory remain with their own owners.

## Input is not output

Pantheon separates input profile from output intent.

```text
Input describes what is available.
Output describes what is requested.
The approach governs the transformation.
```

Example:

```text
Input: graphical pieces
Possible outputs: summary, CCTP candidate, question list, surface table, form prefill, risk note.
```

Example:

```text
Output: source-backed claim
Possible inputs: project source, official web source, registered method source, evidence candidate, register entry.
```

Input availability never authorizes final output by itself.

## Complexity drivers

The method becomes more governed when any driver increases:

```text
cap ambiguity
multi-intent request
project-specific fact
source dependency
evidence dependency
regulatory or contractual effect
professional responsibility
client / company / administration visibility
external action
memory or register effect
freshness dependency
contradiction
missing context
sensitive input
```

## Context-sufficiency seam

`CONTEXT_STACK.md` owns Context Stack composition, context-sufficiency states, Context Stack Change Candidates and the candidate HESTIA context-watch boundary.

This method only determines when that responsibility should be activated during request handling:

```text
context dependency or missing context
-> consult context sufficiency
-> consume the resulting candidate / limitation signal
-> narrow output, request context or escalate when consequence requires it
```

It does not redefine HESTIA, Context Card families or Context Stack status vocabulary.

## Source-need seam

`SOURCE_NEED_AND_REGISTRY.md` owns Source Need Candidate structure, source families, legitimate routes, source registry semantics and freshness policy.

When request handling reveals a source dependency, this method applies that owner rather than defining a second source policy:

```text
missing or insufficient source
-> Source Need Candidate under SOURCE_NEED_AND_REGISTRY.md
-> permitted external retrieval handoff when applicable
-> Source Candidate / Evidence Candidate review
-> output status narrowed or blocked if sufficiency is not reached
```

External search or retrieval is a handoff, not authority. Retrieved material remains candidate until the applicable source and Evidence owners qualify it.

## Output consequence

Output intent drives governance depth.

Common output families:

```text
orientation
internal_draft
extraction_candidate
source_backed_claim
document_candidate
comparison_candidate
pre_transmission_candidate
external_action_preparation
memory_candidate
register_candidate
```

A higher-consequence output requires stronger input admission, source review, evidence and approval.

## Safe defaults

If the cap, context, source status or output consequence is unclear:

```text
allow orientation only
allow draft only
mark missing source
surface assumptions
request source or context
block external action
block memory promotion
send to ZEUS or human gate
```

## Boundary

`active_support_doctrine` boundary profile applies. This document owns proportional activation and output-consequence adaptation for request handling; it does not own Context Stack semantics, source policy, Evidence, approval, memory, workflow execution or runtime authority.

```text
The request opens the situation.
The method adapts to consequence.
Owned context/source rules are composed when needed.
The runtime may execute externally.
The candidate returns.
The gate decides status.
The human engages.
```