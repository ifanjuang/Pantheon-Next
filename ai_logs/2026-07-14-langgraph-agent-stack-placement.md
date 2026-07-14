# LangGraph Agent Stack external placement

Date: 2026-07-14

Status: validation-only trace — documented non-implemented.
Boundary profile: validation_only_trace.

## Change

- Added `Brescou/langgraph-agent-stack` to the External Tool Placement Register.
- Recorded the pinned upstream commit, reviewed scope and local verification status.
- Classified the repository as an external runtime reference and watchlist item, not an adopted dependency.
- Recorded reusable industrialization patterns and forbidden boundary crossings.

## Why

The repository provides useful LangGraph runtime, pack-contract, evaluation, canary, cost-control and supply-chain patterns, but it also owns orchestration, memory, providers, connectors, plugins and runtime control. The placement record prevents those execution responsibilities from being mistaken for Pantheon governance or silently duplicated beside Hermes.

## Evidence

```text
repository: https://github.com/Brescou/langgraph-agent-stack
reviewed_commit: f18b04ee78aae78abe61b694c22f1e8156dc9950
observation_date: 2026-07-14
source_review: performed
local_pytest: 801 passed, 33 skipped, 1 failed because the minimal sync omitted the optional anthropic dependency
local_lint_format: passed
local_typecheck: 0 errors, 29 optional-dependency warnings
exact_upstream_CI: not established
```

## Boundary

Boundary profile applies: `validation_only_trace`.

Protected paths touched: no.
Runtime impact: none.
Authority impact: support register updated; no doctrine promotion.
Schema/test/CI impact: none.
External action: GitHub documentation PR only; no external runtime action.
Memory behavior: none.

## Local distinctions

```text
external_reference != dependency_adopted
watchlist_item != install_instruction
runtime_success != evidence
review_recorded != approval_gate
LangGraph_control_plane != Pantheon_governance
```
