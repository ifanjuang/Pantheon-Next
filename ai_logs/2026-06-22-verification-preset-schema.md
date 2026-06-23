# 2026-06-22 per-module verification preset schema

Status: implemented (schema + example + docs). Second of the two owner-chosen
follow-ups (after verify_update #211). Answers "a-t-on besoin d'un preset config /
fichiers par module vis-à-vis de Pantheon".

## Finding

A module already declares to Pantheon via its capability passport and module
manifest. What was missing: nothing bound a module to the verification family
(install / observability / backup / exposure / update) — each verify_* call took
thresholds inline. The owner chose a dedicated schema.

## Change

- schemas/verification_preset.schema.yaml (new) — per-module declaration: which
  verifications apply and the thresholds the evidence should meet
  (expected_checks, expected_signals, freshness_max_age_s, errors_threshold,
  require_restore, max_reach, require_auth, require_scope, channel). Thresholds
  mirror the corresponding evidence schema fields. `x-boundary` records it runs no
  verification, gathers no evidence and decides nothing.
- schemas/examples/verification_preset.example.yaml (new) — a Hermes preset,
  registered in tests/test_schema_examples.py (validates against the schema).
- schemas/README.md — lists it as structure-only, documented-but-not-consumed.
- docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md — a "Per-module
  verification preset" section: this is the governance answer to what a module
  declares to Pantheon for verification, alongside its passport and manifest. A
  producer (Hermes / operator / cockpit) reads the preset to know which
  verifications to gather evidence for and which bar to apply; the verify_* tools
  still classify the provided evidence and return verdicts as data.

## Honest status

Documented, not yet consumed: no tool currently reads a preset to drive or gate a
verification. That is deliberate (the preset is a declarative contract); wiring a
reader is a separate, opt-in step if desired. Schema/example agreement is tested.

## Validation

`pytest tests/test_schema_examples.py` — 4 passed (new pair validates). governance
doctor checks (status headers, internal links, index coverage, axis vocabulary)
green vs baseline; runtime-phrase guard passes on the edited authority doc.

Boundary: a schema (structure only), an example and documentation. Nothing
executes, runs a verification, gathers evidence, probes, installs or decides. The
preset is a contract, not a gate; the verify_* tools decide nothing; the gate and
the human decide. One-way dependency intact.
