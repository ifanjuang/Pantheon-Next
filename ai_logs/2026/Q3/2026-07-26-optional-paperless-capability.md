# AI intervention trace — Optional Paperless capability

Date: 2026-07-26
Status: validation-only trace
Boundary profile: validation_only_trace.

## Human direction

The repository owner explicitly decided that Paperless-ngx should not be mandatory for Pantheon document ingestion.

The required architectural distinction is:

```text
document_ingestion
  core capability

governed local/NAS source
  default supported source path

document_source_management
  optional Capability Slot

preferred binding
  paperless_ngx
```

Paperless remains recommended for a professional DMS deployment but is not a prerequisite for a valid Pantheon installation.

## Repository recheck

Before implementation, active repository authority/status documents and recent commits were re-read.

During external implementation, `pantheon-mvp/main` advanced with Hermes Runs API, launch-junction and operator live-acceptance work. The optional-Paperless change was therefore rebuilt on that newer main rather than overwriting those updates.

External result:

```text
repository: ifanjuang/pantheon-mvp
PR: #84
merge: d8d51d587bc7b28bb313f4148668f42da655d990
CI: green
```

## External implementation

`compose.phase-b.yaml` now places these services behind the optional Compose profile `paperless`:

```text
paperless-broker
paperless-db
paperless
paperless-gateway
```

Core Phase B remains:

```text
pgvector
Docling when selected
Cockpit API
Hermes Agent
document-runtime observer
```

Core invocation:

```bash
docker compose -f compose.phase-b.yaml up -d
```

Optional Paperless binding:

```bash
docker compose -f compose.phase-b.yaml --profile paperless up -d
```

Hermes core no longer receives Paperless gateway configuration by default.

## Observation semantics

The network observer now receives explicit binding selection:

```text
PANTHEON_PAPERLESS_BINDING_SELECTED=false | true
```

When Paperless is not selected, it performs no Paperless gateway request and records:

```text
binding_status = not_selected
installation_status = not_applicable
reachability_status = not_applicable
health_status = not_applicable
```

When selected, the bounded Paperless gateway probe is enabled normally.

Preserved distinctions:

```text
Paperless absent != Pantheon degraded
Paperless absent != document ingestion unavailable
Paperless installed != binding selected
binding selected != activated
```

## Core ingestion boundary

The existing external runtime already supports declared local/NAS source ingestion through:

```text
Task Contract source declaration
-> resolved-path boundary
-> source digest
-> reviewed extraction binding when needed
-> Project Document candidate
-> optional later governed Knowledge publication
```

This path remains subject to Pantheon scope, provenance, Knowledge and Evidence rules. Paperless optionality does not create unmanaged ingestion.

## Pantheon Next documents reconciled

```text
docs/governance/COMMON_INSTALLATION_BASELINE.md
docs/governance/WHAT_RUNS.md
docs/governance/DOCUMENT_RUNTIME_LIVE_OBSERVATIONS.md
docs/governance/authority/RUNTIME_ADAPTERS_AUTHORITY_INDEX.md
docs/install/PORTAINER_PHASE_B_HANDOFF.md
docs/install/PAPERLESS_INITIAL_INSTALLATION.md
```

The Paperless installation document remains as an operator artifact but now applies only after explicit selection of the optional Capability Slot.

## Responsibility allocation

```text
Pantheon governs
  capability selection status
  source scope/provenance
  activation/adoption semantics
  Knowledge/Evidence boundaries

Hermes executes
  core governed work
  Paperless-specific skill only when selected/configured

OpenWebUI exposes
  core document/cockpit surfaces
  optional Paperless source surfaces only when binding exists

Paperless executes
  DMS/source-management functions only when selected

Human approves
  Paperless installation/selection/activation
  real-dossier use
```

## Forbidden interpretation

```text
Paperless optional != Paperless deprecated
Paperless absent != fallback around Task Contract scope
Paperless profile enabled != binding activated
local source available != unrestricted filesystem access
runtime success != Evidence
```

## Target status

At the time of this trace:

```text
optional Paperless runtime implementation   merged externally
Pantheon optional-capability doctrine       candidate branch / review pending
target Paperless installation               not established
target local/NAS ingestion proof            not established
target health                               not established
activation                                  not authorized
real-dossier use                            not authorized
production adoption                         not decided
```

This trace creates no runtime behavior or authority.
