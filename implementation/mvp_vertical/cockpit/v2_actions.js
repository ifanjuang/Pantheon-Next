(() => {
  "use strict";

  const $ = id => document.getElementById(id);
  const SUPPORTED = new Set(["Modifier avec Hermès", "Acter", "Nouvelle version", "Valider", "Refuser"]);
  const CARD_SELECTOR = "#v2-stage :is(.card, .v2-card)";
  const ENTITY_SELECTOR = ":is(.card-entity-id, .v2-entity-id)";
  const TITLE_SELECTOR = ":is(.card-title, .v2-card-title)";
  const ACTIONS_SELECTOR = ":is(.card-actions, .v2-card-actions) button";

  const key = prefix => `${prefix}-${globalThis.crypto?.randomUUID?.() || `${Date.now()}-${Math.random().toString(16).slice(2)}`}`;

  function credentials() {
    const token = $("v2-token")?.value?.trim() || "";
    const actor = $("v2-handoff-actor")?.value?.trim() || "";
    if (!token) throw new Error("Clé éditeur requise pour cette action.");
    if (!actor) throw new Error("Renseignez l’acteur humain dans le dock Hermès.");
    return { token, actor };
  }

  function currentIdentity() {
    const card = document.querySelector(CARD_SELECTOR);
    const entityId = card?.querySelector(ENTITY_SELECTOR)?.textContent?.trim() || "";
    const title = card?.querySelector(TITLE_SELECTOR)?.textContent?.trim() || entityId;
    if (!entityId) throw new Error("La carte courante n’expose pas d’identité stable.");
    return { entityId, title };
  }

  function informationId(entityId) {
    if (!entityId.startsWith("information:")) throw new Error("Cette action exige une Carte Information.");
    return entityId.slice("information:".length);
  }

  function workIssueId(entityId) {
    const prefix = "decision:work:";
    if (!entityId.startsWith(prefix)) throw new Error("Cette action exige une Carte Décision issue d’un Travail.");
    return entityId.slice(prefix.length);
  }

  async function request(path, { method = "GET", body = null } = {}) {
    const { token, actor } = credentials();
    const headers = {
      Authorization: `Bearer ${token}`,
      "X-Pantheon-Actor": actor,
      "X-Pantheon-Human-Actor": actor,
    };
    if (body !== null) headers["Content-Type"] = "application/json";
    const response = await fetch(path, {
      method,
      headers,
      body: body === null ? undefined : JSON.stringify(body),
    });
    const payload = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(payload.detail || response.statusText);
    return payload;
  }

  function nextIndex(value) {
    const match = String(value || "").trim().match(/^([A-Z]+)(\d+)$/i);
    if (!match) return "A01";
    const width = Math.max(2, match[2].length);
    return `${match[1].toUpperCase()}${String(Number(match[2]) + 1).padStart(width, "0")}`;
  }

  function reloadProject() {
    $("v2-load")?.click();
  }

  async function informationContextForCurrent() {
    const { entityId, title } = currentIdentity();
    const id = informationId(entityId);
    const payload = await request(`../v1/agency/information/${encodeURIComponent(id)}/context`);
    const context = payload.information_context || {};
    if (!context.current) throw new Error("L’Information courante n’est plus disponible.");
    return { id, title, context, current: context.current };
  }

  async function prepareHermesEdit() {
    const { title, current } = await informationContextForCurrent();
    if (!["draft", "in_progress"].includes(current.status)) {
      throw new Error("Hermès ne peut préparer une modification que sur une version de travail.");
    }
    const instruction = window.prompt(
      `Que doit faire Hermès sur « ${title} » ?`,
      "Améliorer, détailler et développer cette version de travail sans modifier ce qui est ACTÉ."
    );
    if (!instruction?.trim()) return;
    const question = $("v2-handoff-question");
    const descendants = $("v2-handoff-descendants");
    if (!question) throw new Error("Le dock Hermès n’est pas disponible.");
    question.value = instruction.trim();
    question.dispatchEvent(new Event("input", { bubbles: true }));
    if (descendants) descendants.checked = true;
    question.focus();
    $("v2-handoff-prepare")?.click();
  }

  async function actInformation() {
    const { id, title, current } = await informationContextForCurrent();
    if (!["draft", "in_progress"].includes(current.status)) {
      throw new Error("Seule une version de travail peut être actée.");
    }
    if (!window.confirm(`Acter « ${title} » ${current.index_label || ""} ?\n\nCette version deviendra immuable.`)) return;
    await request(`../v1/agency/information/${encodeURIComponent(id)}/act`, {
      method: "POST",
      body: { expected_revision: current.revision },
    });
    reloadProject();
  }

  async function deriveInformation() {
    const { id, title, current: acted } = await informationContextForCurrent();
    if (acted.status !== "acted") throw new Error("La nouvelle version doit dériver d’une Information ACTÉE.");

    const newIndex = window.prompt("Nouvel indice", nextIndex(acted.index_label));
    if (!newIndex?.trim()) return;
    const sourceRef = window.prompt(
      `Nouvelle source pour « ${title} »\n(fichier, email, dossier, URL… ; laisser vide pour une note)`,
      ""
    );
    let sourceNote = null;
    if (!sourceRef?.trim()) {
      sourceNote = window.prompt("Note / brouillon constituant la nouvelle source", "");
      if (!sourceNote?.trim()) return;
    }
    const sourceVersion = window.prompt("Version portée par la source (optionnel)", "") || null;

    await request(`../v1/agency/information/${encodeURIComponent(id)}/working-version`, {
      method: "POST",
      body: {
        new_index_label: newIndex.trim(),
        source_ref: sourceRef?.trim() || null,
        source_note: sourceNote?.trim() || null,
        source_version: sourceVersion?.trim() || null,
      },
    });
    reloadProject();
  }

  async function decide(action) {
    const { entityId, title } = currentIdentity();
    const issueId = workIssueId(entityId);
    const snapshot = await request(`../v1/work-issues/${encodeURIComponent(issueId)}/decision`);
    const issue = snapshot.work_issue;
    if (!snapshot.decision_available || issue?.status !== "review") {
      throw new Error("Cette décision n’est plus disponible dans l’état courant du Travail.");
    }

    const validate = action === "Valider";
    const message = validate
      ? `Valider « ${title} » et clôturer le Travail comme répondu ?`
      : `Refuser « ${title} » et renvoyer le Travail en cours ?`;
    if (!window.confirm(message)) return;

    await request(`../v1/work-issues/${encodeURIComponent(issueId)}/decision/${validate ? "validate" : "refuse"}`, {
      method: "POST",
      body: {
        expected_version: issue.version,
        idempotency_key: key(validate ? "decision-validate" : "decision-refuse"),
      },
    });
    reloadProject();
  }

  async function runAction(label) {
    if (label === "Modifier avec Hermès") return prepareHermesEdit();
    if (label === "Acter") return actInformation();
    if (label === "Nouvelle version") return deriveInformation();
    if (label === "Valider" || label === "Refuser") return decide(label);
  }

  function enableRenderedActions(root = document) {
    for (const button of root.querySelectorAll?.(ACTIONS_SELECTOR) || []) {
      if (!SUPPORTED.has(button.textContent?.trim())) continue;
      button.disabled = false;
      button.title = "";
      button.dataset.cardAction = button.textContent.trim();
    }
  }

  function install() {
    const stage = $("v2-stage");
    if (!stage) return;
    enableRenderedActions(stage);
    new MutationObserver(() => enableRenderedActions(stage)).observe(stage, { childList: true, subtree: true });
    stage.addEventListener("click", event => {
      const button = event.target.closest?.("button[data-card-action]");
      if (!button) return;
      event.preventDefault();
      button.disabled = true;
      void runAction(button.dataset.cardAction)
        .catch(error => window.alert(error.message || String(error)))
        .finally(() => enableRenderedActions(stage));
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", install, { once: true });
  else install();
})();