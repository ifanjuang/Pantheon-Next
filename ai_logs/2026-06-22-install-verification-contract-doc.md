# 2026-06-22 install verification — evidence contract documented

Status: implemented (documentation + schema + example + test wiring). Follows the
`verify_install` tool (PR #201) and its cockpit/CLI surfaces (PR #202).

## Why

Reviewing the two prior PRs surfaced one real asymmetry: every other governed
input in the repo has an authoritative schema under `schemas/`, but
`verify_install`'s evidence input lived only in docstrings and a JS comment.
Producers (Hermes, operators) had no canonical spec of what evidence to provide,
and the verdict rules were stated in code in two places (Python + cockpit JS)
without a documented source of truth.

## Changes

- schemas/install_verification_evidence.schema.yaml (new) — documents the
  recommended evidence shape (component, installed / markers / logs, health,
  checks, expected_checks) with `x-boundary` flags and `governance_refs`. Every
  field is optional: the classifier is permissive and turns missing signals into
  capability gaps rather than rejecting, so the schema documents the contract for
  producers but is **not** enforced as a gate. Stated explicitly in the schema
  description and the README so it is not mistaken for runtime validation.
- schemas/examples/install_verification_evidence.example.yaml (new) — a green
  example, registered in tests/test_schema_examples.py. Verified twice: it
  validates against the schema, and `install.verify_install` classifies it
  `green` with no gaps — so schema, example and tool agree.
- schemas/README.md — lists the new schema with its documented-not-enforced note.
- docs/governance/PANTHEON_MCP_POLICY_SERVER_DEVELOPMENT.md — adds a
  `verify_install` evidence-contract section: field table, verdict semantics
  (absent / green / degraded / unknown), and an explicit statement that the
  Python classifier is the single source of truth and the cockpit surface mirrors
  it for display and must not diverge. Records that a `green` verdict is evidence
  for review, not an approval.

## Known residual risk (documented, not yet guarded)

The verdict rules now exist in Python (`install.py`, source of truth) and mirrored
in cockpit JS (`verifyInstallVerdict`). Parity was checked manually under node and
is asserted in prose, but no CI check enforces Python↔JS parity. A future guard (a
small node parity test, or generating the JS rules) would remove the drift risk;
left as a proposal rather than built unasked. The schema/example/tool agreement is
covered by tests; the JS mirror is not.

## Validation

- tests/test_schema_examples.py — 4 passed (new pair validates).
- root `pytest tests/` — 9 passed; `verify_install` agrees on the example (green).
- mcp-server suite — 51 OK.
- governance doctor checks (status headers, internal links, index coverage, axis
  vocabulary) green vs baseline; runtime-phrase guard passes on the edited doc.

Boundary: documentation, a schema (structure only) and an example. Nothing
executes, probes, accesses a NAS, installs, routes, schedules, queues, promotes or
approves. The schema is a contract, not a gate; the tool decides nothing; the gate
and the human decide. One-way dependency intact.
