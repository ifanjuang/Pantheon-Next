# 2026-09-06 — Hermes context-read Q1

## Objective

Turn the repository-side Context Read Budget into a runtime-specific qualification without creating another Hermes runtime, prompt owner or context authority.

## Revalidated baseline

```text
Pantheon-Next main = 785c9719a1b25192c5fdacbc842cdd62a30ae767
Hermes canonical qualification pin = 0.21.0
Hermes release commit = 29112bef099274229cadff79cdff7bf7b99c4b77
```

Open parallel work was checked before writing. PR #975 changes the existing Hermes runtime-lab harness while extending the current Context Admission bridge for known external content. This Q1 therefore does not modify that harness or plugin. PR #976 owns the separate Hermes improvement-path decision.

## Observed exact-pin upstream behavior

The exact qualified Hermes source already owns project-context discovery in `agent.prompt_builder` and exposes an offline `hermes prompt-size --json` diagnostic.

At the exact pin, project-context discovery is ordered as:

```text
.hermes.md / HERMES.md
-> AGENTS.override.md / AGENTS.md / agents.md
-> CLAUDE.md / claude.md
-> .cursorrules / .cursor/rules/*.mdc
```

Only one project-context type is selected; `SOUL.md` is a separate HERMES_HOME source. `AGENTS.md` may compose a git-root-to-cwd directory chain. `CLAUDE.md` is cwd-only.

The exact pin also owns context truncation. Its no-explicit-config/no-context-length fallback is 20,000 characters; the source supports a model-window-derived dynamic cap and an explicit `context_file_max_chars` override. Over-cap content is represented with retained head and tail plus an explicit truncation marker rather than as a complete read.

These are upstream-source observations. They are not observations of the user's Ubuntu target.

## Repository change

Added a standalone qualification harness and workflow:

```text
implementation/tools/run_hermes_context_read_q1.py
.github/workflows/implementation-hermes-context-read-q1.yml
tests/test_hermes_context_read_q1_contract.py
```

The workflow:

1. loads the existing canonical `hermes-agent` external qualification pin;
2. checks out that exact upstream commit;
3. installs it in an isolated temporary virtual environment;
4. runs the official offline `hermes prompt-size --json` diagnostic in a synthetic workspace;
5. executes the exact installed `agent.prompt_builder.build_context_files_prompt` over bounded synthetic cases;
6. uploads technical observation artifacts only.

The Q1 exercises:

- HERMES.md priority over lower-priority project context types;
- git-root-to-cwd AGENTS.md composition;
- cwd-only CLAUDE.md behavior;
- README.md / DESIGN.md / SKILLS.md not becoming Hermes project context merely by existing;
- EOF-sentinel retention for one below-cap file;
- head/tail truncation with an intentionally omitted middle sentinel for one over-cap file;
- a non-empty context tier from the official offline prompt-size diagnostic.

## Executed observation

PR #982 workflow run `33998891896` completed successfully against the exact canonical pin. The installed package reported `Hermes Agent v0.21.0 (2026.8.31)` and the checkout SHA matched `29112bef099274229cadff79cdff7bf7b99c4b77`.

Observed synthetic results:

```text
default/effective fallback cap = 20,000 chars
below-cap AGENTS.md input = 1,057 chars
below-cap EOF sentinel = present
below-cap truncation marker = absent

over-cap AGENTS.md input = 26,000 chars
over-cap head sentinel = present
over-cap middle sentinel = absent
over-cap tail sentinel = present
over-cap truncation marker = present

offline prompt-size context tier = 133 bytes
offline prompt-size system prompt = 2,782 bytes
```

The runtime also emitted its own truncation warning for the over-cap synthetic file. The Q1 confirmed HERMES.md priority, git-root-to-cwd AGENTS composition, cwd-only CLAUDE behavior and non-loading of README.md / DESIGN.md / SKILLS.md when no recognized project-context file exists.

The observation artifact records source/output digests for the bounded cases and keeps `target_installation_observed=false`.

## Boundary preserved

```text
repository orientation surface != Hermes runtime context-file set
repository size check != deployed runtime observation
file present != file read completely
truncation marker != complete read proof
synthetic exact-pin observation != target installation observation
runtime context loaded != instruction authorized
CI success != production activation
technical observation != Evidence
```

The emitted artifact fixes all authority/effect flags false and explicitly records `target_installation_observed=false`.

## Status

`exact_pin_ci_observed_passed` for the synthetic GitHub-hosted Q1. Real Ubuntu/Hermes target observation remains open and must reuse the target/operator qualification path rather than being inferred from this CI result.
