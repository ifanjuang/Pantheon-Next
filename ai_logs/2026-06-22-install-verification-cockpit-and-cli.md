# 2026-06-22 install verification — cockpit wiring + CLI

Status: implemented (thin cockpit display + read-only CLI; tests added). Follows
the merged `verify_install` mcp-server tool (PR #201).

Two requested follow-ups, in order: wire the `installations.html` cockpit mockup
to the `verify_install` contract, then add a CLI.

## Cockpit wiring (docs/assets/pantheon-control)

The cockpit is a static, read-only surface that already replicates governance
classifications client-side (`scoreNasProfile`, `scoreModulePlan`). Added an
"Vérification d'installation" panel that is a faithful **display reflection** of
`verify_install`: the Python contract stays the single source of truth; the JS
mirrors its rules.

- installations-data.js — adds the verification contract block (evidence shape),
  `VERIFY_VERDICT_TONE`, `VERIFY_TRISTATE`, `VERIFY_CHECKS_STATE`.
- installations-ui.js — `verifyInstallVerdict(state)` mirrors install.py exactly
  (installed / answers from reachable + 2xx status / checks_green → verdict
  green / degraded / absent / unknown, with capability gaps). Plus the panel
  (`renderVerifier` / `renderVerifyResult` / `prepareVerify`), wired into the
  page and the mount refresh.
- installations.html — bumps the cache-busting version of the two changed
  scripts to `20260622-verify-1`.

The panel classifies evidence the human enters and shows the verdict + gaps. It
runs no probe, no NAS access, installs nothing and decides nothing; the
"consigner" button only appends a candidate line, like the rest of the page.

Parity checked under node: green / degraded (unreachable) / degraded (red check)
/ absent / unknown / 5xx-degraded / no-checks-unknown all match install.py.

## CLI (mcp-server)

- pantheon_mcp/install_cli.py (new) — `pantheon-verify-install [file|-]`, mirrors
  the APU CLI. Prints the verdict report as JSON; exit 0 only when the verdict is
  `green`, 1 otherwise (degraded / absent / unknown / input error), so it can
  gate a script. Probes nothing, decides nothing.
- pyproject.toml — registers the `pantheon-verify-install` entry point.
- mcp-server/README.md — adds the "Install verification CLI" section and the
  `install_cli.py` layout line.
- tests/test_install_cli.py (new) — five read-only tests: green exits 0;
  degraded / unknown exit 1; missing file; invalid YAML.

Validation: `python3 -m unittest discover -s mcp-server/tests` — 51 tests OK
(46 prior + 5). `node --check` on both cockpit scripts passes; CLI stdin smoke
returns the green verdict with exit 0.

Boundary: read-only, candidate-only; the gate and the human decide. The cockpit
displays; it does not act. No probe, no NAS access, no install, no routing,
scheduling, queueing, approval or promotion. One-way dependency intact.
