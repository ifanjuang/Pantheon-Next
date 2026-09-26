const STATUS = {
  COMPLETE: { label: "Complet", color: "#287652" },
  CHECK: { label: "À vérifier", color: "#a76800" },
  CARTOUCHE_MISSING: { label: "Cartouche manquant", color: "#6648a8" },
  SOURCE_MISSING: { label: "Source manquante", color: "#a53535" },
  FOLDER: { label: "Dossier", color: "#315d9c" },
};

const state = { data: null, workspace: "all", status: "all", query: "" };
const elements = Object.fromEntries(
  ["package-count", "status-counts", "workspace-tabs", "status-filters", "search", "refresh", "loading", "error", "cards", "empty"]
    .map((id) => [id, document.getElementById(id)]),
);

const escapeHtml = (value) => String(value ?? "")
  .replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;").replaceAll("'", "&#039;");

function tagTemplate(tag) {
  return `<span class="tag">${escapeHtml(tag)}</span>`;
}

function tagsTemplate(tags) {
  if (!Array.isArray(tags) || tags.length === 0) return "";
  return `<div class="tags" aria-label="Tags">${tags.map(tagTemplate).join("")}</div>`;
}

function fact(label, value, stateClass = "") {
  if (value === null || value === undefined || value === "") return "";
  return `<div class="fact ${stateClass}"><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong></div>`;
}

function documentCardBody(card) {
  const details = [
    card.document_type,
    card.phase,
    card.index ? `Indice ${card.index}` : "",
    card.document_date,
  ].filter(Boolean);

  const summary = card.summary
    ? `<p class="card-summary">${escapeHtml(card.summary)}</p>`
    : "";

  const facts = [
    fact("Chemin", card.path),
    fact("Source", card.source_present ? (card.source || card.name) : "Manquante", card.source_present ? "" : "fact-alert"),
    fact("Cartouche", card.cartouche_present ? card.cartouche : "Absent", card.cartouche_present ? "" : "fact-alert"),
    fact("Identité", card.document_id),
    fact("Émetteur", card.issuer),
    fact(
      card.revision_mode === "supersedes" ? "Remplace" : card.revision_mode === "supplements" ? "Complète" : "Relation",
      card.revision_of,
      card.revision_target_status === "MISSING" || card.revision_target_status === "AMBIGUOUS" ? "fact-alert" : "",
    ),
  ].join("");

  const generate = card.can_generate_cartouche
    ? `<div class="card-action">
        <button type="button" disabled title="La route d’écriture du cartouche n’est pas encore qualifiée">Générer le cartouche</button>
        <small>Action visible, écriture non activée dans cette tranche.</small>
      </div>`
    : "";

  const reconcile = card.status === "COMPLETE"
    && card.document_id
    && card.hindsight_representation_candidate === "source"
    ? `<div class="reconcile-action" data-reconcile-document="${escapeHtml(card.document_id)}">
        <label>
          <span>Focus optionnel</span>
          <input type="text" maxlength="2000" data-reconcile-focus placeholder="Ex. vérifier les contradictions de dates">
        </label>
        <button type="button" data-reconcile-button>Réconcilier avec Hermes</button>
        <small>Analyse transitoire de la mémoire Hindsight. La source NAS n’est pas ouverte.</small>
        <div class="reconcile-result" data-reconcile-result hidden></div>
      </div>`
    : "";

  return `
    <div class="document-meta">
      <span class="file-type">${escapeHtml(card.extension || "FILE")}</span>
      ${details.length ? `<span>${escapeHtml(details.join(" · "))}</span>` : ""}
    </div>
    ${summary}
    ${tagsTemplate(card.tags)}
    <div class="facts">${facts}</div>
    ${reconcile}
    ${generate}
  `;
}

