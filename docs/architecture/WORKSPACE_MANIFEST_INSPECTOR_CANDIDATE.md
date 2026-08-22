# Workspace Manifest Inspector — candidate companion to file-native convergence

Status: candidate architecture note — documentation only.

Parent roadmap: `docs/roadmaps/FILE_NATIVE_CONTROL_CONVERGENCE.md` in PR #687.
Parent workspace exploration: Pantheon-Next #684.
Related qualification: #660 for LiveSync/CouchDB offline/reconnect/conflict behavior.

This note refines one bounded user-facing slice of the file-native convergence roadmap: how logical workspace objects may carry small sidecar manifests, how those manifests may be inspected locally in Obsidian, and how the existing Pantheon Card visual grammar may be reused without making Obsidian, Swiper, a plugin cache or Hermes into a new authority owner.

It does **not** adopt a production manifest schema, authorize file-native owner migration, choose a final vault topology, implement an Obsidian plugin, or change current Pantheon doctrine.

## 1. Goal

Make the health of a file-native workspace understandable at a glance while preserving ordinary filesystem/Obsidian workflows.

Candidate UX:

```text
workspace object selected
→ Pantheon inspector Card
→ manifest/source diagnostics
→ direct safe edits where permitted
→ optional Hermes-assisted enrichment
```

The plugin is primarily:

```text
local workspace inspector
+ manifest editor
+ deterministic consistency checker
+ Card/Swiper projection surface
```

It is not:

```text
business database
workflow engine
memory system
Hindsight replacement
sync engine
approval engine
new Card authority
```

## 2. Core authority model

Keep the durable convergence model unchanged:

```text
Files / Sources = professional and workspace content
Pantheon        = rules and governed boundaries
Hermes          = reasoning and action runtime
Hindsight       = derived retrieval and associations
Cockpit         = projection and interaction
```

For this slice:

```text
workspace manifest file
= source metadata for the logical object only where that responsibility
  is explicitly file-native

plugin local index/cache
= reconstructible projection state

plugin offline outbox
= device-local unsent user intent

Card
= composed projection

Pantheon
= validation / qualification / protected-transition rules

Hermes
= semantic enrichment and proposed work
```

Additional non-equivalences:

```text
manifest present != governed identity admitted
manifest valid != professional state approved
folder contains files != logical Document
plugin warning != professional currentness verdict
local outbox item != WorkIssue
Hermes proposal != manifest truth
Swiper position != authority
```

## 3. Manifest belongs to a logical object, not every filesystem entry

Do **not** require one manifest per folder or file.

Candidate document package:

```text
CCTP/
├── document.yaml
├── CCTP.md
├── CCTP - Ind C.pdf
├── assets/
└── Archives/
    └── CCTP - Ind B.pdf
```

This may represent one logical professional Document family even though it contains several filesystem entries.

Examples that may legitimately remain without a manifest:

```text
Notes/
Photos/
assets/
one ordinary working note
one temporary image
```

The plugin must therefore distinguish:

```text
FREE
no manifest expected

QUALIFIABLE
logical object may benefit from a manifest, but none exists yet

MANAGED
manifest exists and passes applicable structural/consistency checks

CHECK
manifest exists but a non-fatal divergence requires attention

INVALID
manifest exists but cannot satisfy the applicable contract
```

Names/icons/colors are UX vocabulary candidates only. They must not create a parallel professional lifecycle.

## 4. Candidate package sidecar

For a document package, `document.yaml` is the preferred candidate user-facing sidecar name because it is readable, editable and schema-validatable.

Do not maintain both YAML and JSON representations of the same manifest by default.

Illustrative candidate only:

```yaml
schema: pantheon.document-package/v1

document_id: document:cctp-lieurey
title: CCTP
display_name: Cahier des clauses techniques particulières — DCE
document_role: authored

tags:
  - type/cctp
  - phase/dce
  - sujet/lot/plomberie

representation:
  markdown: CCTP.md
  represented_revision: revision:cctp-C

source:
  file: CCTP - Ind C.pdf
  revision: revision:cctp-C
  index_label: C
  digest: sha256:...

summary:
  text: >
    CCTP de consultation...
  based_on_digest: sha256:...
  status: generated_unreviewed

changes:
  compared_to: revision:cctp-B
  target: revision:cctp-C
  based_on:
    before_digest: sha256:...
    after_digest: sha256:...
  items:
    - location: Lot 07 > Ventilation
      summary: Révision du principe d'extraction...
  status: generated_unreviewed
```

