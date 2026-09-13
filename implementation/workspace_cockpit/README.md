# Workspace Cockpit

This is the first read-only Linux projection of the workspace manifest
inspector described in
[`docs/architecture/WORKSPACE_MANIFEST_INSPECTOR_CANDIDATE.md`](../../docs/architecture/WORKSPACE_MANIFEST_INSPECTOR_CANDIDATE.md).

It scans the filesystem mirrors produced by Self-hosted LiveSync and projects
document packages as cards. CouchDB remains a synchronization transport; the
Cockpit does not query it directly. It also has no PostgreSQL or pgvector
dependency. An optional transient sidecar can read the public event stream of
an already-admitted Hermes run and project its visible Role stages.

The local HTTP process exposes:

- `/` for the Cockpit interface;
- `/api/workspaces` for the current read-only projection;
- `/api/health` for service supervision;
- `/api/role-traces/*` as an optional same-origin, read-only proxy to the Role
  sidecar.

The browser never receives the Hermes Runs key or either internal sidecar key.
The sidecar is in-memory only and cannot create, approve, retry or stop a run.

Run against the repository fixture:

```bash
python3 implementation/workspace_cockpit/server.py \
  --root FIXTURE="$PWD/docs/examples/workspace_manifest_inspector/workspace"
```

The recommended Linux installation uses the already pinned local Hermes Python
runtime as a base image, but does not mount Hermes state or credentials:

```bash
docker compose --env-file deployment/ubuntu/release.env \
  -f deployment/ubuntu/compose.workspace-cockpit-local.yaml up -d --build
```

The two containers have read-only root filesystems, no Linux capabilities and
read-only vault mounts. The Role sidecar is the only component that reads the
configured public Hermes Runs stream; the Cockpit contacts only that sidecar.
A native systemd alternative is also available:

```bash
sudo deployment/ubuntu/configure-workspace-cockpit-local --user "$USER" --enable
```

The native installer grants the selected unprivileged service user read/traverse ACLs
on the configured mirrors. The application contains no mutation route and does
not serve document contents.
