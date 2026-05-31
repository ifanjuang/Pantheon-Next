# AI Log — Quarkdown reference review

Date: 2026-05-31

## Scope

Recorded `iamgio/quarkdown` as an external publication tooling reference for Pantheon Next.

This intervention follows the modular placement doctrine:

```text
The exposure surface exposes.
The execution runtime executes.
Pantheon governs.
```

Quarkdown is classified as a candidate publication adapter, not as Pantheon Core.

## Files changed

Added:

- `docs/governance/reference_reviews/QUARKDOWN.md`;
- `ai_logs/2026-05-31-quarkdown-reference-review.md`.

## Why

Quarkdown may be useful for rendering governed source material into:

- HTML documentation;
- PDF handbooks;
- slide decks;
- professional fiches;
- printable checklists.

The value is publication and formatting reuse, not governance.

## Governance boundary

Documentation only.

The review does not approve a dependency, install a tool, add CI, create an adapter, create templates, create executable configuration, mutate schemas or authorize publication automation.

Quarkdown remains candidate / to verify.

## Placement decision

Accepted:

- external publication adapter candidate;
- possible future renderer for validated source material.

Refused:

- Pantheon Core;
- source of truth;
- approval engine;
- Evidence Pack;
- Canonical Memory;
- runtime;
- workflow engine;
- professional advice engine.

To verify:

- GPL / AGPL licensing implications;
- sandboxing and local/remote file access;
- CI behavior if ever used;
- generated artifact stamping with source revision, date and status.

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
Quarkdown may publish.
Pantheon governs status.
The validated remains.
```
