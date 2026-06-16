# Architecture use-case path clean landing patch

Date: 2026-06-16
Branch: `docs-usecase-path-clean`
Base: documentation-layout landing from PR148 (`84f6bc4b3a67d648e66433239226b77fdc33cafa`)

## What changed

Adds a clean documentation-layout landing patch that injects the architecture proof-of-use layer without reusing the broader PR152 branch.

The page now includes:

- a stronger architecture-first hero;
- a six-step user journey: choose matter, deposit piece, ask question, receive note, see alerts, decide;
- three architecture use cases: VISA validation request, PLU / mairie response, client programme change;
- a mock Pantheon note showing question, candidate reading, expected sources, risk/status and expected decision;
- preserved documentation-style layout and existing external CSS files from PR148.

## Why

PR152 was useful as a drafting branch but too broad for merge because it was based on the architecture-first landing and conflicted conceptually with the current documentation-layout landing on `main`.

This patch is the clean reconciliation path: keep the current documentation structure, add only the proof-of-use sections needed to make the product legible to an architecture agency.

## Doctrine alignment

Documentation / static HTML only.

No runtime, connector, workflow engine, provider router, scheduler, queue, approval engine, memory engine, OpenWebUI Function, Hermes skill, schema, test, operation file, Docker change or `.env` change is introduced.

The use cases and note are fictional candidate-output examples. They do not provide professional validation.

## Repo state

Documented non-implemented.
