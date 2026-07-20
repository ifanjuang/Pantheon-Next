# ai_logs — Index

Status: validation-only / generated navigation index over the AI intervention logs.

Every significant AI intervention adds an `ai_logs/` entry (see `CLAUDE.md`). This
table is a read-only map of them, newest first. It is **generated** — do not edit by
hand; run `python3 .github/scripts/generate_ai_logs_index.py` after adding a log.

## Convention going forward

```text
New logs are dated (YYYY-MM-DD-<slug>.md) and, once the quarterly archive lands,
grouped as ai_logs/<year>/Q<n>/. The mass move of the existing flat logs is a
separate follow-up PR so its diff stays readable and reversible; this index already
covers the flat files in the meantime.
```

Total indexed entries: **661**.

| Date | Log | Subject |
|---|---|---|
| — | `LOG_FORMAT.md` | AI Log Format |
| 2026-07-20 | `2026-07-20-retire-predecessor-dependency.md` | Retire the predecessor repository dependency |
| 2026-07-20 | `2026-07-20-final-active-reference-cleanup.md` | Final active-reference cleanup |
| 2026-07-20 | `2026-07-20-document-runtime-reconciliation.md` | Document architecture and runtime reconciliation |
| 2026-07-20 | `2026-07-20-document-knowledge-runtime-reconciliation.md` | Reconcile the external Document to Knowledge runtime |
| 2026-07-20 | `2026-07-20-document-knowledge-contract.md` | Add the Document to Knowledge slice contract |
| 2026-07-19 | `2026-07-19-native-hermes-multi-model-deliberation.md` | Native Hermes multi-model deliberation candidate |
| 2026-07-19 | `2026-07-19-document-and-knowledge-organization.md` | Architecture document and knowledge organization decision |
| 2026-07-18 | `2026-07-18-work-issue-delegated-merge.md` | Work Issue and delegated merge model |
| 2026-07-16 | `2026-07-16-hermes-single-renderer-preview.md` | AI log — Single renderer for Hermes live and public demo |
| 2026-07-16 | `2026-07-16-hermes-dashboard-shared-design.md` | Hermes dashboard shared design |
| 2026-07-16 | `2026-07-16-hermes-dashboard-operator-language.md` | AI log — Hermes dashboard operator language and demo fixture repair |
| 2026-07-16 | `2026-07-16-hermes-dashboard-demo-live-adapter.md` | AI log — Hermes dashboard demo/live adapter |
| 2026-07-16 | `2026-07-16-hermes-bounded-night-operation-controls.md` | Hermes bounded night-operation controls |
| 2026-07-15 | `2026-07-15-shadow-reconstruction-memory-integrity.md` | Shadow reconstruction memory-integrity review |
| 2026-07-15 | `2026-07-15-mcp-consultation-contract.md` | MCP consultation contract and bounded architecture explanations |
| 2026-07-15 | `2026-07-15-mcp-authority-resolution-wiki.md` | AI log — MCP authority resolution and governance wiki |
| 2026-07-15 | `2026-07-15-ifixai-placement-review.md` | iFixAi external placement review |
| 2026-07-15 | `2026-07-15-honest-packaging-release-contract.md` | AI log — honest packaging and release contract |
| 2026-07-15 | `2026-07-15-hermes-pantheon-modules-dashboard.md` | Hermes Pantheon Modules dashboard plugin |
| 2026-07-15 | `2026-07-15-hermes-native-mcp-wiki-config.md` | Hermes-native MCP policy/wiki configuration |
| 2026-07-15 | `2026-07-15-hermes-governed-night-operations.md` | Hermes governed night operations |
| 2026-07-15 | `2026-07-15-governance-doctor-fail-closed.md` | Governance Doctor fail-closed contract |
| 2026-07-14 | `2026-07-14-opik-hermes-uplink-external-placement.md` | Opik and Hermes Uplink external placement |
| 2026-07-14 | `2026-07-14-langgraph-agent-stack-placement.md` | LangGraph Agent Stack external placement |
| 2026-07-13 | `2026-07-13-strict-mcp-evidence-validation.md` | Strict MCP evidence validation |
| 2026-07-13 | `2026-07-13-mvp-decision-schema-reconciliation.md` | 2026-07-13 — MVP decision vocabulary and schema reconciliation |
| 2026-07-13 | `2026-07-13-cockpit-consolidation-roadmap.md` | Cockpit consolidation roadmap launch |
| 2026-07-13 | `2026-07-13-card-stack-a1-reconciliation.md` | Card Stack A1 reconciliation |
| 2026-07-12 | `2026-07-12-provisioner-handoff-contracts.md` | AI intervention trace — provisioner handoff contracts |
| 2026-07-12 | `2026-07-12-handoff-human-decision-contract.md` | AI intervention trace — handoff human decision contract |
| 2026-07-12 | `2026-07-12-handoff-decision-hardening.md` | AI intervention trace — handoff decision hardening |
| 2026-07-12 | `2026-07-12-governance-object-relationship-map-audit.md` | Targeted audit of Governance Object Relationship Map |
| 2026-07-12 | `2026-07-12-card-stack-model-reconciliation.md` | Card Stack Model reconciliation |
| 2026-07-11 | `2026-07-11-pantheon-graph-model.md` | Pantheon graph model intervention |
| 2026-07-11 | `2026-07-11-install-catalog-swiper-prototype.md` | Install catalog Swiper prototype trace |
| 2026-07-11 | `2026-07-11-declarative-capability-manifests.md` | AI intervention trace — declarative capability manifests |
| 2026-07-11 | `2026-07-11-catalog-validation-loader-candidate.md` | AI intervention trace — catalog validation, loader and candidate |
| 2026-07-11 | `2026-07-11-capability-resource-preset-model.md` | AI intervention trace — reduced catalog model |
| 2026-07-10 | `2026-07-10-what-runs-mvp-vertical-binding.md` | 2026-07-10 — WHAT_RUNS entry for MVP Vertical binding |
| 2026-07-10 | `2026-07-10-mvp-loop-first-demonstration.md` | Première démonstration complète de la boucle gouvernée (blocs 1-3) |
| 2026-07-10 | `2026-07-10-align-mvp-repo-name.md` | 2026-07-10 — Align MVP binding repository name |
| 2026-07-09 | `2026-07-09-resource-dashboard-boundary-profile-fix.md` | Resource dashboard boundary profile fix |
| 2026-07-09 | `2026-07-09-pantheon-mvp-vertical-binding-review.md` | 2026-07-09 — Pantheon MVP Vertical binding review |
| 2026-07-09 | `2026-07-09-mvp-vertical-review-cleanup.md` | 2026-07-09 — MVP Vertical reference review cleanup |
| 2026-07-09 | `2026-07-09-governed-resource-dashboard-model.md` | 2026-07-09 — Governed Resource Dashboard model |
| 2026-07-08 | `2026-07-08-template-status-guard-repair.md` | Template status guard repair |
| 2026-07-08 | `2026-07-08-template-model-and-prompt-templates.md` | Template model and prompt templates |
| 2026-07-08 | `2026-07-08-status-runtime-read-path.md` | 2026-07-08 — Status runtime read-path reconciliation |
| 2026-07-08 | `2026-07-08-status-header-rules-integration.md` | Status header rules integration |
| 2026-07-08 | `2026-07-08-status-header-rules-dedup.md` | Status header rules dedup pass |
| 2026-07-08 | `2026-07-08-static-pages-runtime-language.md` | 2026-07-08 — Static pages runtime-language pass |
| 2026-07-08 | `2026-07-08-skill-watchlist-finding-unknowns-vercel-skills.md` | Skill watchlist: finding-unknowns-skills and vercel-labs/skills records |
| 2026-07-08 | `2026-07-08-readme-entry-refactor.md` | 2026-07-08 — README entry refactor |
| 2026-07-08 | `2026-07-08-public-cockpit-wording-rule.md` | 2026-07-08 — Public cockpit wording rule |
| 2026-07-08 | `2026-07-08-non-equivalence-rules-dedup.md` | Non-equivalence rules dedup pass |
| 2026-07-08 | `2026-07-08-mvp-vocabulary-invariants.md` | AI log — MVP vocabulary and invariants tightening |
| 2026-07-08 | `2026-07-08-mvp-validation-report-shape.md` | AI log — MVP validation report shape |
| 2026-07-08 | `2026-07-08-mvp-validation-plan.md` | AI log — MVP validation plan |
| 2026-07-08 | `2026-07-08-mvp-prevalidator-consolidation.md` | AI log — MVP prevalidator consolidation |
| 2026-07-08 | `2026-07-08-mvp-minimal-schema-candidates.md` | AI log — MVP minimal schema candidates |
| 2026-07-08 | `2026-07-08-mvp-local-validator.md` | AI log — MVP local validator |
| 2026-07-08 | `2026-07-08-mvp-fixture-schema-alignment.md` | AI log — MVP fixture schema alignment |
| 2026-07-08 | `2026-07-08-mvp-fixture-guard-repair-resolved.md` | 2026-07-08 — Resolved MVP fixture guard repair |
| 2026-07-08 | `2026-07-08-mvp-deliberate-failing-fixture.md` | AI log — MVP deliberate failing fixture |
| 2026-07-08 | `2026-07-08-modules-truncation-repair-from-hermes-pr.md` | Modules truncation repair from Hermes runtime governance PR |
| 2026-07-08 | `2026-07-08-issue-183-public-cockpit-comment.md` | 2026-07-08 — Issue #183 public cockpit wording comment |
| 2026-07-08 | `2026-07-08-install-module-catalog.md` | Install module catalog grammar |
| 2026-07-08 | `2026-07-08-hosting-arbitration-option-a.md` | 2026-07-08 — Arbitrage d'hébergement du code exécutable : Option A |
| 2026-07-08 | `2026-07-08-hermes-runtime-governance.md` | Hermes runtime governance |
| 2026-07-08 | `2026-07-08-hermes-installation-assistance.md` | Hermes installation assistance |
| 2026-07-08 | `2026-07-08-guard-readonly-verification.md` | 2026-07-08 — Guard read-only verification |
| 2026-07-08 | `2026-07-08-evidence-pack-boundary-dedup.md` | 2026-07-08 — Evidence Pack boundary dedup |
| 2026-07-08 | `2026-07-08-doctrine-boundary-dedup.md` | 2026-07-08 — Doctrine boundary dedup pass |
| 2026-07-08 | `2026-07-08-boundary-profiles-dedup.md` | Boundary profiles dedup pass |
| 2026-07-08 | `2026-07-08-awesome-claude-code-watchlist-distillation.md` | awesome-claude-code watchlist distillation |
| 2026-07-08 | `2026-07-08-authority-protected-path-alignment.md` | 2026-07-08 — Authority protected-path alignment |
| 2026-07-08 | `2026-07-08-ai-log-format-dedup.md` | AI log format dedup pass |
| 2026-07-08 | `2026-07-08-absent-dashboard-boundary-pr.md` | Absent dashboard boundary reconciliation |
| 2026-07-07 | `2026-07-07-mvp-vertical-yaml-fixture.md` | AI log — MVP vertical YAML fixture |
| 2026-07-07 | `2026-07-07-mvp-vertical-implementation-plan.md` | 2026-07-07 — Plan d'implémentation du vertical MVP |
| 2026-07-07 | `2026-07-07-mvp-object-shape-reconciliation.md` | AI log — MVP object shape reconciliation |
| 2026-07-07 | `2026-07-07-mvp-governed-task-loop-plan.md` | 2026-07-07 — Plan MVP : mvp-governed-task-loop |
| 2026-07-07 | `2026-07-07-governance-cleanup-pass-b.md` | 2026-07-07 — Nettoyage gouvernance, passe B : absorption des clusters |
| 2026-07-07 | `2026-07-07-governance-cleanup-pass-a.md` | 2026-07-07 — Nettoyage gouvernance, passe A : suppressions mécaniques |
| 2026-07-06 | `2026-07-06-card-stack-knowledge-scope-fix.md` | Card Stack Knowledge Scope Fix |
| 2026-07-06 | `2026-07-06-card-stack-hardening-note.md` | Card Stack Hardening Note |
| 2026-07-05 | `2026-07-05_obsolete_absent_index_population.md` | AI Log — Obsolete and Absent Index Population (first migration group) |
| 2026-07-05 | `2026-07-05_negation_vocabulary_and_branch_protection.md` | AI Log — Negation Vocabulary Extension and Branch Protection Priority |
| 2026-07-05 | `2026-07-05_loop_governance_index_row_insertion.md` | AI Log — Loop Governance Model: Real Authority Index Row (PR #282) |
| 2026-07-05 | `2026-07-05_hermes_code_hosting_boundary_proposal.md` | AI Log — Hermes Code Hosting Boundary Proposal |
| 2026-07-05 | `2026-07-05_coverage_checker_subindex_extension.md` | AI Log — Coverage Checker Sub-Index Extension (PR C) |
| 2026-07-05 | `2026-07-05_coverage_check_row_tightening.md` | AI Log — Coverage Check Tightening: Table Rows Only |
| 2026-07-05 | `2026-07-05_authority_subindex_reshelving.md` | AI Log — Authority Sub-Index Re-Shelving After Review |
| 2026-07-05 | `2026-07-05_authority_sub_index_skeletons.md` | AI Log — Authority Sub-Index Skeletons (PR B) |
| 2026-07-05 | `2026-07-05_authority_index_row_migration_architecture_external.md` | AI Log — Authority Index Row Migration: Architecture + External References (PR C + PR D) |
| 2026-07-05 | `2026-07-05_authority_index_full_decomposition.md` | AI Log — Authority Index Full Decomposition (checker extension + PR D/E) |
| 2026-07-05 | `2026-07-05-loop-governance-model.md` | 2026-07-05 — Loop governance model distillation |
| 2026-07-05 | `2026-07-05-hermes-loop-candidate-templates.md` | 2026-07-05 — Hermes loop candidate templates |
| 2026-07-05 | `2026-07-05-guard-debt-purge-and-full-tree-ci.md` | 2026-07-05 — Purge de la dette de guards et passage de la CI en full-tree |
| 2026-07-05 | `2026-07-05-crawlberg-reference-review.md` | 2026-07-05 — Crawlberg reference review |
| 2026-07-05 | `2026-07-05-control-plane-boundary-revit-first-contract.md` | AI log — Control-plane hardening and Revit first sandbox contract |
| 2026-07-05 | `2026-07-05-control-plane-bindings-revit-sandbox.md` | AI log — Control plane, Hermes bindings and Revit sandbox exception |
| 2026-07-05 | `2026-07-05-authority-subindex-control-plane-bindings-revit.md` | AI log — Authority sub-index rows for control plane, Hermes bindings and Revit sandbox |
| 2026-07-04 | `2026-07-04_revit_v0_capability_registry.md` | AI Log — Revit V0 Capability Registry Slice |
| 2026-07-04 | `2026-07-04_revit_v0_authority_index_fix.md` | AI log — Revit V0 authority index fix |
| 2026-07-04 | `2026-07-04_revit_free_exploration_v0.md` | AI Log — Revit Free Exploration V0 |
| 2026-07-04 | `2026-07-04_revit_2027_prototype_plan.md` | AI Log — Revit 2027 Prototype Plan |
| 2026-07-04 | `2026-07-04_post_pr_cleanup_external_run_issue.md` | AI log — post-PR cleanup and external run issue |
| 2026-07-04 | `2026-07-04_maintainer_release_license_checklist.md` | AI log — maintainer release and licence checklist |
| 2026-07-04 | `2026-07-04_external_live_run_protocol.md` | AI log — external live run protocol |
| 2026-07-04 | `2026-07-04_authority_index_decomposition_plan_review.md` | AI Log — Authority Index Decomposition Plan Review (PR #276) |
| 2026-07-04 | `2026-07-04_authority_index_decomposition_plan.md` | AI Log — Authority Index Decomposition Plan |
| 2026-07-04 | `2026-07-04-governed-method-standard.md` | AI Log — Governed Method Standard |
| 2026-07-04 | `2026-07-04-governed-autonomy-gradient.md` | AI Log — Governed Autonomy Gradient |
| 2026-07-04 | `2026-07-04-control-ux-density-pass.md` | AI Log — Pantheon Control UX density pass |
| 2026-07-04 | `2026-07-04-control-revit-connector-status.md` | AI Log — Revit connector status in Pantheon Control |
| 2026-07-04 | `2026-07-04-control-consolidation-pass.md` | AI Log — Pantheon Control consolidation pass |
| 2026-07-04 | `2026-07-04-analyse-complete-repository.md` | 2026-07-04 — Analyse complète du dépôt (audit externe) |
| 2026-07-03 | `2026-07-03_landing_path_note.md` | AI log — landing path note |
| 2026-07-03 | `2026-07-03_landing_intro_liberal_method.md` | AI log — landing intro liberal-method repositioning |
| 2026-07-03 | `2026-07-03-runtime-health-main-landing.md` | AI log — runtime-health cockpit main landing |
| 2026-07-03 | `2026-07-03-pr266-authority-index-fix.md` | AI log — PR #266 authority index fix |
| 2026-07-03 | `2026-07-03-post-claude-cleanup-step1.md` | AI log — post-Claude cleanup step 1 |
| 2026-07-03 | `2026-07-03-pantheon-control-html-editorial-audit.md` | AI Log — Pantheon Control HTML editorial audit |
| 2026-07-03 | `2026-07-03-openwebui-template-primitive-map.md` | AI log — map the OpenWebUI template classes to real primitives |
| 2026-07-03 | `2026-07-03-open-branch-roadmap-update.md` | AI log — open branch landing roadmap update |
| 2026-07-03 | `2026-07-03-hermes-v018-card-adapter-projection.md` | AI Log — Hermes v0.18 card and adapter projection |
| 2026-07-03 | `2026-07-03-hermes-page-agent-integration.md` | AI Log — Hermes Page-Agent Integration Framing |
| 2026-07-03 | `2026-07-03-hermes-agent-v018-release-review.md` | AI Log — Hermes Agent v0.18.0 release boundary review |
| 2026-07-03 | `2026-07-03-external-reference-prs-260-265.md` | AI log — external-reference PRs #260 and #265 |
| 2026-07-03 | `2026-07-03-control-visible-pages-editorial-pass.md` | AI Log — Pantheon Control visible pages editorial pass |
| 2026-07-03 | `2026-07-03-control-navigation-infrastructure-cut.md` | AI Log — Pantheon Control navigation and infrastructure cut |
| 2026-07-03 | `2026-07-03-control-modules-usage-page.md` | AI Log — Pantheon Control modules usage page |
| 2026-07-03 | `2026-07-03-control-infrastructure-submenu.md` | AI Log — Pantheon Control infrastructure submenu consolidation |
| 2026-07-03 | `2026-07-03-control-home-tool-qualities.md` | AI Log — Pantheon Control home tool qualities explanation |
| 2026-07-03 | `2026-07-03-control-home-simplified-stack-language.md` | AI Log — Pantheon Control simplified stack language |
| 2026-07-03 | `2026-07-03-control-home-openwebui-hermes-choice.md` | AI Log — Pantheon Control home stack choice explanation |
| 2026-07-03 | `2026-07-03-control-home-nav-cache.md` | AI Log — Pantheon Control home navigation cache refresh |
| 2026-07-03 | `2026-07-03-control-home-manifest.md` | AI Log — Pantheon Control home manifest narrative |
| 2026-07-03 | `2026-07-03-cognicore-runtime-review.md` | 2026-07-03 — CogniCore runtime review |
| 2026-07-03 | `2026-07-03-cognicore-distillation-path.md` | 2026-07-03 — CogniCore distillation path |
| 2026-07-03 | `2026-07-03-close-pr190-first-principles-crawl4ai.md` | AI log — close PR #190 first-principles / Crawl4AI draft |
| 2026-07-03 | `2026-07-03-claude-work-review.md` | AI log — Claude work review |
| 2026-07-03 | `2026-07-03-branch-pr-cleanup-189-190.md` | AI log — branch / PR cleanup for #189 and #190 |
| 2026-07-02 | `2026-07-02-vertical-slice-phase2-bridge.md` | AI log — vertical slice phase-2 bridge (candidate templates) |
| 2026-07-02 | `2026-07-02-vertical-slice-devis-reprise.md` | AI log — governed vertical slice architecture_devis_reprise (B-3 phase 1) |
| 2026-07-02 | `2026-07-02-tripartite-mcp-refusal-docs.md` | AI log — tripartite interface, MCP V0 and refusal fixtures |
| 2026-07-02 | `2026-07-02-pr-259-merged.md` | AI Log — PR #259 merged |
| 2026-07-02 | `2026-07-02-post-consolidation-handoff.md` | AI Log — post-consolidation handoff |
| 2026-07-02 | `2026-07-02-align-openwebui-hermes-upstream.md` | AI log — align templates/configs with upstream OpenWebUI 0.10.2 / Hermes 0.18 / agentskills.io |
| 2026-07-01 | `2026-07-01-version-changelog-realign.md` | AI log — realign VERSION with the CHANGELOG head (B-7) |
| 2026-07-01 | `2026-07-01-referent-rule.md` | AI log — the referent rule (B-5) |
| 2026-07-01 | `2026-07-01-pr-246-landing-plan-update.md` | AI Log — PR #246 landing plan update |
| 2026-07-01 | `2026-07-01-pr-218-protected-review.md` | AI Log — PR #218 protected review |
| 2026-07-01 | `2026-07-01-pr-218-merged.md` | AI Log — PR #218 merged |
| 2026-07-01 | `2026-07-01-pr-217-merged.md` | AI Log — PR #217 merged |
| 2026-07-01 | `2026-07-01-maintainer-actions-tags-pdf-licence.md` | AI Log — maintainer actions for tags, PDF purge and licence |
| 2026-07-01 | `2026-07-01-governed-composition-step-signatures-and-evidence-gate.md` | AI log — governed_composition: complete signatures + conditional evidence gate (#218) |
| 2026-07-01 | `2026-07-01-domain-pack-architecture-move.md` | AI log — execute the architecture domain-pack move (B-4) |
| 2026-07-01 | `2026-07-01-claude-md-mcp-ui-dashboard-alignment.md` | AI log — align CLAUDE.md with the real MCP / UI / dashboard state (B-1) |
| 2026-07-01 | `2026-07-01-bilingual-glossary.md` | AI log — single bilingual glossary EN ↔ FR (B-6) |
| 2026-07-01 | `2026-07-01-base-metier-deversion-pdfs.md` | AI log — de-version base_metier PDFs, keep out of git (B-2, decision c) |
| 2026-07-01 | `2026-07-01-base-metier-architecte-inventory.md` | AI log — inventory of base_metier/architecte/ (B-2, read-only) |
| 2026-07-01 | `2026-07-01-ai-logs-index.md` | AI log — generated ai_logs index (B-8, phase 1) |
| 2026-06-30 | `2026-06-30-what-runs-status-map.md` | AI Log — What Runs status map |
| 2026-06-30 | `2026-06-30-status-spine-reconciliation.md` | AI Log — Status spine reconciliation |
| 2026-06-30 | `2026-06-30-repository-consolidation-landing-plan.md` | AI Log — Repository consolidation landing plan |
| 2026-06-30 | `2026-06-30-pr-239-protected-review.md` | AI Log — PR #239 protected review |
| 2026-06-30 | `2026-06-30-pr-239-merged.md` | AI Log — PR #239 merged |
| 2026-06-30 | `2026-06-30-pr-234-merged.md` | AI Log — PR #234 merged |
| 2026-06-30 | `2026-06-30-open-branch-landing-plan.md` | AI Log — Open branch landing plan |
| 2026-06-30 | `2026-06-30-modules-mcp-alignment.md` | AI Log — MODULES MCP alignment |
| 2026-06-30 | `2026-06-30-method-card-hermes-specialization.md` | AI Log — Method Card Hermes handoff specialization |
| 2026-06-30 | `2026-06-30-mcp-status-after-pr-239.md` | AI Log — MCP status alignment after PR #239 |
| 2026-06-30 | `2026-06-30-fix-runtime-phrase-landing-queue.md` | AI log — unblock CI: reword affirmative "landing queue" |
| 2026-06-30 | `2026-06-30-authority-index-mcp-alignment-applied.md` | AI log — AUTHORITY_INDEX.md MCP alignment applied |
| 2026-06-30 | `2026-06-30-audit-qualite-global.md` | 2026-06-30 — Audit qualité global du dépôt |
| 2026-06-29 | `2026-06-29_bfl_openai_image_proxy_cartography.md` | AI Log — BFL OpenAI Image Proxy cartography |
| 2026-06-29 | `2026-06-29-moa-reference-role-cleanup.md` | AI Log — MoA Reference Role Cleanup |
| 2026-06-29 | `2026-06-29-method-role-cleanup.md` | AI Log — Method Role Cleanup |
| 2026-06-29 | `2026-06-29-method-cards-reconciliation.md` | AI Log — Method Cards Reconciliation |
| 2026-06-29 | `2026-06-29-hermes-moa-review.md` | AI Log — Hermes MoA Review Classification |
| 2026-06-29 | `2026-06-29-architecture-method-run-tests-tier-alignment.md` | AI Log — Architecture Method Run Tests Tier Alignment |
| 2026-06-29 | `2026-06-29-architecture-method-deck-pruning.md` | AI Log — Architecture Method Deck Pruning Review |
| 2026-06-28 | `2026-06-28-deck-topnav-and-topbar-refinement.md` | AI Log — Deck top navigation and cockpit topbar refinement |
| 2026-06-28 | `2026-06-28-deck-run-type-title-date-index.md` | AI Log — Deck run type title and metadata cleanup |
| 2026-06-28 | `2026-06-28-deck-nested-swiper-navigation.md` | AI Log — Deck nested Swiper navigation correction |
| 2026-06-28 | `2026-06-28-deck-axis-inversion-verified.md` | AI Log — Deck axis inversion verified |
| 2026-06-28 | `2026-06-28-dcode-agent-kit-placement.md` | AI log — dcode-agent-kit placement review |
| 2026-06-28 | `2026-06-28-card-stack-run-task-model.md` | AI Log — Card stack run-task model revision |
| 2026-06-27 | `2026-06-27-reasoning-modes-guide-placement.md` | AI Log — Reasoning modes library placement remediation |
| 2026-06-27 | `2026-06-27-pantheon-control-hierarchy-deck-prototype.md` | AI Log — Pantheon Control hierarchy deck prototype |
| 2026-06-27 | `2026-06-27-iterative-deliberation-lifecycle.md` | AI Log — Iterative Deliberation Lifecycle note |
| 2026-06-27 | `2026-06-27-generic-net-truncation-guard.md` | AI Log — Generic net-truncation guard for long governance docs |
| 2026-06-27 | `2026-06-27-deliberation-ledger-template-and-scenario.md` | AI Log — Constraint & Decision Ledger template + CR chantier scenario |
| 2026-06-27 | `2026-06-27-deck-vertical-depth-swipe.md` | AI Log — Deck vertical hierarchy swipe correction |
| 2026-06-27 | `2026-06-27-deck-card-detail-toggle.md` | AI Log — Deck card detail toggle |
| 2026-06-27 | `2026-06-27-deck-axis-hierarchy-fix.md` | AI Log — Deck axis hierarchy fix |
| 2026-06-27 | `2026-06-27-competence-model-vocabulary.md` | AI Log — Competence model vocabulary |
| 2026-06-27 | `2026-06-27-card-stack-scenes-decks-reconciliation.md` | AI Log — Card Stack Model reconciled to scenes / decks / constellation |
| 2026-06-27 | `2026-06-27-card-stack-role-quality-alignment.md` | AI Log — Card stack role quality alignment |
| 2026-06-27 | `2026-06-27-card-stack-model-candidate.md` | AI Log — Card Stack Model candidate |
| 2026-06-27 | `2026-06-27-card-stack-knowledge-corpus-alignment.md` | AI Log — Card stack knowledge corpus alignment |
| 2026-06-27 | `2026-06-27-card-stack-cluster-indexation.md` | AI Log — Card stack cluster indexation |
| 2026-06-27 | `2026-06-27-authority-index-truncation-repair.md` | AI Log — Repair truncated tail of AUTHORITY_INDEX.md |
| 2026-06-26 | `2026-06-26-validation-report-template.md` | AI Log — Validation report candidate template |
| 2026-06-26 | `2026-06-26-source-need-registry-adaptive-method.md` | AI Log — Source need, registry and adaptive request method |
| 2026-06-26 | `2026-06-26-runtime-review-model-passport-validation-promotion.md` | AI Log — Runtime review and model passport validation promotion |
| 2026-06-26 | `2026-06-26-runtime-review-model-passport-templates.md` | AI Log — Runtime review and model passport templates |
| 2026-06-26 | `2026-06-26-role-facets-as-qualities-reconciliation.md` | AI Log — Role facets as qualities reconciliation |
| 2026-06-26 | `2026-06-26-role-facet-expression-model.md` | AI Log — Role facet expression model |
| 2026-06-26 | `2026-06-26-modules-index-runtime-review-and-truncation-repair.md` | AI Log — MODULES.md: index runtime-review validation + repair truncation |
| 2026-06-26 | `2026-06-26-cortex-hyperspacedb-distillation.md` | AI log — CORTEX / HyperspaceDB distillation |
| 2026-06-26 | `2026-06-26-authority-index-architecture-reflex-registration.md` | AI Log — Authority index architecture reflex registration |
| 2026-06-26 | `2026-06-26-architecture-role-reflex-coordination.md` | AI Log — Architecture role reflex coordination |
| 2026-06-26 | `2026-06-26-architecture-role-facets.md` | AI Log — Architecture role facets |
| 2026-06-26 | `2026-06-26-architecture-role-activation-model.md` | AI Log — Architecture role activation model |
| 2026-06-26 | `2026-06-26-architecture-reflex-operating-model-and-mission-boundary.md` | AI Log — Architecture reflex operating model and mission boundary |
| 2026-06-26 | `2026-06-26-architecture-method-taxonomy-role-owned-reflexes.md` | AI Log — Architecture method taxonomy and role-owned reflexes |
| 2026-06-26 | `2026-06-26-architecture-material-choice-reflex.md` | AI Log — Architecture material choice reflex |
| 2026-06-25 | `2026-06-25-workflow-depth-policy.md` | AI Log — Workflow Depth Policy |
| 2026-06-25 | `2026-06-25-runtime-review-model-passport-promotion.md` | AI Log — Runtime review and model passport promotion |
| 2026-06-25 | `2026-06-25-operational-brain-distillation.md` | AI log — operational Brain / second-brain distillation |
| 2026-06-25 | `2026-06-25-odysseus-reference-distillation.md` | AI Log — Odysseus reference distillation |
| 2026-06-25 | `2026-06-25-missing-information-discipline.md` | AI Log — Missing Information Discipline |
| 2026-06-25 | `2026-06-25-governed-composition-examples-and-schema.md` | AI Log — Governed composition: examples and schema fields (re-land) |
| 2026-06-25 | `2026-06-25-context-stack-candidate.md` | AI Log — Context Stack candidate |
| 2026-06-23 | `2026-06-23-verification-preset-reader.md` | 2026-06-23 verification preset reader |
| 2026-06-23 | `2026-06-23-role-drift-early-warning-slice.md` | AI Log — Role Drift Early Warning Slice |
| 2026-06-23 | `2026-06-23-governance-ci-lockfile.md` | Governance CI lockfile |
| 2026-06-23 | `2026-06-23-governance-ci-direct-dependency-pinning.md` | Governance CI direct dependency pinning |
| 2026-06-23 | `2026-06-23-governance-ci-dependency-centralization.md` | Governance CI dependency centralization |
| 2026-06-23 | `2026-06-23-github-repository-governance-guards.md` | GitHub repository governance guards |
| 2026-06-23 | `2026-06-23-frontsign-pro-exe-hardening.md` | AI Log — Frontsign PRO / EXE hardening pass |
| 2026-06-23 | `2026-06-23-frontsign-partial-project-sources.md` | AI Log — Frontsign partial project sources |
| 2026-06-23 | `2026-06-23-frontsign-charpente-evidence-tree-candidate.md` | AI Log — Frontsign / charpente Evidence Tree Candidate |
| 2026-06-23 | `2026-06-23-financial-lot-insurance-review-workflow.md` | AI Log — Financial lot insurance review workflow |
| 2026-06-23 | `2026-06-23-communication-pattern-taxonomy.md` | AI Log — Architecture Communication Pattern Taxonomy |
| 2026-06-23 | `2026-06-23-communication-pattern-registry.md` | AI Log — Communication Pattern Registry |
| 2026-06-23 | `2026-06-23-communication-pattern-metadata-priority.md` | AI Log — Priority Communication Pattern Metadata |
| 2026-06-23 | `2026-06-23-architecture-mvp-run-cards-index.md` | AI Log — Architecture MVP run cards index |
| 2026-06-23 | `2026-06-23-architecture-mvp-cockpit-view-optimization.md` | AI Log — Architecture MVP cockpit view optimization |
| 2026-06-23 | `2026-06-23-architecture-mvp-assets-exposure.md` | AI Log — Architecture MVP assets exposure |
| 2026-06-22 | `2026-06-22-verification-preset-schema.md` | 2026-06-22 per-module verification preset schema |
| 2026-06-22 | `2026-06-22-update-verification.md` | 2026-06-22 update-availability verification — pattern declined (5th) |
| 2026-06-22 | `2026-06-22-pro-exe-responsibility-slice-template.md` | AI Log — PRO / EXE Responsibility Slice Template |
| 2026-06-22 | `2026-06-22-plano-ai-dataplane-review.md` | AI Log — Plano AI dataplane review |
| 2026-06-22 | `2026-06-22-observability-verification.md` | 2026-06-22 observability verification — pattern declined |
| 2026-06-22 | `2026-06-22-mcp-install-verification.md` | 2026-06-22 mcp-server install / liveness verification surface |
| 2026-06-22 | `2026-06-22-install-verification-contract-doc.md` | 2026-06-22 install verification — evidence contract documented |
| 2026-06-22 | `2026-06-22-install-verification-cockpit-and-cli.md` | 2026-06-22 install verification — cockpit wiring + CLI |
| 2026-06-22 | `2026-06-22-hermes-profile-constitution-adapter.md` | AI Log — Hermes profile constitution adapter |
| 2026-06-22 | `2026-06-22-hermes-multi-profile-kanban-distillation.md` | AI Log — Hermes multi-profile Kanban distillation |
| 2026-06-22 | `2026-06-22-flexible-graphrag-architecture-mvp-slice.md` | AI Log — Flexible GraphRAG architecture MVP slice |
| 2026-06-22 | `2026-06-22-exposure-verification.md` | 2026-06-22 exposure-surface verification — pattern declined (4th) |
| 2026-06-22 | `2026-06-22-cockpit-parity-guard.md` | 2026-06-22 cockpit ↔ classifier parity guard |
| 2026-06-22 | `2026-06-22-backup-verification.md` | 2026-06-22 backup / recoverability verification — pattern declined (3rd) |
| 2026-06-22 | `2026-06-22-architecture-probative-instruction.md` | AI Log — Architecture Probative Instruction |
| 2026-06-22 | `2026-06-22-architecture-mvp-static-html-card.md` | AI Log — Architecture MVP static HTML card |
| 2026-06-22 | `2026-06-22-architecture-mvp-review-card.md` | AI Log — Architecture MVP review card |
| 2026-06-22 | `2026-06-22-architecture-mvp-review-card-json.md` | AI Log — Architecture MVP review card JSON companion |
| 2026-06-22 | `2026-06-22-architecture-mvp-manual-run-001.md` | AI Log — Architecture MVP manual run 001 |
| 2026-06-21 | `2026-06-21-row-bot-4-2-0-reference-review.md` | AI log — Row-Bot 4.2.0 reference review |
| 2026-06-21 | `2026-06-21-role-dialogue-trace.md` | AI log — Role Dialogue Trace candidate orientation |
| 2026-06-21 | `2026-06-21-revit-gate-developer-dossier.md` | AI Log — Pantheon Revit Gate Developer Dossier |
| 2026-06-21 | `2026-06-21-rag-made-simple-reference-intake.md` | AI log — RAG Made Simple reference intake |
| 2026-06-21 | `2026-06-21-promote-property-vocab-shared.md` | 2026-06-21 Promote property vocab to shared catalogue |
| 2026-06-21 | `2026-06-21-pantheon-revit-gate.md` | 2026-06-21 Pantheon Revit Gate framing dossier |
| 2026-06-21 | `2026-06-21-pantheon-control-pages-split.md` | 2026-06-21 — Pantheon Control pages split |
| 2026-06-21 | `2026-06-21-on-the-flow-skills.md` | AI log — On-the-flow skill lifecycle clarification |
| 2026-06-21 | `2026-06-21-nas-installation-profiles.md` | AI log — NAS installation profiles candidate |
| 2026-06-21 | `2026-06-21-modules-map-mcp-server.md` | 2026-06-21 Add MCP policy server to the module map |
| 2026-06-21 | `2026-06-21-module-installation-planner.md` | AI log — Module installation planner mock |
| 2026-06-21 | `2026-06-21-mcp-apu-validation.md` | 2026-06-21 mcp-server APU validation surface |
| 2026-06-21 | `2026-06-21-mcp-apu-reference-coverage.md` | 2026-06-21 Harden mcp-server APU validation reference coverage |
| 2026-06-21 | `2026-06-21-landing-rag-probatoire-link.md` | 2026-06-21 Landing → RAG probatoire navigation link (issue #183) |
| 2026-06-21 | `2026-06-21-intent-log-cockpit-exposure.md` | AI log — Intent Log cockpit exposure |
| 2026-06-21 | `2026-06-21-installations-nas-classifier.md` | AI log — NAS classifier mock in bootstrap cockpit |
| 2026-06-21 | `2026-06-21-installations-bootstrap-cockpit.md` | AI log — Installations & bootstrap cockpit page |
| 2026-06-21 | `2026-06-21-document-apu-validation-tool.md` | 2026-06-21 Document the APU validation tool |
| 2026-06-21 | `2026-06-21-ci-mcp-server-tests.md` | 2026-06-21 CI: run mcp-server module tests + align mcp doctor |
| 2026-06-21 | `2026-06-21-ci-exclude-reference-reviews-forbidden-phrase.md` | 2026-06-21 CI: exclude reference_reviews from forbidden-phrase guard |
| 2026-06-21 | `2026-06-21-bootstrap-installation-ladder.md` | AI log — Bootstrap installation ladder candidate |
| 2026-06-21 | `2026-06-21-autotelic-agency-governance-review.md` | AI log — Autotelic agency governance review |
| 2026-06-21 | `2026-06-21-architectural-project-graph.md` | AI log — Architectural Project Graph candidate orientation |
| 2026-06-21 | `2026-06-21-apu-zonetype-and-adapter-contract.md` | 2026-06-21 APU zone_type requirement + adapter contract |
| 2026-06-21 | `2026-06-21-apu-validation-cli.md` | 2026-06-21 Read-only APU validation CLI |
| 2026-06-21 | `2026-06-21-apu-defs-factoring.md` | 2026-06-21 APU $defs factoring + cross-file ref resolver |
| 2026-06-21 | `2026-06-21-apu-defs-factoring-objectmodel.md` | 2026-06-21 APU $defs factoring — program/conformance + object model |
| 2026-06-21 | `2026-06-21-apu-certainty-e0e4.md` | 2026-06-21 APU certainty unification (decision A) |
| 2026-06-20 | `2026-06-20-program-and-conformance-extension.md` | 2026-06-20 program and conformance extension |
| 2026-06-20 | `2026-06-20-pr155-authority-index-row.md` | PR155 — authority index correction |
| 2026-06-20 | `2026-06-20-pantheon-control-mobile-drawer.md` | 2026-06-20 Pantheon Control mobile drawer |
| 2026-06-20 | `2026-06-20-pantheon-control-cache-buster.md` | 2026-06-20 Pantheon Control cache-buster |
| 2026-06-20 | `2026-06-20-hermes-017-adapter-boundary.md` | AI log — Hermes 0.17 adapter boundary review |
| 2026-06-20 | `2026-06-20-architecture-vertical-mvp.md` | 2026-06-20 — Architecture vertical MVP slice |
| 2026-06-20 | `2026-06-20-architecture-referential-integrity.md` | 2026-06-20 architecture project understanding referential integrity |
| 2026-06-20 | `2026-06-20-architecture-project-understanding-external-references.md` | 2026-06-20 architecture project understanding external references |
| 2026-06-20 | `2026-06-20-architecture-project-understanding-belief-contract.md` | 2026-06-20 architecture project understanding belief contract |
| 2026-06-20 | `2026-06-20-architecture-project-object-model.md` | 2026-06-20 architecture project object model |
| 2026-06-20 | `2026-06-20-architecture-knowledge-registry-blueprint.md` | 2026-06-20 architecture knowledge registry blueprint |
| 2026-06-19 | `2026-06-19-governed-evidence-registry-lifecycle-model.md` | 2026-06-19 governed evidence registry lifecycle model |
| 2026-06-19 | `2026-06-19-dify-langflow-reference-review.md` | AI Log — Dify / Langflow Agentic Builder Review |
| 2026-06-19 | `2026-06-19-agentvision-visual-evidence-adapter.md` | AI Log — AgentVision / Visual Evidence Adapter Review |
| 2026-06-18 | `2026-06-18-radical-signage-evidence-card-direction.md` | 2026-06-18 radical signage evidence card direction |
| 2026-06-18 | `2026-06-18-editorial-magazine-evidence-card-direction.md` | 2026-06-18 editorial magazine evidence card direction |
| 2026-06-18 | `2026-06-18-all-evidence-examples-radical-signals.md` | 2026-06-18 all evidence examples radical signals |
| 2026-06-17 | `2026-06-17-standalone-evidence-card-game.md` | 2026-06-17 standalone evidence card game rewrite |
| 2026-06-17 | `2026-06-17-remove-bottom-action-summary-align-dependencies.md` | 2026-06-17 remove bottom action summary and align dependencies |
| 2026-06-17 | `2026-06-17-one-second-description-scan.md` | 2026-06-17 one-second description scan |
| 2026-06-17 | `2026-06-17-multiple-large-suggestion-options.md` | 2026-06-17 multiple large suggestion options |
| 2026-06-17 | `2026-06-17-mobile-card-alignment.md` | 2026-06-17 mobile card alignment |
| 2026-06-17 | `2026-06-17-layered-typography-echo.md` | 2026-06-17 layered typography echo |
| 2026-06-17 | `2026-06-17-impact-passive-conflict-active.md` | 2026-06-17 passive impact and active conflict distinction |
| 2026-06-17 | `2026-06-17-impact-conflict-lifecycle-algorithm.md` | 2026-06-17 impact conflict lifecycle algorithm |
| 2026-06-17 | `2026-06-17-hide-drawer-evidence-mobile.md` | 2026-06-17 evidence mobile drawer fix |
| 2026-06-17 | `2026-06-17-full-height-card-body-checkbox-suggestions.md` | 2026-06-17 full-height card body with checkbox suggestions |
| 2026-06-17 | `2026-06-17-force-description-typography-above-title.md` | 2026-06-17 force description typography above title |
| 2026-06-17 | `2026-06-17-floor-selection-three-card-draft.md` | 2026-06-17 floor selection three-card draft |
| 2026-06-17 | `2026-06-17-floor-selection-regression-logic.md` | 2026-06-17 floor selection regression logic |
| 2026-06-17 | `2026-06-17-floor-selection-pending-impact.md` | 2026-06-17 floor selection pending impact lifecycle |
| 2026-06-17 | `2026-06-17-fast-read-card-keywords.md` | 2026-06-17 fast-read card keyword override |
| 2026-06-17 | `2026-06-17-evidence-card-mobile-hierarchy.md` | Evidence card mobile hierarchy refinement |
| 2026-06-17 | `2026-06-17-evidence-card-game-prototype.md` | 2026-06-17 evidence card game prototype |
| 2026-06-17 | `2026-06-17-evidence-card-description-tail.md` | Evidence card description tail tweak |
| 2026-06-17 | `2026-06-17-evidence-card-data-fixture.md` | 2026-06-17 evidence card data fixture split |
| 2026-06-17 | `2026-06-17-description-suggestion-action-labels-large-type.md` | 2026-06-17 description suggestion action labels large type |
| 2026-06-17 | `2026-06-17-description-42px-ultrabold.md` | 2026-06-17 description 42px ultrabold |
| 2026-06-17 | `2026-06-17-confirmed-impact-links-conflict-rules.md` | 2026-06-17 confirmed impact links and conflict rules |
| 2026-06-17 | `2026-06-17-card-top-sections-bottom-actions.md` | 2026-06-17 card top sections and bottom actions layout |
| 2026-06-17 | `2026-06-17-card-spacing-metadata-relation-section.md` | 2026-06-17 card spacing metadata and relation section refinement |
| 2026-06-17 | `2026-06-17-card-revision-proposal-lifecycle.md` | 2026-06-17 card revision proposal lifecycle |
| 2026-06-17 | `2026-06-17-card-relation-footer-detail-toggle.md` | 2026-06-17 card relation footer detail toggle |
| 2026-06-17 | `2026-06-17-card-option-oriented-suggestions.md` | 2026-06-17 option-oriented card suggestions |
| 2026-06-17 | `2026-06-17-card-log-link-rules.md` | 2026-06-17 card log and link rules |
| 2026-06-17 | `2026-06-17-card-large-concise-text.md` | 2026-06-17 large concise card text update |
| 2026-06-17 | `2026-06-17-candidate-impact-graph.md` | 2026-06-17 candidate impact graph lifecycle |
| 2026-06-16 | `2026-06-16-pantheon-control-langfuse-observability-page.md` | AI Log — Pantheon Control Langfuse observability page |
| 2026-06-16 | `2026-06-16-langfuse-dashboard-link-card.md` | AI Log — Langfuse Dashboard link card candidate |
| 2026-06-16 | `2026-06-16-landing-dark-square-ui.md` | AI Log — landing dark square UI pass |
| 2026-06-16 | `2026-06-16-landing-architecture-clarity-pass.md` | AI Log — landing architecture clarity pass |
| 2026-06-16 | `2026-06-16-evidence-mobile-swiper-mockup.md` | 2026-06-16 — Evidence mobile Swiper mockup |
| 2026-06-16 | `2026-06-16-evidence-compact-no-scroll-ux.md` | 2026-06-16 — Evidence compact no-scroll UX |
| 2026-06-16 | `2026-06-16-architecture-usecase-path-clean.md` | Architecture use-case path clean landing patch |
| 2026-06-16 | `2026-06-16-architecture-source-policy.md` | AI Log — Architecture Source Policy |
| 2026-06-15 | `2026-06-15_terminology_cleanup_pass_1.md` | AI log — terminology cleanup pass 1 |
| 2026-06-15 | `2026-06-15_terminology_boundaries.md` | AI log — terminology boundaries |
| 2026-06-15 | `2026-06-15-status-headers-normalisation.md` | AI Log — Status-header normalisation (Lot B) |
| 2026-06-15 | `2026-06-15-shared-defs-seed.md` | AI Log — Shared definitions seed |
| 2026-06-15 | `2026-06-15-langfuse-hermes-installation-package-candidate.md` | AI Log — Langfuse / Hermes installation package candidate |
| 2026-06-15 | `2026-06-15-langfuse-first-test-runbook.md` | AI Log — Langfuse / Hermes first-test runbook |
| 2026-06-15 | `2026-06-15-langfuse-first-test-posture.md` | AI Log — Langfuse first-test posture |
| 2026-06-15 | `2026-06-15-landing-langfuse-docs-visual-pass.md` | AI Log — landing page documentation visual pass |
| 2026-06-15 | `2026-06-15-landing-flow2a-refined-d3-patch.md` | AI Log — Landing flow2a refined D3 patch |
| 2026-06-15 | `2026-06-15-internal-links-lot-d.md` | AI Log — Internal-link reconciliation (Lot D) |
| 2026-06-15 | `2026-06-15-index-coverage-lot-c.md` | AI Log — Index the 18 top-level candidate docs (Lot C) |
| 2026-06-15 | `2026-06-15-index-coverage-grouped-rows.md` | AI Log — Index-coverage honors grouped rows (Lot A) |
| 2026-06-15 | `2026-06-15-governance-linkage-reconciliation.md` | AI Log — Governance linkage & status reconciliation overview |
| 2026-06-15 | `2026-06-15-flow2a-mobile-text-overlap-fix.md` | AI Log — flow2a mobile text overlap fix |
| 2026-06-15 | `2026-06-15-flow2a-mobile-regression-observed.md` | AI Log — flow2a mobile regression observed |
| 2026-06-15 | `2026-06-15-flow2a-mobile-hotfix-todo.md` | AI Log — flow2a mobile hotfix todo |
| 2026-06-15 | `2026-06-15-architecture-os-reconciliation.md` | AI Log — Architecture OS reconciliation |
| 2026-06-14 | `2026-06-14-workflow-navigation.md` | AI log — workflow navigation |
| 2026-06-14 | `2026-06-14-schema-d3-reconciliation.md` | AI Log — Schema D3 reconciliation apply |
| 2026-06-14 | `2026-06-14-register-link-cascade-schema-proposal.md` | AI Log — Register Link & Cascade schema proposal |
| 2026-06-14 | `2026-06-14-register-instances-doctor-single-source.md` | AI Log — Register-instance validation promoted into the doctor |
| 2026-06-14 | `2026-06-14-pantheon-control-ux-integration.md` | AI Log — Pantheon Control UX integration |
| 2026-06-14 | `2026-06-14-pantheon-cockpit-ux-spec.md` | AI Log — Pantheon Cockpit UX candidate spec |
| 2026-06-14 | `2026-06-14-pantheon-cockpit-ux-mock.md` | AI Log — Pantheon Cockpit UX mock |
| 2026-06-14 | `2026-06-14-paddleocr-dashboard-install-candidate.md` | AI Log — PaddleOCR dashboard install candidate |
| 2026-06-14 | `2026-06-14-paddleocr-dashboard-hermes-boundary.md` | AI Log — PaddleOCR dashboard-installable / Hermes-managed boundary |
| 2026-06-14 | `2026-06-14-existing-dashboard-reconciliation.md` | AI Log — Existing dashboard reconciliation |
| 2026-06-14 | `2026-06-14-d3-entry-output-memory-flow.md` | AI log — D3 entry/output/memory flow visual |
| 2026-06-14 | `2026-06-14-d3-entries-outputs-memory-flow.md` | AI Log — D3 entries / outputs / memory flow |
| 2026-06-14 | `2026-06-14-cascade-instances-ci.md` | AI Log — Validated register instances + CI cascade enforcement |
| 2026-06-14 | `2026-06-14-cascade-followups.md` | AI Log — Cascade follow-ups (rule check, link reference, mockup wiring) |
| 2026-06-14 | `2026-06-14-awesome-free-models-watchlist-boundary.md` | AI Log — awesome-free-models external tooling watchlist boundary |
| 2026-06-14 | `2026-06-14-agentcanvas-trace-visualization-review.md` | AI Log — AgentCanvas trace visualization review |
| 2026-06-13 | `2026-06-13-spice-reference-distillation.md` | AI Log — Spice reference distillation |
| 2026-06-13 | `2026-06-13-ecosystem-map-registre-probatoire-ux.md` | AI log — Ecosystem map realigned around Registre Probatoire |
| 2026-06-13 | `2026-06-13-dossier-situation-intake-workflows.md` | AI log — Dossier Situation Intake and workflow-under-hood examples |
| 2026-06-13 | `2026-06-13-decision-surface-spec.md` | AI Log — Decision surface specification |
| 2026-06-13 | `2026-06-13-decision-surface-index-consolidation.md` | AI Log — Decision surface index consolidation |
| 2026-06-13 | `2026-06-13-dashboard-mockup-multipage-reorg.md` | AI Log — Réorganisation multi-pages du mockup Pantheon Control |
| 2026-06-12 | `2026-06-12-vertical-tilleuls-proven.md` | AI log — Step 4: the vertical is proven end to end (Tilleuls) |
| 2026-06-12 | `2026-06-12-stubs-wave3-epistemic-skill.md` | AI log — Stub resolution wave 3: epistemic disposition + fresh SKILL_LIFECYCLE |
| 2026-06-12 | `2026-06-12-stubs-wave2-merges.md` | AI log — Stub resolution wave 2: four merges |
| 2026-06-12 | `2026-06-12-stubs-wave1-obsolete.md` | AI log — Stub resolution wave 1: four obsolete markings |
| 2026-06-12 | `2026-06-12-registre-e6-applied.md` | AI log — E6 applied: register_candidate rename + spine schemas completed |
| 2026-06-12 | `2026-06-12-pr35-reprise-completed.md` | AI log — PR #35 reprise: review and completion |
| 2026-06-12 | `2026-06-12-mcp-phase5-6-review-fixes.md` | AI log — mcp-server Phases 5-6: review and fixes |
| 2026-06-12 | `2026-06-12-lot2-boundary-topology-consolidation.md` | AI log — Lot 2: boundary standard, evidence topology consolidation, stub plan |
| 2026-06-12 | `2026-06-12-governed-execution-handoff.md` | AI log — governed execution handoff slice |
| 2026-06-12 | `2026-06-12-dlthub-canonical-text-to-sql-review.md` | AI log — dltHub canonical Text-to-SQL review |
| 2026-06-11 | `2026-06-11-chatgpt-work-order-mcp-phase5-6-logement.md` | Note de travail — Piste ChatGPT : mcp-server Phases 5-6 + exemple vertical « logement collectif / promoteur » |
| 2026-06-10 | `2026-06-10-pantheon-control-boundary-consolidation.md` | AI log — Pantheon Control consolidation into one boundary document |
| 2026-06-10 | `2026-06-10-open-pr-triage-plan.md` | AI log — Open PR triage plan (9 open PRs) |
| 2026-06-10 | `2026-06-10-mcp-server-first-slice.md` | AI log — mcp-server: first implementation slice |
| 2026-06-10 | `2026-06-10-lot1-read-only-governance-checks.md` | AI log — Lot 1 read-only governance checks |
| 2026-06-10 | `2026-06-10-global-repo-analysis-and-direction.md` | AI log — Global repository analysis and direction synthesis |
| 2026-06-10 | `2026-06-10-chatgpt-work-order-repo-optimizations.md` | Note de travail — Piste ChatGPT : optimisations du dépôt Pantheon Next |
| 2026-06-10 | `2026-06-10-changelog-rotation.md` | AI log — CHANGELOG rotation (archive older entries) |
| 2026-06-09 | `2026-06-09-uniform-capability-governance.md` | AI log — Uniform Capability Governance keystone |
| 2026-06-09 | `2026-06-09-target-architecture-coherence-compass.md` | AI log — Target Architecture coherence compass |
| 2026-06-09 | `2026-06-09-spine-hardening-proposal.md` | AI log — Spine Hardening Proposal update |
| 2026-06-09 | `2026-06-09-monorepo-integration-proposal.md` | AI log — Monorepo integration proposal |
| 2026-06-09 | `2026-06-09-chokepoint-enforcement-rule.md` | AI log — make the consequential chokepoint explicit |
| 2026-06-08 | `2026-06-08-workflow-schema-governed-composition.md` | AI log — WORKFLOW_SCHEMA governed composition (two gates) + Registre alignment |
| 2026-06-08 | `2026-06-08-skillsgate-mcp-skill-admission.md` | AI Log — SkillsGate MCP skill admission guard |
| 2026-06-08 | `2026-06-08-registre-vocabulary-sweep.md` | AI log — corpus-wide Registre Probatoire vocabulary sweep (issue #90) |
| 2026-06-08 | `2026-06-08-registre-e6-schema-proposal.md` | AI log — E6: Registre Probatoire schema rename proposal |
| 2026-06-08 | `2026-06-08-registre-e5-reindex.md` | AI log — E5: reindex the authority map to the Registre Probatoire vocabulary |
| 2026-06-08 | `2026-06-08-registre-e3-canonicalization-doc.md` | AI log — E3: promote EVIDENCE_MEMORY_CANONICALIZATION as the central Registre Probatoire document |
| 2026-06-08 | `2026-06-08-pr53-keystone-index-completion.md` | AI log — complete the rebased governed-composition keystone (#88) with index integration |
| 2026-06-08 | `2026-06-08-ci-vocabulary-regression-guard.md` | AI log — CI guard against Registre Probatoire vocabulary regression |
| 2026-06-08 | `2026-06-08-capability-registry-review-feedback.md` | AI log — Capability Registry review feedback fix |
| 2026-06-07 | `2026-06-07-self-inspect-rite-trigger-catalogue.md` | AI log — self-inspect-mcp review and the Rite Trigger Catalogue |
| 2026-06-07 | `2026-06-07-review-recent-merges-architecture.md` | AI log — Review of recent merges and open PRs, architecture and next-step sequencing |
| 2026-06-07 | `2026-06-07-registre-probatoire-direction.md` | AI log — Memory becomes Hermès-owned; Pantheon governs the Registre Probatoire |
| 2026-06-07 | `2026-06-07-registre-e2-memory-reframe.md` | AI log — E2: reframe MEMORY.md under the Registre Probatoire direction |
| 2026-06-07 | `2026-06-07-registre-e1-glossary-axes.md` | AI log — E1: GLOSSARY owns the Registre Probatoire vocabulary and the three axes |
| 2026-06-07 | `2026-06-07-mcp-policy-server-development.md` | AI Log — MCP Policy Server development roadmap |
| 2026-06-07 | `2026-06-07-mcp-policy-server-candidate.md` | 2026-06-07 — MCP policy server candidate |
| 2026-06-07 | `2026-06-07-green-governance-ci-lint-precision.md` | AI log — Green the Governance CI by widening the forbidden-phrase lint |
| 2026-06-07 | `2026-06-07-external-runtime-memory-adapters.md` | AI Log — External Runtime Memory Adapters |
| 2026-06-07 | `2026-06-07-domain-pack-pre-analysis-intake.md` | AI Log — Domain pack pre-analysis intake discipline |
| 2026-06-07 | `2026-06-07-assert-directory-mcp-reference-reviews.md` | AI log — Reference reviews: ASSERT and directory-mcp |
| 2026-06-07 | `2026-06-07-architecture-proof-register-vertical-example.md` | AI Log — Architecture Proof Register vertical example |
| 2026-06-07 | `2026-06-07-answer-verification-gate.md` | AI Log — Answer Verification Gate |
| 2026-06-07 | `2026-06-07-answer-verification-gate-hardening.md` | AI Log — Answer Verification Gate hardening |
| 2026-06-06 | `2026-06-06-sub-agent-mcp-reference-review.md` | 2026-06-06 — Sub-Agent-MCP reference review |
| 2026-06-06 | `2026-06-06-repository-review-watcher.md` | AI Log — Repository Review Watcher workflow candidate |
| 2026-06-06 | `2026-06-06-hermes-kanban-execution-patterns.md` | AI Log — Hermes Kanban execution patterns |
| 2026-06-06 | `2026-06-06-elt-reference-review.md` | AI Log — ELT external reference review |
| 2026-06-06 | `2026-06-06-document-learning-explainer-boundary.md` | AI Log — Document learning and explainer boundary |
| 2026-06-06 | `2026-06-06-dashboard-v15-evidence-memory.md` | AI Log — Dashboard v15 Evidence → Memory prototype |
| 2026-06-04 | `2026-06-04_landing_stack_rewrite_attempt.md` | AI log — landing stack rewrite attempt |
| 2026-06-04 | `2026-06-04-landing-responsive-diagrams-glossary.md` | AI log — responsive mobile diagrams, animation, agentic/RAG glossary |
| 2026-06-04 | `2026-06-04-landing-four-diagrams-ecosystem.md` | AI log — landing four-diagram set, decision outside the frame, ecosystem view |
| 2026-06-03 | `2026-06-03-landing-detail-iterative-d3-diagram.md` | AI log — landing detailed iterative D3 diagram |
| 2026-06-03 | `2026-06-03-governed-composition-forge.md` | AI Log — Governed composition (HÉPHAÏSTOS forges, capability registry, two gates) |
| 2026-06-03 | `2026-06-03-cerfa-rag-d3-asset-and-pr51-merge-check.md` | AI log — Cerfa RAG D3 asset and PR51 merge check |
| 2026-06-03 | `2026-06-03-architecture-target-workflows-pr.md` | AI log — architecture target workflow synthesis PR |
| 2026-06-02 | `2026-06-02-site-photo-review-workflow.md` | AI log — site photo review workflow example |
| 2026-06-02 | `2026-06-02-post-42-index-ci-repair.md` | AI Log — Post-#42 index and CI wording repair |
| 2026-06-02 | `2026-06-02-landing-architecture-mobile-d3-refocus.md` | AI log — landing architecture mobile D3 refocus |
| 2026-06-02 | `2026-06-02-d3-invoice-visa-spine-workflow.md` | AI log — D3 invoice visa spine workflow |
| 2026-06-02 | `2026-06-02-autonomy-minimalism-reconciled.md` | AI Log — Autonomy minimalism reconciliation |
| 2026-06-01 | `2026-06-01_operations_spec_first_boundary.md` | AI Log — Operations spec-first boundary |
| 2026-06-01 | `2026-06-01_doctor_module_spec.md` | AI Log — Doctor module specification |
| 2026-06-01 | `2026-06-01_authority_index.md` | AI Log — Authority Index |
| 2026-06-01 | `2026-06-01-truncated-update-repair.md` | AI Log — Truncated Update Repair |
| 2026-06-01 | `2026-06-01-status-optimization.md` | AI Log — Governance index optimization and de-duplication |
| 2026-06-01 | `2026-06-01-request-lifecycle-metis.md` | AI Log — Request Lifecycle (MÈTIS, cap, memory gates) |
| 2026-06-01 | `2026-06-01-landing-architect-schema-table.md` | AI Log — Landing page: architect schema + table, other professions to-study |
| 2026-06-01 | `2026-06-01-landing-architect-d3-flow.md` | AI Log — Landing page: architect flow as a D3.js diagram |
| 2026-06-01 | `2026-06-01-governed-form-filling.md` | AI Log — Governed Form Filling |
| 2026-06-01 | `2026-06-01-external-tool-placement-register.md` | AI Log — External Tool Placement Register |
| 2026-06-01 | `2026-06-01-core-records-model.md` | AI Log — Core Records Model |
| 2026-06-01 | `2026-06-01-agentos-reference-review.md` | AgentOS reference review |
| 2026-05-31 | `2026-05-31-urgent-review-triage.md` | AI Log — Urgent Review Triage |
| 2026-05-31 | `2026-05-31-urgent-fiche-triage-template.md` | AI Log — Urgent Fiche Triage Template |
| 2026-05-31 | `2026-05-31-soul-md-hermes-profile-boundary.md` | AI Log — SOUL.md Hermes profile boundary |
| 2026-05-31 | `2026-05-31-session-handoff-template.md` | AI Log — Session Handoff Template Distillation |
| 2026-05-31 | `2026-05-31-review-queue-governance-rule.md` | AI Log — Review Queue Governance Rule |
| 2026-05-31 | `2026-05-31-quarkdown-reference-review.md` | AI Log — Quarkdown reference review |
| 2026-05-31 | `2026-05-31-placement-template-consolidation-audit.md` | AI Log — Placement, templates and audit consolidation |
| 2026-05-31 | `2026-05-31-paddleocr-hermes-skill-placement.md` | AI Log — PaddleOCR Hermes Skill Placement |
| 2026-05-31 | `2026-05-31-modular-domain-reorientation.md` | AI Log — Modular domain reorientation |
| 2026-05-31 | `2026-05-31-modular-domain-reorientation-reconciliation.md` | AI Log — Modular domain reorientation reconciliation |
| 2026-05-31 | `2026-05-31-landing-page-rewrite.md` | AI Log — Landing page rewrite for liberal professions |
| 2026-05-31 | `2026-05-31-landing-architect-dropdown.md` | AI Log — Landing page: architect detail dropdown |
| 2026-05-31 | `2026-05-31-indexed-document-version-governance.md` | AI Log — Indexed Document Version Governance |
| 2026-05-31 | `2026-05-31-governance-scan-review-queue.md` | AI Log — Governance scan: allow governed review/decision queue |
| 2026-05-31 | `2026-05-31-github-pages-landing.md` | AI Log — GitHub Pages Landing Page |
| 2026-05-31 | `2026-05-31-document-intelligence-architecture-review.md` | AI Log — Document Intelligence / Architecture Review |
| 2026-05-31 | `2026-05-31-data-platform-reconciliation-uploaded-postgres-analysis.md` | AI Log — Data Platform Reconciliation / Uploaded Postgres Analysis |
| 2026-05-31 | `2026-05-31-data-platform-boundary-review.md` | AI Log — Data platform boundary review |
| 2026-05-31 | `2026-05-31-d3-tool-placement-map.md` | AI Log — D3 Tool Placement Map |
| 2026-05-31 | `2026-05-31-architecture-proof-register.md` | AI Log — Architecture Proof Register |
| 2026-05-31 | `2026-05-31-architecture-proof-register-implementation-spec.md` | AI Log — Architecture Proof Register Implementation Spec |
| 2026-05-31 | `2026-05-31-architecture-index-effect-matrix.md` | AI Log — Architecture Index Effect Matrix |
| 2026-05-31 | `2026-05-31-architectural-pattern-reference-boundary.md` | AI Log — Architectural pattern reference boundary |
| 2026-05-31 | `2026-05-31-align-readme-page-with-reorientation.md` | AI Log — Align README and landing page with the modular reorientation |
| 2026-05-31 | `2026-05-31-adapters-and-bindings.md` | AI Log — Adapters and bindings |
| 2026-05-30 | `2026-05-30-workflow-manifest-evidence-topology-finish.md` | Workflow Manifest Evidence Topology Finish |
| 2026-05-30 | `2026-05-30-schema-test-dependencies.md` | AI Log — Schema Test Dependencies |
| 2026-05-30 | `2026-05-30-schema-test-dependencies-present.md` | AI Log — Schema Test Dependencies Present |
| 2026-05-30 | `2026-05-30-readme-module-relation-diagram.md` | AI Log — README: module relation diagram |
| 2026-05-30 | `2026-05-30-readme-dossier-sorting-and-rag.md` | AI Log — README: dossier sorting and plain-language RAG |
| 2026-05-30 | `2026-05-30-public-readme-clarity-architecture.md` | AI Log — Public README Clarity Pass (Architecture Examples) |
| 2026-05-30 | `2026-05-30-public-readme-channel-framing.md` | AI Log — Public README Channel and Conduct Framing |
| 2026-05-30 | `2026-05-30-public-index-reconciliation.md` | AI Log — Public Index Reconciliation |
| 2026-05-30 | `2026-05-30-pre-execution-simulation-doctrine.md` | AI Log — Pre-Execution Simulation Doctrine |
| 2026-05-30 | `2026-05-30-hermes-evaluation-simulation-candidate.md` | AI Log — Hermes Evaluation and Simulation Candidate |
| 2026-05-30 | `2026-05-30-governance-ci-stub-section-optional.md` | AI Log — Governance CI: tolerate absent "Stub present" section |
| 2026-05-30 | `2026-05-30-future-agi-task-contract-boundary.md` | AI Log — Future AGI Task Contract Boundary Clarification |
| 2026-05-30 | `2026-05-30-future-agi-simulation-registry-reconcile.md` | AI Log — Future AGI Simulation Registry Reconcile |
| 2026-05-30 | `2026-05-30-future-agi-reference-review.md` | AI Log — Future AGI Reference Review |
| 2026-05-30 | `2026-05-30-evidence-topology-status-readme-fr-index.md` | Evidence Topology Status and Bilingual README Indexing |
| 2026-05-30 | `2026-05-30-evidence-topology-schema-option-b.md` | Evidence Topology Schema Option B |
| 2026-05-30 | `2026-05-30-evidence-topology-schema-finish.md` | Evidence Topology Schema Finish |
| 2026-05-30 | `2026-05-30-evidence-topology-public-readme-index.md` | Evidence Topology Public README Index |
| 2026-05-30 | `2026-05-30-evidence-topology-governance-index-changelog.md` | Evidence Topology Governance Index and Changelog |
| 2026-05-30 | `2026-05-30-evidence-topology-checklist-antipatterns-architecture.md` | Evidence Topology Checklist, Anti-patterns and Architecture Example |
| 2026-05-30 | `2026-05-30-evidence-topology-acb-reconciliation.md` | Evidence Topology ACB Reconciliation |
| 2026-05-30 | `2026-05-30-domain-pack-general-spec.md` | AI Log — General Domain Pack Specification |
| 2026-05-30 | `2026-05-30-core-concepts-map.md` | AI Log — Core Concepts Map |
| 2026-05-30 | `2026-05-30-architecture-pre-execution-simulation-example.md` | AI Log — Architecture Pre-Execution Simulation Example |
| 2026-05-29 | `2026-05-29-understand-anything-structural-examples.md` | AI Log — Understand-Anything Structural Analysis Examples |
| 2026-05-29 | `2026-05-29-understand-anything-hermes-adapter.md` | AI Log — Understand-Anything Hermes Boundary |
| 2026-05-29 | `2026-05-29-understand-anything-graph-authority-lock.md` | AI Log — Understand-Anything Graph Authority Lock |
| 2026-05-29 | `2026-05-29-rites-task-evidence-openwebui-raccord.md` | 2026-05-29 - Rites raccord to Task Contracts, Evidence Packs and OpenWebUI |
| 2026-05-29 | `2026-05-29-rites-status-college-raccord.md` | 2026-05-29 - Rites status and Governance College raccord |
| 2026-05-29 | `2026-05-29-rites-p3-examples.md` | 2026-05-29 - Rites P3 examples |
| 2026-05-29 | `2026-05-29-rites-p2-selection-modes.md` | 2026-05-29 - Rites P2 selection matrix and modes |
| 2026-05-29 | `2026-05-29-rites-p1-antidrift.md` | 2026-05-29 - Rites P1 anti-drift hardening |
| 2026-05-29 | `2026-05-29-rites-invocation-policy-hardening.md` | 2026-05-29 - Rites invocation policy hardening |
| 2026-05-29 | `2026-05-29-rites-governance-layer.md` | 2026-05-29 - Rites governance layer |
| 2026-05-29 | `2026-05-29-rag-boundary-reconciliation.md` | AI Log — RAG Boundary Reconciliation |
| 2026-05-29 | `2026-05-29-parallel-governance-audit.md` | AI Log — Parallel Governance Audit |
| 2026-05-29 | `2026-05-29-nango-connector-gateway-review.md` | Nango connector gateway review |
| 2026-05-29 | `2026-05-29-discordia-divergence-sentinel.md` | 2026-05-29 - Discordia divergence sentinel |
| 2026-05-29 | `2026-05-29-ai-learning-repos-distillation.md` | AI learning repositories distillation |
| 2026-05-27 | `2026-05-27-schema-validation-tests.md` | AI Log — Schema Validation Tests |
| 2026-05-27 | `2026-05-27-role-domain-skill-activation.md` | AI Log — Role, Domain and Skill Activation |
| 2026-05-27 | `2026-05-27-role-activation-coherence-fix.md` | AI Log — Role Activation Coherence Fix |
| 2026-05-27 | `2026-05-27-rag-evidence-boundaries.md` | AI Log — RAG Evidence Boundaries |
| 2026-05-27 | `2026-05-27-phase-d1-schema-reconciliation.md` | AI Log — Phase D1 Schema Reconciliation |
| 2026-05-27 | `2026-05-27-openwebui-template-hierarchy.md` | AI Log — OpenWebUI Template Hierarchy |
| 2026-05-27 | `2026-05-27-module-activation-langgraph.md` | AI Log — Module Activation and LangGraph Boundary |
| 2026-05-27 | `2026-05-27-architecture-legal-module-panel-example.md` | AI Log — Architecture Legal Module Panel Example |
| 2026-05-26 | `2026-05-26-external-reference-governance.md` | AI Log — External Reference Governance System |
| 2026-05-24 | `2026-05-24-ai-literacy-ulysse-poster-distillation.md` | AI log — Ulysse poster distillation |
| 2026-05-24 | `2026-05-24-ai-literacy-hydre-html-planche.md` | AI log — Hydre HTML planche asset |
| 2026-05-24 | `2026-05-24-ai-literacy-hercule-poster-distillation.md` | AI log — Hercule poster distillation |
| 2026-05-23 | `2026-05-23-ai-literacy-ulysse-hercule-diptych.md` | AI log — Ulysse Hercule diptych matrix |
| 2026-05-23 | `2026-05-23-ai-literacy-pommes-or-scene-card.md` | AI log — Pommes d'Or scene card |
| 2026-05-23 | `2026-05-23-ai-literacy-hercule-reconciliation-matrix.md` | AI log — Hercule reconciliation matrix |
| 2026-05-23 | `2026-05-23-ai-literacy-hercule-master-reconcile.md` | AI log — Hercule master reconciliation |
| 2026-05-23 | `2026-05-23-ai-literacy-hercule-index.md` | AI log — AI literacy Hercule index update |
| 2026-05-23 | `2026-05-23-ai-literacy-hercule-first-six-scene-cards.md` | AI log — Hercule first six scene cards |
| 2026-05-23 | `2026-05-23-ai-literacy-cerbere-scene-card.md` | AI log — Cerbere scene card |
| 2026-05-23 | `2026-05-23-ai-literacy-boeufs-geryon-scene-card.md` | AI log — Boeufs de Geryon scene card |
| 2026-05-22 | `2026-05-22-ai-literacy-taureau-crete-scene-card.md` | AI log — Taureau de Crete scene card |
| 2026-05-22 | `2026-05-22-ai-literacy-sanglier-steering-frame.md` | AI log — Sanglier steering frame |
| 2026-05-22 | `2026-05-22-ai-literacy-sanglier-scene-card.md` | AI log — Sanglier scene card |
| 2026-05-22 | `2026-05-22-ai-literacy-readme-reconciliation.md` | AI log — AI literacy README reconciliation |
| 2026-05-22 | `2026-05-22-ai-literacy-oiseaux-stymphale-scene-card.md` | AI log — Oiseaux du Stymphale scene card |
| 2026-05-22 | `2026-05-22-ai-literacy-juments-diomede-scene-card.md` | AI log — Juments de Diomede scene card |
| 2026-05-22 | `2026-05-22-ai-literacy-hydre-scene-card.md` | AI log — Hydre scene card |
| 2026-05-22 | `2026-05-22-ai-literacy-ecuries-scene-card.md` | AI log — Ecuries scene card |
| 2026-05-22 | `2026-05-22-ai-literacy-ceinture-mandate-hierarchy.md` | AI log — Ceinture mandate hierarchy |
| 2026-05-22 | `2026-05-22-ai-literacy-ceinture-hippolyte-scene-card.md` | AI log — Ceinture d'Hippolyte scene card |
| 2026-05-22 | `2026-05-22-ai-literacy-biche-scene-card.md` | AI log — Biche scene card |
| 2026-05-22 | `2026-05-22-ai-literacy-biche-sanglier-repartition.md` | AI log — Biche / Sanglier repartition |
| 2026-05-22 | `2026-05-22-ai-literacy-biche-prompt-trajectory.md` | AI log — Biche prompt trajectory |
| 2026-05-22 | `2026-05-22-ai-literacy-biche-instantaneity.md` | AI log — Biche instantaneity refinement |
| 2026-05-21 | `2026-05-21-ai-literacy-ulysse-theoretical-preface.md` | AI log — Ulysse theoretical preface |
| 2026-05-21 | `2026-05-21-ai-literacy-ulysse-reconciled-longform.md` | AI log — Ulysse reconciled longform |
| 2026-05-21 | `2026-05-21-ai-literacy-lestrygons-scene-card.md` | AI log — Lestrygons scene card |
| 2026-05-21 | `2026-05-21-ai-literacy-ithaque-scene-card.md` | AI log — Ithaque scene card |
| 2026-05-21 | `2026-05-21-ai-literacy-circe-scene-card.md` | AI log — Circe scene card |
| 2026-05-20 | `2026-05-20-ulysse-academic-framing.md` | AI Log — 2026-05-20 — Ulysse academic framing refinement |
| 2026-05-20 | `2026-05-20-ai-literacy-ulysse-scene-cards.md` | AI log — AI literacy Ulysse scene cards |
| 2026-05-20 | `2026-05-20-ai-literacy-lotophages-scene-card.md` | AI log — AI literacy Lotophages scene card expansion |
| 2026-05-20 | `2026-05-20-ai-literacy-eole-scene-card.md` | AI log — Eole scene card expansion |
| 2026-05-20 | `2026-05-20-ai-literacy-cyclope-scene-card.md` | AI log — AI literacy Cyclope scene card expansion |
| 2026-05-19 | `2026-05-19-ulysse-poster-distillation.md` | AI Log — Ulysse poster distillation |
| 2026-05-19 | `2026-05-19-ulysse-ia-rapport.md` | AI Log — Ulysse IA rapport article |
| 2026-05-19 | `2026-05-19-ulysse-ia-rapport-enrichment.md` | AI Log — Ulysse IA rapport enrichment |
| 2026-05-19 | `2026-05-19-ulysse-ai-traps-practical-cases.md` | AI Log — 2026-05-19 — Ulysse AI traps practical cases |
| 2026-05-19 | `2026-05-19-ulysse-academic-version.md` | AI Log — Ulysse/Hercule audit integration and academic version |
| 2026-05-19 | `2026-05-19-tool-legal-pattern-keepers-roadmap.md` | Tool and Legal Pattern Keepers Roadmap Update |
| 2026-05-19 | `2026-05-19-roadmap-ci-wording-alignment.md` | Roadmap CI Wording Alignment |
| 2026-05-19 | `2026-05-19-persistent-role-team-topology.md` | Persistent Role-Team Topology Update |
| 2026-05-19 | `2026-05-19-memory-event-scope-alignment.md` | Memory Event Scope Alignment |
| 2026-05-19 | `2026-05-19-hercule-ai-discipline.md` | AI Log — 2026-05-19 — Hercule AI discipline note |
| 2026-05-19 | `2026-05-19-external-agent-pattern-keepers-roadmap.md` | External Agent Pattern Keepers Roadmap Update |
| 2026-05-19 | `2026-05-19-evidence-topology-gate.md` | Evidence Topology Gate Doctrine |
| 2026-05-19 | `2026-05-19-evidence-topology-examples.md` | Evidence Topology Examples |
| 2026-05-19 | `2026-05-19-deep-learning-illustrated-reference.md` | AI Log — Deep Learning Illustrated reference note |
| 2026-05-18 | `2026-05-18-vertical-central-flow-map.md` | AI Log — Vertical central flow map |
| 2026-05-18 | `2026-05-18-roadmap-workflow-rag-reconcile.md` | Roadmap Phase 1 Workflow and RAG Reconcile |
| 2026-05-18 | `2026-05-18-readme-simplify-pro-com.md` | README Simplification — Less AI, More Professional, More Communication |
| 2026-05-18 | `2026-05-18-optimized-bubble-map.md` | AI Log — Optimized bubble map |
| 2026-05-18 | `2026-05-18-mobile-menu-toggle-map.md` | AI Log — Mobile menu toggle for interactive map |
| 2026-05-18 | `2026-05-18-migrate-task-contract-revisions.md` | Migrate TASK_CONTRACT_REVISIONS.md |
| 2026-05-18 | `2026-05-18-migrate-memory-event-schema.md` | Migrate MEMORY_EVENT_SCHEMA |
| 2026-05-18 | `2026-05-18-migrate-execution-discipline.md` | Migrate EXECUTION_DISCIPLINE.md |
| 2026-05-18 | `2026-05-18-mcp-memory-flow-clarification.md` | AI Log — MCP and memory flow clarification |
| 2026-05-18 | `2026-05-18-map-visual-semantics-inputs-tools.md` | AI Log — Map visual semantics for inputs and tools |
| 2026-05-18 | `2026-05-18-map-top-menu-bottom-sheet.md` | AI Log — Map top menu and bottom sheet UX |
| 2026-05-18 | `2026-05-18-interactive-map-visual-hierarchy.md` | AI Log — Interactive map visual hierarchy update |
| 2026-05-18 | `2026-05-18-governance-ci-bootstrap.md` | Governance CI Bootstrap |
| 2026-05-18 | `2026-05-18-github-pages-interactive-map.md` | AI Log — GitHub Pages interactive map setup |
| 2026-05-18 | `2026-05-18-compact-mobile-map.md` | AI Log — Compact mobile map adjustment |
| 2026-05-18 | `2026-05-18-bubble-detail-bottom-sheet.md` | AI Log — Bubble detail bottom sheet |
| 2026-05-17 | `2026-05-17-status-roadmap-architecture-schema-reconcile.md` | Status / Roadmap / Architecture / Schema Reconcile |
| 2026-05-17 | `2026-05-17-status-changelog-alignment.md` | AI Log — Status and changelog alignment |
| 2026-05-17 | `2026-05-17-simple-tool-role-table.md` | AI Log — Simplified tool role table |
| 2026-05-17 | `2026-05-17-sensitive-examples-draft-status.md` | AI Log — Sensitive examples draft status |
| 2026-05-17 | `2026-05-17-rpg-assets-stable-fullwidth-final.md` | AI Log — RPG assets stable names and full-width README layout |
| 2026-05-17 | `2026-05-17-rpg-asset-stable-name-execution.md` | AI Log — Pantheon RPG stable asset names execution |
| 2026-05-17 | `2026-05-17-rpg-asset-rename-plan.md` | AI Log — Pantheon RPG asset rename plan |
| 2026-05-17 | `2026-05-17-rpg-asset-register-readme-integration.md` | AI Log — Pantheon RPG asset register and README integration |
| 2026-05-17 | `2026-05-17-readme-worked-example-samples.md` | AI Log — README worked-example samples |
| 2026-05-17 | `2026-05-17-readme-toc-worked-examples-reader-actions.md` | AI Log — README TOC, worked examples and reader-oriented next steps |
| 2026-05-17 | `2026-05-17-readme-professional-landing-structure.md` | AI Log — README professional landing structure |
| 2026-05-17 | `2026-05-17-readme-method-positioning.md` | AI Log — README method positioning |
| 2026-05-17 | `2026-05-17-readme-fr-rpg-fullwidth-sync.md` | AI Log — README.fr RPG full-width sync |
| 2026-05-17 | `2026-05-17-rag-ingestion-pipeline.md` | AI Log — RAG ingestion pipeline doctrine |
| 2026-05-17 | `2026-05-17-product-differentiation.md` | AI Log — Product differentiation doctrine |
| 2026-05-17 | `2026-05-17-practitioner-hooks-regulatory-watch.md` | AI Log — Practitioner hooks and regulatory watch example |
| 2026-05-17 | `2026-05-17-pattern-distillation-retry.md` | 2026-05-17 - Pattern Distillation Retry |
| 2026-05-17 | `2026-05-17-openwebui-knowledge-handoff.md` | AI Log — Governed OpenWebUI Knowledge handoff doctrine |
| 2026-05-17 | `2026-05-17-migrate-modules-governance-map.md` | Migrate MODULES.md as Governance Module Map |
| 2026-05-17 | `2026-05-17-migrate-code-audit-post-pivot.md` | Migrate CODE_AUDIT_POST_PIVOT.md |
| 2026-05-17 | `2026-05-17-markdown-dossier-workflow.md` | AI Log — Markdown dossier workflow governance proposal |
| 2026-05-17 | `2026-05-17-governance-college-readme.md` | AI Log — Governance College README integration |
| 2026-05-17 | `2026-05-17-external-repo-inspirations.md` | AI Log — External repository inspiration map |
| 2026-05-17 | `2026-05-17-external-agentic-skill-watchlist.md` | AI Log — External agentic inspirations and skill watchlist |
| 2026-05-17 | `2026-05-17-editorial-language-readme-captions.md` | AI Log — Editorial language and README caption pass |
| 2026-05-17 | `2026-05-17-dossier-flow-slogan.md` | AI Log — Dossier flow slogan update |
| 2026-05-17 | `2026-05-17-contracts-skill-watchlist.md` | AI Log — Contracts Skill Watchlist Entry |
| 2026-05-17 | `2026-05-17-context-pack-doctrine.md` | AI Log — Context Pack Doctrine Integration |
| 2026-05-16 | `2026-05-16-readme-visual-narrative-distribution.md` | AI Log — README visual narrative distribution |
| 2026-05-16 | `2026-05-16-readme-frontdoor-refactor.md` | AI Log — README front door and visual reading path refactor |
| 2026-05-16 | `2026-05-16-pantheon-rpg-visual-production-guides.md` | AI Log — Pantheon RPG visual production guides |
| 2026-05-16 | `2026-05-16-local-installation-and-governed-channels.md` | AI Log — local installation and governed channels framing |
| 2026-05-15 | `2026-05-15-readme-traceability-boundaries.md` | AI Log — README traceability and boundary clarification |
| 2026-05-15 | `2026-05-15-readme-rpg-board-links.md` | AI Log — README RPG board links |
| 2026-05-15 | `2026-05-15-readme-repetition-reduction.md` | AI Log — README repetition reduction and product narrative cleanup |
| 2026-05-15 | `2026-05-15-readme-professional-pitch-practical-usage.md` | AI Log — README professional pitch and practical usage |
| 2026-05-15 | `2026-05-15-readme-product-governance-layer.md` | AI Log — README product governance repositioning |
| 2026-05-15 | `2026-05-15-readme-control-mastery-positioning.md` | AI Log — README control and mastery positioning |
| 2026-05-15 | `2026-05-15-readme-anchor-narrative.md` | AI Log — README anchor narrative update |
| 2026-05-15 | `2026-05-15-readme-ai-adoption-objection.md` | AI Log — README AI adoption objection framing |
| 2026-05-15 | `2026-05-15-pantheon-rpg-city-memory-export-provenance.md` | Pantheon RPG City Memory Export Provenance Update |
| 2026-05-15 | `2026-05-15-bilingual-readme-professional-entry.md` | AI Log — Bilingual README professional entry |
| 2026-05-14 | `2026-05-14-workflow-language-stabilization.md` | AI Log — Workflow Language Stabilization |
| 2026-05-14 | `2026-05-14-pantheon-rpg-visual-system.md` | Pantheon RPG visual system |
| 2026-05-14 | `2026-05-14-pantheon-rpg-phase-1-prompt-workspace.md` | Pantheon RPG phase 1 prompt workspace |
| 2026-05-14 | `2026-05-14-pantheon-rpg-composition-study-prompt.md` | Pantheon RPG composition study prompt |
| 2026-05-14 | `2026-05-14-pantheon-rpg-city-memory-board.md` | Pantheon RPG city memory board |
| 2026-05-14 | `2026-05-14-integration-knowledge-scope-stabilization.md` | AI Log — 2026-05-14 — Integration, Knowledge and Scope Stabilization |
| 2026-05-13 | `2026-05-13-role-semantics-stabilization.md` | AI Log — Role Semantics Stabilization |
| 2026-05-13 | `2026-05-13-memory-governance-stabilization.md` | AI Log — Memory Governance Stabilization |
| 2026-05-13 | `2026-05-13-conceptual-stabilization-guardrail.md` | AI Log — Conceptual Stabilization Guardrail |
| 2026-05-13 | `2026-05-13-approval-doctrine-stabilization.md` | AI Log — Approval Doctrine Stabilization |
| 2026-05-12 | `2026-05-12-status-index-changelog-reconcile.md` | Status / Index / Changelog Reconcile |
| 2026-05-12 | `2026-05-12-pantheon-next-bootstrap.md` | Pantheon Next Bootstrap |
| 2026-05-12 | `2026-05-12-p0-7-hermes-iris-hephaistos.md` | P0.7 Hermes Profiles: IRIS and HEPHAISTOS |
| 2026-05-12 | `2026-05-12-p0-6d-ecosystem-stubs.md` | P0.6D Ecosystem Read-Order Stubs |
| 2026-05-12 | `2026-05-12-p0-6c-governance-safety-stubs.md` | P0.6C Governance Safety Stubs |
| 2026-05-12 | `2026-05-12-p0-6-read-order-stubs.md` | P0.6 Read Order Governance Stubs |
| 2026-05-12 | `2026-05-12-migration-playbook-proposal.md` | Migration Playbook Proposal (Phase C) |
| 2026-05-12 | `2026-05-12-migration-playbook-canonical.md` | Migration Playbook Canonical |
| 2026-05-12 | `2026-05-12-migrate-architecture.md` | Migrate ARCHITECTURE — Phase C Lot 1 gabarit |
| 2026-05-12 | `2026-05-12-governance-md-bootstrap-reconcile.md` | Governance Markdown Bootstrap Reconcile |
