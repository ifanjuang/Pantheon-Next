# Workspace / AFFAIRES cartouche inspector and sync target

Status: selected target architecture; implementation remains bounded by #660 and Hindsight qualification by #659.

Current decision baseline:

```text
Pantheon-Next/main = c5860fe8750ca6c81d9b8dfb4e21e1427ff6e865
```

This document remains the architecture owner for the Workspace Cockpit filesystem projection. It supersedes the earlier productive target based on Obsidian + Self-hosted LiveSync + CouchDB + Ubuntu-local vault mirrors.

Historical LiveSync/Obsidian qualification remains useful capability evidence, especially #703, #706 and #717. It no longer selects the productive AFFAIRES topology.

## 1. Goal

Project the existing professional filesystem into the Cockpit and Hindsight without creating a second document authority.

Selected target:

```text
NAS / AFFAIRES
        │
        ▼
one AFFAIRES indexer/sync daemon
        │
        ├─ initial scan
        ├─ filesystem watcher
        ├─ periodic reconcile
        ├─ source/cartouche pairing
        ├─ reconstructible technical index
        │
        ├────────────► Cockpit
        │
        └────────────► Hindsight
```

The daemon is a technical synchronization/indexing component. It is not a business database, professional truth owner, Project identity owner, Evidence owner or approval engine.

## 2. Authority boundaries

Preserve:

```text
source bytes != cartouche interpretation
cartouche != Evidence
retrieved != truth
memory != Evidence
folder != governed identity
sync success != authorization
projection != persistence
```

The source file remains the source for its content.

The Markdown cartouche is an intentional human/derived description of that source. It may improve retrieval and Cockpit presentation but does not rewrite what the source proves.

Pantheon remains responsible for governed identities, decisions and professional authority where applicable.

Hindsight remains derived retrieval/memory.

Cockpit remains projection and interaction.

## 3. User-facing document convention

A normal documented source is represented by a pair in which the cartouche is dot-prefixed and preserves the complete source filename, including its extension:

```text
CCTP_IND_C.pdf
.CCTP_IND_C.pdf.md
```

or:

```text
DPGF.xlsx
.DPGF.xlsx.md
```

A Markdown source is unambiguous as well:

```text
notes.md
.notes.md.md
```

The source may be PDF, DOCX, XLSX, PPTX, Markdown or another admitted professional file type.

The leading dot distinguishes a document cartouche from an ordinary Markdown source. Preserving the complete source filename prevents collisions when several source formats share the same stem, for example `CCTP.pdf` and `CCTP.docx`.

The sidecar is Markdown, not a parallel JSON/YAML business sidecar.

```text
source.ext = source
.source.ext.md = cartouche
```

The cartouche may contain YAML frontmatter because Markdown frontmatter is a convenient carrier, but the user-facing artifact remains one `.md` file.

## 4. Cartouche contract

Candidate minimal frontmatter:

```yaml
---
document_id: doc_...
source: CCTP_IND_C.pdf
project: LIEUREY
phase: DCE
type: CCTP
index: C
document_date: 2026-09-12
issuer: FRONTSign
tags:
  - structure
  - ossature-bois
---
```

Candidate body:

```markdown
# CCTP — Lot 03 Ossature bois

## Résumé
...

## Points importants
...

## Limites / incertitudes
...

## Relations
...
```

Fields are not automatically governed merely because they appear in frontmatter.

In particular:

```text
project hint != governed project_id
folder name != governed project_id
index label != professional currentness
summary != source claim
relation note != governed relation
```

## 5. Identity

The cartouche may carry a stable `document_id` for the filesystem bundle.

This identity exists to keep the source/cartouche pair stable across ordinary filesystem moves. It must not silently replace an already governed Professional Document identity where one exists.

When a bundle later maps to a governed Document owner, reuse/resolve that owner rather than create a competing identity system.

### Move

The operator moves both files together:

```text
/DCE/CCTP_IND_C.pdf
/DCE/.CCTP_IND_C.pdf.md

→

/MARCHE/CCTP_IND_C.pdf
/MARCHE/.CCTP_IND_C.pdf.md
```

The stable cartouche identity remains the same.

The path changes.

```text
path != identity
```

### New index / new physical document

