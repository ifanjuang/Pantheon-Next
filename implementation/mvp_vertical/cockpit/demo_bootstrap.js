const nativeFetch = window.fetch.bind(window);
const fixtureResponse = payload => new Response(JSON.stringify(payload), {
  status: 200,
  headers: { "Content-Type": "application/json; charset=utf-8" },
});

const [fixture, workActivityFixture] = await Promise.all([
  nativeFetch("demo-data.json", { cache: "no-store" }).then(response => {
    if (!response.ok) throw new Error(`Fixture indisponible (${response.status})`);
    return response.json();
  }),
  nativeFetch("demo-work-activity.json", { cache: "no-store" }).then(response => {
    if (!response.ok) throw new Error(`Fixture Work indisponible (${response.status})`);
    return response.json();
  }),
]);

if (workActivityFixture.schema_id !== "cockpit.demo_work_activity" || workActivityFixture.revision !== 1) {
  throw new Error("Fixture Work incompatible");
}

function strictWorkIssues(payload) {
  return (payload.work_issues || []).map(item => {
    const issueId = item?.work_issue?.issue_id;
    const strict = workActivityFixture.items?.[issueId];
    if (!strict) throw new Error(`Fixture Work manquante : ${String(issueId)}`);
    return strict;
  });
}

function projectPayload(projectId) {
  const payload = fixture.project_payloads[projectId] || {
    information: [],
    documents: [],
    knowledge: [],
    work_issues: [],
    change_candidates: [],
  };
  return { ...payload, work_issues: strictWorkIssues(payload) };
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
  if (url.pathname.endsWith("/agency/projects")) return fixtureResponse({ projects: fixture.projects });
  if (url.pathname.endsWith("/agency/schema/project")) return fixtureResponse({ schema: fixture.project_schema });

  const agencyProject = url.pathname.match(/\/agency\/projects\/([^/]+)\/(information|change-candidates)$/);
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

    if (projectInput) projectInput.value = "VALLONS";
    if (tokenInput) tokenInput.value = "demo-read-only";
    if (network) network.textContent = "univers fictif · lecture seule";

    await new Promise(resolve => window.setTimeout(resolve, 120));
    document.getElementById("v2-load")?.click();
  },
};