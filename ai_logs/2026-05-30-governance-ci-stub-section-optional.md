# AI Log — Governance CI: tolerate absent "Stub present" section

Date: 2026-05-30

## Scope

Fixed a Governance CI failure that affected `main` itself and every open PR.

## Problem

The workflow step "STATUS.md does not list migrated files as stub" extracts the
`## Stub present` section from `docs/governance/STATUS.md` and **hard-failed when
that section was empty or absent**:

```bash
if [ -z "$stub_block" ]; then
  echo "FAIL: could not extract Stub section from STATUS.md"
  exit 1
fi
```

Recent `main` work restructured `STATUS.md` (584 -> 286 lines) and removed the
`## Stub present - non implemented` section entirely. The workflow still expected
that header, so `awk` extracted nothing and the job exited 1 in ~4 seconds,
before reaching the phrase scan.

Because the workflow also runs on `push` to `main`, `main` was red, and every PR
branched from or merged with it inherited the red check — including PR #21.

## Change made

Updated:

- `.github/workflows/governance-ci.yml`.

Added:

- `ai_logs/2026-05-30-governance-ci-stub-section-optional.md`.

The empty/absent case now **passes** instead of failing:

```bash
if [ -z "$stub_block" ]; then
  echo "OK: STATUS.md has no 'Stub present' section; nothing can be listed as stub."
  exit 0
fi
```

## Rationale

The step's real guard is: *no migrated file may be listed as a stub*. If there is
no stub section, that guard is trivially satisfied. The `exit 1` on empty was a CI
assumption (that the section always exists), not a governance rule. The actual
guard — the per-file grep loop — is preserved unchanged for the case where a stub
section is present.

## Verification

Against the committed HEAD tree, all steps now pass:

- mandatory files present;
- `ai_logs/` present;
- stub step: PASS (no stub section);
- migration-mapping: all five migrated files marked `migrated`;
- phrase scan: clean under both the branch regex and the original `main` regex;
- workflow YAML parses.

## Boundary

No runtime behavior added. No governance doctrine changed. This only relaxes a CI
extraction assumption to match the current `STATUS.md` structure on `main`.
