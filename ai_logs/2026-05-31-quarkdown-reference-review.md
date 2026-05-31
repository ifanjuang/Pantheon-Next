# AI Log — Quarkdown reference review

Date: 2026-05-31

## Scope

Recorded `iamgio/quarkdown` as an external publication tooling reference for Pantheon Next.

Clarified after user arbitration that Quarkdown's operational projection should be a Hermes Skill Candidate for document rendering, not merely a generic publication adapter.

This intervention follows the modular placement doctrine:

```text
The exposure surface exposes.
The execution runtime executes.
Pantheon governs.
```

Quarkdown is classified as a candidate publication / rendering tool whose governed operational projection is a Hermes Skill Candidate, not Pantheon Core.

## Files changed

Added:

- `docs/governance/reference_reviews/QUARKDOWN.md`;
- `ai_logs/2026-05-31-quarkdown-reference-review.md`.

Updated:

- `docs/governance/reference_reviews/QUARKDOWN.md` to add the Hermes Skill Candidate projection;
- `docs/governance/reference_reviews/README.md` to index the Quarkdown review;
- `ai_logs/2026-05-31-quarkdown-reference-review.md` to record this clarification.

## Why

Quarkdown may be useful for rendering governed source material into:

- HTML documentation;
- PDF handbooks;
- slide decks;
- professional fiches;
- printable checklists.

The value is publication and formatting reuse, not governance.

If operationalized, the rendering belongs in Hermes as a task-bound skill candidate returning a Rendered Artifact Candidate, compile logs and source metadata.

## Governance boundary

Documentation only.

The review does not approve a dependency, install a tool, add CI, create an adapter, create templates, create executable configuration, mutate schemas or authorize publication automation.

It also does not install a Hermes skill.

Quarkdown remains candidate / to verify.

## Placement decision

Accepted:

- external publication / rendering candidate;
- possible future Hermes Skill Candidate for governed document rendering;
- possible future renderer for validated or explicitly candidate source material.

Refused:

- Pantheon Core;
- source of truth;
- approval engine;
- Evidence Pack final status;
- Canonical Memory;
- workflow engine;
- professional advice engine;
- external publication authority.

To verify:

- GPL / AGPL licensing implications;
- sandboxing and local/remote file access;
- CI behavior if ever used;
- generated artifact stamping with source revision, date and status;
- whether the rendering skill can run without mutating governed source files.

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
Quarkdown may render.
Hermes may execute the rendering as a candidate skill.
Pantheon governs status.
The validated remains.
```
