# 2026-06-23 verification preset reader

Status: implemented (reader tool + CLI + tests). Consumes the verification preset
schema (#212), closing its "documented but not yet consumed" status.

## Why

#212 added the verification_preset schema (per-module: which verifications apply +
thresholds) but nothing read it. This adds the read-only reader the owner asked
for: it turns a preset into an actionable plan as data without running anything.

## Change

- mcp-server/pantheon_mcp/presets.py (new) — `load_verification_preset(preset)`.
  Validates the preset against schemas/verification_preset.schema.yaml (parallel
  to validate_apu_dossier; schema errors -> result error + problems), then projects
  it into a plan: `active` (each {verification, thresholds, evidence_fields}),
  `inactive` (applies:false or absent), and capability_gaps. `evidence_fields`
  mirror each verification's evidence schema, so a producer learns exactly what to
  gather. Read-only: runs no verification, gathers no evidence, probes nothing,
  decides nothing.
- server.py — exposes the `load_verification_preset(preset_yaml)` tool.
- presets_cli.py (new) + pyproject — `pantheon-load-verification-preset`; exit 0
  when the preset is valid, 1 on schema/input errors.
- docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md — tool list entry plus
  an update to the preset section describing the reader.
- schemas/README.md — the preset is now "read by load_verification_preset" rather
  than "not yet consumed".
- mcp-server/README.md — intro tool table, CLI section, layout.

Tests:
- tests/test_presets.py — 6 cases (valid plan + known order with backup excluded;
  thresholds/evidence_fields carried; schema error on unknown verification; schema
  error on missing module_id; gap when nothing applies; non-mapping error).
- tests/test_presets_cli.py — 4 CLI cases.
- The shipped example preset projects all five verifications active.

## Validation

`unittest discover -s mcp-server/tests` — 118 OK (108 prior + 10). `pytest tests/`
9 passed. governance doctor checks + runtime-phrase guard green.

Boundary: read-only. The reader validates and projects a declaration into a plan;
it runs no verification, gathers no evidence, probes nothing, installs nothing and
decides nothing. The verify_* tools still classify gathered evidence; the gate and
the human decide. One-way dependency intact.

## State of the verification family

Five verifications (install, observability, backup, exposure, update), each with a
tested schema example and a CI parity guard; a per-module verification preset that
binds them; and now a reader that projects a preset into a plan. The chain is:
preset declares -> reader projects the plan -> producer gathers evidence -> verify_*
classifies -> gate/human decide.
