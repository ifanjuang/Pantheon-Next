# Pantheon Control — Observability, Usage Metrics and Voice Options

Status: candidate — to verify.

This document captures candidate dashboard functions for diff views, logs, usage metrics, telemetry, cost visibility, voice input and French voice output for OpenWebUI-facing use.

This is documentation only. It does not implement telemetry collection, audio routing, OpenWebUI configuration, TTS/STT services, dashboards, exporters, billing, queues, schedulers or automatic provider routing.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Control should make operational changes, module behavior and usage visible.

The dashboard should answer:

```text
what changed?
who changed it?
which module was used?
which route was selected?
which model answered?
which data left the LAN?
which gate blocked the action?
what did it cost?
how long did it take?
which preflight failed?
which logs support the diagnosis?
```

Observability is not proof. Metrics and logs support review; they do not validate truth, approve action or promote memory.

## Diff surfaces

Pantheon Control should expose diffs for governed and operational changes.

Required diff views:

```text
repository diff
Markdown rendered diff
configuration diff
docker-compose diff
.env schema / redacted diff
module selection diff
connection registry diff
machine inventory diff
endpoint registry diff
model catalog diff
preflight result diff
permission / OAuth scope diff
version lock diff
backup manifest diff
```

Diffs should be shown before applying changes.

Blocking rule:

```text
No visible diff, no expert change.
No compatible config diff, no update.
No permission diff, no OAuth scope escalation.
```

## Logs

Pantheon Control should centralize pointers to logs without pretending logs are evidence by themselves.

Log families:

```text
install logs
update logs
backup / restore logs
healthcheck logs
preflight logs
Hermes execution logs
OpenWebUI interaction logs where available
connector logs
MCP tool discovery logs
browser worker logs
OCR / document processing logs
transcription logs
model endpoint logs
sync logs
incident logs
```

Each log entry should carry:

```text
timestamp
instance
machine
module
connection
operation
scope
status
risk
correlation id
task contract id when applicable
result candidate id when applicable
evidence candidate id when applicable
```

Logs must be filterable by project, module, machine, time range, status and risk.

## Usage metrics

Usage metrics should be shown at dashboard level and per module.

Metrics:

```text
requests count
tokens in / out where available
local vs external model calls
model used
endpoint used
latency
error rate
retry count
queue time if any external runtime reports it
storage used
vector index size
OCR pages processed
audio minutes transcribed
files processed
backup size
preflight pass / fail / blocked counts
human gate approvals / refusals / deferrals
external actions blocked / approved
```

Usage metrics should distinguish:

```text
local
LAN
VPN
external provider
unknown egress
```

The dashboard should make it easy to see when a task used a cloud model or external API.

## Cost and resource view

Optional cost tracking should support:

```text
API cost estimates
model provider costs
GPU time
CPU time
storage growth
backup growth
transcription minutes
OCR pages
ComfyUI generation counts
```

Cost estimates are operational estimates, not accounting records.

## Privacy and egress metrics

The dashboard should expose:

```text
which module sent data out
which endpoint received it
which provider was used
which scope authorized it
which gate approved it
which data category was involved
```

Unknown egress should be treated as degraded or blocked depending on policy.

## Voice input

Voice input should be split from voice output.

Speech-to-text slot:

```text
Primary local: faster-whisper
CPU fallback: whisper.cpp
External API fallback: gated by privacy policy
```

Preflight checks:

```text
microphone or uploaded audio accepted
sample audio transcribed
language auto-detection works or forced French works
model present
local-only mode respected
external STT blocked unless approved
```

Voice input produces a text candidate. It is not a validated instruction until scoped and accepted by the user.

## French voice output for OpenWebUI-facing use

Text-to-speech should be configurable as a user-facing voice option.

Recommended candidate slot:

```text
Primary local TTS candidate: Piper with French voice models
Fallback: browser/system TTS if acceptable
External TTS provider: gated by privacy and cost policy
```

Dashboard controls:

```text
TTS enabled / disabled
voice language: French
voice choice
speed
volume
sample playback
local-only mode
external provider disabled by default
OpenWebUI endpoint integration status
```

The dashboard should not hard-code one French voice forever. It should expose a small curated allowlist of French voices with sample playback and admin selection.

Voice output is presentation. It must not create memory, proof, approval or external action.

## Voice governance

Rules:

```text
A spoken answer is only a rendering of a textual result.
The text result remains the reviewable object.
TTS does not approve anything.
STT does not turn speech into a validated Task Contract without review.
External voice providers require explicit privacy review.
```

## Suggested dashboard views

```text
Diff Center
Log Explorer
Usage Metrics
Cost / Resource View
Privacy / Egress View
Voice Settings
Audio Preflights
Model / Endpoint Metrics
Human Gate Inbox
Incident Timeline
```

## Preflight checks

Minimum checks:

```text
render a Markdown diff safely
show config diff before update
read latest install/update/preflight logs
filter logs by module and task id
record usage metric from a sandbox task
show local vs external route
block unknown egress
transcribe a French audio sample
play a French TTS sample
verify TTS stays local if local-only mode is enabled
verify external TTS is blocked without approval
```

## Boundary

Pantheon Control may display metrics, logs and traces.

It must not:

```text
turn logs into proof
turn metrics into approval
turn voice input into an authorized task without review
turn voice output into a decision
route to external providers silently
collect unnecessary private telemetry
```

## Open questions

```text
Should logs be stored in PostgreSQL, Loki, files, or all three by role?
Should Langfuse be allowed as optional AI trace observability?
Should voice output be implemented through OpenWebUI settings, a local TTS endpoint, or browser TTS first?
Which French TTS voices should be allowlisted?
Should external TTS providers be disabled by default for all professional dossiers?
How long should usage metrics be retained?
```

## Final rule

```text
Metrics explain operation.
Logs support diagnosis.
Diffs constrain change.
Voice renders interaction.
None of them decide.
```