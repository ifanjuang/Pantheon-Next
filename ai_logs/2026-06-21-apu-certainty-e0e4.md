# 2026-06-21 APU certainty unification (decision A)

Status: documented non-implemented (schema vocabulary change, approved).

Resolves the "single certainty representation" item of #169, arbitrated by the
maintainer as decision A: the governance certainty is the E0–E4 axis; the numeric
0..1 score survives only inside derivation as a computed detail, banded to E0–E4.

Changes (schemas/architecture-project-understanding/):

- attribute_claim: `certainty_score` (number) -> `certainty` (E0–E4 enum).
- stable_object: matches[].`certainty_score` (number) -> `certainty` (E0–E4).
- derivation: `produced_certainty_score` kept as the internal numeric score, with
  a description stating it is banded to the E0–E4 certainty and is not itself a
  governance field.

Also updated: the schema examples and the worked dossier (score -> band, e.g.
0.7 -> E3, >=0.8 -> E4), the contract doc L2 / object #4 / invariant #2, and the
dossier README (item marked resolved).

Mapping used (documented): <0.2 E0, 0.2–0.4 E1, 0.4–0.6 E2, 0.6–0.8 E3, >=0.8 E4.

Verified: pytest 9/9; referential-integrity 16/16; axis-vocabulary clean (no new
flags; `certainty` is now the desired field name); mcp-server 29/29.

Boundary: schema vocabulary alignment only; no runtime, no new object, no behavior
engine. The remaining #169 items ($defs factoring, zone_type-when-zone) stay open.

Refs #169.
