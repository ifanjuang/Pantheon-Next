# OpenWebUI exposure/example convergence — 2026-08-28

## Objective

Continue #785 from merged main `ed88fb263e4ac6609ec6f62cf4b895d6c790b43e` with a bounded exposure/example slice. Retire current OpenWebUI ownership from reference-boundary doctrine and active rite examples, reducing the machine-tracked allowlist from 14 paths to 12.

## Scope

- `docs/governance/REFERENCE_BOUNDARIES.md`
- `docs/governance/rites/RITE_EXAMPLES.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Owner review

`REFERENCE_BOUNDARIES.md` remains the owner for controlling what Pantheon may distill from external references without importing runtime responsibility.

`rites/RITE_EXAMPLES.md` remains a fictional, non-executable support surface for demonstrating rite usage.

Neither responsibility is merged or reclassified. Broader documentation-topology convergence remains deferred to #787.

## Convergence

The reference-boundary test now requires runtime clients to remain non-authoritative interaction surfaces and Pantheon Cockpit to remain projection rather than authority or persistence.

Rite examples now distinguish governed Cockpit projection from optional runtime-client interaction. A status card, client control or Cockpit projection cannot execute a rite or convert its status into approval.

Product-specific comparative/rejected references remain when they are explicitly reference-boundary material, including references that say a product is not a replacement or that a product-specific runtime surface is forbidden.

No Hermes WebUI dependency or replacement owner is introduced.

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

Documentation and regression-only convergence. No runtime, API, schema, persistence, provider, approval, memory or external-effect behavior changes.

No long document was truncated or substantially reduced, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior check evidence. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact published head and reviews/threads/comments have been read.
