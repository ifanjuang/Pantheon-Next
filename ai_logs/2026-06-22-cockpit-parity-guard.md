# 2026-06-22 cockpit ↔ classifier parity guard

Status: implemented (CI test). Closes the residual drift risk flagged in
2026-06-22-install-verification-contract-doc.md.

## Why

The install verdict rules live in two places by necessity: `install.verify_install`
(Python, source of truth) and the cockpit mirror `verifyInstallVerdict`
(installations-ui.js). Parity was only checked manually and asserted in prose;
nothing prevented the JS mirror from drifting silently.

## Change

- mcp-server/tests/test_cockpit_parity.py (new) — replays a 108-case matrix
  (installed × reachable × status_code × checks) through both implementations and
  asserts the same verdict. It maps each cockpit tri-state form to verify_install
  evidence, computes the Python verdict, and evaluates the shipped cockpit JS in a
  sandboxed `node -e` process (DOM/helpers stubbed) for the JS verdict.

Read-only: it evaluates the shipped scripts, touches no system and writes nothing.
It skips gracefully when node is absent (best-effort locally) and runs in CI,
where the mcp-server job's ubuntu-latest runner ships node.

## Validation

- The 108-case matrix passes (Python and JS agree on every case).
- Drift detection verified: injecting a divergence into a temp copy of the JS
  (forcing verdict `green`) makes the parity comparison fail as intended.
- Full mcp-server suite: 52 OK (51 prior + 1).

Boundary: a test only. Nothing executes, probes, installs or decides. The Python
classifier remains the single source of truth; this guard simply forbids the
display mirror from disagreeing with it.
