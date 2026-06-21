# 2026-06-21 Add MCP policy server to the module map

Status: documentation only (governance map entry).

The bounded `mcp-server/` module — implemented and now documented (#184–#188) —
had no row in the canonical module map of `MODULES.md`, although most modules
do. This adds it, so the governance map answers its three questions for the
module (what area, which authority document, which surface).

Change:

- docs/governance/MODULES.md — adds to the canonical module map:
  `MCP policy server | PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md, mcp-server/ |
  active_support | Bounded read-only policy / validation MCP surface centered on
  the capability passport; also validates candidate Architecture Project
  Understanding dossiers. Serves doctrine and returns decisions as data; does not
  execute, send, write, approve, schedule, queue, route providers or promote
  memory. The gate decides; the human decides.`
  Placed beside the OpenWebUI / Hermes exposure surfaces. Status `active_support`
  from the module status vocabulary (read-only support surface).

Verified: status_headers / internal_links clean; index_coverage and
axis_vocabulary green vs baseline (the authority doc is already in
AUTHORITY_INDEX.md); the docs/governance runtime-phrase guard passes (the
boundary is stated in explicit "does not …" negation).

Boundary: documentation only. The module stays read-only and candidate-only.
