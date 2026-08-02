# Card Projection Definition tranche

Date: 2026-08-03

## Observed need

`CARD_STACK_MODEL.md` defines the cockpit projection doctrine, while `pantheon-mvp` still hard-codes card roles, families, mappings and root navigation metadata in JavaScript. Moving navigation metadata directly into an ad hoc registry would create an implicit second card model.

## Change

- define a bounded Card Projection Definition model;
- add a machine-readable schema;
- add one fictive navigation-space example;
- validate the example and closed authority boundaries.

## First pilot

The first implementation pilot remains limited to root navigation cards. No Project, Information, Work, Decision or Evidence business rule is migrated in this tranche.

## Boundaries

```text
card projection definition != underlying object schema
projection configuration != workflow
visible action != authorized action
Cockpit rendering != execution
```
