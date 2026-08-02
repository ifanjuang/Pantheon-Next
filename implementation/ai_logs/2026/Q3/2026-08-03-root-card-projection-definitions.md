# Root card projection definitions

Date: 2026-08-03

Status: implementation candidate — dependent on Pantheon-Next #518.

## Change

- add one operational projection-definition registry for the four root navigation spaces;
- keep the same identities, titles, summaries, roles, presentation families, statuses and boundary notes already exposed by the Cockpit;
- verify exact alignment with `navigation_registry.json`;
- keep children assembly in the existing navigation projection path.

## Current boundary

This tranche introduces the validated operational instance but does not yet switch `cockpit_projection.js` to consume it. That wiring remains a focused follow-up so the behavioral diff can be reviewed independently.

```text
projection definition present != projection consumed
projection consumed != authorization
static status label != lifecycle owner
navigation source != endpoint
```
