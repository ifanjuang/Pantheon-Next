# AI Log — Hermes Evaluation and Simulation Candidate

Date: 2026-05-30

## Summary

Added the two-layer design for a Hermes-side evaluation and simulation candidate.

This completes the selected C approach:

1. Pantheon governance framing.
2. Hermes candidate capability template.

## Files changed

- `docs/governance/HERMES_EVALUATION_AND_SIMULATION_LAYER.md`
- `hermes/profiles/_base/EVALUATION_AND_SIMULATION_CANDIDATE.md`
- `hermes/profiles/_base/README.md`
- `ai_logs/2026-05-30-hermes-evaluation-simulation-candidate.md`

## Why

The Future AGI review and `PRE_EXECUTION_SIMULATION.md` created the doctrine that simulation can reveal risk but cannot authorize execution.

This pass translates that doctrine into a bounded Hermes candidate design without implementing anything.

## Governance interpretation

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Pantheon defines the legitimacy frame.

Hermes may later execute bounded simulations under Task Contract.

OpenWebUI may expose status, risks, Evidence Pack Candidate links and User Decision Gates.

The human decides when risk remains material.

## Candidate components described

- `simulation_runner`
- `persona_suite`
- `scenario_set`
- `trajectory_eval`
- `guardrail_signal`
- `trace_summary`
- `simulation_evidence_summary`
- `improvement_candidate_builder`
- `capability_gap_reporter`

These are design terms only.

They are not implemented classes, tools, workers, services or skills.

## Boundary preserved

This intervention does not:

- install Future AGI;
- create a Hermes skill;
- create a simulator;
- create an evaluator;
- create a provider router;
- create a gateway;
- create an observability backend;
- create MCP or A2A infrastructure;
- create a scheduler, queue or worker;
- create automatic approval;
- create automatic memory promotion;
- create a self-improvement loop;
- modify schemas, tests, operations, Docker, `.env`, `pyproject.toml` or `CLAUDE.md`.

## Final rule

```text
Hermes may test a candidate.
Hermes must not validate it.
Pantheon governs what the test means.
The human decides when risk remains material.
```
