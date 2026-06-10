# ASSERT Reference Review

Status: support review only — spec-driven evaluation and regression-testing framework, Hermès governance-regression candidate boundary, and forbidden-import record.

Observed date: 2026-06-07

Reviewed sources:

- `https://github.com/responsibleai/ASSERT`.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Review scope

This review evaluates ASSERT ("Adaptive Spec-driven Scoring for Evaluation and Regression Testing"), a framework that turns natural-language specifications (requirements, policies, system prompts) into structured, executable evaluations scored by LLM judges and grounded in execution traces.

This document does not approve installation.

This document does not add a dependency.

This document does not create a Pantheon runtime, tool runtime, provider router, scheduler, queue, evaluation backend, LLM-judge authority, approval engine, automatic memory promotion engine, OpenWebUI function, tool, pipe, filter, action or pipeline.

## External project summary

ASSERT derives test cases directly from a specification rather than from generic benchmarks:

```text
extract behavior categories from the specification
generate single-turn and multi-turn test cases
run inferences against the target system
score conversations with LLM judges against the stated policy
```

Notable properties:

```text
multi-target (model via a routing library, agent via tracing integration, or a plain callable)
trace-aware judgment grounded in tool calls, routing and latency spans
local-first JSON / JSONL artifacts for CI pipelines and inspection
baseline comparison and a viewer for per-behavior dimensions
MIT, Python 3.11+, young (v0.1.0, 2026)
```

Pantheon interpretation:

```text
ASSERT is useful because it makes a natural-language specification testable and non-regressive.
ASSERT is risky because its LLM-judge score can be mistaken for truth, evidence or approval.
```

## Technical characterization

ASSERT should be classified as:

```text
spec_driven_evaluation_framework
regression_testing_harness
llm_judge_scoring_surface
trace_grounded_assessment_surface
external_runtime_candidate
```

It is not:

```text
Pantheon governance
the Registre Probatoire
Pantheon approval
Pantheon runtime
proof by itself
```

An ASSERT verdict is a review signal.

An ASSERT score is a ranking aid, not a certainty level.

An ASSERT regression diff is a risk signal.

None of these objects is a Registre Probatoire entry, approval, proof by itself or doctrine.

## Layer mapping

| Layer | Classification |
|---|---|
| Pantheon Next | governance policy, scope, approval, evidence and certainty boundaries |
| Hermes Agent | optional external evaluation / regression runner under Task Contract |
| ASSERT | external spec-driven evaluation and regression harness |
| OpenWebUI | cockpit exposure of eval summaries, regression diffs and Evidence Pack Candidates |

## Recommended classification

```text
name: assert
classification: External Spec-Driven Evaluation and Regression Framework
pantheon_status: reference_review_only
hermes_status: optional_governance_regression_candidate
openwebui_status: eval_result_and_regression_report_surface_candidate
memory_status: non_canonical
approval_status: not_approved_for_installation
runtime_status: external_only
```

## Valuable patterns to distill

The following patterns are useful for Pantheon if stripped of judge authority:

```text
specification turned into explicit, executable checks
behavior categories extracted from a spec before test generation
trace-grounded judgment instead of opinion-only scoring
single-turn and multi-turn coverage of a stated policy
local-first artifacts and baseline comparison for governance regression
an eval verdict expressed as a review signal, never as approval
```

These map directly to the accepted keeper "regression review for governance behavior": ASSERT is a concrete shape for testing whether the executor conforms to the governance specification, and for keeping a proven vertical (for example the architecture proof-register example) non-regressive.

## Forbidden imports

Pantheon must not import:

```text
ASSERT as a Pantheon evaluation backend
an ASSERT LLM-judge verdict as approval
an ASSERT score as a Registre Probatoire certainty level by itself
an ASSERT pass as delivery authorization
ASSERT artifacts as Canonical proof or Registre Probatoire entry
ASSERT as an internal Pantheon runtime, provider router, scheduler or queue
OpenWebUI direct execution of ASSERT bypassing Hermès and a Task Contract
```

## Boundary with the certainty axes

ASSERT informs, it does not set certainty. The three governed axes stay distinct:

```text
E0–E4 probative certainty is set by reviewed evidence, not by a judge score.
V0–V4 answer verification may consult an ASSERT signal as one input.
C0–C5 approval is never produced by an eval pass.
```

## Decision

```text
Adopt the spec-to-executable-check and trace-grounded-regression patterns.
Do not adopt the framework into Pantheon.
Keep ASSERT external; route eligible eval / regression runs through Hermès under Task Contract.
Expose eval summaries and regression diffs through OpenWebUI only.
Represent every ASSERT output as a candidate signal until reviewed.
Reject any path where a judge score becomes truth, certainty, evidence or approval.
```

## Final rule

```text
ASSERT may test conformance to the spec.
Hermès may run the test under contract.
OpenWebUI may show the score and the diff.
Pantheon decides what the result means.
The human decides what is established.
```
