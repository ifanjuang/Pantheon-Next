# AI Log — Langfuse / Hermes first-test runbook

Date: 2026-06-15

## Trigger

User approved proceeding after the safe first-test posture was recorded.

Because `operations/` is a protected path, this intervention is recorded as explicitly authorized by the user instruction `Ok vas-y` in direct continuation of the stated next step.

## Doctrine read first

Read or relied on immediately before this step:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/reference_reviews/LANGFUSE_HERMES_INSTALLATION_PACKAGE_CANDIDATE.md`

Relevant boundary:

```text
operations files may translate validated governance into procedural guidance.
They must not invent doctrine or become runtime.
```

## Change

Added:

```text
operations/langfuse-hermes-first-test-runbook.md
```

## Classification

```text
Accepted:
- Candidate operations runbook for manual first test.
- LAN/VPN-only posture.
- Dashboard link-only posture.
- Synthetic trace only.
- Seven-day retention target.
- Prompt management and datasets disabled initially.

Refused:
- Actual installation.
- Container start.
- Real `.env`.
- Secret creation.
- Public exposure.
- Embedded Dashboard iframe.
- Client dossier trace.
- Dashboard implementation.
- Hermes SDK integration.
- Automatic Evidence Pack, approval or memory promotion.

To verify before execution:
- target host;
- operator;
- secret storage location;
- backup location;
- rollback owner;
- first Hermes trace path.
```

## Boundary

Documented non-implemented.

No Langfuse service was installed.
No container was started.
No `.env` was created.
No `platform/`, schema, test, Dashboard implementation, Hermes integration, approval engine, memory engine or runtime code was added.
