# AI log — branch / PR cleanup for #189 and #190

Date: 2026-07-03

## Scope

Responded to the request to verify and remove useless branches, starting with the old Crawl4AI / first-principles draft branches surfaced by the current landing roadmap.

## Checked

- PR #189 `chatgpt/crawl4ai-hermes-skill`
- PR #190 `docs/first-principles-crawl4ai-qualification`
- Current open PR list
- Review threads and submitted reviews for #189 / #190

## Decisions

### PR #189

Decision Zeus: `CLOSE_SUPERSEDED`.

Reason:

- The branch overlaps with #190 on Crawl4AI qualification.
- It adds a Hermes web extraction skill candidate plus templates before the current landing cleanup has reduced older candidate noise.
- It should not land as-is.

Action taken:

- Added a PR comment recording the decision.
- Closed PR #189 without merge.

Repo state:

- Not merged.
- Historical direction only.
- Documented non-implemented.

### PR #190

Decision Zeus: `KEEP_DRAFT / SPLIT`.

Reason:

- It combines three separable topics: first-principles review, Crawl4AI adapter review and a New Capability Effect Review rite.
- It remains useful as source material, but should not be merged in its current broad form.

Action taken:

- Added a PR comment recording that it must be split or extracted before landing.
- Left PR #190 open as a draft.

## Branch deletion limitation

The GitHub connector available in this session exposes branch search, branch creation and ref update, but no safe `delete_ref` / branch-delete action.

Therefore:

- I closed the useless/superseded PR (#189).
- I did not delete the remote branch ref itself.
- Manual deletion or a separate tool with branch-delete support is still required if the remote branch must be removed.

## Boundary

No repository file content was changed except this ai_log.
No protected path was touched.
No runtime, dependency, Docker service, crawler, approval engine, memory engine or external action was added.
