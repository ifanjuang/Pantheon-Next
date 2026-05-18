# Governance CI Bootstrap

Date: 2026-05-18

## Scope

This intervention introduced a read-only CI workflow for governance content.

Files added:

- `.github/workflows/governance-checks.yml`.

No file under `tests/`, `operations/`, `schemas/`, `pyproject.toml`, `CLAUDE.md` or `platform/` was touched. This respects `docs/governance/MIGRATION_PLAYBOOK.md` line 158.

## Doctrine boundary

The workflow is read-only. It validates governance content and exits with a status code. It does not:

- start a runtime, scheduler, queue, message bus, provider router or workflow engine;
- install Hermes profiles, skills, plugins or external tools;
- promote memory, approve outputs, merge branches or push commits;
- modify any tracked file;
- post comments back to GitHub.

It corresponds to the allowed scope of `ROADMAP.md` Phase 4 (read-only Doctor checks, governance reference validation, schema validation, stub/migration status checks, forbidden-runtime surface checks), delivered via GitHub Actions rather than `operations/doctor.py`.

GitHub Actions is treated as external CI infrastructure, not as a Pantheon runtime.

## Checks implemented

`doctrine` job:

1. **No Python source outside `operations/` and `tests/`** — guards against runtime drift in a markdown-first repository.
2. **No forbidden runtime artifacts at repository root** — `Dockerfile`, `docker-compose*.yml`.
3. **Stubs carry canonical header** — extracts the stub list from `STATUS.md` and verifies each listed file exists and starts with `Status: stub`.
4. **Hermes profile uniformity** — each of the seven profiles must have `profile.yaml`, `soul.md`, `README.md`.
5. **Canonical agent ids in YAML schemas and profiles** — `HEPHAESTUS` / `hephaestus-agent` forbidden in `.yaml` / `.yml` under `hermes/profiles` and `schemas`. Markdown narrative may still mention the non-canonical spelling as an explicit warning, per `MIGRATION_PLAYBOOK.md`.
6. **Schema governance_refs resolve** — every `docs/governance/*.md` path referenced in a schema must exist.
7. **AI log filename format** — `YYYY-MM-DD-slug.md` enforced for all `ai_logs/*.md` except `README.md` and `migration-mapping.md`.

`links` job:

- **Markdown link check** — lychee in offline mode (no external network), excluding `legacy/`.

## Triggers

- `push` on `main`;
- `pull_request` (any base).

No `schedule` trigger. The repository has no cron job, no automatic remediation, no scheduled scan.

## Permissions

`contents: read` only. The workflow cannot write to the repository.

## Risks and limitations

- The stub list is extracted from `STATUS.md` by regex. A change in `STATUS.md` section layout could break extraction; the workflow fails closed if the list comes out empty.
- The HEPHAESTUS guard intentionally allows the spelling in markdown. A future stricter rule could narrow this further.
- Lychee runs offline only; external URLs in markdown are not checked. This is a deliberate trade-off to keep the CI deterministic and avoid network flakiness.
- The workflow does not validate YAML schema structure (no `jsonschema` validation). Adding that would require touching `pyproject.toml` and a `tests/` directory, which is forbidden for Claude under the current playbook coordination rule.
- No Python `pytest` or `ruff` step is configured; the `pyproject.toml` configuration remains dormant until `tests/` exists.

## Next recommended action

1. Run the workflow on a PR and confirm all jobs are green.
2. When `tests/` and `operations/` are created (Phase 4 implementation), extend this workflow with a `python` job that runs `pytest` and `ruff check`.
3. Consider adding a separate workflow for GitHub Pages deployment from `docs/`, decoupled from governance checks.
