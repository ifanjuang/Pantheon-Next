# Converge LangGraph runtime candidate boundary

Date: 2026-08-27
Issue: #666
Role: architecture convergence
Rite: compatibility retirement
Space: Hermes optional runtime candidate
Change level: semantic

## Objective

Remove the historical OpenWebUI binding from the optional LangGraph runtime candidate while preserving useful checkpoint, interrupt, tool, Evidence and memory boundaries.

## Observed state

The current candidate remained explicitly optional behind Hermes Agent, but still assigned exposure/interruption to OpenWebUI, depended on `OPENWEBUI_INTEGRATION.md`, named OpenWebUI Knowledge/database inputs and used an OpenWebUI Function anti-pattern. Those product-specific references were no longer consistent with the selected architecture.

## Change

- retain LangGraph only as a not-installed, not-implemented, replaceable Hermes runtime candidate;
- keep Hermes Agent as execution owner under Task Contract;
- route runtime-facing status/interrupt controls to compatible Hermes clients;
- route consequential governed status/gates to Pantheon Cockpit and existing governed projection owners;
- remove the OpenWebUI integration pointer and product-specific input/function assumptions;
- preserve checkpoint continuity, Task Contract constraints, tool admission, runtime-memory separation, Evidence boundaries and User Decision Gate escalation;
- prefer the simpler existing Hermes execution path whenever graph state has no demonstrated need;
- add targeted regression tests.

Historical earlier `ai_logs/` and dated audits are unchanged.

## Invariants

```text
runtime backend selected != authority transfer
client selected != governance authority
runtime success != authorization
projection != persistence
memory != Evidence
```

## Exit criteria

No active OpenWebUI owner remains in the LangGraph candidate; the generic optional runtime capability remains; no new runtime or owner is added; all relevant CI checks are green on the exact PR head.
