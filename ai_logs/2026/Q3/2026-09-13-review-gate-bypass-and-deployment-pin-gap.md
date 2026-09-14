# AI log — gate bypass, presentation key namespace, deployment pin gap

Date: 2026-09-13

Status: implementation intervention — bounded defect correction plus two guards.
Boundary profile: validation_only_trace.

## Why

A line-by-line review of the 74 commits between `37ce4413` and `b2a0b7f8` found
nine reproducible defects. Three shared one shape: a control that exists and
controls nothing. This intervention closes the two that are correctable in
place and puts a floor under the third, which is not.

## Change

- Updated `mcp-server/pantheon_mcp/policy.py`: `_semantic_bool` now composes a
  caller `observations` entry with the legacy top-level field instead of letting
  the observation win. `external_effect` keeps its tri-state shape and composes
  upward only, so `"unknown"` still escalates.
- Updated `implementation/mvp_vertical/hermes_runs_observer.py`: per-platform
  presentation keys are read under `display.platforms.<platform>.<name>`, the
  namespace `deployment/ubuntu/configure-hermes-activity-projection` actually
  writes.
- Updated `implementation/tests/test_hermes_presentation_observation.py`: its
  fixtures mirrored the implementation's wrong keys, which is why it passed
  against the defect. Added a test that reads the namespace off the deployment
  script.
- Added `mcp-server/tests/test_intake_signal_composition.py`.
- Added `tests/test_deployment_release_env_completeness.py`.
- Updated the `runtime-observer` digest in
  `implementation/hermes/distribution/pantheon-standard.lock.yaml`.

## What each defect did

`observations` overruled the request in both directions. A request declaring
`external_effect: True` classified K4 with `blocked_until_gate: True`; adding
`observations: {"external_effect": False}` dropped it to K3 and removed the User
Decision Gate. Reproduced identically for `transmission_requested`,
`memory_promotion_requested`, `professional_position`,
`financial_or_contractual_effect` and `writes_state`. The asymmetry was internal
evidence of oversight: `conditions` already composed upward only, three lines
away.

The observer queried `platforms.<p>.show_reasoning` while the deployment script
sets `display.platforms.<p>.show_reasoning`. Hermes answered "no such key" for
every platform, so the per-platform value was permanently `unknown` and
`configuration_alignment` could never reach `misaligned` — while
`PROFILE_CONSTITUTION.md` declares `private_reasoning_projection: forbidden`.

## What was not fixed, and why

Ten `${RELEASE_*:?}` pins are consumed by `deployment/ubuntu/` and defined
nowhere in `release.env`. Under `set -Eeuo pipefail` each script dies on its
first line: `install-node`, `update-node`, `configure-docling-local` and
`configure-marker-local` cannot run at all.

`release.env` carries reviewed deployment targets. Inventing a value there would
assert a review that did not happen, and a wrong CUDA pin breaks a real node.
`download.pytorch.org` is outside this environment's network policy, and the ten
names have never existed in the file's history, so no value was recoverable or
verifiable. The gap is therefore recorded as a shrink-only ratchet: a new
undefined pin fails immediately, and each reviewed value added retires its line.
Filling the ten remains a human decision.

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: the policy classification restores gates that were reachable
around; the observer now reads keys that resolve. Neither activates anything.
Authority impact: none. No approval, admission or promotion path changed.
Schema/test/CI impact: two test files added, one corrected, one distribution
digest refreshed. `mcp-server/tests` 273 passed, `tests` 734 passed,
`implementation/tests` 1432 passed / 413 skipped.
External action: none.
Memory behavior: none.

## Local distinctions

```text
described condition != consequence classification
observation supplied != signal absent
control present != control effective
test passing != behavior correct
pin demanded != pin reviewed
reproduction != approval
```
