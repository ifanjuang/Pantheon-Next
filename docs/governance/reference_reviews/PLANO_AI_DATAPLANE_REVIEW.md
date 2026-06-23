# Plano AI Dataplane Review

Status: external reference / adapter candidate — AI gateway, routing, orchestration, observability and filter-chain review.

Reviewed source:

```text
https://github.com/katanemo/plano
Review date: 2026-06-22
```

This document records a Pantheon Next placement review of Plano.

It is not canonical doctrine.

It is not an implementation request.

It does not install Plano, configure a gateway, create a data plane, route models, run agents, create filters, configure traces, add a provider key, add Docker, add a service, change `.env`, mutate `operations/`, mutate `platform/`, add schemas or create tests.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Source signal

Plano presents itself as an AI-native proxy server and data plane for agentic applications.

The repository positions Plano around:

```text
agent routing and orchestration;
model agility / LLM routing;
agentic signals;
OpenTelemetry traces and metrics;
filter chains for safety, moderation and memory hooks;
OpenAI-compatible agent endpoints;
Envoy-based proxy infrastructure.
```

The useful signal for Pantheon is not the product claim that a data plane makes agentic apps production-ready.

The useful signal is this architectural separation:

```text
agent code remains focused on execution;
routing, provider management, traces and filters move to an out-of-process gateway / data plane;
Pantheon can govern the consequences without becoming that gateway.
```

## Pantheon placement

Plano belongs, if ever used, outside the Pantheon kernel.

Candidate placement:

```text
exposure surface -> OpenWebUI / Pantheon Control
execution runtime -> Hermes Agent
AI gateway / data plane -> Plano candidate
observability layer -> Plano / Langfuse / other candidate
connector gateway -> separate candidate, unless Plano proves bounded fit
Pantheon -> status, proof, approval, memory, scope, external-action governance
```

Plano may be a carrier for runtime routing and observation.

Plano must not be treated as a governance authority.

## Capability classification

| Plano surface | Pantheon classification | Accepted use | Refused interpretation |
|---|---|---|---|
| AI-native proxy / data plane | external runtime adapter candidate | Centralize agent traffic and model calls outside Pantheon | Pantheon runtime or governance kernel |
| Agent orchestration | execution routing candidate | Route to bounded HTTP agents under Task Contract | self-authorized workflow or Governance College |
| Model routing / model aliases | provider-router candidate outside Pantheon | Select provider/model according to runtime config | proof, approval or truth status |
| OpenAI-compatible agent endpoints | runtime interoperability | Let agents remain simple HTTP services | automatic capability authorization |
| Filter chains | policy enforcement point candidate | Apply safety/moderation/redaction checks before or during runtime calls | Pantheon approval engine or final policy authority |
| Memory hooks | high-risk adapter candidate | Possibly write runtime memory candidates under strict scope | Registre Probatoire, canonical memory, automatic memory promotion |
| Agentic signals | observability candidate | Produce trace / behavior signals for review | Evidence Pack by themselves |
| OpenTelemetry traces / metrics | observability candidate | Support Trace Candidates and runtime diagnostics | Evidence Pack authority or validation |
| Hosted Plano LLMs / orchestrator | provider dependency candidate | Developer bootstrap only, if allowed by scope and data policy | stable trusted infrastructure or local professional perimeter |
| Envoy-based infrastructure | implementation detail | May support reliable proxying if self-hosted | Pantheon dependency or doctrine source |

## Accepted

```text
Plano as external AI gateway / data-plane candidate.
Plano as LLM routing and model-agility reference.
Plano as out-of-process agent orchestration reference.
Plano as trace / signal / observability reference.
Plano as possible Policy Enforcement Point carrier for runtime filters.
Plano as possible adapter between Hermes profiles and model/provider traffic.
Plano as possible NUC / server-side component, not mobile-phone core.
```

## Refused

```text
Plano as Pantheon runtime.
Plano as canonical governance layer.
Plano as approval engine.
Plano as Evidence Pack authority.
Plano as Registre Probatoire or canonical memory.
Plano as automatic memory promotion mechanism.
Plano as source of truth for claims.
Plano as autonomous agent team manager.
Plano as hidden scheduler, queue or workflow authority.
Plano as bypass around Task Contract, Context Pack, evidence expectation or approval ceiling.
Plano as automatic external-action authorizer.
```

## To verify

Before any local installation, verify:

