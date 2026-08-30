# Hermes Runtime Surface Review

Status: candidate external-runtime review — reviewed release, not installed, activated or task-authorized.
Boundary profile: external_reference_review.
Current reviewed target: Hermes Agent 0.20.6 (`v2026.8.27`).

## Responsibility

This document owns release-specific Hermes runtime facts that can affect Pantheon runtime qualification.

Stable runtime/governance boundaries remain owned by `HERMES_INTEGRATION.md`. Client selection and runtime-status posture remain owned by `WHAT_RUNS.md` / `EXTERNAL_TOOLS_POLICY.md`. Optional external bindings remain owned by `HERMES_CAPABILITY_BINDINGS.md`.

Do not duplicate those owners here. A new Hermes surface belongs here only when it changes what must be observed or refused before a concrete runtime can be qualified.

## Reviewed upstream artifact

Official upstream state reviewed on 2026-08-30:

```text
repository: NousResearch/hermes-agent
version: 0.20.6
tag: v2026.8.27
release_date: 2026-08-27
release_commit: 5fc308a70719a83cccdbba4c0e39c23f5a8239d5
```

The upstream release is a roll-up patch release covering roughly 525 merged PRs / 1,313 commits since 0.20.5. Its release note says the full curated 0.20.x feature summary is deferred to 0.21.0.

The 0.20.6 source and tagged API documentation were therefore reviewed only for material qualification deltas. This review does not prove that any local Hermes installation runs this artifact.

## Existing Runs bridge compatibility

The exact 0.20.6 tagged API documentation still exposes the stable discovery and Runs surfaces used by the Pantheon candidate bridge, including:

```text
GET  /v1/capabilities
GET  /v1/toolsets
POST /v1/runs
GET  /v1/runs/{run_id}
GET  /v1/runs/{run_id}/events
POST /v1/runs/{run_id}/stop
```

`/v1/capabilities` advertises run submission, status, event streaming and stop support. `/v1/toolsets` exposes the concrete tool expansion for the API-server platform behind bearer authentication.

0.20.6 also exposes `POST /v1/runs/{run_id}/approval` for runtime-side pending approvals. The current Pantheon run binding does not need this endpoint and must not treat a runtime approval response as a Pantheon approval.

No source-review evidence requires a Pantheon kernel or run-binding change for 0.20.6. Wire compatibility still requires observation against the exact installed artifact.

## Material 0.20.6 qualification deltas

Only deltas that materially change the trust, tool, execution-host or administration surface are retained here.

| Surface | Upstream 0.20.6 observation | Qualification consequence |
|---|---|---|
| Browser control / real browser profile | The release adds consent-gated use of a real Chromium profile. Tagged API docs also expose opt-in authenticated browser-extension control with exact controller/session/profile matching and fail-closed controller routing. | Keep real-profile / extension control disabled for the governed profile unless separately qualified. If enabled later, record exact controller identity, browser-profile scope, authentication and failure behavior. |
| Desktop remote administration | The release adds managed SSH remote-update behavior and a fleet profile rail. | Treat remote administration/update as an operator surface outside the governed task path. It requires separate deployment qualification before use; it is not implied by runtime qualification. |
| Remote MCP catalogue | The release expands live-verified vendor-hosted MCP availability substantially. | Re-observe the exact enabled toolsets on the target profile. Catalogue/discovery growth must not widen the reviewed runtime tool envelope. |
| Terminal environment backends | The release adds pluggable terminal environment backends. | Record the exact terminal backend used by the target profile because host identity, filesystem mounts, environment and network reach can change with the backend. |
| Secret storage | The release adds opt-in OS-keychain encryption for stored secrets. | Record the configured secret-storage posture. Encryption at rest is useful operational hardening but does not qualify authentication, scope or external-effect safety. |
| Gateway lifecycle / cron | Updaters can pause gateways over the control socket; cron gains durable incident acknowledgements and clearer code-skew failures. | If gateway, messaging or cron surfaces are selected for a deployment, qualification must include restart/update/skew/recovery behavior rather than inferring availability from a healthy process. |
| Runtime approval API | Runs may expose a pending runtime approval and resume through `/v1/runs/{run_id}/approval`. | Keep runtime approval mechanics distinct from Pantheon decision/approval state. No automatic bridge from runtime approval UI/API to Pantheon approval is authorized by this review. |
| Per-request model/provider routing | Tagged API docs continue to accept `model`, `provider` and `model_options` on `/v1/runs` and other authenticated request surfaces. | The Pantheon candidate binding continues to omit these overrides. Provider/model choice remains runtime configuration unless a separately reviewed binding says otherwise. |
| Session-scoped runtime memory | Tagged API docs continue to accept `X-Hermes-Session-Key` on Runs/API conversation surfaces for stable long-term-memory scope. | Keep this header absent from the governed Pantheon run path unless a separately qualified memory posture explicitly requires it. |

