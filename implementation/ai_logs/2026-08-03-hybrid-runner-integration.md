# Hybrid retrieval runner integration

Date: 2026-08-03

## Change

Connect the existing bounded runner to the scoped hybrid retrieval candidate implemented in PR #174.

The runner now:

```text
Task Contract perimeter
→ semantic candidates
→ lexical candidates
→ deterministic weighted RRF
→ usefulness admission
→ drafting candidate
→ Evidence Pack Candidate
→ human decision stand-in
```

A lexical match may remain useful when the local semantic embedder is weak. A semantic-only result still has to satisfy the reviewed cosine-distance threshold. The RRF score orders candidates but is never used as a truth, Evidence-quality or approval threshold.

## Observable metrics

The existing evidence output shape is preserved. Its retrieval profile records:

```text
semantic rank;
lexical rank;
hybrid score;
fusion profile.
```

## Boundaries

```text
lexical match != truth
hybrid rank != Evidence quality
hybrid score != confidence
retrieved != approved
runner success != Evidence admission
```

No provider, reranker, router, scheduler, queue, memory engine, automatic Evidence admission or approval behavior is introduced.

## Status

Implemented candidate in `pantheon-mvp`; not an adopted or activated Hermes binding.
