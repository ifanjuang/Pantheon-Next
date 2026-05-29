# 2026-05-29 - Rites governance layer

## Summary

Added a documentation-level Rites layer for Pantheon Next.

The change introduces rites as shared governance procedures used to coordinate Pantheon Roles around recurring methodological tensions.

## Files added

- `docs/governance/rites/README.md`
- `docs/governance/rites/_TEMPLATE_RITE.md`
- `docs/governance/rites/RITE_DIVERGENCE_CONTROLEE.md`
- `docs/governance/rites/AUTOCRITIQUE_CONTRADICTOIRE.md`
- `docs/governance/rites/CONCORDANCE_DES_SOURCES.md`
- `docs/governance/rites/PREMISSES_CACHEES.md`
- `docs/governance/rites/REFONDATION_DE_SESSION.md`

## Reason

The external divergent-ideation pattern reviewed from `uditakhourii/adhd` is better modeled as a shared rite than as a new Pantheon Role.

A new god would duplicate ATHENA, HEPHAISTOS, THEMIS, ARGOS, APOLLO and ZEUS responsibilities.

A rite preserves role separation while making the method reusable.

## Doctrine

Rites are shared governance methods.

They are not agents.

They are not Pantheon Roles.

They are not Hermes profiles.

They are not a runtime.

```text
Roles judge.
Rites coordinate.
Task Contracts bound.
Evidence Packs prove.
ZEUS states procedure.
The human decides.
```

## Boundary

This is documentation-level governance only.

It does not implement:

- runtime;
- scheduler;
- queue;
- provider router;
- tool runtime;
- hidden role debate;
- autonomous workflow;
- Hermes skill installation;
- OpenWebUI plugin;
- automatic approval;
- automatic memory promotion.

## Risk and limitation

The change creates a new conceptual layer.

The main risk is terminology drift if rites are later treated as executable workflows.

The mitigation is explicit boundary wording in every rite file and in the rites index.

No schemas, tests, operations files, Docker files, environment files or protected configuration files were changed in this pass.
