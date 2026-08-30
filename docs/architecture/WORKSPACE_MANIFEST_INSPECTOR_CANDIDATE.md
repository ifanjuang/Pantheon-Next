# Workspace Manifest Inspector — candidate companion to file-native convergence

Status: candidate architecture note — documentation only.

Parent roadmap: `docs/roadmaps/FILE_NATIVE_CONTROL_CONVERGENCE.md` in PR #687.
Parent workspace exploration: Pantheon-Next #684.
Related qualification: #660 for Self-hosted LiveSync/CouchDB offline, reconnect, conflict and optional Obsidian Web behavior.

This note defines one bounded UX/adapter candidate for the file-native convergence roadmap. It does **not** adopt a production manifest schema, migrate a current owner, create a new Document identity model, modify currentness semantics, extend the Tag Registry, implement an Obsidian plugin or authorize production writes.

## 1. Repository facts this candidate must respect

Checkpoint: 2026-08-22.

```text
Pantheon-Next/main = 8c15eff5c767c76410db9e0f3a2e388f85ed1aac
pantheon-mvp/main  = d960862dd0e23b7003a0f3e4ee0ea630ffc12af9
```

Observed contracts relevant to this slice:

- the existing Professional Document family contract uses a stable `document_family_id` UUID across revisions;
- Document currentness is a **read-only calculated projection** per declared purpose, with `resolved | unresolved | conflicting`, and is explicitly not a persisted universal current-version authority;
- professional purposes already include `latest_received`, `latest_reviewed`, `current_working`, `current_for_coordination`, `current_for_consultation`, `current_contractual`, `current_for_execution`, `current_for_site` and `latest_as_built_candidate`;
- the current Tag Registry accepts simple stable slugs and currently exposes the `type` and `subject` groups; slash-separated hierarchical tag paths are not part of the current schema;
- WorkIssue already carries comments, Hermes runs and events and has `waiting` as a governed status, but persistence/transition enforcement belongs to its reviewed executable adapter;
- #660 remains open: CouchDB on Synology, native Obsidian clients with Self-hosted LiveSync, offline/reconnect/conflict qualification and optional Obsidian Web are **targets to verify**, not completed production facts;
- `Pantheon-plugins` has no observed Obsidian Pantheon implementation; its current open implementation PR is the draft Revit adapter.

Therefore this note must not invent parallel Document IDs, parallel currentness, a second tag vocabulary, a second Work owner or a new synchronization owner.

## 2. Goal

Make file-native workspace health understandable and actionable close to the files, especially from Obsidian, while retaining the existing Pantheon Card visual grammar.

Candidate UX:

```text
selected workspace object
→ Pantheon inspector Card
→ local manifest/package diagnostics
→ safe direct edits where explicitly allowed
→ optional Hermes semantic assistance
```

The candidate plugin is primarily:

```text
local workspace inspector
+ manifest editor
+ deterministic consistency checker
+ Card projection surface
+ optional fluid Card navigation
```

It is not:

```text
business database
Document lifecycle owner
currentness owner
workflow engine
memory system
Hindsight replacement
sync engine
approval engine
new Card authority
```

## 3. Authority model

Keep the file-native roadmap model unchanged:

```text
Files / Sources = professional and workspace content
Pantheon        = rules and governed boundaries
Hermes          = reasoning and action runtime
Hindsight       = derived retrieval and associations
Cockpit         = projection and interaction
```

For this slice:

```text
manifest file
= source metadata only for a logical object whose responsibility
  has explicitly become file-native

plugin local index/cache
= reconstructible projection state

plugin offline outbox
= unsent device-local user intent

Card
= composed projection

Pantheon
= normative validation and governed-boundary rules

Hermes
= semantic enrichment and candidate work
```

Preserve:

```text
manifest present != governed identity admitted
manifest valid != professional approval
folder contains files != logical Document
folder/path != governed identity
plugin warning != professional currentness result
local outbox item != WorkIssue
Hermes proposal != manifest truth
Swiper position != authority
sync success != Evidence
```

