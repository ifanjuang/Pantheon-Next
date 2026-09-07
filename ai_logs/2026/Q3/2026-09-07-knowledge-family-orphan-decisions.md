# Two of #989's three orphan categories resolved by maintainer decision

Date: 2026-09-07

Status: candidate — partial maintainer decision recorded; full reconciliation
of #989 remains open.
Boundary profile: candidate_support_note.

## Change

- Updated: `docs/domain-packs/architecture/KNOWLEDGE_REGISTRY_BLUEPRINT.md` —
  `supplier_product` and `lesson_learned` removed from the candidate category
  list, each with a stated reason; `precedent` marked explicitly still open;
  the list itself stated as illustrative rather than a frozen enumeration.
- Removed: nothing else. No schema, no code, no `knowledge_family` enum value.

## The two decisions, as given

**`supplier_product` is not a Knowledge family. It belongs to Document,
project-scoped.** A supplier's technical sheet for a specific piece of
equipment is not reusable interpretation carried across projects — it is a
source-backed record tied to one affair, one lot, one piece of equipment.
`AGENCY_DOMAIN_PACK.md` already defines exactly this shape under "Documents and
versions" and its "DOE equipment item" specialized extension
(`equipment_tag`, `system_type`, `serial_number`, `manual_document_id`, …).
Checked before writing this: no new field, schema or owner was needed: the
category is declared out of Knowledge's scope, not migrated into a new home.

**`lesson_learned` does not exist as a category this practice needs.** Declared
out of scope outright, not mapped elsewhere. It was never enforced by the
schema, so this changes nothing executable — only removes a documented
placeholder that had no real referent.

Both were stated as illustrative placeholders from the blueprint's first draft
rather than categories a maintainer had reviewed and confirmed — removing them
here is that review, not a reversal of an accepted decision.

## What remains open, unchanged

`precedent` — the third orphan — has no owner yet and is marked explicitly
open rather than silently resolved by omission. The core #989 question — which
vocabulary governs where the enforced enum and the blueprint's surviving three
categories (`regulation`/`reglementations`, `construction_detail`/`techniques`,
`agency_standard`/`methodologie`) diverge in naming — is untouched. This entry
does not choose option A, B, C or D from #989; it resolves two of the six
original items on the list, independent of which option is eventually chosen
for the rest.

## Boundary

Boundary profile applies: `candidate_support_note`.

Protected paths touched: no.
Runtime impact: none. No schema, contract or code changed; `knowledge_family`
never enforced either removed category, so nothing that previously wrote
successfully can now fail.
Authority impact: none gained. The blueprint remains candidate status; removing
two placeholder categories does not promote it, and the reconciliation with the
enforced enum remains exactly as open as before.
Schema/test/CI impact: none.
External action: none.
Memory behavior: none.

## Verification

```text
tests/                                    678 passed
check_status_headers.py                   OK
check_internal_links.py                   OK
check_no_truncation.py                    OK
check_obsolete_authority_consistency.py   OK
check_ai_logs_index_current.py            OK
check_index_coverage.py                   OK
```

## Local distinctions

```text
placeholder category   != reviewed category
out of Knowledge scope != unowned
partial decision       != full reconciliation
illustrative list      != frozen enumeration
```
