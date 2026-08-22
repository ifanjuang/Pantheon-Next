# File-native Pantheon Control Convergence

Status: candidate convergence roadmap — documentation only.

This document records a target architecture and migration method. It does **not** modify current Pantheon doctrine, transfer authority, migrate persistence, authorize a runtime, remove PostgreSQL, adopt a vault topology, or deprecate any existing owner by itself.

Parent exploration: `Pantheon-Next#684`.

## 1. Objective

Converge the current Pantheon ecosystem toward a smaller and more maintainable architecture in which:

```text
FILES / WORKSPACE
= human-readable professional content and declared state

PANTHEON-NEXT
= rules, schemas, registries, policy and governance invariants

PANTHEON EXECUTABLE CONTROL
= validation, policy enforcement, bounded gates and transactional runtime safety

HERMES
= reasoning and execution runtime

HINDSIGHT
= derived semantic retrieval and associative graph

MNEMOSYNE
= Hermes conversational/runtime continuity

COCKPIT
= projection and interaction surface
```

The intended simplification is not "replace PostgreSQL with Obsidian". It is:

```text
put each responsibility in the simplest storage/mechanism that actually needs it
```

The target should preserve useful functionality while reducing duplicate systems of record, duplicate retrieval paths and unnecessary business persistence.

## 2. Verified repository baseline

Checkpoint: 2026-08-22.

```text
Pantheon-Next/main
= 8c15eff5c767c76410db9e0f3a2e388f85ed1aac

pantheon-mvp/main
= d960862dd0e23b7003a0f3e4ee0ea630ffc12af9
```

Observed active work at this checkpoint:

- `Pantheon-Next` PR #685 records Hermes memory-provider qualification;
- `Pantheon-Next` PR #686 converges source research into one Hermes skill candidate;
- `pantheon-mvp` has no open PR;
- `pantheon-mvp` #333 and #337 already provide the first read-only filesystem workspace projection seam into generic Card/Collection navigation;
- `Pantheon-Next` #684 remains the parent workspace/navigation brainstorming issue.

This roadmap must be rechecked against current `main`, open PRs and active branches before every implementation tranche.

## 3. Problem being solved

The current executable MVP is deliberately broad. It has been useful for discovering, encoding and testing responsibilities including:

```text
Projects / Agency Data
Information
Knowledge
Categories
Relations
Documents
Claims
Decisions
Work Issues
source ingestion
extraction
pgvector retrieval
Hermes handoff/admission/results
Cockpit
human access
storage retention
```

That breadth has produced strong contracts and tests, but also creates a long-term risk of several concurrent representations of the same professional reality:

```text
PostgreSQL business state
+ workspace / Obsidian files
+ Hindsight derived memory
+ Cockpit projections
```

The target architecture should keep the contracts and invariants that proved useful while removing persistence or abstraction that no longer has a demonstrated independent responsibility.

## 4. Minimal mental model

The architecture should remain understandable through five primary statements:

```text
Files     = professional/workspace content
Pantheon  = rules
Hermes    = action
Hindsight = retrieval
Cockpit   = view
```

Two supporting components remain deliberately separate:

```text
Mnemosyne
= Hermes conversational/runtime memory

Transactional control storage
= only state that genuinely requires atomicity, replay protection or durable execution authorization history
```

Terms such as PDP, PEP, ledger, admission or receipt are implementation responsibilities. They should not become additional user-facing architecture layers unless a distinct deployed component is demonstrably required.

## 5. Target responsibility model

### 5.1 Files / workspace

Candidate target:

```text
workspace files
= canonical professional/work content when that owner has been explicitly migrated to file-native persistence
```

The architecture is **file-native**, not Obsidian-native.

Obsidian may be the preferred human editor, but the source remains the file so another editor can replace Obsidian without migrating business state.

A path is not a governed identity:

```text
folder != Project identity
path != EntityRef
rename != new professional object
```

File-native governed records therefore require stable IDs when stable identity is needed.

Example candidate shape:

```yaml
id: project:lieurey
kind: project
```

No exact frontmatter vocabulary is adopted by this roadmap.

### 5.2 Pantheon-Next

Pantheon-Next remains the unique normative source for:

```text
doctrine
schemas
controlled vocabularies / registry contracts
policy classification
validation rules
governance boundaries
promotion / approval / Evidence distinctions
tests of invariants
```

Pantheon-Next must not become the business database for real agency projects.

The existing policy service/PDP direction should be reused rather than creating another policy compiler or parallel rules engine.

### 5.3 Pantheon executable control

The future reduced role currently implemented largely inside `pantheon-mvp` is to apply Pantheon rules around real operations.

Candidate responsibilities:

```text
TaskContract / ContextPack validation
policy enforcement
bounded write gates
human approval gates where required
workspace adapter
exact-source reads and digests
authentication / technical access adapters
ExecutionAdmission
LaunchReservation
replay / idempotency protection
runtime execution receipts
```

