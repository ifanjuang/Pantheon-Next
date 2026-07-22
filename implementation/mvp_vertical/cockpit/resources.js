(() => {
  const emptyProfiles = () => ({ documents: new Map(), knowledgeSites: new Map(), crawlCapability: null });
  state.resourceProfiles = emptyProfiles();
  sceneCopy.resources = ["RESSOURCES", "Formats, contenus observés et sites liés"];

  Object.assign(iconPaths, {
    pdf: '<path d="M6 2.75h8l4 4V21.25H6z"/><path d="M14 2.75v4h4"/><path d="M8.5 13h7M8.5 16h5"/>',
    image: '<rect x="3.5" y="4.5" width="17" height="15" rx="2"/><circle cx="9" cy="10" r="1.5"/><path d="m5.5 17 4.5-4 3 2.5 2.5-2 3 3.5"/>',
    text: '<path d="M5 5h14M8 9h8M8 13h8M8 17h5"/>',
    table: '<rect x="3.5" y="4.5" width="17" height="15" rx="1.5"/><path d="M3.5 10h17M9 4.5v15M15 4.5v15"/>',
    web: '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.2 2.3 3.3 5.1 3.3 8.5S14.2 18.2 12 20.5M12 3.5C9.8 5.8 8.7 8.6 8.7 12s1.1 6.2 3.3 8.5"/>',
    structure: '<path d="M12 4v5M6 20v-5h12v5M6 15v-3h12v3"/><circle cx="12" cy="3.5" r="1.5"/><circle cx="6" cy="20.5" r="1.5"/><circle cx="18" cy="20.5" r="1.5"/>',
    archive: '<path d="M4 6h16v14H4zM3 3h18v4H3zM9 11h6"/>',
  });

  const formatLabels = {
    pdf: "PDF",
    image: "IMAGE",
    text: "TEXTE",
    word_processing: "DOC",
    spreadsheet: "TABLEUR",
    presentation: "DIAPO",
    archive: "ARCHIVE",
    other: "FICHIER",
  };

  const compositionLabels = {
    text_only: "Texte observé",
    structured_text: "Texte structuré et tableaux",
    text_and_images: "Texte et images observés",
    image_with_extracted_text: "Image avec texte extrait",
    images_only: "Images observées",
    unknown: "Composition non déterminée",
  };

  const formatIcon = family => ({
    pdf: "pdf",
    image: "image",
    text: "text",
    word_processing: "text",
    spreadsheet: "table",
    presentation: "image",
    archive: "archive",
  })[family] || "document";

  const contentIcon = content => {
    if (content?.has_images) return "image";
    if (content?.has_tables) return "table";
    if (content?.has_text) return "text";
    return "document";
  };

  const originalTypeLockup = typeLockup;
  typeLockup = function resourceTypeLockup(model) {
    const lockup = originalTypeLockup(model);
    if (model.formatBadge) {
      const badge = document.createElement("span");
      badge.className = "format-chip";
      badge.textContent = model.formatBadge;
      badge.title = model.formatDescription || model.formatBadge;
      lockup.append(badge);
    }
    return lockup;
  };

  const originalResponsibilityButton = responsibilityButton;
  responsibilityButton = function resourceIndicator(item) {
    const badge = originalResponsibilityButton(item);
    if (item.count && item.count > 1) {
      const count = document.createElement("span");
      count.className = "indicator-count";
      count.textContent = item.count > 99 ? "99+" : String(item.count);
      badge.append(count);
    }
    return badge;
  };

  const originalDocumentModel = documentModel;
  documentModel = function resourceDocumentModel(item) {
    const model = originalDocumentModel(item);
    const profile = state.resourceProfiles.documents.get(item.document_id);
    if (!profile) return model;

    const format = profile.format || {};
    const content = profile.content || {};
    const formatLabel = formatLabels[format.family] || (format.extension || "FICHIER").toUpperCase();
    model.formatBadge = format.extension ? format.extension.toUpperCase() : formatLabel;
    model.formatDescription = `${formatLabel} · ${format.media_type || "type média inconnu"}`;
    model.signal = `${formatLabel} · ${compositionLabels[content.composition] || "composition à vérifier"}`;
    model.responsibilities = [
      { icon: formatIcon(format.family), label: model.formatDescription },
      { icon: contentIcon(content), label: compositionLabels[content.composition] || "Composition à vérifier" },
      { icon: "source", label: "Source liée · la carte n’est pas la source" },
      ...(model.attention ? [{ icon: "review", label: "Revue humaine nécessaire", attention: true }] : []),
    ];
    model.sections.splice(1, 0, ["Format et composition observée", [
      `Format : ${formatLabel}${format.extension ? ` (.${format.extension})` : ""}`,
      `Type média : ${format.media_type || "non renseigné"}`,
      `Composition : ${compositionLabels[content.composition] || content.composition || "non déterminée"}`,
      `Texte observé : ${content.has_text ? "oui" : "non"}`,
      `Images observées : ${content.has_images ? "oui" : "non"}${content.observed_image_items ? ` · ${content.observed_image_items} élément(s) structuré(s)` : ""}`,
      `Tableaux observés : ${content.has_tables ? "oui" : "non"}${content.observed_table_items ? ` · ${content.observed_table_items} élément(s)` : ""}`,
      "Profil dérivé de l’extraction : il oriente la lecture mais ne constitue pas une inspection exhaustive de l’original.",
    ]]);
    return model;
  };

  const originalKnowledgeModel = knowledgeModel;
  knowledgeModel = function resourceKnowledgeModel(item) {
    const model = originalKnowledgeModel(item);
    const sites = state.resourceProfiles.knowledgeSites.get(item.knowledge_id) || [];
    if (!sites.length) return model;

    model.formatBadge = `${sites.length} WEB`;
    model.formatDescription = `${sites.length} adresse(s) web liée(s)`;
    model.siteManifestCandidate = { knowledgeId: item.knowledge_id, sites };
    const visibleSiteIndicators = sites.slice(0, 3).map(site => ({
      icon: "web",
      label: `${site.host} · ${site.site_kind} · adresse seulement`,
    }));
    if (sites.length > 3) {
      visibleSiteIndicators.push({
        icon: "web",
        label: `${sites.length - 3} autre(s) site(s) lié(s)`,
        count: sites.length - 3,
      });
    }
    model.responsibilities = [
      ...visibleSiteIndicators,
      { icon: "memory", label: "Knowledge n’est pas mémoire gouvernée" },
      ...(model.attention ? [{ icon: "review", label: statusLabel(model.status), attention: true }] : []),
    ];
    model.signal = `${sites.length} site(s) lié(s) · adresses seulement`;
    model.sections.splice(-1, 0, ["Sites liés", [
      ...sites.map(site => `${site.host} · ${site.site_kind} · ${site.url}`),
      "État actuel : adresses conservées dans la Knowledge ; aucun crawl ni index vectoriel web n’est autorisé.",
      "Modes futurs possibles après définition du périmètre : structure seule, pages sélectionnées ou contenu complet.",
    ]]);
    return model;
  };

  const originalCurrentModels = currentModels;
  currentModels = function resourceFilteredModels() {
    if (state.scene !== "resources") return originalCurrentModels();
    const linkedKnowledge = state.knowledge
      .filter(item => (state.resourceProfiles.knowledgeSites.get(item.knowledge_id) || []).length)
      .map(knowledgeModel);
    const profiledDocuments = state.documents
      .filter(item => state.resourceProfiles.documents.has(item.document_id))
      .map(documentModel);
    return [...linkedKnowledge, ...profiledDocuments];
  };

  function normalizeProfiles(payload) {
    return {
      documents: new Map((payload.documents || []).map(item => [item.document_id, item])),
      knowledgeSites: new Map((payload.knowledge_sites || []).map(item => [item.knowledge_id, item.sites || []])),
      crawlCapability: payload.crawl_capability || null,
    };
  }

  function defaultPathPrefix(value) {
    try {
      return new URL(value).pathname || "/";
    } catch (_error) {
      return "/";
    }
  }

  async function postJson(path, body) {
    const response = await fetch(path, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${state.token}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });
    if (!response.ok) {
      const payload = await response.json().catch(() => ({ detail: response.statusText }));
      throw new Error(payload.detail || response.statusText);
    }
    return response.json();
  }

  function renderManifestResult(output, payload) {
    output.replaceChildren();
    const heading = document.createElement("h4");
    heading.textContent = "Manifeste candidat";
    const summary = document.createElement("p");
    summary.textContent = `${payload.status} · ${payload.manifest_id}`;
    const list = document.createElement("ul");
    const sites = payload.manifest?.sites || [];
    const entries = [
      `Empreinte : ${payload.manifest_digest}`,
      `Mode : ${payload.manifest?.mode || "structure_only"}`,
      `Réseau exécuté : ${payload.execution?.network_requests || 0} requête`,
      `Binding Hermes : ${payload.capability_slot?.candidate_hermes_binding || "non sélectionné"}`,
      `Activation : ${payload.capability_slot?.activation || "non autorisée"}`,
      ...sites.map(site => `${site.host} · ${site.path_prefixes.join(", ")} · profondeur ${site.max_depth}`),
      ...(payload.warnings || []).map(warning => `Attention : ${warning}`),
      ...(payload.gates || []).map(gate => `Gate : ${gate.gate} · ${gate.status}`),
      "Aucun crawl, index, planning ou handoff n’a été créé.",
    ];
    for (const entry of entries) {
      const item = document.createElement("li");
      item.textContent = entry;
      list.append(item);
    }
    output.append(heading, summary, list);
  }

  function manifestPreviewSection(model) {
    const section = document.createElement("section");
    section.className = "detail-section manifest-preview";
    const heading = document.createElement("h3");
    heading.textContent = "Préparer un périmètre structurel";
    const explanation = document.createElement("p");
    explanation.textContent = "La prévisualisation ne contacte aucun site. Elle prépare seulement les hôtes, chemins et profondeurs à soumettre aux Gates Pantheon.";
    const siteList = document.createElement("div");
    siteList.className = "manifest-site-list";

    model.siteManifestCandidate.sites.forEach((site, index) => {
      const row = document.createElement("div");
      row.className = "manifest-site-row";
      const selection = document.createElement("label");
      selection.className = "manifest-site-select";
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.checked = true;
      checkbox.dataset.manifestUrl = site.url;
      const name = document.createElement("span");
      name.textContent = `${site.host} · ${site.site_kind}`;
      selection.append(checkbox, name);

      const prefixLabel = document.createElement("label");
      prefixLabel.className = "manifest-prefix-label";
      prefixLabel.textContent = "Chemin autorisé";
      const prefix = document.createElement("input");
      prefix.type = "text";
      prefix.value = defaultPathPrefix(site.url);
      prefix.dataset.manifestPrefixFor = String(index);
      prefixLabel.append(prefix);
      row.append(selection, prefixLabel);
      siteList.append(row);
    });

    const depthLabel = document.createElement("label");
    depthLabel.className = "manifest-depth-label";
    depthLabel.textContent = "Profondeur maximale";
    const depth = document.createElement("select");
    for (let value = 0; value <= 5; value += 1) {
      const option = document.createElement("option");
      option.value = String(value);
      option.textContent = String(value);
      option.selected = value === 2;
      depth.append(option);
    }
    depthLabel.append(depth);

    const action = document.createElement("button");
    action.type = "button";
    action.className = "primary-action";
    action.textContent = "Prévisualiser le manifeste";
    const output = document.createElement("div");
    output.className = "manifest-output";
    output.setAttribute("aria-live", "polite");

    action.addEventListener("click", async () => {
      const rows = [...siteList.querySelectorAll(".manifest-site-row")];
      const sites = rows.flatMap(row => {
        const checkbox = row.querySelector('input[type="checkbox"]');
        const prefix = row.querySelector('input[type="text"]');
        if (!checkbox?.checked) return [];
        return [{
          url: checkbox.dataset.manifestUrl,
          path_prefixes: [prefix?.value.trim() || "/"],
          max_depth: Number(depth.value),
        }];
      });
      if (!sites.length) {
        output.textContent = "Sélectionnez au moins un site lié.";
        return;
      }
      action.disabled = true;
      output.textContent = "Préparation du manifeste candidat…";
      try {
        const project = encodeURIComponent(state.project);
        const knowledgeId = encodeURIComponent(model.siteManifestCandidate.knowledgeId);
        const payload = await postJson(
          `../v1/projects/${project}/knowledge/${knowledgeId}/site-manifests/preview`,
          { mode: "structure_only", sites },
        );
        renderManifestResult(output, payload);
      } catch (error) {
        output.textContent = `Prévisualisation refusée : ${error.message}`;
      } finally {
        action.disabled = false;
      }
    });

    section.append(heading, explanation, siteList, depthLabel, action, output);
    return section;
  }

  const originalOpenDetail = openDetail;
  openDetail = function resourceOpenDetail(model) {
    originalOpenDetail(model);
    if (!model.siteManifestCandidate) return;
    $("detail-content").append(manifestPreviewSection(model));
  };

  function addResourcesTab() {
    const rail = document.querySelector(".scene-rail");
    if (!rail || rail.querySelector('[data-scene="resources"]')) return;
    const button = document.createElement("button");
    button.className = "scene-tab";
    button.dataset.scene = "resources";
    button.type = "button";
    button.textContent = "Ressources";
    button.addEventListener("click", () => {
      state.scene = "resources";
      document.querySelectorAll("[data-scene]").forEach(tab => {
        tab.classList.toggle("is-active", tab === button);
      });
      render();
    });
    const questionnaire = rail.querySelector('[data-scene="questionnaire"]');
    rail.insertBefore(button, questionnaire || null);
  }

  async function loadResourceProfiles() {
    const project = $("project").value.trim();
    if (!project || !$("token").value) return;
    state.resourceProfiles = emptyProfiles();
    try {
      const payload = await api(`../v1/projects/${encodeURIComponent(project)}/resource-profiles`);
      if (project !== state.project) return;
      state.resourceProfiles = normalizeProfiles(payload);
      render();
    } catch (error) {
      console.warn("Resource profiles unavailable", error);
    }
  }

  addResourcesTab();
  $("load").addEventListener("click", loadResourceProfiles);
})();
