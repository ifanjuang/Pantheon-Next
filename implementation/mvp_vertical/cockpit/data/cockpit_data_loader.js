(() => {
  "use strict";

  function create(options = {}) {
    const fetchImpl = options.fetchImpl || window.fetch.bind(window);
    let projectSchemaToken = null;
    let projectSchemaRequest = null;

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

    async function loadDecisionInbox(token) {
      const payload = await authorizedJson(
        "../decision-inbox?status=pending&limit=200",
        token,
      );
      const requests = Array.isArray(payload.decision_requests) ? payload.decision_requests : [];
      window.PantheonGlobalDecisionRequests = Object.freeze(requests.slice());
      return requests;
    }

    async function loadAgencyProjects(token) {
      const [payload] = await Promise.all([
        authorizedJson("../agency/projects?limit=200", token),
        loadDecisionInbox(token),
      ]);
      return Array.isArray(payload.projects) ? payload.projects : [];
    }

    async function loadProjectSchema(token, options = {}) {
      const normalizedToken = String(token || "");
      if (options.forceRefresh === true || projectSchemaToken !== normalizedToken) {
        projectSchemaToken = normalizedToken;
        projectSchemaRequest = null;
      }
      if (!projectSchemaRequest) {
        const pending = authorizedJson("../agency/schema/project", token)
          .then(payload => payload.schema || null)
          .catch(error => {
            if (projectSchemaRequest === pending) projectSchemaRequest = null;
            throw error;
          });
        projectSchemaRequest = pending;
      }
      return projectSchemaRequest;
    }

    async function loadProjectBundle(projectId, token) {
      const encoded = encodeURIComponent(projectId);
      const [information, documents, knowledge, workIssues, decisionRequests, pendingCandidates, revisionCandidates] = await Promise.all([
        authorizedJson(`../agency/projects/${encoded}/information`, token),
        authorizedJson(`../projects/${encoded}/documents`, token),
        authorizedJson(`../projects/${encoded}/knowledge`, token),
        authorizedJson(`../work/scopes/project/${encoded}/issues`, token),
        authorizedJson(`../agency/projects/${encoded}/decision-requests?status=pending&limit=100`, token),
        authorizedJson(`../agency/projects/${encoded}/change-candidates?status=pending_review&limit=100`, token),
        authorizedJson(`../agency/projects/${encoded}/change-candidates?status=revision_requested&limit=100`, token),
      ]);
      const projectDecisionRequests = Array.isArray(decisionRequests.decision_requests)
        ? decisionRequests.decision_requests
        : [];
      window.PantheonProjectDecisionRequests = Object.freeze(projectDecisionRequests.slice());
      return {
        information: Array.isArray(information.information) ? information.information : [],
        legacyDocuments: Array.isArray(documents.documents) ? documents.documents : [],
        knowledge: Array.isArray(knowledge.knowledge) ? knowledge.knowledge : [],
        workIssues: Array.isArray(workIssues.work_issues) ? workIssues.work_issues : [],
        decisionRequests: projectDecisionRequests,
        changeCandidates: [
          ...(Array.isArray(pendingCandidates.change_candidates) ? pendingCandidates.change_candidates : []),
          ...(Array.isArray(revisionCandidates.change_candidates) ? revisionCandidates.change_candidates : []),
        ],
      };
    }

    return Object.freeze({
      loadRegistry: (path, collectionKey) => loadOptionalCollection(path, collectionKey),
      loadToolCatalog: () => loadOptionalCollection("tool_catalog.json", "items"),
      loadAgencyProjects,
      loadDecisionInbox,
      loadProjectSchema,
      loadProjectBundle,
    });
  }

  window.PantheonGlobalDecisionRequests = Object.freeze([]);
  window.PantheonProjectDecisionRequests = Object.freeze([]);
  window.PantheonCockpitDataLoader = Object.freeze({ create });
})();
