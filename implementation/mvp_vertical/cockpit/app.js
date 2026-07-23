const $ = id => document.getElementById(id);

const state = {
  project: "",
  token: "",
  scene: "now",
  documents: [],
  knowledge: [],
  workIssues: [],
};

const sceneCopy = {
  now: ["MAINTENANT", "Cartes à examiner"],
  work: ["TRAVAIL", "Sujets suivis et retours Hermes"],
  documents: ["DOCUMENTS", "Sources et représentations dérivées"],
  knowledge: ["KNOWLEDGE", "Connaissances éditoriales à revoir"],
  questionnaire: ["QUESTIONNAIRE", "Préciser une demande"],
};

const statusLabels = {
  ready: "Prêt à examiner",
  partial: "Partiel",
  failed: "Échec visible",
  generated_unreviewed: "Généré · non revu",
  needs_review: "Revue nécessaire",
  reviewed: "Revu",
  superseded: "Remplacé",
  conflict: "Conflit",
  draft: "Brouillon local",
  open: "Ouvert",
  in_progress: "En cours",
  waiting: "En attente",
  review: "Revue humaine",
  done: "Clôturé",
  cancelled: "Annulé",
};

const eventLabels = {
  created: "Nouveau",
  updated: "Mis à jour",
  status_changed: "Statut modifié",
  processed: "Analysé",
};

const supportedIcons = new Set([
  "document",
  "knowledge",
  "work",
  "questionnaire",
  "source",
  "review",
  "scope",
  "memory",
  "history",
  "decision",
  "hermes",
  "comment",
  "project",
  "evidence",
  "gate",
  "close",
]);

function icon(name) {
  const glyph = document.createElement("span");
  glyph.className = "radix-icon";
  glyph.dataset.icon = supportedIcons.has(name) ? name : "document";
  glyph.setAttribute("aria-hidden", "true");
  return glyph;
}

function setNetwork() {
  $("network").textContent = navigator.onLine ? "en ligne" : "hors ligne";
}

async function api(path) {
  const response = await fetch(path, {
    headers: { Authorization: `Bearer ${state.token}` },
  });
  if (!response.ok) {
    const payload = await response.json().catch(() => ({ detail: response.statusText }));
    throw new Error(payload.detail || response.statusText);
  }
  return response.json();
}

function statusLabel(status) {
  return statusLabels[status] || String(status || "À vérifier").replaceAll("_", " ");
}

function formatMoment(value) {
  if (!value) return "date non renseignée";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return String(value);
  return new Intl.DateTimeFormat("fr-FR", {
    dateStyle: "short",
    timeStyle: "short",
  }).format(date);
}

function eventWithin(kind, occurredAt, label = eventLabels[kind]) {
  const timestamp = new Date(occurredAt || 0).getTime();
  if (!timestamp || Date.now() - timestamp > 48 * 60 * 60 * 1000) return null;
  return { kind, label: label || "Activité récente", occurredAt };
}

function knowledgeRecentEvent(item) {
  const updated = item.updated_at || item.created_at;
  const created = item.created_at;
  const isUpdate = (item.version || 1) > 1 || (created && updated && created !== updated);
  return eventWithin(isUpdate ? "updated" : "created", updated);
}

function workRecentEvent(item) {
  const events = item.events || [];
  const latest = events.at(-1);
  if (!latest) return null;
  const mapping = {
    issue_created: ["created", "Nouveau"],
    comment_added: ["updated", "Commenté"],
    status_changed: ["status_changed", "Statut modifié"],
    hermes_started: ["updated", "Hermes lancé"],
    hermes_returned: ["updated", "Retour Hermes"],
    review_requested: ["status_changed", "Revue demandée"],
    issue_closed: ["status_changed", "Clôturé"],
  };
  const [kind, label] = mapping[latest.event_type] || ["updated", "Mis à jour"];
  return eventWithin(kind, latest.occurred_at, label);
}