## 4. Manifestability — logical object, not filesystem entry

Do **not** require a manifest for every file or folder.

Architecture-agency folder conventions and their optional posture are owned by `docs/domain-packs/architecture/DOCUMENT_AND_KNOWLEDGE_ORGANIZATION.md`. The Inspector must accept another existing organization as usable. It may expose a mapping or reclassification proposal, but neither manifest absence nor divergence from the recommended profile makes an ordinary folder invalid or authorizes a move.

One candidate document package may contain several physical entries:

```text
CCTP/
├── document.yaml
├── CCTP.md
├── CCTP - Ind C.pdf
├── assets/
└── Archives/
    └── CCTP - Ind B.pdf
```

This may represent one logical professional Document family, not one Pantheon object per file.

Examples that may legitimately remain unmanifested:

```text
Notes/
Photos/
assets/
ordinary working notes
temporary images
pure navigation folders
```

The inspector may expose these **UX health states**:

```text
FREE
no manifest is expected

QUALIFIABLE
local observations suggest a logical object could benefit from qualification,
but no governed identity is inferred

COHERENT
manifest/package passes the applicable local structural checks

CHECK
non-fatal divergence or stale derived metadata requires attention

INVALID
manifest cannot satisfy the applicable contract
```

These labels are presentation vocabulary only. In particular:

```text
COHERENT health state
!= managed/protected write posture
```

A heuristic may suggest `QUALIFIABLE`, but only an explicit rule/qualification path may make a manifest required.

Optional Obsidian skills or second-brain behavior are consumers of this posture, not alternative manifest owners. They may discover, read or lint a sidecar and prepare a correction candidate, but they must not silently create a required-manifest rule, redefine manifest semantics, mutate professional status or move files. The capability boundary and optional layering are recorded in `docs/governance/OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`.

The first executable slice derived from this candidate is read-only. It may
parse a present sidecar, calculate exact observed digests and project local
health, but it must not persist those observations on read. Persisted manifest
writes require a separately admitted schema and write contract.

## 5. Candidate document sidecar

For a real document package, `document.yaml` remains a reasonable candidate user-facing sidecar name because it is readable, editable and schema-validatable.

Do not maintain YAML and JSON mirrors of the same sidecar by default.

### Identity constraint

If the sidecar represents an existing governed Professional Document, it must reuse the existing Document family/version identity semantics rather than inventing a second ID namespace.

Current contracts use UUIDs such as:

```text
document_family_id
Document version identity
```

Therefore examples such as:

```text
document:cctp-lieurey
revision:cctp-C
```

must **not** be treated as adopted IDs.

An offline skeleton may exist before qualification, but it must not silently manufacture a governed Document identity. The eventual qualification path must first determine whether it maps to an existing Document family/revision or creates a new admitted identity under the applicable owner.

### Illustrative carrier only

The exact schema is intentionally not fixed here. A future sidecar may need concepts equivalent to:

```yaml
schema: <candidate schema identity/version>

identity:
  document_family_id: <existing admitted UUID or unresolved candidate>

display:
  full_name: Cahier des clauses techniques particulières — DCE

artifact_origin: authored

tags:
  - cctp

representation:
  markdown:
    file: CCTP.md
    role: <candidate representation role>

represented_version:
  document_version_id: <existing admitted UUID when known>
  index_label: C

derived_summary:
  text: CCTP de consultation...
  based_on_digest: sha256:...
  generation_status: generated_unreviewed
```

This is explanatory structure, not a schema proposal ready for implementation.

### Tag constraint

The example deliberately uses current-compatible simple slugs such as `cctp`.

Candidate paths discussed elsewhere, for example:

```text
type/cctp
phase/dce
sujet/lot/plomberie
```

require explicit Tag Registry convergence first. The current `stable_slug` contract does not accept slash-separated paths and the current operational groups are only `type` and `subject`.

Do not persist candidate hierarchical tags through this sidecar before that convergence is reviewed.