function folderCardBody(card) {
  const summary = card.summary
    ? `<p class="card-summary">${escapeHtml(card.summary)}</p>`
    : `<p class="card-summary muted">Contexte de dossier non renseigné.</p>`;
  const facts = [
    fact("Chemin", card.path),
    fact("Cartouche dossier", card.folder_context_present ? (card.folder_context || "_folder.md") : "Absent", card.folder_context_present ? "" : "fact-muted"),
    fact("Phase", card.phase),
    fact("Projet", card.project),
  ].join("");
  const contextBadge = card.folder_context_present
    ? '<span class="folder-context-state is-present">Cartouche présent</span>'
    : '<span class="folder-context-state is-missing">Sans _folder.md</span>';
  return `
    <div class="document-meta"><span class="file-type">DOSSIER</span>${contextBadge}</div>
    ${summary}
    ${tagsTemplate(card.tags)}
    <div class="facts">${facts}</div>
  `;
}

function cardTemplate(card) {
  const warnings = card.warnings?.length
    ? `<ul class="warnings">${card.warnings.map((warning) => `<li>${escapeHtml(warning)}</li>`).join("")}</ul>`
    : "";
  const body = card.kind === "folder" ? folderCardBody(card) : documentCardBody(card);
  const classes = [
    "card",
    card.kind === "folder" ? "folder-card" : "document-card",
    card.status === "CARTOUCHE_MISSING" ? "missing-cartouche" : "",
    card.status === "SOURCE_MISSING" ? "missing-source" : "",
  ].filter(Boolean).join(" ");

  return `<article class="${classes}" data-status="${escapeHtml(card.status)}">
    <div class="card-head">
      <div class="card-kicker">
        <span>${escapeHtml(card.workspace)}</span>
        <span class="status">${escapeHtml(STATUS[card.status]?.label || card.status)}</span>
      </div>
      <h2>${escapeHtml(card.title || card.name)}</h2>
      <p class="subtitle">${escapeHtml(card.subtitle || "")}</p>
    </div>
    ${body}
    ${warnings}
  </article>`;
}

function allCards() {
  return state.data.workspaces.flatMap((workspace) => workspace.cards);
}

function renderCards() {
  const query = state.query.trim().toLocaleLowerCase("fr");
  const cards = allCards().filter((card) => {
    const workspaceMatch = state.workspace === "all" || card.workspace === state.workspace;
    const statusMatch = state.status === "all" || card.status === state.status;
    const text = [
      card.name,
      card.title,
      card.subtitle,
      card.summary,
      card.path,
      card.source,
      card.cartouche,
      card.revision_mode,
      card.revision_of,
      ...(card.tags || []),
    ].filter(Boolean).join(" ").toLocaleLowerCase("fr");
    return workspaceMatch && statusMatch && (!query || text.includes(query));
  });
  elements.cards.innerHTML = cards.map(cardTemplate).join("");
  elements.cards.hidden = cards.length === 0;
  elements.empty.hidden = cards.length !== 0;
}

function tabsTemplate() {
  const tabs = [{ name: "all", label: "Tous" }, ...state.data.workspaces.map((item) => ({ name: item.name, label: item.name }))];
  elements["workspace-tabs"].innerHTML = tabs.map((tab) =>
    `<button class="tab" type="button" data-workspace="${escapeHtml(tab.name)}" aria-selected="${state.workspace === tab.name}">${escapeHtml(tab.label)}</button>`,
  ).join("");
}

function filtersTemplate() {
  const filters = [{ name: "all", label: "Tous les états" }, ...Object.entries(STATUS).map(([name, item]) => ({ name, label: item.label }))];
  elements["status-filters"].innerHTML = filters.map((filter) =>
    `<button class="filter" type="button" data-status="${filter.name}" aria-pressed="${state.status === filter.name}">${filter.label}</button>`,
  ).join("");
}

function renderSummary() {
  elements["package-count"].textContent = state.data.item_count ?? state.data.package_count ?? 0;
  elements["status-counts"].innerHTML = Object.entries(STATUS).map(([name, item]) =>
    `<div class="count" style="--state:${item.color}"><strong>${state.data.totals[name] || 0}</strong><span>${item.label}</span></div>`,
  ).join("");
}

