# OpenWebUI editorial convergence — 2026-08-28

## Objective

Continue #785 from merged main `58ef38bfcbc8e884fc46ba1638a71be86255fef1` with a bounded editorial slice. Remove current OpenWebUI ownership from the public-language guide while preserving its editorial responsibility. Reduce the machine-tracked allowlist from 9 paths to 8.

## Scope

- `docs/governance/EDITORIAL_LANGUAGE.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Observed need

`EDITORIAL_LANGUAGE.md` still carried the old `OpenWebUI exposes / Hermes executes / Pantheon governs` architecture block even though the document is only an editorial owner. Repeating product-specific architecture inside public-language guidance creates a competing formulation and can make a replaceable client look canonical.

## Owner review

`EDITORIAL_LANGUAGE.md` remains the owner for public-facing language and vocabulary. `HERMES_INTEGRATION.md` remains the stable runtime/client/PDP/PEP boundary owner. The editorial guide consumes that boundary only when technical placement must be explained.

## Overlap analysis

The slice does not redefine public messaging, slogans, terminology policy, runtime placement, Cockpit ownership, Task Contracts, PDP or PEP. It removes one duplicated architecture formulation and replaces it with a reference to the existing integration owner plus an editorial consequence: public copy must not turn a client or UI into governance authority.

## Affected consumers

Maintainers drafting public-facing Pantheon text, documentation reviewers, and the #785 regression are affected. No executable consumer changes.

## Convergence

Technical architecture is no longer restated product-specifically in the editorial owner. The guide inherits compatible runtime-client interaction, external runtime execution, Cockpit projection and Pantheon authority from `HERMES_INTEGRATION.md` while keeping its own responsibility limited to language.

## Migration and rollback

Documentation-only change. No runtime, client, data, schema or persistent state migration exists. Rollback is a normal Git revert.

## Role / Rite / Space

- Role: MNEMOSYNE for wording continuity, with THEMIS authority-boundary review.
- Rite: Concordance des sources across exact main, #785, the regression and `HERMES_INTEGRATION.md`.
- Space: Pantheon Next governance repository.

These labels describe review context only and create no runtime state.

## Authority impact

None. The editorial guide does not become an architecture owner. Compatible clients remain optional interaction surfaces, Pantheon Cockpit remains governed projection, Pantheon retains governance authority and the policy/runtime boundary remains owned elsewhere.

## Runtime impact

None. No runtime, client, adapter, provider, external effect, approval or deployment behavior changes.

## Preserved invariants

```text
editorial explanation != architecture ownership
client selected != governance authority
runtime interaction != governed projection
projection != persistence
runtime success != authorization
```

## Boundary

Documentation and regression-only convergence. No API, schema, persistence, provider, approval or memory behavior changes.

No long document was truncated or substantially reduced; `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior checks. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the final exact head and reviews/threads/comments have been read.