## 6. Authored, received and derived are separate dimensions

Do not use one `document_role: derived` value to mean both a received professional artifact and its generated Markdown representation.

Separate at least conceptually:

```text
ARTIFACT ORIGIN / AUTHORSHIP
= authored internally | received/external | other declared origin

REPRESENTATION ROLE
= canonical working representation | exact source/snapshot | derived representation
```

### Internally authored example

```text
CCTP.md
= candidate canonical working representation after owner migration

CCTP - Ind C.pdf
= exact issued/export snapshot when declared as such
```

The PDF is not automatically the source owner merely because it exists next to the Markdown.

### Received/external example

```text
Rapport BET - Ind C.pdf
= exact received source

Rapport BET.md
= derived structural/Markdown representation
```

The received artifact itself is not `derived`; only its generated representation is.

Hermes may analyse a derived Markdown representation, but must not rewrite it as though it were the exact received source.

If a generated Markdown file changes after generation, automatic regeneration must first compare its current digest with the last generated-output/baseline digest. A mismatch is a deterministic overwrite-risk signal; the system must not claim it has semantically classified the human change merely from the digest.

## 7. Sidecar scope versus currentness

Candidate sidecar responsibilities may include:

```text
stable identity mapping once admitted
schema identity/version
full human designation
short human-authored annotation
artifact origin / representation role
current-compatible classification refs
representation refs
represented version/index label
source/snapshot refs and digests where applicable
derived summary + exact basis digest
source-to-source change summary + both exact basis digests
conversion/derivation provenance where useful
navigation refs to bounded workspace discussions
```

Human annotation and discussion references remain collaboration metadata. They
do not express professional approval, purpose-specific currentness, Evidence or
a Decision. A detailed Hermes exchange belongs in a separate Markdown working
note rather than being copied into the sidecar.

Do **not** make ordinary editable sidecar fields authoritative for:

```text
latest_received
latest_reviewed
current_working
current_for_coordination
current_for_consultation
current_contractual
current_for_execution
current_for_site
Evidence admission
Decision legitimacy
authorization
professional approval
```

Currentness is already defined as a calculated purpose-specific projection from governed inputs.

Therefore:

```text
represented index label = C
!= C is current_for_execution

latest_received = D
!= D is contractual or executable authority
```

The inspector may display currentness only from the applicable currentness projection/resolver. Offline, it must show that overlay as unavailable or based on a clearly identified last-known projection; it must never infer it from filenames, path order, modification time or the sidecar alone.

## 8. Card projection

The Card is a **composition**, not a YAML mirror.

Candidate inputs:

```text
manifest
+ observed local package state
+ locally available/pinned registry rules
+ purpose-specific Pantheon currentness projection when available
+ related Work projection when relevant
→ Card
```

### Title/subtitle rule

For filesystem/workspace navigation:

```text
Card title
= actual selected folder/file name

Card subtitle
= fuller human designation from the sidecar or a reviewed/generated proposal
```

Example:

```text
CCTP
Cahier des clauses techniques particulières — DCE
```

The semantic subtitle does not replace the filesystem title.

### No sidecar

```text
CCTP
Dossier non qualifié

Markdown détecté
PDF détecté

[ Générer la fiche ]
```

The Card remains a neutral workspace projection. It does not claim the folder already is a governed Document.

### Sidecar present

```text
CCTP
Cahier des clauses techniques particulières — DCE

✓ Manifest structurel
✓ Source/référence locale
⚠ MD représente C
? Currentness distante indisponible ou projetée séparément
✓ Tags connus localement
⚠ Résumé fondé sur un ancien digest

[ Modifier ]
[ Modifier avec Hermes ]
```

If the currentness projection is online and resolves `latest_received = D`, the Card may add that fact while preserving the distinction between `latest_received` and other professional purposes.

Do not encode candidate status/phase/portée dimensions in the sidecar merely to reproduce a visual example until their actual owner/registry contract is resolved.

