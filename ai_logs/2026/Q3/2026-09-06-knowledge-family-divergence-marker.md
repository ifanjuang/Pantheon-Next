# The architecture Knowledge blueprint names a vocabulary the schema refuses

Date: 2026-09-06

Status: implemented — `KNOWLEDGE_REGISTRY_BLUEPRINT.md`'s category section is
marked `to verify`, states the enforced vocabulary alongside its own, and
corrects an unverifiable alignment claim. The taxonomy decision itself is
deferred to #989 and not taken here.
Boundary profile: candidate_support_doctrine.

## Change

- Updated: `docs/domain-packs/architecture/KNOWLEDGE_REGISTRY_BLUEPRINT.md`,
  "What the registry holds" section only.
- Added: issue #989 (maintainer decision, four options with cost/consequence/risk).
- Removed: nothing. No category was renamed, added or deleted; no schema,
  code or enum was touched.

## Why

Two independent subject taxonomies existed for architecture Knowledge, neither
referencing the other:

```text
enforced   schemas/document_knowledge_slice.schema.yaml:80-87 -> knowledge_family enum
           implementation/mvp_vertical/knowledge.py:29 enforces it, :347 refuses the rest
           referentiels, responsabilite, methodologie, techniques, reglementations

documented KNOWLEDGE_REGISTRY_BLUEPRINT.md "What the registry holds"
           regulation, agency_standard, construction_detail,
           lesson_learned, supplier_product, precedent
```

Three approximate correspondences under different names and languages, two
enforced families absent from any doctrine, and three documented categories
with nowhere to be stored. A reader following the blueprint would author a
Knowledge item and have it refused at write time, with nothing in the document
warning them.

## What was corrected beyond the marker

The blueprint claimed *"Categories align with `docs/governance/KNOWLEDGE_TAXONOMY.md`;
they extend it for the architecture domain."* That claim cannot hold as written:
`KNOWLEDGE_TAXONOMY.md` (active doctrine) defines governance-lifecycle categories
— `Raw Source`, `Source Reference`, `Knowledge Item`, `Retrieved Knowledge`,
`Working Context`, `Evidence Item`, … — and defines no subject-matter family axis
at all. The axis the blueprint claimed to extend does not exist in the owner it
named. The wording now says the blueprint specializes the architecture domain
*alongside* that owner rather than extending an axis it does not own.

This correction is a statement of fact, not a taxonomy decision. It would be
true under any of #989's four options.

## Why the decision was deferred rather than taken

`CLAUDE.md` makes Markdown authoritative over code unless code is demonstrably
better, in which case the reconciliation must be proposed explicitly. Here the
enforced vocabulary is the undocumented one and no design rationale for the five
families is recorded anywhere in the repository — so neither side can be adopted
silently without violating that rule.

Choosing now would also repeat the move #978 and #984 deliberately refused for
relation semantics: adding vocabulary before a demonstrated need. #827 is the
instrument that would demonstrate which categories real professional review work
actually requires. Until it runs, the honest state is a recorded divergence, not
a resolution.

## What this does not fix

`lesson_learned`, `supplier_product` and `precedent` still have no owner.
`agency_information.py` carries no fixed category enum, so Information could
absorb them without a schema change — that possibility is recorded as an option
in #989, not exercised.

## Boundary

Boundary profile applies: `candidate_support_doctrine`.

Protected paths touched: no.
Runtime impact: none — documentation only. No enum, schema or validation changed.
Authority impact: none gained. The blueprint's categories remain candidates and
are now explicitly marked as not the validated vocabulary.
Schema/test/CI impact: no schema change; no test added or modified.
External action: none.
Memory behavior: none.

## Verification

```text
check_status_headers.py    OK
check_internal_links.py    OK
check_no_truncation.py     OK
tests/                     656 passed
```

The enum was read at `schemas/document_knowledge_slice.schema.yaml:80-87` and
its enforcement at `implementation/mvp_vertical/knowledge.py:29,347`. The absence
of the three orphan categories from every owner was checked across
`implementation/mvp_vertical/` and `docs/governance/`.

## Local distinctions

```text
enum enforced        != vocabulary governed
documented category  != storable family
alignment claimed    != alignment verifiable
divergence recorded  != divergence resolved
```
