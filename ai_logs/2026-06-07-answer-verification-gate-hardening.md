# AI Log — Answer Verification Gate hardening

Date: 2026-06-07

## Context

The Answer Verification Gate PR already separated memory, evidence, status and approval.

Further review identified edge cases that needed explicit treatment before the doctrine can be safely reviewed:

- knowledge base material mistaken for memory;
- retrieval or RAG chunks mistaken for proof;
- runtime logs mistaken for evidence;
- delivery records mistaken for validation;
- stale or superseded sources;
- oral decisions;
- OCR extraction weakness;
- contradiction between sources;
- cross-dossier memory leakage;
- sensitive information retention;
- runtime state from orchestration tools;
- correction, revocation and supersession.

## Action

Updated `docs/governance/ANSWER_VERIFICATION_GATE.md` on the existing PR branch.

## Changes

- Expanded the core doctrine from four layers to eight visible layers:
  - Knowledge Layer;
  - Free Memory;
  - Retrieval / Candidate Discovery;
  - Evidence Layer;
  - Status / Choice Registry;
  - Approval Layer;
  - Logs / Observability;
  - Delivery / External Action.
- Added forbidden equivalences:
  - Memory != Evidence;
  - Retrieval != Proof;
  - Logs != Evidence by default;
  - Delivery != Validation;
  - Sent != True;
  - Runtime state != Governed status.
- Renamed consequence levels from `C0-C4` to `K0-K4` to avoid collision with approval levels owned by `APPROVALS.md`.
- Expanded the `answer_status` documentary shape with knowledge, runtime log and delivery references.
- Added a candidate `claim_record` shape for consequential statements.
- Clarified Evidence Item / Evidence Pack / Evidence Registry separation.
- Added status transition rules.
- Added a case catalogue covering weak evidence, scope gaps, stale sources, contradictions, oral decisions, drafts, delivery, logs, OCR, RAG version drift, repeated claims, cross-dossier memory, sensitive data, external stale rules, professional triggers, role outputs, runtime state and revocation.
- Added relationships to logs / observability and delivery / external action.
- Added a review decision proposal.

## Governance classification

- Authority: candidate / to verify.
- Repo state: documented non-implemented.
- Decision Zeus: to verify.
- Implementation status: not implemented.

## Boundary

This change does not implement:

- runtime classification;
- a COP feature;
- an executable schema;
- an Evidence Registry database;
- a Status / Choice Registry database;
- a log explorer;
- a delivery engine;
- an approval engine;
- a memory engine;
- automatic memory promotion;
- external action authorization.

## Review note

The change deliberately strengthens the existing PR rather than creating a new governance document, because issue #41 warns against doctrine sprawl.

The next review should decide whether `ANSWER_VERIFICATION_GATE.md` remains standalone candidate doctrine or is later reconciled into `MEMORY.md`, `EVIDENCE_PACK.md` and `REQUEST_LIFECYCLE.md`.
