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
- remove the legacy local dashboard pages, navigation, styling, project fixtures and obsolete renderers;
- retain the synthetic Hermes renderer preview because protected tests validate parity with the external plugin template;
- retain six read-only JavaScript classifier mirrors because protected MCP parity tests compare them with the Python policy functions;
- retain the still-referenced card revision lifecycle specification until its owner document is changed in the same future PR;
- retire the old local Intent Log implementation claim while preserving the candidate governance model;
- point the retained entry to the external public MVP demo;
- preserve Git history instead of migrating obsolete prototypes.

The retained parity artifacts are validation support. They do not recreate the local dashboard or provide an operational surface.

## Architecture scenario migration

The product-facing fictional architecture scenario was transformed and merged into:

```text
repository: ifanjuang/pantheon-mvp
pull request: #49
merge commit: ec7c9414a3b45542a835d1c5447ac0d17fccf9ba
destination: demo/scenarios/architecture-mvp-fictif/
```

The ten-source corpus and a compact expected-review fixture were retained. Review added a separate foundation/site-risk finding for the steep terrain and undocumented void. The verbose manual-run outputs and standalone duplicate HTML were not migrated; Git history preserves them. Their former local copies are removed by the dependent Pantheon Next change.

Conformance fixtures that validate Pantheon contracts remain in Next.

## Boundary

No runtime was installed or activated. No professional document was moved. No secret, real dossier, approval, Register entry or external action was created.

```text
migration != adoption
public demo != live cockpit
parity mirror != user-facing dashboard
runtime success != Evidence
```
