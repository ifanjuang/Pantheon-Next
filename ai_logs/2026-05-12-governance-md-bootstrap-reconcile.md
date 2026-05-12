# Governance Markdown Bootstrap Reconcile

Date: 2026-05-12

## Objective

Reconcile Pantheon Next governance doctrine, repository structure and Hermes profile templates during bootstrap.

## Implemented

Created or stabilized:

- `docs/governance/README.md`
- `docs/governance/STATUS.md`
- `docs/governance/ROADMAP.md`
- `docs/governance/AGENTS.md`
- `docs/governance/GLOSSARY.md`
- `docs/governance/REPOSITORY_SIMPLIFICATION_PLAN.md`
- `hermes/README.md`
- `hermes/profiles/README.md`
- `hermes/profiles/_base/*`
- Hermes profiles for:
  - ATHENA
  - ARGOS
  - THEMIS
  - APOLLO
  - ZEUS

## Key decisions

- `AGENTS.md` remains the canonical Pantheon Role registry.
- Hermes profiles remain lightweight.
- No `governance.md` per profile.
- No automatic Hermes installation.
- No runtime implementation inside Pantheon Next.
- `HEPHAISTOS` is the canonical spelling.

## Risks

Governance migration remains incomplete.

Schemas, tests and read-only tooling are not migrated yet.

Several governance documents still require migration from Pantheon-OS.

## Non implemented

- runtime execution;
- provider routing;
- scheduling;
- queueing;
- automatic memory promotion;
- Docker runtime stack;
- FastAPI runtime endpoints.
