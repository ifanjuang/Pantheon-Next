# AI log — governed execution handoff slice

Date: 2026-06-12.

## Intent

The maintainer asked to use the Spice repository only where relevant to Pantheon Next, without creating a reference review. The useful pattern is the boundary contract between a governed decision and external execution, not Spice as a runtime or decision brain.

This slice strengthens Pantheon's existing placement doctrine by documenting a governed execution handoff between the exposure surface / bridge and the execution runtime.

## Sources read

Active repository doctrine was read before editing:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`
- `docs/governance/TASK_CONTRACTS.md`
- `docs/governance/CONTEXT_PACKS.md`
- `docs/governance/EVIDENCE_PACK.md`
- `docs/examples/README.md`
- `docs/examples/architecture_devis_reprise/README.md`

Related open PRs and discussions were checked:

- PR #101 — Pantheon Control boundary; no comments found.
- PR #102 — `mcp-server/` first slice; no comments found.
- PR #87 — E6 / schema-spine work order; relevant because schemas are protected and not touched here.
- PR #35 — proof-register schema discussion; relevant warnings around source evidence and external-effect gating.

## External inspiration distilled

Spice / SDEP was treated as an external inspiration only. Useful ideas were translated into Pantheon vocabulary:

- execution intent / result boundary -> governed execution handoff;
- status separation -> handoff delivery, runtime task and governance result status;
- idempotency -> mandatory key for non-read-only effects;
- agent describe / capability availability -> capability gap if availability does not equal authorization;
- outcome -> Outcome Observation Candidate.

Rejected from adoption:

- Spice as runtime;
- brain vocabulary;
- `.spice`-style local runtime state;
- autonomous decision loops;
- direct execution or memory promotion inside Pantheon.

## Work performed

- Updated `docs/governance/CAPABILITY_PLACEMENT.md` with a governed execution handoff section.
- Added effect classes: `read_only`, `internal_state_change`, `external_effect`, `canonical_effect`.
- Added preflight outcomes: `allow_read_only`, `allow_candidate_only`, `needs_approval`, `pending_confirmation`, `capability_gap`, `block`.
- Added Capability Gap shape and typical gap values.
- Added idempotency discipline for non-read-only effects.
- Added Outcome Observation Candidate shape.
- Added placement-matrix row for the governed execution handoff.
- Added rejected collapses for handoff delivery, runtime success, pending confirmation and capability gaps.
- Added fictional architecture / urbanisme example: `docs/examples/architecture_abf_handoff/README.md`.
- Updated `docs/examples/README.md` to index the new example and align wording with Registre vocabulary.
- Updated `CHANGELOG.md` with version `0.1.51`.

## Boundary

Documentation and fictional example only.

No runtime bridge, OpenWebUI Action, Hermes skill, MCP change, schema, test, operation file, Docker change, `.env` change, queue, scheduler, provider router, approval engine or memory promotion was added.

No protected path was touched.

## Repo state

Documented non-implemented.

Candidate support doctrine until reviewed.

The architecture / ABF example is fictional and non-executable.
