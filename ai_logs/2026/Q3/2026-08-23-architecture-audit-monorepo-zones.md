# Architecture Audit — monorepo zone convergence

Date: 2026-08-23
Status: implementation/CI convergence trace; not doctrine.

## Objective

Replace the Architecture Audit's obsolete two-repository physical model with explicit Pantheon monorepo zones while preserving an independent merge gate.

## Observed starting point

The audit was green but still checked out and compared multiple full copies of Pantheon-Next and described the executable candidate as a separate `pantheon-mvp` repository. The pinned authority checkout was not treated as removable duplication: it prevented a pull request from changing both the candidate and the rule used to judge the same run.

## Result

The audit now models two physical zones:

- `governance-core`: repository-root governance, schemas, registries and guards outside `implementation/`;
- `implementation`: the executable candidate under `implementation/`.

Zone membership is deliberately separate from support-registry owner identity. The existing support identities (`Pantheon-Next`, `pantheon-mvp`, external Hermes/Cockpit responsibilities) are not implicitly renamed by a folder move.

Nested roots are assigned by most-specific path, so an `implementation/**` artifact is inventoried once as implementation rather than simultaneously as governance.

The permanent closure guard now requires explicit architecture and module-analysis zones and preserves its existing refusal rules for generation-named active artifacts, internal versioned routes, parse failures and unreferenced implementation candidates.

## Independent audit authority

The workflow uses:

1. one checkout of the current monorepo candidate;
2. one sparse immutable audit-authority snapshot containing only:
   - `docs/governance/authority/PANTHEON_SYSTEM_OWNERSHIP_REGISTRY.json`;
   - `templates/hermes/distribution/distribution-lock.schema.yaml`.

The snapshot is pinned to `db30006b070a74df249be8060a0b010ed994c054`, whose relevant authority-file bytes matched the previously pinned audit authority when checked before the change. Candidate changes to those files are reported as drift and do not rewrite the merge-gating rule used in the same run.

The previous separate current-main and distribution-schema full checkouts are removed.

## Transitional distribution lock

The Hermes distribution lock remains revision 2 in this tranche. Its historical `Pantheon-Next` / `pantheon-mvp` source identities are mapped to the current monorepo physical roots during validation. Migrating that manifest/schema to explicit source zones is intentionally deferred to a separately reviewed change.

## Validation during transformation

Before publication, the transformed tree was exercised in an ephemeral GitHub Actions checkout:

- 22 targeted architecture/module/closure/distribution tests passed;
- the real monorepo architecture inventory completed;
- the real module-usage inventory completed;
- the permanent convergence closure guard passed;
- the Hermes distribution lock validator passed with its existing three component digests and non-authority posture.

The first transformation attempt failed closed on an overly strict source anchor. The second reached tests but lacked the editable implementation install. Both failures produced no published transformed tree. The validated third attempt could not push the workflow file because the Actions token lacked `workflows` permission. The non-workflow changes were therefore published separately, with workflow files restored first, and the active workflow was then updated through the GitHub connector with workflow permission.

## Non-equivalences

```text
zone/folder != governed identity
audit success != authorization
runtime success != Evidence
projection != persistence
drift report != authority adoption
```