Release-note items such as search caching, compression defaults, picker additions and Slack link-unfurl controls do not currently create a distinct Pantheon qualification requirement and are intentionally not copied into this review.

## Governed runtime-profile posture

The existing `pantheon-governed` posture remains the target for a Pantheon-admitted Hermes run. This is deployment configuration, not a new Pantheon identity or authority object.

```text
profile: pantheon-governed
external_memory_provider: off
built_in_memory_injection: off
built_in_user_profile_injection: off
memory_tool: off
session_memory_key: forbidden
provider_and_model_override_in_run_payload: omitted
allowed_tools: exact reviewed runtime-profile/binding envelope
real_browser_profile: disabled unless separately qualified
browser_extension_control: disabled unless separately qualified
remote_admin_update_surface: outside governed task path
terminal_environment_backend: exact observed backend required
consequential_effects: existing Pantheon policy / human gates apply
```

The existing runtime observer already records route/tool/memory posture in the candidate distribution composition. 0.20.6 does not justify a second observer or a parallel runtime inventory path. Any missing 0.20.6 observation should extend that existing seam only after a real target proves the gap.

## Adjacent ownership

This release review does not reclassify external products or clients.

Use existing owners instead:

```text
runtime/client selection and current status -> WHAT_RUNS.md / EXTERNAL_TOOLS_POLICY.md
optional capability bindings               -> HERMES_CAPABILITY_BINDINGS.md
stable Hermes/Pantheon authority boundary  -> HERMES_INTEGRATION.md
technical execution receipt                -> HERMES_EXECUTION_TRACE_SUMMARY.md
```

A mobile, browser, desktop or messaging client may therefore evolve without requiring a new Pantheon architecture document unless it introduces a genuinely new governed consequence.

## Current repository decision

Current repository state deliberately distinguishes source review from the candidate runtime pin:

```text
reviewed upstream release: 0.20.6
current candidate distribution runtime target: 0.20.5
```

The candidate distribution lock already contains a runtime observer and remains default-off / not observed / not activated / not task-authorized. This source review does not change that lock.

```text
reviewed_runtime_target: 0.20.6
kernel_change_required: false
run_binding_change_required: false
new_runtime_owner_required: false
new_client_owner_required: false
candidate_distribution_pin_change_authorized: false
real_instance_observation_required: true
runtime_artifact_digest_required_before_observed: true
composed_acceptance_required_before_qualified: true
installation_effect: none
activation_effect: none
task_authorization_effect: none
```

A later bounded qualification may move the candidate distribution pin from 0.20.5 to 0.20.6 only after the target artifact and the additional release-sensitive checks below are exercised.

## Required live checks before selecting 0.20.6 for the governed distribution

1. record the exact installed Hermes package/image identity and immutable digest;
2. observe the named profile route and `/v1/capabilities` / `/v1/toolsets` from that exact runtime;
3. verify active tools remain within the reviewed profile/binding envelope, including any remotely discoverable MCP surface;
4. record the existing read-only memory-posture observation and prove memory/profile injection and the memory tool remain disabled for `pantheon-governed`;
5. verify no `X-Hermes-Session-Key` is supplied by the governed run client;
6. verify the Pantheon run payload contains no `model`, `provider` or `model_options` override;
7. record the exact terminal environment backend and its effective host/mount/network boundary;
8. confirm real-browser-profile and browser-extension-control paths are disabled, or run a separate explicit qualification before allowing either;
9. confirm remote Desktop/fleet/SSH update administration is not part of the admitted run path and cannot silently mutate the qualified runtime during acceptance;
10. execute one admitted read-only run through the existing launch/reconciliation path and exercise the existing real-runtime ambiguity/failure case required by the current environment qualification work;
11. verify the runtime approval API, if surfaced by a client, produces no Pantheon approval state by implication;
12. if gateway/messaging/cron is selected in the deployment, exercise restart and code-skew/recovery behavior separately and retain delivery/runtime outcomes as technical observations only.

No new schema or test is required by this source review alone. A protected-path change is justified only if live 0.20.6 acceptance exposes an invariant that the existing observer, binding or tests cannot represent.

## Local non-equivalences

The generic repository non-equivalences remain owned by `NON_EQUIVALENCE_RULES.md`. This review adds only the release-sensitive distinctions needed here:

```text
release reviewed != distribution pin changed
release reviewed != release installed
runtime approval endpoint != Pantheon approval
remote admin available != update authorized
remote MCP available != tool admitted
real browser profile available != profile access authorized
terminal backend selected != host boundary qualified
keychain encryption enabled != service exposure safe
```
