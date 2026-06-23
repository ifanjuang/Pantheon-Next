# 2026-06-21 Document the APU validation tool

Status: implemented-but-not-documented gap closed (documentation only).

The `validate_apu_dossier` MCP tool shipped in #184 (and hardened in #187) was
implemented but absent from every doctrine surface — exactly the
"implemented but not documented" state the work rules require resolving. This
records it where the module is governed and described. No code change.

Changes:

- mcp-server/README.md:
  - intro now states the server also validates candidate Architecture Project
    Understanding dossiers;
  - tool table gains a `validate_apu_dossier(dossier_yaml)` row (schema errors,
    unresolved references, candidate-only posture, no canonical effect,
    regulatory claims lacking approval, human decisions required);
  - layout lists `apu.py`; the tests paragraph mentions APU dossier validation.
- docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md (the module's
  authority doc): adds `validate_apu_dossier(input) -> apu_validation_report` to
  the Phase 4 read-only validation tools, with a sentence on what it returns and
  the read-only/candidate-only posture.

Verified: status_headers / internal_links / index_coverage clean;
axis_vocabulary green vs baseline; the docs/governance runtime-phrase guard
passes (the additions describe a validate-only tool in negated/“executes
nothing” context).

Boundary: documentation only. The tool stays read-only, candidate-only; the gate
and the human decide.
