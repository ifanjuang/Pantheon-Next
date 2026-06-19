# 2026-06-19 governed evidence registry lifecycle model

Status: documented non-implemented.

Created `docs/assets/pantheon-control/evidence_registry_model.json` as a prototype target model for evidence cards.

The model separates:

- `cards`: current state displayed by the UI;
- `events`: append-only history of changes, proposals, approvals, merges and revisions;
- `relations`: graph edges between cards;
- `sources`: proof references;
- `merge_requests`: governed merge proposals and approved merge history;
- `split_requests`: governed split proposals;
- `transactions`: anti-loop propagation containers;
- `view_models`: precomputed UI views for fast mobile rendering.

Key principles encoded:

- AI analysis proposes candidate changes, not direct mutations;
- approval validates candidate changes;
- merge never deletes historical cards;
- merged cards become lifecycle redirects;
- propagation is transaction-scoped to avoid loops;
- one card can be recalculated only once per transaction;
- propagation can create impact/conflict/review candidates, never automatic validation.

This is a prototype registry model only. No runtime, datastore, schema validation, approval engine, memory promotion or external action was implemented.
