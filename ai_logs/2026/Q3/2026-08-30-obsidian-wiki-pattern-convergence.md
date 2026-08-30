# 2026-08-30 — converge bounded obsidian-wiki maintenance patterns

## Objective

Review the current `Ar9av/obsidian-wiki` maintenance model against current Pantheon Next `main` and retain only behavior that fills a demonstrated gap without creating a parallel Knowledge, manifest, retrieval, provenance or approval owner.

## Current-state checks

- #848 is merged and already owns `search-before-create` plus explicit conversation consolidation in `docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`.
- `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md` already owns reusable Markdown Knowledge organization and the visible `generated_unreviewed | needs_review | reviewed | superseded` review posture.
- `docs/governance/DOCUMENT_KNOWLEDGE_SLICE_CONTRACT.md` plus `implementation/mvp_vertical/knowledge.py` already provide source refs/digests, optimistic versions, idempotent material writes and candidate edit requests for the implemented candidate Knowledge slice.
- `docs/architecture/WORKSPACE_MANIFEST_INSPECTOR_CANDIDATE.md` already owns manifestability and local package-health semantics.
- Hindsight remains the qualified/recommended optional derived retrieval provider in the current Obsidian reference profile; the generic external runtime-memory binding remains unbound.
- #852 adds Word-Smith only as optional Obsidian authoring/document-assembly UX in the same owner. That addition is preserved and does not replace or conflict with the maintenance behavior distilled here.
- #855 is merged and changes only Hermes pin assertions; it does not overlap this workspace slice.
- #849 is merged and remains confined to the professional quote-review qualification corpus; it does not overlap this workspace slice.

## External patterns reviewed

The current `Ar9av/obsidian-wiki` architecture demonstrates useful ideas including:

- staged LLM writes;
- source-delta manifest tracking;
- statement posture such as extracted/inferred/ambiguous;
- lint/dedup/cross-link maintenance;
- whole-vault equilibrium checks;
- tiered graph/query behavior.

Its current repository also has open edge cases around reserved staging paths and valid Obsidian wikilink/embed forms. Those observations support retaining maintenance as report-only by default rather than importing automatic rewrite behavior into professional workspaces.

## Convergence decision

Do not import the upstream subsystem.

The staging, source-delta ledger, lifecycle/trust and retrieval responsibilities are already covered by existing Pantheon owners or would create parallel authority if copied literally.

Retain only two additive behaviors inside the existing optional second-brain owner:

1. a bounded report-only workspace audit that may surface duplicate candidates, malformed/unresolved links, stale summaries/source refs, contradiction candidates, orphans and missing cross-links, while refusing automatic mutation;
2. lightweight narrative annotations `extracted`, `inferred` and `ambiguous` when useful for human legibility, explicitly non-authoritative and subordinate to existing Pantheon provenance/Claim/Evidence owners.

```text
audit finding != defect confirmed
duplicate candidate != merge authorization
local equilibrium != professional review completion
workspace annotation != Evidence provenance owner
```

## Deliberate non-change

This slice introduces no:

- `_staging` directory contract;
- `.manifest.json` contract;
- trust ledger;
- required frontmatter lifecycle;
- second Knowledge lifecycle;
- second provenance schema;
- graph-query/retrieval engine;
- Hindsight replacement;
- automatic contradiction reconciliation;
- automatic whole-vault rewrite;
- runtime activation or dependency on `Ar9av/obsidian-wiki`.

Word-Smith remains a separate optional authoring UX classification and is not widened by this change.

## Changed paths

Final tree:

- `docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`;
- `tests/test_workspace_organization_routing.py`;
- `ai_logs/2026/Q3/2026-08-30-obsidian-wiki-pattern-convergence.md`;
- generated `ai_logs/INDEX.md`.

## Verification target

Reconstruct the final branch on exact current `main`, keep `ai_logs/INDEX.md` equal to the repository generator output, run the focused workspace-organization regression and normal governance CI, then inspect exact-head reviews before merge.

## Status

Doctrine/regression-only. Runtime status, authority ownership and external bindings are unchanged.
