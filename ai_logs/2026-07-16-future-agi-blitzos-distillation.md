# AI Log — Future AGI and BlitzOS current review and distillation

Date: 2026-07-16  
Status: completed documentation review; no runtime implementation  
Scope: current upstream review, Pantheon distillation, Hermes Capability Slot placement

## Request

Review the current `future-agi/future-agi`, `blitzdotdev/blitzos` and Pantheon Next repositories, decide whether the external projects should be distilled or incorporated into Hermes, and prepare the governed repository update.

## Sources pinned

```text
future-agi/future-agi
commit: 7d5eb27d383067e61f2812ffb7528c24060e56c0
observed: 2026-07-16

blitzdotdev/blitzos
commit: ea6700253cd942aa436d636fe36b142d4097149f
observed: 2026-07-16

NousResearch/hermes-agent
release reviewed: v0.18.2 / v2026.7.7.2
release date: 2026-07-07

Pantheon Next base
commit: e5633a2159eff6492752b747b3814a6f12166651
```

## Future AGI observations

- The repository is a broad reliability platform with more than 8,000 tracked files and substantial Python, Go and frontend code.
- The documented default stack includes frontend, Django backend, worker, AgentCC gateway, model serving, privileged code executor, PostgreSQL, ClickHouse, Redis, RabbitMQ, MinIO and Temporal; Compose also contains PeerDB components.
- Minimum documented resources are 8 GB RAM and 20 GB disk, with 16 GB RAM recommended. The code executor requires `privileged: true` and is incompatible with several managed container platforms.
- The README marks the release as nightly / early testing. `TESTING.md` says frontend CI is active while backend CI remains on the roadmap.
- Optional PostHog middleware can record authenticated email as distinct identifier plus endpoint, organization and workspace context.
- Production Sentry initialization, when configured, enables default PII and full request-body capture.
- The README documents `FUTURE_AGI_TELEMETRY_DISABLED=1`; repository search found no implementation reference outside the README at the pinned commit.
- The inspected prompt-optimizer path stores trials and identifies a best candidate for display. No automatic replacement of the active prompt was observed in that path.

## BlitzOS observations

- The repository is a small, young implementation centered on Claude Cloud.
- Its primary artifact is a private context repository containing `CLAUDE.md`, repository membership / gitlinks, portable skills and `sessions/` work records.
- The current README lists Codex support and self-updating context as future work.
- Files-in-repository warm context was experimentally demonstrated upstream, while several earlier private-repository clone/push approaches failed or depended on changing Claude-specific capabilities.
- The local scanner deliberately reads environment-variable names from templates rather than secret values and the builder includes fail-closed secret checks.
- The generated operating instructions can copy skills automatically into cloud sessions and write session records to the default branch.
- The self-hosted portal requests GitHub OAuth scope `repo`, stores the token in D1 and defaults to any GitHub login unless `ALLOWED_LOGINS` is configured.
- The repository exposed one shell test suite and no root GitHub Actions workflow at the pinned commit.

## Hermes overlap

Hermes v0.18.x already provides profiles, skills, memory and session search, gateway channels, provider selection, scheduler / cron, subagents, coding projects, completion contracts and verification evidence. Importing either external project wholesale would duplicate or compete with existing Hermes responsibilities.

The especially sensitive overlap is self-improvement and memory:

```text
Hermes /learn or background review
+ Future AGI optimizer / feedback loop
= two possible mutation authorities

Hermes profile memory / session history
+ BlitzOS shared context repository / session log
= working context easily mistaken for canonical memory
```

Pantheon keeps both below its approval and memory gates.

## Decision

```text
Future AGI:
  distill current delta
  do not incorporate the platform
  retain one optional evaluation_simulation_lab Capability Slot
  install_status: absent
  activation_status: unavailable

BlitzOS:
  distill context and handoff patterns
  do not incorporate the product or portal
  prefer a Pantheon-native portable_context_handoff adapter for Hermes
  install_status: absent
  activation_status: unavailable
```

Executable adapter code, if later approved, belongs in the separate Hermes-side repository under `HERMES_CODE_HOSTING_BOUNDARY.md`. This PR adds no executable adapter, dependency, service, secret, scheduler, provider route, MCP host, plugin manager, memory engine or installer.

## Files changed

- `docs/governance/reference_reviews/README.md`
- `docs/governance/DISTILLATION_REGISTRY.md`
- `docs/governance/REJECTED_PATTERNS.md`
- `docs/governance/HERMES_CAPABILITY_BINDINGS.md`
- `docs/governance/EXTERNAL_TOOL_PLACEMENT_REGISTER.md`
- `docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md`
- this AI log

## Validation expectations

- internal Markdown links resolve;
- every governance file has an accepted status header;
- authority index coverage remains complete;
- obsolete-authority consistency remains intact;
- no affirmative runtime claim is introduced;
- no runtime or dependency file changes.

## Boundary

```text
reviewed != adopted
distilled != installed
installed != approved
healthy != safe
simulation_pass != approval
session_handoff != canonical_memory
context_update_candidate != merged_context
```
