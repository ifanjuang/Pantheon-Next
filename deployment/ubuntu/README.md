# Ubuntu node bootstrap candidate

Status: operator convenience artifact — candidate, non-authoritative.

This directory turns the existing manual installation runbook into a bounded convenience path for one Ubuntu compute node. It does not make Pantheon an installer, package manager, runtime owner, approval engine, or deployment authority.

The generic owners remain:

- `docs/governance/COMMON_INSTALLATION_BASELINE.md`;
- `docs/install/COMMON_BASELINE_RUNBOOK.md`;
- `docs/governance/BOOTSTRAP_INSTALLATION_LADDER.md`.

## Intended profile

The first profile deliberately consolidates the active compute/runtime path on one Ubuntu host:

```text
Ubuntu node
├── Docker / Compose
├── Hermes Agent + dashboard
├── CouchDB
├── Self-hosted LiveSync CLI daemon candidate
├── local filesystem vault mirror
├── Ollama
├── ComfyUI
└── pinned Pantheon checkout + bounded policy/MCP package
```

Hindsight is an optional prepared profile and is not started by default. Comfy MCP, Syncthing replication, Tailscale and any public/external access remain separate optional qualification/configuration steps in this first slice.

A NAS is not required in the active execution path. It may remain project storage and/or a backup/snapshot target. A later Syncthing profile may replicate the Ubuntu filesystem mirror to a NAS without making that replica a second LiveSync producer.

## Install

From an exact Pantheon checkout on Ubuntu Server 26.04:

```bash
sudo deployment/ubuntu/install-node
```

Read-only preflight:

```bash
deployment/ubuntu/install-node --doctor
```

The default service bind is `127.0.0.1`. Expose deliberately to a specific LAN or private-network address only when required:

```bash
sudo deployment/ubuntu/install-node --bind <private-address> --comfy-bind <private-address>
```

The installer is intentionally interactive unless `--yes` is supplied. If the Ubuntu-recommended NVIDIA driver must be installed, the script stops after driver installation and requires a reboot before it is rerun.

## What starts automatically

```text
CouchDB      yes, loopback/private bind selected by operator
Ollama       yes
ComfyUI      yes
Hermes       only after its first-time setup exists
LiveSync     no — installed as a daemon service but disabled until settings.json exists
Hindsight    no — optional profile only, even with --with-hindsight
Pantheon MCP installed/validated, but not exposed as an independently authorized service
```

The LiveSync composition preserves the executable qualification already carried by the repository:

```text
CouchDB
-> one long-running LiveSync CLI daemon
-> dedicated local DB
-> dedicated filesystem vault mirror
```

Repeated one-shot `sync` + `mirror` is not used.

## Update

Check only:

```bash
deployment/ubuntu/update-node --check
```

Apply the reviewed target set:

```bash
sudo deployment/ubuntu/update-node --apply
```

Or one component family:

```bash
sudo deployment/ubuntu/update-node --apply --component comfyui
```

Pantheon never follows `main` implicitly. A Pantheon change requires a reviewed full commit SHA:

```bash
sudo PANTHEON_COMMIT_OVERRIDE=<40-char-sha> deployment/ubuntu/update-node --apply --component pantheon
```

A stateful CouchDB/Hindsight version change is refused unless the operator first establishes a verified backup/rollback point and explicitly sets `STATEFUL_BACKUP_CONFIRMED=1`.

## Version posture

`release.env` is a deployment-candidate lock, not the external qualification registry. It may intentionally differ from `implementation/qualification/external-pins.json` where a newer upstream stable release has been reviewed for installation but has not been promoted as a qualified Pantheon binding.

In particular, the first profile keeps Self-hosted LiveSync on the repository's exact executable qualification ref rather than silently replacing that proof with a newer plugin release.

```text
upstream release available != deployment target selected
selected deployment target != qualified provider binding
installed != activated
activated != task-authorized
runtime success != Evidence
filesystem mirror != governed identity
```

## Persistence

Operational data stays outside Git checkouts:

```text
/opt/pantheon/          pinned code checkouts
/opt/pantheon-node/     installer-managed application material
/etc/pantheon-node/     root-owned configuration and generated secrets
/srv/pantheon/          runtime state and workspace mirror
/srv/ai/                models, caches and ComfyUI output
```

Generated secrets are root-only and must not be committed. The updater creates a configuration checkpoint before changes; it does not pretend that checkpoint is a complete stateful database backup.

## Not in the first executable slice

The following remain intentionally optional rather than becoming hidden baseline dependencies:

- Syncthing Ubuntu `send-only` -> NAS `receive-only` replication;
- Tailscale/private remote access;
- external authenticated web publication;
- Comfy MCP binding and Hermes tool allowlist;
- Hindsight durable ingestion/producer activation;
- automatic custom-node or model marketplace management.

Those can be added only when their actual configuration and qualification needs are demonstrated.
