# New Capability Effect Review

Status: active support doctrine — rite, documented non-implemented.

```text
OpenWebUI exposes.
Hermes Agent executes.
The Governance College judges the effects.
Zeus arbitrates the status and the rule.
Pantheon Next governs.
```

## Purpose

Pantheon does not grow by absorbing every new tool, feature, connector, skill or runtime surface.

Pantheon grows by qualifying the effects those capabilities make possible.

This rite defines the review to run when a new capability appears and could change truth, memory, evidence, approval, scope, status, external action or professional responsibility.

It adds no runtime. It adds no scheduler, queue, gateway, crawler, plugin manager, approval engine, memory engine or execution surface.

## Trigger

Run this rite when a new or changed capability appears in any bound or candidate tool layer, including:

- execution runtime;
- exposure surface;
- observability layer;
- connector gateway;
- document or web extraction adapter;
- local plugin;
- domain-pack method support;
- workflow forging surface;
- memory, graph, RAG, trace or data-platform candidate.

Examples:

```text
new Hermes skill
new browser/crawler/extractor
new OpenWebUI action
new Revit plugin operation
new Langfuse trace/signal
new Notion/Gmail/Slack connector path
new memory batch operation
new automation blueprint
new graph/data platform capability
```

## Core rule

```text
The tool expands what can be done.
The College judges what that changes.
Zeus decides whether the rule exists.
Pantheon governs the rule.
Hermes executes within it.
```

A new capability is never admitted because it is impressive, popular, installed, secure-scanned, technically successful or already available in the runtime.

Admission starts from effect classification.

## Review question

For each new capability, ask:

```text
What effects can this capability produce?
```

Then classify whether it can produce or alter:

```text
truth_effect
memory_effect
evidence_effect
approval_effect
scope_effect
status_effect
external_action_effect
professional_responsibility_effect
security_or_access_effect
```

If none apply, the capability is a feature of the appropriate tool.

If any apply, Pantheon governs the decision and the capability must be mapped to existing doctrine or escalated for a new rule.

## College roles

The Governance College does not execute the capability. It judges the effect surface.

```text
MÈTIS      frames the request, detects ambiguity and keeps the cap.
ATHENA     judges coherence, strategic fit and doctrine drift.
ARGOS      checks evidence, sources, traceability and claim status.
THEMIS     checks approval, responsibility, external effect and risk.
HEPHAISTOS checks technical feasibility, adapter shape and failure modes.
APOLLON    checks clarity, quality and final review posture.
ZEUS       arbitrates status, rule creation, refusal or escalation.
```

No role may promote its own candidate into doctrine, approval, memory or truth.

## Decision path

```text
new_capability
  -> effect_review
  -> existing_rule_found ? adapter_mapping : kernel_gap_candidate
  -> Zeus arbitration
  -> accepted | refused | to_verify | to_arbitrate
```

### Existing rule found

If existing doctrine already covers the effect, write only an adapter, binding, reference review, profile note or handoff rule.

The tool remains outside Pantheon.

### Kernel gap found

If the new capability reveals an effect that the current governance model cannot express without distortion, Zeus may arbitrate a new tool-agnostic rule.

A kernel rule must pass this test:

```text
Can the rule be written without naming the tool?
```

If yes, it may belong in Pantheon support doctrine or canonical doctrine.

If no, it belongs in an adapter, binding or reference review.

## Required output

The rite outputs a `capability_effect_review_candidate`.

```yaml
capability_effect_review_candidate:
  status: candidate
  capability:
    name:
    source:
    layer:
    version_or_ref:
  effect_classes:
    truth_effect: false
    memory_effect: false
    evidence_effect: false
    approval_effect: false
    scope_effect: false
    status_effect: false
    external_action_effect: false
    professional_responsibility_effect: false
    security_or_access_effect: false
  college_review:
    metis:
    athena:
    argos:
    themis:
    hephaistos:
    apollon:
  existing_rules:
    -
  missing_rules:
    -
  decision_zeus:
    classification: accepted | refused | to_verify | to_arbitrate
    reason:
    required_rule:
    required_adapter_note:
    required_approval_level:
  forbidden_collapses:
    -
  next_action:
```

## Forbidden collapses

```text
new runtime power = new Pantheon power
installed capability = admitted capability
security scan = approval
retrieval = evidence
crawl = source admission
trace = Evidence Pack
RAG ingestion = memory promotion
automation success = valid decision
plugin preview = approval
adapter convenience = legitimacy
```

## Relationship to adapters

Adapters remain useful and replaceable.

A feature can be powerful in the adapter while still being constrained by Pantheon.

```text
Adapter expresses the capability.
Pantheon classifies the effect.
```

The dependency points toward Pantheon, not the reverse.

## Example — Crawl4AI

Crawl4AI can extract public web pages into Markdown and structured output.

Effect review:

```text
source_read: yes
source_transformation: yes
evidence_effect: possible
memory_effect: possible if ingested
external_action_effect: no by default
security_or_access_effect: yes
```

Pantheon rule implication:

```text
Extraction is not source admission.
Source admission is not evidence.
Evidence Candidate is not proof.
Proof is not approval.
Approval is not memory.
```

Therefore Crawl4AI belongs in the execution runtime as an extraction adapter candidate. Pantheon governs the source status, evidence status, approval need, memory boundary and scope.

## Example — first-principles assumption review

A first-principles skill can expose hidden assumptions.

Effect review:

```text
truth_effect: possible if mistaken for conclusion
scope_effect: possible if it reframes the task
professional_responsibility_effect: possible in domain work
```

Pantheon rule implication:

```text
Assumption exposure is not decision.
A rebuilt candidate is not approved doctrine.
A critique lens is not Zeus arbitration.
```

The skill may support the College. It does not replace the College.

## Guiding sentence

```text
Pantheon becomes stronger when tools become stronger, not by absorbing their execution, but by judging their effects and adding rules when the governance model lacks them.
```
