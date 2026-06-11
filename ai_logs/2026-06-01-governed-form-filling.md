# AI Log — Governed Form Filling

Date: 2026-06-01

## Scope

Added `docs/governance/GOVERNED_FORM_FILLING.md`: active support doctrine for the
governed filling of any structured document (form, CERFA, administrative template)
from project records and authorized sources, with a per-field resolution loop and
fallback, a claim-ledger field model, mandatory guardrails, and a modular
decomposition into reusable skills.

Generic by design; the CERFA (permis de construire, déclaration préalable,
autorisation de travaux ERP, permis d'aménager) is the first cited instance.

## Why

User first example: from a project database, prepare a required document — find which
one, where to look, retrieve, verify, fill what is certain, ask when in doubt,
document every value's source, save, and produce a downloadable annotated draft. The
user then asked to make it modular / split into several skills.

## What the doctrine fixes

- Field as claim: every field carries value + status (known / retrieved / inferred /
  unverified / entity_to_confirm / conflicting) + source + date.
- Per-field resolution loop with fallback: known -> source A -> source B -> ask; a
  fallback is another authorized source, never a guess; after sources are exhausted
  the answer is "ask", not "assume"; every attempt is recorded.
- Guardrails: entity verification before keeping a contact/company; dated source for
  any regulatory value; no submission/signature ever; scope isolation; save and resume.
- Modular decomposition: classify-document, resolve-known, retrieve-source,
  verify-entity, fill-fields, raise-doubt, render-annotated, save-provenance — each a
  manifest + envelope, never calling each other, returning candidates, degrading
  gracefully. Fan-out then synthesis topology. The composition is a Workflow Manifest.

## Governance boundary

Documentation only. It does not implement a form filler, PDF writer, OCR, web scraper,
API connector, contact synchronization or runtime. Connectors and PDF filling are
adapters outside Pantheon, executed under a Task Contract. Submission and signature
remain entirely human.

## Files changed

Added:

- `docs/governance/GOVERNED_FORM_FILLING.md`;
- `ai_logs/2026-06-01-governed-form-filling.md`.

Updated:

- `CHANGELOG.md`;
- `docs/governance/MODULES.md`, `docs/governance/AUTHORITY_INDEX.md` (indexing).

`STATUS.md` / `README.md` are being rewritten in PR #42 and should index this when
that lands.

## Explicit non-implementation

No files were touched under:

```text
schemas/
tests/
operations/
platform/
Docker
.env
pyproject.toml
CLAUDE.md
```

## Boundary phrase

```text
Find where to look. Verify. Fill what is sure. Ask what is not.
Document every source. Save the work.
The draft is the system's. The signature is the human's.
```
