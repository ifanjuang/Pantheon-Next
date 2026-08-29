# Final active-owner residue convergence

Date: 2026-08-29
Issue: #787
Base `main`: `ce8321ce074f991d81f2463b1370b48218abf6bf`
Branch: `codex/converge-final-active-owner-residues`

## Objective

Complete a bounded readiness slice for #787 by removing or demoting active-support documents that still duplicated an existing owner, without creating a new governance document, schema, runtime component or parallel authority path.

## Observed residues

### `BOUNDARY_STANDARD.md`

The file claimed to be the single standard non-implementation boundary, while `BOUNDARY_PROFILES.md` already owns reusable boundary vocabulary and the repository contribution rules already instruct maintainers to use those profiles. Current code search found no current consumer of `BOUNDARY_STANDARD.md` beyond its historical intervention log.

Disposition: remove the duplicate owner. Git history preserves provenance.

### `SKILL_WATCHLIST.md`

The file was active support doctrine and repeated the general observation/adoption/approval boundary already owned by `WATCHLIST.md`, while also carrying long source-specific watch records.

Disposition: demote it to a compact, non-authoritative specialized reference view. `WATCHLIST.md` remains the owner of observation policy, statuses and routing. Useful source signals remain listed compactly; detailed historical analyses remain in Git history.

### `RAG_INGESTION_PIPELINE.md`

The file claimed provider-agnostic ingestion/retrieval ownership that is already covered by `SOURCE_INGESTION_RETRIEVAL_MODEL.md`. Its implementation-profile material is observational and belongs with the existing implementation-coverage inventory. `RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` separately owns the post-retrieval Evidence interpretation.

Disposition: demote the path to a compact compatibility/profile pointer and update the Evidence-boundary document to point directly to the real source/retrieval doctrine owner.

## Distinct owners deliberately retained

The readiness audit did not re-absorb documents whose prior convergence work already demonstrated an independent responsibility:

- `ROLE_ACTIVATION.md`: role/domain/skill participation and eligibility semantics, with targeted regression tests;
- `DOCTOR_MODULE_SPEC.md`: audit-only Doctor boundary and output contract;
- `EDITORIAL_LANGUAGE.md`: public-facing language and vocabulary;
- `ROADMAP.md`: outcome-oriented repository roadmap subordinate to the status spine;
- `WHAT_RUNS.md`: runtime-status honesty map in the active status spine;
- `SOURCE_NEED_AND_REGISTRY.md`: missing-source, source-route and freshness method, recently reviewed again through #818.

This distinction matters: reducing documentation debt must not delete a useful responsibility merely because it composes other owners.

## Change

- remove `docs/governance/BOUNDARY_STANDARD.md`;
- reduce `docs/governance/SKILL_WATCHLIST.md` to a non-authoritative specialized reference view;
- reduce `docs/governance/RAG_INGESTION_PIPELINE.md` to a non-authoritative compatibility/profile pointer;
- update `docs/governance/RAG_INGESTION_AND_EVIDENCE_BOUNDARIES.md` so source/retrieval doctrine points to `SOURCE_INGESTION_RETRIEVAL_MODEL.md` and implementation status points to `SOURCE_RETRIEVAL_IMPLEMENTATION_COVERAGE.md`;
- add the required deliberate-reduction acknowledgment for `SKILL_WATCHLIST.md`; no CI logic is changed.

## Preserved boundaries

```text
reference view != authority
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
implementation coverage != adoption
```

No new current-authority Markdown owner, capability family, schema, router, store, scheduler, runtime path or provider dependency is introduced.

## Validation

The branch starts from exact `main` `ce8321ce074f991d81f2463b1370b48218abf6bf`. Pull-request CI must validate the exact final head before merge. After merge, #787 still requires a final criterion-by-criterion closure audit; this log does not close the umbrella issue by itself.
