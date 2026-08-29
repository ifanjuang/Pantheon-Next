# Module Activation — owner-seam convergence — 2026-08-29

## Objective

Continue #787 from exact `main` `b8e2b98ac2e2333568b77fe6732af482882812f4` by narrowing `MODULE_ACTIVATION.md` to the activation responsibility it actually owns before deciding its final authority-index placement.

## Observed need

`MODULE_ACTIVATION.md` is active support doctrine and has current consumers, including `ROLE_ACTIVATION.md`, `MODULAR_DOMAIN_REORIENTATION.md` and convergence tests, but it is not currently present in the authority sub-indexes.

The prior document also repeated substantial doctrine already owned by:

- `UNIFORM_CAPABILITY_GOVERNANCE.md` — universal law/passport/gate;
- `CAPABILITY_PLACEMENT.md` — generic capability/effect placement;
- `TASK_CONTRACTS.md` — task scope;
- `APPROVALS.md`, `EVIDENCE_PACK.md`, `MEMORY.md` — downstream governance;
- `HERMES_CAPABILITY_BINDINGS.md` — product-specific optional binding posture;
- `HERMES_INTEGRATION.md` — runtime/client/PDP/PEP/Cockpit placement;
- Cockpit capability owners — projection and supported management actions.

It also carried long LangGraph/n8n examples and repeated UI/control lists that were not required to own activation semantics.

## Overlap analysis

After removing those repeated responsibilities, the remaining seam is independently meaningful:

```text
capability detection
-> governance activation for explicit scope
-> task authorization under Task Contract + applicable policy
-> runtime/PEP execution only after admission
```

It additionally owns activation status vocabulary, activation scope, Effective Policy composition and suspension/review semantics.

## Changes

`MODULE_ACTIVATION.md` now retains only:

- the detection / activation / task-authorization non-equivalence;
- activation statuses and scope levels;
- the rule that activation may narrow but never widen the capability passport;
- local optional switches that cannot override universal mandatory constraints;
- a compact Effective Policy composition seam;
- compact activation-record vocabulary;
- runtime-administration versus governance-activation separation;
- Cockpit projection boundary;
- suspension/review triggers;
- explicit handoffs to canonical owners.

Removed from this owner:

- duplicated universal mandatory rulebook;
- large Effective Policy YAML example;
- detailed Cockpit UI/control inventory;
- detailed Hermes administration procedure;
- capability-class catalogue;
- LangGraph and n8n examples;
- duplicate detection/activation/task-record examples;
- repeated Evidence, approval, memory and external-reference doctrine.

## Quantitative convergence

Before this ai_log:

```text
MODULE_ACTIVATION.md   +204 / -507
```

Net doctrine reduction: **303 lines**.

## Truncation acknowledgement

The deliberate reduction is large enough to trigger the existing net-truncation guard. This branch therefore adds exactly one temporary acknowledgement for `docs/governance/MODULE_ACTIVATION.md` with a bounded rationale. Guard logic is unchanged.

If this reduction merges, the acknowledgement must be removed in the subsequent owner-decision/authority-coverage slice, as the guard file itself requires.

## Affected consumers

Consumer names and the core activation semantics they rely on are preserved. No runtime, schema or test file is changed in this slice.

## Migration and rollback

No runtime/data migration. Rollback is restoration from Git history. If the narrowed seam proves not independently useful, a later #787 slice may absorb it; if it remains distinct, the next slice should repair authority-index coverage and remove the temporary truncation acknowledgement.

## Authority impact

No authority promotion. Existing authority is reduced to the local activation seam. The document remains active support doctrine while the pre-existing missing-index condition stays visible for the next owner decision.

## Runtime impact

None. No registry, installer, plugin manager, provider router, workflow engine, scheduler, queue, runtime, approval engine or memory engine is introduced.

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

Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final HEAD, the truncation guard accepts the explicit acknowledgement, and reviews/threads/comments have been read. Any later HEAD modification invalidates prior check evidence.
