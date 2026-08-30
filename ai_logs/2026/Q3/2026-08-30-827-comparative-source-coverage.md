# 2026-08-30 — ratchet #827 comparative source coverage

## Objective

Convert the first observed #827 professional-review failure into the smallest existing-owner constraint.

PR #860 established the baseline fact:

```text
resolved comparison sources = CCTP B + DPGF B + quote Q-2026-041
final retrieved context      = 3 DPGF + 1 CCTP + 0 quote
```

The contractor quote was correctly resolved through access/currentness and exact preserved identity, but global top-k fusion omitted it before drafting.

```text
selected comparison document resolved
!=
selected comparison document represented in retrieved context
```

## Repository state

This slice started from:

```text
main = cfc69b3902b3f3128ee530eeec67c431dc859b82
```

At branch creation:

- #860 was merged;
- no other open #827 PR owned comparative source coverage;
- `retrieval.py` already owned semantic/lexical ranking and weighted RRF;
- `retrieval_scope.py` already owned stateless composition of access, currentness and exact immutable source identities;
- the `devis_reprise` Task Contract already had an extensible `retrieval_boundary`;
- no second retriever, ranking service, schema or professional method owner was needed.

## Change

`retrieval.py` adds one final-selection helper:

```text
select_minimum_source_hits(...)
```

The helper operates only on candidates that already exist in the weighted-RRF pool.

With the default:

```text
minimum_hits_per_source = 0
```

historical global top-k behavior is unchanged.

When explicitly enabled, it:

1. retains up to the declared minimum from each exact `(source_ref, source_digest)` identity when such candidates already exist;
2. fills remaining slots from the unchanged global RRF order;
3. restores the final list to the original global RRF relative order;
4. never creates a candidate or changes a score.

If a selected source produces no candidate, it remains absent. Selection is therefore not converted into relevance.

## Task-specific opt-in

Only the synthetic comparative quote-review Task Contract opts in:

```yaml
retrieval_boundary:
  store: pgvector
  boundary: retrieval_only
  minimum_hits_per_source: 1
```

`retrieval_scope.py` validates and forwards this declared parameter to the existing retrieval owner. It still does not rank.

No default changes for other Task Contracts or for `retrieve_hybrid_scoped(...)`.

## Failure-to-constraint ratchet

The merged #860 baseline deliberately measured source coverage without freezing its defect.

This slice converts that observed defect into the next stable constraint:

```text
for the #827 selected comparative sources,
CCTP + DPGF + quote must each contribute useful retrieved context
when a candidate is available
```

The baseline test now requires complete Evidence Candidate source coverage across those three human-selected/currentness-resolved sources while continuing to leave professional findings observational.

This does not mean:

```text
selected source = relevant passage
retrieved passage = truth
source coverage = professional finding
source coverage = Evidence admission
source coverage = approval
```

The runner's existing usefulness filter, exact claim-support checks, Evidence Candidate boundary and human decision gate remain unchanged.

## Regression coverage

Focused tests protect:

- zero floor returns the historical global top-k unchanged;
- a one-per-source floor represents every available exact source without rewriting RRF scores/order;
- a source absent from the candidate pool is never fabricated;
- impossible slot requirements fail;
- the scope seam forwards only the Task Contract's declared floor;
- invalid declared configuration fails before ranking;
- the real #827 corpus now requires CCTP + DPGF + quote coverage and still rejects the revision-A control.

## Deliberate non-change

This slice does not:

- increase `top_k` blindly;
- change embedding, lexical ranking, RRF weights or scores;
- add another retrieval owner;
- make source selection semantic authority;
- alter currentness;
- add a professional finding taxonomy or drafter behavior;
- change schemas;
- wire Hermes/model runtime;
- admit runtime output as Evidence or authorize an external action.

## Next classification

If exact-head execution confirms the quote now reaches the useful context, the upstream retrieval-coverage blocker is closed for this corpus.

The next observed failure should then be measured rather than assumed. The known current candidate is the deliberately non-analytic deterministic drafter (zero explicit professional claim types), but it must be rerun against the now-complete context before selecting the next correction layer.

## Boundary

```text
candidate coverage != relevance proof
retrieved context != truth
runtime success != authorization
Evidence Candidate != Evidence admission
human oracle != automatic approval authority
```
