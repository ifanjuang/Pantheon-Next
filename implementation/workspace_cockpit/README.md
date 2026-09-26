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
.source.ext.md
```

where the hidden Markdown file is the document cartouche and preserves the complete source filename. Optional `_folder.md` files may add useful folder context.

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
- is configured by the Ubuntu deployment against the reviewed AFFAIRES path mounted directly by Linux; no source-tree mirror is required.

The remaining migration owned by #660 is:

```text
Slice 1  source.ext + .source.ext.md projection and broken-pair states — merged #1112
Slice 2  reconstructible index + watcher + periodic reconcile — candidate #1115
Slice 3  same daemon emits bounded Hindsight producer operations
Slice 4  Ubuntu deployment converges from vault mirrors to the reviewed Linux-mounted AFFAIRES root — implemented candidate
```

Do not create a second filesystem Cockpit or an independent Hindsight watcher to bypass this migration.

## Source integrity

A cartouche may optionally bind itself to exact source bytes:

```yaml
source_sha256: <64 hexadecimal characters>
source_size_bytes: <exact source byte length>
```

The checksum is verified only when it is declared. Ordinary AFFAIRES navigation therefore does not hash every large source.

```text
document_id = identity of this filesystem document occurrence
path        = current location
source_sha256 = observed byte identity

index/date/name != revision order
filename pairing != byte identity
declared checksum != verified checksum
verified source bytes != professional truth
```

For `.eml` bundles, `source_sha256` and `source_size_bytes` are required because the RAW message and its Markdown derivative must remain explicitly bound. A missing, invalid or mismatched integrity declaration makes the bundle `CHECK`.

Producer eligibility is separate from parser-format support:

```text
format supported + CARTOUCHE_MISSING/CHECK
→ visible in Cockpit
→ hindsight_format_supported = true
→ hindsight_eligible = false

COMPLETE source format supported
→ hindsight_representation_candidate = source

verified COMPLETE .eml
→ hindsight_representation_candidate = cartouche
```

These fields are only structural candidates for the producer owned by #659. They do not select Hindsight's durable A/B/C mapping and do not authorize a retain/write.

## Revision semantics

Indices, dates and filenames are descriptive only. They may contain human errors and must never create a hidden version chain.

Optional explicit relation:

```yaml
revision_mode: supersedes
revision_of: doc_previous
```

or:

```yaml
revision_mode: supplements
revision_of: doc_base
```

Rules:

```text
same index != same occurrence
higher index != newer
later date != replacement
earlier date + higher index != error inferred by Pantheon
similar filename != same document

supersedes
= explicit declaration that this occurrence replaces another

supplements
= explicit declaration that this occurrence adds to another;
  both remain independently relevant
```

No relation fields means no known relation. A missing referenced historical document is exposed as an unresolved/missing relation but does not invalidate an otherwise valid source. Self-reference or malformed relation fields produce `CHECK`.

If a source is corrected in place and remains the same intended filesystem occurrence, it may keep the same `document_id`; changed bytes then replace the same Hindsight `doc_...:source`. If the old file is retained and a second physical document is created—even with the same index—the new bundle gets a new `document_id` and any relationship must be declared explicitly.

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

The container/native installers now require the Linux-visible AFFAIRES mount directly. They do not create, synchronize or maintain a local source-tree copy.

## Hindsight boundary

The Workspace Cockpit does not itself make retrieved material authoritative.

The first producer qualification implements only the smallest A mapping:

```text
COMPLETE
+ unique document_id
+ Hindsight-supported source format
+ source representation candidate
        │
        ▼
same Workspace reconcile owner
        │
        ▼
Hindsight files/retain
document_id = doc_...:source
```

The source file is opened directly from the admitted Linux-visible AFFAIRES root. Pantheon creates no local staging file. The HTTP adapter uses a bounded transient in-memory multipart buffer; the default source bound is 100 MiB, matching Hindsight 0.10.1's default file-conversion batch-size limit.

Only bounded orientation fields are passed as context/metadata. The first slice deliberately excludes `index`, `document_date`, `revision_mode` and `revision_of` from Hindsight file-retain extraction context because these labels may be wrong or incomplete. The cartouche body and derived summary are not injected as source claims.

This slice does **not** close #659's A/B/C comparison:

```text
A = source only + bounded descriptive context   ← implemented qualification slice
B = richer bounded cartouche context            ← not selected
C = separately retrievable cartouche            ← not selected
```

Verified `.eml` bundles currently project a cartouche representation candidate and therefore remain outside this source-only producer slice.

The daemon records only reconstructible synchronization mechanics in the same SQLite state database:

```text
SUBMITTED / PENDING / PROCESSING
→ poll Hindsight operation
→ COMPLETED

