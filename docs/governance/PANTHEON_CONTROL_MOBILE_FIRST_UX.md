# Pantheon Control — Mobile-first UX

Status: candidate — to verify.

This document captures mobile-first UX constraints for Pantheon Control.

It is documentation only. It does not implement a mobile application, web UI, PWA, notification system, approval engine, connector gateway, runtime, queue, scheduler or external action mechanism.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Control should be usable from a phone first, because the user may need to review stack state, preflight failures, upload/drop documents, inspect alerts or approve a gated administrative action away from a desktop.

Mobile-first does not mean simplified governance. It means the critical governance state must be readable in one hand.

## Primary mobile jobs

The mobile UX should prioritize:

```text
see stack health
see blocked items
see human gates waiting
see failed preflights
see machine / endpoint availability
see whether data may leave the LAN
preview a dropped document
review a diff summary
read an incident timeline
copy or share a diagnostic summary
```

Mobile should not prioritize dense configuration editing.

## Screen hierarchy

The first mobile screen should answer four questions:

```text
Is the stack safe?
What is broken?
What needs my decision?
What changed recently?
```

Suggested mobile navigation:

```text
1. Overview
2. Gates
3. Alerts
4. Preflights
5. Modules
6. Machines
7. Documents
8. Logs
9. Settings
```

Advanced areas such as config generation, update application, restore and expert overrides should stay desktop-first or require an explicit expert unlock.

## Mobile information pattern

Use progressive disclosure:

```text
summary card
status reason
required action
details
raw logs / diff
```

Do not show raw logs, giant tables, full docker-compose diffs or dense connection graphs by default on mobile.

## Cards over tables

Mobile views should prefer cards over tables.

Example module card:

```text
Hermes Agent
Status: healthy
Authorization: task_authorized for sandbox only
Risk: medium
Last preflight: pass_with_gate
Next action: none
```

Example blocked action card:

```text
Telegram outbound
Status: blocked
Reason: external action requires human gate
Scope: project / demo
Action: review draft
```

## Decision safety

Mobile gates must be hard to approve accidentally.

Required pattern for consequential approval:

```text
summary
risk
scope
diff or evidence summary
explicit action wording
hold-to-confirm or second confirmation
post-action receipt
```

The primary button must never hide the consequence. Bad: `OK`. Better: `Approve sandbox Telegram test send`.

## Mobile-first status language

The UI should use short but precise labels:

```text
Healthy
Degraded
Blocked
Needs review
Candidate only
Read-only
Write gated
External
Local only
Unknown egress
```

Avoid vague labels such as:

```text
Active
Ready
Smart
Connected
Synced
```

because they collapse technical status and authorization status.

## Offline and degraded behavior

Mobile may be used over unstable network conditions.

The dashboard should clearly distinguish:

```text
stale view
last checked time
live status
unknown status
unreachable machine
blocked by policy
```

A stale green status must not look like a current green status.

## Template drop zones on mobile

Mobile should support document intake, but only as candidate intake.

Allowed mobile actions:

```text
upload document to inbox
photograph or scan a document into inbox
preview parsed result
mark as candidate template
reject or archive candidate
```

Forbidden by default:

```text
approve template automatically
promote memory
create workflow
send extracted content externally
```

## Logs and metrics on mobile

Mobile logs should start as summaries:

```text
latest failures
latest gates
latest external egress
latest updates
latest preflight failures
```

Raw logs should be available only behind detail views and should be redacted by default.

## Connection graph on mobile

A full graph is usually poor on mobile.

Mobile should show path cards instead:

```text
OpenWebUI -> Hermes -> SearXNG
Status: read-only candidate search
Risk: low
Gate: none
```

```text
Hermes -> Telegram
Status: connected, outbound gated
Risk: external action
Gate: required
```

Desktop may show a graph. Mobile should show explainable paths.

## Visual density

Mobile cards should avoid decorative noise. Prioritize:

```text
one status
one reason
one next action
one drill-down
```

Long doctrine text should appear as `why this is blocked` help, not as default content.

## Accessibility

Minimum UX requirements:

```text
large tap targets
keyboard navigability where applicable
high contrast status markers
status not communicated by color alone
readable monospace blocks
copy buttons for diagnostics
reduced motion option
```

## PWA candidate

A future implementation may consider a Progressive Web App for:

```text
home-screen shortcut
local cache of last safe status
upload/share target
push notifications for gates or incidents
```

Push notifications must be opt-in and must not include sensitive dossier content by default.

## What mobile must not become

Mobile convenience must not weaken governance.

Mobile must not become:

```text
one-tap approval for external actions
silent runtime trigger
unreviewed update button
unrestricted file uploader
raw secret viewer
provider router
memory promotion shortcut
```

## MVP mobile cut line

Mobile MVP includes:

```text
Overview
Human Gate Inbox read-only / review mode
Alerts
Preflight summaries
Machine and endpoint status
Template inbox preview
Redacted logs summary
Copy diagnostic bundle summary
```

Mobile MVP excludes:

```text
expert config edits
update application
restore application
secret editing
connector scope escalation
production external send
```

## Final rule

```text
Mobile-first means the critical state is visible anywhere.
It does not mean consequential action becomes easier than review.
```
