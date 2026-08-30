# 2026-08-30 — compose #827 review through existing currentness retrieval

## Objective

Advance the first professional-value vertical #827 with the smallest executable convergence justified by current `main`: make the existing stand-in review runner able to use the already-owned access + professional-currentness + exact-source retrieval composition before drafting.

No new ACT engine, retrieval owner, currentness owner, Evidence owner, schema, runtime, parser or model binding is introduced.

## Exact repository state

Final branch base after revalidation:

```text
main = 79fb8f028cac747bb6f825e03d89f99c851e74de
```

Observed before final reconstruction:

- #849 is merged and the nine-case human-labelled professional quote-review corpus is already on `main`;
- #824 is closed; its evaluation pilot remains blocked on a reproducible qualified runtime rather than on missing evaluation doctrine;
- #853, #854 and #856 are merged;
- #856 records a separate observed Obsidian graph-health qualification and does not overlap this review/runtime seam;
- no other open PR owned this #827 composition when the final branch was reconstructed;
- `implementation/mvp_vertical/retrieval_scope.py` already composes project access, project-document access, professional currentness, exact preserved source identity and digest-exact hybrid retrieval;
- `implementation/mvp_vertical/runner.py` still used the older Task-Contract-scoped hybrid retrieval path directly.

The observed executable gap was therefore composition through an existing stronger seam, not missing architecture.

## Change

`implementation/mvp_vertical/runner.py` now exposes one additional project-aware entry point:

```text
run_accessible_applicable(...)
```

Its path is:

```text
Task Contract + authenticated principal + requested Project Documents
-> existing human access owner
-> existing professional currentness owner
-> exact document_version_id
-> preserved source_ref + source_digest + source_version
-> existing digest-exact hybrid ranking
-> existing drafting / claim-support / Evidence Candidate path
```

The historical `run()` entry point remains unchanged in responsibility and continues to support the existing stand-in/tests.

The common post-retrieval drafting path was factored only enough to avoid duplicating the current candidate/Evidence logic.

## Fail-closed behavior

The project-aware entry point converts existing scope-resolution failures into bounded refusals before drafting:

```text
outside declared perimeter  -> refusal
currentness unresolved       -> refusal
currentness conflicting      -> refusal
access denied                -> refusal
scope resolution unavailable -> refusal
```

A forbidden external-send request still refuses before project/document lookup.

No scope-resolution exception is treated as permission to fall back to a newer path, source-only lookup or model knowledge.

## Provenance projection

When currentness resolves, the Evidence Pack Candidate carries a `source_scope_resolution` observation containing:

```text
project_id
document_id
purpose
document_version_id
source_ref
source_digest
source_version
basis_refs
```

This is additive under the existing schema's extensible Evidence Pack shape; no schema change is required.

Required distinction:

```text
resolved for retrieval != professional approval
resolved for retrieval != Evidence admission
currentness basis != model truth
source digest != governed document identity
runtime output != Evidence
```

The projection explicitly declares that it cannot approve, admit Evidence or widen the Task Contract.

## Regression coverage

`implementation/tests/test_runner_project_scope.py` covers:

1. delegation to the existing currentness/retrieval seam and preservation of exact revision/digest provenance;
2. unresolved currentness refusing before drafting;
3. forbidden external-send intent refusing before any project-scope lookup.

The existing `run()` behavior and ranking constants are not changed by this slice.

## Deliberate non-change

This branch does not:

- execute or claim success on the nine-case #827 professional oracle;
- create a professional finding ontology;
- change retrieval ranking, RRF weights or thresholds;
- assign contractual authority to filenames, source paths or highest revisions;
- modify `project_document_currentness` semantics;
- alter the Task Contract schema or Evidence schema;
- wire Hermes or another model runtime;
- promote any candidate to Evidence or professional approval.

## Done criterion for this slice

The slice is complete when the exact branch head passes the focused runner/currentness tests and repository CI, and review confirms that the new path only composes existing owners.

A green test proves the composition seam behaves as specified; it does **not** prove the professional quote-review corpus is behaviorally solved.

Next #827 work should execute the nine-case corpus through an actual bounded drafting/runtime seam and let the first observed professional failure choose the next correction layer.
