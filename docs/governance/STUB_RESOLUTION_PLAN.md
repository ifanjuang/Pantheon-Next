# Stub resolution plan

Status: validation-only — decision note for the maintainer. It deletes nothing and promotes nothing; each row is a recommendation awaiting an explicit decision.

Thirteen governance documents are stubs ("à migrer depuis Pantheon-OS" or partial). Per the migration policy of `CLAUDE.md`, migration only happens deliberately. A stub without a decision is debt; this note proposes one disposition per stub.

| Stub | Lines | Recommendation | Rationale (one line) |
|---|---|---|---|
| `EPISTEMIC_CONTROL.md` | 27 | **migrate** (one consolidated doc with PROPAGATION) | Epistemic control is core to the proof discipline; worth a real migration pass. |
| `EPISTEMIC_CONTROL_PROPAGATION.md` | 26 | **merge into EPISTEMIC_CONTROL** | Same subject; two stubs for one concept is sprawl. |
| `EXTERNAL_TOOLS_POLICY.md` | 101 | **keep as is** (partial) | Already partially implemented; completes naturally via reference reviews. |
| `EXTERNAL_RUNTIME_OPTIONS.md` | 26 | **obsolete** | Superseded by `EXTERNAL_RUNTIME_MEMORY_ADAPTERS.md` and the reference reviews. |
| `MODEL_ROUTING_POLICY.md` | 26 | **obsolete** | Provider routing is a forbidden Pantheon capability; routing lives in Hermes. A policy doc would only restate the boundary, which `BOUNDARY_STANDARD.md` now owns. |
| `ROUTING_FOUNDATION.md` | 26 | **obsolete** | Same rationale as MODEL_ROUTING_POLICY. |
| `OPENWEBUI_DOMAIN_MAPPING.md` | 27 | **merge into OPENWEBUI_INTEGRATION.md** | One OpenWebUI boundary doc is enough until a real mapping exists. |
| `OPENWEBUI_PLUGIN_POLICY.md` | 27 | **merge into OPENWEBUI_INTEGRATION.md** | Same; plugin policy is already stated there and in the runtime policy. |
| `ROLE_SIGNAL_PROFILES.md` | 26 | **merge into ROLE_SIGNALS.md** | Profiles are an annex of the signals doctrine. |
| `SKILL_LIFECYCLE.md` | 19 | **migrate** | Skill admission is now load-bearing (SkillsGate, capability registry); the lifecycle deserves a real doc. |
| `WORKFLOW_ADAPTATION.md` | 19 | **merge into WORKFLOW_LIFECYCLE.md** | Adaptation is a lifecycle stage, not a separate doctrine. |
| `MEMORY_EVENT_SCHEMA.md` | — | **obsolete** | Superseded by the E6 schema baseline (`register_candidate`, `answer_status`). |
| `MIGRATION_PLAYBOOK.md` | — | **keep** (mandatory CI file) | Still the governing process for any future migration. |

## Proposed execution once decided

One small PR per disposition class: (a) the two real migrations, (b) the four merges, (c) the obsolete markings. Each PR updates `AUTHORITY_INDEX.md` in the separate reindex pass per the indexing rule.

## Boundary

Decision note only. No stub was deleted, merged or migrated by this document.
