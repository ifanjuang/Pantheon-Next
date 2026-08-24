# 2026-08-24 — ai-memory vs Mnemosyne comparison

Status: dated external-runtime-memory qualification trace; no installation, activation or authority change.

Repository baseline reviewed: `30e794dd8d70c7d99e219d1602d4716fcfb001ac`.

Primary review:

```text
docs/governance/reference_reviews/AI_MEMORY_MNEMOSYNE_RUNTIME_MEMORY_REVIEW.md
```

## Objective

Record why `akitaonrails/ai-memory` is worth qualifying against Mnemosyne without adding a concurrent third memory path or changing Hindsight's distinct workspace/document retrieval role.

## Observed upstream state

```text
ai-memory
  release: v1.32.0
  release commit: c304ff6ecba54b05c488345e2c4b0bba81cb9574

Mnemosyne
  reviewed main: 8e6c010bc823b7833061f0ee53c2a73a9dd6dd24

ai-memory Hermes bridge
  repository: MrLuciano/ai-memory-hermes-plugin
  support level in ai-memory: Community
  current main still uses obsolete POST /api/v1/search
  compatibility PR #2: open/unmerged
```

The ai-memory compatibility PR reports validation against Hermes 0.20.5 and ai-memory 1.28.1, while ai-memory itself has since advanced to 1.32.0. This is evidence of a viable bridge direction, not current-target compatibility.

Upstream ai-memory PR #399 for strong per-session deletion was also reviewed. It remains draft/unmerged and retains a production-scale validation gap.

## Comparison result

The two systems optimize for different primary effects.

```text
Mnemosyne
= semantic/conversational memory
  working memory
  episodic memory
  importance/recency
  temporal graph
  vector + FTS retrieval
  dedicated sync

ai-memory
= agent-work continuity
  lifecycle observations
  sessions
  decisions
  failed approaches
  gotchas/procedures
  handoffs
  cross-harness workstreams
  Markdown/Git external memory artifact + derived SQLite index
```

Current interpretation:

```text
fluid conversational recall              -> Mnemosyne stronger/currently proven
cross-agent workstream continuity         -> ai-memory architecturally stronger
current Hermes integration                -> Mnemosyne stronger
human inspectability/versioned memory     -> ai-memory stronger
current NAS simplicity                    -> Mnemosyne stronger
purpose-built multi-instance sync         -> Mnemosyne stronger
```

## Pantheon classification

```text
ai-memory
capability_slot: external_runtime_memory
status: to_verify
comparison_target: Mnemosyne
possible_role: Mnemosyne successor for cross-session/cross-agent workstream continuity
not_a_target: Hindsight
activation: none
Pantheon authority: none
```

No new `workstream_memory` Capability Slot is introduced. Existing `external_runtime_memory` doctrine already covers semantic recall, checkpoint/resume and context assembly.

The existing sandbox order is intentionally not changed by this trace:

```text
Hindsight -> Mnemosyne -> Mem0
```

A candidate should not move the registry before target-topology evidence exists.

## Convergence rule

The rejected steady-state direction is:

```text
Mnemosyne + ai-memory + Hindsight
```

because it would add overlapping runtime-memory paths without a demonstrated need.

The preferred evaluation direction is:

```text
KEEP      Mnemosyne now
KEEP      Hindsight in its distinct retrieval role
QUALIFY   ai-memory against Mnemosyne
REPLACE   Mnemosyne only if the gain is demonstrated
```

## Required qualification

The reference review defines the bounded gate. The decisive checks are:

```text
current Hermes compatibility
Hermes cross-session continuity
Codex/Claude <-> Hermes workstream handoff
strict project isolation
capture exclusion before spool/network
NAS outage/restart/replay behavior
exact deletion/export/restore behavior
Hindsight non-duplication
Pantheon governance invariants
```

The first ai-memory test must keep its Markdown wiki outside the current LiveSync/Hindsight source path so Git/watcher behavior is not mixed with Obsidian/CouchDB synchronization before the runtime-memory candidate itself is qualified.

## Preserved invariants

```text
memory recalled != truth
memory page != Evidence
handoff delivered != authorization
runtime write success != ingestion authority
projection/index != canonical external memory artifact
external memory artifact != Pantheon persistence
```

## Final status

```text
Mnemosyne current Hermes role -> retained
ai-memory candidate posture   -> to_verify
Hindsight role                -> unchanged
external_runtime_memory       -> unbound for Pantheon
pantheon-governed memory      -> forbidden/off
subject                       -> open pending sandbox qualification
```