function documentModel(item) {
  const naming = item.naming || {};
  const extraction = item.extraction || {};
  const status = item.analysis_status || "partial";
  const title = naming.object_name || naming.document_type || item.title || "Document";
  const descriptor = [naming.document_type, naming.phase_code, naming.revision_index].filter(Boolean).join(" · ");
  const signal = extraction.error
    ? "Une erreur d’extraction doit être examinée"
    : `${extraction.chunk_count || 0} segment(s) dérivé(s)`;

  return {
    id: item.card_id || `card-${item.document_id}`,
    kind: "document",
    typeLabel: "Document",
    title,
    summary: descriptor || "Document projet avec provenance et état d’analyse visibles.",
    status,
    signal,
    context: naming.phase_folder || item.parent_project_id,
    event: eventWithin("processed", extraction.finished_at),
    attention: status !== "ready" ? "human" : null,
    responsibilities: [
      { icon: "source", label: "Source liée · la carte n’est pas la source" },
      { icon: "history", label: "Extraction et provenance" },
      ...(status !== "ready" ? [{ icon: "review", label: "Revue humaine nécessaire", attention: true }] : []),
    ],
    sections: [
      ["Identité", [
        `Document : ${item.title || title}`,
        `Projet : ${item.parent_project_id || "non renseigné"}`,
        `Type média : ${item.media_type || "non renseigné"}`,
      ]],
      ["Source", [
        item.source_ref || "Localisation non exposée",
        `Empreinte : ${item.source_digest || "non exposée"}`,
        `La carte est une projection : source=${Boolean(item.authority?.is_source)}, preuve=${Boolean(item.authority?.is_evidence)}, mémoire=${Boolean(item.authority?.is_memory)}.`,
      ]],
      ["Extraction", [
        `Statut : ${statusLabel(status)}`,
        `Convertisseur : ${extraction.converter || "non renseigné"}`,
        `Version : ${extraction.converter_version || "non renseignée"}`,
        `Segments : ${extraction.chunk_count || 0}`,
        `Dernière analyse : ${formatMoment(extraction.finished_at)}`,
        ...(extraction.quality_flags || []).map(flag => `Signal qualité : ${flag}`),
        ...(extraction.error ? [`Erreur : ${extraction.error}`] : []),
      ]],
      ["Prochaine revue", [
        status === "ready"
          ? "Ouvrir le document ou son Markdown dérivé avant toute qualification."
          : "Examiner l’état incomplet ou l’erreur avant de s’appuyer sur le contenu.",
      ]],
    ],
  };
}

function knowledgeModel(item) {
  const status = item.review_status || "generated_unreviewed";
  const sourceCount = (item.source_chunk_refs || []).length;
  return {
    id: item.card_id || `card-${item.knowledge_id}`,
    kind: "knowledge",
    typeLabel: "Knowledge",
    title: item.title || "Knowledge",
    summary: `${item.family || "famille non renseignée"} · version ${item.version || 1}`,
    status,
    signal: `${sourceCount} segment(s) source · ${statusLabel(status)}`,
    context: item.parent_project_id,
    event: knowledgeRecentEvent(item),
    attention: ["generated_unreviewed", "needs_review"].includes(status) ? "human" : null,
    responsibilities: [
      { icon: "source", label: `${sourceCount} segment(s) source lié(s)` },
      { icon: "memory", label: "Knowledge n’est pas mémoire gouvernée" },
      {
        icon: "review",
        label: statusLabel(status),
        attention: ["generated_unreviewed", "needs_review"].includes(status),
      },
    ],
    sections: [
      ["Identité", [
        `Knowledge : ${item.knowledge_id || "non renseignée"}`,
        `Famille : ${item.family || "non renseignée"}`,
        `Version : ${item.version || 1}`,
        `Créée par : ${item.created_by || "non renseigné"}`,
        `Créée : ${formatMoment(item.created_at)}`,
        `Mise à jour : ${formatMoment(item.updated_at)}`,
      ]],
      ["Statut", [
        statusLabel(status),
        "Knowledge ≠ Evidence.",
        "Knowledge ≠ mémoire gouvernée.",
        "Knowledge ≠ doctrine.",
      ]],
      ["Provenance", [
        `Document lié : ${item.document_ref || "non renseigné"}`,
        `${sourceCount} référence(s) de segment conservée(s).`,
        `Empreinte Markdown : ${item.markdown_digest || "non exposée"}`,
      ]],
      ["Prochaine revue", [
        ["generated_unreviewed", "needs_review"].includes(status)
          ? "Relire le Markdown, les sources et les limites avant toute réutilisation conséquente."
          : "La réutilisation reste dépendante du dossier, du périmètre et des sources applicables.",
      ]],
    ],
  };
}

