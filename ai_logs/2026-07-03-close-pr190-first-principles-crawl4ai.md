# AI log — close PR #190 first-principles / Crawl4AI draft

Date: 2026-07-03

## Scope

Continued the open-branch landing roadmap after #269.

Reviewed PR #190:

- first-principles analytical skill candidate;
- Crawl4AI Hermes-side extraction adapter candidate;
- New Capability Effect Review rite candidate.

## Decision

Decision Zeus: `CLOSE_SUPERSEDED / DO NOT MERGE AS-IS`.

## Reason

The draft remains useful as historical source material, but it combines three separable topics in one large PR.

It should not land during the current cleanup phase because:

- it adds over 1,000 lines;
- it mixes a Hermes skill template, an extraction adapter review and a new governance rite;
- the new capability-effect rite is directionally valid but overlaps with the current placement rule in `CAPABILITY_PLACEMENT.md`;
- the current roadmap prioritizes reducing open draft noise before adding more candidate doctrine.

## Accepted

- First-principles review may remain a Hermes-side analytical skill candidate.
- Crawl4AI may remain a Hermes-side web/document extraction adapter candidate.
- The effect-review question is valid and should continue to guide admission of high-impact capabilities.

## Refused

- No broad merge of a three-topic draft.
- No new rite promoted during cleanup.
- No crawler, runtime, plugin manager, RAG ingestion path, approval engine, memory engine or external-action authority.

## Action taken

- Added a PR comment recording the decision.
- Closed PR #190 without merge.

## Future path

Reopen only as narrow PRs if a later task specifically needs one of these:

- `Crawl4AI` reference review;
- first-principles skill template;
- compact capability-effect checklist.

## Repo state

- PR #190: closed unmerged.
- Runtime implication: non applicable.
- Protected paths touched: none.
- This ai_log is documentation only.
