# Meetily Capability Review

Status: external reference / sensitive capability candidate review — documented non-implemented.

Review date: 2026-07-07.

Repository: `Zackriya-Solutions/meetily`.

Reviewed source: `https://github.com/Zackriya-Solutions/meetily`.

This review records a sensitive candidate capability for Pantheon Next. It does not adopt, clone, install, execute, configure, approve, record, transcribe, summarize, export, update, benchmark or add Meetily as a dependency.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Short assessment

Meetily is an interesting candidate for local meeting capture, transcription and meeting-minute preparation.

It is not a near-term integration candidate.

Recommended outcome:

```text
quarantined_capability_candidate
```

with strict default:

```text
reference review only;
no agency installation;
no client meeting use;
no audio capture test with confidential material;
analytics must be reviewed and disabled before any sandbox;
updater must be governed before any sandbox;
external providers must be blocked unless explicitly approved.
```

## Abstract function

```text
Capture, transcribe and summarize meetings.
```

Capability Slot:

```yaml
capability_slot:
  id: meeting_capture_transcription
  title: Meeting Capture and Local Transcription
  abstract_function: record or import meeting audio, transcribe it, prepare transcript and summary candidates
  expected_inputs:
    - microphone audio
    - system audio
    - imported audio files
    - local speech-to-text model
    - optional summary provider
  expected_outputs:
    - Transcript Candidate
    - Meeting Summary Candidate
    - Action Candidate
    - Decision Candidate
    - Runtime Status Candidate
  forbidden_outputs:
    - validated meeting minutes
    - approved decisions
    - automatic external transmission
    - automatic memory promotion
    - client-facing record without review
```

## Candidate binding

```yaml
candidate_binding:
  id: meetily-desktop-local
  runtime_owner: external_desktop_runtime
  execution_surface: local Tauri desktop app outside Pantheon
  exposure_surface: future OpenWebUI or cockpit projection only after adapter review
  pantheon_role: govern consent, status, provider boundary, transcript validation, export and memory gates
```

Binding selected does not mean dependency adopted.

## What Pantheon governs

Pantheon governs:

```text
recording consent;
confidentiality scope;
provider admissibility;
analytics admissibility;
update authorization;
local storage and deletion policy;
transcript status;
summary status;
decision extraction status;
export approval;
meeting-minute validation;
memory promotion;
external communication gates.
```

Pantheon must not record, transcribe, summarize, store audio, join meetings, export minutes, send summaries or manage the desktop application.

## What Hermes may execute

No Hermes execution is currently approved.

A future Hermes-side adapter could, if separately authorized:

```text
read exported transcript files;
classify Transcript Candidates;
extract Decision Candidates;
prepare Meeting Summary Candidates;
prepare Action Candidates;
return Evidence Pack Candidates;
```

Hermes must not start recording, bypass user consent, auto-join meetings, send minutes or promote meeting memory.

## What OpenWebUI may expose

OpenWebUI may eventually expose:

```text
Meeting Candidate Card;
Transcript Candidate Card;
Summary Candidate Card;
Decision Candidate Card;
Action Candidate Card;
Consent Gate;
Export Gate;
Memory Gate;
provider and analytics warnings.
```

OpenWebUI must not turn an imported transcript or summary into a validated compte rendu.

## What the human approves

Human approval is required for:

```text
any recording;
any participant-consent posture;
any client or professional meeting use;
any external provider use;
any analytics allowance;
any export;
any transformation into formal meeting minutes;
any extracted decision;
any action list;
any memory promotion;
any update.
```

## Forbidden by default

```text
automatic recording;
auto-join;
client meeting capture;
external provider summary;
analytics telemetry;
unreviewed updater;
automatic export;
automatic decision validation;
automatic memory promotion;
production activation.
```

## Status classification

```yaml
repository_status: active_public_repository_with_renaming_signals
governance_status: capability_candidate_to_verify
runtime_status: not_installed
install_status: absent
health_status: unknown
update_status: unknown
activation_status: unavailable
implementation_status: documented_non_implemented
safe_default: reference_only_quarantine
```

## Risk review

| Risk | Classification | Gate |
|---|---|---|
| Audio capture without valid consent | critical | recording_consent_gate |
| Client or confidential meeting exposure | critical | client_data_gate |
| External provider call for summary | high | external_provider_gate / data_exit_gate |
| Analytics telemetry | high | analytics_gate |
| Updater changes behavior after review | high | update_authorization_gate |
| Transcript treated as proof | high | evidence_quality_gate |
| Summary treated as compte rendu validé | high | transcript_validation_gate / approval_gate |
| Decisions extracted automatically | high | decision_validation_gate |
| Memory promoted from meeting notes | high | memory_promotion_gate |
| Local desktop app has broad file or host permissions | high | external_runtime_review_gate |

## Required gates

```text
recording_consent_gate
privacy_scope_gate
client_data_gate
analytics_gate
external_provider_gate
data_exit_gate
update_authorization_gate
transcript_validation_gate
meeting_minutes_approval_gate
decision_validation_gate
export_approval_gate
memory_promotion_gate
external_runtime_review_gate
```

## Quarantine conditions

Meetily remains blocked from sandbox use until these points are reviewed:

```text
analytics can be disabled and verified;
updater behavior is understood and governable;
local storage path and deletion policy are documented;
external providers are disabled by default;
meeting export format is inspected;
recording consent UX is reviewed;
renaming / repository-release relationship is clarified;
Windows agency compatibility is tested without client data.
```

## Future sandbox test proposal

Allowed only after quarantine blockers are cleared:

```text
Use synthetic or deliberately created test audio.
No client data.
No real meeting.
No external provider.
No analytics.
No auto-update.
Export transcript only.
Review transcript error rate and status model.
Do not promote to memory.
Do not generate formal minutes without human validation.
```

Expected result:

```text
Transcript Candidate
Summary Candidate if local model only
Risk Notes
Capability Gap list
Gate Recommendation
```

## Decision

```yaml
decision_recommendation: quarantined_capability_candidate
reason: useful meeting workflow potential but high-risk data capture, consent, telemetry, updater and provider surfaces must be governed before any test
default_activation: forbidden
next_allowed_step: documentation review only
```

## Boundary phrase

```text
Meetily may capture and summarize.
That makes it sensitive, not authoritative.
Pantheon governs consent, status, export and memory.
The human decides.
Nothing is recorded, exported or remembered by default.
```
