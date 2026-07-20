# Historical Migration Playbook

Status: obsolete — completed migration procedure — obsolete.
Boundary profile: active_support_doctrine.

This file preserves the outcome of the completed governance migration without creating a dependency on a retired repository.

Pantheon Next is now self-contained and canonical for its governance Markdown, schemas, validators, status maps and bounded read-only surfaces. No active workflow may fetch, compare, re-vendor or recover doctrine from the retired predecessor.

## Closed outcome

The migration applied these durable rules:

```text
distill governance value; never bulk-copy runtime;
rewrite execution assumptions as external-runtime boundaries;
remove obsolete or contradictory material;
preserve evidence, approval and memory distinctions;
record material interventions in ai_logs/;
make Pantheon Next authoritative after review.
```

Inherited doctrine is now maintained directly in Pantheon Next. Its historical provenance remains available in git history and dated validation logs, but those traces are not live dependencies or sources of authority.

## Current rule

New governance work starts from the current Pantheon Next authority and status spine:

```text
docs/governance/STATUS.md
docs/governance/WHAT_RUNS.md
docs/governance/AUTHORITY_INDEX.md
docs/governance/MODULES.md
docs/governance/README.md
CONTRIBUTING.md
```

If an old trace conflicts with these files, the current authority and status spine wins.

## Removed dependency

The repository no longer carries or requires a full predecessor snapshot in its current tree. Removing the snapshot from the current tree does not rewrite git history; earlier provenance and migration decisions remain recoverable from prior commits.

Current CI checks repository independence directly. It does not validate historical migration tables or require this playbook as part of the active governance baseline.

## Boundary

```text
historical trace != active doctrine
historical source != live dependency
inherited wording != runtime adoption
migration complete != production activation
```

This playbook is retained only as an obsolete historical record and to preserve older links. It must not be used to restart migration work, and no active workflow depends on its presence.