async function load() {
  elements.loading.hidden = false;
  elements.error.hidden = true;
  elements.cards.hidden = true;
  elements.empty.hidden = true;
  elements.refresh.disabled = true;
  try {
    const response = await fetch("/api/workspaces", { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    state.data = await response.json();
    renderSummary(); tabsTemplate(); filtersTemplate(); renderCards();
  } catch (error) {
    elements.error.textContent = "Impossible de lire AFFAIRES. Vérifiez le service, le montage NAS et ses permissions.";
    elements.error.hidden = false;
  } finally {
    elements.loading.hidden = true;
    elements.refresh.disabled = false;
  }
}

function reconciliationFindingNode(finding) {
  const item = document.createElement("li");
  const title = document.createElement("strong");
  title.textContent = `${finding.category} — ${finding.summary || "Constat"}`;
  const detail = document.createElement("p");
  detail.textContent = finding.detail || "";
  item.append(title, detail);
  if (finding.suggestion) {
    const suggestion = document.createElement("p");
    suggestion.className = "reconcile-suggestion";
    suggestion.textContent = `Proposition : ${finding.suggestion}`;
    item.append(suggestion);
  }
  const refs = [...(finding.memory_refs || []), ...(finding.chunk_refs || [])];
  if (refs.length) {
    const ref = document.createElement("small");
    ref.textContent = `Références : ${refs.join(", ")}`;
    item.append(ref);
  }
  return item;
}

function renderReconciliationResult(container, result) {
  container.replaceChildren();
  const summary = document.createElement("p");
  summary.className = "reconcile-summary";
  summary.textContent = result.summary || "Analyse terminée.";
  container.append(summary);
  const findings = Array.isArray(result.findings) ? result.findings : [];
  if (findings.length) {
    const list = document.createElement("ol");
    list.className = "reconcile-findings";
    for (const finding of findings) list.append(reconciliationFindingNode(finding));
    container.append(list);
  } else {
    const empty = document.createElement("p");
    empty.className = "reconcile-empty";
    empty.textContent = "Aucune incohérence bornée relevée dans les éléments transmis.";
    container.append(empty);
  }
  const boundary = document.createElement("small");
  const chunks = result.inputs?.hindsight_chunks_sent ?? 0;
  const memories = result.inputs?.hindsight_memories_sent ?? 0;
  boundary.textContent = `Hindsight uniquement · ${chunks} chunks · ${memories} mémoires · source NAS non ouverte · aucune écriture`;
  container.append(boundary);
  container.hidden = false;
}

async function runMemoryReconciliation(action) {
  const button = action.querySelector("[data-reconcile-button]");
  const input = action.querySelector("[data-reconcile-focus]");
  const resultNode = action.querySelector("[data-reconcile-result]");
  const documentId = action.dataset.reconcileDocument;
  if (!button || !input || !resultNode || !documentId) return;
  button.disabled = true;
  button.textContent = "Analyse…";
  resultNode.hidden = true;
  resultNode.replaceChildren();
  try {
    const response = await fetch(`/api/documents/${encodeURIComponent(documentId)}/reconcile-memory`, {
      method: "POST",
      cache: "no-store",
      headers: {
        "Content-Type": "application/json",
        "X-Pantheon-Intent": "memory-reconcile",
      },
      body: JSON.stringify({ focus: input.value.trim() }),
    });
    const payload = await response.json();
    if (!response.ok) throw new Error(payload.detail || payload.error || `HTTP ${response.status}`);
    renderReconciliationResult(resultNode, payload);
  } catch (error) {
    const message = document.createElement("p");
    message.className = "reconcile-error";
    message.textContent = `Réconciliation impossible : ${error.message || error}`;
    resultNode.replaceChildren(message);
    resultNode.hidden = false;
  } finally {
    button.disabled = false;
    button.textContent = "Réconcilier avec Hermes";
  }
}

elements.cards.addEventListener("click", (event) => {
  const button = event.target.closest("[data-reconcile-button]");
  if (!button) return;
  const action = button.closest("[data-reconcile-document]");
  if (action) void runMemoryReconciliation(action);
});

elements.search.addEventListener("input", (event) => { state.query = event.target.value; renderCards(); });
elements.refresh.addEventListener("click", load);
elements["workspace-tabs"].addEventListener("click", (event) => {
  const button = event.target.closest("[data-workspace]");
  if (!button) return;
  state.workspace = button.dataset.workspace; tabsTemplate(); renderCards();
});
elements["status-filters"].addEventListener("click", (event) => {
  const button = event.target.closest("[data-status]");
  if (!button) return;
  state.status = button.dataset.status; filtersTemplate(); renderCards();
});

load();

const ROLE_ICONS = Object.freeze({ Athena: "🦉", Argos: "🔎", Themis: "⚖", Apollo: "☀", Hephaistos: "🛠", Iris: "📨", Zeus: "⚡", Mnemosyne: "🧠", Hermes: "⚙" });
const ROLE_ORDER = Object.freeze(["Athena", "Argos", "Hermes", "Hephaistos", "Themis", "Apollo", "Zeus", "Iris", "Mnemosyne"]);
const roleView = {
  runId: "", cursor: 0, controller: null, stages: new Map(), stageEvents: new Map(), observedOrder: new Map(),
  observationCounter: 0, activeView: "dialogue", selectedStageId: "",
  state: document.getElementById("role-dialogue-state"),
  events: document.getElementById("role-dialogue-events"),
  graph: document.getElementById("role-graph"),
  graphLanes: document.getElementById("role-graph-lanes"),
  graphDetail: document.getElementById("role-graph-detail"),
};

function roleState(value) { roleView.state.textContent = value; }

function roleStageSort(left, right) {
  const leftSequence = Number(left?.sequence);
  const rightSequence = Number(right?.sequence);
  const leftHasSequence = Number.isSafeInteger(leftSequence);
  const rightHasSequence = Number.isSafeInteger(rightSequence);
  if (leftHasSequence && rightHasSequence && leftSequence !== rightSequence) return leftSequence - rightSequence;
  return (roleView.observedOrder.get(left.stage_id) ?? 0) - (roleView.observedOrder.get(right.stage_id) ?? 0);
}

function orderedRoleStages() { return [...roleView.stageEvents.values()].sort(roleStageSort); }

function visibleRoleOrder(events) {
  const present = new Set(events.map((event) => event.visible_role));
  return [...ROLE_ORDER.filter(role => present.has(role)), ...[...present].filter(role => !ROLE_ORDER.includes(role))];
}

function renderRoleGraphDetail(event) {
  roleView.graphDetail.replaceChildren();
  if (!event) {
    const empty = document.createElement("p");
    empty.className = "role-graph-detail-empty";
    empty.textContent = "Sélectionnez un jalon pour afficher ses détails observables.";
    roleView.graphDetail.append(empty);
    return;
  }
  const head = document.createElement("div");
  head.className = "role-graph-detail-head";
  const title = document.createElement("strong");
  title.textContent = `${event.visible_role} — ${event.semantic_function || event.role_family || "Jalon"}`;
  const status = document.createElement("span");
  status.textContent = event.phase === "completed" ? "terminé" : "en cours";
  head.append(title, status);
  const summary = document.createElement("p");
  summary.className = "role-graph-detail-summary";
  summary.textContent = event.summary || "Jalon public observé.";
  const origin = document.createElement("p");
  origin.className = "role-graph-detail-origin";
  origin.textContent = event.projection === "derived_transient"
    ? "Projection transitoire dérivée du flux public Hermes."
    : "Événement structuré émis par le runtime.";
  roleView.graphDetail.append(head, summary, origin);
  const entries = Object.entries(event.details || {}).filter(([, value]) => value != null && value !== "");
  if (entries.length) {
    const list = document.createElement("dl");
    for (const [key, value] of entries) {
      const dt = document.createElement("dt");
      const dd = document.createElement("dd");
      dt.textContent = key.replaceAll("_", " ");
      dd.textContent = String(value);
      list.append(dt, dd);
    }
    roleView.graphDetail.append(list);
  }
}

function renderRoleGraph() {
  const events = orderedRoleStages();
  roleView.graphLanes.replaceChildren();
  if (!events.length) {
    const empty = document.createElement("p");
    empty.className = "role-graph-empty";
    empty.textContent = "Aucun jalon observable pour cette exécution.";
    roleView.graphLanes.append(empty);
    renderRoleGraphDetail(null);
    return;
  }

  const stageColumns = new Map(events.map((event, index) => [event.stage_id, index + 1]));
  for (const role of visibleRoleOrder(events)) {
    const lane = document.createElement("div");
    lane.className = "role-graph-lane";
    const label = document.createElement("div");
    label.className = "role-graph-label";
    const icon = document.createElement("span");
    icon.setAttribute("aria-hidden", "true");
    icon.textContent = ROLE_ICONS[role] || "•";
    const name = document.createElement("strong");
    name.textContent = role;
    label.append(icon, name);

    const rail = document.createElement("div");
    rail.className = "role-graph-rail";
    rail.style.gridTemplateColumns = `repeat(${events.length}, 3.1rem)`;
    for (const event of events.filter(candidate => candidate.visible_role === role)) {
      const node = document.createElement("button");
      node.type = "button";
      node.className = "role-graph-node";
      node.style.gridColumn = String(stageColumns.get(event.stage_id));
      node.dataset.phase = event.phase || "updated";
      node.dataset.projection = event.projection || "native";
      node.classList.toggle("is-selected", event.stage_id === roleView.selectedStageId);
      node.textContent = ROLE_ICONS[role] || "•";
      node.title = event.summary || `${role} — jalon observable`;
      node.setAttribute("aria-label", `${role}, ${event.semantic_function || event.role_family || "jalon"}, ${event.summary || "jalon public observé"}`);
      node.addEventListener("click", () => {
        roleView.selectedStageId = event.stage_id;
        renderRoleGraph();
      });
      rail.append(node);
    }
    lane.append(label, rail);
    roleView.graphLanes.append(lane);
  }

  if (roleView.selectedStageId && !roleView.stageEvents.has(roleView.selectedStageId)) roleView.selectedStageId = "";
  renderRoleGraphDetail(roleView.selectedStageId ? roleView.stageEvents.get(roleView.selectedStageId) : null);
}

function setRoleTraceView(view) {
  roleView.activeView = view === "graph" ? "graph" : "dialogue";
  roleView.events.hidden = roleView.activeView !== "dialogue";
  roleView.graph.hidden = roleView.activeView !== "graph";
  for (const button of document.querySelectorAll("[data-role-trace-view]")) {
    const selected = button.dataset.roleTraceView === roleView.activeView;
    button.setAttribute("aria-selected", String(selected));
    button.tabIndex = selected ? 0 : -1;
  }
  if (roleView.activeView === "graph") renderRoleGraph();
}

function renderRoleStage(event) {
  if (!event?.stage_id || !event?.visible_role) return;
  if (!roleView.observedOrder.has(event.stage_id)) roleView.observedOrder.set(event.stage_id, roleView.observationCounter++);
  roleView.stageEvents.set(event.stage_id, { ...event });
  let item = roleView.stages.get(event.stage_id);
  if (!item) {
    item = document.createElement("li");
    item.className = "role-stage";
    roleView.stages.set(event.stage_id, item);
    roleView.events.append(item);
  }
  item.dataset.phase = event.phase || "updated";
  item.replaceChildren();
  const icon = document.createElement("span"); icon.className = "role-stage-icon"; icon.setAttribute("aria-hidden", "true"); icon.textContent = ROLE_ICONS[event.visible_role] || "•";
  const title = document.createElement("strong"); title.className = "role-stage-title"; title.textContent = `${event.visible_role} — ${event.semantic_function || event.role_family || "Jalon"}`;
  const status = document.createElement("span"); status.className = "role-stage-status"; status.textContent = event.phase === "completed" ? "terminé" : "en cours";
  const summary = document.createElement("p"); summary.className = "role-stage-summary"; summary.textContent = event.summary || "Jalon public observé.";
  const origin = document.createElement("span"); origin.className = "role-stage-origin"; origin.textContent = event.projection === "derived_transient" ? "Dérivé du flux public" : "Événement natif";
  item.append(icon, title, status, summary, origin);
  if (roleView.activeView === "graph") renderRoleGraph();
}

function consumeRoleBlock(block) {
  let kind = "message";
  let id = 0;
  const data = [];
  for (const line of block.split("\n")) {
    if (line.startsWith("event:")) kind = line.slice(6).trim();
    else if (line.startsWith("id:")) id = Number(line.slice(3).trim());
    else if (line.startsWith("data:")) data.push(line.slice(5).trimStart());
  }
  if (!data.length) return;
  const event = JSON.parse(data.join("\n"));
  if (Number.isSafeInteger(id) && id > roleView.cursor) roleView.cursor = id;
  if (kind === "role.stage") renderRoleStage(event);
  else if (kind === "role.trace.error") roleState("Rejeu incomplet");
}

async function followRoleTrace(runId) {
  if (!runId) return;
  if (runId !== roleView.runId) {
    roleView.controller?.abort();
    roleView.runId = runId;
    roleView.cursor = 0;
    roleView.observationCounter = 0;
    roleView.selectedStageId = "";
    roleView.stages.clear();
    roleView.stageEvents.clear();
    roleView.observedOrder.clear();
    roleView.events.replaceChildren();
    roleView.graphLanes.replaceChildren();
    roleView.graphDetail.replaceChildren();
  }
  roleView.controller = new AbortController();
  const headers = roleView.cursor ? { "Last-Event-ID": String(roleView.cursor) } : {};
  try {
    roleState("En direct");
    const response = await fetch(`/api/role-traces/${encodeURIComponent(runId)}/events`, { headers, cache: "no-store", signal: roleView.controller.signal });
    if (!response.ok || !response.body) throw new Error(`HTTP ${response.status}`);
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let buffer = "";
    while (true) {
      const { value, done } = await reader.read();
      buffer += decoder.decode(value || new Uint8Array(), { stream: !done }).replaceAll("\r\n", "\n");
      let end;
      while ((end = buffer.indexOf("\n\n")) >= 0) {
        const block = buffer.slice(0, end); buffer = buffer.slice(end + 2);
        if (block.trim()) consumeRoleBlock(block);
      }
      if (done) break;
    }
    roleState("Terminé");
  } catch (error) {
    if (error?.name !== "AbortError") roleState("Trace indisponible");
  }
}

async function discoverLatestRoleTrace() {
  try {
    const response = await fetch("/api/role-traces/latest", { cache: "no-store" });
    if (response.status === 404) { roleState("Aucune trace"); return; }
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const trace = await response.json();
    if (trace.run_id && trace.run_id !== roleView.runId) void followRoleTrace(trace.run_id);
  } catch (_error) {
    roleState("Relais indisponible");
  }
}

for (const button of document.querySelectorAll("[data-role-trace-view]")) {
  button.addEventListener("click", () => setRoleTraceView(button.dataset.roleTraceView));
}
setRoleTraceView("dialogue");
void discoverLatestRoleTrace();
window.setInterval(discoverLatestRoleTrace, 5000);