This control layer should not own professional content merely because it needs to validate or mutate that content.

### 5.4 Hermes

Hermes remains the reasoning/execution runtime.

Pantheon should constrain boundaries, not prescribe the internal chain of thought or every intermediate reasoning step.

Pantheon may define:

```text
objective
scope
available sources
allowed tools/effects
forbidden effects
required review/approval
expected result contract
```

Hermes may choose how to search, plan, reason, use skills and compose tools inside those boundaries.

### 5.5 Hindsight

Hindsight is the preferred candidate for:

```text
semantic retrieval
associative recall
entity/relationship discovery
temporal context
derived semantic graph
```

It remains reconstructible from source material and must not become Pantheon authority.

Target retrieval safety for consequential work:

```text
question
→ Hindsight candidate recall
→ exact source references
→ exact current file/source read
→ Pantheon validation/qualification
→ Hermes use
```

Therefore:

```text
Hindsight recall != source
Hindsight relation != governed relation
retrieved != truth
```

A successful Hindsight migration may allow retirement of Pantheon's duplicate custom chunk/embedding/pgvector path, but only after comparative acceptance tests.

### 5.6 Mnemosyne

Mnemosyne remains separate from Hindsight:

```text
Mnemosyne
= fluid Hermes conversational/runtime continuity

Hindsight
= workspace-derived retrieval / knowledge context
```

Neither becomes Evidence or professional authority.

### 5.7 Cockpit

Cockpit remains a projection and interaction surface.

The already-merged generic filesystem Card/Collection projection should be reused as the main workspace seam rather than inventing another navigation model.

Candidate long-term root UX may converge toward a small set such as:

```text
Pantheon
Affaires
Documentation
Outils
```

Names and topology are not adopted by this roadmap and must not become hard-coded business constants prematurely.

## 6. Canonical content versus authorized transition

File-native persistence must not collapse professional content with execution authorization.

A file may declare a state while Pantheon separately determines whether the transition into that state was legitimately admitted.

Example:

```text
file contains status: approved
!= approval was authorized
```

The architecture therefore separates:

```text
FILE
= declared professional/work state

SCHEMA
= structural validity

POLICY / GATE
= whether a transition is permitted

RECEIPT / CONTROL RECORD
= whether a consequential transition was actually admitted/executed against the expected identity/revision/digest
```

This distinction is essential to preserve:

```text
execution success != authorization
edited text != approved state change
```

## 7. Candidate protection classes

To avoid making all workspace editing equally heavy, future doctrine should evaluate a small protection model rather than forcing every write through the same workflow.

Candidate distinction:

```text
NORMAL
ordinary direct edit

MANAGED
must satisfy declared schema/invariants

PROTECTED
consequential transition requires a Pantheon gate/receipt
```

Illustrative only:

```text
working note            -> normal
Project metadata        -> managed
tag/nomenclature file   -> managed
professional Decision   -> protected where consequential
Evidence admission      -> protected
external effect         -> protected
```

This roadmap does not adopt these names or classifications. Phase 2 must decide whether the existing doctrine can express the same requirement more simply.

## 8. Tags, folders, Categories and relations

### Folders

Candidate role:

```text
location / navigation / working scope
```

Never professional identity or authorization.

### Tags

Candidate role:

```text
classification / facets / discoverability / presentation context
```

The existing Tag Registry should be extended/reused before creating another taxonomy owner.

### Category

The current Category/CategoryAssignment implementation is mature, but its long-term independent responsibility is now open.

Phase 2/3 should test whether hierarchical stable tags plus folders/facets can preserve every useful Category requirement.

Only if that equivalence is demonstrated should Category become a deprecation candidate.

```text
possible simplification != Category already obsolete
```

### Entity relations

Tags do not replace typed relations.

A governed relation has at minimum:

```text
source EntityRef
relation type
target EntityRef
```

Examples:

```text
A supersedes B
A contradicts B
A relies_on B
```

The relation does not necessarily require a dedicated PostgreSQL owner. Phase 2 should evaluate structured file-native relation declarations using stable EntityRefs while keeping Hindsight-inferred relations explicitly derived/candidate-only.

## 9. PostgreSQL target posture

This roadmap does **not** decide to remove PostgreSQL.

It proposes reducing business persistence only where another source owner is demonstrated.

Long-term candidate residual responsibility:

```text
transactional control state
```

Typical examples:

```text
ExecutionAdmission
LaunchReservation
one-shot authorization consumption
idempotency keys
technical grants/auth state
short-lived locks/reservations
runtime execution receipts
```

These are poor candidates for normal Obsidian editing because their essential properties are atomicity, concurrency protection or replay safety.