If the user intentionally keeps the old file and creates a new indexed file:

```text
CCTP_IND_B.pdf + .CCTP_IND_B.pdf.md
CCTP_IND_C.pdf + .CCTP_IND_C.pdf.md
```

they are separate bundles with separate cartouche identities unless an explicit governed relation later links them.

Do not infer a hidden version chain merely from similar names or contents.

## 6. Pairing

Primary pairing rule:

```text
source filename = SOURCE.ext
cartouche name  = .SOURCE.ext.md
+ cartouche declares source: SOURCE.ext
→ paired bundle
```

The filename relation is exact and one-to-one. The explicit `source` reference remains a consistency check, not a second identity owner.

Do not infer pairing from a shared stem alone.

If filesystem events arrive separately during a move/save, use a bounded grace/stability window before declaring a source or cartouche deleted.

## 7. Broken-pair states

### Source + cartouche

Cockpit renders the rich document card from the cartouche and verifies the declared source exists.

### Source without cartouche

The source remains visible.

Render a deliberately different minimal card:

```text
CCTP_IND_C.pdf
PDF

Cartouche manquant

[ Générer le cartouche ]
```

Do not silently invent business metadata from the filename.

The first productive posture is that an uncartouched file is visible but not automatically promoted to the normal Hindsight document route.

### Cartouche without source

Render an explicit source-missing state.

```text
cartouche present != source present
```

Never treat a retained summary as proof that the source still exists.

## 8. Folder context

Optional `_folder.md` may describe a folder when that context has actual value. The projection must explicitly distinguish `folder_context_present=true` from `false`; document cartouches such as `CCTP.md` do not satisfy the folder-context check:

```text
LIEUREY/
└─ DCE/
   ├─ _folder.md
   ├─ CCTP_IND_C.pdf
   ├─ .CCTP_IND_C.pdf.md
   ├─ DPGF.xlsx
   └─ .DPGF.xlsx.md
```

It can provide display/context fields and retrieval hints.

Architecture-agency folder conventions and their optional posture remain owned by `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`. The inspector must accept another existing organization as usable; it may observe or propose a mapping, but it must not silently reorganize AFFAIRES.

Do not require it for every directory.

```text
_folder.md != Project identity
folder context != professional approval
```

## 9. Cockpit navigation

The existing `implementation/workspace_cockpit` is the component to evolve. Do not add a parallel filesystem Cockpit.

The current implementation recursively scans LiveSync filesystem mirrors on each `/api/workspaces` request. That is acceptable as historical implementation evidence, but it is not the selected performance model for large AFFAIRES trees.

Target behavior:

```text
filesystem changes
→ daemon updates reconstructible index

Cockpit navigation
→ reads index
→ does not recursively rescan AFFAIRES on every click
```

The index may keep:

```text
path
parent path
basename
kind
document_id
source_present
card_present
source mtime / size / digest state
card mtime / digest
frontmatter projection
summary excerpt
sync state / last error
```

The index is technical cache/state only.

Deleting it must cause a rebuild, not loss of professional knowledge.

### Workspace-health projection

The Cockpit should preserve a report-oriented health view without turning presentation labels into professional status.

Candidate states include:

```text
COMPLETE
source + cartouche are present and structurally coherent

CARTOUCHE_MISSING
source exists but no cartouche is paired

SOURCE_MISSING
cartouche exists but its declared source is absent

CHECK
pair exists but local deterministic checks need attention

SYNC_ERROR
the technical producer has not converged with its target
```

These states support counts, filters and anomaly review. They are local projection vocabulary only:

```text
workspace health != professional currentness
health finding != defect confirmed
SYNC_ERROR != source invalid
COMPLETE != Evidence
```

The view may suggest a correction or explicit Generate action, but it must not auto-fix, rename, merge, archive, relink or rewrite professional material merely because a health check fires.

## 10. One producer

Do not introduce:

```text
Cockpit watcher
+
Hindsight watcher
```

Use one daemon:

```text
AFFAIRES daemon
├─ maintains Cockpit index
└─ emits Hindsight synchronization operations
```

This removes duplicated scans, duplicated event handling and competing delete/rename semantics.

## 11. Watcher + reconcile

Use both mechanisms:

