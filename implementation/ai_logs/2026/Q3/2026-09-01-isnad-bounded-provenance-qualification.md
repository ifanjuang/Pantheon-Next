# 2026-09-01 — ISNAD bounded provenance qualification

Status: validation-only implementation slice.

Tracking issue: #922.

## Objective

Qualify ISNAD as a replaceable provenance/transmission-chain and audit observer without creating a second Pantheon Claim, Evidence, review, persistence, authorization, or identity authority.

## Verified baseline

```text
Pantheon-Next/main:
f412fc38488c11448ef697f89084c6a821cfe818

ISNAD:
package 2.20.1
repository alizahidraja/isnad
commit 4a9a9a3dd22b459c5e6a15d87af0997febad1703
latest GitHub release v2.20.1
published 2026-09-01
```

The branch was reconstructed after #923 advanced `main`; the intervening changes touch Hermes/Haystack documentation and adaptability tests only. The Pantheon baseline already reserves `ProjectClaim.status=verified` for reviewed execution-result candidates. This slice does not alter that path.

## Change

- canonical external qualification pin for ISNAD;
- distinct upstream-freshness observation for the current `v2.20.1` release;
- isolated `implementation/labs/isnad_provenance/` adapter;
- provider-neutral advisory observation;
- ISNAD chain-grade observation only;
- self-hashed audit record with claim-text redaction and snapshot hashes;
- optional detached HMAC signature;
- structural and tamper tests;
- dedicated path-scoped qualification workflow;
- convergence correction of a Haystack pin literal left in an active adaptability test by #923.

## Corrections discovered by qualification and review

1. The first exact-head `External Pin Freshness` run failed because the new pin had no corresponding upstream-observation record. That failure was valid: a pin without an independent observation leaves freshness unanswerable. The current GitHub latest release was checked directly (`v2.20.1`, published 2026-09-01) and recorded separately without moving or authorizing the pin.
2. Review found that an incomplete 0→2 chain was graded `munqati` but its audit graph still emitted a direct 0→2 upstream edge. The adapter now emits an upstream edge only for contiguous steps, and the regression test proves the gap remains unbridged.
3. `Hermes LiveSync Reverse Q3` caught an exact ISNAD commit literal duplicated inside the new workflow. The workflow now consumes the ref only through the canonical pin exporter and validates its SHA shape instead of restating its value.
4. After that correction, the same pin-authority contract exposed an inherited #923 defect: `tests/test_hermes_ecosystem_adaptability.py` restated `Haystack 3.1.0` even though the canonical external pin registry already owns that version. The assertion now resolves the Haystack version through `_external_pin_version("haystack")`, removing the duplicate authority rather than exempting it.

These corrections preserve:

```text
upstream observed != pin selected
pin selected for qualification != installed
qualification green != adopted
chain gap != inferred transmission edge
exported pin != second pin authority
active regression assertion != duplicated external version authority
```

## Boundaries

```text
transmission observed != truth
ISNAD grade != Evidence
audit integrity != claim truth
signature verification != Pantheon authorization
narrator id != governed identity
observer output != persistence
ISNAD decision vocabulary != Pantheon decision
qualification presence != adoption
```

The adapter imports neither ISNAD's decision path nor its API/database/review persistence surfaces. It does not import Pantheon product mutation modules.

## Completion criterion

The slice is complete when the exact-package qualification CI, external-pin freshness contract and current blocking workflow set are green and no review thread identifies an unresolved authority or provenance defect. Until then it remains an unmerged candidate.
