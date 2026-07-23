# Pantheon Platform — Implementation Roadmap

Status: validation-only roadmap — documented non-implemented.
Boundary profile: candidate_support_note.

Date: 2026-07-23

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides consequential effects.
```

This roadmap turns the merged governance doctrine into a working platform **one
governed vertical slice at a time**. It records a plan; it installs, activates,
adopts and approves nothing. It does not make Pantheon a runtime.

## Why this document exists

The doctrine is now rich and internally coherent, but the running surface has
not moved with it: what executes today is `mcp-server/` (read-only policy, tested)
and the `pantheon-mvp` vertical loop (tested, **candidate / not adopted**, Gate 8
open). Recent work added ~10 000 lines of cockpit and platform **specification**
and zero lines of executable cockpit. The next useful step is not more
specification — it is a thin end-to-end slice wired to the governance chokepoint.

Governing rule for this roadmap:

```text
No new cockpit/platform specification is promoted beyond candidate until an
executable slice has exercised it. Spec follows implementation from here.
```

## Where code lives (placement, unchanged)

```text
Pantheon Next        governance, schemas, validators, policy/preflight (mcp-server/)
pantheon-mvp         executable cockpit, adapters, scenarios, OpenWebUI code
private deploy layer  compose/secrets/reverse-proxy for one real environment
Hermes host          the execution runtime (external), the Policy Enforcement Point
```

## The chokepoint (the invariant every slice must honor)

Pantheon is the Policy Decision Point; Hermes is the Policy Enforcement Point
(`HERMES_INTEGRATION.md`). Before any consequential effect, the runtime calls the
policy preflight and obeys the verdict; it fails closed when the PDP is
unavailable. Hermes 0.19 turns an in-runtime "smart approval" LLM review on by
default — the PEP must **disable it for consequential effects** so it never
substitutes for the human gate (`HERMES_INTEGRATION.md`, Hermes 0.19 review).

## Phases

### Phase A — Coherence debt from the Codex review (prerequisite, cheap)

Fix the review findings on the freshly merged doctrine so implementation builds
on consistent specs. Covered by this change set:

```text
Decision is a distinct linked object, not a Work Issue projection   (IA §3)
a pre-response card is a Decision Request / Gate, not a Decision     (IA §4.6)
Kanban columns map onto the owner Work Issue vocabulary              (IA §5.5)
distribution record keeps an exact-output ref when not archived      (production §9)
engagements reference identity records, no duplicated master fields  (project nav §10.4)
PROJECT_NAVIGATION_UX gets an explicit authority row                 (architecture index)
runbook /health probe is optional / version-guarded                  (baseline runbook §13)
```

### Phase B — Reference platform + policy PDP (deployment layer)

Stand up the reference stack of `REFERENCE_PLATFORM_COMPONENTS.md` on `ai-net`
(pgvector, Ollama, **Hermes 0.19**, OpenWebUI, SearXNG, Browserless) in a private
deployment layer, and deploy the policy PDP (`compose.policy-api.yaml`) with its
consultation key. Deliverable: a private deploy repo/layer with pinned revisions
and external secrets. Verify install/exposure posture with the MCP `verify_*` /
doctor checks. Nothing here is adopted; it is one operator environment.

### Phase C — First governed vertical slice, end to end

Extend the existing `mvp_vertical` "document intake → Knowledge" path to the
merged lifecycle doctrine, wired to the chokepoint:

```text
immutable source capture -> versioned projections -> Knowledge publication/index
before the consequential effect (publish/index): call the policy preflight
enforce: fail-closed, block external/canonical effects until allowed
neutralize Hermes smart-approvals so consequential effects still require the human decision
expose via the OpenWebUI Document Cards tool + the cockpit
respect Phase A constraints (owner Kanban states, Decision as its own object)
```

Deliverable: one dossier processed end to end in a real environment, every
consequential step gated, producing candidates and Evidence Pack candidates —
never a self-approval. Still a candidate; adoption stays a separate human gate.

### Phase D — Capability-management slice (Outils)

Implement `COCKPIT_CAPABILITY_MANAGEMENT.md` for **one** capability type (a
bounded MCP binding is the smallest): inventory → candidate → preflight → human
approval → native operation by Hermes → technical receipt + fresh observation.
The cockpit action never executes code; it requests one bounded operation.

### Phase E — Gate-validation slice (the assurance chainlink)

In `mcp-server/`, validate a caller-provided `human_decision_ref` (digest, scope,
approval level, expiry, object identity). Today the preflight reports
`gate_signal_validation_performed: false`; this slice makes the verdict
**opposable** rather than trusting unverified references. Protected path → review.

### Later (each a separate human-gated decision)

```text
identity / scope / permission service (absent today)
governed memory backend / persistent Registre Probatoire
Adoption Gate 8 decision, once a slice runs live and healthy
```

## Sequencing and dependencies

```text
A (coherence)  -> unblocks building on consistent doctrine
B (platform)   -> unblocks C and D (needs a real PDP + runtime)
C (doc slice)  -> first proof the cage holds end to end
E (gate-valid) -> raises assurance of C/D; can proceed in parallel in mcp-server/
D (capability) -> after C proves the pattern
```

## Non-goals / boundaries

This roadmap creates no runtime, scheduler, queue, provider router, plugin
manager, memory engine or approval engine inside Pantheon, and authorizes no
production or real-dossier use. Every slice remains a candidate until reviewed;
the human approves adoption, activation and consequential action.

```text
plan != implementation
slice implemented != adopted
installed != approved
runtime success != evidence
```
