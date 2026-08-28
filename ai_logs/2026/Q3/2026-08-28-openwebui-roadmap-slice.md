# OpenWebUI roadmap convergence — 2026-08-28

## Objective

Continue #785 from merged main `137721d939f34c2a8dfd0e5596eb2782c97ef1f2` with a bounded roadmap slice. Remove the remaining current OpenWebUI ownership from the outcome roadmap and make the first fictional external vertical compatible with no selected runtime client. Reduce the machine-tracked allowlist from 10 paths to 9.

## Scope

- `docs/governance/ROADMAP.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Observed need

`ROADMAP.md` simultaneously stated that no external binding is adopted and defined R4 with OpenWebUI as a mandatory first step plus an exact OpenWebUI version as an entry condition. The contradiction made a refused/retired product look like a selected requirement for the next external proof.

## Owner review

`ROADMAP.md` remains the outcome-oriented repository roadmap. `HERMES_INTEGRATION.md` remains the stable runtime/client/PDP/PEP boundary owner. The status spine (`STATUS.md`, `WHAT_RUNS.md`, `AUTHORITY_INDEX.md`, `MODULES.md`) remains authoritative over roadmap facts.

## Overlap analysis

The slice does not change roadmap priority order, select a client, adopt a binding, modify the R4 professional vertical, or redefine Task Contract/PDP/PEP/Cockpit owners. It only consumes the established client-agnostic integration boundary.

## Affected consumers

Maintainers selecting roadmap work, the future operator of R4, reviewers checking external-environment prerequisites, and the #785 regression are affected. No executable consumer changes.

## Convergence

The roadmap doctrine now inherits the current split from `HERMES_INTEGRATION.md`.

R4 now starts from a bounded Task Contract, treats runtime-client interaction as optional and non-authoritative, keeps Hermes/external runtime as execution, preserves candidate outputs and explicit human decision, and records a runtime-client version only when a client is actually selected.

This aligns R4 with the roadmap's own statement that no binding is adopted.

## Migration and rollback

Documentation-only migration. No runtime/client is installed, removed or configured. No data or persistent state changes. Rollback is a normal Git revert.

## Role / Rite / Space

- Role: MNEMOSYNE for roadmap continuity, with THEMIS authority-boundary review.
- Rite: Concordance des sources across exact main, #785, the roadmap status spine and `HERMES_INTEGRATION.md`.
- Space: Pantheon Next governance repository.

These labels describe review context only and create no runtime state.

## Authority impact

None. Client selection is no longer implied by the roadmap. Pantheon retains governance authority; the policy service remains bounded PDP; Hermes/external runtime remains PEP/executor; Cockpit remains governed projection; the human decides consequential effects.

## Runtime impact

None. The first fictional vertical remains documented and not executed. No client, runtime, adapter, provider, deployment or external-effect behavior changes.

## Preserved invariants

```text
roadmap intent != binding adoption
client available != client selected
client selected != governance authority
PDP decision != PEP execution
runtime success != authorization
projection != approval
```

## Boundary

Documentation and regression-only convergence. No API, schema, persistence, provider, approval or memory behavior changes.

No long document was truncated or substantially reduced. `ROADMAP.md` was read through EOF before editing, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior checks. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the final exact head and reviews/threads/comments have been read.
