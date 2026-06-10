# AI log — Green the Governance CI by widening the forbidden-phrase lint

Date: 2026-06-07.

## Intent

The Governance CI was failing on `main` and across the recent merges. The
forbidden-phrase lint in `.github/workflows/governance-ci.yml` flagged seven
occurrences that are in fact legitimately negated. The maintainer chose to fix
the check rather than reword the doctrine (decision D0a in
`OPEN_PR_RECONCILIATION.md`).

## Root cause

The lint passes an affirmative runtime word only when its section context
contains a recognized negation token. Two precision gaps caused false failures:

- the negation regex recognized `reject(ed)` but not `Refused`, so the
  `Refused:` blocks in `MCP_POLICY_SERVER_CANDIDATE.md` and the rejected list in
  `reference_reviews/ELT_REFERENCE_REVIEW.md` were not treated as negation;
- the queue allow-list recognized `review queue` / `decision queue` but not
  `Impact queue`, a governed review surface used in the Evidence → Memory notes.

Flagged lines (all under Refused / rejected / review-surface context):

```text
MCP_POLICY_SERVER_CANDIDATE.md:55   "Pantheon as provider router."
MCP_POLICY_SERVER_CANDIDATE.md:58   "...automatic memory promotion engine."
EVIDENCE_MEMORY_CANONICALIZATION.md:662   "Impact queue"
EVIDENCE_MEMORY_DEV_PLAN.md:131,294,579   "Impact queue" / impact queue
reference_reviews/ELT_REFERENCE_REVIEW.md:175   "automatic memory promotion;"
```

## Change

In `.github/workflows/governance-ci.yml` only:

- added `refus(e|es|ed|al|ing)?` to the negation alternation;
- added `impact[- ]?queue` to the queue allow-list.

No doctrine wording changed. Verified locally: the full `docs/governance/` tree
is lint-clean after the change, and the workflow YAML still parses.

## Boundary

CI workflow precision only. `.github/workflows/` is not a doctrine-protected
path. No doctrine, schema, test, runtime or protected path under `schemas/`,
`tests/`, `operations/`, `platform/`, `pyproject.toml`, Docker or `.env` was
changed. The guard still fails on genuinely affirmative runtime-suggesting
phrasing; it only stops misreading explicit refusals and the impact-review queue
as violations.
