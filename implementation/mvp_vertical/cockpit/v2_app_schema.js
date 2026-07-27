(() => {
  "use strict";

  const $ = id => document.getElementById(id);
  const ROOT_SPACES = ["pantheon", "decisions", "affaires", "connaissances", "outils"];
  const CONTACT_GROUPS = [
    "Maîtrise d’ouvrage",
    "Équipe de maîtrise d’œuvre",
    "Bureaux d’études",
    "Bureau de contrôle",
    "SSI",
    "Entreprises de travaux",
    "Autres intervenants",
  ];
  const STATUS_LABELS = {
    draft: "Brouillon",
    in_progress: "En rédaction",
    acted: "Acté",
    superseded: "Archivé",
    review: "À valider",
    needs_review: "À valider",
    pending_review: "À valider",
    generated_unreviewed: "Non revu",
    ready: "Prêt",
    reviewed: "Revu",
    active: "Actif",
    waiting: "En attente",
    done: "Terminé",
    conflict: "Conflit",
    failed: "Échec",
    stale: "Obsolète",
    rejected: "Refusé",
    applied: "Appliqué",
    neutral: "Référence",
    open: "À faire",
    partial: "Partiel",
    candidate: "Candidat",
    watch: "À observer",
    unreviewed: "Non revu",
    not_activated: "Non activé",
  };
  const FAMILY_MARKS = {
    pantheon: "P",
    project: "A",
    information: "I",
    contact: "C",
    work: "W",
    decision: "D",
    tool: "#",
  };
  const PROJECT_ACCENTS = ["#244f7b", "#6a4a77", "#356753", "#805a2c", "#76504a", "#4d5f87"];

  const registries = {
    typeTags: new Map(),
    subjectTags: new Map(),
    statuses: new Map(),
    limits: new Map(),
  };

  const state = {
    project: "",
    token: "",
    projects: [],
    projectSchema: null,
    information: [],
    legacyDocuments: [],
    knowledge: [],
    workIssues: [],
    changeCandidates: [],
    toolCatalog: [],
    cards: new Map(),
    children: new Map(),
    flipped: new Set(),
    navigator: null,
    lastMove: "none",
  };

  const slug = value => String(value || "")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLowerCase()
    .trim()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");

  const text = (value, fallback = "") => value == null || value === "" ? fallback : String(value);
  const statusLabel = value => STATUS_LABELS[value] || String(value || "À vérifier").replaceAll("_", " ");

  function stableAccent(value) {
    const input = String(value || "project");
    let hash = 0;
    for (let index = 0; index < input.length; index += 1) {
      hash = ((hash << 5) - hash + input.charCodeAt(index)) | 0;
    }
    return PROJECT_ACCENTS[Math.abs(hash) % PROJECT_ACCENTS.length];
  }

  async function loadRegistry(path, collectionKey, map) {
    try {
      const response = await fetch(path, { cache: "no-store" });
      if (!response.ok) return;
      const payload = await response.json();
      for (const item of payload[collectionKey] || []) map.set(slug(item.slug || item.title), item);
    } catch (_) {
      // Presentation metadata is non-authoritative and must not block the Cockpit.
    }
  }

  async function loadToolCatalog() {
    try {
      const response = await fetch("tool_catalog.json", { cache: "no-store" });
      if (!response.ok) throw new Error(response.statusText);
      const payload = await response.json();
      state.toolCatalog = Array.isArray(payload.items) ? payload.items : [];
    } catch (_) {
      state.toolCatalog = [];
    }
    return state.toolCatalog;
  }

  function registryEntry(map, value) {
    return map.get(slug(value)) || null;
  }

  function setTokenColor(node, entry) {
    if (entry?.color) node.dataset.tokenColor = entry.color;
    if (entry?.icon_key) node.dataset.iconKey = entry.icon_key;
  }

  function card(input) {
    const projection = window.PantheonStructuredInterface?.buildCardProjection?.(input) || {};
    return {
      role: "entity",
      family: "information",
      status: "neutral",
      summary: "",
      type_tags: [],
      subject_tags: [],
      limits: [],
      available_actions: [],
      back: [],
      ...input,
      ...projection,
      presentation_family: projection.presentation_family || input.presentation_family || input.family,
    };
  }

  function putCard(model) {
    state.cards.set(model.entity_id, model);
    return model.entity_id;
  }

  function setChildren(parentId, ids) {
    state.children.set(parentId, [...ids].filter(Boolean));
  }

  function rootCards() {
    return [
      card({ entity_id: "space:pantheon", entity_type: "cockpit_space", role: "conversation", family: "pantheon", presentation_family: "pantheon", category: "Pantheon", title: "Pantheon", summary: "Contexte, gouvernance et décisions conséquentes.", status: "active", back: [["Principe", "Pantheon gouverne ; il ne devient ni runtime ni moteur de workflow."]] }),
      card({ entity_id: "space:decisions", entity_type: "cockpit_space", role: "container", family: "decision", presentation_family: "decision", category: "Décisions", title: "Décisions", summary: "Validations humaines : Travaux en revue et propositions de modification.", status: "review", back: [["Principe", "Décision de Travail et ChangeCandidate restent deux objets distincts."]] }),
      card({ entity_id: "space:affaires", entity_type: "cockpit_space", role: "container", family: "project", presentation_family: "project", category: "Projets", title: "Affaires", summary: "Projets, Informations, Contacts et Travaux.", status: "active", back: [["Source", "PostgreSQL Agency Data reste le system of record."]] }),
      card({ entity_id: "space:connaissances", entity_type: "cockpit_space", role: "container", family: "information", presentation_family: "information", category: "Références", title: "Connaissances", summary: "Références réutilisables et leur état de revue.", status: "neutral", back: [["Limite", "Knowledge ≠ Evidence ≠ mémoire gouvernée."]] }),
      card({ entity_id: "space:outils", entity_type: "cockpit_space", role: "container", family: "tool", presentation_family: "tool", category: "Outils", title: "Outils", summary: "Outils, skills, bindings et runtimes observés ou candidats.", status: "neutral", back: [["Limite", "Installé ≠ approuvé · healthy ≠ safe · update disponible ≠ update autorisée."]] }),
    ];
  }

  function projectEntityId(item) {
    return `project:${item.project_id || item.entity_id || item.code || item.display_name}`;
  }

  function schemaFields(storage) {
    return (state.projectSchema?.fields || []).filter(field => field.storage === storage);
  }

  function formattedValue(field, value) {
    if (value == null || value === "") return "Non renseigné";
    if (Array.isArray(value)) return value.join(" · ");
    if (field?.unit === "EUR" && typeof value === "number") {
      return new Intl.NumberFormat("fr-FR", { style: "currency", currency: "EUR", maximumFractionDigits: 0 }).format(value);
    }
    if (field?.unit === "m2" && typeof value === "number") {
      return `${new Intl.NumberFormat("fr-FR", { maximumFractionDigits: 2 }).format(value)} m²`;
    }
    return String(value);
  }

  function projectSchemaRows(item) {
    if (!state.projectSchema) {
      return Object.entries(item.attributes || {})
        .filter(([, value]) => value !== null && value !== "" && !(Array.isArray(value) && !value.length))
        .map(([key, value]) => [key.replaceAll("_", " "), Array.isArray(value) ? value.join(" · ") : String(value)]);
    }
    const rows = [];
    for (const field of state.projectSchema.fields || []) {
      if (field.presentation?.hidden === true || field.storage === "system") continue;
      const value = field.storage === "attributes"
        ? item.attributes?.[field.key]
        : field.storage === "projection"
          ? item.claim_values?.[field.key]
          : item[field.key];
      if (value == null || value === "" || (Array.isArray(value) && !value.length)) continue;
      rows.push([field.title || field.label || field.key, formattedValue(field, value)]);
    }
    return rows;
  }

  function normalizeProject(item, { selected = false } = {}) {
    const projectId = item.project_id || item.entity_id || item.code || item.display_name;
    const title = item.display_name || item.code || projectId || "Affaire";
    const contactCount = Array.isArray(item.contacts) ? item.contacts.length : 0;
    const informationCount = state.information.length + state.legacyDocuments.length;
    return card({
      entity_id: projectEntityId(item),
      entity_type: "project",
      family: "project",
      presentation_family: "project",
      category: "Projet",
      title,
      summary: selected
        ? `${informationCount} information(s) · ${contactCount} contact(s) · ${state.workIssues.length} travail(aux)`
        : [item.code && item.code !== title ? item.code : null, item.phase, item.location].filter(Boolean).join(" · ") || "Affaire Agency Data",
      status: item.status || "active",
      subject_tags: Array.isArray(item.tags) ? item.tags : [],
      identity_accent: stableAccent(projectId),
      index: item.display_index || item.index || null,
      date: item.updated_at || null,
      front: { issuer: item.primary_client || null },
      back: projectSchemaRows(item),
      source_project_id: String(projectId || ""),
    });
  }

  function normalizeInformation(item) {
    return card({
      entity_id: `information:${item.information_id}`,
      entity_type: "information",
      family: "information",
      presentation_family: "information",
      category: item.category || "Information",
      title: item.title || "Information",
      summary: item.summary || "Résumé non renseigné",
      status: item.status || "draft",
      index: item.index_label || null,
      date: item.information_date || item.updated_at || null,
      author: item.author || null,
      type_tags: item.type_tags || [],
      subject_tags: item.subject_tags || [],
      limits: item.limits || [],
      available_actions: item.status === "acted" ? ["Nouvelle version"] : ["Modifier avec Hermès", "Acter"],
      back: [
        ["Résumé", text(item.summary, "Résumé non renseigné")],
        ["Informations détaillées", text(item.details, "Informations détaillées non renseignées")],
        ["Source", text(item.source_ref || item.source_note, "Source non renseignée")],
        ["Version source", text(item.source_version, "Non renseignée")],
        ["Auteur", text(item.author, "Non renseigné")],
      ],
      source_refs: [item.source_ref].filter(Boolean),
      base_acted_id: item.base_acted_id || null,
      series_id: item.series_id || null,
      technical_revision: item.revision || null,
    });
  }

  function normalizeLegacyDocument(item) {
    const naming = item.naming || {};
    const id = item.document_id || item.card_id || item.source_ref || crypto.randomUUID();
    const category = naming.document_type || item.category || "Document";
    return card({
      entity_id: `document:${id}`,
      entity_type: "document",
      family: "information",
      presentation_family: "information",
      category,
      title: naming.object_name || item.title || category,
      summary: item.summary || [naming.document_type, naming.phase_code].filter(Boolean).join(" · ") || "Document source",
      status: item.status || item.analysis_status || "partial",
      index: naming.revision_index || item.index || null,
      date: item.document_date || item.date || item.created_at || null,
      author: item.author || naming.issuer || item.issuer || null,
      type_tags: item.type_tags || [slug(category)],
      subject_tags: item.subject_tags || item.tags || [],
      limits: item.limits || [],
      back: [
        ["Résumé", text(item.summary, "Résumé non renseigné")],
        ["Informations détaillées", text(item.details, "À produire dans une Information métier")],
        ["Source", text(item.source_ref, "Source non exposée")],
      ],
      source_refs: [item.source_ref].filter(Boolean),
    });
  }

  function normalizeKnowledge(item) {
    return card({
      entity_id: `knowledge:${item.knowledge_id || item.card_id || crypto.randomUUID()}`,
      entity_type: "knowledge",
      family: "information",
      presentation_family: "information",
      category: item.family || "Référence",
      title: item.title || "Knowledge",
      summary: item.summary || `Version ${item.version || 1}`,
      status: item.review_status || "generated_unreviewed",
      date: item.updated_at || null,
      author: item.author || null,
      type_tags: item.type_tags || ["etude"],
      subject_tags: item.subject_tags || item.tags || [],
      limits: item.limits || ["consultatif"],
      back: [["Informations détaillées", text(item.markdown, "Contenu non exposé")]],
    });
  }

  function workData(projection) {
    return projection.work_issue || projection;
  }

  function normalizeWork(projection) {
    const issue = workData(projection);
    const id = issue.issue_id || crypto.randomUUID();
    const milestones = issue.milestones || issue.steps || [];
    const resources = [
      ...(issue.responsibilities || []),
      ...(issue.skills || []),
      ...(issue.functions || []),
      ...(issue.tools || []),
    ];
    return card({
      entity_id: `work:${id}`,
      entity_type: "work_issue",
      family: "work",
      presentation_family: "work",
      category: "Travail",
      title: issue.title || "Travail",
      summary: issue.description || "Objectif de travail non renseigné",
      status: issue.status || "open",
      subject_tags: issue.tags || [],
      back: [
        ["Objectif", text(issue.description, "Non renseigné")],
        ["Jalons", milestones.length ? milestones.map(step => typeof step === "string" ? step : step.label || step.title).filter(Boolean).join("\n") : "Non renseignés"],
        ["Responsabilités · Skills · Fonctions · Outils", resources.length ? resources.map(String).join(" · ") : "Non renseignés"],
        ["Résultat attendu", text(issue.result_ref || issue.output_ref || issue.requested_effect, "Non renseigné")],
      ],
      source_work_id: id,
    });
  }

  function normalizeWorkDecision(projection) {
    const issue = workData(projection);
    const id = issue.issue_id || crypto.randomUUID();
    return card({
      entity_id: `decision:work:${id}`,
      entity_type: "work_decision",
      family: "decision",
      presentation_family: "decision",
      category: "Décision · Travail",
      title: issue.decision_title || issue.title || "Validation du travail",
      summary: issue.decision_question || "Le Travail demande une validation humaine.",
      status: "review",
      subject_tags: issue.tags || [],
      available_actions: ["Refuser", "Valider"],
      back: [
        ["Travail", text(issue.title, id)],
        ["Question", text(issue.decision_question, "Valider le résultat ou l’orientation proposée ?")],
        ["Résultat présenté", text(issue.result_summary || issue.description, "Non renseigné")],
        ["Effet demandé", text(issue.requested_effect, "Non renseigné")],
      ],
      source_work_id: id,
    });
  }

  function candidateFieldTitle(key) {
    const field = (state.projectSchema?.fields || []).find(item => item.key === key);
    return field?.title || field?.label || key.replaceAll("_", " ");
  }

  function candidateChangeLine(change) {
    const field = (state.projectSchema?.fields || []).find(item => item.key === change.field);
    return `${candidateFieldTitle(change.field)} : ${formattedValue(field, change.before)} → ${formattedValue(field, change.proposed)}`;
  }

  function normalizeChangeCandidate(item) {
    const changes = Array.isArray(item.changes) ? item.changes : [];
    return card({
      entity_id: `decision:change:${item.candidate_id}`,
      entity_type: "project_change_candidate",
      family: "decision",
      presentation_family: "decision",
      category: "Décision · Modification",
      title: changes.length === 1 ? `Modifier ${candidateFieldTitle(changes[0].field)}` : `Modifier ${changes.length} champs du Projet`,
      summary: item.reason || changes.map(candidateChangeLine).join(" · ") || "Proposition de modification à examiner.",
      status: item.status || "pending_review",
      date: item.created_at || null,
      available_actions: item.status === "pending_review" ? ["Refuser", "Valider"] : [],
      back: [
        ["Projet", text(item.entity_id, state.project)],
        ["Proposition", changes.map(candidateChangeLine).join("\n") || "Aucun diff exposé"],
        ["Proposé par", `${text(item.proposer, "Inconnu")} · ${text(item.proposer_kind, "inconnu")}`],
        ["Révision de base", text(item.base_revision, "Non renseignée")],
        ["Motif", text(item.reason, "Non renseigné")],
        ["Sources", (item.source_refs || []).join("\n") || "Aucune source déclarée"],
      ],
      source_candidate_id: item.candidate_id,
      source_project_id: item.entity_id,
    });
  }

  function contactDisplay(item) {
    const identity = [item.name, item.organization].filter(Boolean).join(" · ");
    const role = item.role ? ` — ${item.role}` : "";
    const details = [item.email, item.phone].filter(Boolean).join(" · ");
    return `${identity || "Contact non renseigné"}${role}${details ? `\n${details}` : ""}`;
  }

  function normalizeContacts(projectId, contacts = []) {
    const groups = new Map(CONTACT_GROUPS.map(name => [name, []]));
    for (const item of Array.isArray(contacts) ? contacts : []) {
      const group = CONTACT_GROUPS.includes(item.group) ? item.group : "Autres intervenants";
      groups.get(group).push(item);
    }
    const back = [];
    for (const group of CONTACT_GROUPS) {
      const values = groups.get(group) || [];
      if (values.length) back.push([group, values.map(contactDisplay).join("\n")]);
    }
    return card({
      entity_id: `project:${projectId}:contacts`,
      entity_type: "project_contacts",
      family: "contact",
      presentation_family: "contact",
      category: "Contacts",
      title: "Contacts",
      summary: `${Array.isArray(contacts) ? contacts.length : 0} contact(s)`,
      status: "neutral",
      identity_accent: stableAccent(projectId),
      back: back.length ? back : [["Contacts", "Aucun contact renseigné pour cette affaire."]],
      source_project_id: projectId,
    });
  }

  function toolStatus(item) {
    if (item.governance_state === "approved") return "reviewed";
    if (item.governance_state === "candidate") return "candidate";
    if (item.governance_state === "watch") return "watch";
    if (item.health_state === "observed_ready") return "ready";
    if (item.governance_state === "unreviewed") return "unreviewed";
    return "neutral";
  }

  function permissionLines(permissions = {}) {
    return Object.entries(permissions)
      .map(([key, value]) => `${key.replaceAll("_", " ")} : ${value}`)
      .join("\n");
  }

  function normalizeTool(item) {
    const slots = Array.isArray(item.capability_slots) ? item.capability_slots : [];
    const runtimeCapabilities = Array.isArray(item.capabilities) ? item.capabilities : [];
    const permissions = item.permissions && typeof item.permissions === "object" && !Array.isArray(item.permissions)
      ? item.permissions
      : {};
    return card({
      entity_id: `tool:${item.tool_id}`,
      entity_type: "tool",
      family: "tool",
      presentation_family: "tool",
      category: item.category || item.resource_type || "Outil",
      type_tags: ["outil"],
      subject_tags: slots,
      title: item.name || item.tool_id,
      summary: item.short_description || "Outil ou binding candidat.",
      status: toolStatus(item),
      date: item.observed_at || null,
      back: [
        ["Description", text(item.long_description || item.short_description, "Non renseignée")],
        ["Capability Slots", slots.length ? slots.join("\n") : "Aucun slot déclaré"],
        ["Provenance", text(item.provenance_mode, "Non renseignée")],
        ["Owner runtime", text(item.runtime_owner, "Non renseigné")],
        ["Installation", text(item.installation_state, "unknown")],
        ["État natif", text(item.native_state, "unknown")],
        ["Santé observée", text(item.health_state, "unknown")],
        ["Gouvernance", text(item.governance_state, "unknown")],
        ["Activation scope", text(item.activation_state, "unknown")],
        ["Mise à jour", text(item.update_state, "unknown")],
        ["Permissions", permissionLines(permissions) || "Non qualifiées"],
        ["Capacités runtime", runtimeCapabilities.length ? runtimeCapabilities.join("\n") : "Non observées"],
        ["Evidence attendue", text(item.evidence_expectation, "À définir avant usage conséquent")],
        ["Rollback", text(item.rollback_posture, "Non renseigné")],
        ["Prochaine décision humaine", text(item.next_human_decision, "Aucune")],
        ["Risques connus", (item.known_risks || []).join("\n") || "Non renseignés"],
        ["Interdits", (item.forbidden || []).join("\n") || "Aucun interdit déclaré"],
      ],
    });
  }

  function buildToolCards() {
    if (state.toolCatalog.length) return state.toolCatalog.map(normalizeTool);
    return [
      card({
        entity_id: "tools:catalog-unavailable",
        entity_type: "tool_container",
        role: "container",
        family: "tool",
        presentation_family: "tool",
        category: "Outil",
        type_tags: ["outil"],
        title: "Catalogue indisponible",
        summary: "Aucun état runtime n’est inventé lorsque le catalogue ne peut pas être chargé.",
        status: "neutral",
        back: [["Principe", "Catalogue absent ≠ outil absent · runtime non observé ≠ non installé."]],
      }),
    ];
  }

  function projectLookup() {
    const wanted = state.project.trim().toLocaleLowerCase("fr-FR");
    if (!wanted) return null;
    return state.projects.find(item => [item.project_id, item.code, item.display_name]
      .filter(Boolean)
      .some(value => String(value).toLocaleLowerCase("fr-FR") === wanted)) || null;
  }

  function rebuildGraph() {
    state.cards.clear();
    state.children.clear();
    for (const model of rootCards()) putCard(model);

    const selected = projectLookup();
    const selectedProjectId = selected?.project_id || state.project || null;
    const selectedCardId = selected ? projectEntityId(selected) : selectedProjectId ? `project:${selectedProjectId}` : null;

    const projectIds = state.projects.map(item => putCard(normalizeProject(item, { selected: item.project_id === selectedProjectId })));
    if (selectedProjectId && !projectIds.includes(selectedCardId)) {
      projectIds.push(putCard(normalizeProject({ project_id: selectedProjectId, display_name: selectedProjectId, code: selectedProjectId, status: "active", contacts: [], attributes: {} }, { selected: true })));
    }
    setChildren("space:affaires", projectIds);

    const knowledgeIds = state.knowledge.map(item => putCard(normalizeKnowledge(item)));
    setChildren("space:connaissances", knowledgeIds);

    const workDecisionIds = state.workIssues
      .filter(item => ["review", "needs_review"].includes(workData(item).status))
      .map(item => putCard(normalizeWorkDecision(item)));
    const changeDecisionIds = state.changeCandidates
      .filter(item => item.status === "pending_review")
      .map(item => putCard(normalizeChangeCandidate(item)));
    setChildren("space:decisions", [...changeDecisionIds, ...workDecisionIds]);
    setChildren("space:pantheon", []);

    const tools = buildToolCards();
    tools.forEach(putCard);
    setChildren("space:outils", tools.map(item => item.entity_id));

    if (selectedCardId && state.cards.has(selectedCardId)) {
      const contactsId = putCard(normalizeContacts(selectedProjectId, selected?.contacts || []));
      const informationIds = state.information.map(item => putCard(normalizeInformation(item)));
      const legacyIds = state.legacyDocuments.map(item => putCard(normalizeLegacyDocument(item)));
      const workIds = state.workIssues.map(item => putCard(normalizeWork(item)));
      setChildren(contactsId, []);
      setChildren(selectedCardId, [contactsId, ...informationIds, ...legacyIds, ...workIds]);
    }

    state.navigator = window.PantheonSpatialNavigation.create({
      root_collection_id: "primary-spaces",
      root_item_ids: ROOT_SPACES.map(space => `space:${space}`),
    });
  }

  function familyLabel(model) {
    return ({ pantheon: "Pantheon", project: "Projet", information: "Information", contact: "Contacts", work: "Travail", decision: "Décision", tool: "Outil" })[model.presentation_family] || model.category || model.family;
  }

  function tagToken(value, kind) {
    const map = kind === "type" ? registries.typeTags : registries.subjectTags;
    const entry = registryEntry(map, value);
    const node = document.createElement("span");
    node.className = kind === "type" ? "v2-type-tag" : "v2-subject-tag-icon";
    node.title = entry?.description || entry?.title || String(value);
    node.setAttribute("aria-label", entry?.title || String(value));
    setTokenColor(node, entry);
    const short = entry?.title || String(value);
    node.textContent = short.length <= 3 ? short.toUpperCase() : short.slice(0, 2).toUpperCase();
    return node;
  }

  function stateToken(value, kind = "status") {
    const entry = registryEntry(kind === "limit" ? registries.limits : registries.statuses, value);
    const node = document.createElement("span");
    node.className = "v2-state-icon";
    node.title = entry?.title || statusLabel(value);
    node.setAttribute("aria-label", node.title);
    setTokenColor(node, entry);
    node.textContent = (entry?.title || statusLabel(value)).slice(0, 2).toUpperCase();
    return node;
  }

  function renderIdentity(model) {
    const identity = document.createElement("div");
    identity.className = "v2-card-identity";
    const line = document.createElement("div");
    line.className = "v2-card-identity-line";
    const mark = document.createElement("span");
    mark.className = "v2-family-mark v2-family-mark--identity";
    mark.textContent = FAMILY_MARKS[model.presentation_family] || "I";
    mark.title = familyLabel(model);
    const category = document.createElement("span");
    category.className = "v2-card-category";
    category.textContent = model.category || familyLabel(model);
    const typeTags = document.createElement("span");
    typeTags.className = "v2-card-type-tags";
    for (const tag of (model.type_tags || []).slice(0, 4)) typeTags.append(tagToken(tag, "type"));
    line.append(mark, category, typeTags);
    const meta = document.createElement("div");
    meta.className = "v2-card-meta";
    meta.textContent = [model.index, model.date ? String(model.date).slice(0, 10) : null].filter(Boolean).join(" · ");
    identity.append(line, meta);
    return identity;
  }

  function renderStates(model) {
    const states = document.createElement("div");
    states.className = "v2-card-states";
    states.append(stateToken(model.status, "status"));
    for (const limit of (model.limits || []).slice(0, 3)) states.append(stateToken(limit, "limit"));
    return states;
  }

  function renderFront(model) {
    const face = document.createElement("div");
    face.className = "v2-card-face v2-card-front";
    const header = document.createElement("header");
    header.className = "v2-card-top";
    header.append(renderIdentity(model), renderStates(model));
    const body = document.createElement("div");
    body.className = "v2-card-body";
    if (model.front?.issuer) {
      const issuer = document.createElement("p");
      issuer.className = "v2-card-kicker";
      issuer.textContent = model.front.issuer;
      body.append(issuer);
    }
    const title = document.createElement("h2");
    title.className = "v2-card-title";
    title.textContent = model.title;
    const summary = document.createElement("p");
    summary.className = "v2-card-summary";
    summary.textContent = model.summary;
    body.append(title, summary);
    const footer = document.createElement("footer");
    footer.className = "v2-card-footer";
    const rail = document.createElement("div");
    rail.className = "v2-indicator-rail";
    for (const tag of (model.subject_tags || []).slice(0, 5)) rail.append(tagToken(tag, "subject"));
    footer.append(rail);
    face.append(header, body, footer);
    return face;
  }

  function renderBackValue(value) {
    const node = document.createElement("p");
    const lines = String(value ?? "").split("\n").filter(Boolean);
    if (lines.length <= 1) {
      node.textContent = String(value ?? "");
      return node;
    }
    node.className = "v2-back-multiline";
    for (const line of lines) {
      const span = document.createElement("span");
      span.textContent = line;
      node.append(span);
    }
    return node;
  }

  function renderBack(model) {
    const face = document.createElement("div");
    face.className = "v2-card-face v2-card-back";
    const header = document.createElement("header");
    header.className = "v2-card-top";
    header.append(renderIdentity(model), renderStates(model));
    const machineKicker = document.createElement("span");
    machineKicker.className = "v2-card-kicker v2-card-kicker--machine";
    machineKicker.textContent = `${model.family} · ${model.entity_type}`;
    machineKicker.hidden = true;
    header.append(machineKicker);

    const body = document.createElement("div");
    body.className = "v2-back-body";
    const title = document.createElement("h2");
    title.className = "v2-back-title";
    title.textContent = model.title;
    body.append(title);
    for (const [heading, value] of model.back || []) {
      const row = document.createElement("section");
      row.className = "v2-back-section";
      const headingNode = document.createElement("h3");
      headingNode.textContent = heading;
      row.append(headingNode, renderBackValue(value));
      body.append(row);
    }

    const footer = document.createElement("footer");
    footer.className = "v2-card-footer";
    const actions = document.createElement("div");
    actions.className = "v2-card-actions";
    for (const action of model.available_actions || []) {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = action;
      button.disabled = true;
      button.title = "L’action ne devient cliquable qu’après autorisation serveur";
      actions.append(button);
    }
    const labels = document.createElement("div");
    labels.className = "v2-back-tag-labels";
    for (const tag of model.subject_tags || []) {
      const entry = registryEntry(registries.subjectTags, tag);
      const chip = document.createElement("span");
      chip.className = "v2-back-tag-label";
      chip.textContent = entry?.title || tag;
      setTokenColor(chip, entry);
      labels.append(chip);
    }
    const machineIdentity = document.createElement("span");
    machineIdentity.className = "v2-entity-id";
    machineIdentity.textContent = model.entity_id;
    machineIdentity.hidden = true;
    footer.append(actions, labels, machineIdentity);
    face.append(header, body, footer);
    return face;
  }

  function renderCard(model) {
    const wrapper = document.createElement("article");
    wrapper.className = "v2-card";
    wrapper.dataset.family = model.presentation_family || model.family;
    wrapper.dataset.role = model.role;
    wrapper.dataset.status = model.status;
    wrapper.dataset.flipped = state.flipped.has(model.entity_id) ? "true" : "false";
    if (model.base_acted_id) wrapper.dataset.baseActedId = model.base_acted_id;
    wrapper.style.setProperty("--identity-accent", model.identity_accent || stableAccent(model.entity_id));
    const inner = document.createElement("div");
    inner.className = "v2-card-inner";
    inner.append(renderFront(model), renderBack(model));
    wrapper.append(inner);
    return wrapper;
  }

  function currentModel() {
    return state.cards.get(state.navigator?.currentId()) || null;
  }

  function breadcrumbLabels() {
    return state.navigator.snapshot().path.map(part => state.cards.get(part.current_id)?.title).filter(Boolean);
  }

  function setMessage(message) {
    $("v2-status").textContent = message;
  }

  function updateSpaceRail() {
    const rootCurrent = state.navigator.snapshot().path[0]?.current_id;
    for (const button of document.querySelectorAll("[data-space]")) {
      button.classList.toggle("is-active", `space:${button.dataset.space}` === rootCurrent);
    }
  }

  function render() {
    if (!state.navigator) return;
    const snap = state.navigator.snapshot();
    const model = currentModel();
    const stage = $("v2-stage");
    stage.replaceChildren();
    stage.dataset.motion = state.lastMove;
    if (model) stage.append(renderCard(model));
    else {
      const empty = document.createElement("div");
      empty.className = "v2-empty";
      empty.textContent = "Aucune carte dans cette collection.";
      stage.append(empty);
    }
    $("v2-breadcrumb").textContent = breadcrumbLabels().join(" / ");
    $("v2-previous").disabled = !snap.can_move_previous;
    $("v2-next").disabled = !snap.can_move_next;
    $("v2-ascend").disabled = !snap.can_ascend;
    $("v2-descend").disabled = !model || (!(state.children.get(model.entity_id) || []).length && model.entity_type !== "project");
    $("v2-flip").disabled = !model;
    updateSpaceRail();
  }

  function moveHorizontal(delta) {
    state.lastMove = delta < 0 ? "right" : "left";
    state.navigator.moveHorizontal(delta);
    render();
  }

  async function descend() {
    const model = currentModel();
    if (!model) return;
    const children = state.children.get(model.entity_id) || [];
    if (!children.length && model.entity_type === "project" && model.source_project_id && model.source_project_id !== state.project) {
      $("v2-project").value = model.source_project_id;
      await loadProject({ focusProject: true });
      return;
    }
    if (!children.length) {
      toggleFlip();
      setMessage("Cette carte n’a pas d’enfant déclaré ; verso affiché à la place.");
      return;
    }
    state.lastMove = "up";
    state.navigator.descend({
      parent_entity_id: model.entity_id,
      collection_id: `children:${model.entity_id}`,
      item_ids: children,
    });
    render();
  }

  function ascend() {
    if (!state.navigator.snapshot().can_ascend) return;
    state.lastMove = "down";
    state.navigator.ascend();
    render();
  }

  function toggleFlip() {
    const model = currentModel();
    if (!model) return;
    if (state.flipped.has(model.entity_id)) state.flipped.delete(model.entity_id);
    else state.flipped.add(model.entity_id);
    render();
  }

  function jumpToSpace(space) {
    state.lastMove = "root";
    state.navigator.returnToRoot(`space:${space}`);
    render();
  }

  async function api(path) {
    const response = await fetch(path, { headers: { Authorization: `Bearer ${state.token}` } });
    if (!response.ok) {
      const payload = await response.json().catch(() => ({ detail: response.statusText }));
      throw new Error(payload.detail || response.statusText);
    }
    return response.json();
  }

  async function loadAgencyProjects() {
    const payload = await api("../v1/agency/projects?limit=200");
    state.projects = payload.projects || [];
    return state.projects;
  }

  async function loadProjectSchema() {
    const payload = await api("../v1/agency/schema/project");
    state.projectSchema = payload.schema || null;
    return state.projectSchema;
  }

  async function loadProject(options = {}) {
    const focusProject = Boolean(options.focusProject);
    const requested = $("v2-project").value.trim();
    state.token = $("v2-token").value;
    if (!state.token) {
      setMessage("Clé d’accès requise pour lire Agency Data.");
      return;
    }
    $("v2-load").disabled = true;
    setMessage("Chargement d’Agency Data…");
    try {
      await Promise.all([loadAgencyProjects(), loadProjectSchema()]);
      state.project = requested;
      const matched = projectLookup();
      if (matched?.project_id) {
        state.project = matched.project_id;
        $("v2-project").value = matched.code || matched.display_name || matched.project_id;
      }
      if (!state.project) {
        state.information = [];
        state.legacyDocuments = [];
        state.knowledge = [];
        state.workIssues = [];
        state.changeCandidates = [];
        rebuildGraph();
        state.navigator.returnToRoot("space:affaires");
        render();
        setMessage(`${state.projects.length} affaire(s) chargée(s).`);
        return;
      }

      const [information, documents, knowledge, workIssues, candidates] = await Promise.all([
        api(`../v1/agency/projects/${encodeURIComponent(state.project)}/information`),
        api(`../v1/projects/${encodeURIComponent(state.project)}/documents`),
        api(`../v1/projects/${encodeURIComponent(state.project)}/knowledge`),
        api(`../v1/projects/${encodeURIComponent(state.project)}/work-issues`),
        api(`../v1/agency/projects/${encodeURIComponent(state.project)}/change-candidates?status=pending_review&limit=100`),
      ]);
      state.information = information.information || [];
      state.legacyDocuments = documents.documents || [];
      state.knowledge = knowledge.knowledge || [];
      state.workIssues = workIssues.work_issues || [];
      state.changeCandidates = candidates.change_candidates || [];

      rebuildGraph();
      state.navigator.returnToRoot("space:affaires");
      if (focusProject || state.project) {
        const projectIds = state.children.get("space:affaires") || [];
        const target = projectIds.find(id => state.cards.get(id)?.source_project_id === state.project);
        if (target) {
          state.navigator.descend({
            parent_entity_id: "space:affaires",
            collection_id: "children:space:affaires",
            item_ids: projectIds,
            initial_entity_id: target,
          });
        }
      }
      render();
      setMessage(`Affaire ${matched?.display_name || matched?.code || state.project} chargée · ${state.changeCandidates.length} modification(s) à valider.`);
    } catch (error) {
      state.information = [];
      state.legacyDocuments = [];
      state.knowledge = [];
      state.workIssues = [];
      state.changeCandidates = [];
      rebuildGraph();
      render();
      setMessage(`Chargement refusé : ${error.message}`);
    } finally {
      $("v2-load").disabled = false;
    }
  }

  function bindGestures() {
    const stage = $("v2-stage");
    let start = null;
    stage.addEventListener("pointerdown", event => {
      start = { x: event.clientX, y: event.clientY, id: event.pointerId };
      stage.setPointerCapture?.(event.pointerId);
    });
    stage.addEventListener("pointerup", event => {
      if (!start || start.id !== event.pointerId) return;
      const dx = event.clientX - start.x;
      const dy = event.clientY - start.y;
      start = null;
      if (Math.max(Math.abs(dx), Math.abs(dy)) < 54) return;
      if (Math.abs(dx) > Math.abs(dy)) moveHorizontal(dx < 0 ? 1 : -1);
      else if (dy < 0) void descend();
      else ascend();
    });
  }

  function bindControls() {
    $("v2-previous").addEventListener("click", () => moveHorizontal(-1));
    $("v2-next").addEventListener("click", () => moveHorizontal(1));
    $("v2-ascend").addEventListener("click", ascend);
    $("v2-descend").addEventListener("click", () => void descend());
    $("v2-flip").addEventListener("click", toggleFlip);
    $("v2-load").addEventListener("click", () => void loadProject());
    document.querySelectorAll("[data-space]").forEach(button => button.addEventListener("click", () => jumpToSpace(button.dataset.space)));
    document.addEventListener("keydown", event => {
      if (["INPUT", "TEXTAREA"].includes(document.activeElement?.tagName)) return;
      const actions = {
        ArrowLeft: () => moveHorizontal(-1),
        ArrowRight: () => moveHorizontal(1),
        ArrowUp: () => void descend(),
        ArrowDown: ascend,
        Enter: () => void descend(),
        " ": toggleFlip,
      };
      const action = actions[event.key];
      if (action) {
        event.preventDefault();
        action();
      }
    });
    bindGestures();
  }

  function setNetwork() {
    $("v2-network").textContent = navigator.onLine ? "en ligne" : "hors ligne";
  }

  async function init() {
    await Promise.all([
      loadRegistry("registries/type_tags.json", "tags", registries.typeTags),
      loadRegistry("registries/subject_tags.json", "tags", registries.subjectTags),
      loadRegistry("registries/status_registry.json", "values", registries.statuses),
      loadRegistry("registries/limit_registry.json", "values", registries.limits),
      loadToolCatalog(),
    ]);
    rebuildGraph();
    bindControls();
    setNetwork();
    window.addEventListener("online", setNetwork);
    window.addEventListener("offline", setNetwork);
    render();
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", () => void init(), { once: true });
  else void init();
})();