function workIssueModel(projection) {
  const issue = projection.work_issue || {};
  const status = issue.status || "open";
  const comments = projection.comments || [];
  const runs = projection.hermes_runs || [];
  const events = projection.events || [];
  const latestRun = runs.at(-1);
  const latestReturn = latestRun?.normalized_return || {};
  const statusSignals = {
    open: issue.assigned_to === "hermes" ? "Prêt pour un handoff Hermes borné" : "À prendre en charge",
    in_progress: latestRun ? `Run Hermes : ${statusLabel(latestRun.status)}` : "Travail en cours",
    waiting: latestReturn.summary || "Information, reprise ou capacité attendue",
    review: latestReturn.summary || "Résultat candidat à examiner par un humain",
    done: `Clôturé par un humain · ${issue.close_reason || "motif conservé"}`,
    cancelled: `Annulé · ${issue.close_reason || "motif conservé"}`,
  };

  const commentEntries = comments.slice(-3).map(comment => `${comment.author} · ${comment.body}`);
  const runEntries = runs.slice(-3).map(run => {
    const returned = run.normalized_return || {};
    return `${run.run_id} · ${statusLabel(run.status)}${returned.outcome ? ` · ${returned.outcome}` : ""}${returned.summary ? ` · ${returned.summary}` : ""}`;
  });
  const eventEntries = events.slice(-5).reverse().map(event => `${formatMoment(event.occurred_at)} · ${event.event_type} · ${event.actor_kind}`);

  return {
    id: `card-${issue.issue_id}`,
    kind: "work",
    typeLabel: "Travail",
    title: issue.title || "Work Issue",
    summary: `${issue.issue_type || "action"} · priorité ${issue.priority || "normale"}`,
    status,
    signal: statusSignals[status] || statusLabel(status),
    context: issue.case_ref || state.project,
    event: workRecentEvent(projection),
    attention: status === "review" || (status === "open" && issue.assigned_to !== "hermes") ? "human" : null,
    responsibilities: [
      { icon: "scope", label: `Effet demandé : ${issue.requested_effect || "non renseigné"}` },
      ...(issue.assigned_to === "hermes" ? [{ icon: "hermes", label: "Hermes exécute uniquement par handoff borné" }] : []),
      ...(comments.length ? [{ icon: "comment", label: `${comments.length} commentaire(s)` }] : []),
      { icon: "history", label: `${events.length} événement(s) append-only` },
      ...(status === "review" ? [{ icon: "decision", label: "Décision humaine attendue", attention: true }] : []),
    ],
    sections: [
      ["Identité", [
        `Work Issue : ${issue.issue_id || "non renseignée"}`,
        `Dossier : ${issue.case_ref || "non renseigné"}`,
        `Type : ${issue.issue_type || "non renseigné"}`,
        `Priorité : ${issue.priority || "non renseignée"}`,
        `Version : ${issue.version || 1}`,
      ]],
      ["État actuel", [
        `Statut : ${statusLabel(status)}`,
        `Assignation : ${issue.assigned_to || "non assignée"}`,
        `Effet demandé : ${issue.requested_effect || "non renseigné"}`,
        `Mise à jour : ${formatMoment(issue.updated_at)}`,
        ...(issue.close_reason ? [`Motif de clôture : ${issue.close_reason}`] : []),
      ]],
      ["Demande", [issue.description || "Description non renseignée"]],
      ["Périmètre d’exécution", [
        `Task Contract : ${issue.task_contract_ref || "absent"}`,
        `Context Pack : ${issue.context_pack_ref || "absent"}`,
        "Hermes ne dispose d’aucune autorité directe sur la base et ne peut ni clôturer ni annuler ce sujet.",
      ]],
      ["Commentaires récents", commentEntries.length ? commentEntries : ["Aucun commentaire."]],
      ["Runs Hermes récents", runEntries.length ? runEntries : ["Aucun run Hermes enregistré."]],
      ["Trace récente", eventEntries.length ? eventEntries : ["Aucun événement exposé."]],
      ["Prochaine revue", [
        status === "review"
          ? "Examiner le retour candidat, ses traces et ses limites, puis décider explicitement de la suite."
          : status === "done" || status === "cancelled"
            ? "Le statut terminal reste une décision humaine enregistrée ; il ne transforme pas le résultat en preuve."
            : "Poursuivre uniquement dans le périmètre déclaré et conserver tout blocage visible.",
      ]],
    ],
  };
}

