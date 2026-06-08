# AI log — corpus-wide Registre Probatoire vocabulary sweep (issue #90)

Date: 2026-06-08.

## Intent

Finish the Registre Probatoire rename across the governance corpus. After the
core files (E1–E5) and the keystone, `main` still carried ~389 occurrences of
the retired object terms across ~89 files. This sweep retires them everywhere.

## Change

Across `docs/governance/**/*.md` (89 files):

- `Memory Candidate(s)` -> `Register Candidate(s)`;
- `Canonical Memory` -> `Registre Probatoire entry`, with article handling
  (existing determiners kept; `a` inserted and capitalized at sentence / heading
  start; bare in code-block list items; `as a` / `become a` / `promote a`
  forms repaired) and a few compounds (`Canonical Memory registry`
  -> `Registre Probatoire registry`, etc.).

## Exclusions (deliberate)

- Lines containing `formerly / former name / in place of / replaces the former /
  the former term` are preserved verbatim (the deliberate former-name notes in
  `GLOSSARY`, `MEMORY`, `EVIDENCE_MEMORY_CANONICALIZATION`).
- Two meta / trace documents are excluded entirely because they intentionally
  pair both terms in rename migration tables and would be made nonsensical by a
  blind replace: `REGISTRE_PROBATOIRE_DIRECTION.md` and
  `OPEN_PR_RECONCILIATION.md`.
- Boundary phrases (`automatic memory promotion`, `promote memory`) are untouched
  — they do not contain the object terms.
- `CHANGELOG.md` and `ai_logs/` (historical traces) are out of scope.

## Verification

- Zero residual `Canonical Memory` / `Memory Candidate` outside the deliberate
  former-name notes and the two excluded meta-docs.
- The governance forbidden-phrase lint is clean across `docs/governance/`.
- Balanced diff (352 insertions / 352 deletions): a pure rename.
- Spot-checked `EVIDENCE_PACK`, `SCOPE_ISOLATION`, `EVIDENCE_MEMORY_DEV_PLAN`,
  anti-pattern and reference-review files for grammar.

## Boundary

Documentation only. No schema, test, runtime or protected-path change. No
file rename (filenames such as `ANTI_PATTERN_ROLE_MEMORY_AS_CANONICAL_MEMORY.md`
are left so inbound links stay valid). With this sweep, the Registre Probatoire
vocabulary is consistent across the whole governance corpus.
