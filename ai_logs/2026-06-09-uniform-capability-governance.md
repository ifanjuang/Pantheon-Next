# AI log — Uniform Capability Governance keystone

Date: 2026-06-09.

## Intent

Encode the maintainer's architectural invariant: Pantheon stays master over every
added capability (module, skill, function, plugin) without writing per-module
rules. One rulebook, one passport per capability, an unbypassable gate for
consequential effects.

## What was produced

`docs/governance/UNIFORM_CAPABILITY_GOVERNANCE.md` (active support doctrine):

- the principle (one law, one passport per capability, no per-module rules);
- the universal envelope (Task Contract -> capability -> Result Candidate +
  Evidence Pack -> gate -> human);
- the chokepoint rule that makes Pantheon master — the runtime must route
  consequential effects through Pantheon's policy check; a bypassable gate makes
  Pantheon master only in advice;
- the PDP/PEP framing (Pantheon = Policy Decision Point, Hermès = Policy
  Enforcement Point, OpenWebUI = surface, Control = eyes and hands), with PDP/PEP,
  OPA/Gatekeeper, in-toto/SLSA and Backstage cited as distilled external grounding
  (vocabulary and pattern only, no import);
- how modules/skills/functions/domains defer to it;
- Control under this law (applies the passport, displays gate state, decides
  nothing).

Indexed in `AUTHORITY_INDEX.md`.

## Boundary

Documentation only. No runtime, scheduler, queue, provider router, policy engine,
installer or MCP host inside Pantheon Next. Enforcement lives in the runtime
honouring the gate. It coordinates existing canonical doctrine (capability
passport, the two gates, the placement test); it does not replace it. Lint-clean;
no retired vocabulary. The light cross-reference reconciliation of
`MODULE_ACTIVATION` / `ROLE_ACTIVATION` / `SKILL_LIFECYCLE` / `EXTERNAL_TOOLS_POLICY`
and the Pantheon Control reframe are follow-ups.