Conversely, PostgreSQL should not remain the owner of a business concept merely because the implementation already has a table for it.

Storage technology remains replaceable. PostgreSQL should only be replaced later if the proven residual transactional requirements justify a simpler store.

## 10. Required doctrine convergence — phase 2

The architecture in this roadmap intentionally goes beyond several current candidate/support rules. Implementation must not proceed by silently violating those rules.

Before file-native owners replace existing owners, perform a dedicated doctrine-convergence phase.

### 10.1 `AGENCY_DATA_SYSTEM_OF_RECORD.md`

Current direction still declares PostgreSQL Agency Data as the default native system of record.

Required review question:

```text
Can selected Agency/workspace records declare file-native sources of record while Pantheon governs their transitions and stable identities?
```

If accepted, update the doctrine explicitly before migrating those owners.

### 10.2 `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`

Current doctrine distinguishes source and projection but still treats many Obsidian representations as projections and retains Pantheon-side professional owners.

Required review questions:

```text
When is Markdown itself the canonical source?
When is an Obsidian note only a projection?
How are durable trust domains/vaults/banks declared?
How is one-way Hindsight derivation preserved?
```

The rule must distinguish source files from editable projections instead of using "Obsidian" as one semantic category.

### 10.3 Category / Tag doctrine

Do not remove Category first.

Required procedure:

```text
inventory Category consumers/invariants
→ map each to hierarchical Tag/folder/facet capability
→ run acceptance tests
→ decide retain / reduce / retire
```

If Category becomes redundant, update doctrine/contracts before deleting its executable owner.

### 10.4 Registry ownership

Current registry foundation allows Pantheon-Next to own validation contracts while operational instances may live in `pantheon-mvp`.

Required review question:

```text
Should agency-specific registry instances such as tag vocabulary live with the agency workspace while Next retains only the schema/semantic contract?
```

No duplicate `Tags.md` / `tags.json` / MVP registry authority is permitted.

### 10.5 Control-plane boundary

Preserve the existing distinction:

```text
Pantheon governs
Hermes executes
```

Any executable control retained in `pantheon-mvp` must remain an enforcement/adapter responsibility and must not cause Pantheon-Next itself to become scheduler, queue, tool runtime or hidden agent executor.

## 11. Migration method

Use a strangler/convergence migration. Do not rewrite the system in one step.

### Phase 0 — architecture decision and inventory

For each current MVP responsibility, extract:

```text
canonical content
invariants
transaction requirement
provenance requirement
projection
retrieval/index requirement
current consumers/tests
```

Completion criterion:

```text
each responsibility has a proposed owner decomposition with no unexplained duplicate authority
```

### Phase 1 — this documentation tranche

Record target architecture, boundaries, migration procedure and doctrine gaps.

No runtime/persistence change.

### Phase 2 — doctrine convergence

Modify Pantheon-Next rules explicitly where the target would otherwise contradict current doctrine.

Requirements:

- one reviewed change at a time;
- exact current owner and consumer inventory;
- preserve governance non-equivalences;
- add/update schemas/tests when a new machine-checkable invariant is adopted;
- no implementation merge that depends on an unmerged doctrine change.

### Phase 3 — bounded file-native fixture

Build a non-production fixture proving:

```text
stable IDs independent of paths
arbitrary folder hierarchy
file parsing/validation
normal vs consequential write boundary
exact digest/revision checks
workspace → Card/Collection projection
Hindsight one-way derivation
```

No production owner migration yet.

### Phase 4 — retrieval convergence

Compare Hindsight against the existing Pantheon retrieval path on representative agency/project questions.

Acceptance must measure useful retrieval, scope isolation and exact-source recovery rather than only embedding similarity.

Only after demonstrated equivalence/superiority:

```text
retire duplicate Pantheon semantic indexing components
```

### Phase 5 — migrate low-consequence content owners

Candidate order after doctrine approval and fixtures:

```text
Project/workspace metadata
Notes / Information-like working content
Documentation / Knowledge-like working content
agency tag vocabulary
simple explicit relations
```

Each migration must avoid indefinite dual-write synchronization.

Preferred transition pattern:

```text
old owner read-only compatibility
→ new source owner active
→ consumer migration
→ tests
→ old persistence retirement
```

### Phase 6 — governed records

Only after the write/gate/receipt model is proven, evaluate file-native representation for:

```text
Decisions
Claims
Qualifications
other governed records
```

The content may be file-native while consequential transition admission remains controlled separately.

### Phase 7 — reduce `pantheon-mvp`

Remove business persistence and duplicate retrieval only after their consumers and invariants have migrated.

Candidate end-state modules are responsibilities such as:

```text
policy enforcement
workspace adapter
execution/admission safety
auth adapters
exact-source/storage adapters
Cockpit projections
```

Do not rename or split the repository merely to match the target diagram. Rename/extract only if the final code boundary demonstrates a real independent lifecycle.