same document_id + changed source fingerprint
→ wait for active operation to finish
→ retain again with the same doc_...:source id
→ Hindsight replaces the document

bundle still present but no longer eligible
→ BLOCKED

bundle absent
→ STALE
→ no automatic remote delete in this slice
```

The delete boundary is deliberate. Hindsight observations are derived state, and document deletion requires a separate lifecycle qualification before Pantheon may treat source disappearance as authorization to destroy Hindsight state.

No automatic OCR is part of the AFFAIRES baseline. The reviewed Hindsight deployment posture is:

```text
HINDSIGHT_API_RETAIN_MISSION=<professional-document chronology extraction mission>
HINDSIGHT_API_FILE_PARSER=markitdown
HINDSIGHT_API_FILE_DELETE_AFTER_RETAIN=true
HINDSIGHT_API_FILE_PARSER_MARKITDOWN_OCR_ENABLED=false
HINDSIGHT_API_STORE_DOCUMENT_TEXT=true
```

The retain mission asks Hindsight to preserve explicit chronology stated by the source itself: document date, revision/index/version token and explicit supersession relationships. It also tells Hindsight to preserve conflicting chronology statements rather than silently resolving them. The producer sends `timestamp: "unset"` for these reference documents so ingestion time is never presented to the extraction model as the document's event date.

Cartouche-declared `index` and `document_date` remain useful Workspace hints, but they are deliberately not sent to Hindsight as the source revision/date. The source content must establish those observations.

So uploaded source bytes are intended to be transient inside Hindsight after file conversion, while extracted document text/chunks and derived memories remain durable Hindsight state.

### Producer configuration

The producer is disabled unless both its URL and bank are configured.

For the native systemd deployment, create `/etc/pantheon-workspace-cockpit.env` with reviewed values such as:

```text
WORKSPACE_HINDSIGHT_URL=http://127.0.0.1:8888
WORKSPACE_HINDSIGHT_BANK_ID=<reviewed-bank-id>
WORKSPACE_HINDSIGHT_PARSER=markitdown
WORKSPACE_HINDSIGHT_MAX_SUBMITS_PER_RECONCILE=4
WORKSPACE_HINDSIGHT_MAX_FILE_MB=100
```

`WORKSPACE_HINDSIGHT_AUTHORIZATION` may be supplied there when the selected Hindsight exposure requires it. The environment file is optional; absence keeps the producer inactive.

```text
filesystem present != professionally validated
retain submitted != retain completed
retain completed != truth
memory != Evidence
technical synchronization != authorization
```

## On-demand Hindsight memory reconciliation

Cockpit may expose one explicit action for a `COMPLETE` source-backed document:

```text
[ Réconcilier avec Hermes ]
Focus optionnel: [...]
```

This first reconciliation slice is intentionally Hindsight-only:

```text
exact Workspace document_id
        │
        ├─ bounded cartouche projection
        └─ Hindsight <document_id>:source
              ├─ exact document identity/hash/count metadata
              ├─ exact document chunks
              └─ memory units filtered by exact document_id
                         │
                         ▼
              dedicated no-tool Hermes profile
                         │
                         ▼
              transient candidate-only result
```

It does **not** read the original NAS source, does not send the source path to Hermes,
does not send Hindsight `original_text` or arbitrary document/memory metadata, and
does not write to Hindsight, Workspace, NAS or a Pantheon governed owner.

The result categories are bounded to:

```text
missing
inconsistent
too_general
contradictory
organization
```

The optional focus is untrusted orientation text, limited to 2000 characters. The
whole serialized Hindsight/cartouche packet is bounded by
`WORKSPACE_RECONCILE_MAX_CONTEXT_CHARS` (48000 by default).

### Dedicated Hermes profile contract

Do not point this route at the normal Hermes profile. Hermes 0.21.3 does not treat an
OpenAI request `tools: []` as a per-request tool deny-list; the effective tools come
from the profile's `platform_toolsets.api_server`.

The reconciliation profile must be a blank/dedicated profile with no added hooks or
project workspace and this tool posture:

```yaml
platform_toolsets:
  api_server:
    - no_mcp