## 9. Preserve Pantheon Card design; Swiper remains presentation

Reuse the existing Pantheon Card visual grammar where practical:

```text
front   = understand
back    = work around the object
details = provenance / diagnostics
```

Candidate Obsidian surface:

```text
Obsidian custom ItemView
→ Pantheon Card presentation
→ optional fluid Card navigation
```

Swiper is a good implementation candidate because the Cockpit already uses and tests it, but:

```text
Card contract != Swiper
```

If retained in an Obsidian plugin, the dependency should be bundled/pinned with the plugin rather than fetched from a runtime CDN so the local UI does not depend on network availability.

Mobile support must use Obsidian-compatible APIs and avoid unconditional Node/Electron dependencies.

## 10. Workspace-health view

The plugin-specific value is a quality-control view, not a second file explorer.

Candidate summary:

```text
PANTHEON — WORKSPACE

183 coherent
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

A Card/Swiper sequence over anomalies is useful because it creates a review workflow without giving the Card a new lifecycle.

## 11. Deterministic validation

Most structural checks should not require Hermes.

Candidate local checks, **only when the required basis is locally available**:

```text
invalid YAML
unsupported schema version
duplicate admitted ID within the locally declared scope
missing locally referenced source
missing representation
relative path/reference mismatch
digest mismatch
unknown tag against the locally pinned Tag Registry revision
summary basis digest stale
change-summary before/after digest stale
derived Markdown current digest != last generated-output digest
represented source/version binding stale when exact local basis proves it
```

For relations:

```text
locally resolvable target missing
→ local broken-reference warning

external/server-owned target unavailable offline
→ unknown/unresolved locally
→ not automatically broken
```

A filesystem-placement warning is also local only:

```text
newer-looking file observed under Archives/
→ organization warning candidate
!= professional currentness decision
```

## 12. Offline rule bundle / validation provenance

Offline validation cannot claim parity with Pantheon rules unless the client knows which rules it used.

The prototype must therefore define a local rule-bundle posture equivalent to:

```text
schema identity + revision/digest
Tag Registry identity + revision/digest
validator compatibility version
```

The plugin may use a bundled/pinned or previously qualified local rule snapshot, but every local health result should be attributable to that rule revision.

On reconnect, the server remains free to revalidate against the current applicable normative contracts.

```text
local validation passed
!= server/current-rule validation passed
```

Do not create a new rules service merely to solve this. One normative rule owner plus conformance tests is sufficient unless implementation evidence proves otherwise.

## 13. Hermes-assisted generation and modification

Use Hermes only where semantic interpretation adds value.

Candidate actions:

```text
Générer/enrichir la fiche
Générer ou mettre à jour le résumé
Analyser les principaux changements
Proposer des tags compatibles
Expliquer une incohérence
Proposer une correction de fiche
```

One optional `workspace-manifest` skill may expose the bounded modes
`inspect`, `validate`, `propose-create` and `propose-update`. Those modes reuse
the current manifest owner and return candidates; they do not create a second
schema or writer. An `apply` mode is deferred until a deterministic writer,
expected-current-digest checks and the consequential-effect gate are admitted.

Separate responsibilities:

```text
DETERMINISTIC / ADAPTER
observed files
paths
exact digests
existing identity lookup/resolution
schema/registry validation
version/source bindings available from owners

