# 2026-08-09 — I4 Capability eligibility convergence

Parent: #620
Issue: #634

## Objective

Converge Capability admission/eligibility without introducing a second authorization owner.

## Repository finding

The intended read-only owner already existed in `mcp-server`, but its Passport validator had drifted behind current repository contracts:

- it still expected the historical nested `mcp_capability_passport` shape;
- it required an MCP server;
- it did not allow the now-canonical `skill` Capability primitive;
- it did not consume I2 exact implementation provenance.

The canonical `schemas/capability_passport.schema.yaml` is now stronger than that historical validator and is the correct referent.

## Convergence

`mcp-server/pantheon_mcp/passports.py` now validates caller-provided Passports directly against the canonical repository schema rather than maintaining a parallel hand-coded shape.

It adds only read-only eligibility qualification:

```text
status=reviewed
+ exact immutable implementation anchor
-> reviewed_exact_release posture
```

A reviewed Passport without one of:

```text
commit_ref
content_digest
package_digest
```

remains schema-valid when otherwise structurally valid, but reports a governance gap and is not ready for eligibility review.

The template `templates/mcp_capability_passport.yaml` is aligned to the current flat schema and supports optional MCP metadata plus Skill capabilities.

## Authorization boundary

Even a reviewed exact release returns:

```text
authorization_effect: none
activation_effect: none
runtime_probe_performed: false
```

A reviewed Passport carrying `task_authorization: task_authorized` is reported with a governance gap because eligibility review does not itself establish per-task legitimacy.

Task Contract / Execution Admission remains downstream and unchanged.

## Non-equivalences

```text
schema valid != admitted
reviewed != task-authorized
exact release known != safe
eligibility != activation
eligibility != task authorization
replacement release != inherited eligibility by name
runtime success != Evidence
```

## Boundary

No new admission object, persistence table, runtime probe, installer, provisioner, automatic approval, activation, Task Contract authorization, Evidence admission or H qualification path is added.
