# Architecture Target Workflows

Status: candidate support document — target workflow synthesis, documented non-implemented.

This document consolidates the architecture-agency workflow examples into one target model.

It does not implement a runtime, connector, OpenWebUI action, Hermes skill, Gmail sender, Telegram listener, WhatsApp integration, form filler, image analyzer, document generator, PDF exporter or memory engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The examples show the same target pattern in three professional situations:

1. preparing an authorization dossier and Cerfa;
2. analyzing an invoice or situation against CCTP and site reports;
3. reviewing a site photo before adding a point to a site report or escalating.

The common point is not automation. The common point is a governed workflow:

```text
source intake -> source qualification -> scoped context -> candidate production -> quality gates -> user questions -> human decision -> trace decision
```

## Target pattern

A workflow is not a single prompt. It is a dossier path.

```text
User request
-> intake of authorized sources
-> RAG / source retrieval and qualification
-> pre-transmission minimization
-> engine routing: local/internal or external
-> candidate analysis
-> candidate production
-> quality gate
-> feedback / user questions / retry
-> reintegration inside the agency perimeter
-> deliverable preparation through templates
-> final visual and contextual review
-> user decision gate
-> trace / memory decision
```

## Placement

| Layer | Role in the workflow | Must not become |
|---|---|---|
| OpenWebUI | Interface, cockpit, selection, warning, status display, decision capture, review surface | source of truth, autonomous approval surface, hidden workflow runner |
| Hermes Agent | Execution runtime, source retrieval, extraction, analysis, conversion, drafting, image review, candidate production | approval authority, canonical memory, professional decision-maker |
| Pantheon Next | Rules, statuses, gates, evidence expectations, memory boundaries, scope and responsibility | runtime, scheduler, queue, provider router, connector platform |

## OpenWebUI as cockpit

OpenWebUI is the visible workbench.

It may expose:

- the current dossier;
- the selected project;
- the active task contract;
- source lists;
- status labels;
- missing information;
- questions to the user;
- candidate outputs;
- evidence packs;
- approval gates;
- memory decisions;
- action buttons such as prepare draft, request more evidence, revise, approve, reject.

It should not hide consequential decisions inside a chat flow.

## Hermes Agent as execution workshop

Hermes Agent is the place where work happens.

It may execute or delegate:

- document search;
- RAG retrieval;
- source audit;
- OCR or document extraction;
- form prefilling;
- text drafting;
- email draft preparation;
- PDF preparation;
- image analysis;
- photo annotation;
- transcription;
- meeting note preparation;
- plan review assistance;
- data export;
- connector calls;
- evidence pack candidate preparation.

Hermes returns candidates. It does not approve, sign, send, deposit, canonize or decide.

## Candidate connectors and surfaces

These are candidate connection surfaces, not commitments and not implemented by this document.

| Family | Examples | Typical use |
|---|---|---|
| Documents | Google Docs, Word, PDF, Markdown, templates | notices, letters, forms, reports, relecture |
| Spreadsheets | Google Sheets, Excel | project registers, dates, follow-up tables, quantities |
| Messaging | Gmail, Telegram, WhatsApp | incoming photos, email drafts, project exchanges |
| Project knowledge | Notion, Kroqi, project folders, memory candidates | dossier context, project notes, validated traces |
| Calendar | Google Calendar, agenda tools | meetings, site visits, transmission dates |
| Visual and media | Canvas, image generation, ComfyUI, image analysis | annotated photos, diagrams, visual explanations |
| Audio | recording, transcription, meeting minutes | site meeting transcription, CR preparation |
| External references | cadastre, PLU, Géoportail, official forms, APIs, web sources | regulatory context, source verification, Cerfa versioning |

A connector being technically available does not make it authorized. Authorization depends on scope, source policy, risk, approval level and memory rule.

## Candidate skills and tools

Candidate skills and tools should be declared through the module envelope, not hardcoded as doctrine.

Examples:

- source audit;
- RAG retrieval;
- citation verification;
- pre-transmission minimization;
- anonymization and pseudonymization;
- local/external engine routing proposal;
- image description;
- plan reading and annotation;
- surface calculation candidate;
- photo risk review;
- CCTP / CR / invoice comparison;
- form prefilling;
- notice drafting;
- email draft preparation;
- PDF export;
- visual recheck;
- trace registration candidate;
- memory candidate preparation.

Every skill returns:

```text
Task Contract in
-> execution
-> Result Candidate + Evidence Pack Candidate out
```

## Quality gates

A target workflow must stop or loop back if one of these checks fails:

- objective not reached;
- source missing;
- citation not verified;
- source date or version uncertain;
- RAG context incomplete;
- legal, contractual or regulatory consistency uncertain;
- calculation confidence too low;
- image measurement uncertain;
- plan legend inconsistent;
- project context mismatch;
- scope or mandate unclear;
- output vocabulary not aligned with the agency method;
- deliverable status unclear;
- external action not approved;
- memory destination not decided.

## Feedback loops

The target model requires visible return paths:

```text
quality gate -> RAG / source retrieval
quality gate -> analysis
quality gate -> generation
quality gate -> user question
confidence too low -> source request
citation failed -> source verification
image uncertainty -> site verification or photo request
mandate unclear -> user decision gate
external action requested -> approval gate
memory unclear -> trace decision gate
```

A retry is not failure. In a professional workflow, looping back is part of dossier discipline.

## Trace and memory decision

At the end of a task, the system must ask what remains.

Options:

- delete or do not retain the discussion;
- keep a short trace only;
- record a date of transmission;
- register the action in Notion;
- register the action in a spreadsheet;
- create a note in the selected project tool;
- create a Memory Candidate scoped to the dossier;
- create an improvement report candidate.

Nothing becomes canonical memory without validation.

## Example workflows

| Example | Document | D3 prototype | Main lesson |
|---|---|---|---|
| Cerfa and authorization dossier | `docs/examples/architecture_cerfa_workflow/README.md` | `docs/assets/pantheon-workflows/architecture_cerfa_rag_spine_d3.html` | RAG, minimization, local/external engine choice, QA, templates and trace |
| Invoice / situation and visa risk | `docs/examples/architecture_invoice_visa_workflow/README.md` | `docs/assets/pantheon-workflows/architecture_invoice_visa_spine_d3.html` | Distinguish simple transmission, advice, visa and signature |
| Site photo review and escalation | `docs/examples/architecture_site_photo_review_workflow/README.md` | `docs/assets/pantheon-workflows/architecture_site_photo_review_spine_d3.html` | An image is an index, not an automatic finding |

## Boundary

These workflows describe a target operating model. They are not implemented.

They may guide future OpenWebUI templates, Hermes skills, connector manifests, example task contracts and D3 visualizations.

They do not authorize any tool to send, sign, file, deposit, approve, remember or act externally without explicit user decision.

```text
The database records.
The workflow proposes.
The evidence supports.
The approval validates.
The human decides.
```
