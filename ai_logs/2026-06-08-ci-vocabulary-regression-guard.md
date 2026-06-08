# AI log — CI guard against Registre Probatoire vocabulary regression

Date: 2026-06-08.

## Intent

Lock in the Registre Probatoire rename so it cannot regress while the corpus-wide
vocabulary sweep (issue #90) is in progress on the parallel track. Without a
guard, any PR could reintroduce the retired object terms.

## Change

In `.github/workflows/governance-ci.yml` only:

- `actions/checkout@v4` now uses `fetch-depth: 0` so the pull-request diff has a
  merge base;
- a new `pull_request`-only step fails when a PR *adds* a line under `docs/`
  containing `Canonical Memory` or `Memory Candidate`, excluding the deliberate
  "formerly / in place of / replaces the former" notes. It diffs the PR against
  its merge base, so the existing (not-yet-swept) occurrences do not trip it and
  sweep PRs that remove the terms pass.

## Design notes

- Scoped to `docs/` (the governance corpus and examples). `CHANGELOG.md`,
  `ai_logs/` and the workflow itself legitimately mention the old terms when
  describing the rename, so they are not scanned.
- Boundary phrases such as "automatic memory promotion" are unaffected: the
  guard only matches the object terms.
- Uses `git diff --no-color` and `[+]` character classes so it is robust to git
  color configuration and `grep` ERE handling.

## Verification

Tested locally against a real staged diff: an added "becomes Canonical Memory"
line is flagged; a "replaces the former term" note is allowed; a "Register
Candidates" line is clean. The workflow YAML parses.

## Boundary

CI workflow precision only. No doctrine, schema, test or protected-path change
under `schemas/`, `tests/`, `operations/`, `platform/`, `pyproject.toml`, Docker
or `.env`. The guard adds no runtime; it only prevents vocabulary regression on
pull requests.
