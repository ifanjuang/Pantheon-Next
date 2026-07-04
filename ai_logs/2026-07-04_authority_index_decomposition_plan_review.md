# AI Log — Authority Index Decomposition Plan Review (PR #276)

Date: 2026-07-04

Repository: `ifanjuang/Pantheon-Next`

## Context

Review of PR #276 (docs: add authority index decomposition plan), which adds `docs/governance/AUTHORITY_INDEX_DECOMPOSITION_PLAN.md` and its ai_log. The review had to decide: merge with minimal indexing, request corrections, or refuse as premature.

## Findings

```text
1. The plan is doctrine-compatible: AUTHORITY_INDEX.md stays the master
   authority interpreter; the PR moves no row, changes no script, touches
   no protected path. Verified: only 2 documentation files added.

2. CI blocker found: check_internal_links fails on the PR branch with
   7 new missing internal references — the plan named future sub-index
   paths under docs/governance/authority/ that do not exist yet.

3. check_status_headers passes: "validation-only" is an accepted status
   family. check_index_coverage passes: only "candidate" status docs
   require an index row, so indexing is not CI-mandatory for this plan.

4. Repo convention nonetheless indexes validation-only plans
   (RUNTIME_REVIEW_MODEL_PASSPORT_VALIDATION_PROMOTION.md,
   SPINE_HARDENING_PROPOSAL.md, MONOREPO_INTEGRATION_PROPOSAL.md,
   TARGET_ARCHITECTURE.md all have explicit rows).

5. Coverage checker analysis (.github/scripts/check_index_coverage.py):
   grouped rows are supported (directory paths ending in "/" and "*"
   globs under docs/governance/). Sub-indexes are NOT supported: the
   script reads only AUTHORITY_INDEX.md (INDEX_REL constant), so a
   candidate-status doc whose row moves into a sub-index file would
   become a coverage violation unless the master keeps a grouped row
   covering it or the script is extended in a separately approved PR.

6. check_no_truncation fails on main itself: two successive merges
   accidentally truncated the tail of AUTHORITY_INDEX.md. Commit
   47f176b removed the sensitive-path guardrail body (protected-path
   list and end-sentinel line); commit 9ddc409 removed ~54 more tail
   lines (end of the domain pack rule, the external runtime memory
   adapter rule, the data platform rule and the guardrail header),
   replacing them with a 3-line compressed ending. Both commit
   messages describe row edits only, so the tail loss was accidental —
   the partial-read-overwrite failure mode check_no_truncation exists
   to catch. Main CI is red on this check independently of PR #276.

7. check_apu_referential_integrity fails locally only because the
   jsonschema module is not installed in this environment; CI installs
   it. Not related to PR #276.
```

## Corrections applied (this branch)

```text
- Rewrote the 7 forward-looking sub-index paths in the plan to the
  relative form authority/<NAME>.md (already used in the plan's own
  section 6 table) so check_internal_links passes without any change
  to .github/scripts.
- Added one minimal validation-only row for the plan in
  AUTHORITY_INDEX.md, per repository convention.
- Added the missing trailing newline to the plan's ai_log.
- Regenerated ai_logs/INDEX.md (main's copy was stale: 503 -> 555
  entries; regeneration is deterministic via
  .github/scripts/generate_ai_logs_index.py).
- Restored the accidentally truncated tail of AUTHORITY_INDEX.md from
  git history (state before 9ddc409, including the guardrail body
  removed by 47f176b): execution/governance closing lines, external
  runtime memory adapter rule, data platform rule and the
  sensitive-path guardrail with its end-sentinel line. No script
  change; check_no_truncation passes again.
```

## Answers to the review questions

```text
1. Indexing before merge: not required by CI, required by convention —
   one minimal row added.
2. Coverage checker: grouped rows yes; sub-indexes no (script reads
   only AUTHORITY_INDEX.md). Confirms the plan's PR C step.
3. docs/governance/authority/ is a reasonable future location,
   consistent with existing subdirectories (reference_reviews/, rites/).
   Confirm before creating it; the master index will then need a
   grouped row for it.
4. First migration group: start with obsolete/absent, then external
   references. Their rows are mostly non-candidate statuses, so moving
   them out of the master index does not break coverage even before any
   script decision.
5. No schemas/, tests/, operations/, platform/, Docker, pyproject.toml
   or .env change — verified.
```

## Decision

```text
Demande de correction on PR #276 (link-check blocker), resolved by this
corrected branch. The decomposition itself remains documented
non-implemented; no row migration is performed.
```

## Repo state

```text
Documented non-implemented.
```
