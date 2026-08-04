# Hermes 0.20.0 ephemeral laboratory acceptance — 2026-08-04

Status: **passed on an ephemeral GitHub-hosted laboratory installation**. No agency, NAS, OpenWebUI or production installation was observed or qualified.

## Authorities and successful run

```text
Hermes upstream commit
3c27eb6234bf91b8ceee9e9071591b31e9b148cb

Hermes package version
0.20.0

Pantheon-Next authority
db5506668f06bab05b0cad1b244ff19ab17b5f52

pantheon-mvp acceptance head
3380c563fa6ec33730ec2f05a1baddd215f3b9c6

GitHub Actions run
30952996146

Observation artifact
8909893078

Hermes synthetic run
run_5a640a80e0b9
```

The source archive created from the exact upstream commit had this digest:

```text
sha256:289ac0a8d61933dc9f15d7aa5ff8a6ca4a81a447ec8971292f15bbd08c25a114
```

This is the digest of the ephemeral laboratory source artifact, not an agency/NAS installation digest.

## Packaging fact

Hermes `0.20.0` deliberately refuses wheel and sdist builds. The supported development installation is editable source installation.

The laboratory therefore:

```text
git archive exact release commit
→ record archive SHA-256
→ extract into the ephemeral runner
→ uv pip install -e exact extracted source
→ execute installed hermes 0.20.0 CLI
```

```text
source archive digest != production installation digest
editable source installed in lab != production installed
```

## Runtime topology verified

### Listener and named profile

The default profile owns the only API listener. The named profile retains its own API key for `/p/pantheon-governed`, but explicitly disables its port-binding platform:

```yaml
platforms:
  api_server:
    enabled: false
```

The successful run proved:

```text
profile route = /p/pantheon-governed
profile key accepted = true
default profile key rejected on named route = true
secondary listener enabled = false
```

```text
profile key present != secondary listener enabled
route answered != governed profile qualified
```

### Plugin ownership and profile policy

The Pantheon context plugin is installed and enabled once at the gateway/default-process scope. The profile does not own a duplicate plugin copy; it only selects the registered toolset.

```yaml
platform_toolsets:
  api_server:
    - pantheon_context
  cli: []
```

The empty CLI surface is necessary because `hermes memory status` evaluates the `cli` platform. Restricting only `api_server` leaves the built-in memory tool available through the default CLI composite.

```text
API toolset restricted != CLI memory tool disabled
plugin globally registered != profile automatically authorized
plugin enabled != task authorized
```

### Official toolset envelope

Hermes `0.20.0` returns `/v1/toolsets` as:

```json
{
  "object": "list",
  "platform": "api_server",
  "data": []
}
```

The observer now validates that exact envelope and fails closed on an unexpected object, platform or non-list `data` field. A historical bare list is retained only as an explicitly labelled compatibility surface.

The successful observation resolved exactly:

```text
active toolset: pantheon_context
active tools:
- pantheon_context_manifest
- pantheon_context_entity
unexpected tools: []
missing required tools: []
```

### Complete memory posture

The fresh launch receipt qualified every required axis:

```text
external_provider = off
built_in_memory_injection = off
built_in_user_profile_injection = off
memory_tool = off
session_memory_key = absent
raw_output_retained = false
active_axes = []
missing_axes = []
```

No `X-Hermes-Session-Key` reached the provider or Pantheon fixtures.

### Progressive tool disclosure

Hermes did not send the governed tools directly to the model. It exposed its native progressive-disclosure bridge:

```text
tool_search
tool_describe
tool_call
```

The deterministic provider executed the native sequence:

```text
tool_search for Pantheon context tools
→ tool_describe pantheon_context_manifest
→ tool_call pantheon_context_manifest
→ tool_describe pantheon_context_entity
→ tool_call admitted project
→ tool_call outside project
→ final response
```

Seven provider calls were observed. The underlying governed surface remained the two Pantheon tools qualified by `/v1/toolsets`.

```text
model-visible bridge tools != governed runtime tool surface
progressive discovery != tool authorization
```

### Streaming provider contract

The custom provider path sent `stream: true` and `stream_options`. A normal JSON completion was insufficient and produced `EmptyStreamError`.

The laboratory provider was corrected to emit OpenAI-compatible SSE chunks:

```text
chat.completion.chunk delta
→ finish_reason = tool_calls or stop
→ optional usage chunk
→ data: [DONE]
```

Streaming remained enabled; no runtime setting was weakened.

### SQLite safety fallback

The runner linked SQLite `3.45.1`. Hermes detected the affected WAL-reset range and selected DELETE journal mode. This was a safe laboratory fallback, not qualification of the production host database stack.

## End-to-end facts observed

The real Hermes run completed with:

```text
LAB_ACCEPTANCE_COMPLETED
```

The plugin performed these bounded reads:

```text
active Context Pack manifest
admitted entity project/project-lab
outside entity project/project-outside -> HTTP 404 refusal
```

The fixture state recorded:

```text
provider_calls = 7
pantheon_reads = 3
pantheon_writes = 3
```

The Pantheon binding recorded the runtime start and one terminal return. The return remained a technical candidate:

```text
pantheon_return_recorded = true
result_accepted = false
evidence_admitted = false
project_mutated = false
technical_receipt_is_evidence = false
scheduler_effect = false
retry_effect = false
```

The binding itself also reported:

```text
automatic_retry_performed = false
provider_routing_performed = false
model_override_performed = false
session_memory_header_sent = false
```

## Rollback facts observed

The operator sequence:

```text
disabled pantheon-context-bridge
stopped the Hermes gateway
verified /p/pantheon-governed was unreachable
```

The rollback receipt reported:

```text
plugin_disabled = true
gateway_stopped = true
profile_route_unreachable = true
```

## Distribution state deliberately unchanged

The standard distribution still contains exactly:

```text
run-binding
context-bridge
runtime-observer
```

The lock remains:

```text
status = candidate
artifact_digest = null
installation_state = not_observed
activation_state = not_activated
task_authorization_state = not_authorized
acceptance_state = not_run
```

The laboratory result does not justify changing those production-facing states.

## Non-equivalences

```text
lab installed != agency installed
lab route qualified != agency route qualified
synthetic run completed != result accepted
runtime return recorded != Evidence admitted
plugin enabled in lab != production binding activated
lab rollback succeeded != production rollback verified
lab acceptance passed != future tasks authorized
```

## Remaining production proof

`pantheon-mvp#227` remains open for:

```text
agency/NAS Hermes artifact digest
real pantheon-governed profile and keys
real OpenWebUI route and enrichment posture
real Pantheon API and human admission
real operator identity
real activation scope and expiry
real context boundary proof
real return and decision path
real rollback target and proof
production SQLite version or verified safe journal fallback
```
