# Pantheon Control — Implementation Phasing and Technical Risk Register

Status: candidate — to verify.

This document refines the Pantheon Control concept into phased implementation boundaries, technical risks and non-negotiable exclusions.

It is documentation only. It does not implement a dashboard, installer, runtime, queue, scheduler, provider router, connector gateway, approval engine or memory promotion engine.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Product thesis

Pantheon Control is valuable if it makes operational governance visible without becoming operational authority.

It should show:

```text
what exists
what is healthy
what is connected
what is authorized
what is blocked
what changed
what needs review
what must not run
```

It should not silently perform consequential work.

## Working definition

Pantheon Control is a governance-aware stack cockpit.

It is not:

```text
an AI runtime
an agent runtime
a workflow runner
a queue
a scheduler
a provider router
a plugin marketplace
a memory engine
a truth engine
an approval engine
```

The dashboard may display eligible routes. It must not secretly choose or execute them for consequential work.

## Recommended architecture

Candidate implementation architecture:

```text
Frontend V1: server-rendered UI with HTMX or similar light interactivity
Backend V1: FastAPI or equivalent minimal API server
Database: PostgreSQL
Reverse proxy: Caddy
Execution: external workers / Hermes / controlled scripts outside Pantheon Next
Observability: files + PostgreSQL first; Loki/Grafana later if justified
```

OpenWebUI remains the AI exposure surface. Pantheon Control remains the stack administration and governance cockpit. Portainer, if installed, remains a troubleshooting tool only.

## Implementation phases

### Phase 0 — static mockup

Goal:

```text
visualize the dashboard without operational behavior
```

Allowed:

```text
static HTML
fake module states
fake machine states
fake preflight results
fake logs
no secrets
no real calls
```

Exit criteria:

```text
user can understand dashboard structure
sections are not overloaded
state language is clear
risk boundaries are visible
```

### Phase 1 — read-only inventory

Goal:

```text
show what exists without changing anything
```

Allowed:

```text
read module registry
read instance manifest
read machine inventory
read endpoint registry
read model catalog
read generated config snapshots
show docs and ai_logs
show markdown preview
```

Forbidden:

```text
no install
no update
no backup restore
no connector write
no runtime execution
no external send
no memory promotion
```

Exit criteria:

```text
installed != connected != authorized is visible
machines and endpoints are visible
no action button can mutate external state
```

### Phase 2 — technical preflights

Goal:

```text
verify service availability and configuration compatibility
```

Allowed:

```text
health endpoints
version checks
port reachability
read-only API pings
config schema validation
versions.lock comparison
model list read
MCP tool list read
filesystem path checks
```

Forbidden:

```text
no write-capable probe outside sandbox
no real external send
no automatic provider route
no update apply
```

Exit criteria:

```text
technical health is separated from authorization
MCP reachable does not imply tool authorized
model present does not imply model allowed
```

### Phase 3 — governance preflights and refusal tests

Goal:

```text
verify that modules refuse forbidden usage
```

Allowed:

```text
sandbox refusal tests
external-action dry runs
memory auto-promotion refusal tests
browser submit refusal tests
GitHub direct merge refusal tests
vector retrieval-as-proof refusal tests
```

Forbidden:

```text
no real external effect
no production mutation
no silent bypass when refusal test fails
```

Exit criteria:

```text
modules that cannot refuse are marked non-compliant or suspended for that use
```

### Phase 4 — document/media intake preview

Goal:

```text
accept dropped files as candidates only
```

Allowed:

```text
template drop-zone detection
file hashing
quarantine
file type detection
safe preview
OCR / parsing sandbox
metadata extraction
candidate classification
```

Forbidden:

```text
no automatic approved template
no canonical memory
no validated source
no automatic workflow creation
```

Exit criteria:

```text
dropped file != approved template is enforced
Google Sheets pointers are not treated as content
```

### Phase 5 — config generation dry-run

Goal:

```text
generate operational config candidates without applying them
```

Allowed:

```text
generate docker-compose candidate
generate Caddyfile candidate
generate module config candidate
generate .env schema / redacted view
generate versions.lock candidate
show diffs
show conflicts
```

Forbidden:

```text
no write to live config
no docker compose up
no secret export
no automatic merge
```

Exit criteria:

```text
no visible diff, no change
conflicts are shown before application
```

### Phase 6 — backup and restore dry-run

Goal:

```text
prove portability before allowing mutation
```

Allowed:

```text
backup manifest generation
checksums
PostgreSQL dump dry-run plan
volume inventory
secret metadata export
restore plan preview
```

Forbidden:

```text
no restore over live stack without explicit later approval
no secrets in clear text
no connector write reactivation after restore
```