```text
self-hosting requirements;
minimum deployment shape;
whether Docker is required or optional;
provider key storage and redaction behavior;
request / response log retention;
trace export format;
OpenTelemetry compatibility and destination;
filter-chain semantics;
whether filters can fail closed;
whether memory hooks can be disabled or forced candidate-only;
whether hosted Plano LLMs are optional;
whether Plano-Orchestrator can run locally or must call hosted infrastructure;
compatibility with Hermes profiles and Kanban workers;
compatibility with OpenAI-compatible local and cloud providers;
network exposure and authentication model;
ability to bind only to localhost / Tailscale / private network;
license and operational maturity;
rollback / bypass strategy if Plano is unavailable.
```

## To arbitrate

```text
Is Plano needed now, or premature before the Hermes local stack stabilizes?
Should AI gateway / data-plane stay unbound until a real multi-provider routing pain appears?
Should Langfuse remain the first observability candidate instead of introducing Plano traces?
Should filters be treated as runtime PEP candidates under a Pantheon PDP, or kept as purely defensive runtime checks?
Can memory hooks be allowed at all, or must they remain disabled until Registre Probatoire rules are fully implemented?
Should the first trial be local-only on the NUC, never on Termux/mobile?
```

## Termux / mobile relation

Plano should not be placed on the phone by default.

The Termux phone pattern is better treated as a mobile execution satellite:

```text
phone / Termux -> lightweight Hermes client or worker;
NUC / home server -> persistent services, sync, gateway, traces, backups;
Pantheon -> governance of consequence.
```

If Plano is ever tested, the safer first target is the NUC or another always-on server.

Reason:

```text
provider keys, traces, memory hooks, filters and routing state are persistent infrastructure concerns;
Android process lifecycle and mobile storage are not the right authority surface for them.
```

## Candidate architecture

```text
User / OpenWebUI / Pantheon Control
  -> Task Contract / approval gate
  -> Hermes profile or Kanban worker
  -> Plano AI gateway candidate
       -> model provider / agent endpoint / filter chain / trace sink
  -> Result Candidate + Evidence Pack Candidate + Trace Candidate
  -> Pantheon review gate
  -> human decision
```

Plano may sit between Hermes and:

```text
LLM providers;
OpenAI-compatible local models;
HTTP agent endpoints;
trace sinks;
runtime filter chains.
```

Plano must not sit between Pantheon and its own governance status.

## Required return discipline

If Plano is used in a governed execution handoff, the return path must separate:

```text
handoff_delivery_status;
runtime_task_status;
plano_route_status;
filter_outcome;
trace_candidate_refs;
result_candidate;
evidence_pack_candidate;
approval_gap;
memory_impact;
external_effect_status;
unchanged_objects.
```

A successful Plano route is not proof.

A passing filter is not approval.

A trace is not an Evidence Pack.

A memory hook is not a Registre Probatoire entry.

## Capability Gap examples

Plano should surface, not hide, gaps such as:

```text
provider key missing;
model alias unresolved;
agent endpoint unreachable;
filter chain failed open;
filter chain blocked;
trace export unavailable;
memory hook attempted canonical write;
external network target unapproved;
hosted orchestrator outside allowed data perimeter;
Task Contract missing;
approval ceiling missing;
idempotency key missing for non-read-only effect.
```

## Admission test

Plano is admissible only if it can be constrained to this rule:

```text
Plano routes and observes runtime traffic.
It may enforce defensive runtime checks.
It returns candidates and gaps.
It does not decide truth, approval, memory, scope or external legitimacy.
```

If Plano cannot be configured to preserve that boundary, it is refused for Pantheon use.

## Status decisions

```text
Accepted:
Plano as external AI gateway / data-plane reference.
Plano as possible runtime routing and observability adapter candidate.
Plano as possible filter-chain PEP carrier, subject to later review.
Plano as possible NUC-side component for Hermes traffic, not Pantheon kernel.

Refused:
Plano as Pantheon runtime.
Plano as approval engine.
Plano as Evidence Pack authority.
Plano as Registre Probatoire or canonical memory.
Plano as autonomous orchestration authority.
Plano as hidden scheduler, queue, workflow authority or external-action authorizer.

To verify:
Self-hosting requirements.
Provider key handling.
Trace export and retention.
Filter-chain fail behavior.
Memory hook disablement / candidate-only behavior.
Hermes profile / Kanban compatibility.
Local-only or private-network deployment.

To arbitrate:
Whether Plano should be tested before or after Hermes local stack stabilization.
Whether Plano overlaps with Langfuse, Nango, MCP policy-server or future bridge candidates.
Whether filter chains are allowed as PEP candidates.
Whether memory hooks are categorically disabled until Registre Probatoire implementation exists.
```

## Final rule

```text
Plano may route, filter and observe execution traffic.
Hermes still executes.
Pantheon still governs.
The human still decides.
```
