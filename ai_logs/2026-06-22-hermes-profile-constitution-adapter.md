# AI Log — Hermes profile constitution adapter

Date: 2026-06-22

Actor: ChatGPT

## Context

After distilling the Hermes Agent multi-profile / Kanban megathread into `docs/governance/HERMES_KANBAN_EXECUTION_PATTERNS.md`, the user approved continuing the next step.

The next useful step was to create a non-executable profile-routing constitution under the Hermes profile adapter area, not in the governance kernel.

Existing profile constraints were checked first:

- `hermes/profiles/README.md`
- `hermes/profiles/_base/README.md`
- `hermes/profiles/_base/base-soul-rules.md`

## Change made

Created:

- `hermes/profiles/PROFILE_CONSTITUTION.md`

Updated:

- `hermes/profiles/README.md`

The new adapter note defines candidate runtime profile routing for:

- `pantheon-dispatcher`
- `doc-intake`
- `evidence-review`
- `architecture-domain`
- `repo-maintainer`
- `governance-review`
- `external-connector`
- `observability-review`

It also records:

- non-authority rules for Hermes profiles;
- shared output envelope;
- routing rules;
- Kanban handoff convention;
- `delegate_task` convention;
- channel routing convention;
- Capability Gap behavior;
- local verification checklist;
- Accepted / Refused / To verify / To arbitrate decisions.

## Boundary preserved

The change is documentation only.

No Hermes profile was installed.
No `profile.yaml` or `soul.md` profile was created.
No Kanban board was created.
No gateway routing was configured.
No runtime, scheduler, queue, connector, approval mechanism, memory mechanism, schema, test, Docker file, `.env`, `operations/`, `platform/`, `pyproject.toml` or `CLAUDE.md` file was modified.

## Repo state

Documented non-implemented.

## Decision status

Accepted:

- Profile constitution as adapter note outside the governance kernel.
- Profiles as execution identities only.
- Kanban handoff convention as runtime coordination aid.
- `delegate_task` convention as short-lived helper discipline.

Refused:

- Profiles as Pantheon Roles.
- Profile constitution as doctrine source.
- Runtime memory as Registre Probatoire.
- Kanban comments as Evidence Pack by themselves.
- Self-authorized external action.
- Self-organizing agent team as governance.

To verify:

- Installed Hermes profile and Kanban behavior.
- Local gateway / dispatcher behavior.
- Actual profile home and token isolation.
- Loop guardrails.
- Community plugin behavior.

To arbitrate:

- Whether Pantheon Control may trigger Hermes Kanban tasks directly.
- Whether nightly reviews may update dashboard status or only propose status changes.
- Whether a shared context bus is admissible, and under which scope and memory rules.