No exact schema or field vocabulary is adopted by this note.

## 5. What should and should not live in the sidecar

Candidate sidecar responsibilities:

```text
stable logical object/package identity
schema identity/version
title / human display name
object/document role
workspace classification tags
representation references
represented source revision/index label
source refs/digests where applicable
derived summary with source digest
source-to-source change summary with both digests
conversion/derivation provenance where useful
```

Do **not** turn ordinary editable sidecar fields into authority for:

```text
latest_received
current_working
current_contractual
current_for_execution
current_for_site
Evidence admission
Decision legitimacy
authorization
professional approval
```

Purpose-specific Document currentness remains a separate owner/projection concern.

Therefore:

```text
source.index_label = C
= fact about the represented source

current_for_execution = C
= governed/currentness conclusion for a purpose
```

These are not equivalent.

## 6. Authored versus derived document packages

The same package grammar should support both without confusing their editable authority.

### Authored

```yaml
document_role: authored
representation:
  markdown: CCTP.md
```

Candidate semantics:

```text
Markdown = editable working content
issued/export PDF = exact snapshot/source artifact when declared
```

Hermes may propose bounded edits to the Markdown only through the applicable write policy.

### Derived / received

```yaml
document_role: derived
source:
  file: Rapport BET - Ind C.pdf
representation:
  markdown: Rapport BET.md
```

Candidate semantics:

```text
PDF = exact source
Markdown = derived representation
```

Hermes may read/analyse the Markdown, but must not semantically edit it as though it were the received source.

If the derived Markdown diverges through human semantic edits, regeneration must not silently overwrite that divergence.

## 7. Card projection contract

The Card should be a **composition**, not a direct rendering of the YAML file.

Candidate composition:

```text
document.yaml
+ observed package state
+ Tag Registry projection
+ Pantheon currentness projection where available
+ related Work state where relevant
→ Card
```

The manifest therefore remains small even when the Card is rich.

### Title rule

For filesystem/workspace packages:

```text
Card title
= actual selected folder/file name

Card subtitle
= fuller human designation from the manifest or a reviewed/generated proposal
```

Example:

```text
CCTP
Cahier des clauses techniques particulières — DCE
```

The generated/semantic subtitle must not replace the real filesystem title in navigation.

### Manifest absent

Candidate Card:

```text
CCTP
Dossier non qualifié

Markdown détecté
PDF détecté

[ Générer la fiche ]
```

The UI may suggest qualification without claiming the folder already is a governed Document.

### Manifest present

Candidate Card:

```text
CCTP
Cahier des clauses techniques particulières — DCE

Retenu · Projet · DCE

✓ Manifest
✓ Source
⚠ MD représente C / dernier reçu D
✓ Tags
⚠ Résumé basé sur une ancienne source

[ Modifier ]
[ Modifier avec Hermes ]
```

The warning `dernier reçu D` must come from the currentness/document owner, not be guessed from filenames or copied into the manifest as editable truth.

## 8. Preserve Pantheon Card design; keep Swiper as UX implementation

The existing Card visual grammar is worth reusing.

Candidate Obsidian surface:

```text
Obsidian ItemView
→ Pantheon Card presentation
→ optional Swiper-based fluid navigation
```

Reuse visual concepts such as:

```text
front = understand
back = work around the object
details = provenance / diagnostics
```

Preserve mobile/touch-friendly Card navigation where it improves the experience.

However:

```text
Card projection contract != Swiper
```

Swiper is a replaceable presentation mechanism. It must not become a business, identity or navigation-authority contract.

For offline reliability, any Swiper dependency used by an Obsidian plugin should be bundled/pinned with the plugin rather than required from a runtime CDN.

## 9. Workspace-health view

The strongest plugin-specific value is not duplicating the Obsidian file explorer. It is exposing workspace health.

Candidate summary:

```text
PANTHEON — WORKSPACE

183 managed
 12 check
  3 invalid
 27 qualifiable
```

Candidate filters:

```text
All
Errors
Check
Without manifest
Stale derived metadata
```

Candidate issue browsing:

```text
CCTP ⚠
→ BET structure ⚠
→ Notice PC ✕
→ ...
```

