# Pantheon Control Installation Boundary

Status: candidate support doctrine — installation boundary for Pantheon Control.

This document records where installation work belongs and what it must not become.

It is documentation only. It does not implement an installer, Docker stack, platform service, operations procedure, dashboard, MCP server, scheduler, queue, approval engine, memory engine or external action.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

Pantheon Control may later provide a practical installation and administration surface for a local professional AI stack.

The installation layer is allowed to make setup visible, repeatable and reversible. It must not silently turn Pantheon Next into the runtime it governs.

This document separates installation work from MCP Policy Server work.

```text
Installation prepares the local environment.
MCP Policy Server exposes governance validation and candidate preparation.
Hermes executes under contract.
Pantheon remains the source of governance status.
```

## Placement

Installation work belongs under Pantheon Control, not in the MCP policy layer.

Recommended candidate placement:

```text
pantheon-control/
  installer/
  dashboard/
  mcp-policy-server/
```

The `installer/` slice may later contain scripts, templates and presets only after its governing spec is accepted.

The `mcp-policy-server/` slice remains separate. It may be installed by Pantheon Control, but it must stay read-only / validation / candidate-preparation unless a later governed decision explicitly authorizes more.

## Installation scope

The installer may prepare or verify:

```text
Docker presence
Docker Compose presence
local network presence
OpenWebUI service configuration
Hermes service configuration
Ollama endpoint reachability
Pantheon Next repository path
Pantheon MCP Policy Server service presence
read-only repository mount
local configuration file generation
preflight visibility
```

The installer may display status, generate local configuration candidates and ask for explicit human confirmation before changes.

It must keep generated configuration readable and reversible.

## Required status distinctions

Pantheon Control installation must never collapse these states:

```text
installed != connected != authorized != validated
```

A component may be installed but not connected.
A component may be connected but not authorized.
A component may be authorized for one scope but not another.
A component may be technically valid but not yet validated for professional use.

## Synology / NAS posture

Synology NAS installation must not hard-code a single volume such as `/volume1`, `/volume2` or `/volume3`.

The installer should detect candidate Docker roots such as:

```text
/volume*/docker
```

If several candidates exist, the human chooses.

For the current local setup, the known Pantheon Next repository path is:

```text
/volume3/docker/Pantheon-Next
```

This path is an example from the current deployment, not a universal default.

## MCP installation boundary

A future install profile may mount the Pantheon Next repository into the MCP Policy Server container as read-only:

```text
/volumeX/docker/Pantheon-Next:/repo:ro
```

The MCP Policy Server must not receive:

```text
Docker socket access
write access to the repository
write access to professional dossiers
external-action credentials
approval authority
memory promotion authority
scheduler or queue authority
```

Allowed environment posture:

```text
PANTHEON_REPO_PATH=/repo
PANTHEON_MCP_MODE=policy_server
PANTHEON_ALLOW_WRITE=false
PANTHEON_ALLOW_EXTERNAL_ACTIONS=false
```

## Forbidden installer behavior

The installer must not:

```text
silently modify Docker socket access
silently expose services publicly
install or update skills globally without inventory and review
promote a capability from available to authorized
turn a preflight pass into professional validation
write canonical memory
approve an output
trigger external actions
merge code
schedule hidden jobs
```

## Relationship to operations and platform

This document does not authorize changes under:

```text
operations/
platform/
Docker files
.env files
schemas/
tests/
pyproject.toml
```

Any future move into those paths requires explicit review and approval.

## First viable installation slice

The first safe installation slice should be read-oriented and reversible:

```text
1. detect Docker and Docker Compose
2. detect candidate /volume*/docker roots
3. ask the human to choose the install root
4. detect or create local ai-net network only after confirmation
5. locate Pantheon-Next repository
6. generate a local .env candidate
7. generate docker-compose candidate from a template
8. show the planned changes
9. ask for confirmation
10. start only the selected services
11. report installed / connected / authorized / validated separately
```

## Relationship to the MCP Policy Server discussion

This installation boundary is documented so installer work can continue separately.

The current MCP work should focus only on:

```text
validation
scope classification
approval-level classification
Task Contract Candidate preparation
Evidence Pack Candidate skeleton preparation
Result Candidate format preparation
Memory Candidate review framing
```

It should not design the installer.

## Boundary phrase

```text
Pantheon Control may prepare the room.
Hermes performs the work.
The MCP policy server checks the frame.
Pantheon governs status.
The human decides.
```
