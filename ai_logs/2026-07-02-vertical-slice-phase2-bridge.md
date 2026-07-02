# AI log — vertical slice phase-2 bridge (candidate templates)

Date: 2026-07-02.

Actor: Claude Code.

## Intent

B-3 phase 2 asks for the real OpenWebUI → Hermes run. That runtime lives **outside**
this repo (Pantheon governs, does not execute), so the live run cannot happen here.
What Pantheon can own — and what this change delivers — is the in-repo **bridge**:
candidate, non-executable templates that bind the phase-1 governed dossier to a future
Hermes run, so the external runtime need not re-invent the framing.

## Change

- `templates/hermes/skills/quote_variation_review_skill_candidate.template.yaml` and
  `.../external_commitment_guard_skill_candidate.template.yaml` — the two slice
  capabilities as `candidate_template_only` Hermes skill candidates (allowed/forbidden
  inputs and outputs; opens the gate, never sends).
- `templates/hermes/run_manifests/devis_reprise_run_manifest.template.yaml` — binds the
  governed dossier (task contract, forged manifest, gate 1) to the two skill candidates,
  the required envelope, the returned evidence shape verified by mcp-server, and the
  OpenWebUI action; forbids scheduling/queueing/routing/send.
- `docs/examples/vertical_devis_reprise/RUNBOOK.md` gains a "Phase-2 bridge" section
  mapping each external step to its candidate template.

## Boundary

Candidate templates only; they install and execute nothing. No runtime, scheduler,
queue, provider routing, external send or memory promotion is added. The live run
(a real OpenWebUI calling a real Hermes) remains phase 2 proper, outside this repo.
`forged != authorized`.
