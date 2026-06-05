# Pantheon Control — Repository Placement

Status: candidate — to verify.

This document records the placement decision for Pantheon Control.

Pantheon Control should be part of Pantheon Next, but not by collapsing governance doctrine, runtime execution and operational instance state into one uncontrolled repository.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
Pantheon Control makes governed stack state visible.
```

## Decision

Pantheon Control belongs to the Pantheon Next project.

That means:

```text
Pantheon Next owns the concept, doctrine, vocabulary, specs, templates, phasing, boundaries and validation rules.
```

It does not mean:

```text
Pantheon Next immediately becomes a runtime, Docker stack, scheduler, queue, provider router, connector gateway, secret store, approval engine or memory promotion engine.
```

## Placement model

Pantheon Control has three placement layers.

### Layer 1 — Governance and specification

Location:

```text
docs/governance/
templates/
docs/assets/ when needed
ai_logs/
```

Allowed now:

```text
doctrine
candidate specs
module and connection vocabulary
mobile-first UX notes
implementation phasing
static mockup requirements
fictional examples
non-executable templates
AI logs
```

This layer is already valid for Pantheon Next.

### Layer 2 — Static mockup

Location candidate:

```text
docs/assets/pantheon-control/
```

Allowed after explicit acceptance of the mockup step:

```text
static HTML
static CSS
fake JSON fixtures
screenshots
mobile-first prototype
no network calls
no secrets
no runtime behavior
no filesystem mutation
```

Purpose:

```text
validate UX and state language before implementation
```

A static mockup may live in Pantheon Next because it is documentation and design support, not operational runtime.

### Layer 3 — Executable implementation

Location candidate, only after explicit validation:

```text
apps/pantheon-control/
```

or, if repository separation is later preferred:

```text
Pantheon-Control as a sibling repository under the Pantheon Next project umbrella
```

Executable implementation must not be added implicitly through this candidate PR.

Before executable code is added, a future decision must define:

```text
repository path
runtime boundary
data storage boundary
secret handling
write permissions
operator approval model
deployment model
rollback model
security review
```

## Instance state boundary

Even if Pantheon Control belongs to Pantheon Next, operational instance state should remain outside the governance repository.

Outside Pantheon Next by default:

```text
.env
secrets
OAuth tokens
live docker-compose.yml
live Caddyfile
PostgreSQL data
Qdrant collections
OpenWebUI user data
Hermes runtime state
ComfyUI models and outputs
uploaded user documents
backup archives
machine inventory instance file
endpoint registry instance file
model catalog instance file
logs with private content
```

Pantheon Next may define the shapes, templates and validation rules for these artifacts. It should not store live sensitive instance data.

## What Pantheon Next owns

Pantheon Next owns:

```text
Pantheon Control doctrine
status vocabulary
module manifest expectations
connection typing
preflight result shape
refusal test doctrine
mobile-first UX constraints
repository allowlist rules
config compatibility doctrine
backup / restore doctrine
update gate doctrine
human gate requirements
```

## What Pantheon Control may later do

If implemented, Pantheon Control may:

```text
show inventory
show machine and endpoint state
show model catalog
show preflight results
show diffs
show logs metadata
show usage metrics
show drop-zone candidates
show update readiness
show backup readiness
show human gates
```

Later gated actions may be added only after phased validation.

## What Pantheon Control must not become

Pantheon Control must not become:

```text
hidden runtime
agent loop
provider router
message queue
scheduler
uncontrolled connector gateway
plugin marketplace
automatic updater
automatic backup restorer
automatic approval surface
automatic memory promoter
truth engine
```

## Repository relationship to OpenWebUI and Hermes

OpenWebUI remains the user-facing AI exposure surface.

Hermes remains the external execution runtime.

Pantheon Control belongs to Pantheon Next as the governance-aware stack cockpit. It may display OpenWebUI and Hermes status, but it does not replace them.

## Practical repository rule

Current PRs may add:

```text
docs/governance/PANTHEON_CONTROL_*.md
ai_logs/*pantheon-control*.md
docs/assets/pantheon-control/* static mockups, if explicitly accepted
```

Current PRs must not add:

```text
Docker files
operations procedures
platform deployment files
live .env files
runtime source code
connector implementations
scheduler or queue code
secret storage
```

unless a later explicit review promotes that implementation phase.

## Final rule

```text
Pantheon Control is part of Pantheon Next as a governed subsystem.
Its live operational state is not part of the governance repository.
Its executable implementation requires a later explicit promotion.
```
