# AI log — mcp-server: first implementation slice

Date: 2026-06-10.

## Intent

The maintainer instructed: start the `mcp-server/` module. This is the
bounded module authorized by `CLAUDE.md` (read-only policy / validation
MCP surface centered on the capability passport), built per the phases of
`docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md` (merged in
PR #75). The maintainer's instruction is the Phase 8 implementation
authorization for this slice.

## What was built

New bounded code under `mcp-server/` (no Pantheon-OS code copied):

- `pantheon_mcp/repo.py` — read-only repository access, confined to the
  repo root (path-escape rejected).
- `pantheon_mcp/source_map.py` — Phase 1/2: canonical source map, 20
  resources served as `pantheon://<key>`, each labeled with the authority
  and status parsed from `AUTHORITY_INDEX.md`. Missing files report
  `exists: false`; nothing is invented.
- `pantheon_mcp/passports.py` — capability passport validation mirroring
  `templates/mcp_capability_passport.yaml`, with governance gap rules
  (external send requires >= C3 and the User Decision Gate; candidate
  passports cannot be task_authorized — visible != admitted).
- `pantheon_mcp/policy.py` — Phase 4: policy decision as data on the
  GLOSSARY axes (K0–K4 consequence, V0–V4 verification, C0–C5 approval
  ceiling), unknown external effect escalates to K4, and the Phase 7
  refusal posture (send/write/merge/approve/promote/install/schedule/
  route/execute are refused).
- `pantheon_mcp/doctor.py` — read-only doctor checks mirroring the
  governance CI; the retired-vocabulary scan is informational and yields
  the remaining issue #90 worklist (~47 legacy occurrences, mostly under
  docs/examples/ and docs/assets/).
- `pantheon_mcp/server.py` — FastMCP stdio wiring only; 6 tools, 20
  resources. Logic modules import without the SDK.
- `fixtures/`, `tests/` — fictional passports and 16 read-only unit tests
  (all green locally), including refusal tests.
- `README.md`, `pyproject.toml` — module-local packaging (`mcp`, `PyYAML`);
  the root `pyproject.toml` is untouched.

## Verification

- `python3 -m unittest discover -s mcp-server/tests` — 16 tests, all pass.
- FastMCP smoke test: 6 tools and 20 resources listed over the SDK.
- Local equivalents of both CI lints remain green (module adds no
  governance doc except this log).

## Boundary

The module is read-only / validation / candidate-preparation. It performs
no execution, sending, writing, merging, approval, memory promotion,
installation, scheduling or provider routing, and refuses requests to do
so. No protected path (`schemas/`, `tests/`, root `pyproject.toml`,
Docker, `.env`) was changed. The module remains a candidate until
reviewed; serving it to Hermes/OpenWebUI stays a maintainer decision.

## Repo state

`mcp-server/` : implemented as candidate (first slice). Indexing in
STATUS/MODULES/AUTHORITY_INDEX deferred to a separate reindex pass per
the triage convention.
