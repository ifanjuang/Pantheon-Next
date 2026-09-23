# Workspace Cockpit

This is the filesystem Workspace projection owned by Pantheon for local document browsing.

Architecture owner:
[`docs/architecture/WORKSPACE_MANIFEST_INSPECTOR_CANDIDATE.md`](../../docs/architecture/WORKSPACE_MANIFEST_INSPECTOR_CANDIDATE.md).

Tracking:
- #660 owns the AFFAIRES filesystem/cartouche index and single producer;
- #659 owns Hindsight runtime and retain/retrieval qualification.

## Selected target

The selected professional target is now:

```text
NAS / AFFAIRES
      │ mounted on Linux
      ▼
one Linux AFFAIRES indexer/sync daemon
      │
      ├────────► Workspace Cockpit
      └────────► Hindsight on Linux
```

Hindsight does not own a second filesystem watcher. The Workspace daemon watches/reconciles the mounted NAS path and is the only producer into Hindsight.

A normal document bundle is:

```text
source.ext
source.md
```

where the Markdown file is the document cartouche. Optional `_folder.md` files may add useful folder context.

The target does not require Obsidian, Self-hosted LiveSync, CouchDB, a LiveSync filesystem mirror, `hindsight-obsidian-sync`, or `document.yaml` as a business sidecar.

Historical qualifications of those components remain useful evidence and are not erased by this migration.

## Current implementation state

The executable code in this directory is being migrated in bounded slices.

Slice 1 (#1112) is merged and Slice 2 is implemented as candidate #1115.

The current implementation:

- remains read-only for professional source/cartouche material;
- recognizes `source.ext + .source.ext.md` bundles;
- reads optional `_folder.md` context and explicitly exposes whether each folder has one;
- recognizes document cartouches only through the hidden full-source naming rule `.SOURCE.ext.md`;
- treats an ordinary Markdown file such as `notes.md` as a possible source, with `.notes.md.md` as its cartouche;
- does not confuse a document cartouche with the folder cartouche;
- renders complete, cartouche-missing and source-missing states;
- reads only bounded Markdown plus filesystem metadata during reconciliation;
- keeps heavy source bytes unopened;
- exposes a disabled Generate cartouche affordance without introducing a write path;
- serves `/api/workspaces` from an in-memory indexed snapshot;
- persists only reconstructible technical state in SQLite outside watched roots;
- uses Linux inotify as an accelerator and a periodic full reconcile as the convergence guarantee;
- is still configured by the Ubuntu deployment against historical LiveSync filesystem mirrors.

The remaining migration owned by #660 is:

```text
Slice 1  source.ext + .source.ext.md projection and broken-pair states — merged #1112
Slice 2  reconstructible index + watcher + periodic reconcile — candidate #1115
Slice 3  same daemon emits bounded Hindsight producer operations
Slice 4  Ubuntu deployment converges from vault mirrors to reviewed AFFAIRES root
```

Do not create a second filesystem Cockpit or an independent Hindsight watcher to bypass this migration.

## Authority boundaries

```text
source bytes != cartouche interpretation
cartouche != Evidence
retrieved != truth
memory != Evidence
folder != governed identity
projection != persistence
sync success != authorization
```

The Workspace Cockpit is a projection. It does not become a document authority merely because it can render or edit a cartouche.

Postgres-backed governed Information and existing governed document/extraction owners remain authoritative where their contracts apply.

## Local HTTP surface

The current local HTTP process exposes:

- `/` for the Cockpit interface;
- `/api/workspaces` for the current filesystem projection;
- `/api/health` for service supervision;
- `/api/role-traces/*` as the existing compatibility route for the optional same-origin, read-only observable-stage sidecar.

The browser never receives the Hermes Runs key or internal sidecar keys. The sidecar is in-memory only and cannot create, approve, retry or stop a run.

## Current local execution

The historical fixture remains runnable while the migration is in progress:

```bash
python3 implementation/workspace_cockpit/server.py \
  --root FIXTURE="$PWD/docs/examples/workspace_manifest_inspector/workspace"
```

The existing container/native installers remain compatibility surfaces until Slice 4 replaces their active Workspace inputs. Do not interpret their LiveSync mounts as the selected architecture.

## Hindsight boundary

The Workspace Cockpit does not itself make retrieved material authoritative.

Candidate mapping owned by #659:

```text
doc_...:source  → source file via Hindsight files/retain
doc_...:card    → optional separately retrievable Markdown cartouche
```

#659 must compare source-only, bounded cartouche context, and separately retrievable cartouche before the richer mapping is selected.

No automatic OCR is part of the AFFAIRES baseline.


## Linux NAS mount qualification

From the Linux host that mounts AFFAIRES and runs the Workspace/Hindsight stack:

```bash
python3 deployment/ubuntu/qualify-affaires-linux-mount.py --root /path/to/mounted/AFFAIRES
```

The probe writes and removes one temporary pair, validates hidden cartouche persistence, exact pairing, rename identity and reconcile rebuild. It also reports whether inotify events propagate through the mount; periodic reconcile remains mandatory even when they do.
