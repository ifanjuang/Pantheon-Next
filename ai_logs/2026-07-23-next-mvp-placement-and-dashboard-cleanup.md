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

## First cleanup tranche

- keep `docs/assets/pantheon-control/README.md` as a boundary note;
- keep `docs/assets/pantheon-control/index.html` as a stable orientation URL;
- remove legacy local dashboard HTML, JavaScript, CSS, data fixtures and page renderers;
- point the retained entry to the external public MVP demo;
- preserve Git history instead of migrating obsolete prototypes.

## Follow-up migration tranche

Product-facing fictional scenarios, including the old architecture MVP demonstration, are to be migrated into `ifanjuang/pantheon-mvp` before their duplicate Next copies are removed. Conformance fixtures that validate Pantheon contracts remain in Next.

## Boundary

No runtime was installed or activated. No professional document was moved. No secret, real dossier, approval, Register entry or external action was created.

```text
migration != adoption
public demo != live cockpit
runtime success != Evidence
```
