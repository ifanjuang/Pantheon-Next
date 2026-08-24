# ai-memory vs Mnemosyne runtime-memory review

Status: external reference review — comparison only; no binding activation, dependency adoption, installation or authority change.

Date: 2026-08-24

Repository baseline reviewed: `ifanjuang/Pantheon-Next@30e794dd8d70c7d99e219d1602d4716fcfb001ac`.

External repositories reviewed:

```text
akitaonrails/ai-memory
mnemosyne-oss/mnemosyne
MrLuciano/ai-memory-hermes-plugin
```

## Objective

Compare `akitaonrails/ai-memory` with Mnemosyne for the responsibility already covered by Pantheon's `external_runtime_memory` Capability Slot.

The purpose is not to add a third memory system. The useful question is narrower:

```text
Could ai-memory eventually replace Mnemosyne for Hermes-side runtime memory
when cross-session and cross-agent workstream continuity matters?
```

This review does not reconsider Hindsight's separate workspace/document retrieval responsibility.

## Existing Pantheon boundary

Current doctrine already separates the relevant responsibilities:

```text
Mnemosyne
= observed fluid Hermes runtime / conversational memory

Hindsight
= derived workspace/document retrieval from intentional sources

Pantheon
= governance, provenance, authorization, Evidence and Registre Probatoire
```

The `external_runtime_memory` Capability Slot remains `unbound` for Pantheon and external memory remains forbidden in `pantheon-governed` runtime mode.

The currently documented `assistant-personal` sandbox order remains unchanged:

```text
Hindsight -> Mnemosyne -> Mem0
```

This review does not reorder that list because ai-memory has not yet been qualified on the target Hermes/NAS topology.

## Observed Mnemosyne state

The current upstream Mnemosyne repository was active on 2026-08-24 at commit:

```text
mnemosyne-oss/mnemosyne
main: 8e6c010bc823b7833061f0ee53c2a73a9dd6dd24
```

Its current architecture is a local-first semantic memory system centered on:

```text
Working Memory
-> Episodic Memory
-> SQLite
   |- FTS5
   |- vector retrieval
   `- temporal TripleStore
```

The project exposes direct SDK, MCP and a Hermes integration. Its documented default hybrid scoring combines vector similarity, FTS5 rank and importance. It also supports temporal weighting, expiry, banks/scopes, consolidation and bidirectional sync with optional client-side encryption.

Pantheon's own dated runtime qualification observed this concrete path:

```text
Hermes
-> memory.provider: mnemosyne
-> persistent Mnemosyne storage
-> fresh Hermes session
-> explicit recall
```

Observed package identities in that qualification were:

```text
mnemosyne-memory = 3.15.1
mnemosyne-hermes = 0.5.0
```

That result demonstrates functional cross-session Hermes recall for the tested deployment only.

## Observed ai-memory state

The current ai-memory repository was active on 2026-08-24 and released:

```text
akitaonrails/ai-memory
v1.32.0
release commit: c304ff6ecba54b05c488345e2c4b0bba81cb9574
```

Its architecture is materially different from Mnemosyne.

ai-memory treats a Git-versioned Markdown wiki as the canonical artifact of its own external memory state and uses SQLite as a derived index for search, sessions, observations, handoffs, audit and optional embeddings.

Its observed retrieval path combines:

```text
FTS5
+ entity matching
+ link-neighbor retrieval
+ reciprocal-rank fusion
+ optional vector retrieval
+ bounded authority-aware ranking signals
```

Its primary design center is agent work continuity rather than only semantic fact recall. It captures lifecycle observations, synthesizes session pages, creates handoffs and supports cross-harness workstreams across several coding-agent CLIs.

Relevant ai-memory semantics include:

```text
session history
failed approaches
decisions
procedures
gotchas
open questions
handoff context
cross-agent continuation
```

The upstream architecture explicitly states that retrieved historical memory remains untrusted and that current checkout, builds, tests and observed runtime behavior remain operational truth for code work.

This is structurally compatible with Pantheon's boundary:

```text
retrieved memory != truth
runtime history != Evidence
successful continuation != authorization
```

## Hermes integration finding

ai-memory's main repository currently classifies Hermes support as `Community`, not first-party.

The reviewed community bridge is:

```text
MrLuciano/ai-memory-hermes-plugin
```

Its stated intent is appropriate: implement Hermes `MemoryProvider`, automatic prefetch, turn capture, session finalization, wiki search/write tools and handoff support.

However, the plugin's current `main` is not a safe basis for adoption against current ai-memory.

Observed incompatibility on its published `main` includes an obsolete search call:

```text
POST /api/v1/search
```

An open pull request, `MrLuciano/ai-memory-hermes-plugin#2`, corrects material lifecycle/API issues including:

```text
GET /admin/search
correct user-prompt hook shape
preserved configured project scope
handoff response handling
session-switch handling
cross-agent recall behavior
visible hook failure logging
```

