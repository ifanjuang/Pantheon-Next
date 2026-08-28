# OpenWebUI risk/memory convergence — 2026-08-28

## Objective

Continue #785 from merged main `bb00c1f6547e458ef34262a9d83a99443f6f2147` with a bounded risk/memory slice. Retire obsolete present-tense OpenWebUI ownership from two current-support owners and reduce the machine-tracked allowlist from 16 paths to 14.

## Scope

- `docs/governance/EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md`
- `docs/governance/TENSIONS_AND_RISKS.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Owner review

`EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` remains the generic boundary for external runtime memory, checkpoint, graph recall and observability adapters.

`TENSIONS_AND_RISKS.md` remains the persistent governance-tension and risk-taxonomy owner.

Neither responsibility is merged or reclassified. Broader documentary convergence remains deferred to #787.

## Convergence

Both owners inherit runtime/client/authority placement from `HERMES_INTEGRATION.md` rather than assigning present-tense exposure ownership to OpenWebUI.

The memory-adapter owner keeps runtime memory outside Pantheon, keeps retrieved memory as candidate material, and makes the Cockpit/runtime-client distinction explicit at the top-level boundary.

The tensions owner replaces the current `OpenWebUI becomes source of truth` risk with the generic failure mode `runtime client or Cockpit projection becomes source of truth`. The separate `OpenWebUI Knowledge` row is preserved as an external reference pressure, not as current architecture ownership.

No Hermes WebUI dependency or replacement owner is introduced.

## Preserved invariants

```text
runtime memory != Registre Probatoire
retrieved memory != proof
runtime output != Evidence
projection != authority
projection != persistence
client selected != governance authority
runtime success != authorization
```

## Boundary

Documentation and regression-only convergence. No runtime, API, schema, persistence, provider, approval, memory or external-effect behavior changes.

No long document was truncated or substantially reduced, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior check evidence. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact published head and reviews/threads/comments have been read.
