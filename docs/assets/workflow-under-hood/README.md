# Architecture workflow under the hood

Status: visual support asset — documentation only.

This folder contains a static explanatory HTML page showing how a professional architecture workflow may stay simple for the practitioner while exposing the governed under-the-hood steps when needed.

- [`architecture_workflow_under_hood.html`](architecture_workflow_under_hood.html)

## Purpose

The asset explains the operating pattern:

```text
Simple surface
→ precise under-the-hood trace
→ candidate outputs
→ evidence and gaps
→ human decision gate
```

It is designed for architecture / MOE practice, especially cases where a client email, attached document, project record, plan version or ERP notice may change a consequential project decision.

## What it shows

- two practitioner-facing workflows:
  - impact review after a client change of occupancy / effectif;
  - governed preparation of an ERP fire-safety notice;
- the visible user path: question, sources, impact, questions, candidate deliverables, decision;
- the detailed runtime path: OCR, PDF cleanup, document classifier, project lookup, plan retrieval, vision plan analysis, PDF annotation, impact matrix, Evidence Pack Candidate;
- stop conditions: contract gap, version gap, missing source, unclear room function, unconfirmed recipient, external action without approval;
- output statuses: candidate, to verify, blocked, draft-only, approval required.

## Boundary

This is not implementation.

It does not create:

- email access;
- OCR;
- computer vision;
- PDF annotation;
- Notion synchronization;
- ERP regulatory validation;
- Registre Probatoire storage;
- automatic memory promotion;
- automatic approval;
- external transmission.

The page is an explanatory cockpit mockup. It follows the doctrine:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The Registre Probatoire proves.
The human decides.
```
