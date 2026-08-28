# OpenWebUI request/intake owner convergence — 2026-08-28

## Objective

Continue issue #785 from merged main `90e3a3cc89f731cfa436b7a29d7a511b732af589` with a bounded request/intake slice. Retire present-tense OpenWebUI ownership without replacing it with Hermes WebUI and reduce the machine-tracked allowlist from 30 paths to 28.

## Scope

- `docs/governance/REQUEST_LIFECYCLE.md`
- `docs/governance/DOSSIER_SITUATION_INTAKE.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel PR was found for these owners when the slice started.

## Owner review

`REQUEST_LIFECYCLE.md` remains the active-support owner for the governed moments of a request, cap handling, status arbitration and memory-threshold placement.

`DOSSIER_SITUATION_INTAKE.md` remains the active-support owner for the pre-workflow intake brief used to bound ambiguous professional situations.

The broader method-family overlap noted while reading these files is tracked by #787. This slice deliberately does not merge, rename, reclassify or restructure those documents.

## Convergence

Both documents now inherit runtime/client/authority placement from the existing canonical integration boundary in `HERMES_INTEGRATION.md` instead of restating `OpenWebUI exposes.`.

The wording remains client-agnostic:

```text
compatible runtime client = optional interaction surface
Hermes / external runtime = execution
Pantheon governance authority remains Pantheon
client selection != authority transfer
```

The intake owner also keeps Registre admission and consequential human decision separate from runtime/client behavior.

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
folder/dossier != governed identity
```

## Boundary

Documentation and regression-only convergence. No runtime, API, schema, persistence, provider, installation, approval engine, memory engine or external execution behavior changes.

No long document was truncated or substantially reduced; `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any modification after this slice invalidates prior CI evidence. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact published PR head and all reviews/threads have been read.
