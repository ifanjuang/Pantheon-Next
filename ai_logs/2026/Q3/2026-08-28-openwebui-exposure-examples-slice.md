# OpenWebUI exposure/example convergence — 2026-08-28

## Objective

Continue #785 from merged main `ed88fb263e4ac6609ec6f62cf4b895d6c790b43e` with a bounded exposure/example slice. Retire current OpenWebUI ownership from reference-boundary doctrine and active rite examples, reducing the machine-tracked allowlist from 14 paths to 12.

## Scope

- `docs/governance/REFERENCE_BOUNDARIES.md`
- `docs/governance/rites/RITE_EXAMPLES.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Observed need

The #785 regression still identified both files as current-authority OpenWebUI ownership residues. `RITE_EXAMPLES.md` also embedded the obsolete product ownership inside active fictional examples, so changing only its top block would leave its examples semantically inconsistent.

## Owner review

`REFERENCE_BOUNDARIES.md` remains the owner for controlling what Pantheon may distill from external references without importing runtime responsibility.

`rites/RITE_EXAMPLES.md` remains a fictional, non-executable support surface for demonstrating rite usage.

Neither responsibility is merged or reclassified. Broader documentation-topology convergence remains deferred to #787.

## Overlap analysis

The slice consumes the established client/Cockpit split from `HERMES_INTEGRATION.md` and does not create a competing integration, rite, approval or projection owner. Comparative and rejected product references remain in the external-reference owner where they are part of the subject being bounded.

## Affected consumers

Maintainers of reference reviews, rite examples, future Cockpit projections, compatible runtime-client bindings and the #785 regression are affected. No executable consumer changes.

## Convergence

The reference-boundary test now requires runtime clients to remain non-authoritative interaction surfaces and Pantheon Cockpit to remain projection rather than authority or persistence.

Rite examples now distinguish governed Cockpit projection from optional runtime-client interaction. A status card, client control or Cockpit projection cannot execute a rite or convert its status into approval.

Product-specific comparative/rejected references remain when they are explicitly reference-boundary material, including references that say a product is not a replacement or that a product-specific runtime surface is forbidden.

No Hermes WebUI dependency or replacement owner is introduced.

## Migration and rollback

No data or runtime migration exists. The documentation now consumes the already-established integration boundary. Rollback is a normal Git revert of this bounded slice; no external or persisted runtime state requires compensation.

## Role / Rite / Space

- Role: MNEMOSYNE for owner continuity, with THEMIS boundary review.
- Rite: Concordance des sources across exact main, #785, the machine regression and `HERMES_INTEGRATION.md`.
- Space: Pantheon Next governance repository.

These labels describe review context only and create no runtime state.

## Authority impact

None. Pantheon retains governance authority; the bounded policy service remains PDP; the Cockpit remains projection; runtime clients remain non-authoritative.

## Runtime impact

None. No runtime, provider, tool execution, external effect, scheduling, queue, plugin, approval execution or deployment behavior changes.

## Preserved invariants

```text
reference observed != architecture selected
runtime interaction != governed projection
projection != approval
projection != persistence
client selected != governance authority
rite status != runtime execution
```

## Boundary

Documentation and regression-only convergence. No API, schema, persistence, provider, approval, memory or external-effect behavior changes.

No long document was truncated or substantially reduced, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

The initial #795 validation exposed missing PR review-context sections required whenever a rite owner changes. The PR body was corrected and this ai_log context update creates a fresh HEAD so CI evaluates the corrected declaration context. Any earlier checks are invalid for merge. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the new exact head and reviews/threads/comments have been read.
