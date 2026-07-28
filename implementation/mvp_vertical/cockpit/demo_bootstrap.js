const nativeFetch = window.fetch.bind(window);
const fixtureResponse = payload => new Response(JSON.stringify(payload), {
  status: 200,
  headers: { "Content-Type": "application/json; charset=utf-8" },
});

const fixture = await nativeFetch("demo-data.json", { cache: "no-store" }).then(response => {
  if (!response.ok) throw new Error(`Fixture indisponible (${response.status})`);
  return response.json();
});

function projectPayload(projectId) {
  return fixture.project_payloads[projectId] || {
    information: [],
    documents: [],
    knowledge: [],
    work_issues: [],
    change_candidates: [],
  };
}

window.PANTHEON_COCKPIT_DEMO = true;
window.fetch = async (input, init = {}) => {
  const raw = typeof input === "string" ? input : input.url;
  const url = new URL(raw, window.location.href);
  const method = String(init.method || "GET").toUpperCase();

  if (method !== "GET") {
    return new Response(JSON.stringify({ detail: "Démonstration statique : écriture désactivée" }), {
      status: 405,
      headers: { "Content-Type": "application/json; charset=utf-8" },
    });
  }

  if (url.pathname.endsWith("/tool_catalog.json")) return fixtureResponse(fixture.tool_catalog);
  if (url.pathname.endsWith("/v1/agency/projects")) return fixtureResponse({ projects: fixture.projects });
  if (url.pathname.endsWith("/v1/agency/schema/project")) return fixtureResponse({ schema: fixture.project_schema });

  const agencyProject = url.pathname.match(/\/v1\/agency\/projects\/([^/]+)\/(information|change-candidates)$/);
  if (agencyProject) {
    const projectId = decodeURIComponent(agencyProject[1]);
    const payload = projectPayload(projectId);
    return agencyProject[2] === "information"
      ? fixtureResponse({ information: payload.information })
      : fixtureResponse({ change_candidates: payload.change_candidates });
  }

  const projectResource = url.pathname.match(/\/v1\/projects\/([^/]+)\/(documents|knowledge|work-issues)$/);
  if (projectResource) {
    const projectId = decodeURIComponent(projectResource[1]);
    const payload = projectPayload(projectId);
    if (projectResource[2] === "documents") return fixtureResponse({ documents: payload.documents });
    if (projectResource[2] === "knowledge") return fixtureResponse({ knowledge: payload.knowledge });
    return fixtureResponse({ work_issues: payload.work_issues });
  }

  if (url.pathname.includes("/v1/context")) {
    return fixtureResponse({ results: [], selected: [], message: "Démo statique : recherche serveur non simulée." });
  }

  return nativeFetch(input, init);
};

const scripts = [
  "structured_interface.js",
  "context_resolver.js",
  "agency_data_binding.js",
  "spatial_navigation.js",
  "v2_app_schema.js",
  "v2_interaction_policy.js",
  "project_claim_view_adapter.js",
  "information_view_adapter.js",
  "v2_context.js",
  "v2_handoff.js",
  "v2_actions.js",
  "v2_candidate_actions.js",
  "schema_editor.js",
  "contacts_editor.js",
  "information_create.js",
];

for (const src of scripts) {
  await new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.src = src;
    script.onload = resolve;
    script.onerror = () => reject(new Error(`Impossible de charger ${src}`));
    document.body.append(script);
  });
}

const projectInput = document.getElementById("v2-project");
const tokenInput = document.getElementById("v2-token");
const network = document.getElementById("v2-network");
const handoff = document.querySelector(".v2-hermes-dock");

if (projectInput) projectInput.value = "ORANGERIE";
if (tokenInput) tokenInput.value = "demo-read-only";
if (network) network.textContent = "démo · données fictives";
if (handoff) {
  handoff.querySelectorAll("input, textarea, select, button").forEach(control => control.disabled = true);
  const message = handoff.querySelector("#v2-handoff-message");
  if (message) message.textContent = "Démo statique : aucun Work Issue ni run Hermes ne peut être créé.";
}

await new Promise(resolve => window.setTimeout(resolve, 180));
document.getElementById("v2-load")?.click();
