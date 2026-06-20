# AI log — Hermes 0.17 adapter boundary review

Date: 2026-06-20

Branch: `docs/hermes-017-adapter-boundary`

PR: #162

## Trigger

User requested Pantheon Next adaptation after Hermes Agent 0.17, with a specific concern: the Pantheon kernel should stay general and independent from modular, optional tool capabilities while still allowing Hermes and other tools to express their runtime power.

Follow-up user instruction clarified that, because Pantheon Next is not fully deployed yet, important rules may still be promoted into the kernel instead of remaining only in adapters.

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
- Promote durable tool-agnostic invariants into the kernel while Pantheon is still in controlled bootstrap.

Refused:

- Do not move Hermes runtime behavior into Pantheon.
- Do not make Hermes version-specific features part of the generic framework body.
- Do not treat dashboard auth, skill installation, security scans, profile creation, memory batch success or background task completion as approval, proof, canonical memory or professional validation.
- Do not let adapter convenience redefine legitimacy.

To verify:

- Future adapter manifests should declare target Pantheon contract / manifest version.
- Actual runnable Hermes profiles, skills, channels and automation blueprints still belong outside this repository.
- Whether a later schema should codify version-change reviews after doctrine stabilizes.

To arbitrate later:

- Whether external messaging channels such as WhatsApp, iMessage, Telegram or Raft should be enabled for agency workflows.
- Whether automation blueprints should be allowed only read-only at first, or also draft-only for selected recurring governance reviews.

## Kernel rules promoted

The following durable invariants were promoted from adapter discussion into the governance kernel:

```text
Capability installed does not mean capability approved.
Runtime completion does not mean governance approval.
Transport success does not mean task success.
Task success does not mean truth, proof, memory or professional validation.
Retrieval does not mean evidence.
Trace does not mean Evidence Pack.
Runtime state does not mean Pantheon memory.
Profile identity does not mean Pantheon Role authority.
Scheduled or background execution does not change the status of the output.
External communication channel proximity does not lower approval requirements.
Canonical effects are never runtime work.
Ambiguity stops at a visible gate; it must not be resolved by runtime guesswork.
```

## Files changed

- `docs/governance/STATUS.md`
  - Updated status date.
  - Recorded the active kernel/adapters posture.
  - Clarified that controlled bootstrap permits kernel revision when a durable invariant is missing.

- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
  - Promoted kernel/adapters split into modular doctrine.
  - Added kernel-change test.
  - Added version-change discipline as a general rule.
  - Updated the diagram and boundary phrase.

- `docs/governance/CAPABILITY_PLACEMENT.md`
  - Added kernel invariants.
  - Added kernel versus adapter decision rule.
  - Expanded capability gaps and rejected collapses for background, scheduled and messaging-channel cases.

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
