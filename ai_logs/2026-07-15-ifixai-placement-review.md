# iFixAi external placement review

Date: 2026-07-15

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Re-verified the stale draft PR #353 and its governing issue #368 against the current `main` branch.
- Reviewed `ifixai-ai/iFixAi` at pinned commit `b911e25fcdf9d49e0e025162f2650253072449e5`.
- Added a bounded placement record to the External Tool Placement Register.
- Distilled measurability-coverage disclosure and declared-governance demotion as candidate patterns.
- Replaced the former three-line watchlist proposal with a source-pinned record that separates observations, reviewer inferences and unknowns.

## Why

The old draft predated the External Tool Placement Register and did not record a pinned upstream version, data-handling risks, telemetry, reproducibility limits or provenance. Replaying its original diff would create parallel and incomplete classification. The reconstructed record keeps iFixAi external, inactive and non-approved while preserving the useful evaluation-method patterns.

## Evidence

```text
Pantheon repository: ifanjuang/Pantheon-Next
superseded draft: PR #353
governing issue: #368
upstream repository: https://github.com/ifixai-ai/iFixAi
reviewed commit: b911e25fcdf9d49e0e025162f2650253072449e5
upstream version observed: 3.2.0
upstream license observed: Apache-2.0
source paths reviewed: README.md, LICENSE, pyproject.toml, SECURITY.md,
  ifixai/telemetry.py, ifixai/evaluation/manifest.py,
  ifixai/evaluation/analytic_judge.py, ifixai/scoring/engine.py,
  docs/methodology.md, docs/reproducibility.md,
  docs/testing-your-agent.md, docs/scoring.md
observed source inconsistency: docs/reproducibility.md says manifest schema v2;
  ifixai/evaluation/manifest.py defines v3
local upstream installation: not performed
local upstream tests: not performed
live provider evaluation: not performed
exact upstream CI for reviewed commit: not established
```

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: support placement and candidate-pattern registers only; no doctrine promotion.
Schema/test/CI impact: none.
External action: documentation PR only; no iFixAi installation, execution, provider call or telemetry event.
Professional data: none used or transmitted.

## Local distinctions

```text
evaluation_completed != evidence_sufficient
grade_A != approved
independent_judge != professional_validation
manifest_verified != live_result_reproducible
insufficient_evidence_excluded != coverage_sufficient
installed != approved
telemetry_disclosed != telemetry_authorized
```
