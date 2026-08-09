# 2026-08-09 — Project Anatomy V0.2 match continuity

## Objective

Restore the existing H2 reviewed-match application after the Project Anatomy
owner moved to V0.2, without reopening legacy inline matches or introducing a
parallel identity owner.

## Repository state verified before change

- `pantheon-mvp` `main` was `12f8da0`, including H1, H2, H3 and the merged H4
  read projection;
- H2 still prepared, separately authorized and applied
  `add_match_to_existing_object` for V0.1 owners;
- the V0.2 migration deliberately refused that legacy inline carrier;
- V0.2 already persisted `source_representation` and
  `relation_claim(identity.represents)` as its canonical carriers;
- no open issue, PR or active branch already restored this continuity;
- the executable Observation Bundle remains unavailable, so this slice uses the
  exact persisted Document Structure fragment and does not claim H5 coverage.

## Implemented

- vendored the extended Pantheon-Next write-command contract with exact commit
  and Git-blob provenance;
- kept the single existing operation, review gate, human authorization and APU
  owner;
- made newly prepared commands record the owner's active model version;
- for V0.2, resolved the exact Project-scoped document, compilation and fragment
  before preparing a canonical source representation;
- retained source digest, structure digest, fragment digest, locator, page,
  compiler version, observation time and quality limitations;
- prepared an append-only proposed `identity.represents` claim from that source
  occurrence to the human-selected existing stable object;
- required both canonical payloads to remain `candidate` and retained
  `model_interpretation_candidate` source authority;
- applied both records through the existing project-scoped owner and the same
  `source_match_applied` event family;
- incremented the owner revision while leaving the stable-object revision
  unchanged, because V0.2 stores the alignment as a separate relation claim;
- preserved exact V0.1 command replay and legacy migration behavior.

No SQL migration was added: immutable command payloads are already JSONB and the
V0.2 source/claim tables already belong to the executable owner.

## Refusals and boundaries

```text
missing exact Document Structure fragment -> refuse preparation
Document Structure from another Project -> refuse preparation
legacy command against V0.2 owner -> refuse application
stale owner or object revision -> refuse application
same source identity with different content -> refuse application
candidate identity relation appended != identity professionally validated
candidate identity relation appended != source considered mapped by H4
source occurrence stored != Evidence admitted
application event recorded != Decision or WorkIssue transition
```

Historical V0.1 matches remain readable compatibility history. The migration
continues to create zero canonical source representations or claims from them,
because their exact source observation provenance cannot be reconstructed.

## Verification

- Pantheon-Next APU contract tests: `30 passed`;
- targeted MVP owner/write/projection tests: `21 passed, 4 skipped`;
- full MVP suite with isolated test extras: `1182 passed, 339 skipped`;
- Python compilation and diff whitespace checks passed;
- PostgreSQL end-to-end cases are present for the full review → command →
  authorization → application → H4 projection chain, exact replay and
  cross-project refusal; they are skipped locally because no PostgreSQL service
  is listening on the configured port and remain delegated to exact-head CI.

## Remaining scope

This restores structural H2 → V0.2 continuity only. H5 still owns representative
multi-source and revision validation, contradiction/correction behavior and any
future executable Observation Bundle coverage contract.
