# AI Log — External Tool Placement Register

Date: 2026-06-01

## Scope

Created a lightweight governance support register for external tool placement decisions after review of three repositories discussed in conversation:

- `greensock/gsap-skills`;
- `sujan1-3/browser-eyes-mcp`;
- `rowboatlabs/rowboat`.

## Canonical documents checked

- `docs/governance/STATUS.md`;
- `docs/governance/MODULAR_DOMAIN_REORIENTATION.md`;
- `docs/governance/CAPABILITY_PLACEMENT.md`;
- `docs/governance/DOMAIN_PACK_SPEC.md`.

## Files changed

Created:

- `docs/governance/EXTERNAL_TOOL_PLACEMENT_REGISTER.md`.

## Decision summary

- `greensock/gsap-skills`: accepted as Hermes frontend / motion skill candidate; documented non implemented.
- `sujan1-3/browser-eyes-mcp`: accepted as Hermes privileged MCP skill candidate with read-only, interactive and mutation modes; documented non implemented.
- `rowboatlabs/rowboat`: classified as external reference / possible future adapter candidate; not accepted as a Hermes skill or Pantheon core component; documented non implemented.

## Boundary maintained

Pantheon governs placement, status, proof, memory, scope and approval.

Pantheon does not install or implement the reviewed tools.

## Repo state

Documented non implemented.