### Phase 8 — residual storage review

After business-table removal is complete, inventory what PostgreSQL still does.

Only then decide:

```text
keep PostgreSQL
or
replace the small control store with a simpler transactional technology
```

No database migration should be driven by aesthetic preference.

## 12. Procedure for migrating one responsibility

Every responsibility should use the same checklist.

### A. Observe

- current doctrine owner;
- executable owner;
- tables/files/modules;
- APIs;
- Cockpit/Hermes consumers;
- schemas/registries;
- tests and known real deployment usage.

### B. Decompose

Separate:

```text
content
identity
validation
professional authority
transactionality
retrieval
projection
```

### C. Select the simplest owner

Use the following default test:

```text
human-readable durable professional content
→ file when sufficient

shared deterministic rule
→ Next schema/policy/registry contract

semantic retrieval/association
→ Hindsight

conversation continuity
→ Mnemosyne

reasoning/action
→ Hermes

atomic/replay-sensitive control state
→ transactional control store

presentation
→ Cockpit
```

### D. Prove invariants before cutover

Transform important SQL checks/transactions into whichever combination of:

```text
schema
policy
workspace validation
transactional receipt
test
```

actually preserves the requirement.

### E. Migrate consumers

Do not keep two permanent read/write owners.

### F. Retire old implementation

Delete the table/module/path only after:

```text
new owner active
+ all consumers migrated
+ old invariant replaced
+ acceptance tests green
+ rollback understood
```

## 13. Non-negotiable boundaries

The convergence must preserve:

```text
retrieved != truth
memory != Evidence
runtime success != authorization
projection != persistence
folder/path != governed identity
```

Add for the file-native target:

```text
editable file != authorized transition
Hindsight relation != governed relation
tag != relation
tag/status != professional validation
sync success != Evidence
file present != Source/Document admitted unless the applicable owner contract says so
```

## 14. Complexity budget

Future-proofing here means replaceability and explicit contracts, not more services.

Do not create by default:

```text
new microservice
new business database
new relation graph
new memory layer
new workflow engine
new scheduler/queue
new rules compiler
new Card authority
```

Before adding an abstraction, demonstrate that the responsibility cannot be represented by an existing owner plus a schema, adapter or test.

## 15. Success criteria

The convergence is successful when all of the following are true:

1. Humans can understand and edit ordinary professional/work content directly from files without requiring a database UI.
2. Stable governed identity does not depend on folder paths.
3. Hindsight can be rebuilt without losing professional state.
4. Hindsight can be replaced without changing Pantheon authority.
5. Hermes can be replaced without migrating professional records.
6. Cockpit can be rebuilt from declared sources plus governed control/read models.
7. No business concept has two concurrent authoritative persistence paths.
8. Consequential transitions remain provably gated even when their content is stored in files.
9. PostgreSQL remains only where its transactional properties are demonstrated as useful.
10. Existing useful MVP acceptance tests are preserved or replaced by equivalent tests against the new owner boundaries.
11. The everyday model remains understandable as:

```text
Files = content
Pantheon = rules
Hermes = action
Hindsight = retrieval
Cockpit = view
```

## 16. Explicitly out of scope for this PR

This documentation tranche does not:

- modify `AGENCY_DATA_SYSTEM_OF_RECORD.md`;
- modify `OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md`;
- deprecate Category;
- move the Tag Registry;
- rename vaults or banks;
- change Hindsight configuration;
- change Hermes memory configuration;
- modify PostgreSQL schemas;
- modify `pantheon-mvp`;
- authorize file-native writes;
- implement a Workspace write adapter;
- change Decision/Evidence/Claim authority;
- remove pgvector;
- change Cockpit roots;
- rename `pantheon-mvp`;
- approve a PostgreSQL-to-SQLite migration.

## 17. Next action after this roadmap

The next tranche should be **doctrine convergence**, not production migration.

Recommended first output:

```text
current rule
→ target rule
→ invariant retained
→ affected schemas/tests/consumers
→ migration dependency
```

for at least:

```text
AGENCY_DATA_SYSTEM_OF_RECORD.md
OBSIDIAN_HINDSIGHT_WORKSPACE_MODEL.md
Category/Tag classification doctrine
Registry operational ownership
```

Only after those changes are reviewed and merged should implementation begin to move professional owners away from the current PostgreSQL model.

## 18. Closure posture

This roadmap closes the architecture-definition question only at the **candidate target** level.

It deliberately leaves open:

- exact vault topology;
- exact file schemas/frontmatter;
- exact protection vocabulary;
- which current Category requirements survive the Tag comparison;
- which governed records should actually become file-native;
- final residual PostgreSQL scope;
- final repository naming.

Those choices must be resolved from repository evidence and bounded experiments rather than frozen here in advance.
