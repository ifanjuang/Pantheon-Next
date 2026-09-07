# Two doctrines that name the same thing had never referenced each other

Date: 2026-09-07

Status: candidate — doctrine addition and cross-reference; also states an
existing capability publicly.
Boundary profile: candidate_support_note.

## Change

- Updated: `docs/governance/MISSING_INFORMATION_DISCIPLINE.md` — new
  `## Contradiction handling` section stating that a contradiction is a
  terminal state reached instead of "found", not a gap that more searching
  resolves; the `Ask policy` bullet on conflicting sources now cross-references
  it; the retired-owner triad is removed and `Boundary profile:
  candidate_support_note` declared, following the pattern from #998.
- Updated: `implementation/mvp_vertical/project_claim_conflicts.py` — docstring
  names the doctrine document as the policy owner this module mechanizes for
  scalar Claims, and states the scope boundary (geometric/relational
  contradictions) both ways.
- Updated: `README.md`, `README.fr.md` — new section stating the bitemporal
  `ProjectClaim` model (`effective_at` / `observed_at` / `knowledge_time`,
  supersession as lineage, the two as-of read modes) as implemented, with the
  as-of/conflict gap named and linked to #1012.
- Updated: `tests/test_openwebui_integration_owner_retirement.py` — one entry
  removed from `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES`, forced by the ratchet.
- Removed: nothing else.

## Why

Reviewing two architecture diagrams (an uncertainty-resolution tree and a
"semantic spine" from sources to understanding) against what the repository
actually contains turned up two disconnected facts:

```text
docs/governance/MISSING_INFORMATION_DISCIPLINE.md
    already names `source_found_conflicting` as a search outcome
    already lists "multiple sources conflict" as an ask trigger
    -> zero references to project_claim_conflicts.py

implementation/mvp_vertical/project_claim_conflicts.py
    already detects and refuses to resolve scalar Claim tension
    -> zero references to the missing-information doctrine
```

One is candidate doctrine, the other is running code, and they were written as
if the other did not exist. The uncertainty tree under review had the same gap:
its two branches (`non déterminante` / `déterminante`) have no way to represent
a contradiction, which is neither — a contradiction is not resolved by
`chercher davantage`, because more sources cannot reduce a genuine tension
between two admitted ones.

Separately: the bitemporal claim model (`observed_at` / `effective_at` /
`knowledge_time`, supersession-as-lineage, two distinct as-of read modes) is
real, tested, executable, and mentioned in zero governance documents, zero
READMEs and zero landing pages. `898f2fe0` put the less-proven
semantic-continuity hypothesis on every public surface the same day; the more
proven capability had none. That asymmetry is corrected here for the two
READMEs; the landing pages (`docs/index.html`, `docs/index-en.html`) are
deliberately left for a separate, more editorial pass — they are prose
narrative rather than a modular section, and changing marketing copy is a
different judgment call than adding a section to a technical README.

## What was deliberately not done

No new schema, contract, persistence or detection behavior. The contradiction
section states an existing outcome (`source_found_conflicting`) and an existing
implementation (`project_claim_conflicts.py`); it does not invent a third
register field or a new candidate status. The as-of/conflict gap is linked to
#1012 rather than solved here — the same reasoning that opened #1012 applies:
the need is inferred from reading the code side by side, not from an observed
failure in `#986`.

## Boundary

Boundary profile applies: `candidate_support_note`.

Protected paths touched: no.
Runtime impact: none. Two docstrings and two READMEs; no schema, contract,
persistence or detection behavior changes.
Authority impact: none. `MISSING_INFORMATION_DISCIPLINE.md` remains `candidate`;
this change does not promote it. The `project_claim_conflicts.py` docstring
addition documents an existing relationship; it grants the doctrine document no
enforcement power over the module's code.
Schema/test/CI impact: one ratchet entry delisted, forced by #995's mechanism
rather than chosen; no test weakened, skipped or removed.
External action: none.
Memory behavior: none.

## Verification

```text
tests/                                    675 passed
check_status_headers.py                   OK
check_internal_links.py                   OK
check_no_truncation.py                    OK
check_obsolete_authority_consistency.py   OK
implementation/mvp_vertical/project_claim_conflicts.py  parses; module tests unaffected
```

The delisting was mutation-checked before being kept: re-adding the entry to
`KNOWN_CANDIDATE_OPENWEBUI_RESIDUES` failed `no_longer_present`, naming the
file; reverted, 10 passed, `git diff` on the test file empty.

## Local distinctions

```text
contradiction    != gap
terminal state   != state on the way to resolution
doctrine written != doctrine cross-referenced
implemented      != publicly stated
```
