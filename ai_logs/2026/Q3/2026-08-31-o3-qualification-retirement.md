# Historical O3 qualification retirement

Date: 2026-08-31
Status: validation / intervention trace

## Objective

Retire the executable O3 Hindsight/Obsidian/Hermes historical fixture without deleting historical evidence or weakening the reusable current Hindsight/Hermes contract.

## Observed state

- `.github/workflows/implementation-hindsight-obsidian-hermes-o3-lab.yml` declares itself a historical regression fixture.
- It pins Hindsight `0.8.5`, hindsight-obsidian `0.2.0`-era commit `b627aa6f...`, and Hermes commit `3c27eb62...`; the workflow itself states that these are not the current deployed/qualified baseline.
- Pantheon-Next issue #655 is closed as completed and its durable qualification record distinguishes current Hindsight/Hermes workspace qualification from historical O1-O3 fixtures.
- The active `protect-main` repository ruleset requires four status contexts only: `mcp-server module tests`, `Read-only governance checks`, `Packaging and release contract`, and `Obsolete document authority consistency`.
- None of the external qualification labs inventoried by PR #887 is a required status context in that ruleset. A workflow running on `pull_request` is therefore not, by itself, a required merge gate.
- PR #887's proposed `blocking_without_declared_decision_ceiling: 17` would encode that false equivalence as a new permanent registry.
- Langfuse Q1/Q2 and the Obsidian wiki graph/health lab still have current replay consumers in governance/runbook material and are therefore not retired here.
- External qualification pins are intentionally untouched; PR #892 owns current pin alignment.

## Decision

Retire O3 as a live executable lane rather than keep it as `workflow_dispatch`-only.

Historical reproducibility remains available through Git history, issue #655, prior PR/run artifacts and AI logs. Keeping an executable CI surface is not required to preserve provenance.

Two provider-neutral assertions that O3 had been carrying are retained under the current O1 contract:

- strict Hindsight recall tag scope remains configurable;
- the deterministic Hindsight fixture can reject stale or cross-scope markers.

The O1 contract also asserts that the retired O3 workflow, shell harness and dedicated contract do not reappear accidentally.

## Changed

Removed:

- `.github/workflows/implementation-hindsight-obsidian-hermes-o3-lab.yml`
- `implementation/tools/run_hindsight_obsidian_hermes_o3.sh`
- `implementation/tests/test_hindsight_obsidian_hermes_o3_contract.py`

Updated:

- `implementation/tests/test_hindsight_hermes_o1_contract.py`

## Not changed

- no external pin;
- no provider selection or adoption;
- no branch-protection/ruleset setting;
- no current O1/O2, LiveSync, Langfuse or Obsidian-wiki qualification harness;
- no runtime, persistence, Evidence, memory or authorization behavior.

## Boundaries

```text
pull_request-triggered != required merge check
historical qualification != current target
historical evidence != live executable fixture
green lab != qualification
deleting a live fixture != deleting provenance
retrieved != truth
memory != Evidence
runtime success != authorization
```

## Follow-up boundary

Pin-change fan-out remains a separate CI-cost/currentness question. It should not be solved by inventing a merge-blocking registry for workflows that the active ruleset does not require.