```text
watcher   = responsiveness
reconcile = convergence guarantee
```

Startup performs a full reconcile.

A periodic reconcile catches:

- NAS/SMB events missed during outages;
- daemon downtime;
- event coalescing;
- transient move/save sequences;
- state-cache loss/rebuild.

The watcher must not be considered the source of truth.

## 12. Technical persistence

A small SQLite database or equivalent is acceptable for the daemon.

It may hold technical state such as:

```text
document_id
current path
source/card digests
size / mtime
last_seen
Hindsight source/card ids
last sync state
last error
```

It must not become the only owner of:

- title;
- summary;
- tags;
- limits;
- project meaning;
- document type;
- professional status.

Those human-readable descriptive fields belong in the cartouche when this file-native representation owns them.

## 13. Hindsight boundary

#659 owns Hindsight runtime and retain/retrieval qualification.

Candidate Hindsight mapping:

```text
bundle id = doc_...

doc_...:source
→ eligible source file
→ Hindsight files/retain
→ parsed source content

doc_...:card
→ cartouche Markdown
→ optional lightweight retain/chunks/verbatim
→ directly retrievable description
```

Do not assume the second document is valuable until measured.

Qualification must compare:

```text
A = source only
B = source + bounded cartouche metadata/context
C = source + separately retrievable cartouche
```

Select the smallest mapping that materially improves retrieval without confusing provenance or duplicating answers.

## 14. Context passed to source extraction

The cartouche may supply bounded identification context such as:

```text
document type
project/affaire hint
phase
index
issuer
document date
stable tags
```

Do not silently feed a speculative/derived summary into source extraction as though it were source fact.

```text
context for orientation != source evidence
```

## 15. Emails and illustrative attachments

A logical source does not always equal one physical attachment.

For an email:

```text
email body
+ inline images
+ ordinary illustrative photos
→ one logical multimodal Hindsight document where appropriate
```

A genuinely autonomous attached document may become its own source/cartouche bundle after classification.

Do not create a standalone Hindsight document for every decorative/illustrative photo by default.

## 16. File eligibility

Initial automatic Hindsight eligibility:

- PDF with native text;
- DOCX;
- XLSX;
- PPTX;
- TXT/MD/HTML where useful.

No automatic OCR.

For a scanned PDF/image requiring OCR:

```text
visible in Cockpit
→ OCR needed / unavailable state
→ explicit user/Pantheon action
→ derived OCR result
```

Do not NAS-wide OCR automatically.

Initially exclude from automatic Hindsight retain:

- RVT/RFA/RTE;
- PSD/PSB;
- unsupported/heavy binaries;
- lock files;
- temporary files;
- backup/autosave/cache/log artifacts.

A specialized BIM extraction path may be added later only when demonstrated necessary.

## 17. Cockpit generation action

`Générer le cartouche` is an explicit user action.

Candidate sequence:

```text
observe exact source
→ create stable bundle/cartouche skeleton
→ exact technical metadata
→ optional Hermes semantic enrichment
→ render as draft cartouche
→ re-read/validate
```

Hermes may propose:

- full title;
- summary;
- tags;
- important points;
- limits;
- semantic relations.

Hermes must not invent:

- file digest;
- source existence;
- governed Project identity;
- Evidence;
- professional currentness;
- approval.

Generation success does not automatically make the cartouche professionally validated.

## 18. Current Pantheon data owners

The repository already has Postgres-backed governed Information and document/extraction structures.

This file-native cartouche must not silently duplicate those authorities.

Observed current distinctions remain:

```text
source_documents
= governed/ingested source representation in the MVP store

Information
= canonical Postgres-backed Information object

AFFAIRES cartouche
= filesystem-native descriptive representation
```

Where a cartouche is later promoted/mapped into a governed object, use an explicit mapping/admission path.

Do not make Cockpit rendering itself persistence.

## 19. Historical topology

The following are no longer required by the selected AFFAIRES target:

```text
Obsidian
Self-hosted LiveSync
CouchDB
headless LiveSync filesystem mirror
hindsight-obsidian-sync
document.yaml as the default business sidecar
```

They may remain in historical qualification records or optional unrelated workflows.

Do not interpret their historical qualification as a requirement to retain them.