A Card/Swiper sequence over anomalies is useful because it adds a quality-control workflow rather than reproducing ordinary folder navigation.

## 10. Deterministic validator before Hermes

Most workspace-health checks should not require an LLM.

Candidate deterministic checks:

```text
manifest absent where the object was explicitly declared/expected as managed
invalid YAML
unknown schema version
duplicate stable ID
missing referenced source
missing representation
path/reference mismatch
digest mismatch
unknown Tag Registry value
broken stable relation target
summary based_on_digest stale
change summary before/after digest stale
derived representation built from an older source
semantic divergence that would make regeneration destructive
```

A filesystem placement warning may be shown, for example when an observed newer revision sits under `Archives/`, but:

```text
workspace organization warning != professional currentness decision
```

## 11. Hermes-assisted enrichment

Use Hermes only where semantic interpretation adds value.

Candidate actions:

```text
Generate the sheet
Generate/update summary
Analyse principal changes
Propose tags
Explain an inconsistency
Propose a manifest correction
```

Separate deterministic and semantic responsibilities:

```text
DETERMINISTIC
observed files
paths
stable target resolution
digests
schema validation
known registry membership

HERMES
full display name
summary
semantic tags candidates
principal-change summary
ambiguity explanation
proposed correction
```

A button may say `Générer la fiche`, but the implementation must not ask Hermes to invent hashes, source identity or currentness conclusions.

Generated semantic fields should preserve derivation status/provenance and become stale when their source digest changes.

## 12. Direct editing and Hermes editing

The inspector may expose direct form controls only for fields whose write posture permits it.

Candidate categories:

```text
DIRECT / LOW-CONSEQUENCE
human display name
ordinary workspace tags
working summary text
other low-consequence metadata after schema validation

MANAGED
stable ID
schema version
source refs/digests
representation bindings
fields requiring deterministic validation

PROJECTED / GOVERNED ELSEWHERE
purpose-specific currentness
Evidence
Decision
authorization
professional approval
```

Exact field classification must come from Phase 2 doctrine/owner convergence rather than this note.

`Modifier avec Hermes` should produce a bounded proposal/diff against the current target digest. Consequential application remains subject to the existing Pantheon write/gate model.

## 13. Local-first index/cache

The plugin should not need a server round-trip to render basic manifest health.

Candidate model:

```text
local vault
→ initial bounded scan
→ local reconstructible manifest index
→ Cards / warnings / filters
```

Then react incrementally to workspace events:

```text
create
modify
rename
move/delete observation
→ revalidate affected object/package
```

A full manual rescan remains available as repair/rebuild behavior.

The local index may contain values such as:

```text
path → logical package candidate
manifest path/digest
schema status
source digest observation
warnings
last scan observation
```

But:

```text
plugin index/cache != authority
```

Deleting it must cause at most a rebuild, never professional-data loss.

Do not solve performance by making the cache authoritative.

## 14. Offline behavior

Basic workspace work should remain possible without Pantheon/Hermes/Hindsight connectivity where the local vault already contains the needed files.

Candidate offline-capable functions:

```text
browse Cards
read manifests
run deterministic local validation
edit locally permitted manifest fields
create a deterministic manifest skeleton
inspect local source/representation consistency
prepare a Hermes request for later submission
```

Remote-only functions must degrade explicitly rather than fail silently.

```text
Hermes unavailable
→ semantic generation unavailable
→ user may queue intent locally

Pantheon/currentness service unavailable
→ local manifest still readable
→ governed currentness shown unavailable/stale, not invented

Hindsight unavailable
→ semantic retrieval unavailable
→ local workspace inspection remains usable
```

## 15. Offline Hermes outbox

An unsent offline request is device-local user intent, not a WorkIssue and not a Hermes task yet.

Candidate minimal envelope:

```yaml
request_id: request:...
target_ref: document:cctp-lieurey
target_path_observed: Affaires/LIEUREY/Documents/CCTP
expected_digest: sha256:...
action: enrich_manifest
created_at: ...
idempotency_key: ...
```

Exact fields remain open.

Required behavior on reconnect:

```text
resolve current target
→ compare current digest/revision to expected basis
→ if unchanged, submit one idempotent request
→ if changed, mark local intent stale/conflicted
→ do not send blindly
```

The outbox should be device-local by default rather than synchronised as workspace content.

Reason:

