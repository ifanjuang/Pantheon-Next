# Hermes Distribution Lock

Status: template-only composition contract — no installer, runtime or authority.

This directory defines how an operator or implementation repository may record one reproducible composition of Pantheon artifacts for an external Hermes installation.

```text
distribution-lock.schema.yaml   validation contract
distribution-lock.example.yaml  fictional example only
```

The lock records:

- reviewed `Pantheon-Next` and `pantheon-mvp` source revisions;
- an exact external Hermes runtime version target;
- the installed Hermes artifact digest when it has actually been observed;
- independently reviewable component paths and exact content digests;
- which components are required or optional;
- the abstract capabilities each component exposes;
- the acceptance checks required for the composition;
- factual installation and acceptance observations.

Repository refs provide review provenance. They are not sufficient to identify a composition stored inside one of those repositories because the final commit cannot contain its own future SHA. Exact component identity is therefore established by `content_digest`.

It does not merge the components into a new runtime or authority layer.

```text
composition pinned != components installed
components installed != binding activated
acceptance passed != task authorized
runtime success != accepted result
runtime output != Evidence
```

## Digest contract

Every declared component has a `digest_mode` and `content_digest`.

For `digest_mode: file`:

```text
sha256(raw file bytes)
```

For `digest_mode: tree`:

1. reject symbolic links;
2. enumerate every regular file recursively;
3. sort paths by their POSIX relative path;
4. compute the SHA-256 hexadecimal digest of each file's raw bytes;
5. append one UTF-8 record per file:

```text
<relative-path>\0<file-sha256-hex>\n
```

6. compute SHA-256 over the concatenated records.

The digest covers source content only. It does not indicate installation, compatibility, safety, activation or task authorization.

## Runtime artifact

`source_pins.hermes_runtime.version` is an exact version, not a range or wildcard. `artifact_digest` remains `null` while the lock is only a candidate. A lock marked `observed` or `qualified` must contain the SHA-256 digest of the runtime artifact actually observed by the operator.

```text
reviewed runtime version != installed runtime
artifact observed != binding activated
```

## Ownership

`Pantheon-Next` owns this declarative template contract. A candidate operational lock belongs with the implementation or deployment material that it describes, normally in `pantheon-mvp` or an external operator repository.

Each component retains its owner and lifecycle. A dashboard update does not require treating the run binding as changed, and a skill may remain absent even when the required execution bridge is installed.

## Validation

A consumer should validate the lock against the schema, resolve every declared path inside the reviewed checkouts, verify every content digest, verify route and plugin contracts, and run one composed read-only acceptance scenario.

A check result is a technical observation only. Human activation and per-task admission remain separate decisions.
