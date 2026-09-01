# Hermes Runtime Surface Review

Status: candidate external-runtime review and selected qualification target — not installed, observed, activated or task-authorized.
Boundary profile: external_reference_review.
Current reviewed target: Hermes Agent 0.21.0 (`v2026.8.31`).

## Responsibility

This document owns release-specific Hermes runtime facts that can affect Pantheon runtime qualification.

Stable runtime/governance boundaries remain owned by `HERMES_INTEGRATION.md`. Client selection and runtime-status posture remain owned by `WHAT_RUNS.md` / `EXTERNAL_TOOLS_POLICY.md`. Optional external bindings remain owned by `HERMES_CAPABILITY_BINDINGS.md`.

Do not duplicate those owners here. A new Hermes surface belongs here only when it changes what must be observed or refused before a concrete runtime can be qualified.

## Reviewed upstream artifact

Official upstream release and tagged source reviewed on 2026-09-01:

```text
repository: NousResearch/hermes-agent
version: 0.21.0
tag: v2026.8.31
release_date: 2026-08-31
release_commit: 29112bef099274229cadff79cdff7bf7b99c4b77
annotated_tag_object: 6e8f8418e6378eb2617e4de074e13dedd091b8af
```

The annotated tag resolves to the exact commit above. Upstream describes 0.21.0 as a roll-up over the 0.20.x patch window plus materially expanded Bot, peer, cron/continuity, subagent, MCP, browser, approval and verification surfaces.

This review is a source/release qualification input only. It does not prove that any local Hermes installation runs this artifact.

## Existing Runs bridge compatibility

The exact 0.21.0 tagged API documentation still exposes the discovery and Runs surfaces used by the Pantheon candidate bridge:

```text
GET  /v1/capabilities
GET  /v1/toolsets
POST /v1/runs
GET  /v1/runs/{run_id}
GET  /v1/runs/{run_id}/events
POST /v1/runs/{run_id}/stop
POST /v1/runs/{run_id}/approval
```

0.21.0 keeps run submission, polling, SSE events and stop semantics. It additionally documents durable idempotency keys for run creation, optional session/transcript reuse, subagent lifecycle events, and runtime-side approval continuation.

These additions do not require a new Pantheon run binding: the governed candidate binding can continue to submit one admitted run, correlate its runtime identity, observe status/events and stop it without adopting runtime session continuity, runtime approval or subagent orchestration as Pantheon authority.

```text
run_binding_change_required: false
```

Wire compatibility still requires observation against the exact installed artifact.

## Material 0.21.0 qualification deltas

Only deltas that change trust, state, tool, execution-host or administration boundaries are retained here.

### Bot Mode and durable Bot Chats

0.21.0 ships named agent profiles, shared rosters, group chats and durable Bot Chats. These are Hermes runtime interaction and continuity surfaces, not Pantheon governed identities, dossiers, Registers or Evidence stores.

Qualification consequence: no Pantheon Bot registry or multi-agent runtime is added. Any future use must preserve:

```text
Bot identity != governed identity
Bot Chat != dossier
Bot Chat != Register
```

### `hermes peer`

0.21.0 adds direct agent-to-agent messaging across profiles/gateways with replies retained in canonical Bot Chats.

Qualification consequence: peer transport may be used by Hermes internally only after its concrete profile/tool exposure is observed. A peer message does not create a Pantheon Task Contract, governed delegation, approval or Evidence.

### Cron memory, continuity and notepads

0.21.0 adds persistent cron memory, `continuity=true`, durable job notepads and delivery into Bot Chats.

Qualification consequence: the governed runtime mode keeps memory/profile injection, the memory tool and session memory scope off. Runtime cron memory or continuity must not be promoted to Pantheon memory, Evidence or provenance by implication. Cron/jobs remain outside the admitted task path unless separately qualified.

### Subagent steering and structured output

0.21.0 adds live child listing/steering/stop, partial-result handling, JSON-schema validation and per-delegation cost reporting. Runs SSE can expose `subagent.start` and `subagent.complete` lifecycle observations.

Qualification consequence: these are execution/runtime mechanics. Structured-output validity does not prove a claim true; a child result does not become Evidence; steering a child is not a Pantheon decision. Existing run observation may record bounded child lifecycle facts without adding a Pantheon subagent owner.