```text
iPhone queues request R
+ PC receives synchronised outbox R
+ both reconnect
→ duplicate submission opportunity
```

Server-side idempotency remains required as defence in depth.

The existing `pantheon-mvp` mobile editor provides precedent for local offline Hermes edit-request queuing with idempotency; reuse the demonstrated invariant, not necessarily that exact UI/storage implementation.

## 16. WorkIssue begins only after server receipt/admission

Once an eligible user request reaches the governed server path, existing work/execution owners take over.

Candidate boundary:

```text
device-local outbox intent
→ server receipt / validation
→ bounded handoff / WorkIssue when durable treatment is needed
→ execution admission as applicable
→ Hermes
```

If Hermes needs clarification:

```text
WorkIssue
→ waiting / needs-human-attention projection
→ question/comment visible on the related Card
```

A human response may become issue discussion/context. It is not automatically a Decision, approval or Evidence.

Do not use PostgreSQL WorkIssue state, a Hermes Kanban or a vault exchange file as the storage owner for unsent device-local clicks.

## 17. Hermes runtime work queues remain separate

If Hermes uses a runtime-side Kanban/queue to organise admitted work, that remains an execution concern.

Candidate distinction:

```text
WorkIssue
= durable professional treatment identity/scope/review

Hermes runtime queue/Kanban
= how the external runtime schedules/organises admitted execution
```

The plugin should not make Hermes runtime queue state the professional work authority.

## 18. Sync model

Workspace files and manifests follow the selected vault synchronization path.

Candidate topology under #660 qualification:

```text
Obsidian PC / mobile
        │
        │ LiveSync
        ▼
     CouchDB NAS
        ▲
        │ LiveSync
        │
second Obsidian client
```

Preserve:

```text
CouchDB = synchronization
CouchDB != memory
CouchDB != Pantheon authority
sync success != Evidence
```

Manifest source files may synchronize.

The local plugin index/cache should not need to synchronize because it is reconstructible independently on each client.

The device-local Hermes outbox should not be treated as normal vault content by default.

Conflict behavior for managed/protected manifests must reuse the #660 qualification outcome and fail visibly rather than silently merge governed state.

## 19. NAS topology

Do not require an Obsidian plugin to run on the NAS.

Preferred candidate topology:

```text
PC / mobile
= Obsidian + Pantheon Inspector plugin

NAS
= Pantheon services
+ Hermes
+ Hindsight
+ CouchDB/LiveSync
+ other qualified adapters as needed
```

If #660 later qualifies an always-on Obsidian Web/NAS client and that client has a demonstrated use, the same plugin may be installed there.

That remains optional:

```text
Obsidian Web/NAS unavailable
!= inspector architecture unavailable
```

## 20. Shared validator, not duplicated rules

The manifest/plugin design should avoid separate validation semantics in browser/plugin and server.

Candidate responsibility:

```text
Pantheon manifest contracts / rules
         │
         ├── consumed by Obsidian inspector validator
         └── consumed/rechecked by Pantheon server write/admission path
```

This does not require one runtime package or language immediately. It requires one normative rule owner and conformance tests.

A future shared implementation core may be useful only if it reduces real duplication.

Do not create a new rules compiler/service merely for this feature.

## 21. Hindsight boundary

Do not index raw manifest YAML as an independent semantic note by default.

Preferred direction:

```text
document.yaml
→ metadata / classification

Document.md
→ semantic content
→ Hindsight
```

Selected manifest metadata may enrich the Hindsight ingestion context:

```text
document ID
type/phase/tags
represented revision
source digest
```

But:

```text
Hindsight metadata copy != manifest authority
Hindsight result != source citation
```

Derived summaries may assist retrieval only if their generated/stale posture remains explicit.

## 22. Obsidian plugin repository posture

At the 2026-08-22 checkpoint, `ifanjuang/Pantheon-plugins` exists but its only active implementation branch/PR is the draft Revit 2027 W0 adapter.

No Obsidian Pantheon plugin is currently implemented or adopted.

If this candidate proceeds after doctrine/fixture validation, `Pantheon-plugins` is the natural repository candidate for the client adapter because the repository boundary already states that Pantheon-Next governs while plugin repositories own local adapter/plugin implementations.

This note does not authorize creating that implementation yet.

## 23. First synthetic prototype scope

Before production integration, prove the UI/contract on one non-client vault fixture.

