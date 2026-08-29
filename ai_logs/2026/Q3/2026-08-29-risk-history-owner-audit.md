# Risk / historical support owners — #787 audit — 2026-08-29

## Objective

Continue #787 from exact `main` `3b41f9b6ecb93fc471e35a02ec37991f51aa5599` by auditing the historical/risk family for false current owners before considering reclassification or consolidation.

## Observed need

The candidate family from #787 included:

- `TENSIONS_AND_RISKS.md`;
- `REJECTED_PATTERNS.md`;
- `DISCORDIA.md`;
- `CODE_AUDIT_POST_PIVOT.md`.

All four were read to EOF. Each still has a distinct current responsibility, but none had a row in the Governance Authority sub-index.

## Overlap analysis

### TENSIONS_AND_RISKS

Owns the persistent tension/risk taxonomy and the rule that material tension remains visible until governed resolution.

It is not interchangeable with rejection memory or divergence handling.

### REJECTED_PATTERNS

Owns explicit rejection memory: what has been refused, why, which boundary it violates and the safe alternative.

It prevents rejected architecture from returning under a new name. It is not an enforcement engine.

### DISCORDIA

Owns the material-divergence sentinel function: detecting when disagreement must not be smoothed away and recommending procedure/escalation without deciding truth or replacing ZEUS.

It is narrower than the general tension/risk taxonomy and is not a hidden debate runtime.

### CODE_AUDIT_POST_PIVOT

Although its source material is historical, the file remains a current audit method for classifying legacy or runtime-like code before reuse, deletion or reorientation. Governance CI also retains it as a mandatory audit baseline, and `docs/governance/README.md` points to it when protected code/artifacts are involved.

Therefore `active support note` remains justified; the file should not be reclassified as history-only merely because it audits historical runtime material.

## Decision

Retain all four owners unchanged and repair authority coverage only.

Add exactly four rows to `docs/governance/authority/GOVERNANCE_AUTHORITY_INDEX.md`.

## Affected consumers

No consumer content changes. Existing read paths and references remain valid.

## Migration and rollback

No runtime/data migration. Rollback is removal of the four index rows if a later convergence proves one owner is absorbed or reclassified.

## Authority impact

No promotion and no new authority class. Existing current responsibilities are made visible in the authority map.

## Runtime impact

None. No risk engine, rejection blocklist, contradiction runtime, audit worker, scheduler, queue, approval engine or external action is created.

## Exact non-log change

```text
GOVERNANCE_AUTHORITY_INDEX.md   +4 / -0
```

## Preserved invariants

```text
tension != automatic blocker
rejection memory != enforcement engine
divergence detection != truth decision
legacy audit finding != implementation approval
runtime success != authorization
memory != Evidence
projection != approval
```

## Verification rule

Merge only after Governance CI, Pantheon Architecture Audit and Obsolete Authority Consistency are green on the exact final HEAD and reviews/threads/comments have been read. Any later HEAD change invalidates prior check evidence.
