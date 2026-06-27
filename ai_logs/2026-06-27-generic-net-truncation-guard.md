# AI Log — Generic net-truncation guard for long governance docs

Date: 2026-06-27

Actor: Claude (claude-opus-4-8)

## Context

Follow-up to the AUTHORITY_INDEX.md truncation repaired in PR #229. The root
cause was commit `094d0a9`: an *additive* edit (indexing the card-stack and
role-quality cluster) whose net effect silently deleted 107 trailing lines of a
governance doc — the partial-read-written-back-as-full-file failure mode.

The existing tripwire `.github/scripts/check_no_truncation.py` caught it, but
only because `AUTHORITY_INDEX.md` is one of two files hand-listed in its
MANIFEST. New or unlisted long governance docs have no such protection, and the
defect is a *class*, not a one-off.

## Change made

Added a generic, read-only CI guard that generalizes the same class of defect to
every long governance Markdown file, using the base ref the CI already provides.

Created:

- `.github/scripts/check_no_net_truncation.py` — compares each modified
  `docs/governance/**/*.md` file against `GOVERNANCE_BASE_REF`. A file that was
  long at the base (>= 200 lines) and loses both a large absolute share
  (>= 80 lines) and a large proportion (keeps <= 75%) is flagged as a probable
  truncation. Requiring both thresholds avoids firing on ordinary section edits
  while still catching the 094d0a9 shape (369 -> 268: -101, -27%).
- `.github/scripts/truncation_ack.txt` — explicit allowlist. A deliberate shrink
  (a real split or removal) is acknowledged by adding the file's repo-relative
  path here; that edit is itself a reviewable signal.

Updated:

- `.github/workflows/governance-ci.yml` — runs the new check in the existing
  "Governance doctor read-only checks" step, next to `check_no_truncation.py`,
  under the same `GOVERNANCE_BASE_REF` environment.

## Design notes

This encodes an *intent-versus-effect* invariant for the common case: many
governance edits are intended to be additive (index a doc, add a section). When
an additive-looking change produces a large net deletion of a long doc, intent
and effect disagree, and that disagreement is the signal. The check measures the
effect (diffstat-shaped line delta) and fails closed unless the deletion is
explicitly acknowledged.

It is detection, not prevention. The durable fix remains upstream discipline:
never write back a file you only partially read; prefer anchored, in-place
edits. Turning the red into a hard merge gate is a branch-protection decision
left to the maintainer.

## Verification

- No-op against `main`: this branch changes no governance doc, check passes.
- Against base `0efdd87` (pre-truncation), the check flags
  `AUTHORITY_INDEX.md: 369 -> 269 lines (-100, -27%)` — i.e. it would have
  caught `094d0a9`.
- The acknowledgment hatch silences a listed path (verified, then reverted).
- Full doctor suite (`check_status_headers`, `check_internal_links`,
  `check_index_coverage`, `check_axis_vocabulary`, `check_no_net_truncation`)
  passes on this branch under the CI base ref. `check_no_truncation` stays red
  until PR #229 restores the AUTHORITY_INDEX tail on `main`; this branch is
  stacked on the #229 repair so its own CI is green.

## Boundary preserved

`.github/` CI tooling only — a read-only reporter that edits, fixes and decides
nothing. No governance-core, `mcp-server/` or `dashboard/` change. No
`schemas/`, `tests/`, `operations/`, `platform/`, Docker, `.env`,
`pyproject.toml` or `CLAUDE.md` change. No agent, runtime, scheduler, queue,
approval engine or memory engine. No external action. No Registre Probatoire
entry.

## Repo state

Implemented as CI tooling (read-only check) and documentation.

## Decision status

Accepted:

- add a generic net-truncation tripwire over long governance docs;
- acknowledge deliberate shrinks via an explicit, reviewable allowlist.

Left to the maintainer:

- whether to make CI red a hard merge gate (branch protection);
- threshold tuning (currently 200-line floor, 80-line / 25% drop).
