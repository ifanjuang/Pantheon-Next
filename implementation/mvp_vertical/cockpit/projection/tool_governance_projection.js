(() => {
  "use strict";

  const NOT_OBSERVED = "not_observed";
  const loaderApi = window.PantheonCockpitDataLoader;
  if (loaderApi?.create) {
    const originalCreate = loaderApi.create.bind(loaderApi);
    loaderApi.create = (...args) => {
      const loader = originalCreate(...args);
      const originalLoad = loader.loadToolCatalog?.bind(loader);
      if (originalLoad) loader.loadToolCatalog = async (...loadArgs) => {
        const items = await originalLoad(...loadArgs);
        window.PantheonCockpitToolCatalogSnapshot = Array.isArray(items) ? items : [];
        return items;
      };
      return loader;
    };
  }

  function valueOrNotObserved(value) {
    return value == null || value === "" ? NOT_OBSERVED : String(value);
  }

  function anchorLabel(anchor) {
    if (!anchor || typeof anchor !== "object") return NOT_OBSERVED;
    return `${valueOrNotObserved(anchor.kind)} · ${valueOrNotObserved(anchor.value)}`;
  }

  function scopeLabel(scope) {
    if (!scope || typeof scope !== "object") return NOT_OBSERVED;
    return [scope.scope_type, scope.scope_id, scope.scope_label].filter(Boolean).join(" · ") || NOT_OBSERVED;
  }

  function exactGovernanceRows(item) {
    return [
      ["Binding exact", valueOrNotObserved(item.binding_id)],
      ["Release immuable", anchorLabel(item.implementation_anchor)],
      ["Activation", valueOrNotObserved(item.activation_state)],
      ["Scope d’activation", scopeLabel(item.activation_scope)],
      ["Compatibilité observée", valueOrNotObserved(item.compatibility_status)],
      ["Sécurité qualifiée", valueOrNotObserved(item.safety_status)],
      ["Fraîcheur observation", valueOrNotObserved(item.freshness_status)],
      ["Source observation", valueOrNotObserved(item.source_observation_ref)],
      ["Observation datée", valueOrNotObserved(item.compatibility_observed_at)],
      ["Limite d’autorité", "binding sélectionné ≠ dépendance adoptée · compatible ≠ activé · UI projetée ≠ autorisation"],
    ];
  }

  function projectExactGovernance(graph, catalog) {
    if (!graph?.cards || !Array.isArray(catalog)) return;
    const byId = new Map(catalog.map(item => [item.tool_id, item]));
    for (const [entityId, model] of graph.cards.entries()) {
      if (!entityId.startsWith("tool:")) continue;
      const item = byId.get(entityId.slice(5));
      if (!item) continue;
      const rows = exactGovernanceRows(item);
      const replacedLabels = new Set(rows.map(([label]) => label));
      const legacy = Array.isArray(model.back) ? model.back : [];
      model.back = [...legacy.filter(([label]) => !replacedLabels.has(label) && label !== "Activation scope"), ...rows];
    }
  }

  window.PantheonToolGovernanceProjection = Object.freeze({ exactGovernanceRows, projectExactGovernance });
  window.addEventListener("pantheon:graph-updated", () => {
    projectExactGovernance(window.PantheonCockpitGraph, window.PantheonCockpitToolCatalogSnapshot);
  });
})();
