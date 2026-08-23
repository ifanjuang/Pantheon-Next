# Upstream document_knowledge_slice drift — deferred, and the deferral made checkable

Date: 2026-08-06
Scope: `mvp_vertical/vendor/pantheon/`, `tools/check_schema_drift.py`
Axes: E4 certainty, V3 verification, K2 consequence, C1 approval (records a non-adoption decision; adopts nothing)
Status: superseded on 2026-08-06 — the contract was adopted; see 2026-08-06-document-structure-adopted.md

## The drift

Upstream `45a68ae` ("schemas: structure documents before chunking") changed
`document_knowledge_slice.schema.yaml` substantially:

```text
+ document_structure          added to the top-level `required` set
+ fragment_ref                added to `chunk.required`
+ document_structure_recorded added to version_event.event_type
+ $defs                       document_structure, document_fragment,
                              native_unit, normalized_region,
                              fragment_qualification
```

This is not a rewording. It requires the consumer to derive a document structure —
native units, ordered fragments with locators and optional qualification — before
chunking, and to bind every chunk to a fragment.

## Why it cannot be adopted now

`knowledge.validate_document_knowledge_slice` runs on **every publish and every
revise** (`knowledge.py:325` and `knowledge.py:385`), and
`build_document_knowledge_slice` emits neither `document_structure` nor a
`fragment_ref` on its chunks. Re-vendoring the new schema would therefore refuse
every Knowledge publication.

**Correction, same date.** This entry first recorded the blocker as "tranche H
(Anatomie)" and stated that the repository "produces no `document_structure` and no
`fragment_ref`". Both were wrong, and the second materially so:

- tranche H is *Project* Anatomy — sites, parcels, buildings, levels, zones,
  spaces, elements (plan §14). It has nothing to do with structuring a document
  before chunking;
- `document_structure.project_document_structure()` already emits exactly the
  required shape — `structure_id`, `document_ref`, `extraction_ref`, `status`,
  `native_units`, `fragments`, `created_at` — and `primary_fragment_ref()` already
  resolves the chunk binding. Both have existed since `8e5ba8f` (#229). They are
  reachable from the read API and from their own tests, and from nothing else.

So the deferral held only until the wiring was done — the remaining work was
connecting an existing projection to the slice builder, not building a capability,
and it waited on no tranche.

**Superseded, same date.** The contract was adopted a few hours later. See
`2026-08-06-document-structure-adopted.md`. The `deferred_adoption` record is
removed and the drift monitor reports `COHERENT`. This entry is kept for the
mechanism it describes and for the two corrections above; its *decision* no longer
holds.

## Why the deferral needed a mechanism

The drift monitor already detected this correctly. Its standing remediation was
wrong for exactly this case:

> DRIFT DETECTED — re-vendor the drifted schema(s) …

Following that advice breaks the build. And with no way to record a decision, the
monitor reports the same drift every Monday forever — which is how a genuinely new
drift later gets missed, because the signal has become noise.

Deferral is now recorded in the schema's provenance sidecar against an **exact
upstream blob**:

```json
"deferred_adoption": {
  "upstream_commit": "45a68aeeeb12d7063221fb2fcbca27134dc15bcd",
  "upstream_blob_sha": "44116682339ba9f9b1442ce1d6200e624c903d70",
  "reviewed_on": "2026-08-06",
  "blocked_by": "tranche H (Anatomie)",
  "reason": "…"
}
```

The monitor reports `DEFERRED` with the reason and exits 0 **only** while
upstream's current blob equals the one reviewed. When upstream moves again, the new
version is unreviewed and is reported as `DRIFT` — exit 1 — with a note that a
deferral exists for a different version. A deferral silences one reviewed change,
never a class of them.

The remediation text now names both responses instead of one.

## Status

- decided: defer adoption. Nothing re-vendored, nothing adopted.
- implemented: `deferred_adoption` in the sidecar; `blob_sha()` and `deferral()`
  in the monitor; `DEFERRED` state; corrected remediation text.
- verified: with the deferral recorded, exit 0 and `DEFERRED` reported with its
  reason. With the recorded blob altered to simulate further upstream movement,
  it returns to `DRIFT`, exit 1, and says the recorded deferral names a different
  version.
- implemented: unit tests for `blob_sha` against `git hash-object`, for reading a
  deferral, and one hermetic guard that any deferral present in a real sidecar
  carries a version, a date and a reason — an incomplete deferral cannot silence
  a drift.
- full suite `1197 passed`, no skips.

## Boundary

```text
deferred    != adopted
reviewed    != approved
silenced    != resolved
one version != every future version
```

No schema was re-vendored. The vendored copy remains pinned at `e9c237bb`.
