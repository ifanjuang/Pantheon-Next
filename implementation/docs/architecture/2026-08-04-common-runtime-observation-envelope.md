# Common runtime observation envelope

Date: 2026-08-04

Status: implementation note — non-authoritative.

## Verified overlap

The local and network document-runtime observers already emit the same three factual dimensions for every observation:

```text
source
observation_source
observed_at
```

They now validate these dimensions through `RuntimeObservation` and preserve every remaining field as adapter-owned payload.

## Deliberately not shared

The following vocabularies remain local to their adapters and probes:

- reachability status;
- readiness status;
- health endpoint status;
- installation status;
- selection status;
- runtime API or CLI status;
- extraction-quality posture;
- compatibility claims.

No universal `started/progress/completed/failed` ontology is introduced. A document-source binding observation, a PDP readiness probe, a Docling health probe and a Hermes inventory observation do not carry the same semantics merely because they are observations.

## Compatibility

Both `/documents/observations` bindings retain their existing flat JSON payloads. The common envelope is an internal implementation primitive, not a new API object, persistence table or governed identity.

External protocol paths such as Hermes `/v1/skills` and Pantheon policy `/v1/meta` remain external adapter contracts. They are not internal Pantheon route identities.

## Non-equivalences

```text
reported != observed
observed != true
reachable != healthy
healthy != safe
installed != approved
listed != activated
activated != task_authorized
observation != activation decision
runtime success != Evidence
```

The envelope does not install, activate, authorize, schedule, dispatch, route providers, promote memory or admit Evidence.