### MCP command center

0.21.0 expands MCP inventory, health, import/install and usage/cost management surfaces.

Qualification consequence: catalogue/discovery/installability does not widen the admitted tool envelope. The exact enabled toolset remains the qualification boundary.

### Browser control

0.21.0 extends direct control of the Desktop browser. Tagged API docs also retain authenticated browser-extension control with explicit registration, exact controller/profile matching and fail-closed routing.

Qualification consequence: real-profile / extension / Desktop-browser control remains disabled for `pantheon-governed` unless separately qualified. Browser capability availability does not authorize a browser action or its consequence.

### Protected runtime writes and runtime approval

0.21.0 hardens writes to protected agent instruction, skill and memory files behind Hermes write approval and retains `POST /v1/runs/{run_id}/approval`.

Qualification consequence: Hermes approval is a runtime PEP mechanism only. It does not create Pantheon approval, Evidence or governed write authorization. No automatic bridge from runtime approval state into Pantheon decision state is authorized.

### Verify subsystem

0.21.0 adds run-recipe detection and environment-manifest support for technical verification workflows.

Qualification consequence: a successful build/test recipe is a technical execution observation. It may support later Evidence admission only through the existing Pantheon Evidence path; it is not Evidence or authorization by itself.

### Per-request routing and runtime session state

Tagged API docs continue to accept `model`, `provider` and `model_options` on `/v1/runs`; Runs can also load an existing Hermes session transcript when a `session_id` is supplied and no explicit history is supplied.

Qualification consequence: the Pantheon candidate binding continues to omit provider/model overrides and must not opt into runtime transcript reuse or long-term session memory unless a separately qualified binding/profile explicitly requires it.

## Governed runtime-profile posture

The existing `pantheon-governed` posture remains the target for a Pantheon-admitted Hermes run. This is deployment configuration, not a new Pantheon identity or authority object.

```text
profile: pantheon-governed
external_memory_provider: off
built_in_memory_injection: off
built_in_user_profile_injection: off
memory_tool: off
session_memory_key: forbidden
runtime_transcript_reuse: forbidden unless separately qualified
provider_and_model_override_in_run_payload: omitted
allowed_tools: exact reviewed runtime-profile/binding envelope
skill_manage: outside admitted tool surface
peer_transport: outside admitted tool surface unless separately qualified
cron_jobs: outside governed task path unless separately qualified
real_browser_profile: disabled unless separately qualified
browser_extension_control: disabled unless separately qualified
desktop_browser_control: disabled unless separately qualified
remote_admin_update_surface: outside governed task path
terminal_environment_backend: exact observed backend required
consequential_effects: existing Pantheon policy / human gates apply
```

The existing runtime observer already records route/tool/memory posture in the candidate distribution composition. 0.21.0 does not justify a second observer, a Pantheon multi-agent runtime, a second scheduler, a second memory owner or a parallel runtime inventory path. Any missing live observation should extend an existing seam only after a concrete target proves the gap.

The earlier 0.20.6 review of Hermes automatic memory/skill background review remains a useful historical finding, but 0.21.0 changes the wider memory/continuity surface enough that its exact trigger mechanics must be re-observed before any governed profile enables `memory`, `skill_manage` or runtime learning. The current profile admits none of them, so no authority expansion is required for this target selection.

## Adjacent ownership

This release review does not reclassify external products or clients.

Use existing owners instead:

```text
runtime/client selection and current status -> WHAT_RUNS.md / EXTERNAL_TOOLS_POLICY.md
optional capability bindings               -> HERMES_CAPABILITY_BINDINGS.md
stable Hermes/Pantheon authority boundary  -> HERMES_INTEGRATION.md
technical execution receipt                -> HERMES_EXECUTION_TRACE_SUMMARY.md
```

A mobile, browser, desktop, Bot, peer, cron or messaging client may therefore evolve without requiring a new Pantheon architecture document unless it introduces a genuinely new governed consequence.

## Current repository decision

The reviewed release and candidate distribution target are aligned on 0.21.0:

```text
reviewed upstream release: 0.21.0
current candidate distribution runtime target: 0.21.0
```

