# 2026-07-27 — Registre Probatoire vocabulary sweep (issue #90)

Status: validation-only intervention trace.

## Request

Finish the documentary migration to the Registre Probatoire vocabulary
(issue #90) without confusing Hermès runtime memory, governed objects and
deliberate historical mentions.

## Mapping applied

```text
Memory Candidate(s)  -> Register Candidate(s)
Canonical Memory     -> Registre Probatoire entry   (article-adjusted in prose)
## Memory Candidates -> ## Register Candidates
```

Replacements were context-reviewed, not blind: articles were inserted where the
grammar required (`become a Registre Probatoire entry`, `is not a Registre
Probatoire entry`, `treated as a Pantheon Registre Probatoire entry`,
`Can affect a Registre Probatoire entry?`).

## Scope boundary: capitalized object terms only

This sweep migrates the **capitalized object terms** `Canonical Memory` and
`Memory Candidate` — exactly what issue #90 counted (68 files / 174
occurrences, a case-sensitive inventory) and what the `governance-ci.yml`
vocabulary guard enforces (also case-sensitive).

The **lowercase** phrases `canonical memory` / `memory candidate` are a
different and much larger matter: roughly 120 occurrences pervade the core
doctrine (`ARCHITECTURE.md`, `HERMES_INTEGRATION.md`, terminology tables such
as `TERMINOLOGY_BOUNDARIES.md`/`EDITORIAL_LANGUAGE.md`, and many
boundary/forbidden lines like "does not become canonical memory"). Many read as
conceptual or boundary language adjacent to the preserved
`memory promotion` / `promote memory` phrases, and several need per-line
judgment. They are **out of scope** for this case-sensitive sweep and left for a
separate, explicitly-scoped decision. This document does not claim to have
migrated them.

## Preserved verbatim (not touched)

- Boundary phrases: `automatic memory promotion`, `promote memory`,
  `memory promotion` — they name the forbidden effect, not the object.
- Generic `memory` / `Hermes memory` / `runtime memory` when it really means
  Hermès's ungoverned recall.

## Scope migrated (21 files, 46 occurrences)

Live doctrine-adjacent corpus under `docs/`, plus `hermes/profiles/` and
`templates/`:

- `docs/assets/LANDING_STACK_REVISION.md`, `docs/assets/pantheon-dashboard/…`,
  `docs/assets/pantheon-rpg/{CORRECTIONS,PROMPTS,ROADMAP}.md`;
- `docs/examples/…` (PRACTITIONER_HOOKS, architecture_devis_reprise,
  architecture_legal_module_panel, evidence_topology, legal_note,
  regulatory_watch_conflict, understand_anything_structural_analysis);
- `hermes/profiles/_base/LANGGRAPH_RUNTIME_CANDIDATE.md`;
- `templates/{context_handoff/SESSION_HANDOFF,mcp_external_tool_review,openwebui/README}.md`.

## Justified residual exceptions (kept by design)

```text
ai_logs/**                                    historical migration records (not migrated per CLAUDE.md)
CHANGELOG_ARCHIVE.md                          historical changelog
schemas/examples/*.example.yaml (2)           schema rename is protected / deferred (steps E2–E6)
docs/examples/medical_letter/README.md        sensitive medical fixture kept out of this publication pass
.github/workflows/governance-ci.yml (1)       the guard text itself ("Deliberate 'formerly …' allowed")
docs/governance/REGISTRE_PROBATOIRE_DIRECTION.md (11)  migration-plan doc: mapping arrows + "retire wording"
docs/governance/GLOSSARY.md, MEMORY.md        deliberate "formerly …" / "replaces the former term" notes
```

## Verification

```text
authority class: candidate support doctrine (documentation corpus)
repository state: documented — vocabulary migration only
runtime state: unchanged
protected paths touched: none (schemas/ deliberately left; rename protected)
schema or test change: none
```

- CI vocabulary guard (`governance-ci.yml`, diff-scoped to `docs/`) simulated
  locally on this diff: **no violation** — the PR adds only the new terms.
- Guards green: internal-links, status-headers, no-truncation,
  runtime-boundary-language, index-coverage, axis-vocabulary, no-local-cockpit.
- No **capitalized** object term (`Canonical Memory` / `Memory Candidate`)
  remains outside the justified exceptions above. Lowercase phrasings are out of
  scope (see the scope-boundary section) and untouched.

## Non-effects

Documentation only. No schema, test, runtime or protected-path change; no
authority class moved; the Hermès-memory / Registre-Probatoire boundary is
unchanged.
