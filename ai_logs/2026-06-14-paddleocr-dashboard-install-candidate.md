# AI Log — PaddleOCR dashboard install candidate

Date: 2026-06-14

## Request

User narrowed the scope to:

```text
just the possibility to install it in the dashboard and let Hermes manage it
```

## Sources read

Doctrine / support:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/DOCUMENT_INTELLIGENCE.md`
- `docs/governance/EXTERNAL_TOOL_PLACEMENT_REGISTER.md`

Related coordination:

- issue #118 — Hermes-first external modules shortlist;
- issue #33 — governed document intelligence;
- open PR search for OCR / PaddleOCR / document intelligence returned no active PR.

External source:

- `PaddlePaddle/PaddleOCR` README, observed blob `6458242fc136e2fc514fee9c8e4896d09bb8fab5`;
- PaddleOCR MCP server documentation, observed blob `b5d906ff9fbbfcf50781c06417fedf085d8c6b84`.

## Decision

PaddleOCR is documented as a dashboard-installable Hermes-managed module candidate.

Decision Zeus:

```text
Accepté as install candidate.
À vérifier before production or dossier activation.
```

Repo state:

```text
Documented non implemented.
```

## Changes

Added:

- `docs/governance/PADDLEOCR_DASHBOARD_INSTALL_CANDIDATE.md`

Updated after Codex review:

- `docs/governance/AUTHORITY_INDEX.md`

The index update records the new candidate governance note without promoting it to canonical doctrine.

No protected paths modified.

## Boundary

This intervention is documentation only.

It does not install PaddleOCR, add a dependency, create a dashboard implementation, create a Hermes skill, create an MCP host, modify schemas, modify tests, modify operations, modify platform code, modify Docker files or modify `.env` files.

## Placement

```text
Dashboard exposes install/configure/health/log controls.
Hermes manages the tool and execution.
Pantheon governs status, scope, evidence, approval and memory boundaries.
```

Forbidden collapses:

```text
OCR output = validated truth
installation = capability approval
dashboard button = authorization
Hermes success = proof
extracted text = Registre Probatoire entry
```
