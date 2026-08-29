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

This method extends `REQUEST_LIFECYCLE.md` and `CONTEXT_STACK.md` without replacing them.

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
a request with context dependency -> HESTIA
a request with source dependency -> ARGOS
a request with liability / external effect -> THEMIS + ZEUS / human gate
a request with memory effect -> CERBÈRE / CHARON + ZEUS / human gate
a request with candidate output -> evidence and approval posture
```

The method must not impose a heavy ritual on every request.

It becomes stricter when the situation demands it.

## Request decomposition

A request is decomposed into separate candidates:

```text
Request Candidate          -> what the user asked, as received
Cap Candidate              -> what MÈTIS understands as the real aim
Expected Context Profile   -> what HESTIA expects to safely proceed
Input Admission Candidate  -> what was supplied, retrieved, recalled or is absent
Source Need Candidate      -> what source is missing and why it matters
Output Intent Candidate    -> what kind of output is expected and under what status
Situated Approach Candidate -> what motifs are composed to handle this situation
Result Candidate           -> output produced by a role, runtime or adapter
Evidence Pack Candidate    -> review material supporting or contradicting assertions
Gate / Decision            -> accepted, refused, to_verify, to_arbitrate or blocked
```

These are governance objects. They do not execute.

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

## HESTIA and context sufficiency

HESTIA defines expected context after the cap is understood.

She does not validate sources.

She does not produce evidence.

She does not approve, transmit, canonize, promote memory or execute.

She compares:

```text
expected context
vs
available admitted input
vs
requested output status
```

She may produce:

```text
Context Stack Change Candidate
Source Need Candidate
scope limit proposal
allow draft only signal
block external action signal
request role review signal
```

Final arbitration remains with ZEUS.

## Source absence

When information is missing, Pantheon creates a Source Need Candidate before any external search.

```text
missing information
-> why it is needed
-> needed for which output status
-> source family needed
-> permitted source routes
-> freshness requirement
-> fallback if not found
```

External search is a handoff, not an authority.

Search results are candidates.

A read source is still only a Source Candidate until Argos qualifies authority, scope, freshness and applicability.

Evidence supports; approval validates.

## Source families

Pantheon distinguishes source families because they have different authority and allowed uses:

```text
project_source
external_official_source
professional_method_source
agency_method_source
technical_competence_source
stable_knowledge_source
volatile_source
memory_or_recall_source
registered_source
absent_source
```

A method source guides treatment; it does not prove project facts.

A competence source enables a capability; it does not validate the returned content.

A volatile source must be checked at use time or at the relevant project date.

## Source routes

A Source Need Candidate may propose routes such as:

```text
project_corpus
source_registry
official_web_route
professional_method_reference
agency_method_reference
technical_competence_documentation
memory_or_register_review
user_request_for_missing_source
```

The route does not validate the source.

The registry does not validate the source.

ARGOS reviews source status.

ZEUS arbitrates sufficiency when consequential.

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

`active_support_doctrine` boundary profile applies. This document owns the grammar for adaptive request governance; it does not become a workflow engine or execution authority.

```text
The request opens the situation.
The method adapts to consequence.
The runtime may execute externally.
The candidate returns.
The gate decides status.
The human engages.
```