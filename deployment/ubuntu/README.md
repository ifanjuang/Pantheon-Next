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
├── read-only Workspace Cockpit over the local vault mirrors
├── optional Marker 2 local API + OCR-AI Obsidian plugin
├── optional local Docling MCP for Hermes
├── Ollama
├── ComfyUI
└── pinned Pantheon checkout + bounded policy/MCP package
```

Hindsight is an optional prepared profile and is not started by default. Comfy MCP, Syncthing replication, Tailscale and any public/external access remain separate optional qualification/configuration steps in this first slice.

On Linux, the Ubuntu candidate applies `compose.hermes-local.yaml`: Hermes uses
host networking to reach the host Ollama API, while its API and dashboard bind
only to the selected `NODE_BIND_ADDRESS` (`127.0.0.1` by default). The Ollama
model remains an explicit operator choice; the deployment lock does not make a
model a Pantheon architectural dependency.

The local Ollama service uses a 65,536-token effective context window. Hermes
0.21 requires at least 64K; the model's larger advertised native window is not
the effective runtime window unless Ollama is configured accordingly.

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

The optional Hindsight container alone is not the qualified workspace-ingestion
topology. That topology also requires a separately installed and activated
`hindsight-obsidian-sync` producer. This first installer does not install or
activate that producer.

## Governed visible Role milestones

After the `pantheon-governed` Hermes profile exists, install the versioned
activity-projection skill and its managed profile supplement with:

```bash
deployment/ubuntu/configure-hermes-activity-projection --check
sudo deployment/ubuntu/configure-hermes-activity-projection --apply --restart
```

The command keeps a timestamped backup under `/srv/pantheon/backups`. It affects
presentation for new governed sessions only. It does not expose hidden
chain-of-thought, create agents, persist Role Signals or implement the Cockpit
dialogue view.

To route one WhatsApp conversation to the governed profile and enable safe
progressive Role milestones, use its observed Hermes `chat_id`:

```bash
deployment/ubuntu/configure-hermes-activity-projection --check \
  --route-whatsapp --whatsapp-chat-id '<chat-id>'
sudo deployment/ubuntu/configure-hermes-activity-projection --apply --restart \
  --route-whatsapp --whatsapp-chat-id '<chat-id>'
```

Use `--all-authorized-whatsapp` instead of `--whatsapp-chat-id` only when every
conversation already admitted by the WhatsApp adapter should use
`pantheon-governed`. The configurator does not widen that adapter allowlist. It
merges existing profile routes and profile allowlist entries, disables raw
reasoning display on WhatsApp, enables safe interim assistant messages, and
keeps a backup of the Hermes configuration. These are supported Hermes settings;
the provider source and image are not patched.

Hermes routing is based on trusted platform/chat/thread metadata, not on a
semantic guess about each question. Once a chat reaches `pantheon-governed`, the
activity-projection skill applies the content-sensitive part: simple requests
remain quiet, while non-trivial governed work gets compact Role milestones. A
Hindsight retrieval is observable tool use; it does not by itself activate the
Mnemosyne responsibility.

Pantheon's live-acceptance collector also contains a transient, read-only
`role.stage` projector for public Hermes Runs events. It can show canonical Role
headers as they arrive and real Hermes tool lifecycle stages. It deliberately
ignores `reasoning.available`; it is not installed as a service and does not
persist or authorize anything.

The candidate composed Cockpit also has a bounded authenticated SSE relay for
already-admitted runs. It can attach automatically after governed runtime-start
recording and render a compact browser dialogue when its dedicated Hermes trace
URL and key are configured. The Workspace Cockpit on port 8189 can expose the
same projection through an optional transient sidecar. The browser receives no
Hermes credential, and neither component gains run-control or approval methods.

For a new localhost-only Self-hosted LiveSync deployment, provision the
authenticated CouchDB posture, the `pantheon-obsidian` database, and a retained
encryption secret with:

```bash
sudo ./configure-livesync-local
```

The command never prints the CouchDB password or LiveSync passphrase. Obsidian
must initialize the new remote before the headless mirror service is enabled.

## Local OCR for Obsidian

Once LiveSync is active, install Marker 2.0.0, its local upload API, and the
`L3-N0X/obsidian-marker` 1.5.0 plugin without giving either component CouchDB
credentials:

```bash
sudo ./configure-marker-local --enable
```

The installer selects the plugin's `Python Cloud API` mode. The PDF is uploaded
to Marker at `http://127.0.0.1:8001/marker/upload`; Markdown and extracted
images are written by the Obsidian plugin into the client vault and propagated
normally by LiveSync. For an Obsidian client on another trusted machine, pass a
specific private address with `--bind <private-address>` and use that same
address in the plugin. Do not expose this unauthenticated API publicly.

