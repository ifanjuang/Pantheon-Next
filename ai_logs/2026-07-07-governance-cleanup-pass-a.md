# 2026-07-07 — Nettoyage gouvernance, passe A : suppressions mécaniques

## Intervention

Exécution de la passe A du plan de nettoyage approuvé (ampleur standard ; suppression + log de mapping ; les 46+ lignes ARBITRAGE restent intouchées sur décision du mainteneur). 61 documents supprimés ; texte intégral dans l'historique git.

## Pierres tombales obsolètes supprimées (17)

Chaque fichier portait `Status: obsolete — superseded/merged` et pointait déjà son successeur ; le registre `authority/OBSOLETE_AND_ABSENT_INDEX.md` conserve leurs lignes annotées `(removed; git history)`.

- `docs/governance/CHANGELOG_ADDENDUM_EVIDENCE_TOPOLOGY_SCHEMA_D2.md`
- `docs/governance/EPISTEMIC_CONTROL.md`
- `docs/governance/EPISTEMIC_CONTROL_PROPAGATION.md`
- `docs/governance/EVIDENCE_TOPOLOGY_BRIDGES.md`
- `docs/governance/EVIDENCE_TOPOLOGY_CHECKLIST.md`
- `docs/governance/EVIDENCE_TOPOLOGY_GATE.md`
- `docs/governance/EVIDENCE_TOPOLOGY_RECONCILIATION.md`
- `docs/governance/EVIDENCE_TOPOLOGY_ROADMAP.md`
- `docs/governance/EVIDENCE_TOPOLOGY_SCHEMA_CANDIDATE.md`
- `docs/governance/EXTERNAL_RUNTIME_OPTIONS.md`
- `docs/governance/MEMORY_EVENT_SCHEMA.md`
- `docs/governance/MODEL_ROUTING_POLICY.md`
- `docs/governance/OPENWEBUI_DOMAIN_MAPPING.md`
- `docs/governance/OPENWEBUI_PLUGIN_POLICY.md`
- `docs/governance/ROLE_SIGNAL_PROFILES.md`
- `docs/governance/ROUTING_FOUNDATION.md`
- `docs/governance/WORKFLOW_ADAPTATION.md`

## Reviews externes one-shot supprimées (36)

Distillats déjà intégrés à la doctrine ; `reference_reviews/README.md` devient la règle du répertoire et porte l'**index synthétique de retrait** (demande du mainteneur, 2026-07-07) : une ligne par review — outil, capacité abstraite, binding Hermès candidat, statut distilled/to review/superseded, document doctrinal cible, intérêt potentiel, risque principal, mention « removed; git history ».

- `docs/governance/reference_reviews/2026-06-06-truememory-memory-patterns.md`
- `docs/governance/reference_reviews/AGENTCANVAS_TRACE_VISUALIZATION.md`
- `docs/governance/reference_reviews/AGENTOS.md`
- `docs/governance/reference_reviews/AGENTVISION_VISUAL_EVIDENCE_ADAPTER.md`
- `docs/governance/reference_reviews/ASSERT.md`
- `docs/governance/reference_reviews/AUTOTELIC_AGENCY_GOVERNANCE_REVIEW.md`
- `docs/governance/reference_reviews/BFL_OPENAI_IMAGE_PROXY_REVIEW.md`
- `docs/governance/reference_reviews/COGNICORE_RUNTIME_REVIEW.md`
- `docs/governance/reference_reviews/CRAWLBERG_REFERENCE_REVIEW.md`
- `docs/governance/reference_reviews/DCODE_AGENT_KIT_HERMES_SKILL_SCAFFOLDING_REVIEW.md`
- `docs/governance/reference_reviews/DIFY_LANGFLOW_AGENTIC_BUILDER_REVIEW.md`
- `docs/governance/reference_reviews/DIRECTORY_MCP.md`
- `docs/governance/reference_reviews/DLTHUB_CANONICAL_TEXT_TO_SQL.md`
- `docs/governance/reference_reviews/ELT_REFERENCE_REVIEW.md`
- `docs/governance/reference_reviews/FLEXIBLE_GRAPHRAG_REVIEW.md`
- `docs/governance/reference_reviews/FOREVER_AI_COMPONENTS_CARD_AFFORDANCE_REVIEW.md`
- `docs/governance/reference_reviews/FUTURE_AGI.md`
- `docs/governance/reference_reviews/HERMES_AGENT_V018_CARD_AND_ADAPTER_PROJECTION.md`
- `docs/governance/reference_reviews/HERMES_AGENT_V018_RELEASE_REVIEW.md`
- `docs/governance/reference_reviews/HERMES_MOA_REVIEW.md`
- `docs/governance/reference_reviews/LANGFUSE_DASHBOARD_LINK_CARD_CANDIDATE.md`
- `docs/governance/reference_reviews/LANGFUSE_HERMES_INSTALLATION_PACKAGE_CANDIDATE.md`
- `docs/governance/reference_reviews/LANGGRAPH.md`
- `docs/governance/reference_reviews/NANGO.md`
- `docs/governance/reference_reviews/ODYSSEUS_REFERENCE_DISTILLATION.md`
- `docs/governance/reference_reviews/PLANO_AI_DATAPLANE_REVIEW.md`
- `docs/governance/reference_reviews/PYTHIA_GOVERNANCE_STATE_REVIEW.md`
- `docs/governance/reference_reviews/QUARKDOWN.md`
- `docs/governance/reference_reviews/RAG_MADE_SIMPLE_REFERENCE_REVIEW.md`
- `docs/governance/reference_reviews/ROW_BOT_4_2_0_REVIEW.md`
- `docs/governance/reference_reviews/SELF_INSPECT_MCP.md`
- `docs/governance/reference_reviews/SKILL_FORGE_RUNTIMES.md`
- `docs/governance/reference_reviews/SKILL_GOVERNANCE.md`
- `docs/governance/reference_reviews/SOUL_MD_HERMES_PROFILE.md`
- `docs/governance/reference_reviews/SUB_AGENT_MCP.md`
- `docs/governance/reference_reviews/UNDERSTAND_ANYTHING.md`

## Réconciliations one-shot supprimées (8)

Travail accompli ; une ligne de trace par document dans `STATUS.md` (section « Historical reconciliations »).

- `docs/governance/CONCEPTUAL_STABILIZATION.md`
- `docs/governance/DATA_PLATFORM_RECONCILIATION.md`
- `docs/governance/GOVERNANCE_LINKAGE_RECONCILIATION.md`
- `docs/governance/OPEN_BRANCH_LANDING_PLAN.md`
- `docs/governance/OPEN_PR_RECONCILIATION.md`
- `docs/governance/POST_CONSOLIDATION_HANDOFF.md`
- `docs/governance/REPOSITORY_CONSOLIDATION_LANDING_PLAN.md`
- `docs/governance/STATUS_SPINE_RECONCILIATION.md`

## Références réécrites

Toutes les références internes vers les fichiers supprimés ont été converties en mention nominale `(removed; git history)` ou reroutées vers le document consolidé (`EVIDENCE_TOPOLOGY.md` pour GATE/CHECKLIST dans les README racine FR/EN). Guards verts en full-tree après la passe.
