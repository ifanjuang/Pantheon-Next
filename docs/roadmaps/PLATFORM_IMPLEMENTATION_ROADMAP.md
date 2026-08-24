# Pantheon Platform — Implementation Roadmap

Status: validation-only roadmap — documented non-implemented.
Boundary profile: candidate_support_note.

Date: 2026-07-23
Placement reconciled: 2026-08-24

```text
OpenWebUI exposes.
Hermes Agent executes.
Pantheon Next governs.
The human decides consequential effects.
```

This roadmap turns the merged governance doctrine into a working platform **one
governed vertical slice at a time**. It records a plan; it installs, activates,
adopts and approves nothing. It does not make Pantheon a runtime.

The phase ledger below preserves former `pantheon-mvp` PR numbers as historical provenance. Current executable candidate source is co-located under `implementation/` in Pantheon Next; the former repository is not a second active implementation path.

## Why this document exists

The doctrine is rich and internally coherent, while the executable candidate loop now lives under `implementation/` beside the governance source with explicit responsibility boundaries. `mcp-server/` remains the bounded read-only policy surface; `implementation/` contains the tested candidate vertical loop. Gate 8 remains open.

Governing rule for this roadmap:

```text
No new cockpit/platform specification is promoted beyond candidate until an
executable slice has exercised it. Spec follows implementation from here.
```

## Where code lives

```text
Pantheon-Next/
  governance + schemas + validators + policy/preflight  root surfaces / mcp-server/
  executable candidate cockpit/adapters/scenarios       implementation/
private deploy layer                                     compose/secrets/reverse-proxy for one real environment
Hermes host                                              external execution runtime / Policy Enforcement Point participant
```

```text
same repository != same authority
implementation path != governed identity
historical PR provenance != current source checkout
```

## The chokepoint (the invariant every slice must honor)

Pantheon is the Policy Decision Point; Hermes participates as the external Policy Enforcement Point runtime (`HERMES_INTEGRATION.md`). Before any consequential effect, the runtime calls the policy preflight and obeys the verdict; it fails closed when the PDP is unavailable. Runtime/model approval features must not substitute for the human gate.

## Phases

## Implementation status (historical ledger from 2026-07-23)

Four phases were implemented and tested at this checkpoint; only deployment remained.

```text
A  coherence debt        implemented   Pantheon Next #464 (+ former mvp #52)
E  gate-validation (PDP) implemented   Pantheon Next #465 — mcp-server validate_decision
C  chokepoint seam (PEP) implemented   former pantheon-mvp #53 — policy_gate.enforce_consequential
   real HTTP client       implemented   former pantheon-mvp #54 — policy_gate.HttpPolicyClient
D  capability lifecycle  implemented   former pantheon-mvp #54 — capability_manager
B  deployment            not started    needs operator infra — see the runbook below
```

Those former PR identifiers remain provenance for the imported implementation history. Current corresponding source is under `implementation/`.

The software backbone can route a consequential effect through the PDP and fail closed. What remains for Phase B is standing up the infrastructure and injecting reviewed runtime configuration according to `docs/install/PLATFORM_PHASE_B_DEPLOYMENT_RUNBOOK.md`.

### Phase A — Coherence debt from the Codex review (prerequisite, cheap)

Fix the review findings on the freshly merged doctrine so implementation builds on consistent specs. Covered by this change set:

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

Operator steps are in `docs/install/PLATFORM_PHASE_B_DEPLOYMENT_RUNBOOK.md`.

Use one reviewed/pinned Pantheon Next revision. Deploy the policy PDP from `compose.policy-api.yaml`, then deploy the co-located candidate runtime core from `implementation/compose.phase-b.yaml`. When `document_source_management -> paperless_ngx` is explicitly selected, add `implementation/compose.paperless.yaml` as a second Compose file. The private deployment layer owns environment-specific secrets, storage and reverse-proxy configuration.

```text
core compose present != deployed
optional overlay selected != activated
successful deployment != adoption
```

### Phase C — First governed vertical slice, end to end

Extend the existing `implementation/mvp_vertical` "document intake → Knowledge" path to the merged lifecycle doctrine, wired to the chokepoint:

```text
immutable source capture -> versioned projections -> Knowledge publication/index
before the consequential effect (publish/index): call the policy preflight
enforce: fail-closed, block external/canonical effects until allowed
neutralize runtime smart-approval paths so consequential effects still require the human decision
expose via the OpenWebUI Document Cards tool + the cockpit
respect Phase A constraints (owner Kanban states, Decision as its own object)
```

Deliverable: one dossier processed end to end in a real environment, every consequential step gated, producing candidates and Evidence Pack candidates — never a self-approval. Still a candidate; adoption stays a separate human gate.

### Phase D — Capability-management slice (Outils)

Implement `COCKPIT_CAPABILITY_MANAGEMENT.md` for **one** capability type (a bounded MCP binding is the smallest): inventory → candidate → preflight → human approval → native operation by Hermes → technical receipt + fresh observation. The cockpit action never executes code; it requests one bounded operation.

### Phase E — Gate-validation slice (the assurance chainlink)

In `mcp-server/`, validate a caller-provided `human_decision_ref` (digest, scope, approval level, expiry, object identity). The preflight must not trust unverified references. Protected path → review.

### Later (each a separate human-gated decision)

```text
identity / scope / permission service
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

This roadmap creates no runtime, scheduler, queue, provider router, plugin manager, memory engine or approval engine inside Pantheon governance, and authorizes no production or real-dossier use. Every slice remains a candidate until reviewed; the human approves adoption, activation and consequential action.

```text
plan != implementation
slice implemented != adopted
installed != approved
runtime success != Evidence
```
