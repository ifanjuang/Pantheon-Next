# AI log — generated ai_logs index (B-8, phase 1)

Date: 2026-07-01.

Actor: Claude Code.

## Intent

Arbitration B-8 (accepted) from the maintainer's decision on the #246 audit: the
`ai_logs/` directory had grown to ~498 flat, dated entries with no consolidation,
hurting readability while the traceability is a Pantheon strength worth keeping.

Phase 1 (this change): restore navigability without a risky mass move.

## Change

- `.github/scripts/generate_ai_logs_index.py` (new, read-only generator): reads
  every dated `ai_logs/*.md`, takes the date from the filename and the subject from
  the first `# ` heading, and writes a newest-first table. Edits nothing else,
  decides nothing.
- `ai_logs/INDEX.md` (new, generated): the navigation table over all logs, with a
  note on the quarterly convention for new logs.

## Deferred (phase 2)

The physical move of the existing flat logs into `ai_logs/<year>/Q<n>/` is a
separate follow-up PR: it is a large, reference-sensitive rename, so it should land
on its own for a readable, reversible diff. New logs adopt the dated convention now;
the index already covers the flat files in the meantime.

## Boundary

Documentation / tooling only. The generator is read-only (reads logs, writes one
index file); `.github/` is CI/tooling infrastructure. No doctrine, schema, test,
`mcp-server/` code, runtime or other protected-path change.