HERMES
full human designation
summary
semantic classification candidates
principal-change summary
ambiguity explanation
proposed correction
```

A button may say `Générer la fiche`, but Hermes must not invent:

```text
governed identity
exact digest
Document version identity
purpose-specific currentness
professional approval
```

### No-manifest generation path

Preferred candidate sequence:

```text
inspect exact local package
→ determine whether qualification is eligible
→ resolve/reuse existing Document family/version identity when available
→ create only an unadmitted skeleton if identity cannot be governed offline
→ Hermes semantic enrichment if requested/available
→ validate against applicable rules
→ bounded write
→ re-read
```

Creating a sidecar is not itself Document admission.

Generated semantic fields should record their exact basis and become stale when that basis changes.

### Multi-document Hermes working discussion

A workspace-local Markdown discussion may coordinate one request across several
targets, for example a CCTP correction and the corresponding DPGF update. It
should carry explicit relative target refs and expected digests so that a later
proposal can be detected as stale.

The discussion is working context only:

```text
Hermes working discussion != exact-revision professional comment
Hermes working discussion != Decision or approval
manifest discussion ref    != authority transfer
```

The existing implementation owner for comments on one exact admitted document
revision remains unchanged. Promotion of a useful conclusion from a workspace
discussion into that owner is explicit, not an automatic two-way sync.

## 14. Direct editing versus governed fields

The inspector may expose direct controls only for fields whose owner/write posture permits it.

Candidate ownership split:

```text
HUMAN-OWNED WORKSPACE METADATA
short manual comment
explicit request to link or unlink a working discussion

AI-PROPOSED / HUMAN-REVIEWED
full display name
ordinary currently valid tag refs
working derived-summary text
other explicitly admitted workspace metadata

MANAGED / DETERMINISTIC
identity mapping
schema version
source/snapshot digests
representation bindings
version refs
validation result and observation timestamp when the adopted schema permits them

PROJECTED OR GOVERNED ELSEWHERE
purpose-specific currentness
Evidence
Decision
authorization
professional approval
```

This split is not adopted until Phase 2 owner/doctrine convergence classifies the actual fields.

Automatic refresh, if later admitted, is limited to the managed deterministic
subset and must compare the expected current manifest digest before writing.
Human-owned fields are changed only by an explicit human action. AI-proposed
fields remain candidates until reviewed. A managed-field refresh must preserve
unknown and human-owned YAML content through a round-trip-capable writer.

`Modifier avec Hermes` should produce a bounded proposal/diff against an expected current basis digest. Consequential application remains subject to the existing Workspace write/gate model.

## 15. Local-first index/cache

Basic manifest health should not require a server round-trip. The first
implementation slice calculates it on demand and remains read-only; incremental
events, a persistent local index and any sidecar refresh are later qualification
steps rather than MVP prerequisites.

Candidate behavior:

```text
local vault
→ initial bounded scan
→ reconstructible local index
→ Cards / warnings / filters
```

Then use incremental vault events:

```text
create
modify
rename
move/delete observation
→ revalidate affected object/package
```

A manual full rescan remains available for repair/rebuild.

Possible cached observations:

```text
path → package candidate
manifest path/digest
rule-bundle revision used
schema status
source/representation digest observations
warnings
last local scan observation
```

But:

```text
plugin index/cache != authority
```

Deleting it must cause at most a rebuild.

## 16. Offline behavior

Where the local vault contains the required files and local rule bundle, the inspector should remain useful without Pantheon/Hermes/Hindsight connectivity.

Candidate offline-capable functions:

```text
browse local Cards
read manifests
run local deterministic checks
edit fields explicitly allowed offline
create an unadmitted deterministic skeleton
inspect local source/representation consistency
prepare a Hermes request for later submission
```

Degraded overlays must be explicit:

```text
Hermes unavailable
→ semantic generation unavailable
→ optional local intent queue

Pantheon/currentness unavailable
→ local manifest health remains available
→ currentness overlay unavailable or explicitly last-known

