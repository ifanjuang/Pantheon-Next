# Hermes MoA Review

Status: external reference / support review — Hermes Mixture-of-Agents runtime-pattern review and internal benchmark protocol.

Runtime status: non-executable.

This document classifies Hermes Mixture-of-Agents as a runtime-side pattern that Pantheon may govern when consequential outputs are at stake.

It does not implement a Hermes preset, model router, provider configuration, benchmark harness, evaluator, agent loop, approval engine, memory engine, schema, test, connector, queue, scheduler or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Source status

This review is based on:

```text
Primary source:
https://hermes-agent.nousresearch.com/docs/user-guide/features/mixture-of-agents

Research background:
https://arxiv.org/abs/2406.04692

Secondary commentary to treat cautiously:
https://webafterai.substack.com/p/two-new-ways-to-get-top-tier-ai-without
```

The Hermes documentation describes MoA as a virtual model provider: each named preset appears under the `moa` provider, reference models run first, and the aggregator is the acting model that writes the response and emits tool calls.

The paper supports the general hypothesis that multiple model outputs can improve answer quality when used as auxiliary information.

The HermesBench figures mentioned in the public commentary are vendor-side and not independently reproduced here.

## Classification

```text
Accepted: MoA as Hermes runtime capability / runtime_pattern Method Card.
Refused: MoA as Pantheon authority, Zeus substitute, truth engine, approval engine or proof engine.
To verify: quality lift, cost, latency, provider exposure and repeatability on Pantheon tasks.
To arbitrate: promotion from candidate runtime_pattern to active adapter support after internal benchmark.
```

Pantheon classification:

```text
owner_layer: execution_runtime
method_family: runtime_pattern
status: candidate / to verify
repo_state: documented non-implemented
allowed_output: Result Candidate + Evidence Pack Candidate + disagreement notes + trace references
forbidden_output: final truth, approval, canonical memory, external action, professional validation
```

## Boundary rule

MoA may increase deliberation.

It does not increase authority.

```text
MoA increases deliberation.
It does not increase authority.
```

The aggregator is still a model. Its response is still a candidate. A panel of models can share the same false premise, omit the same source, or amplify a confident mistake.

If the result touches truth, memory, approval, scope, client-facing transmission, filing, payment, visa, reception, professional responsibility or other external effect, the normal Pantheon gates still apply.

## Safe use cases

MoA is worth testing only when a hard task benefits from several model perspectives:

```text
doctrine stress test;
contradiction detection;
architecture-domain review;
complex source synthesis;
scope/risk review;
candidate benchmark comparison;
long-form strategy review;
review of another assistant's proposal.
```

MoA should not be the default for:

```text
routine rewriting;
short email drafting;
low-risk formatting;
private raw dossier material;
cheap deterministic checks;
tasks where a single strong model already performs well;
tasks requiring source verification by external evidence rather than model deliberation.
```

## Data exposure rule

MoA may send task context to several providers, depending on the preset.

Before using it on architecture-agency work, the Task Contract or operator must decide:

```text
1. which providers receive context;
2. whether client, address, contractual, financial or regulated data is present;
3. whether minimization or masking is required;
4. whether the task can run on sanitized excerpts;
5. whether a human explicitly accepts provider exposure.
```

Default posture:

```text
Use sanitized context first.
Do not send raw confidential dossiers to multi-provider MoA by default.
```

## Candidate Method Card

```text
method_card:
  id: hermes_moa_review_mode
  name: Hermes MoA Review Mode
  deck_level: runtime_pattern
  family: model_orchestration
  purpose: collect several model perspectives before an aggregator produces a Result Candidate
  use_when: hard review, contradiction search, difficult synthesis, doctrine stress test, architecture-domain reasoning benchmark
  do_not_use_when: routine drafting, private raw dossier material, low-risk rewrite, cheap single-model task, deterministic verification
  expected_output: Result Candidate + Evidence Pack Candidate + disagreement notes + cost/latency note
  evidence_expectation: evidence_pack_candidate_required if the result may support truth, memory, approval or external action
  guardrails: minimization, provider disclosure, no confidential raw payload unless explicitly authorized, no external action
  failure_modes: shared model blind spot, confident aggregation of wrong premise, cost/latency overrun, provider leakage risk, benchmark overtrust
  stop_condition: source gap, provider failure that changes task adequacy, unclear approval ceiling, sensitive data exposure unresolved
  compatible_roles: ARGOS, ATHENA, METIS, ZEUS
  hermes_profile_hint: moa-review, governance-review, evidence-review
  forbidden_outputs: final truth, approval, canonical memory, external transmission, professional validation
  gate_triggers: consequential claim, memory proposal, external action, confidential context, benchmark promotion
  visibility: visible_when_selected
  status: candidate
```

## Internal benchmark protocol

Benchmark status: candidate protocol, not executed.

Minimum internal test set:

```text
1. Doctrine contradiction review
   Input: two Pantheon governance excerpts with possible boundary tension.
   Expected: contradiction map, accepted/refused/to verify/to arbitrate classification.

2. Method-card placement review
   Input: proposed new card or runtime pattern.
   Expected: layer placement, forbidden outputs, gate triggers, candidate status.

3. Architecture source admission
   Input: sanitized PLU / mail / quote / project note conflict.
   Expected: source status, authority class, missing evidence, professional caution.

4. Mission-scope guard
   Input: draft client or enterprise email with engaging wording.
   Expected: risky wording, safer candidate, external-action gate status.

5. Proof gap review
   Input: candidate conclusion with partial sources.
   Expected: assertion map, missing evidence, E-level confidence, no false proof.

6. Cost/latency sanity check
   Input: same task on single model and MoA.
   Expected: quality delta, token/cost delta, latency delta, failure notes.
```

Each test must record:

```text
task_id:
input_class:
models_or_preset:
context_minimization:
single_model_result:
moa_result:
quality_delta:
missed_contradictions:
false_confidence:
cost_delta:
latency_delta:
human_review:
status: useful | not_worth_cost | unsafe | inconclusive
```

Promotion threshold:

```text
Do not promote MoA beyond candidate runtime_pattern unless it repeatedly improves hard-task review quality without increasing false confidence, confidential exposure or unclear authority.
```

## Result status

A MoA result may be strong.

It remains:

```text
Result Candidate;
Evidence Pack Candidate;
reviewable trace;
not proof;
not approval;
not memory;
not external action.
```

The validated remains.
