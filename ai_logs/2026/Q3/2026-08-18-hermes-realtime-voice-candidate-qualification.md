# 2026-08-18 — Hermes realtime voice candidate qualification

Status: validation-only trace — external runtime candidate, not adopted.

Boundary profile: `external_reference_review`.

## Objective

Record the 2026-08-18 realtime-voice qualification around Hermes without creating a Pantheon Voice subsystem, a new doctrine owner, a provider router, an audio runtime or an adoption decision.

The durable owner already exists in `docs/governance/HERMES_INTEGRATION.md`:

```text
Hermes/runtime reach -> adapter concern
Pantheon -> scope, provenance, Evidence boundaries, approvals and consequential authorization
```

Therefore the earlier proposal to add `docs/governance/HERMES_REALTIME_VOICE_CANDIDATE.md` is intentionally not retained as a separate governance document.

## Boundary retained

```text
Audio surface / car / browser / phone
        -> external voice runtime
        -> Hermes
        -> existing Pantheon governed interfaces when required
```

Realtime audio transport, STT, TTS, VAD, interruption, playback state and session mechanics remain outside Pantheon Next.

Pantheon does not gain a `Voice` schema, `VoiceResult`, telephony runtime, speech-model registry, scheduler or audio provider router from this qualification.

```text
voice available != task authorized
transcript != truth
spoken response != approval
runtime success != Evidence
binding selected != dependency adopted
```

## Candidate direction observed on 2026-08-18

The preferred sandbox direction at the review date was:

1. the Hermes upstream `voice_server` gateway direction tracked in `NousResearch/hermes-agent` PR #27040;
2. the companion local runtime `tmylk/hermes-plugin-voice-pipecat`.

At that review date the upstream `voice_server` contract was not merged. The pair was therefore classified only as:

```text
binding_status: to_verify
installation_status: not established by Pantheon
activation_status: not activated
production_status: not authorized
Pantheon dependency: no
```

This trace does not assert that those upstream states remain unchanged after 2026-08-18.

## Why the direction fit the existing architecture

The observed split kept replaceable runtime choices outside Pantheon:

```text
external voice runtime
- microphone / speaker transport
- WebRTC or equivalent transport
- STT / TTS
- VAD / turn detection
- interruption / barge-in
- playback state

Hermes
- conversation session
- history
- tools
- runtime memory/context
- agent turns
- background delegation
- steering/stopping delegated work

Pantheon
- governed scope
- provenance
- Evidence boundaries
- approvals
- consequential authorization
```

No STT, TTS, speech-to-speech model or transport is canonicalized by this trace.

## Conversation and delegation posture

The useful target behavior was conversational continuity while harder work executes through Hermes delegation:

```text
user speech
    -> external realtime voice runtime
    -> Hermes conversational turn

simple request
    -> immediate answer

complex request
    -> Hermes background/delegated work
    -> authorized tools / governed context
    -> candidate result returned to the live Hermes session
    -> spoken restitution
```

A conversational model and delegated worker may differ. Neither the voice runtime nor model agreement becomes professional authority.

## Alternatives observed

### `TheSmokeDev/hermes-talk`

Retained as a useful OpenAI-Realtime-oriented reference/fallback experiment at the review date, not as the preferred local/provider-replaceable binding.

### Hermes conventional voice path

Retained as the lower-risk fallback for functional validation when a provider-neutral realtime gateway is unavailable.

### Local full-duplex speech models

Watch only. No model is selected by Pantheon. French quality, tool reliability, hardware requirements and runtime maturity must be qualified on the actual target before use.

## Validation gate before any promotion

Any future realtime-voice binding remains `to_verify` until a bounded sandbox demonstrates at least:

- usable French conversation on the selected target;
- acceptable latency during concurrent conversation and delegated work;
- interruption/barge-in without corrupting Hermes session history;
- background delegation while the live conversation remains usable;
- steering/stopping a delegated task without cross-session leakage;
- result return into the originating voice session;
- bounded CPU/GPU/RAM use;
- governed project context obtained only through existing Pantheon interfaces;
- provenance and uncertainty preserved in spoken restitution;
- consequential effects still passing through the existing approval/policy path;
- clean rollback to non-realtime Hermes interaction;
- no new Pantheon runtime or provider-routing responsibility.

## Re-evaluation triggers

Recheck the candidate rather than relying on this dated trace when:

- Hermes ships or changes a provider-neutral realtime voice contract;
- the referenced upstream `voice_server` direction is merged, closed or redesigned;
- the Pipecat companion materially changes its session/protocol boundary;
- Hermes gains a native local realtime path that makes the external runtime unnecessary;
- a mature French full-duplex model materially simplifies the runtime stack;
- SIP/phone/CarPlay becomes an actual implementation requirement.

## Result

```text
voice responsibility -> already covered by Hermes integration boundary
new governance owner -> not justified
new Pantheon schema/runtime -> not justified
candidate binding -> historical 2026-08-18 qualification only
adoption -> no
activation -> no
production authorization -> no
```

The correct convergence is to keep the durable rule in the existing Hermes integration owner and keep implementation-specific candidate detail in a dated qualification trace.