The canonical external qualification pin and candidate distribution lock select Hermes 0.21.0 at release commit `29112bef099274229cadff79cdff7bf7b99c4b77`. This is a target-selection decision only. The candidate distribution remains default-off / not observed / not activated / not task-authorized, and its runtime artifact digest remains unset until a concrete installed artifact is observed.

```text
reviewed_runtime_target: 0.21.0
candidate_distribution_runtime_target: 0.21.0
kernel_change_required: false
run_binding_change_required: false
new_runtime_owner_required: false
new_client_owner_required: false
new_memory_owner_required: false
new_scheduler_owner_required: false
candidate_distribution_pin_change_authorized: true
target_selection_effect: candidate-only
real_instance_observation_required: true
runtime_artifact_digest_required_before_observed: true
composed_acceptance_required_before_qualified: true
installation_effect: none
activation_effect: none
task_authorization_effect: none
```

Selecting 0.21.0 as the candidate target does not qualify it. Qualification requires the exact observed 0.21.0 artifact and the checks below.

## Required live checks before qualifying 0.21.0 for the governed distribution

1. record the exact installed Hermes package/image identity and immutable digest;
2. observe the named profile route and `/v1/capabilities` / `/v1/toolsets` from that exact runtime;
3. verify active tools remain within the reviewed profile/binding envelope, including MCP, `memory`, `skill_manage`, peer and browser surfaces;
4. record the existing read-only memory-posture observation and prove memory/profile injection and the memory tool remain disabled for `pantheon-governed`;
5. verify no `X-Hermes-Session-Key`, governed transcript-reuse `session_id`, `previous_response_id` or equivalent continuity input is supplied by the governed run client unless separately qualified;
6. verify the Pantheon run payload contains no `model`, `provider` or `model_options` override;
7. record the exact terminal environment backend and its effective host/mount/network boundary;
8. confirm real-browser-profile, browser-extension-control and Desktop-browser-control paths are disabled, or run a separate explicit qualification before allowing any of them;
9. confirm remote Desktop/fleet/SSH update administration is not part of the admitted run path and cannot silently mutate the qualified runtime during acceptance;
10. execute one admitted read-only run through the existing launch/reconciliation path and exercise the existing real-runtime ambiguity/failure case;
11. observe 0.21.0 run idempotency/replay behavior and confirm a replayed runtime run is not treated as fresh Pantheon authorization;
12. if subagent lifecycle events are emitted, retain them as technical observations only and confirm they create no Evidence, decision or governed child identity by implication;
13. verify the runtime approval API and protected-file write approvals produce no Pantheon approval/write authorization state by implication;
14. if Bot/peer surfaces are enabled in the runtime installation, prove they remain outside the admitted governed tool envelope unless separately qualified;
15. if gateway/messaging/cron/continuity is selected in the deployment, exercise restart, persistence, code-skew and recovery behavior separately and retain outcomes as runtime observations only;
16. if Verify is exercised, retain detected recipes/manifests/results as technical execution material until separately admitted through Pantheon Evidence rules.

No new schema, observer or runtime owner is required by this target selection. A new protected-path invariant is justified only if live 0.21.0 acceptance exposes something the existing observer, binding or tests cannot represent.

## Local non-equivalences

The generic repository non-equivalences remain owned by `NON_EQUIVALENCE_RULES.md`. This review adds only release-sensitive distinctions needed here:

```text
release reviewed != distribution pin changed
candidate pin selected != runtime observed
candidate pin selected != runtime qualified
release reviewed != release installed
Bot identity != governed identity
Bot Chat != dossier
peer message != governed delegation
cron memory != Pantheon memory
continuity != governed provenance
runtime memory != Evidence
subagent result != Evidence
subagent steering != Pantheon decision
JSON schema valid != claim true
Verify success != Evidence
runtime approval endpoint != Pantheon approval
runtime write approval != Pantheon write authorization
MCP discovered != MCP admitted
tool admitted != effect authorized
browser available != browser action authorized
runtime replay != fresh task authorization
runtime success != Evidence
runtime success != authorization
remote admin available != update authorized
terminal backend selected != host boundary qualified
```
