# AI Log — Authority Index Row Migration: Architecture + External References (PR C + PR D)

Date: 2026-07-05

Repository: `ifanjuang/Pantheon-Next`

## Context

User request: the authority index file is too long — how can it be separated?
This continues `docs/governance/AUTHORITY_INDEX_DECOMPOSITION_PLAN.md` after
PR A (plan, #277) and PR B (sub-index skeletons + obsolete/absent first
migration group). This intervention performs PR C (coverage validation,
recorded here) and PR D for the next two migration groups.

## PR C — Coverage validation (verified by reading, no script changed)

```text
.github/scripts/check_index_coverage.py reads only
docs/governance/AUTHORITY_INDEX.md (INDEX_REL). Consequences:

1. It scans *.md under docs/governance/ recursively; a file whose
   Status header contains "candidate" must appear (as a substring)
   in the master index text or be covered by a grouped row
   (a backticked path ending in "/" or containing "*", strictly
   under docs/governance/).
2. docs/domain-packs/** is NOT scanned. Rows for domain-pack files
   can migrate to a sub-index with no checker change.
3. Grouped-row coverage is computed from the master file only, so
   the grouped rows docs/governance/reference_reviews/,
   docs/governance/rites/, docs/governance/DATA_PLATFORM_*.md and
   docs/governance/authority/ must stay in the master index.
4. check_no_truncation.py requires AUTHORITY_INDEX.md >= 300 lines
   and its end-sentinel; check_no_net_truncation.py flags drops of
   >= 80 lines and <= 75% kept. This migration removes a net 21
   lines (423 -> 402): both checks pass without MANIFEST or
   truncation_ack changes.

Conclusion: candidate-status documents under docs/governance/ cannot
migrate until the checker is extended in a separately approved PR
(.github/scripts is approval-gated). Domain-pack rows and
non-candidate rows can migrate now.
```

## PR D — Rows migrated

```text
To docs/governance/authority/ARCHITECTURE_AUTHORITY_INDEX.md (20 rows,
copied verbatim): all docs/domain-packs/architecture/* rows of the
Current authority map. Replaced in the master index by one grouped row
docs/domain-packs/architecture/ that keeps the area visible and covers
members without an individual row.

To docs/governance/authority/EXTERNAL_REFERENCES_AUTHORITY_INDEX.md
(2 rows, copied verbatim):
- docs/governance/SPICE_REFERENCE_DISTILLATION.md (Status header has
  no "candidate": movable);
- docs/domain-packs/architecture/PROJECT_UNDERSTANDING_EXTERNAL_REFERENCES.md.

Deliberately kept in the master index, with the reason recorded in the
relevant sub-index:
- PANTHEON_REVIT_GATE.md, PANTHEON_REVIT_GATE_2027_PROTOTYPE_PLAN.md,
  PANTHEON_REVIT_GATE_DEVELOPER_DOSSIER.md (candidate Status under
  docs/governance/ -> coverage requires master-index presence);
- the grouped row docs/governance/reference_reviews/ (grouped coverage
  is computed from the master file only).

Master index updated: authority/ row note, Sub-index map prose and the
Architecture / External references rows marked populated. No authority
class or repo state changed; rows moved verbatim.
```

## Verification

```text
Run locally with GOVERNANCE_BASE_REF=origin/main:
check_index_coverage, check_internal_links, check_no_truncation,
check_no_net_truncation, check_status_headers, check_axis_vocabulary,
check_register_instances, check_vertical_slice: all pass.
check_apu_referential_integrity fails identically on the clean tree
(local ModuleNotFoundError: jsonschema) — environment, not this change.
AUTHORITY_INDEX.md: 423 -> 402 lines; end-sentinel untouched.
```

## Boundary

```text
No change to .github/scripts or any checker.
No schema, test, operation, platform, Docker, pyproject or .env change.
No authority class changed; no candidate promoted; rows moved verbatim.
Remaining migration groups (governance kernel, runtime adapters,
implementation artifacts) are blocked on the checker extension,
which needs its own approved PR.
```