Minimum prototype:

```text
Obsidian custom Pantheon view
Pantheon Card visual grammar
bundled/pinned fluid Card navigation, Swiper if still preferred
active folder/file selection
logical package recognition
manifest absent → minimal Card
manifest present → composed Card
deterministic validation
workspace-health counters/filter
manifest direct edit for explicitly low-consequence fixture fields
Generate sheet / Modify with Hermes intent buttons
device-local offline outbox simulation
reconnect basis/digest conflict check
```

Do not add in the first prototype:

```text
production owner migration
new document/currentness owner
new tag owner
new database
new sync engine
new runtime scheduler
new memory
automatic approval
protected production write
```

## 24. Acceptance tests

### Manifestability / non-overreach

```text
ordinary folder without manifest is FREE, not erroneous
qualifiable package without manifest is visible but not treated as governed Document
generating a manifest does not itself admit professional identity
assets do not each become Pantheon objects
one package can contain many files with one logical object manifest
```

### Identity and files

```text
move/rename package preserves stable logical ID when manifest identity is unchanged
duplicate manifest stable IDs are surfaced
missing referenced source is surfaced
path/reference mismatch is surfaced
unknown schema version is surfaced
```

### Derived metadata

```text
source digest changes → generated summary becomes stale
comparison baseline digest changes → generated change summary becomes stale
derived Markdown with semantic divergence is not silently regenerated over
```

### Card

```text
Card title uses actual folder/file name
Card subtitle may use manifest/Hermes display name
Card remains a projection when manifest is absent
currentness warning cannot be created solely from newest-looking filename
Swiper/navigation state has no authority effect
```

### Offline

```text
manifest Cards render with network unavailable
local deterministic validation still works
local index deletion → successful rebuild
Hermes intent queued offline remains device-local
reconnect with same target digest → one idempotent submission candidate
reconnect with changed target digest → stale/conflict, no blind send
```

### Governance

```text
direct low-consequence fixture edit passes schema validation
invalid managed field edit is refused/surfaced
manifest field cannot directly manufacture current_for_execution
manifest field cannot admit Evidence/Decision/approval
Hermes generated summary remains derived/unreviewed until separately reviewed
```

### Sync

```text
manifest file change received through qualified sync path → local revalidation
simple manifest conflict → visible conflict, no silent governed merge
plugin cache does not need cross-device synchronization
```

## 25. Explicit non-goals

This candidate does not:

- require a manifest for every folder/file;
- make a folder a governed identity;
- make Obsidian authoritative merely because it edits the source file;
- make a manifest the authority for purpose-specific professional currentness;
- make Swiper part of the domain model;
- make plugin cache/index durable authority;
- synchronize the device-local outbox as normal workspace content by default;
- use Hindsight as the manifest owner;
- use Hermes to calculate deterministic hashes/identity;
- create a second WorkIssue/task owner;
- make Hermes Kanban the professional work authority;
- require an Obsidian instance on the NAS;
- create a new sync service;
- adopt a production manifest schema in this documentation tranche.

## 26. Decisions still open

Resolve only when the bounded fixture or owner migration needs them:

```text
which logical object types deserve a sidecar manifest
exact sidecar schema(s) and stable schema IDs
whether non-document objects use object-specific names or a generic sidecar name
exact DIRECT/MANAGED/PROJECTED field split
the final Card field grammar exposed by the plugin
whether Swiper remains the preferred plugin navigation library after prototype testing
exact device-local outbox persistence mechanism
how .obsidian plugin data interacts with the finally qualified #660 sync configuration
which low-consequence real responsibility should be the first migration candidate
```

Do not resolve these by speculative abstraction.

## 27. Candidate conclusion

The intended user experience is deliberately simple:

```text
select workspace object
→ see one Pantheon Card
→ understand whether its manifest/package is healthy
→ edit safe metadata directly
→ ask Hermes for semantic enrichment when useful
→ keep working offline
→ synchronize source files through the normal vault path
```

The architectural discipline underneath remains:

```text
manifest = source metadata for one logical object
Card = projection
plugin index = reconstructible
outbox = unsent local intent
Pantheon = rules
Hermes = semantic/action runtime
Hindsight = derived retrieval
sync = transport, not truth
```

This companion should be folded into later doctrine/schema work only where repository evidence demonstrates an owner migration need.