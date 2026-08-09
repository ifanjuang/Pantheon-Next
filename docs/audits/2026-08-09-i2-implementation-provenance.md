# I2 implementation / release provenance — 2026-08-09

Status: validation-only convergence note.

Parent: #620
Issue: #630

## Result

Repository inspection demonstrated one bounded gap: generic non-Agent-Plugin Capability Passports could classify a Skill/Tool but could not identify an exact executable release with immutable provenance comparable to the existing Agent Plugin observation path.

The smallest convergence is to extend the existing Capability Passport with an optional closed `implementation_provenance` object.

## Reused vocabulary

The contract deliberately reuses existing Agent Plugin observation names where applicable:

```text
package_name
package_version
package_digest
component_id
component_kind
component_ref
observed_at
```

Generic repository/package cases add only the source/release anchors needed outside Agent Plugin packaging:

```text
source_kind
source_ref
repository_ref
commit_ref
content_digest
```

At least one of `commit_ref`, `content_digest`, or `package_digest` is required whenever provenance is supplied.

## Authority boundary

This data identifies the artifact/release reviewed or observed. It does not discover, install, adopt, bind, admit, activate, execute, authorize or qualify that artifact.

```text
same Capability != same release
new release != new Capability by default
digest known != safe
provenance recorded != binding selected
binding selected != dependency adopted
installed != approved
activated != task-authorized
runtime success != Evidence
```

## Existing owners retained

- Capability Passport: uniform governed capability classification plus optional exact artifact provenance.
- Skill Manifest: Skill-oriented declaration/admission lifecycle.
- Agent Plugin loader: runtime/package observation and normalization.
- Capability Slots/bindings: I3 concern; not promoted here.
- Execution Admission: sole task/run legitimacy seam.
- H: source/adapter qualification owner.

No parallel implementation registry is introduced.
