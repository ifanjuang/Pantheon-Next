# AI log — Target Architecture coherence compass

Date: 2026-06-09.

## Intent

Give the system a single coherence compass: a coherent end-to-end picture, the
map of which external pattern fills which slot (absorb the patterns, not the
repositories), the gaps that keep the system from being real, and the sequence
to close them — so the project consolidates rather than absorbing more repos.

## What was produced

`docs/governance/TARGET_ARCHITECTURE.md` (validation-only):

- the layered system (surface / law-PDP / execution-PEP / proof / observability),
  with each layer's reality state;
- the invariant (the chokepoint, per UNIFORM_CAPABILITY_GOVERNANCE);
- the absorption map: PDP-PEP and OPA/Gatekeeper for the gate, in-toto/SLSA for
  signed proof, Backstage for Control, TUF for safe install/update, directory-mcp
  for the Registre actor layer, ASSERT for conformance, self-inspect for rites,
  SkillsGate for skill admission, CBR for composition;
- the coherence gaps, ranked (the gate is not enforced; no Registre; no validator;
  no proven vertical; observability/attestation links unspecified);
- the sprawl to consolidate;
- the sequence (name and enforce the chokepoint -> harden the spine -> wire proof
  and observability -> prove one vertical -> consolidate);
- the one rule of coherence (a vertical passes the gate, leaves proof, stays green).

Indexed in `AUTHORITY_INDEX.md`.

## Boundary

Direction record only. No runtime, schema, test, installer, policy engine or
protected-path change. Coordinates existing doctrine and external reference
reviews; instantiates none of it. Lint-clean; no retired vocabulary.
