# AI Log — Pantheon Cockpit UX candidate spec

Date: 2026-06-14

## Context

The user asked whether Pantheon should progressively replace OpenWebUI, whether Pantheon needs its own discussion interface, and whether it should support OpenWebUI-like hierarchical conversations with branches plus assisted drafting over selected text in working documents.

The discussion clarified that Pantheon should not clone OpenWebUI or become an execution runtime. The proposed direction is a governed professional cockpit: project context, hierarchical discussion, workflow proposals, assisted drafting, proofs and sources, decision capture and traceability.

## Repository reading

The following active governance documents were reviewed before writing:

- `docs/governance/STATUS.md`
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`
- `docs/governance/CAPABILITY_PLACEMENT.md`
- `docs/governance/DOMAIN_PACK_SPEC.md`

Relevant boundaries confirmed:

- OpenWebUI exposes.
- Hermes Agent executes.
- Pantheon Next governs.
- Pantheon is governance-first and not an execution runtime.
- The cockpit may expose and capture decisions, but must not approve, execute, promote memory or become a runtime.
- Domain packs frame professional AI use and do not advise, validate, send, execute or remember by themselves.

## Change made

Created:

- `docs/governance/PANTHEON_COCKPIT_UX_SPEC.md`

The document is marked:

```text
Status: candidate — to verify.
```

It specifies a product/UX candidate for:

- cabinet mode vs technical administration mode;
- main navigation;
- professional request lifecycle;
- Workflow Proposal card;
- hierarchical discussion and branches;
- assisted drafting surface;
- Draft Anchor candidate;
- Proofs and sources panel;
- Capability Gap display;
- system health for non-technical professionals;
- local AI / external AI display;
- Google Docs, Google Sheets and Office projections;
- UX microcopy rules;
- accepted / rejected / to verify orientation.

## Boundary state

This change is documentation only.

It does not implement:

- UI;
- chat engine;
- runtime;
- editor;
- plugin;
- bridge;
- provider router;
- scheduler;
- queue;
- approval engine;
- memory engine;
- OpenWebUI Function;
- Hermes skill;
- Google Apps Script;
- Office add-in;
- external connector.

## Notion tracking

The existing Notion card `PR119 — lecture détaillée Pantheon Control usage-focused` was commented with the new orientation because this work extends the dashboard/cockpit follow-up already tracked there.

A dedicated Notion card may still be useful if the spec is later turned into a PR or a larger follow-up issue.

## Follow-up

Recommended next steps:

1. Decide whether to update `AUTHORITY_INDEX.md` and `README.md` to reference this candidate document. These files were not edited in this pass.
2. Convert the spec into a non-executable HTML mockup update.
3. Keep UI copy aligned with the boundary: candidate, proposed, to verify, human decision required.
4. Avoid any implementation claim until a runtime or UI actually exists outside the governance document.