function questionnaireModel() {
  return {
    id: "local-questionnaire",
    kind: "questionnaire",
    typeLabel: "Questionnaire",
    title: "Préciser la demande",
    summary: "Quatre questions pour réduire l’ambiguïté avant de préparer une réponse.",
    status: "draft",
    signal: "Brouillon local · aucun effet serveur",
    context: state.project || "non rattaché",
    event: null,
    attention: "human",
    responsibilities: [
      { icon: "scope", label: "Périmètre de la demande", attention: true },
      { icon: "decision", label: "Réponses confirmées par l’humain" },
    ],
    questionnaire: true,
  };
}

function currentModels() {
  const documents = state.documents.map(documentModel);
  const knowledge = state.knowledge.map(knowledgeModel);
  const work = state.workIssues.map(workIssueModel);
  if (state.scene === "work") return work;
  if (state.scene === "documents") return documents;
  if (state.scene === "knowledge") return knowledge;
  if (state.scene === "questionnaire") return [questionnaireModel()];
  return [...work, ...knowledge, ...documents].sort((a, b) => {
    const priority = value => value.attention === "human" ? 0 : value.event ? 1 : 2;
    const priorityDiff = priority(a) - priority(b);
    if (priorityDiff) return priorityDiff;
    const aTime = new Date(a.event?.occurredAt || 0).getTime();
    const bTime = new Date(b.event?.occurredAt || 0).getTime();
    return bTime - aTime;
  });
}

function typeLockup(model) {
  const lockup = document.createElement("div");
  lockup.className = "type-lockup";
  const iconCircle = document.createElement("span");
  iconCircle.className = "type-icon";
  iconCircle.append(icon(model.kind));
  const label = document.createElement("span");
  label.className = "type-label";
  label.textContent = model.typeLabel;
  lockup.append(iconCircle, label);
  return lockup;
}

function responsibilityButton(item) {
  const badge = document.createElement("span");
  badge.className = "responsibility-icon";
  badge.title = item.label;
  badge.setAttribute("aria-label", item.label);
  if (item.attention) badge.dataset.attention = "true";
  badge.append(icon(item.icon));
  return badge;
}

function renderCard(model) {
  const card = document.createElement("article");
  card.className = "p-card";
  card.dataset.kind = model.kind;
  card.dataset.status = model.status;
  card.dataset.frame = "gradient";
  if (model.event) card.dataset.event = model.event.kind;
  if (model.attention) card.dataset.attention = model.attention;

  const button = document.createElement("button");
  button.className = "card-button";
  button.type = "button";
  button.setAttribute("aria-label", `Ouvrir le détail : ${model.title}`);
  button.addEventListener("click", () => openDetail(model));

  const header = document.createElement("header");
  header.className = "card-header";
  header.append(typeLockup(model));
  if (model.event) {
    const event = document.createElement("span");
    event.className = "event-chip";
    event.textContent = model.event.label || eventLabels[model.event.kind] || "Récent";
    event.title = formatMoment(model.event.occurredAt);
    header.append(event);
  }

  const body = document.createElement("div");
  body.className = "card-body";
  const title = document.createElement("h3");
  title.className = "card-title";
  title.textContent = model.title;
  const summary = document.createElement("p");
  summary.className = "card-summary";
  summary.textContent = model.summary;
  const signal = document.createElement("p");
  signal.className = "card-signal";
  signal.textContent = model.signal;
  body.append(title, summary, signal);

  const footer = document.createElement("footer");
  footer.className = "card-footer";
  const meta = document.createElement("div");
  meta.className = "card-meta";
  const status = document.createElement("p");
  status.className = "card-status";
  status.textContent = statusLabel(model.status);
  const context = document.createElement("p");
  context.className = "card-context";
  context.textContent = model.context || "Contexte non renseigné";
  meta.append(status, context);
  const responsibilities = document.createElement("div");
  responsibilities.className = "responsibility-row";
  for (const item of model.responsibilities || []) responsibilities.append(responsibilityButton(item));
  footer.append(meta, responsibilities);

  card.append(button, header, body, footer);
  return card;
}

