# Twenty-one architecture documents still named a retired integration as the exposure surface

Date: 2026-09-06

Status: implemented — the boundary triad in `docs/domain-packs/architecture/`
no longer names OpenWebUI as the current exposure surface. One line per file,
21 files. First bounded slice of a repository-wide residue.
Boundary profile: candidate_support_doctrine.

## Change

- Updated: 21 files under `docs/domain-packs/architecture/`, one line each —
  `OpenWebUI exposes.` → `Optional runtime clients may expose interaction.`
- Removed: nothing. No other line, section, status header or claim was touched.

## Why

`CLAUDE.md` states OpenWebUI is a refused/retired target integration with no
current target responsibility, and that historical references remain provenance
only and "must not be used to restore them as architecture owners."

A boundary triad opening a live candidate doctrine document is not provenance.
It is that document's own statement of the current architecture:

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

Twenty-one of the domain pack's 31 files carried it, each exactly once, in the
standard boundary block directly after the "It does not create…" sentence —
including `HISTORICAL_ARCHITECTURE_RECONCILIATION.md`, where it is the document's
own header block rather than a quoted historical statement, so it is the same
case as the other twenty.

## Why this wording

No single replacement is dominant in the repository. Counting the first line of
every already-corrected triad in `docs/governance/`:

```text
7   Hermes clients handle runtime interaction.
6   Optional runtime clients may expose interaction.
5   Optional Hermes WebUI or other compatible clients may expose runtime interaction.
3   (near-variants of the "Optional runtime clients" family)
```

`Optional runtime clients may expose interaction.` was chosen as the most
frequent member of the largest family, already in use in six governance
documents, and closest to `CLAUDE.md`'s own runtime policy ("Compatible runtime
clients remain optional and replaceable; client selection does not transfer
Pantheon authority"). It is quoted, not invented.

## What was found and deliberately not fixed here

Ten files in the same directory still mention OpenWebUI outside the triad, in
two distinct classes:

**Negative boilerplate** — "does not implement a … OpenWebUI template …",
"no mandatory Obsidian, OpenWebUI, Hindsight or Hermes dependency". These do not
name OpenWebUI as a current owner; they disclaim it. They are arguably now noise
(disclaiming non-implementation of a retired integration), but they are not
false, and `#787`'s boundary-boilerplate reduction is their owner, not this PR.

**Stale architecture claims** — `DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md` still
describes an "OpenWebUI cockpit" / "OpenWebUI read-only cockpit" as target
components and states "The candidate adapter and OpenWebUI Tool are committed
and tested". That is the same class as the triad and should be corrected, but
rewriting that file's component list is a doctrine change rather than a
mechanical substitution — and `CLAUDE.md` names that document as an owner to
read before workspace/organization changes. The same file also still calls
`ifanjuang/pantheon-mvp` "external", predating the monorepo co-location.

Reported rather than swept, to keep this change minimal and reviewable.

## Scope beyond this slice

The triad appears in roughly 126 files repository-wide (`docs/governance/`,
`docs/examples/`, `docs/assets/`, `docs/audits/`, `docs/roadmaps/`). The audit
files are dated point-in-time traces where the old formulation is legitimately
historical and must not be rewritten. Deciding that boundary file by file is the
remaining work; this slice covers only the domain pack, where all 21 are live
candidate doctrine.

## The Roles/Rites/Spaces guard fired, and was right to

Three of the 21 files are `ROLE_` owner surfaces
(`ROLE_ACTIVATION_MODEL.md`, `ROLE_FACETS.md`, `ROLE_REFLEX_COORDINATION.md`),
which `.github/scripts/check_roles_rites_spaces_change.py` treats as sensitive
via its `docs/domain-packs/architecture/ROLE_` prefix rule. It requires the pull
request body to declare eight sections — `Change level`, `Observed need`,
`Existing owners checked`, `Overlap analysis`, `Affected consumers`,
`Migration and rollback`, `Authority impact`, `Runtime impact` — with
`Change level` starting at `editorial`, `guidance` or `semantic`. The first PR
body had none of them, so CI went red.

Declared `editorial`: one boundary line per file, no Role, Rite or governed Space
added, removed, renamed or re-scoped, every other line byte-identical.

Two mechanical facts worth recording, because they cost a cycle:

```text
rerun_failed_jobs replays the original event payload
-> PR_BODY stays frozen at the body as it was when the PR opened
-> a body-only fix can never be picked up by a re-run

governance-ci.yml declares `pull_request:` with no `types:` filter
-> default types are opened / synchronize / reopened
-> editing a PR body triggers `edited`, which fires nothing
```

So a fix that lives in the PR body requires a subsequent commit to produce a
fresh `synchronize` payload. This log entry is that commit's content: the guard
interaction belongs in the intervention record regardless, and an empty commit
to kick CI is forbidden.

## Boundary

Boundary profile applies: `candidate_support_doctrine`.

Protected paths touched: no.
Runtime impact: none — documentation only.
Authority impact: none gained. The change removes a false statement of current
architecture; it grants nothing and selects no client.
Schema/test/CI impact: none; no test added or modified.
External action: none.
Memory behavior: none.

## Verification

```text
check_status_headers.py                   OK
check_internal_links.py                   OK
check_no_truncation.py                    OK
check_obsolete_authority_consistency.py   OK
tests/                                    664 passed
```

Each of the 21 files was confirmed to contain exactly one occurrence before the
substitution, and zero after. The replacement string was counted across
already-corrected governance documents rather than composed.

## Local distinctions

```text
retired integration     != absent from prose
boundary block          != historical provenance
disclaimed dependency   != declared owner
mechanical substitution != doctrine change
```
