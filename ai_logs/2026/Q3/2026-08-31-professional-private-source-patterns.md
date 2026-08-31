# #827 — sanitized private-source-derived professional review patterns

Date: 2026-08-31

## Objective

Extend the existing #827 professional quote-review qualification with structural patterns observed in privately supplied real project documents, without committing those documents or creating a second review/runtime owner.

## Repository baseline

```text
main = e933ac81dd20125bc841f0990dd4a4780ec1abcf
#880 = merged; project-aware final context regression-protects CCTP + DPGF + quote coverage
#878 = merged after initial preparation; bounded multi-source research Workflow Manifest is disjoint from this #827 fixture/test slice
```

Open work was checked before the change. No open PR was found covering this #827 private-source pattern fixture or the same professional-review boundary tests.

## Existing owners reused

- `implementation/tests/fixtures/professional_quote_review_cases.yaml` remains the executable synthetic human-labelled oracle;
- `project_documents` remains the governed document/revision seam;
- `project_document_currentness` remains the purpose-specific currentness owner;
- `retrieval_scope` remains the access/currentness/exact-source composition seam;
- `runner.py` remains the current project-aware review path;
- no new ACT engine, finding ontology, parser, retriever, Evidence owner or professional approval owner is introduced.

The privacy posture follows the already-merged real-private-source qualification pattern used by the drawing M4 work: retain a sanitized structural pattern only, not the private source.

## Private-source posture

The repository does **not** retain from the motivating documents:

- source files or raw extraction;
- project/client names or identifying contact metadata;
- original file names or local paths;
- exact source/content digests;
- original dates;
- original amounts or project-specific quantities;
- original document geometry.

The fixture is intentionally insufficient to reconstruct or fingerprint the private documents.

## Sanitized patterns retained

1. a primary project document containing a stale foreign-project marker from residual template/header text;
2. an earlier technical-document state conflicting with a later pricing-document state where the later source explicitly marks a change but inter-document authority is not yet resolved;
3. a foreign contractor quote with high technical-vocabulary overlap, distinguishing accidental same-project retrieval from an explicitly authorized cross-project benchmark;
4. a prescribed item for which the available reference set does not establish a comparison quantity although the quote carries a quantity;
5. a functionally similar offered system without evidence sufficient to establish technical/regulatory equivalence;
6. pricing rows carrying mixed base/option/to-confirm/to-verify/to-measure postures that must not be flattened into one settled contractual base.

## Change

Added one companion fixture under the existing professional-review test fixtures and one focused boundary test module.

The tests protect that:

- no obvious private-source material or digest is retained;
- the fixture is explicitly non-authoritative;
- revision conflict routes to the existing currentness owner rather than revision-label heuristics;
- a foreign source is excluded from an accidental same-project review but may be compared under explicit authorized benchmark intent without relabeling its identity;
- missing reference quantity remains `requires_more_evidence` rather than becoming a fabricated mismatch;
- semantic similarity does not become technical conformity;
- option/unresolved pricing statuses are not flattened into a settled base.

## Non-equivalences preserved

```text
private pattern != private source
retrieved match != governed identity
later revision marker != currentness
selected context != truth
semantic similarity != technical equivalence
missing reference quantity != quantity mismatch
benchmark intent != same-project applicability
runtime success != professional validation
```

## What this does not prove

This change does not execute a model against the private documents and does not claim professional finding coverage, noise, usefulness or approval. The existing synthetic oracle still carries the executable behavioral expectations; these private-source-derived patterns identify additional real-world cases for future bounded behavioral qualification.

## Next decision

When a reproducible reviewed runtime is available through the existing runtime seam, instantiate the smallest necessary sanitized cases or run privately against the real source set and compare observed outputs against the existing human-labelled method. Do not introduce a new runtime merely to execute these patterns.
