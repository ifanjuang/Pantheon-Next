# OpenWebUI rejection/provenance convergence — 2026-08-28

## Objective

Continue #785 from merged main `235c9080ef3e93b665752d2c4dc689e2672a862f` with a bounded rejection/provenance slice. Retire current OpenWebUI ownership from rejection memory and the post-pivot code-audit register while preserving product-specific historical and rejected examples. Reduce the machine-tracked allowlist from 12 paths to 10.

## Scope

- `docs/governance/REJECTED_PATTERNS.md`
- `docs/governance/CODE_AUDIT_POST_PIVOT.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Observed need

Both owners still carried the old `OpenWebUI exposes / Hermes executes / Pantheon governs` block. They also contained current status/classification or safe-alternative wording that assigned OpenWebUI an active exposure responsibility, even though other OpenWebUI mentions are legitimate rejected-pattern or historical-provenance records.

## Owner review

`REJECTED_PATTERNS.md` remains rejection memory only. `CODE_AUDIT_POST_PIVOT.md` remains the independently maintained historical runtime-audit and reclassification owner. `HERMES_INTEGRATION.md` remains the stable runtime/client/PDP/PEP boundary owner.

## Overlap analysis

No rejected pattern is promoted or removed. The slice changes only current placement vocabulary and safe alternatives. Historical endpoint/product references remain where their value is to document what was refused or observed. No new audit, adapter, client or Cockpit owner is introduced.

## Affected consumers

Maintainers reviewing rejected architecture patterns, historical predecessor assets, reclassification decisions and the #785 regression are affected. Runtime consumers are not affected.

## Convergence

`REJECTED_PATTERNS.md` now uses a generic `runtime_client_exposure_only_possible` status and a safe alternative that separates Pantheon Cockpit governed projection from compatible runtime-client interaction.

`CODE_AUDIT_POST_PIVOT.md` now classifies dashboard/runtime-client/Cockpit candidates without assigning current ownership to OpenWebUI and preserves concrete historical hard blockers such as automatic OpenWebUI database access by Hermes.

## Migration and rollback

Documentation-only vocabulary migration. No data, runtime or persistence migration exists. Rollback is a normal Git revert; historical provenance remains available in Git either way.

## Role / Rite / Space

- Role: MNEMOSYNE for provenance continuity, with THEMIS authority-boundary review.
- Rite: Concordance des sources across exact main, #785, the regression and `HERMES_INTEGRATION.md`.
- Space: Pantheon Next governance repository.

These labels describe review context only and create no runtime state.

## Authority impact

None. Rejected products remain rejected examples, not authority owners. Pantheon remains governance authority; the policy service remains the bounded PDP interface; Cockpit projection and runtime interaction remain non-authoritative.

## Runtime impact

None. No runtime, tool execution, external effect, provider, plugin, deployment, persistence, approval or memory behavior changes.

## Preserved invariants

```text
historical product reference != current architecture owner
rejected pattern != selected binding
runtime interaction != governed projection
projection != approval
runtime success != authorization
```

## Boundary

Documentation and regression-only convergence. No API or schema changes.

No long document was truncated or substantially reduced, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior checks. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the final exact head and reviews/threads/comments have been read.
