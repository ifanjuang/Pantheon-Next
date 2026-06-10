# AI Log — Document learning and explainer boundary

Date: 2026-06-06

Updated: 2026-06-08 after the Registre Probatoire direction landed.

## Context

A multi-tool document-learning workflow was reviewed as an external reference pattern:

```text
live web discovery
closed-corpus synthesis
visual / animated explanation
autonomous task execution
polished deliverable generation
```

The useful lesson is not the specific product stack. The useful lesson is the separation of capability families.

For Pantheon Next, the pattern must remain tool-agnostic:

```text
source discovery produces Source Candidates
corpus synthesis produces Interpretation Candidates
visual or narrated explanation produces Learning / Explainer Candidates
execution runtimes produce Result Candidates and Evidence Pack Candidates
deliverable generators produce Output Candidates
Pantheon governs status, evidence, approval, Registre Probatoire qualification and external-action boundaries
```

Hermès memory may help recall, accelerate or suggest. It does not become the source one may cite for a consequential decision. For that, the output must point back to the Registre Probatoire or to an Evidence Pack Candidate awaiting review.

## Proposed doctrine placement

The right placement is a small addition to `docs/governance/DOCUMENT_INTELLIGENCE.md`, not a new governance perimeter document.

Suggested section:

```text
## Learning and explainer outputs

Document intelligence may produce learning, teaching or explainer artifacts such as summaries, narrated overviews, visual explainers, animated diagrams, training videos, slide drafts or shareable reports.

These artifacts are useful for orientation and communication, but they do not raise the authority of the underlying source, fragment or interpretation.

A learning artifact must therefore carry the same candidate discipline as any other model-produced output:

- it must reference the source scope it used;
- it must distinguish source quotation, extraction, interpretation and narrative simplification;
- it must expose missing visual, tabular or diagram evidence when the artifact depends on it;
- it must not turn a fluent explanation into a conformity verdict, professional conclusion or approved transmission;
- it must not become Registre Probatoire material merely because it was polished, shared, repeated or visually convincing;
- it must not be treated as reliable Hermès memory unless the recall points back to reviewable evidence.

Suggested statuses:

- learning_candidate;
- explainer_candidate;
- shareable_draft;
- requires_human_review;
- approved_for_training_use;
- approved_for_internal_communication;
- approved_for_client_transmission_draft.

The exposure surface may display or play the artifact.
The execution runtime may generate it.
Pantheon governs the status and delivery gate.
The human decides whether it may leave the working perimeter.
```

## Boundary

This log does not implement a document-processing stack, video generator, NotebookLM adapter, Perplexity adapter, Manus connector, Runable connector, OCR pipeline, vector index, scheduler, queue, approval engine or memory promotion mechanism.

## Status

Documented non-implemented.

Candidate / to verify.

## Relation

Relevant existing thread:

```text
#33 — Add governed document intelligence and architecture review slice
#41 — Coordination: prefer PRs over direct-to-main, and pause doctrine sprawl
#79 — Direction: memory to Hermès, Pantheon governs the Registre Probatoire
```

This note respects #41 by avoiding a new governance document. It records the proposed narrow insertion point for later PR review.