Hindsight unavailable
→ semantic retrieval unavailable
→ local manifest inspection remains available
```

## 17. Offline Hermes outbox

An unsent request is device-local intent, not a WorkIssue or Hermes task.

Candidate envelope dimensions:

```text
request/correlation ID
local target locator
admitted target identity if already known
expected manifest/package digest or revision basis
action
creation time
idempotency key
```

Exact fields remain open.

Reconnect behavior:

```text
resolve current target
→ compare current basis with expected basis
→ unchanged: submit one idempotent request candidate
→ changed: mark local intent stale/conflicted
→ never send blindly
```

### Device-local means proven device-local

Do **not** assume Obsidian plugin data is device-local merely because it is stored by the plugin.

Self-hosted LiveSync can optionally synchronize selected hidden/configuration/plugin files under `.obsidian`. Therefore the prototype must prove that the chosen outbox persistence is excluded from the qualified synchronization path, or use another explicitly device-local mechanism.

```text
outbox storage observed local on one device
!= guaranteed device-local under every LiveSync configuration
```

Server idempotency remains defence in depth even when the outbox is correctly device-local.

The existing `pantheon-mvp` mobile editor is precedent for local queued Hermes edit requests with idempotency; reuse the invariant, not necessarily its current localStorage implementation.

## 18. WorkIssue and Hermes boundary

Do not say that WorkIssue begins only after execution admission.

The current sequence may create durable Work before runtime admission.

Candidate boundary:

```text
device-local unsent intent
→ server receipt + validation
→ bounded handoff / WorkIssue when durable treatment is needed
→ separate execution admission when applicable
→ Hermes runtime
```

If Hermes needs clarification, the existing Work model can represent a `waiting` state and comments. A future Card projection may surface the related question, but that UI behavior is not currently implemented by this note.

```text
human response to issue
!= Decision
!= approval
!= Evidence
```

Do not use WorkIssue, Hermes Kanban or a synchronized vault exchange file as the owner of **unsent** device-local clicks.

A Hermes runtime-side queue/Kanban, if used for admitted execution, remains runtime organization rather than professional Work authority.

## 19. Sync and NAS topology

#660 is a qualification issue, not a completed deployment contract.

Target under test:

```text
PC / portable / mobile
= native Obsidian + Self-hosted LiveSync
        │
        ▼
CouchDB on Synology
        ▲
        │
other qualified Obsidian client
```

Preserve:

```text
CouchDB = synchronization transport/state
CouchDB != memory
CouchDB != Pantheon authority
sync success != Evidence
```

Source workspace files and manifests may use the selected vault sync path once #660 qualifies it.

The reconstructible local index should not require synchronization.

The outbox must be excluded from synchronization unless a different, explicitly designed multi-device intent owner is later demonstrated.

For managed/protected records, a sync conflict must be surfaced and must not silently create a professional currentness or approval decision.

### NAS

Do not require Obsidian or the Inspector plugin on the NAS.

Candidate service topology:

```text
clients
= Obsidian + Pantheon Inspector

NAS
= Pantheon services as deployed
+ Hermes
+ Hindsight
+ CouchDB
+ other qualified services/adapters
```

If #660 later qualifies an optional Obsidian Web/Docker client on the NAS, that client may run Self-hosted LiveSync and, if useful, the same Inspector plugin. It remains optional and must not become an authority merely because it is always on.

## 20. Hindsight boundary

Do not index raw manifest YAML as a separate semantic note by default.

Preferred candidate direction:

```text
document.yaml
→ metadata/classification carrier

