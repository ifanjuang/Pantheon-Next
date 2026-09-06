# Seven documents declared a boundary profile and restated the boundary anyway

Date: 2026-09-06

Status: implemented — `BOUNDARY_PROFILES.md` now states the role separation
every profile inherits, and the seven documents that declared a profile *and*
restated the separation in prose no longer restate it. Three of them leave the
retired-owner debt list in the process.
Boundary profile: active_support_doctrine.

## Change

- Updated: `docs/governance/BOUNDARY_PROFILES.md` — new `## Inherited role
  separation` section, quoting `ARCHITECTURE.md`'s Doctrine block as the owner
  and stating that a document declaring a profile inherits it.
- Updated: 7 documents — the four-line role block removed, nothing else touched:
  `catalog/current-decision/README.md`,
  `docs/assets/card-stack/README.md`,
  `docs/assets/card-stack/VISUAL_LANGUAGE.md`,
  `docs/domain-packs/architecture/HISTORICAL_ARCHITECTURE_RECONCILIATION.md`,
  `docs/governance/COCKPIT_ARCHITECTURE.md`,
  `docs/governance/GOVERNANCE_OBJECT_RELATIONSHIP_MAP.md`,
  `docs/governance/concept-model/README.md`.
- Updated: `tests/test_openwebui_integration_owner_retirement.py` — three entries
  removed from `KNOWN_CANDIDATE_OPENWEBUI_RESIDUES` (67 -> 64), and the two
  references to the migration owner corrected from `#787` to `#996`.
- Removed: no document, no test, no check.

## Why the issue's framing of this slice was wrong, and what was done instead

#996 called these seven "pure redundancy, no judgment needed". They were not,
and the check is one line of reading:

```text
the triad says            who exposes / who executes / who governs
the seven profiles say    runtime: false, external_action: false, ...
```

`validation_only_trace` and `candidate_support_note` state what the *document*
does not do. Neither states the role separation. Deleting the block on the
strength of a declared profile would therefore have deleted a claim the profile
does not carry — a small loss, repeated 112 more times if the slicing had been
followed as written.

`BOUNDARY_PROFILES.md` already owns the remedy and already names the fields
(`exposed_by` / `executed_by` / `governed_by`), so the missing piece was one
sentence in the owner, not a new profile and not a new document. With the
inheritance written down, the deletion is a deduplication rather than a loss,
and every later slice of #996 rests on a stated rule instead of on the assumption
this slice would have set as precedent.

The quoted block is `ARCHITECTURE.md`'s (active doctrine), verbatim. It is the
current owner of the separation; the seven copies were older, shorter and, in
six cases, still named a retired client.

## What was deliberately not done

`HISTORICAL_ARCHITECTURE_RECONCILIATION.md` keeps its entry in the residue list.
Its remaining occurrence is at line 358, inside a recorded arbitration
(`### 5. OpenWebUI mapping as authority` / `Decision Zeus: refused.`). Whether a
refusal record should be rewritten when its subject is retired is a judgment
about historical traces, not a deduplication, and it is not this change's.

Nothing was migrated. 112 documents still restate the separation with no profile
at all; they need a profile chosen per document, which is #996's remaining work.

## Measured state, corrected

#996 recorded 74 profiles / 93 triads / 5 duplicates. Re-measured on this branch
by fenced-block detection over every tracked `*.md` outside `ai_logs/`:

```text
before   78 declare a profile   119 restate the triad    7 do both
after    78 declare a profile   112 restate the triad    0 do both
```

The issue's 93 understated the population: it missed `docs/domain-packs/` (19),
`templates/` (4), `hermes/profiles/` (1) and `mcp-server/docs/` (1) entirely.
The correction is posted on the issue rather than silently absorbed here.

## Boundary

Boundary profile applies: `active_support_doctrine`.

Protected paths touched: no.
Runtime impact: none — documentation and one test list.
Authority impact: none gained. The added section grants nothing, defines no new
profile and introduces no vocabulary; it names an existing active-doctrine owner
and states that profiles inherit from it. No document changed status.
Schema/test/CI impact: one test file — three allowlist entries removed (the
ratchet forced this, and refused the change until it was done) and two issue
references corrected. No test added, removed or weakened.
External action: none.
Memory behavior: none.

## Verification

```text
tests/                                    665 passed
check_status_headers.py                   OK
check_internal_links.py                   OK
check_no_truncation.py                    OK
check_obsolete_authority_consistency.py   OK
```

The ratchet was observed to bite before being satisfied: with the seven blocks
removed and the allowlist untouched, it failed naming exactly the three fixed
governance documents. That is the lockstep #996 asked for, working unprompted.

## Local distinctions

```text
profile declared   != separation stated
duplication        != redundancy
deletion           != deduplication
slice suggested    != slice correct
```
