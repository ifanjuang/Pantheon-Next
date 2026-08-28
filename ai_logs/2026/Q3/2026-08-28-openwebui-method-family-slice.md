# OpenWebUI method-family convergence — 2026-08-28

## Objective

Continue #785 from merged main `76558c619caba6872cb35f07ed7d241cfe3fd7f2` with a larger but still owner-coherent method/execution-discipline slice. Retire present-tense OpenWebUI ownership without replacing it with Hermes WebUI and reduce the machine-tracked allowlist from 28 paths to 25.

## Scope

- `docs/governance/ADAPTIVE_REQUEST_METHOD.md`
- `docs/governance/WORKFLOW_FORGING_PROTOCOL.md`
- `docs/governance/EXECUTION_MINIMALISM.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel #785 PR was open when this slice started.

## Owner review

The three documents retain distinct current responsibilities:

- adaptive proportional treatment of requests;
- forging and pre-launch status of Workflow Candidates;
- reliability-first execution growth and anti-overengineering discipline.

The broader documentation overlap remains deferred to #787. No merge, rename, status reclassification or topology change is performed here.

`HERMES_INTEGRATION.md` remains the stable owner of runtime/client/authority placement and PDP/PEP integration.

## Convergence

The three owners no longer assign present-tense exposure/decision ownership to OpenWebUI. They inherit the generic integration split instead:

```text
compatible runtime client = optional interaction surface
Hermes / external runtime = execution
Pantheon Cockpit = governed projection where applicable
Pantheon = governance authority
client selection != authority transfer
```

`EXECUTION_MINIMALISM.md` also replaces two current product-specific examples (`Human conflict` placement and the single-display-surface growth example) with client-agnostic runtime/Cockpit wording. This preserves the capability while removing obsolete product ownership.

Hermes WebUI is not introduced as a required replacement.

## Preserved invariants

```text
retrieved != truth
memory != Evidence
runtime success != authorization
runtime output != Evidence
projection != persistence
client selected != governance authority
PDP decision != PEP execution
runtime approval UI != Pantheon human approval
```

## Boundary

Documentation and regression-only convergence. No runtime, API, schema, persistence, provider, installation, approval, memory or external-effect behavior changes.

No long document was truncated or substantially reduced, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent change invalidates prior check evidence. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact published head and reviews/threads/comments have been read.
