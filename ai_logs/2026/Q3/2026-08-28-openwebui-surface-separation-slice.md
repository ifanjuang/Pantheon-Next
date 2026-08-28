# OpenWebUI surface-separation convergence — 2026-08-28

## Objective

Continue #785 from merged main `dd6809f8325fc833d313bd3909be4b95d213080a` with a bounded surface-separation slice. Retire present-tense OpenWebUI ownership by distinguishing runtime interaction from Pantheon Cockpit governed projection, reducing the machine-tracked allowlist from 23 paths to 21.

## Scope

- `docs/governance/PROMPT_PLACEMENT.md`
- `docs/governance/PRE_EXECUTION_SIMULATION.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Owner review

`PROMPT_PLACEMENT.md` remains the owner for prompt placement and authority separation across doctrine, runtime and observability layers.

`PRE_EXECUTION_SIMULATION.md` remains the owner for governed pre-execution simulation and its evidence/approval effects.

Neither responsibility is merged or reclassified. Broader documentary convergence remains deferred to #787.

## Convergence

The two documents now use the current split:

```text
Pantheon doctrine = governance source
Pantheon Cockpit = governed projection / decision visibility
compatible runtime client = optional runtime interaction
Hermes / external runtime = execution
human = consequential decision when required
```

Prompt placement now distinguishes Cockpit projection instructions from runtime-client prompts.

Simulation now distinguishes runtime execution state from governed simulation/decision state. A runtime-client approval control does not become Pantheon approval, and a simulation pass does not authorize execution.

No Hermes WebUI dependency or replacement owner is introduced.

## Preserved invariants

```text
runtime interaction != governed projection
projection != approval
projection != persistence
runtime approval UI != Pantheon human approval
runtime success != authorization
runtime output != Evidence
PDP decision != PEP execution
```

## Boundary

Documentation and regression-only convergence. No runtime, API, schema, persistence, provider, installation, approval, memory or external-effect behavior changes.

No long document was truncated or substantially reduced, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior check evidence. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact published head and reviews/threads/comments have been read.