## 20. Migration of the current Workspace Cockpit

Current implementation facts after the Slice 1 candidate (#1112):

- `implementation/workspace_cockpit/server.py` remains read-only;
- it projects `source.ext + .source.ext.md` bundles and optional `_folder.md` context;
- it exposes `COMPLETE`, `CHECK`, `CARTOUCHE_MISSING`, `SOURCE_MISSING` and `FOLDER`;
- bounded Markdown is read, while heavy source bytes are not opened for ordinary projection;
- temp/lock/Revit-backup files are filtered and heavy professional binaries remain visible;
- the Generate cartouche affordance is visible but has no write route in this slice;
- it still scans on request rather than through the selected reconstructible index;
- Ubuntu deployment still mounts historical LiveSync vault mirrors.

Migration sequence:

### Slice 1 — source/cartouche projection — implemented candidate #1112

- recognize source.ext + .source.ext.md pairs;
- parse bounded frontmatter/body;
- expose complete, missing-card and missing-source states;
- preserve safe same-directory source references;
- keep the UI read-only; a visible Generate affordance does not authorize a write.

### Slice 2 — index/reconcile — implementation candidate #1115

- build a reconstructible SQLite technical index outside watched roots;
- keep the current Cockpit snapshot in memory so `/api/workspaces` does not rescan AFFAIRES per request;
- perform a startup reconcile and periodic full reconcile;
- use Linux inotify only as a responsiveness accelerator;
- coalesce filesystem event bursts through a bounded debounce window before reconcile;
- preserve source/cartouche `document_id` when the operator moves both files together;
- expose `folder_context_present` so a folder explicitly reports whether `_folder.md` exists;
- do not treat a missing `_folder.md` as invalid because folder context remains optional;
- keep the state database reconstructible and non-authoritative.

### Slice 3 — Hindsight producer

- one producer from the same daemon;
- explicit eligible formats;
- source retain;
- optional cartouche retain based on #659 A/B/C result;
- delete/update reconciliation;
- no automatic OCR.

### Slice 4 — deployment convergence

- mount the actual reviewed AFFAIRES root read-only/read-write only as required by explicit cartouche-generation posture;
- retire CouchDB/LiveSync/vault-mirror requirements from the active Workspace Cockpit baseline;
- keep historical tooling only if another demonstrated workflow still uses it.

## 21. Performance acceptance

Ordinary folder navigation must not depend on hashing or parsing every source file in AFFAIRES.

Expected:

```text
open Cockpit folder
→ index lookup / bounded immediate children
→ render
```

Heavy hashing, parsing and Hindsight retain happen asynchronously in daemon reconciliation, not in the UI request path.

Qualification should measure at least:

- initial cold scan;
- warm folder navigation;
- 1 changed cartouche;
- 1 changed PDF;
- move of a source/cartouche pair;
- daemon restart;
- NAS unavailable then restored.

## 22. Security and safety

Reject:

- symlink escapes outside admitted roots;
- relative source refs escaping the bundle/root;
- arbitrary server path reads from browser input;
- public unauthenticated write actions;
- secret values in cartouches;
- automatic consequential writes based solely on a filesystem event.

The generated cartouche action requires an explicit user request and whatever existing admission/authorization path applies to the actual write surface.

## 23. Done criteria

The target is qualified when:

- one source + one Markdown cartouche is the normal user-facing document bundle;
- no separate JSON/YAML business sidecar is required;
- complete and broken pairs are represented explicitly;
- Cockpit shows folders/files without full-tree rescans on each navigation;
- the technical index is reconstructible;
- watcher + periodic reconcile converge after restart/outage;
- source + cartouche moves preserve stable bundle identity;
- one daemon owns both Cockpit indexing and Hindsight synchronization;
- unsupported/heavy/temp files do not enter Hindsight automatically;
- OCR is explicit only;
- Hindsight source/card provenance remains distinguishable;
- no folder/path is silently promoted into governed Project identity;
- no cartouche/retrieval result is promoted into Evidence automatically;
- current Postgres/governed owners remain authoritative where applicable.

Tracking: #660 for filesystem/Cockpit producer, #659 for Hindsight runtime and retain/retrieval qualification.