Exit criteria:

```text
archive can be verified
restore plan can be reviewed
write-capable connectors remain disabled after restore until revalidated
```

### Phase 7 — controlled updates

Goal:

```text
apply updates only when config compatibility is known
```

Allowed:

```text
update availability detection
compatibility matrix check
config migration dry-run
backup before update
healthcheck after update
rollback metadata
```

Forbidden by default:

```text
automatic major updates
PostgreSQL major update without manual plan
OAuth scope escalation
reverse proxy mutation without diff
write-capable connector updates without gate
```

Exit criteria:

```text
no compatible config, no update
no migration, no update
no backup, no update
```

### Phase 8 — gated operational actions

Goal:

```text
allow narrow administrative actions under explicit human gate
```

Allowed only after previous phases:

```text
restart service
apply approved config
run approved backup
restore into empty instance
trigger approved update
send approved test message to sandbox
```

Forbidden:

```text
silent production send
silent workflow execution
silent provider route
silent memory promotion
silent doctrine mutation
```

Exit criteria:

```text
human gate records action, diff, scope, evidence and operator decision
```

## Technical risk register

### Risk 1 — scope explosion

Cause:

```text
too many modules, connectors, media processors, runtimes and dashboards at once
```

Mitigation:

```text
phase by read-only first
one preferred tool per slot
fallbacks explicit
no broad marketplace
```

### Risk 2 — runtime creep

Cause:

```text
dashboard starts dispatching work rather than displaying eligibility
```

Mitigation:

```text
Pantheon Control displays routes
Hermes executes under Task Contract
external tools do the work
human decides
```

### Risk 3 — authorization confusion

Cause:

```text
reachable API treated as allowed action
```

Mitigation:

```text
technical_status != governance_status
connected != authorized
task_authorized required for consequential use
```

### Risk 4 — secrets exposure

Cause:

```text
.env, OAuth tokens, bot tokens or API keys stored or exported incorrectly
```

Mitigation:

```text
secret metadata only
redacted env view
encrypted secret export optional
permission diff on scope changes
write scopes blocked by default
```

### Risk 5 — unsafe file intake

Cause:

```text
user-dropped files processed as trusted templates
```

Mitigation:

```text
hash first
quarantine
parse as candidate
preview before approval
no automatic template approval
```

### Risk 6 — vector index drift

Cause:

```text
embedding model or dimension changes after indexing
```

Mitigation:

```text
store embedding model, dimension, source commit, hash and index timestamp
mark stale on mismatch
require reindex before use
```

### Risk 7 — backup illusion

Cause:

```text
copying live volumes without valid dumps, checksums or restore test
```

Mitigation:

```text
PostgreSQL dump
manifest
checksums
restore dry-run
connector revalidation
```

### Risk 8 — update breakage

Cause:

```text
image updated while config schema stays old
```

Mitigation:

```text
compatibility matrix
config schema version
migration dry-run
backup before update
healthcheck after update
rollback metadata
```

### Risk 9 — observability becoming surveillance

Cause:

```text
logs store raw client data, prompts, files or secrets
```

Mitigation:

```text
log metadata first
redact content
scope logs by project
retention policy
no secrets in logs
```

### Risk 10 — UI overload

Cause:

```text
all module, machine, preflight, log, metric and update details shown on one page
```

Mitigation:

```text
overview -> module detail -> raw logs/diff drill-down
human gate inbox for decisions only
```

## MVP cut line

The first real implementation should stop at read-only plus preflight display.

MVP includes:

```text
Overview
Module inventory
Machine inventory
Endpoint registry
Model catalog
Connection registry
Technical preflight display
Governance preflight display
Markdown viewer
Template drop-zone queue as preview only
Logs metadata viewer
No mutation buttons by default
```

MVP excludes:

```text
installing modules
updating modules
restoring backups
writing connectors
sending messages
mutating GitHub
promoting memory
routing providers automatically
```

## Success criteria

Pantheon Control is successful when an admin can answer these questions quickly:

```text
What is installed?
What is connected?
What is healthy?
What is authorized?
What is blocked?
What changed?
Which machine is used?
Which model is present?
Which data may leave the LAN?
Which preflight failed?
Which action needs human approval?
```

## Failure criteria

Pantheon Control fails if it becomes:

```text
a better-looking Portainer with doctrine labels
a hidden orchestrator
a loose plugin marketplace
a provider router
a memory engine
a dashboard that can send or mutate without explicit human gate
a system that treats extraction as proof
```

## Final rule

```text
Start with visibility.
Add refusal before action.
Add dry-run before mutation.
Add backup before update.
Add human gate before external effect.
```