Marker 2 uses the Surya 2 VLM through a GPU vLLM container. The installer pins
NVIDIA Container Toolkit 1.19.1 and vLLM 0.20.1. It also applies a bounded local
patch to Surya 0.22.1 so the auto-spawned inference port binds to `127.0.0.1`
instead of all host interfaces. If the toolkit was absent, Docker is restarted
once during installation; the node's restart policies restore its containers.

The API wrapper releases any models currently loaded by local Ollama before an
OCR request. Ten minutes after the last Marker conversion finishes, it stops
only the auto-spawned `surya-vllm-*` container recorded by Marker and clears the
local inference handle. The next Obsidian conversion starts it again
automatically. Every new conversion cancels and resets that idle delay, so a
batch keeps one warm vLLM process for the whole run. This gives Hermes/Ollama
the GPU while OCR is idle, at the cost of a cold-start delay on the next OCR.
Set `MARKER_GPU_IDLE_SECONDS=0` in
`/etc/pantheon-node/marker.env` to disable idle release.

```text
OCR-AI 1.5.0        -> POST PDF to Marker /marker/upload
Marker 2.0.0        -> Markdown + base64 images
OCR-AI              -> writes note and assets into the Obsidian vault
LiveSync            -> CouchDB and the other Obsidian clients
Hermes              -> reads the resulting Markdown through existing vault access
```

The plugin files are installed under `.obsidian/plugins/marker-api`, added to
`community-plugins.json`, and preconfigured for French and English. In Obsidian,
reload the application after LiveSync has received the files, then use
right-click → **Convert to MD** on a PDF. Review Marker's model-weight licence
before commercial use.

## Docling for Hermes

Install the pinned Docling SDK and Docling MCP server separately from Marker:

```bash
sudo ./configure-docling-local --enable
```

Docling `2.126.0` and Docling MCP `3.2.0` run as the restricted
`pantheon-docling` user. The MCP endpoint is loopback-only at
`http://127.0.0.1:8020/mcp`; no CouchDB credentials are involved. The installer
writes a reviewable Hermes fragment to `/srv/pantheon/hermes/docling-mcp.yaml`;
it does not silently modify Hermes' active configuration or authorize a new
tool. Merge that fragment into Hermes after reviewing the active MCP policy.
The Hermes container mounts `/srv/pantheon/obsidian`,
`/srv/pantheon/obsidian-affaires` and `/srv/pantheon/obsidian-documentaires` at
the same paths so Docling can process PDF paths passed by Hermes without
translation. LiveSync state and Hindsight indexes remain outside Hermes' file
surface.

The qualified LiveSync CLI source is built with a pinned npm 11 build tool.
This avoids the npm 10.9.8 Arborist `edgesOut` crash in `node:22-slim` while
leaving the reviewed LiveSync source commit unchanged.

## Read-only Workspace Cockpit

The first local Cockpit slice does not require PostgreSQL or pgvector. It reads
the filesystem mirrors produced by LiveSync and projects folders as Pantheon
Cards without reading CouchDB directly, duplicating document content, or
writing to the vaults.

The recommended deployment reuses the locally cached, release-pinned Hermes
Python image without sharing Hermes state or credentials:

```bash
docker compose --env-file release.env \
  -f compose.workspace-cockpit-local.yaml up -d --build
```

To bind to one reviewed LAN/private address, keep host-specific values and
secrets in an ignored local env file and load it after the release lock:

