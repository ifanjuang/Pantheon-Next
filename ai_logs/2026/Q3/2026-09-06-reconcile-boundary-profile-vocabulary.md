# The drift had one cause: no term for what a document *is*

Date: 2026-09-06

Status: implemented — `BOUNDARY_PROFILES.md` defines three profiles it lacked,
seven live documents drop subject labels for role labels, and non-conforming
live declarations reach zero. Resolves #1000.
Boundary profile: active_support_doctrine.

## Change

- Updated: `docs/governance/BOUNDARY_PROFILES.md` — a new rule section
  ("A profile classifies the document, not its subject") and three profile
  definitions: `active_governance_doctrine`, `external_reference_review`,
  `bounded_implementation_change`. 7 profiles -> 10.
- Updated: 7 documents, one line each — see the table below.
- Updated: `tests/test_boundary_profile_vocabulary_conformance.py` —
  `KNOWN_UNDEFINED_PROFILE_DECLARATIONS` emptied. The ratchet stays as the floor.
- Removed: no document, no profile, no test.

## Why the fix is a rule, not nineteen renames

#1000 listed 19 undefined names and sorted them into seven classes. Reading the
ten live documents together collapsed most of that list to one cause.

Every free-form label described what the document was **about**, never what it
**was**:

```text
external runtime adapter                       REVIT_LOCAL_ADAPTER.md
architecture source adapter specialization     DRAWING_TAKEOFF_LOCAL_ADAPTER.md
architecture_project_understanding_projection  PROJECT_ANATOMY_MODEL.md, +1
projection_definition                          CARD_PROJECTION_DEFINITION_MODEL.md
external_capability_review                     EXTERNAL_TOOLS_POLICY.md
external_runtime_integration                   HERMES_INTEGRATION.md
```

`EXTERNAL_TOOLS_POLICY.md` is the clearest case. Its status is *active support
doctrine*; it is a policy that governs how external tools are treated. It is not
a review of an external tool. `external_capability_review` labels its subject and
misstates its role — and by doing so it silently claims `installed: false,
adopted: false` about a document that adopts nothing because it is a policy.

So the cure is one sentence in the owner: **choose the profile from what the
document is and does, never from what it is about.** A subject belongs in the
title and the `Status:` line. Without that sentence the vocabulary will drift
again the moment a document's subject has no matching noun.

## The two real gaps, and one that was not

Two classes in #1000 were genuine holes rather than sloppiness, and both are now
defined using names already in use:

- `active_governance_doctrine` — every profile asserted the document *supports*
  doctrine. Nothing covered a document that **is** it. `EVIDENCE_TOPOLOGY.md`
  (active doctrine) had invented the name rather than wait; `GLOSSARY.md`
  (canonical) hits the same hole in #996's next slice.
- `bounded_implementation_change` — every profile asserted
  `implementation: false` / `runtime: false`, so a change under `implementation/`
  could not honestly declare any of them. Fourteen declarations invented one.

`external_reference_review` (5 uses) was adopted as a third: reviewing an
external thing without adopting it is a distinct, recurring, doctrinally loaded
act, and `AGENT_PLUGINS_INTEROPERABILITY.md` and `HERMES_RUNTIME_SURFACE_REVIEW.md`
are genuinely that.

Projection was **not** a gap. `projection_definition` and
`architecture_project_understanding_projection` looked like a missing concept and
were subject labels: those documents are active support doctrine and candidate
support notes respectively. The non-equivalence that matters there
(`projection != authorization`) is doctrine content, not a boundary claim. Three
declarations converged; nothing was defined.

## Convergence table

```text
DRAWING_TAKEOFF_LOCAL_ADAPTER.md          -> candidate_support_note
PROJECT_ANATOMY_KNOWLEDGE_STRUCTURE.md    -> candidate_support_note
PROJECT_ANATOMY_MODEL.md                  -> candidate_support_note
REVIT_LOCAL_ADAPTER.md                    -> candidate_support_note
CARD_PROJECTION_DEFINITION_MODEL.md       -> active_support_doctrine
EXTERNAL_TOOLS_POLICY.md                  -> active_support_doctrine
HERMES_INTEGRATION.md                     -> active_governance_doctrine

EVIDENCE_TOPOLOGY.md                      unchanged, now defined
AGENT_PLUGINS_INTEROPERABILITY.md         unchanged, now defined
HERMES_RUNTIME_SURFACE_REVIEW.md          unchanged, now defined
```

Each document keeps its `Status:` line, its title and every local boundary
section. Only the profile line moved.

## Traces were not rewritten, and twelve became conformant anyway

```text
before   27 non-conforming declarations in ai_logs/
after    15
```

Not one `ai_logs/` entry was edited. Defining three profiles that were already in
use made twelve historical traces conformant on their own — which is the argument
for adopting observed names rather than inventing tidy ones.

The remaining 15 stay as written: three `implementation_artifact`, one
`bounded_ci_authority_repin`, one `bounded_governance_support_change`, three
`validation_only` and two `candidate_support_doctrine` (near-miss typos, mine),
and five free-form phrases. A past entry's declared profile is part of what that
intervention recorded about itself. #1000's non-goals protect them, and the
conformance test does not govern `ai_logs/`.

## The two unused profiles were kept

`schema_contract` and `read_only_verification_surface` still have zero
declarations. Retiring them now would be backwards: #996 has 112 documents left
to place, and they include schema notes and the `mcp-server/docs/` read-only
surfaces these two describe. Re-check after that migration, when the question has
evidence behind it.

## Boundary

Boundary profile applies: `active_support_doctrine`.

Protected paths touched: no.
Runtime impact: none — documentation and one test constant.
Authority impact: none. Three profiles were defined and none grants anything;
`active_governance_doctrine` says so in its own text, because a profile that
could promote a document to doctrine would be an authority mechanism rather than
a boilerplate reduction. No document's `Status:` line changed, so no document
gained or lost authority.
Schema/test/CI impact: one allowlist emptied. No test added, weakened, skipped
or removed; the ratchet's two assertions are untouched and now run with no
seeded debt to hide in.
External action: none.
Memory behavior: none.

## Verification

```text
tests/                                    675 passed
check_status_headers.py                   OK
check_internal_links.py                   OK
check_no_truncation.py                    OK
check_obsolete_authority_consistency.py   OK

live declarations naming an undefined profile:  10 -> 0
profiles defined by the owner:                   7 -> 10
```

The floor was mutation-checked after the list was emptied: reintroducing a
subject label (`Boundary profile: revit adapter specialization.`) failed
immediately on `unexpected`, naming the file. Reverted, tree clean.

## Local distinctions

```text
about a subject     != is that subject
name adopted        != name invented
gap in vocabulary   != sloppiness
list emptied        != guard removed
```
