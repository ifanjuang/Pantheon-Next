# PAIR + Unsloth Runtime Qualification

Status: candidate qualification plan. No live lab has been executed by this document.

## Objective

Determine whether NVIDIA Personal AI Router (PAIR) can safely provide the external physical inference-routing layer for Pantheon's local GPU fleet, and whether Unsloth can be used as a separate local Hermes model/provider surface, without adding a Pantheon scheduler, inference router, runtime owner, memory owner, or authorization path.

The exact external artifacts are owned only by `implementation/qualification/external-pins.json`. Upstream observations are owned separately by `implementation/qualification/external-upstream-observations.json`.

## Authority boundary

The candidate composition under qualification is:

```text
Pantheon
  -> governs capability / admission / consequence
Hermes
  -> semantic orchestration and selected provider/model use
PAIR
  -> physical placement of an eligible Ollama/LM Studio request
Ollama / LM Studio
  -> inference execution on one node

Hermes
  -> optional custom OpenAI-compatible provider binding
Unsloth
  -> separate local inference / training / quantization surface
```

PAIR is not a Pantheon authorization owner. Unsloth is not a second Hermes owner. A successful request does not become Evidence.

## Existing seams that make the lab necessary

The Ubuntu deployment candidate currently installs and starts Ollama itself on the standard Ollama port. PAIR can expose that same standard port as its local compatibility proxy and may relocate a PAIR-managed backend behind it. The ownership interaction must therefore be observed before any deployment change.

The Ubuntu deployment candidate currently runs Hermes in Docker Compose. PAIR's source-reviewed plaintext client ingress is loopback-only, while paired peer traffic uses cluster mTLS. The current container-to-host path must be executed as-is before proposing host networking, a native Hermes process, or any relay.

These are qualification questions, not conclusions about the live environment.

## Q1 sequence

### Q1A — isolated PAIR on the always-on Linux GPU node

Use an isolated test setup rather than the Pantheon Ubuntu deployment candidate. Resolve the selected PAIR artifact from the external pin registry. Record the exact installed artifact identity.

Observe service lifecycle, Ollama ownership mode, standard-port proxy behavior, backend relocation when PAIR owns the engine, one-model inference, Jobs/workload visibility, and uninstall/reset behavior. Confirm model weights are retained when PAIR is removed unless the engine/model store is explicitly deleted.

No Pantheon deployment file changes are part of Q1A.

### Q1B — add the always-on Windows GPU node

Pair the Linux and Windows nodes explicitly. Put the same bounded test model on both engines as independent copies.

Generate concurrent independent requests and record which node serves them. Stop or power down one node and confirm it becomes ineligible while the remaining node continues serving. Return the node and observe whether it becomes eligible again.

Do not interpret success as pooled VRAM, model sharding, or one request split across machines.

### Q1C — current Hermes container to local PAIR proxy

Use the current Pantheon candidate Compose networking path without first adding a workaround. Send a bounded Hermes/provider request to the local PAIR proxy.

Record the HTTP status, PAIR error if any, and the caller network identity visible at the proxy boundary. In particular, do not pre-record `403` as the result merely because source review indicates a loopback-only gate.

If the current path is refused, end Q1C with an observed finding. Host networking, native Hermes, or a relay are separate candidate experiments and must not be smuggled into the same result.

### Q1D — Unsloth through the existing Hermes provider seam

Resolve the Unsloth target from the external pin registry and run an isolated local Unsloth endpoint.

Configure the existing Hermes candidate with a named custom OpenAI-compatible provider pointing to that endpoint. Do not use `unsloth start hermes` for this qualification because the target question is provider compatibility with the existing Hermes runtime, not creation of a second session-scoped Hermes home.

Observe endpoint health, streaming, tool-call round trip, context behavior, provider error behavior, and whether the `pantheon-governed` Hermes profile remains unchanged outside the explicit provider configuration under test.

Unsloth does not enter the PAIR cluster in Q1. Current PAIR engine support and generic external OpenAI-compatible endpoint support are separate upstream concerns.

### Q1E — classify without activating

Classify PAIR and Unsloth independently as `accepted`, `rejected`, or `unresolved` candidates from recorded observations. A PAIR result must not automatically decide Unsloth, and vice versa.

Before any later deployment PR, the review must explicitly resolve or retain as open:

- Ollama process/port ownership between the Pantheon bootstrap candidate and PAIR;
- Hermes container access to PAIR's local client ingress;
- rollback behavior;
- exact runtime artifact identities;
- supported model/engine scope;
- network exposure and telemetry posture;
- whether the resulting topology removes duplication rather than adding another routing path.

## Q1 done gate

Q1 is complete only when every required check in `tests/fixtures/pair_unsloth_runtime_q1.json` has a real recorded result and the two candidates have an explicit classification.

The Q1 planning PR must remain `live_executed = false` and every stage `not_run`. A later observation PR may change those fields only from actual lab records.

No Q1 planning result may change `deployment/ubuntu/release.env`, `deployment/ubuntu/install-node`, the Hermes distribution lock, runtime activation state, task authorization, or Evidence state.

## Non-equivalences

```text
retrieved upstream information != truth about the live machine
upstream observed != qualification pin selected
qualification pin selected != runtime observed
runtime observed != runtime qualified
runtime qualified != runtime activated
PAIR node reachable != model approved
PAIR routing success != Pantheon authorization
Unsloth endpoint configured != provider authorized
runtime success != Evidence
projection != persistence
```
