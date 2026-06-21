# 2026-06-21 mcp-server APU validation surface

Status: implemented (bounded read-only mcp-server tool).

Extends the bounded `mcp-server/` read-only policy/validation surface with a new
tool that validates a candidate Architecture Project Understanding (APU) dossier
against the governance schemas and returns the gate posture as data. Read-only:
it executes nothing, canonizes nothing, approves nothing, writes nothing. The
gate decides; the human decides. Stays within the doctrine boundary —
`mcp-server/` validates and prepares candidates, it does not execute.

Added:

- mcp-server/pantheon_mcp/apu.py — `validate_apu_dossier(dossier: dict) -> dict`:
  - maps each APU object_type to its schema under
    `schemas/architecture-project-understanding/` (program, requirement,
    deviation, stable_object, attribute_claim, derivation, contradiction, the
    object-model family, etc.);
  - validates each object with `jsonschema.Draft202012Validator`, resolving
    cross-file `$ref` to `shared.schema.yaml#/$defs/...` through a
    `referencing.Registry`;
  - runs light referential-integrity checks (program/requirement/deviation links,
    attribute_claim about/derived_from), tolerating documented external prefixes
    (SRC-, DET-, EQ-, SYS-, OP-CAND-, REV-, MAIL-);
  - returns gate posture: `posture: candidate-only`, `canonical_effect: false`,
    `regulatory_claims_without_approval` (regulatory_claim use without an
    approved_for_contractual_action state + evidence), and
    `human_decisions_required` (pending_human deviations/contradictions,
    unconfirmed object-identity matches).
- mcp-server/pantheon_mcp/server.py — imports `apu` and exposes the
  `validate_apu_dossier(dossier_yaml)` tool (YAML in -> JSON out via `_dump`).
- mcp-server/pyproject.toml — `jsonschema>=4.22` moved into runtime
  `dependencies` (the server now validates dossiers; the test extra is retained).
- mcp-server/tests/test_apu.py — four read-only tests: a clean dossier validates
  and stays candidate-only (pending deviation surfaced as a human decision); a
  regulatory_claim without approval is flagged; an unresolved reference is
  reported; an unknown object_type is reported.

Validation: `python3 -m unittest discover -s mcp-server/tests` — 33 tests OK
(29 prior + 4 new). `check_apu_referential_integrity.py` still green.

Boundary: candidate-only, human-gated, one-way dependency (mcp-server depends on
the governance core, never the reverse). No execution, routing, scheduling,
queueing, memory promotion or approval engine introduced.
