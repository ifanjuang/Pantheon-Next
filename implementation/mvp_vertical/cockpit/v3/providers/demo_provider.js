// Cockpit — DemoProvider.
//
// Projects the fictional fixture into CockpitSnapshots. This is the demo half of
//
//   DemoProvider ─┐
//                 ├→ CockpitSnapshot → same cockpit
//   LiveProvider ─┘
//
// Pure data in, pure data out: no DOM, no Swiper, no rendering. The fixture is
// synthetic; nothing here is evidence, authority or an authorization.

import { createSnapshot } from "../collection/cockpit_snapshot.js";

const ROOT_ITEMS = Object.freeze([
  { id: "space:pantheon", title: "Pantheon", category: "Pantheon", family: "pantheon", status: "active", summary: "Contexte, gouvernance et décisions conséquentes.", details: "Pantheon gouverne ; il ne devient ni runtime, ni scheduler, ni moteur d’approbation automatique." },
  { id: "space:decisions", title: "Décisions", category: "Décisions", family: "decision", status: "review", summary: "Validations humaines et propositions à examiner." },
  { id: "space:affaires", title: "Affaires", category: "Projets", family: "project", status: "active", summary: "Projets, Informations, Contacts et Travaux." },
  { id: "space:connaissances", title: "Connaissances", category: "Références", family: "information", status: "neutral", summary: "Références réutilisables et état de revue." },
  { id: "space:outils", title: "Outils", category: "Outils", family: "tool", status: "neutral", summary: "Outils, skills, bindings et runtimes observés ou candidats." },
]);

function model(id, title, category, family, summary, statusValue = "neutral", details = "") {
  return { id, title, category, family, summary, status: statusValue, details };
}

export function createDemoProvider(fixture) {
  const currency = new Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR", maximumFractionDigits: 0 });

  function projectModels() {
    return fixture.projects.map(project => model(
      `project:${project.project_id}`,
      project.display_name || project.code,
      "Projet",
      "project",
      [project.code, project.phase, project.location].filter(Boolean).join(" · "),
      project.status || "active",
      [
        project.primary_client ? `Client : ${project.primary_client}` : null,
        project.claim_values?.budget_target != null ? `Budget cible : ${currency.format(project.claim_values.budget_target)}` : null,
        project.claim_values?.surface_projected != null ? `Surface projetée : ${project.claim_values.surface_projected} m²` : null,
      ].filter(Boolean).join("\n"),
    ));
  }

  function projectChildren(projectId) {
    const project = fixture.projects.find(item => item.project_id === projectId);
    const payload = fixture.project_payloads[projectId] || {};
    return [
      model(`contacts:${projectId}`, "Contacts", "Contacts", "contact", `${project?.contacts?.length || 0} contact(s)`, "neutral", (project?.contacts || []).map(item => [item.name, item.role, item.organization].filter(Boolean).join(" · ")).join("\n")),
      ...(payload.information || []).map(item => model(`information:${item.information_id}`, item.title, item.category || "Information", "information", item.summary, item.status, item.details || item.source_ref || "")),
      ...(payload.documents || []).map(item => model(`document:${item.document_id}`, item.title || item.naming?.object_name || "Document", item.naming?.document_type || "Document", "information", item.source_ref || "Document source", item.status || "ready", item.document_date || "")),
      ...(payload.knowledge || []).map(item => model(`knowledge:${item.knowledge_id}`, item.title, item.family || "Référence", "information", item.markdown || "Référence", item.review_status || "neutral", `Version ${item.version || 1}`)),
      ...(payload.work_issues || []).map(entry => {
        const item = entry.work_issue || entry;
        return model(`work:${item.issue_id}`, item.title, "Travail", "work", item.description || "Travail à traiter", item.status || "open", (item.tags || []).join(" · "));
      }),
    ];
  }

  function decisionModels() {
    return Object.values(fixture.project_payloads).flatMap(payload => (payload.change_candidates || []).map(item => model(
      `decision:${item.candidate_id}`,
      item.reason || "Modification à valider",
      "Décision",
      "decision",
      `Révision de base ${item.base_revision ?? "?"} · ${item.proposer || "Provenance non renseignée"}`,
      item.status || "pending_review",
      (item.changes || []).map(change => `${change.field}: ${change.before ?? "—"} → ${change.proposed ?? "—"}`).join("\n"),
    )));
  }

  function toolModels() {
    return (fixture.tool_catalog?.items || []).map(item => model(
      `tool:${item.tool_id}`,
      item.name || item.tool_id,
      item.category || "Outil",
      "tool",
      item.short_description || "Outil candidat",
      item.governance_state || "neutral",
      [
        `Installation : ${item.installation_state || "unknown"}`,
        `Santé : ${item.health_state || "unknown"}`,
        `Activation : ${item.activation_state || "unknown"}`,
        `Evidence : ${item.evidence_expectation || "À définir"}`,
      ].join("\n"),
    ));
  }

  function knowledgeModels() {
    return Object.values(fixture.project_payloads).flatMap(payload => (payload.knowledge || []).map(item => model(
      `knowledge:${item.knowledge_id}`,
      item.title,
      item.family || "Référence",
      "information",
      item.markdown || "Référence",
      item.review_status || "neutral",
      `Version ${item.version || 1}`,
    )));
  }

  // The root collection: the five primary spaces.
  function rootCollection() {
    return { id: "root", title: "Pantheon", canCreate: false, items: ROOT_ITEMS.slice() };
  }

  // The collection reachable by descending into `item`, or null.
  function collectionFor(item) {
    if (!item) return null;
    if (item.id === "space:affaires") return { id: "projects", title: "Affaires", canCreate: true, items: projectModels() };
    if (item.id === "space:decisions") return { id: "decisions", title: "Décisions", canCreate: false, items: decisionModels() };
    if (item.id === "space:connaissances") return { id: "knowledge", title: "Connaissances", canCreate: true, items: knowledgeModels() };
    if (item.id === "space:outils") return { id: "tools", title: "Outils", canCreate: true, items: toolModels() };
    if (item.id.startsWith("project:")) {
      const projectId = item.id.slice("project:".length);
      return { id: `project:${projectId}:children`, title: item.title, canCreate: true, items: projectChildren(projectId) };
    }
    return null;
  }

  // Wrap a collection into the versioned snapshot envelope.
  function toSnapshot(collection, { index = 0, path = [], space = null } = {}) {
    return createSnapshot({
      source: "demo",
      space,
      collection,
      items: collection?.items || [],
      index,
      path,
      warnings: ["Univers fictif : aucune donnée réelle, aucune autorisation."],
    });
  }

  return Object.freeze({ rootCollection, collectionFor, toSnapshot, rootItems: ROOT_ITEMS });
}
