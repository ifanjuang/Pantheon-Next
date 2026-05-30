# AI Log — General Domain Pack Specification

Date: 2026-05-30

## Scope

Added the general specification that every profession-specific domain pack must
satisfy, before any per-métier pack (architecture first) is written.

## Changes made

Added:

- `docs/governance/DOMAIN_PACK_SPEC.md`;
- `ai_logs/2026-05-30-domain-pack-general-spec.md`.

Updated (index only):

- `docs/governance/STATUS.md` (active governance documents list);
- `docs/governance/README.md` (active governance index).

## Governance intent

`ROLE_ACTIVATION.md` already defines a "professional domain pack" as a governed
configuration of vocabulary, source expectations, risk triggers, templates and
review gates — explicitly not a profession-specific autonomous agent.

`DOMAIN_PACK_SPEC.md` turns that definition into a reusable specification: the
eleven sections and the minimum declared fields every domain pack must provide.
Profession-specific packs reuse the same headings.

The eleven required sections:

```text
1 scope and audience
2 vocabulary
3 source policy
4 evidence expectations
5 risk triggers
6 pre-transmission minimization
7 output statuses and delivery gates
8 answering / acting boundary
9 memory rules
10 review angles and decision gates
11 templates
```

This directly encodes the user's request: per-profession deontological rules,
what is masked before transmission, the email/output candidate→delivery
lifecycle, and the answering-vs-acting boundary — all as governed configuration,
not runtime.

## Cross-references used

The spec cites existing doctrine rather than restating it: `APPROVALS.md`
(C0-C5), `CONTEXT_PACKS.md` and `SCOPE_ISOLATION.md` (minimization),
`EVIDENCE_PACK.md`, `MEMORY.md`, `GOVERNANCE_COLLEGE.md`, `rites/README.md`,
`USER_DECISION_GATE.md`, `OPENWEBUI_TEMPLATES.md`, `EDITORIAL_LANGUAGE.md`.

## Honesty boundary

A domain pack is **draft-only until reviewed**. It does not advise, validate,
send, execute or remember by itself. Activation reveals tensions and constrains
context; it does not grant professional authority. No runtime, agent, router or
automatic action is introduced.

## Explicit non-implementation

No files touched under `schemas/`, `tests/`, `hermes/`, `operations/`,
`pyproject.toml`, or `CLAUDE.md`. No per-profession pack written yet.

## Boundary phrase

```text
A domain pack frames professional AI use.
It does not advise, validate, send, execute or remember by itself.
The professional decides. Only the validated remains.
```
