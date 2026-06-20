# AI log — Hermes 0.17 adapter boundary review

Date: 2026-06-20

Branch: `docs/hermes-017-adapter-boundary`

## Trigger

User requested Pantheon Next adaptation after Hermes Agent 0.17, with a specific concern: the Pantheon kernel should stay general and independent from modular, optional tool capabilities while still allowing Hermes and other tools to express their runtime power.

## Source documents read

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/ADAPTERS_AND_BINDINGS.md`
- `docs/governance/HERMES_INTEGRATION.md`

Related coordination reviewed:

- PR #35 comments, including unresolved review posture around proof support, external-effect gates and schema proposal status.
- Notion governance tracker search for Hermes adapter / execution-pattern cards.

## External change reviewed

Hermes Agent v0.17 expands execution reach through background subagents, image editing, automation blueprints, dashboard profile builder, Skills Hub changes, memory batch operations and external messaging / agent-network channels.

## Decision

Accepted:

- Treat Hermes 0.17 as an adapter-surface change, not a kernel rewrite.
- Add an explicit kernel/adapters split to the adapters doctrine.
- Add Hermes 0.17 mapping to the Hermes integration boundary.

Refused:

- Do not move Hermes runtime behavior into Pantheon.
- Do not make Hermes version-specific features part of the generic framework body.
- Do not treat dashboard auth, skill installation, security scans, profile creation, memory batch success or background task completion as approval, proof, canonical memory or professional validation.

To verify:

- Future adapter manifests should declare target Pantheon contract / manifest version.
- Actual runnable Hermes profiles, skills, channels and automation blueprints still belong outside this repository.

To arbitrate later:

- Whether external messaging channels such as WhatsApp, iMessage, Telegram or Raft should be enabled for agency workflows.
- Whether automation blueprints should be allowed only read-only at first, or also draft-only for selected recurring governance reviews.

## Files changed

- `docs/governance/ADAPTERS_AND_BINDINGS.md`
  - Added kernel/adapters split.
  - Added version-change discipline.
  - Clarified tool update -> adapter review by default.

- `docs/governance/HERMES_INTEGRATION.md`
  - Added kernel and Hermes adapter boundary.
  - Added Hermes 0.17 runtime-surface review table.
  - Added version-change review rule.
  - Added bridges for background subagents, automation blueprints, messaging channels and memory batch operations.

## Status

Documented, not implemented.

No schemas, tests, operations, platform files, Docker files or `.env` files were modified.
