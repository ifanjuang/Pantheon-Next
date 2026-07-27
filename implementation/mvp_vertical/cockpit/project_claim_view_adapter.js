(() => {
  "use strict";

  const $ = id => document.getElementById(id);
  let schemaPromise = null;

  function token() {
    return $("v2-token")?.value || "";
  }

  async function request(path) {
    const response = await fetch(path, {
      headers: { Authorization: `Bearer ${token()}` },
      cache: "no-store",
    });
    const payload = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(payload.detail || response.statusText);
    return payload;
  }

  function schema() {
    if (!schemaPromise) {
      schemaPromise = request("../v1/agency/schema/project")
        .then(payload => payload.schema || null)
        .catch(error => {
          schemaPromise = null;
          throw error;
        });
    }
    return schemaPromise;
  }

  function projectId(card) {
    const entityId = card.querySelector(".v2-entity-id")?.textContent?.trim() || "";
    return entityId.startsWith("project:") && !entityId.endsWith(":contacts")
      ? entityId.slice("project:".length)
      : "";
  }

  function hasValue(value) {
    return !(value == null || value === "" || (Array.isArray(value) && value.length === 0));
  }

  function formatValue(field, value) {
    if (Array.isArray(value)) return value.join(" · ");
    if (field?.unit === "EUR" && typeof value === "number") {
      return new Intl.NumberFormat("fr-FR", {
        style: "currency",
        currency: "EUR",
        maximumFractionDigits: 0,
      }).format(value);
    }
    if (field?.unit === "m²" && typeof value === "number") {
      return `${new Intl.NumberFormat("fr-FR", { maximumFractionDigits: 2 }).format(value)} m²`;
    }
    return String(value);
  }

  function provenanceLabel(ref) {
    const first = Array.isArray(ref) ? ref[0] : ref;
    if (!first || typeof first !== "object") return "";
    const backing = first.backing_ref || {};
    const provenance = first.provenance || {};
    const pieces = [
      first.status,
      backing.entity_type && backing.entity_id ? `${backing.entity_type}:${backing.entity_id}` : null,
      provenance.source_ref || null,
    ].filter(Boolean);
    return pieces.join(" · ");
  }

  function renderProjection(card, project, projectSchema) {
    const body = card.querySelector(".v2-card-back .v2-back-body");
    if (!body) return;
    body.querySelectorAll("[data-project-claim-projection]").forEach(node => node.remove());

    const values = project.claim_values && typeof project.claim_values === "object"
      ? project.claim_values
      : {};
    const refs = project.claim_refs && typeof project.claim_refs === "object"
      ? project.claim_refs
      : {};

    for (const field of projectSchema?.fields || []) {
      if (field.storage !== "projection" || field.semantics !== "claim") continue;
      const claimType = field.claim_type || field.key;
      const value = values[claimType];
      if (!hasValue(value)) continue;

      const section = document.createElement("section");
      section.className = "v2-back-section";
      section.dataset.projectClaimProjection = field.key;
      const heading = document.createElement("h3");
      heading.textContent = field.title || field.label || field.key;
      const content = document.createElement("p");
      content.textContent = formatValue(field, value);
      const provenance = provenanceLabel(refs[claimType]);
      if (provenance) {
        section.title = `Provenance : ${provenance}`;
        section.dataset.claimProvenance = provenance;
      }
      section.append(heading, content);
      body.append(section);
    }
  }

  async function enhance(card) {
    if (card.dataset.family !== "project" || card.dataset.claimProjectionState) return;
    const id = projectId(card);
    if (!id || !token()) return;
    card.dataset.claimProjectionState = "loading";
    try {
      const [projectSchema, payload] = await Promise.all([
        schema(),
        request(`../v1/agency/projects/${encodeURIComponent(id)}`),
      ]);
      renderProjection(card, payload.project || {}, projectSchema);
      card.dataset.claimProjectionState = "ready";
    } catch (error) {
      card.dataset.claimProjectionState = "error";
      card.dataset.claimProjectionError = error.message || String(error);
    }
  }

  function scan(root = document) {
    for (const card of root.querySelectorAll?.(".v2-card[data-family='project']") || []) {
      void enhance(card);
    }
  }

  function install() {
    const stage = $("v2-stage");
    if (!stage) return;
    scan(stage);
    new MutationObserver(() => scan(stage)).observe(stage, { childList: true, subtree: true });
    $("v2-load")?.addEventListener("click", () => { schemaPromise = null; });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", install, { once: true });
  else install();
})();
