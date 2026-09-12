const STATUS = {
  COHERENT: { label: "Cohérent", color: "#287652" },
  CHECK: { label: "À vérifier", color: "#a76800" },
  INVALID: { label: "Invalide", color: "#a53535" },
  QUALIFIABLE: { label: "Qualifiable", color: "#6648a8" },
  FREE: { label: "Libre", color: "#7a7d83" },
};

const state = { data: null, workspace: "all", status: "all", query: "" };
const elements = Object.fromEntries(
  ["package-count", "status-counts", "workspace-tabs", "status-filters", "search", "refresh", "loading", "error", "cards", "empty"]
    .map((id) => [id, document.getElementById(id)]),
);

const escapeHtml = (value) => String(value ?? "")
  .replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;")
  .replaceAll('"', "&quot;").replaceAll("'", "&#039;");

function resource(label, value) {
  return `<div class="resource"><strong>${Number(value || 0)}</strong><span>${label}</span></div>`;
}

function cardTemplate(card) {
  const warnings = card.warnings?.length
    ? `<ul class="warnings">${card.warnings.map((warning) => `<li>${escapeHtml(warning)}</li>`).join("")}</ul>`
    : "";
  return `<article class="card" data-status="${escapeHtml(card.status)}">
    <div class="card-head">
      <div class="card-kicker"><span>${escapeHtml(card.workspace)}</span><span class="status">${STATUS[card.status]?.label || card.status}</span></div>
      <h2>${escapeHtml(card.name)}</h2>
      <p class="subtitle">${escapeHtml(card.subtitle)}</p>
    </div>
    <div class="resource-grid">
      ${resource("Markdown", card.resources.markdown)}${resource("PDF", card.resources.pdf)}
      ${resource("Images", card.resources.images)}${resource("Tableaux", card.resources.tables)}
    </div>
    <div class="facts">
      <div class="fact"><span>Chemin</span><strong>${escapeHtml(card.path)}</strong></div>
      <div class="fact"><span>Manifeste</span><strong>${escapeHtml(card.manifest || "Absent")}</strong></div>
      <div class="fact"><span>Document principal</span><strong>${escapeHtml(card.primary_markdown || "Non détecté")}</strong></div>
    </div>${warnings}
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
    const text = `${card.name} ${card.subtitle} ${card.path}`.toLocaleLowerCase("fr");
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
  elements["package-count"].textContent = state.data.package_count;
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
    elements.error.textContent = "Impossible de lire les miroirs locaux. Vérifiez le service et ses permissions.";
    elements.error.hidden = false;
  } finally {
    elements.loading.hidden = true;
    elements.refresh.disabled = false;
  }
}

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
