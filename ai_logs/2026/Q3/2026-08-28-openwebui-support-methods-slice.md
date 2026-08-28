# OpenWebUI support-method convergence — 2026-08-28

## Objective

Continue #785 from merged main `7613760bdd1d84ed21548401ca23e0c07fde09b1` with a bounded support-method slice. Retire obsolete present-tense OpenWebUI ownership from three current-support owners while preserving their distinct governance responsibilities, reducing the machine-tracked allowlist from 21 paths to 18.

## Scope

- `docs/governance/DISCORDIA.md`
- `docs/governance/SOURCE_NEED_AND_REGISTRY.md`
- `docs/governance/evidence_topology_antipatterns/README.md`
- `tests/test_openwebui_integration_owner_retirement.py`

No parallel pull request was open when the slice started.

## Owner review

- `DISCORDIA.md` remains the material-divergence sentinel.
- `SOURCE_NEED_AND_REGISTRY.md` remains the source-need, source-route and freshness-policy owner.
- `evidence_topology_antipatterns/README.md` remains the index of documentation-level Evidence topology failure cards.

No merge, rename or status reclassification is performed. Broader documentary convergence remains deferred to #787.

## Convergence

The three owners inherit the current runtime/client/authority split from `HERMES_INTEGRATION.md` instead of restating `OpenWebUI exposes.`.

The source-registry owner also replaces the obsolete product-specific non-implementation phrase `OpenWebUI action` with the generic `runtime-client action` while preserving the rule that search/retrieval executes outside Pantheon and retrieved material is not Evidence by itself.

No product-specific historical/rejected provenance is removed merely for lexical cleanup.

## Preserved invariants

```text
retrieved != truth
source registered != Evidence
runtime output != Evidence
runtime success != authorization
client selected != governance authority
projection != persistence
```

## Boundary

Documentation and regression-only convergence. No runtime, API, schema, persistence, provider, approval, memory or external-effect behavior changes.

No long document was truncated or substantially reduced, so `.github/scripts/truncation_ack.txt` is unchanged.

## Verification rule

Any subsequent modification invalidates prior check evidence. Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact published head and reviews/threads/comments have been read.