plugins:
  enabled: []
```

`no_mcp` is material. An explicit empty `api_server: []` list does not suppress
globally enabled MCP servers in Hermes 0.21.3.

Defense in depth:

```text
managed dedicated profile with api_server: [no_mcp]
        +
Cockpit GET /v1/toolsets before every analysis
        +
fail closed if any toolset reports enabled=true
        +
fail closed if Responses output contains a function_call
```

Cockpit calls the Hermes Responses API with `store:false`. Hermes still creates an
internal agent session for the turn, so Cockpit requires the returned
`X-Hermes-Session-Id` and deletes that session before returning a successful
candidate. If session cleanup cannot be proven, the candidate is withheld and the
request returns a residency failure.

Configuration is disabled by default:

```text
WORKSPACE_RECONCILE_HERMES_URL=http://127.0.0.1:8642/p/reconciliation
WORKSPACE_RECONCILE_HERMES_KEY=<profile-specific API_SERVER_KEY>
WORKSPACE_RECONCILE_HERMES_MODEL=
WORKSPACE_RECONCILE_HERMES_TIMEOUT_SECONDS=120
WORKSPACE_RECONCILE_MAX_CONTEXT_CHARS=48000
```

The URL may target a separately supervised profile or a multiplexed
`/p/<profile>` API surface, but it must resolve to the dedicated no-tool profile.
The API key is profile-specific.

The Ubuntu operator helper can create or verify that profile without activating a
gateway or changing profile routing:

```bash
export HERMES_RECONCILIATION_API_KEY="$(openssl rand -hex 32)"
sudo -E bash deployment/ubuntu/configure-hermes-reconciliation-profile --apply

# Once a dedicated route has been activated separately, qualify the live surface:
bash deployment/ubuntu/configure-hermes-reconciliation-profile --check \
  --runtime-url http://127.0.0.1:8642/p/reconciliation
```

The helper disables external memory, requires built-in profile memory files to
remain empty, keeps only Hermes' no-bundled-skills baseline, disables dynamic tool
search, empties MCP/plugin bindings, and refuses a reconciliation API key equal to
the default Hermes API key. With `--runtime-url` it also verifies the live
`/v1/toolsets` surface is empty and that the Responses API plus session deletion
endpoint are advertised. It deliberately does **not** start a profile gateway,
enable multiplexing, change routes, or write Cockpit configuration.

```text
configured profile != activated route
runtime route observed != task authorization
```

```text
reconciliation candidate != memory update
declared inconsistency != proven source defect
Hindsight chunk != original source
Hindsight memory != Evidence
Hermes analysis != authorization
candidate returned != candidate persisted
```

Exact NAS-source verification remains a later, separate path through a bounded admitted
source reference. It is deliberately not hidden inside this button.

## Linux NAS mount qualification

From the Linux host that mounts AFFAIRES and runs the Workspace/Hindsight stack:

```bash
python3 deployment/ubuntu/qualify-affaires-linux-mount.py --root /path/to/mounted/AFFAIRES
```

The probe writes and removes one temporary pair, validates hidden cartouche persistence, exact pairing, rename identity and reconcile rebuild. It also reports whether inotify events propagate through the mount; periodic reconcile remains mandatory even when they do.

## No local source mirror

The professional source tree remains on the NAS.

```text
NAS / AFFAIRES
      │
      │ mounted by Linux
      ▼
/path/to/mounted/AFFAIRES
      │
      ├─ Workspace daemon reads in place
      └─ Hindsight producer reads in place
```

Pantheon does not maintain a second durable copy of `AFFAIRES` on the Linux disk.

Allowed local state is reconstructible or derived:

```text
/var/lib/pantheon-workspace-cockpit/index.sqlite3
Hindsight durable derived-memory volumes
temporary process buffers / bounded transient extraction
```

These are not professional source copies.

For the container deployment set `AFFAIRES_ROOT` to the Linux-mounted NAS path. For native systemd installation use `--affaires-root /path/to/mounted/AFFAIRES`.

The installer verifies read/traverse access but never rewrites NAS ACLs recursively.