function sectionElement(title, entries) {
  const section = document.createElement("section");
  section.className = "detail-section";
  const heading = document.createElement("h3");
  heading.textContent = title;
  section.append(heading);
  const values = entries.flat().filter(Boolean);
  if (values.length === 1) {
    const paragraph = document.createElement("p");
    paragraph.textContent = values[0];
    section.append(paragraph);
  } else {
    const list = document.createElement("ul");
    for (const entry of values) {
      const item = document.createElement("li");
      item.textContent = entry;
      list.append(item);
    }
    section.append(list);
  }
  return section;
}

function questionnaireContent() {
  const wrapper = document.createElement("div");
  wrapper.className = "questionnaire-form";
  const stored = JSON.parse(sessionStorage.getItem(`pantheon-questionnaire:${state.project || "unscoped"}`) || "{}");

  const intro = sectionElement("Limite", ["Ce questionnaire reste un brouillon local. Il ne crée, ne modifie, ne remplace et n’approuve aucune carte."]);
  wrapper.append(intro);

  const questions = [
    {
      id: "deliverable",
      title: "Quel résultat attendez-vous ?",
      type: "radio",
      options: ["Réponse courte", "Analyse détaillée", "Document à relire", "Décision à préparer"],
    },
    {
      id: "priorities",
      title: "Quels points doivent être prioritaires ?",
      type: "checkbox",
      options: ["Périmètre", "Sources", "Responsabilités", "Délais", "Coût"],
    },
    {
      id: "external",
      title: "Le résultat est-il destiné à une action externe ?",
      type: "radio",
      options: ["Oui", "Non", "À déterminer"],
    },
  ];

  for (const question of questions) {
    const block = document.createElement("section");
    block.className = "question-block";
    const heading = document.createElement("h3");
    heading.textContent = question.title;
    const options = document.createElement("div");
    options.className = "option-list";
    for (const option of question.options) {
      const label = document.createElement("label");
      const input = document.createElement("input");
      input.type = question.type;
      input.name = question.id;
      input.value = option;
      const previous = stored[question.id];
      input.checked = Array.isArray(previous) ? previous.includes(option) : previous === option;
      input.addEventListener("change", saveQuestionnaireDraft);
      label.append(input, document.createTextNode(option));
      options.append(label);
    }
    block.append(heading, options);
    wrapper.append(block);
  }

  const noteBlock = document.createElement("section");
  noteBlock.className = "question-block";
  const noteLabel = document.createElement("label");
  noteLabel.textContent = "Précision libre";
  const note = document.createElement("textarea");
  note.id = "question-note";
  note.rows = 4;
  note.placeholder = "Élément utile, limite ou contexte à conserver";
  note.value = stored.note || "";
  note.addEventListener("input", saveQuestionnaireDraft);
  noteLabel.append(note);
  noteBlock.append(noteLabel);
  wrapper.append(noteBlock);

  const action = document.createElement("button");
  action.type = "button";
  action.className = "primary-action";
  action.textContent = "Préparer le résumé";
  action.addEventListener("click", reviewQuestionnaire);
  wrapper.append(action);

  const output = document.createElement("section");
  output.id = "question-summary";
  output.className = "detail-section";
  wrapper.append(output);
  return wrapper;
}

function questionnaireValues() {
  const values = {};
  for (const name of ["deliverable", "external"]) {
    values[name] = document.querySelector(`input[name="${name}"]:checked`)?.value || "";
  }
  values.priorities = [...document.querySelectorAll('input[name="priorities"]:checked')].map(input => input.value);
  values.note = $("question-note")?.value.trim() || "";
  return values;
}

