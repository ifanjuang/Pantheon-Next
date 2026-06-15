# AI Log — Harden WORK_CONTEXT_COMPOSER_SPEC boundary and governance binding

Date: 2026-06-15

## Trigger

User asked for a sincere review of the latest `WORK_CONTEXT_COMPOSER_SPEC.md`
(authored via ChatGPT), then approved patching the document along the lines of
that review. The doc is a candidate orientation; the patch closes doctrinal
ambiguities, it does not implement anything.

## Doctrine read first

- `docs/governance/WORK_CONTEXT_COMPOSER_SPEC.md` (the doc being patched).
- `CLAUDE.md` non-negotiable boundaries (no Agent Runtime, no LLM Provider
  Router, no scheduler/queue/session state inside the governance core).
- `docs/governance/USER_DECISION_GATE.md` and
  `docs/governance/PANTHEON_CONTROL_BOUNDARY.md` for canonical naming of the
  User Decision Gate and the consequential chokepoint, to bind the spec to
  existing governance rather than a parallel vocabulary.

## Review findings addressed

1. **Who composes** — the "Allowed posture" list (identify project, classify
   request, score risk, propose mode) could read as governance-core work, which
   would recreate an agent runtime / LLM router. Added a `Composition
   responsibility` section: detection/classification/composition is a Hermes
   candidate; the governance core only validates, displays, records the required
   human decision and returns the policy decision as data.
2. **Lock as state** — `accepted_context_lock` risked implying live session
   enforcement in the core. Added that the lock is recorded data; enforcement
   belongs to the consuming runtime (Hermes/OpenWebUI).
3. **No tie to existing governance** — added a `Chokepoint and gate binding`
   section mapping `human_decision_required` to the User Decision Gate, the
   retrieval handoff to the consequential chokepoint, and reaffirming that a
   Registre Probatoire change stays a governed candidate, never a direct write.
4. **Pseudo-shape vs schema** — flagged that `work_context_proposal` stays
   ungoverned until promoted to a JSON Schema candidate in the governance core;
   added to "To verify".
5. **missing_evidence reliability** — added a `confidence` field and a caveat
   that naming absent evidence is domain inference, must carry confidence, and
   an empty list is not proof nothing is missing.
6. **Google scope creep** — marked the Google projections as adjacent scope to
   be extracted into a dedicated external-projections document; added to
   "To verify".

## Boundary

Documentation-only change to a single candidate spec. No code, schema, runtime,
connector or UI. The doc remains "candidate — to verify".

## Verification

- Manual re-read of the patched doc for internal consistency and boundary
  alignment.
- No schema/code touched, so no test impact; existing checks unaffected.