```bash
umask 077
cat > .env.workspace-cockpit <<'EOF'
WORKSPACE_COCKPIT_BIND=192.0.2.10
WORKSPACE_COCKPIT_PORT=8189
HERMES_ROLE_TRACE_BASE_URL=http://192.0.2.10:8642/p/pantheon-governed
HERMES_ROLE_TRACE_API_KEY=replace-with-governed-runs-key
ROLE_TRACE_ATTACH_KEY=replace-with-random-attach-key
ROLE_TRACE_READ_KEY=replace-with-random-read-key
EOF
docker compose --env-file release.env --env-file .env.workspace-cockpit \
  -f compose.workspace-cockpit-local.yaml up -d --build
```

This is private/LAN publication, not authenticated Internet publication.

For authenticated access outside the LAN, prepare the pinned Tailscale
userspace container without granting `/dev/net/tun` or host network access:

```bash
docker compose --env-file release.env \
  -f compose.workspace-cockpit-tailscale.yaml up -d
docker logs pantheon-cockpit-tailscale
```

Visit the one-time login URL from the logs. Once the node is authorized, proxy
the private Cockpit endpoint within the tailnet:

```bash
docker exec pantheon-cockpit-tailscale \
  tailscale serve --bg http://192.168.50.135:8189
```

The named volume preserves the Tailscale node identity. No auth key belongs in
Compose, Git or shell history.

Both containers have read-only root filesystems and drop every Linux
capability. The Cockpit publishes only on its configured host address
(loopback by default) and mounts the three vaults read-only. The Role sidecar's
attach route is published on host loopback only; it is the sole component that
reads the configured public Hermes Runs stream. The native systemd
alternative is available when container deployment is unwanted:

```bash
sudo ./configure-workspace-cockpit-local --user <linux-user> --enable
```

The service binds to `127.0.0.1:8189` by default and reads these mirrors:

```text
/srv/pantheon/obsidian
/srv/pantheon/obsidian-affaires
/srv/pantheon/obsidian-documentaires
```

It recognizes `document.yaml`, checks for a Markdown representation bearing
the same name as its folder, counts PDF/image/table resources, and exposes the
local presentation states `FREE`, `QUALIFIABLE`, `COHERENT`, `CHECK`, and
`INVALID`. These are workspace-health labels, not governed Document status.

The native installer grants the selected unprivileged service user read-only ACLs on
the mirrors, installs a hardened systemd unit, and never receives CouchDB
credentials. Bind to a private address only after a separate access review.

The LiveSync composition preserves the executable qualification already carried by the repository:

```text
CouchDB
-> one long-running LiveSync CLI daemon
-> dedicated local DB
-> dedicated filesystem vault mirror
```

Repeated one-shot `sync` + `mirror` is not used.

The Docker image entrypoint supplies its database-path argument. The node wrapper
selects the dedicated database mount with `LIVESYNC_DB_PATH=/data/db` instead of
passing a second positional database path.

## Governed Hermes skills

`release.env` carries a small reviewed list of Pantheon-authored Hermes skills.
The install/update path copies only those named packages from the exact target
Pantheon checkout into `/srv/pantheon/hermes-governed-skills`, mounts that
directory read-only, and adds it to the existing `pantheon-governed` profile
when that profile is already present.

The deployment does not expose the whole template tree, create the governed
profile or replace pre-existing external skill directories. Availability of a
skill remains distinct from use, authorization, persistence and approval.

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

Hindsight's rootless embedded database uses the Docker named volume
`pantheon-hindsight-data`; this avoids host/user-namespace UID mismatches that
make a bind-mounted `.pg0` directory unwritable. Include that named volume in
stateful backup and restore procedures.

Generated secrets are root-only and must not be committed. The updater creates a configuration checkpoint before changes; it does not pretend that checkpoint is a complete stateful database backup.

## Not in the first executable slice

The following remain intentionally optional rather than becoming hidden baseline dependencies:

- Syncthing Ubuntu `send-only` -> NAS `receive-only` replication;
- Tailscale/private remote access;
- external authenticated web publication;
- Comfy MCP binding and Hermes tool allowlist;
- Hindsight durable ingestion/producer activation;
- authenticated Workspace Cockpit publication beyond a reviewed private bind;
- automatic custom-node or model marketplace management.

Those can be added only when their actual configuration and qualification needs are demonstrated.
