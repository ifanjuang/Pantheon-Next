# OpenWebUI support-boundary convergence — 2026-08-28

## Objective

Continue #785 from merged main `f128662a68614ce35e89a3998faac8c2dfc0be81` with a bounded support-boundary slice. Retire obsolete present-tense OpenWebUI ownership from two current-support owners and reduce the machine-tracked allowlist from 18 paths to 16.

## Scope

- `docs/governance/DOCTOR_MODULE_SPEC.md`
- `docs/governance/HERMES_INTEGRATION_MODELS_RECONCILIATION.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Owner review

`DOCTOR_MODULE_SPEC.md` remains the audit-only Doctor boundary and output-contract owner.

`HERMES_INTEGRATION_MODELS_RECONCILIATION.md` remains an active-support reconciliation note for the run-admission and per-effect chokepoint models.

`HERMES_INTEGRATION.md` remains the stable owner of runtime/client/PDP/PEP placement. No #787 structural consolidation is performed.

## Convergence

Doctor now distinguishes:

```text
compatible runtime client = runtime interaction / candidate exposure only
Pantheon Cockpit = governed projection of audit status and decision material
Hermes / external runtime = admitted audit preparation / execution
Pantheon = governance authority
```

A Doctor report remains candidate material. Runtime interaction is not governed projection; projection is not approval or persistence.

The integration-model reconciliation now inherits the same stable boundary and names the Pantheon policy service as the bounded PDP interface rather than assigning a current exposure role to OpenWebUI.

No Hermes WebUI dependency or replacement owner is introduced.

## Preserved invariants

```text
runtime interaction != governed projection
projection != approval
projection != persistence
PDP decision != PEP execution
runtime success != authorization
runtime output != Evidence
client selected != governance authority
```

## Boundary

Documentation and regression-only convergence. No runtime, API, schema, persistence, provider, approval, memory or external-effect behavior changes.

No long document was truncated or substantially reduced, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior check evidence. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact published head and reviews/threads/comments have been read.
