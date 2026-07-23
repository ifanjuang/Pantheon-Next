# 2026-07-23 — Next/MVP placement and dashboard cleanup

Status: validation-only intervention trace.

## Human direction

The maintainer approved a clearer repository split and authorized deletion of superseded files to avoid repository overload.

## Decision applied

```text
Pantheon Next -> doctrine, schemas, conformance fixtures, validators, policy and trace
pantheon-mvp  -> executable cockpit, demo projects, runtime scenarios and integration fixtures
private layer -> deployment configuration and real professional data
```

The detailed placement rule is recorded in:

```text
docs/governance/NEXT_MVP_REPOSITORY_PLACEMENT.md
```

## Pantheon Control cleanup

- keep `docs/assets/pantheon-control/README.md` as a boundary note;
- keep `docs/assets/pantheon-control/index.html` as a stable orientation URL;
- remove the complete legacy local dashboard subtree: HTML, JavaScript, CSS, JSON, fixtures, page renderers and duplicate Hermes previews;
- point the retained entry to the external public MVP demo;
- preserve Git history instead of migrating obsolete prototypes.

## Architecture scenario migration

The product-facing fictional architecture scenario was transformed into:

```text
repository: ifanjuang/pantheon-mvp
pull request: #49
head commit: 673d3faccfdc78c7d4eb2ceaa24f8d7dc8d6a7fa
destination: demo/scenarios/architecture-mvp-fictif/
```

The ten-source corpus and a compact expected-review fixture were retained. The verbose manual-run outputs and standalone duplicate HTML were not migrated; Git history preserves them. Their former copies under `examples/architecture/mvp_dossier_fictif/` and `docs/assets/architecture-mvp/` are removed by the dependent Pantheon Next change.

Conformance fixtures that validate Pantheon contracts remain in Next.

## Boundary

No runtime was installed or activated. No professional document was moved. No secret, real dossier, approval, Register entry or external action was created.

```text
migration != adoption
public demo != live cockpit
runtime success != Evidence
```
