# Future AGI Reference Review

Status: support review only — AI reliability suite, Hermes evaluation and simulation candidate boundary, and forbidden-import record.

Observed date: 2026-05-29

Reviewed sources:

- `https://github.com/future-agi/future-agi`;
- `https://docs.futureagi.com`;
- `https://futureagi.com`.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Review scope

This review evaluates Future AGI as an external AI-agent reliability platform that combines simulation, evaluation, tracing, guardrails, gateway behavior, datasets and optimization loops.

This document does not approve installation.

This document does not add a dependency.

This document does not create a Pantheon runtime, tool runtime, provider router, scheduler, queue, observability backend, MCP layer, A2A layer, plugin manager, simulation runtime, evaluation backend, automatic approval system, automatic memory system, OpenWebUI function, OpenWebUI tool, OpenWebUI pipe, OpenWebUI filter, OpenWebUI action or OpenWebUI pipeline.

## External project summary

Future AGI presents itself as an open-source platform for evaluating, observing and improving LLM and AI-agent applications.

Its public materials describe a combined lifecycle:

```text
simulate -> evaluate -> protect -> monitor -> optimize
```

The main capability surfaces are:

```text
simulation
evaluation metrics
OpenTelemetry-style tracing
guardrail scanners
gateway and provider routing
prompt optimization
datasets and experiments
feedback loops from production traces
```

Pantheon interpretation:

```text
Future AGI is useful because it makes agent reliability observable, testable and stress-tested.
Future AGI is risky because it also combines gateway authority, runtime infrastructure and self-improvement language.
```

## Technical characterization

Future AGI should be classified as:

```text
ai_reliability_platform
observability_and_eval_system
agent_simulation_surface
guardrail_scanning_surface
provider_gateway_surface
prompt_optimization_surface
feedback_loop_platform
external_runtime_candidate
```

It is not:

```text
Pantheon governance
Pantheon memory
Pantheon approval
Pantheon runtime
OpenWebUI cockpit
Hermes profile
Hermes skill by itself
```

A Future AGI trace is runtime trace material.

A Future AGI evaluation score is a review signal.

A Future AGI simulation result is a stress-test candidate.

A Future AGI guardrail result is a risk signal.

A Future AGI optimization proposal is a candidate only.

None of these objects is Canonical Memory, approval, proof by itself or doctrine.

## Layer mapping

| Layer | Classification |
|---|---|
| Pantheon Next | governance policy, scope, approval, evidence and memory boundaries |
| Hermes Agent | optional external execution caller or evaluation runner under Task Contract |
| Future AGI | external reliability suite for simulation, evaluation, tracing, guardrails, gateway and optimization |
| OpenWebUI | cockpit exposure of simulation status, evaluation summaries, guardrail results, Evidence Pack Candidates and User Decision Gates |
| Providers and external tools | external systems with read, write, routing or data exposure effects |

## Recommended classification

```text
name: future_agi
classification: External AI Reliability Suite
pantheon_status: reference_review_only
hermes_status: optional_evaluation_and_simulation_candidate
openwebui_status: evaluation_result_and_decision_surface_candidate
memory_status: non_canonical
approval_status: not_approved_for_installation
runtime_status: external_only
```

## Component decision matrix

| Future AGI surface | Pantheon decision | Hermes decision | OpenWebUI decision | Boundary |
|---|---|---|---|---|
| Simulate | KEEP as pattern | optional Hermes-side pre-execution stress test | expose scenario, result and limitation summaries | simulation success is not delivery approval |
| Evaluate | KEEP as signal | optional evaluator under Task Contract | expose scores as review signals | eval pass is not C0-C5 approval |
| TraceAI / tracing | ADAPT | optional trace source or instrumentation candidate | expose governance-relevant trace summary | trace store is not Evidence Pack by itself |
| Guardrails | ADAPT | optional scanner signal | expose risk warning and block reason | guardrail pass is not policy approval |
| Gateway / routing | REJECT as Pantheon import | Hermes-only possible under separate tool policy | expose provider/status only if governed | Pantheon must not become provider router |
| Prompt optimization | ADAPT strongly | optimization candidate only | expose diff and rationale for review | no automatic prompt or policy mutation |
| Datasets and experiments | ADAPT | evaluation dataset candidate | expose dataset scope and version | dataset result is not proof by itself |
| MCP / A2A exposure | REJECT as Pantheon import | external-only capability if separately reviewed | expose as capability gap or tool surface | no internal Pantheon MCP/A2A layer |
| Self-improving agent loop | REJECT | convert to improvement candidate flow only | expose approval requirement | no self-evolution or auto-promotion |

## Valuable patterns to distill

The following patterns are useful for Pantheon if stripped of runtime authority:

```text
pre-execution simulation before high-risk tasks
persona and edge-case stress tests before external exposure
trajectory evaluation rather than only final-output scoring
evaluation score as review signal, not approval
guardrail result as risk note, not policy authority
trace-to-evidence summary instead of raw trace import
feedback loop broken into explicit improvement candidates
simulation failure as User Decision Gate trigger
```