That PR reports validation with:

```text
Hermes Agent 0.20.5
ai-memory 1.28.1
Python 3.11
Windows 11
```

At review time the PR remained open and unmerged, while ai-memory itself had advanced to v1.32.0.

Therefore:

```text
Hermes bridge exists != current compatibility qualified
community plugin available != production-ready binding
```

## Capture/privacy boundary

ai-memory v1.32.0 includes an opt-in capture allowlist mode so unmarked repositories can emit no lifecycle events.

A critical implementation boundary remains: the strong client-side allowlist gate is enforced by the native `ai-memory hook` path. Script/direct-HTTP hook paths do not automatically inherit that guarantee.

The reviewed Hermes community plugin sends hook requests through its HTTP client.

For Pantheon this means the following must be proven rather than inferred:

```text
configured allowlist != Hermes capture exclusion proven
server accepts hook != confidentiality boundary satisfied
```

No professional/client-data qualification should rely on the allowlist property until the exact Hermes path is demonstrated to enforce capture before spool/network transmission.

## Deletion and retention finding

ai-memory has active work toward strong per-session deletion in upstream PR `akitaonrails/ai-memory#399`.

The proposed design addresses session tombstones, derived pages, FTS5 residual bytes, Git history, late spool replay, restore and backup interactions. The work is technically relevant to Pantheon's data-governance concerns.

At review time the PR remained draft/unmerged and explicitly retained a production-scale validation gap.

Therefore strong per-session erasure must not be treated as a capability of the released baseline until a merged release and target-topology verification establish it.

## Functional comparison

### Mnemosyne is stronger today for fluid conversational memory

Mnemosyne's design directly models:

```text
working memory
semantic/episodic recall
importance
recency
temporal facts
persona/preferences
memory consolidation
```

That matches questions such as:

```text
What preference did the user state previously?
What fact or relation was remembered across sessions?
What prior conversational context is relevant now?
```

For the currently deployed Hermes memory role, this is a close fit and has already been observed working.

### ai-memory is stronger conceptually for workstream continuity

ai-memory directly models the continuity of agent work:

```text
what was attempted
what failed
what was decided
why it was decided
what remains open
which project/workstream it belongs to
what the next agent needs to continue
```

That is closer to the emerging Pantheon use case where Hermes, Codex, Claude Code or another execution surface may need to resume the same bounded project work without reconstructing prior sessions manually.

### Multi-agent continuity

Mnemosyne can expose the same memory store through multiple clients, but its central abstraction remains memory recall.

ai-memory additionally models explicit cross-harness continuation and handoff.

This gives ai-memory the stronger architectural fit when the requirement is:

```text
agent A works
-> agent B resumes the same workstream
-> agent C can recover decisions, failures and open work
```

### Inspectability and versioning

Mnemosyne's authoritative runtime store is SQLite-centric.

ai-memory's external memory artifact is Markdown + Git with a derived SQLite index.

For human inspection this gives ai-memory useful properties:

```text
readable pages
grep-able content
git diff/history
manual inspection
Obsidian-readable Markdown
replaceable derived index
```

This is a design advantage for auditability, but it does not turn ai-memory pages into Pantheon Evidence or governed truth.

### NAS/runtime simplicity

Mnemosyne remains operationally simpler for the current Hermes deployment:

```text
Hermes provider
-> local Python memory library
-> SQLite
```

The reviewed ai-memory path adds a separate server plus plugin/hook/watcher/wiki lifecycle:

```text
Hermes bridge
-> ai-memory HTTP server
-> lifecycle capture
-> SQLite index
-> Git/Markdown wiki
```

The additional complexity is justified only if workstream continuity produces a demonstrated gain.

### Sync

Mnemosyne currently exposes dedicated delta sync with optional client-side encryption.

ai-memory primarily assumes a central service plus Git/backup/rsync-style durability for its wiki/data directory.

For multi-instance memory replication, Mnemosyne currently has the more explicit purpose-built path.

## Relationship to Hindsight

ai-memory is not a Hindsight replacement in this review.

The desired separation remains:

```text
Hindsight
= retrieve intentional workspace/document sources

runtime-memory candidate
= preserve conversational or workstream continuity

Pantheon
= govern status, provenance, authorization and Evidence
```

If ai-memory is qualified later, its wiki must not automatically become another copy of the Obsidian/Hindsight source corpus.

The main duplication risk is:

```text
agent learns a project statement
-> ai-memory persists it as operational knowledge
-> the same statement is also intentionally authored in Obsidian
-> Hindsight indexes the Obsidian source
```

The two records may coexist only if their roles remain explicit. ai-memory history would remain runtime-derived memory; the Obsidian/Hindsight path would remain intentional workspace material. Neither becomes Evidence automatically.

## Current classification

The observed comparison supports this classification:

