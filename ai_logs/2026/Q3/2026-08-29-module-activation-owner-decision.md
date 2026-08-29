# Module Activation — owner retention and authority coverage — 2026-08-29

## Objective

Close the #787 owner test for `MODULE_ACTIVATION.md` after #812 narrowed it on exact merged `main` `cb1e371ab3c1760cb6af4264b563b3e270d5c278`.

## Observed need

#812 deliberately removed 303 net lines of duplicated capability, Evidence, approval, memory, binding, Cockpit and runtime doctrine from `MODULE_ACTIVATION.md` and passed Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency on its exact final HEAD.

After that narrowing, the document still owns a distinct seam:

```text
capability detection
-> scoped governance activation
-> task authorization under Task Contract + applicable policy
-> runtime/PEP execution only after admission
```

It also owns activation status/scope vocabulary, Effective Policy composition and suspension/review semantics.

## Overlap analysis

The remaining owner is distinct from adjacent capability documents:

```text
UNIFORM_CAPABILITY_GOVERNANCE.md
  -> universal capability law, passport and gate

MODULE_ACTIVATION.md
  -> current activation state and scope before task use

HERMES_CAPABILITY_BINDINGS.md
  -> product-specific optional binding selection posture

TASK_CONTRACTS.md + Pantheon policy
  -> task-specific admissibility and bounded policy decision

HERMES_INTEGRATION.md
  -> runtime/client/PDP/PEP/Cockpit boundary
```

Absorbing activation into the uniform owner would mix universal law with lifecycle/state specialization and would recreate the multi-responsibility shape #812 just removed.

## Decision

Retain `MODULE_ACTIVATION.md` as a distinct active support owner subordinate to Uniform Capability Governance.

Add one row to `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md` recording the existing class and documented non-implemented state.

No authority class is promoted and no runtime behavior is inferred.

## Truncation acknowledgement cleanup

#812 temporarily added `MODULE_ACTIVATION.md` to `.github/scripts/truncation_ack.txt` because the deliberate reduction crossed the guard threshold.

That reduction is now merged. The guard file explicitly requires temporary acknowledgements to be removed after the deliberate shrink merges, so this slice restores `truncation_ack.txt` to its exact pre-acknowledgement blob.

The guard logic is unchanged.

## Affected consumers

Existing consumers continue to reference `MODULE_ACTIVATION.md`; no consumer content changes are required.

The new authority row makes current ownership visible rather than changing those consumers.

## Migration and rollback

No runtime or data migration.

Rollback is removal of the single authority row. The narrowed doctrine remains independently reviewable regardless of index placement.

## Authority impact

No new authority class and no authority transfer.

The authority map now reflects an already-active owner whose responsibility was validated after convergence.

## Runtime impact

None. No capability registry, installer, plugin manager, provider router, scheduler, queue, runtime, approval engine, memory engine or external action is created or activated.

## Exact non-log change

```text
docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md   +1 / -0
.github/scripts/truncation_ack.txt                        +0 / -6
```

## Preserved invariants

```text
detected != activated
installed != activated
activated != task-authorized
task-authorized != approved
activation != execution authorization
runtime enabled != governance activated
projection != persistence
PDP decision != PEP execution
runtime success != authorization
```

## Verification rule

Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final HEAD and reviews/threads/comments have been read. Any later HEAD change invalidates earlier check evidence.
