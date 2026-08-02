(() => {
  "use strict";

  function create(options = {}) {
    const fetchImpl = options.fetchImpl || window.fetch.bind(window);

    async function readJson(path, requestOptions = {}) {
      const response = await fetchImpl(path, requestOptions);
      if (!response.ok) {
        const payload = await response.json().catch(() => ({ detail: response.statusText }));
        throw new Error(payload.detail || response.statusText);
      }
      return response.json();
    }

    async function loadOptionalCollection(path, collectionKey) {
      try {
        const payload = await readJson(path, { cache: "no-store" });
        return Array.isArray(payload[collectionKey]) ? payload[collectionKey] : [];
      } catch (_) {
        return [];
      }
    }

    function authorizedJson(path, token) {
      return readJson(path, { headers: { Authorization: `Bearer ${token}` } });
    }

    async function loadAgencyProjects(token) {
      const payload = await authorizedJson("../v1/agency/projects?limit=200", token);
      return Array.isArray(payload.projects) ? payload.projects : [];
    }

    async function loadProjectSchema(token) {
      const payload = await authorizedJson("../v1/agency/schema/project", token);
      return payload.schema || null;
    }

    async function loadProjectBundle(projectId, token) {
      const encoded = encodeURIComponent(projectId);
      const [information, documents, knowledge, workIssues, candidates] = await Promise.all([
        authorizedJson(`../v1/agency/projects/${encoded}/information`, token),
        authorizedJson(`../v1/projects/${encoded}/documents`, token),
        authorizedJson(`../v1/projects/${encoded}/knowledge`, token),
        authorizedJson(`../v1/projects/${encoded}/work-issues`, token),
        authorizedJson(`../v1/agency/projects/${encoded}/change-candidates?status=pending_review&limit=100`, token),
      ]);
      return {
        information: Array.isArray(information.information) ? information.information : [],
        legacyDocuments: Array.isArray(documents.documents) ? documents.documents : [],
        knowledge: Array.isArray(knowledge.knowledge) ? knowledge.knowledge : [],
        workIssues: Array.isArray(workIssues.work_issues) ? workIssues.work_issues : [],
        changeCandidates: Array.isArray(candidates.change_candidates) ? candidates.change_candidates : [],
      };
    }

    return Object.freeze({
      loadRegistry: (path, collectionKey) => loadOptionalCollection(path, collectionKey),
      loadToolCatalog: () => loadOptionalCollection("tool_catalog.json", "items"),
      loadAgencyProjects,
      loadProjectSchema,
      loadProjectBundle,
    });
  }

  window.PantheonCockpitDataLoader = Object.freeze({ create });
})();