```text
ai-memory
capability_slot: external_runtime_memory
status: to_verify
role_under_test: possible Mnemosyne successor for cross-session/cross-agent workstream continuity
target_to_replace_if_qualified: Mnemosyne
not_a_target: Hindsight
activation: none
Pantheon authority: none
```

Mnemosyne remains the current observed Hermes fluid-memory path.

No concurrent steady-state architecture with all three memory systems is recommended:

```text
Mnemosyne + ai-memory + Hindsight
```

would introduce overlapping runtime-memory paths without a demonstrated need.

The preferred evaluation principle is replacement by convergence:

```text
keep Mnemosyne + Hindsight now
qualify ai-memory against Mnemosyne
replace Mnemosyne only if the gain is demonstrated
keep Hindsight for its distinct retrieval responsibility
```

## Qualification gate

A meaningful ai-memory qualification should compare both candidates on the same scenarios rather than merely proving that ai-memory starts.

### Q1 — current Hermes compatibility

Verify the exact current target matrix, including the current Hermes release and a current ai-memory release.

The Hermes adapter must use a reviewed/merged compatible implementation or an explicitly pinned patch. Do not infer compatibility from the plugin README.

### Q2 — Hermes cross-session continuity

Perform the same controlled remember/resume test already used for Mnemosyne:

```text
session A records bounded context
-> session closes
-> fresh Hermes session
-> relevant context is recovered
```

Measure relevance, false recall, stale recall and context size.

### Q3 — cross-agent workstream handoff

Demonstrate the differentiating capability:

```text
Codex or Claude Code
-> recorded decision + failed attempt + open task
-> Hermes resumes
-> Hermes can identify all three without invented state
```

Then reverse the direction where supported.

### Q4 — scope isolation

Demonstrate strict isolation for agency/project boundaries and explicitly test a same-named concept in two projects.

Cross-project global recall must not be enabled merely to make handoff tests pass.

### Q5 — capture confidentiality

Demonstrate that an unapproved repository produces no captured prompt/tool content before spool or network transmission.

This must be tested on the exact Hermes bridge path, not inferred from native ai-memory hook behavior.

### Q6 — NAS outage and restart

Test:

```text
server unavailable
Hermes continues safely
captured data behavior is bounded
server restart
replay converges without duplicate semantic effects
```

Record spool retention, retry and failure visibility.

### Q7 — deletion/export/restore

Verify what can be deleted by exact identity, what remains in Git history/indexes/backups, and whether restore can resurrect removed content.

Do not claim strong deletion until the released implementation proves it on the target topology.

### Q8 — Hindsight non-duplication

Keep the ai-memory wiki outside the current LiveSync/Hindsight source path for the first qualification.

Do not introduce simultaneous writers/watchers over the same Obsidian Markdown tree.

### Q9 — governance invariants

Every scenario must preserve:

```text
memory recalled != truth
memory page != Evidence
handoff delivered != authorization
runtime write success != ingestion authority
project folder != governed identity
```

## Replacement decision rule

Replacing Mnemosyne is justified only if ai-memory demonstrates a material operational gain in the actual Pantheon workflow and does not create a worse confidentiality, scope, deletion, recovery or maintenance boundary.

A reasonable pass condition is:

```text
cross-agent/workstream continuity gain: demonstrated
Hermes current compatibility: demonstrated
scope isolation: no regression
confidentiality boundary: no regression
outage/recovery: acceptable
memory quality: acceptable vs Mnemosyne baseline
Hindsight role: remains distinct
Pantheon authority: unchanged
steady-state active runtime-memory providers: one
```

If these conditions are not met, Mnemosyne remains the simpler runtime-memory choice.

## Non-claims

This review does not establish:

```text
ai-memory installed
ai-memory approved
ai-memory production-ready on the target NAS
Hermes community plugin compatible with v1.32.0
capture allowlist enforced through Hermes
strong per-session deletion available in the released baseline
ai-memory superior on semantic recall
ai-memory replacement of Hindsight
Mnemosyne deprecated
CapabilityBinding activation
Evidence admission
```

## Re-evaluation triggers

Re-run this comparison when one of the following materially changes:

- the ai-memory Hermes integration becomes first-party or the compatibility PR is merged and released;
- ai-memory strong session deletion is merged and released;
- the target Hermes memory-provider contract changes;
- Mnemosyne's runtime behavior or deployment requirements materially change;
- Pantheon demonstrates a real need for cross-agent workstream continuation that Mnemosyne cannot satisfy cleanly;
- Hindsight begins to overlap the same runtime-memory responsibility.

## Conclusion

Current recommendation:

```text
KEEP      Mnemosyne as the observed Hermes fluid-memory path
KEEP      Hindsight as the distinct workspace/document retrieval path
QUALIFY   ai-memory as a possible Mnemosyne successor
DO NOT    run Mnemosyne + ai-memory as concurrent steady-state fluid memories
DO NOT    change Pantheon authority or Evidence semantics
```

The subject remains open pending a bounded target-topology qualification.