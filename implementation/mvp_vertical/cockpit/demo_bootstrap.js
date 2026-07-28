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

window.PantheonDemoBootstrap = {
  async start() {
    const projectInput = document.getElementById("v2-project");
    const tokenInput = document.getElementById("v2-token");
    const network = document.getElementById("v2-network");

    if (projectInput) projectInput.value = "ORANGERIE";
    if (tokenInput) tokenInput.value = "demo-read-only";
    if (network) network.textContent = "démo · données fictives";

    await new Promise(resolve => window.setTimeout(resolve, 120));
    document.getElementById("v2-load")?.click();
  },
};
