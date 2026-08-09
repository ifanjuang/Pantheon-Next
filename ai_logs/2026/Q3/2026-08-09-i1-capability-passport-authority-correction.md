# 2026-08-09 — I1 Capability / Passport authority correction

Parent: #620
Correction: #628

## Finding

After merging the first I1 slice, authority verification found that the candidate `CAPABILITY_REGISTRY.md` had been made stricter than stronger repository authority.

Current active support doctrine and executable referents establish:

- `UNIFORM_CAPABILITY_GOVERNANCE.md`: a Skill/Tool/module can be governed as a Capability through one uniform Passport;
- `schemas/capability_passport.schema.yaml`: `capability.primitive` includes `skill`;
- merged #573 generalized the Passport deliberately to non-MCP Skill capabilities.

The earlier I1 assertion `Capability != Skill` was therefore too broad.

## Corrected model

```text
Capability Slot != Capability
Capability Slot = abstract replaceable function / binding target

Capability = governed unit under the Capability Passport
Skill / Tool / Prompt / Resource may be Capability primitives
Capability Passport != runtime binding
valid / discovered / installed != admitted != task-authorized
```

`workflow_manifest.skill_manifest_ref` remains an explicit Skill admission/reference link. It does not by itself prove a separate abstract Capability object above every Skill.

## Change

- align candidate Capability Registry wording with active Passport doctrine;
- replace the over-broad CI guard with Passport/Slot/admission boundary checks;
- preserve task authorization in Task Contract / Execution Admission;
- introduce no schema or runtime owner.

## Process lesson

Authority class must be checked before promoting a candidate-document interpretation. Candidate registry prose cannot override active support doctrine plus an executable schema referent.
