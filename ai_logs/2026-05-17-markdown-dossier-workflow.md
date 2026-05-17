# AI Log — Markdown dossier workflow governance proposal

Date: 2026-05-17

## Scope

Created a governance proposal for progressive Markdown dossier production.

The work documents how a professional dossier could be edited over time with:

- inline comments;
- source and citation markers;
- questions to the user or source;
- assumptions;
- contradictions;
- selected-zone operations;
- variants;
- coherence review;
- versioning;
- validation thresholds;
- memory proposal boundaries.

## Files changed

- `docs/governance/MARKDOWN_DOSSIER_WORKFLOW.md`
- `docs/governance/README.md`
- `docs/governance/STATUS.md`
- `CHANGELOG.md`
- `ai_logs/2026-05-17-markdown-dossier-workflow.md`

## Why

The product need identified was not a generic document editor.

The need was a governed professional writing surface where a dossier can evolve progressively while keeping sources, questions, hypotheses, contradictions, evidence, coherence and version history visible.

OpenWebUI and Hermes Agent already expose likely candidate surfaces:

- OpenWebUI Notes, selected text enhancement, action functions and native tools for cockpit behavior;
- Hermes Agent file tools, skills, context files, patch candidates, search and coherence-review execution possibilities.

Pantheon should therefore govern the workflow rather than implement an editor/runtime.

## Changes

Added `MARKDOWN_DOSSIER_WORKFLOW.md` as documentation-level governance doctrine.

The document defines:

- purpose and product promise;
- user-facing vocabulary;
- scope and non-goals;
- possible Markdown dossier structure;
- inline governance comment grammar;
- annotation vocabulary;
- selected-zone operation model;
- coherence review checklist;
- update proposal model;
- versioning expectations;
- evidence linkage;
- OpenWebUI mapping;
- Hermes Agent mapping;
- Pantheon responsibility;
- candidate workflow;
- approval guidance;
- first prototype acceptance criteria;
- risks and guardrails.

Updated `docs/governance/README.md` to register the new governance document.

Updated `docs/governance/STATUS.md` to classify the Markdown dossier workflow as active documentation-level governance and explicitly mark runtime implementation as absent.

Updated `CHANGELOG.md` with version `0.1.3 - 2026-05-17`.

## Boundary check

This intervention is documentation-only.

It does not implement:

- Markdown editor runtime;
- OpenWebUI plugin;
- Hermes tool;
- hidden workflow runner;
- scheduler;
- queue;
- provider router;
- automatic document rewriting;
- automatic source validation;
- automatic memory promotion;
- OpenWebUI as source of truth;
- Hermes self-approval.

Pantheon remains the governance layer.

OpenWebUI exposes.

Hermes Agent executes.

Pantheon Next governs.

## Risks and limitations

- The new workflow can be misread as an implemented product feature if status lines are ignored.
- The OpenWebUI and Hermes mappings require deeper verification before implementation.
- No schema was added.
- No test was added.
- No operations tooling was added.
- No runtime behavior was changed.

## Status

Implemented as a governance documentation proposal.

Implementation not started.
