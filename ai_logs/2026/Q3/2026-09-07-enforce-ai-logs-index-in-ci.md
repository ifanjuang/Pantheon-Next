# The index said "generated" and nothing checked it

Date: 2026-09-07

Status: implemented — `ai_logs/INDEX.md` staleness now fails Governance CI.
No document content changed; the check imports the generator rather than
duplicating it.
Boundary profile: bounded_ci_authority_repin.

## Change

- Added: `.github/scripts/check_ai_logs_index_current.py` — imports
  `collect_rows` and `render_index` from `generate_ai_logs_index.py`, compares
  the result against the committed `ai_logs/INDEX.md`, fails on mismatch.
- Updated: `.github/workflows/governance-ci.yml` — one step, placed directly
  after the existing "ai_logs directory exists" check.
- Removed: nothing. No index content changed by this PR; today's index is
  already current.

## Why

This morning's audit (`docs/audits/2026-09-06-enforcement-and-exercised-authority.md`)
named a repeated pattern: a rule is written, an owner is named, and nothing is
built that can fail when the rule is broken. `ai_logs/INDEX.md` was itself an
instance of exactly that pattern, found while writing the audit:

```text
INDEX.md's own text     "It is generated — do not edit by hand; run
                         generate_ai_logs_index.py after adding a log."
enforcement              none
check_index_coverage.py  reads as though it might cover this; explicitly
                         excludes ai_logs/ at line 59
```

39 of 245 Q3 entries were missing, discovered only by reading the file by hand.
Every session-produced entry from earlier today was among them. The gap closed
itself twice more since — once when #1005 merged (one entry), once when #1013
merged (three entries) — each time requiring a manual regeneration that a check
would have caught for free.

## Why a Python check rather than a shell `git diff`

The workflow already checks out full history (`fetch-depth: 0`), so a
`generate then git diff --exit-code` step would have worked. It was not chosen:
it mutates the checkout as a side effect of checking it, and a check that writes
before it verifies is one incident away from "passed by accidentally leaving the
write in." Importing `collect_rows` and `render_index` directly computes the
expected content without touching the working tree, and — more importantly —
means the check and the generator share one implementation. They cannot drift
from each other the way `check_index_coverage.py` and `ai_logs/` did.

## Boundary

Boundary profile applies: `bounded_implementation_change` would overstate this —
no `implementation/` code is touched. Recorded as `bounded_ci_authority_repin`:
a scoped CI authority change (one new required check), not a runtime or doctrine
change. If #1000's reconciliation is revisited, this may deserve its own defined
profile; noted rather than resolved here.

Protected paths touched: `.github/workflows/` — CI configuration only, following
the same class of change as #997.
Runtime impact: none. One additional read-only check in CI; no runtime, schema
or document content changes.
Authority impact: none. The check enforces an existing stated contract
(`ai_logs/INDEX.md`'s own text); it grants nothing and defines no new rule.
Schema/test/CI impact: one new check script, one new required CI step. No
existing test or check weakened, skipped or removed.
External action: none.
Memory behavior: none.

## Verification

```text
tests/                                    678 passed
check_status_headers.py                   OK
check_internal_links.py                   OK
check_no_truncation.py                    OK
check_obsolete_authority_consistency.py   OK
check_ai_logs_index_current.py            OK
.github/workflows/governance-ci.yml       parses as valid YAML
```

The check was proven to fail before being wired in: `ai_logs/INDEX.md` was
overwritten with placeholder content, the check failed with the stated remedy,
the original content was restored, and the check passed again with `git diff`
empty throughout.

## Local distinctions

```text
stated contract   != enforced contract
generated         != verified generated
mutate then check != check without mutating
shared logic      != logic that can drift
```