Document.md
→ semantic content
→ Hindsight derived retrieval
```

Selected manifest metadata may enrich ingestion context only after the actual Tag/Document mapping is defined.

```text
Hindsight metadata copy != manifest authority
Hindsight result != source citation
retrieved != truth
```

Derived summaries may assist retrieval only with their generated/stale posture preserved.

## 21. Plugin repository posture

No Obsidian Pantheon plugin is currently observed in `Pantheon-plugins`.

If this candidate survives doctrine and synthetic-fixture review, `Pantheon-plugins` is a reasonable repository candidate because it already separates local adapters/plugins from Pantheon-Next governance.

This is a repository-placement recommendation, not an implementation authorization.

## 22. First synthetic prototype

Use a non-client/sandbox vault only.

Minimum proof:

```text
Obsidian custom view
Pantheon Card visual grammar
optional bundled/pinned Swiper or equivalent fluid navigation
active folder/file selection
FREE versus QUALIFIABLE distinction
manifest absent → neutral Card
manifest present → composed Card
current-compatible tag validation
deterministic local health checks with rule-bundle revision
workspace-health counters/filter
safe fixture-only direct edit
Generate/Modify-with-Hermes intent button
device-local outbox proof under the selected LiveSync settings
reconnect basis/digest conflict check
```

Do not add:

```text
production owner migration
new Document/currentness owner
new tag owner
new database
new sync engine
new runtime scheduler
new memory
automatic approval
protected production write
```

## 23. Acceptance tests

### Manifestability / non-overreach

```text
ordinary folder without manifest = FREE, not error
heuristic package suggestion = QUALIFIABLE, not governed Document
sidecar creation alone does not admit Document identity
assets do not each become Pantheon objects
one logical package may contain many physical files
read-only inspection does not persist observed fields
```

### Identity

```text
existing Document family is reused when qualification resolves it
unadmitted offline skeleton cannot manufacture professional admission
move/rename preserves admitted stable family identity
local duplicate admitted IDs are surfaced
unknown/foreign identity is not selected by path order
```

### Currentness

```text
index label alone cannot create current_for_execution
latest_received cannot be treated as universal authority
unresolved/conflicting currentness remains visible
currentness unavailable offline is not inferred from filename/mtime/path
```

### Tags

```text
current simple slugs validate against exact local Tag Registry revision
slash-separated candidate paths are rejected until registry convergence adopts them
unknown tag is surfaced without invented semantics
```

### Derived metadata

```text
source basis digest changes → generated summary stale
comparison basis digest changes → generated change summary stale
derived Markdown digest differs from generated baseline → no silent overwrite
```

### Card

```text
Card title = real folder/file name
Card subtitle may use reviewed/generated full designation
Card remains projection without sidecar
Swiper/navigation state has no authority effect
```

### Offline/local rules

```text
Cards render without network
local validation records schema/registry revision used
local index deletion → rebuild succeeds
server reconnect may revalidate against newer rules
```

### Outbox

```text
offline intent remains device-local under qualified sync settings
same basis on reconnect → one idempotent submission candidate
changed basis → stale/conflict; no blind send
second device does not receive the outbox through ordinary vault sync
```

### Work/governance

```text
unsent intent != WorkIssue
server receipt may create Work before execution admission
waiting/comment does not become Decision or approval
manifest edit cannot admit Evidence/Decision/approval
Hermes generated summary remains derived/candidate
automatic technical refresh cannot change human or governed fields
workspace discussion remains distinct from exact-revision comments
```

### Sync

```text
manifest change through qualified sync path → local revalidation
manifest conflict → visible conflict; no silent governed merge
plugin index does not need cross-device synchronization
```

## 24. Open decisions

Resolve only when a bounded fixture or owner migration demonstrates the need:

```text
which logical object types deserve sidecars
exact sidecar schema IDs and fields
exact mapping to existing Document family/version schemas
whether non-document objects use object-specific or generic sidecar names
how an offline candidate skeleton represents unresolved identity
exact low-consequence versus managed field split
final Card field grammar
whether Swiper remains preferred after mobile prototype
exact local rule-bundle packaging/update mechanism
exact device-local outbox persistence mechanism
final #660 hidden/config/plugin sync posture
first low-consequence real owner migration candidate
```

Do not solve these with speculative abstractions.

## 25. Conclusion

The intended UX stays small:

```text
select workspace object
→ see one Pantheon Card
→ understand local manifest/package health
→ edit explicitly safe metadata
→ ask Hermes for semantic assistance when useful
→ keep local inspection usable offline
→ synchronize source files through the qualified vault path
```

The architecture stays smaller than the interface:

```text
manifest = metadata carrier for one logical object after explicit owner mapping
Card = projection
plugin index = reconstructible
outbox = proven device-local unsent intent
Pantheon = normative rules and governed boundaries
Hermes = semantic/action runtime
Hindsight = derived retrieval
sync = transport, not truth
```

This companion should feed later doctrine/schema work only where repository evidence demonstrates a real owner-migration need.
