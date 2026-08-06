# The Knowledge slice carries the document structure it already computed

Date: 2026-08-06
Scope: `mvp_vertical/knowledge.py`, `vendor/pantheon/document_knowledge_slice.schema.yaml`
Axes: E4 certainty, V4 verification, K2 consequence, C1 approval (adopts a reviewed upstream contract; changes no authority)

## What was adopted

Upstream `45a68ae` made `document_structure` required on the Document → Knowledge
slice and added a required `fragment_ref` to every chunk. That change is now
vendored and satisfied; the `deferred_adoption` record is removed and the drift
monitor reports `COHERENT` because the drift is gone, not because it is silenced.

## Why the deferral was shorter-lived than recorded

The deferral first said the blocker was "tranche H (Anatomie)" and that this
repository "produces no `document_structure` and no `fragment_ref`". Both were
wrong. Tranche H is *Project* Anatomy — sites, buildings, levels, zones (plan
§14) — and has nothing to do with structuring a document before chunking. And
`document_structure_read.get_document_structure()` had produced the whole shape
since `8e5ba8f` (#229), `chunk_anchors` included, serving it to its own read API
and to nothing else.

So the work was wiring, and the contract's name had been the only thing tying the
projection to the slice. Upstream making the field required is what turned an
unused projection into a conformance failure — which is the useful kind of
pressure a vendored contract is supposed to apply.

## Projection, not pass-through

The read API is this repository's richer shape. Three places needed narrowing to
the declared fields, because the contract closes `additionalProperties`:

```text
document_structure   drops chunk_anchors and the authority block
native_units         keeps unit_id, unit_kind, ordinal, label
fragments            keeps the eight declared fields
fragments[].locator  keeps structural_locator and region
```

The last one is the one worth noting: this repository records `page_start` and
`page_end` in the locator, while the contract carries the page through the
`native_unit` the fragment references. Nothing is lost — it is stated once, where
the contract states it. Projecting rather than passing through is what lets the
internal shape and the contract move independently.

## The new refusal

`document_structure` being required means a document that was never compiled
cannot produce a conforming slice. `get_document_structure` raises `KeyError`, so
publication would have failed with a bare key name from three layers down. It now
raises a `KnowledgeError` naming the missing step.

## Status

- implemented: the slice carries `document_structure` and binds every chunk to a
  fragment; the contract is vendored at `45a68ae` with a verified sidecar.
- implemented: two tests — one asserting the structure is present, correctly
  narrowed, and that every chunk's `fragment_ref` resolves to a declared fragment;
  one asserting a document whose compilation binding is removed is refused by
  name.
- removed: the `deferred_adoption` record.
- full suite `1238 passed`, no skips. Drift monitor `COHERENT`, exit 0.

## Boundary

```text
structure   != professional truth
fragment    != card
conformance != adoption of authority
compiled    != validated
```

No Evidence is admitted, no memory promoted, no card created by this change.
