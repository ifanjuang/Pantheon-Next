# AI Log — Skill admission guard for capability registry

Date: 2026-06-07

## Scope

Added a supply-chain and admission guard to `docs/governance/CAPABILITY_REGISTRY.md` inside PR #53.

The goal was to absorb the skills.sh / external skill catalogue concern without creating a separate governance track or treating a catalogue as authority.

## Change made

`CAPABILITY_REGISTRY.md` now states explicitly:

```text
Availability is not authorization.
Installability is not capability approval.
```

It adds a `Skill admission guard` section requiring a runtime skill declaration to record, before eligibility:

- source;
- pinned version or immutable reference;
- author / owner;
- installer information, if relevant;
- permissions and perimeter;
- scope;
- forbidden effects and outputs;
- risk class;
- approval ceiling;
- required Evidence Pack Candidate shape;
- accountable owner;
- reviewer and review date;
- lifecycle status.

## Why

External skill catalogues and installers may expose or distribute capabilities. They do not approve them.

A skill can be discoverable, popular, recommended, easy to install or already present in a runtime and still remain ineligible for governed work until admitted by Pantheon metadata.

## Boundary

Documentation only.

No runtime, installer, schema, test, operation, platform, Docker, environment, automatic skill update, automatic skill promotion, approval engine or memory engine was added.

The registry declares. The runtime executes. Pantheon governs eligibility, proof and status. The human decides.