## Forbidden imports

Pantheon must not import:

```text
Future AGI platform as Pantheon runtime
Future AGI gateway as Pantheon provider router
Future AGI tracing backend as Pantheon observability backend
Future AGI simulations as automatic Task Contract execution
Future AGI eval pass as approval
Future AGI guardrail pass as delivery authorization
Future AGI optimization as automatic doctrine, prompt, workflow or skill mutation
Future AGI production feedback loop as self-evolution
Future AGI datasets as Canonical Memory
Future AGI traces as Evidence Packs by themselves
Future AGI MCP or A2A exposure as internal Pantheon capability layer
Future AGI schedules, workers, queues, Temporal, RabbitMQ or runtime services into Pantheon
OpenWebUI direct execution of Future AGI bypassing Hermes and Task Contract
```

## Risk classification

| Capability surface | Default risk class | Reason |
|---|---:|---|
| Reading public Future AGI documentation | T1 | external reference retrieval only |
| Running evaluation against supplied candidate output | T2 | transforms output into score and review signals |
| Running simulation against a bounded Hermes candidate | T2/T3 | may affect later approval or task mutation |
| Creating optimization candidates from traces | T3 | may alter prompts, policies, skills or future behavior if adopted |
| Gateway/provider routing | T5 | touches provider choice, secrets, routing, trust boundary and cost behavior |
| Guardrail enforcement inline with live calls | T4/T5 | may block, alter or route live external effects |
| Self-hosting or deployment | T5 | runtime installation, configuration, secrets and infrastructure |
| MCP/A2A exposure | T5 | creates tool/routing surface and possible hidden execution path |
| Automatic self-improvement | T5 | doctrine, skill, prompt or memory mutation risk |

Final approval remains governed by `APPROVALS.md` and `EXTERNAL_TOOLS_POLICY.md`.

## Task Contract requirement

A Future AGI-mediated evaluation, simulation or optimization pass requires a Task Contract when it touches:

- private or professional dossier material;
- model/provider routing;
- guardrail configuration;
- traces or production calls;
- prompt, policy, skill or workflow mutation;
- repository mutation;
- protected governance areas;
- memory-sensitive output;
- external write or communication effects;
- MCP, A2A, gateway, scheduler, queue or deployment surfaces.

Minimum Task Contract checks:

```text
capability_surface
input_scope
excluded_data
simulation_or_eval_goal
risk_class
provider_or_runtime_boundary
expected Evidence Pack summary
approval level
memory rule
optimization_candidate_rule
rollback or correction path when relevant
```

## Evidence interpretation

Future AGI output may support an Evidence Pack Candidate as:

```text
Evaluation Signal
Simulation Result
Trace Summary
Guardrail Result
Dataset Reference
Prompt Optimization Candidate
Capability Gap
Risk Note
```

It must not become:

```text
Canonical Memory
Approval
Proof by itself
Doctrine
Runtime State owned by Pantheon
Delivery authorization
```

Raw traces, prompt logs, private payloads, secrets, API keys, provider credentials and production-call contents must not be copied into Evidence Packs unless explicitly scoped, redacted and approved.

## User Decision Gate triggers

Use a User Decision Gate when Future AGI involvement affects:

- external delivery or transmission;
- provider routing or gateway policy;
- guardrail blocking or override;
- optimization of prompts, skills, workflows, policies or doctrine;
- production trace reuse;
- private, client, patient, legal, financial, architectural or contractual material;
- memory promotion from traces, datasets or repeated outcomes;
- discrepancy between simulation result and evidence state;
- evaluation score being treated as approval;
- simulated persona result being treated as proof of real-user safety;
- self-hosting, deployment, secrets, MCP or A2A exposure.

## Pantheon interpretation of self-improvement

Future AGI's self-improvement vocabulary must be translated into Pantheon vocabulary as:

```text
Improvement Candidate
```

An Improvement Candidate may include:

```text
observed failure
source trace summary
simulation scenario
evaluation signal
proposed change
risk note
affected scope
approval requirement
memory implication
rollback path
```

It must not include:

```text
automatic merge
automatic prompt promotion
automatic skill activation
automatic doctrine mutation
automatic memory promotion
automatic workflow change
```

## Decision

```text
Adopt the reliability patterns.
Do not adopt the platform into Pantheon.
Keep Future AGI external.
Route eligible evaluation and simulation work through Hermes under Task Contract.
Expose simulation, evaluation, guardrail and trace summaries through OpenWebUI only.
Represent all outputs as candidates until reviewed.
Reject gateway, self-improvement and runtime-infrastructure imports into Pantheon.
```

## Final rule

```text
Future AGI may test the candidate.
Hermes may run the test under contract.
OpenWebUI may show the result.
Pantheon decides what the result means.
The human decides what changes.
```