function saveQuestionnaireDraft() {
  sessionStorage.setItem(`pantheon-questionnaire:${state.project || "unscoped"}`, JSON.stringify(questionnaireValues()));
}

function reviewQuestionnaire() {
  const values = questionnaireValues();
  saveQuestionnaireDraft();
  const output = $("question-summary");
  output.replaceChildren();
  const heading = document.createElement("h3");
  heading.textContent = "Résumé à confirmer";
  const list = document.createElement("ul");
  const entries = [
    `Résultat attendu : ${values.deliverable || "non répondu"}`,
    `Priorités : ${values.priorities.length ? values.priorities.join(", ") : "non répondu"}`,
    `Action externe : ${values.external || "non répondu"}`,
    `Précision : ${values.note || "aucune"}`,
    "Aucun effet n’a été appliqué. Le rapprochement CREATE / UPDATE / SUPERSEDE / CONFLICT n’est pas encore implémenté dans ce lot.",
  ];
  for (const entry of entries) {
    const item = document.createElement("li");
    item.textContent = entry;
    list.append(item);
  }
  output.append(heading, list);
}

function openDetail(model) {
  $("detail-kind").replaceChildren(typeLockup(model));
  const content = $("detail-content");
  content.replaceChildren();
  const title = document.createElement("h2");
  title.id = "detail-title";
  title.textContent = model.title;
  content.append(title);
  if (model.event) content.append(sectionElement("Activité récente", [`${model.event.label} · ${formatMoment(model.event.occurredAt)}`]));
  if (model.questionnaire) content.append(questionnaireContent());
  else for (const [heading, entries] of model.sections || []) content.append(sectionElement(heading, entries));
  $("detail-dialog").showModal();
}

function render() {
  const [eyebrow, title] = sceneCopy[state.scene];
  $("scene-eyebrow").textContent = eyebrow;
  $("scene-title").textContent = title;
  const models = currentModels();
  $("scene-status").textContent = state.scene === "questionnaire"
    ? "Brouillon conservé uniquement pour cette session."
    : state.project
      ? `${models.length} carte(s) projetée(s) pour ${state.project}.`
      : "Indiquez un projet pour charger ses cartes.";
  const deck = $("deck");
  deck.replaceChildren();
  if (!models.length) deck.append($("empty-template").content.cloneNode(true));
  else for (const model of models) deck.append(renderCard(model));
}

async function loadProject() {
  state.project = $("project").value.trim();
  state.token = $("token").value;
  if (!state.project) {
    $("scene-status").textContent = "Le projet est obligatoire.";
    return;
  }
  if (!state.token) {
    $("scene-status").textContent = "La clé d’accès est obligatoire.";
    return;
  }
  $("load").disabled = true;
  $("scene-status").textContent = "Chargement des projections…";
  try {
    const [documents, knowledge, workIssues] = await Promise.all([
      api(`../v1/projects/${encodeURIComponent(state.project)}/documents`),
      api(`../v1/projects/${encodeURIComponent(state.project)}/knowledge`),
      api(`../v1/projects/${encodeURIComponent(state.project)}/work-issues`),
    ]);
    state.documents = documents.documents || [];
    state.knowledge = knowledge.knowledge || [];
    state.workIssues = workIssues.work_issues || [];
    render();
  } catch (error) {
    state.documents = [];
    state.knowledge = [];
    state.workIssues = [];
    render();
    $("scene-status").textContent = `Chargement refusé : ${error.message}`;
  } finally {
    $("load").disabled = false;
  }
}

for (const button of document.querySelectorAll("[data-scene]")) {
  button.addEventListener("click", () => {
    state.scene = button.dataset.scene;
    document.querySelectorAll("[data-scene]").forEach(tab => tab.classList.toggle("is-active", tab === button));
    render();
  });
}

$("load").addEventListener("click", loadProject);
window.addEventListener("online", setNetwork);
window.addEventListener("offline", setNetwork);
setNetwork();
render();
