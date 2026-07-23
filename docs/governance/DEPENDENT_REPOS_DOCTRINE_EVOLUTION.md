# Dependent Repositories — Doctrine Evolution (proposal)

Status: candidate support doctrine — proposal for review. It changes no rule until reviewed through the chokepoint; `CLAUDE.md` remains authoritative.

Boundary: the standard non-implementation boundary applies — see `BOUNDARY_STANDARD.md`. This document specifically proposes only doctrine text and one read-only verification; it implements no runtime, no external action, and no schema.

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
```

## Purpose

The doctrine describes the repository's internal zones (governance core, `mcp-server/`, exposure surface) and their one-way dependency. It is silent, however, on the external dependent that now consumes the governance core in practice — `ifanjuang/pantheon-mvp` — and on how that consumption stays honest over time.

A deep analysis of the `Pantheon-Next` ↔ `pantheon-mvp` coupling (tracked in issue #448, first corrections landed in `pantheon-mvp#48`) surfaced one silent drift and four places where the doctrine has fallen behind the repository's actual shape. This document proposes the doctrine text to close that gap. It is a proposal: nothing here is canonical until reviewed.

## Findings, in one paragraph

The coupling is architecturally sound: it is a **one-way vendored snapshot**. MVP vendors a small, explicit subset of governance artifacts (three schemas plus a derived decision vocabulary), pinned to a `Pantheon-Next` commit via `UPSTREAM_COMMIT`, and never writes back. The core depends on nothing — correct. But a vendored copy had drifted onto a retired decision word (`approve_for_internal_draft`) with nothing watching that class of drift, and the doctrine names neither the consumption relationship nor the real exposure surface that now lives in MVP. The risk is not excess rigor; it is rigor running dry — a governance apparatus heavy relative to the execution surface it actually governs.

## Proposed doctrine additions

### 1. Name the external consumption relationship (vendoring)

Add to the doctrine: *an external candidate may vendor read-only governance artifacts — schemas, vocabularies, read-only checks — pinned to a commit, one-way, under drift surveillance.* The vendored copy is authoritative for the consumer at its pin; the upstream artifact is authoritative on divergence. The consumer never edits the vendored copy and pushes nothing back. This turns an existing practice into a named boundary so the next consumer inherits the same discipline.

### 2. Reconcile the exposure-surface map with reality

`CLAUDE.md` states the `dashboard/` module is "voluntarily absent" and that exposure exists only as the `docs/assets/pantheon-control/` prototype. The exposure surface that actually **runs today** is the MVP cockpit (`mvp_vertical/cockpit/`, `mobile_editor/`, the OpenWebUI cards) — external to this repository and candidate by status. Update the described topology to name that external cockpit as the current exposure reality, so "the UI exposes, `mcp-server/` verifies" rests on a component the doctrine actually acknowledges. See `COCKPIT_ARCHITECTURE.md`.

### 3. Make the boundary verifiable, not only declared

`BOUNDARY_STANDARD.md` states the standard non-implementation boundary once, as prose. Nothing verifies it. Because `mcp-server/` already runs read-only `verify_*` checks, the doctrine should govern itself with the same instrument: a **read-only boundary check** that fails CI when a forbidden runtime pattern appears in the governance core (a scheduler import, a queue, a message bus, an external-action call). Report-only first, gating once stable. A boundary nothing verifies is not a boundary; it is a wish. This proposes the *contract* for such a check; the check itself is a separate reviewed change.

### 4. Structure `ai_logs`, do not delete them

`ai_logs` is provenance; its value is being append-only and complete, so bulk deletion is the one act most opposed to the doctrine it embodies. `ai_logs/INDEX.md` already plans the quarterly archive (`ai_logs/<year>/Q<n>/`); this proposal refines the destination rather than inventing it:

- **Partition** by `ai_logs/<year>/Q<n>/` (already planned — this endorses it).
- **Classify** each log as *decisional* (changes governance, schema, or policy → retained indefinitely) or *operational* (routine → eligible for compaction). The current "every significant intervention adds an entry" rule treats both alike, which drowns the decisional signal in operational noise.
- **Compact**: past a retention horizon, operational logs fold into a signed monthly digest that preserves the decision trace while collapsing the noise. Raw logs remain in git history — never truly lost — but leave the working-tree tip.

Net effect: working-tree footprint reduced to the maximum the doctrine allows, provenance intact.

### 5. Elevate "consumed artifacts must be drift-monitored" to a first-class rule

The silent vendored drift was a governance hole: the source of truth had a consumer diverging unseen. It is now covered on the MVP side (a schema + vocabulary drift monitor, `pantheon-mvp#48`). Make the principle doctrinal: *any governance artifact consumed by an external candidate must be drift-monitored against its upstream, and divergence resolves in favor of upstream.*

## What this proposal does NOT change

The one-way purity of the governance core; the truth taxonomy (implemented / documented / partial / obsolete / to verify / not implemented); "candidate until reviewed." These are the strongest parts of the doctrine and stay as written.

## Transverse recommendation

The fastest way to improve this doctrine is not another governance document — it is to adopt **one** vertical slice of MVP under the real gate, end to end, so the doctrine is exercised rather than only described. A doctrine that never meets a runtime is coherent but not falsifiable.

## Review path

Per the work rules, this is the documentation proposal that precedes any change to canonical text. If accepted, the follow-ups are: (a) the `CLAUDE.md` and exposure-map edits for points 1–2, (b) a read-only boundary-check contract for point 3, (c) the `ai_logs` classification + compaction policy for point 4 (building on the planned quarterly archive), and (d) the drift-monitoring rule for point 5. Each is a separate reviewed change routed through the chokepoint and the User Decision Gate.

## Local distinctions

```text
vendored copy != upstream authority (upstream wins on divergence)
consumed artifact != unmonitored artifact
declared boundary != verified boundary
provenance compaction != provenance deletion
described doctrine != exercised doctrine
proposal != canonical text
```
