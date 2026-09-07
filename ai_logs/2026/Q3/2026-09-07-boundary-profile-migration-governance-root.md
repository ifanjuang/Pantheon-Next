# First real slice of #996: 48 docs/governance/ root documents

Date: 2026-09-07

Status: implemented — 48 documents in `docs/governance/` root declare a
`Boundary profile` and drop the redundant separation triad where it was
purely redundant. 41 entries leave #995's OpenWebUI ratchet.
Boundary profile: candidate_support_note.

## Change

- Updated: 48 files in `docs/governance/` root — one `Boundary profile:` line
  each, chosen by reading the document's Status line and framing, not by
  pattern-matching the Status text alone.
- Updated: 46 of the 48 had the generic three-line separation removed
  (`OpenWebUI exposes.` / `Hermes Agent executes.` / `Pantheon Next governs.`)
  per #998's inheritance rule.
- Updated: `tests/test_openwebui_integration_owner_retirement.py` — 41 entries
  removed from `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES`, forced by the ratchet.
- Removed: nothing else. No `Status:` line, title or protected content changed.

## The two exceptions, and why they are exceptions

**`CAPABILITY_PLACEMENT.md`** keeps its block untouched. Its fence reads:

```text
Replaceable clients expose runtime interaction.
Pantheon Cockpit/Card surfaces project governed state.
Hermes Agent executes.
Pantheon Next governs.
```

Two of its four lines are not the generic separation — "Pantheon Cockpit/Card
surfaces project governed state" is a specific claim this document makes about
its own subject. #998's rule inherits only the generic separation; a document
naming a specific surface must still state it explicitly. This file was never
in the OpenWebUI ratchet for the same reason: its first line was never
`OpenWebUI exposes.`

**`WORK_ISSUE_AND_DELEGATED_MERGE_MODEL.md`** had a fourth line —
`The human defines consequential authority.` — inside its fence, distinct from
the generic separation and specific to a document about delegated authority.
Only the first three lines were removed; the fence and the fourth line remain.

## The classification, briefly

```text
39  candidate / to verify / candidate orientation / product direction  -> candidate_support_note
 4  validation-only ...                                                -> validation_only_trace
 2  active support doctrine / addendum to active doctrine              -> active_support_doctrine
 1  canonical                                                          -> active_governance_doctrine
 1  illustrative narrative                                             -> documentation_only
 1  external pattern review, not doctrine by itself                    -> external_reference_review
```

`GLOSSARY.md` (canonical) is the case #1005 predicted when it defined
`active_governance_doctrine`: nothing before that profile covered a document
that *is* doctrine rather than one that supports it.

`TASK_CONTRACT_REVISIONS.md` is `active_support_doctrine` rather than
`candidate_support_note` on a specific reading: it is an addendum to
`TASK_CONTRACTS.md` (active doctrine), operationalizing already-accepted
doctrine rather than proposing new doctrine awaiting review — confirmed by
reading `TASK_CONTRACTS.md`'s own header before assigning this one.

`SPICE_REFERENCE_DISTILLATION.md` is `external_reference_review` rather than
`candidate_support_note`: it distills patterns from an external repository
(`Dyalwayshappy/Spice`) Pantheon has not adopted, which is exactly what that
profile is for.

## What was found and deliberately not fixed here

Six of the 48 keep their ratchet-listed residue, because removing the triad did
not make them clean — each carries a *separate* sentence naming OpenWebUI
(`OpenWebUI may expose`, `OpenWebUI may display`) outside the triad block:

```text
EVIDENCE_MEMORY_DEV_PLAN.md
MARKDOWN_DOSSIER_WORKFLOW.md
NANGO_HERMES_CONNECTOR_GATEWAY.md
PANTHEON_CONTROL_PLANE_BOUNDARY.md
TASK_CONTRACT_REVISIONS.md
UNDERSTAND_ANYTHING_HERMES_ADAPTER.md
```

This was verified, not assumed: the ratchet's own residue scan was run after
the edits, and these six are exactly the files it still flags. They correctly
remain in `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES` — delisting them would have
been a false claim the ratchet itself would not support. Fixing the prose
naming OpenWebUI in these six is #787's remaining OpenWebUI-retirement scope,
not this boundary-profile slice's.

## Remaining #996 scope

`docs/governance/` root is now fully migrated. Still open:
`docs/governance/examples/`, `rites/`, `reference_reviews/` (13), 19 files in
`docs/domain-packs/`, 13 in `docs/examples/`, 8 in `docs/assets/` (scope
decision still needed), 4 in `templates/`, and one each in `docs/roadmaps/`,
`hermes/profiles/`, `mcp-server/docs/`.

## Boundary

Boundary profile applies: `candidate_support_note`.

Protected paths touched: no.
Runtime impact: none — documentation only.
Authority impact: none gained or lost. No `Status:` line changed; every
document keeps exactly the authority class it declared before this slice.
`active_governance_doctrine` on `GLOSSARY.md` does not promote it — it was
already canonical; the profile only names what it already was.
Schema/test/CI impact: one ratchet's allowlist shrinks by 41, forced by the
mechanism rather than chosen; no test added, weakened or removed.
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

The ratchet's own residue scan was computed programmatically before and after
the edits rather than assumed: 41 files left the allowlist because they are
now genuinely clean; 6 correctly remain because a non-triad sentence still
names OpenWebUI.

## Local distinctions

```text
triad removed        != residue cleared
generic separation    != specific local claim
profile assigned      != authority changed
canonical             != promoted
```
