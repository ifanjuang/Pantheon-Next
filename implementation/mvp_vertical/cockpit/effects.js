(() => {
  const byId = id => document.getElementById(id);
  const moduleState = { proposals: [], response: null };

  const effectIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7h11"/><path d="m12 4 3 3-3 3"/><path d="M20 17H9"/><path d="m12 14-3 3 3 3"/></svg>';
  const decisionIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v13M7 7h10M5 20h14"/><path d="m7 7-3 5h6zM17 7l-3 5h6z"/></svg>';
  const scopeIcon = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="3.5"/><path d="M12 1.5v3M22.5 12h-3M12 22.5v-3M1.5 12h3"/></svg>';

  function currentProject() {
    return byId("project")?.value.trim() || "";
  }

  function currentToken() {
    return byId("token")?.value || "";
  }

  function draftKey() {
    return `pantheon-effect-preview:${currentProject() || "unscoped"}`;
  }

  function readDraft() {
    try {
      return JSON.parse(sessionStorage.getItem(draftKey()) || "{}") || {};
    } catch {
      return {};
    }
  }

  function writeDraft(value) {
    sessionStorage.setItem(draftKey(), JSON.stringify(value));
  }

  function typeLockup(label = "Rapprochement") {
    const lockup = document.createElement("div");
    lockup.className = "type-lockup";
    lockup.innerHTML = `<span class="type-icon">${effectIcon}</span><span class="type-label">${label}</span>`;
    return lockup;
  }

  function responsibility(svg, label, attention = false) {
    const item = document.createElement("span");
    item.className = "responsibility-icon";
    item.title = label;
    item.setAttribute("aria-label", label);
    if (attention) item.dataset.attention = "true";
    item.innerHTML = svg;
    return item;
  }

  function section(title, entries) {
    const wrapper = document.createElement("section");
    wrapper.className = "detail-section";
    const heading = document.createElement("h3");
    heading.textContent = title;
    wrapper.append(heading);
    const values = entries.filter(Boolean);
    if (values.length === 1) {
      const paragraph = document.createElement("p");
      paragraph.textContent = values[0];
      wrapper.append(paragraph);
    } else {
      const list = document.createElement("ul");
      for (const value of values) {
        const item = document.createElement("li");
        item.textContent = value;
        list.append(item);
      }
      wrapper.append(list);
    }
    return wrapper;
  }

  function openDialog(title, content) {
    const dialog = byId("detail-dialog");
    byId("detail-kind").replaceChildren(typeLockup());
    const detail = byId("detail-content");
    detail.replaceChildren();
    const heading = document.createElement("h2");
    heading.id = "detail-title";
    heading.textContent = title;
    detail.append(heading, content);
    dialog.showModal();
  }

  function createCard({ title, summary, signal, status, context, label, onOpen, attention = false }) {
    const card = document.createElement("article");
    card.className = "p-card";
    card.dataset.kind = "effect";
    card.dataset.status = status;
    card.dataset.frame = "gradient";
    if (attention) card.dataset.attention = "human";

    const button = document.createElement("button");
    button.type = "button";
    button.className = "card-button";
    button.setAttribute("aria-label", `Ouvrir le détail : ${title}`);
    button.addEventListener("click", onOpen);

    const header = document.createElement("header");
    header.className = "card-header";
    header.append(typeLockup(label));

    const body = document.createElement("div");
    body.className = "card-body";
    const heading = document.createElement("h3");
    heading.className = "card-title";
    heading.textContent = title;
    const copy = document.createElement("p");
    copy.className = "card-summary";
    copy.textContent = summary;
    const mainSignal = document.createElement("p");
    mainSignal.className = "card-signal";
    mainSignal.textContent = signal;
    body.append(heading, copy, mainSignal);

    const footer = document.createElement("footer");
    footer.className = "card-footer";
    const meta = document.createElement("div");
    meta.className = "card-meta";
    const statusLine = document.createElement("p");
    statusLine.className = "card-status";
    statusLine.textContent = status === "proposal" ? "Proposition seulement" : "Brouillon local";
    const contextLine = document.createElement("p");
    contextLine.className = "card-context";
    contextLine.textContent = context || "Contexte non renseigné";
    meta.append(statusLine, contextLine);
    const icons = document.createElement("div");
    icons.className = "responsibility-row";
    icons.append(
      responsibility(scopeIcon, "Périmètre exact du projet"),
      responsibility(decisionIcon, "Confirmation humaine obligatoire", true),
    );
    footer.append(meta, icons);
    card.append(button, header, body, footer);
    return card;
  }

  function effectInputCard() {
    return createCard({
      title: "Rapprocher une information",
      summary: "Chercher d’abord un objet existant avant de proposer une création ou une modification.",
      signal: "Aucun effet ne sera appliqué",
      status: "draft",
      context: currentProject() || "Projet non ouvert",
      label: "Rapprochement",
      attention: true,
      onOpen: openEffectForm,
    });
  }

  function proposalCard(proposal) {
    const target = proposal.target;
    const targetLabel = target ? `${target.object_type} · ${target.title}` : "Nouvel objet à qualifier";
    return createCard({
      title: proposal.effect,
      summary: targetLabel,
      signal: `${proposal.confidence} · score ${Math.round((proposal.score || 0) * 100)} %`,
      status: "proposal",
      context: currentProject(),
      label: "Effet candidat",
      attention: true,
      onOpen: () => openProposal(proposal),
    });
  }

  function renderEffectScene() {
    document.querySelectorAll("[data-scene]").forEach(button => {
      button.classList.toggle("is-active", button.dataset.scene === "effects");
    });
    byId("scene-eyebrow").textContent = "RAPPROCHEMENT";
    byId("scene-title").textContent = "Qualifier une nouvelle information";
    byId("scene-status").textContent = moduleState.proposals.length
      ? `${moduleState.proposals.length} proposition(s) non persistée(s).`
      : "La création reste le dernier recours ; aucune proposition n’est appliquée automatiquement.";
    const deck = byId("deck");
    deck.replaceChildren(effectInputCard());
    for (const proposal of moduleState.proposals) deck.append(proposalCard(proposal));
  }

  function openEffectForm() {
    const draft = readDraft();
    const form = document.createElement("div");
    form.className = "effect-form";
    form.append(section("Limite", [
      "Cette prévisualisation recherche des objets dans le projet exact.",
      "Elle ne crée, ne modifie, ne remplace et ne marque aucun objet en conflit.",
    ]));

    const informationBlock = document.createElement("label");
    informationBlock.textContent = "Nouvelle information";
    const information = document.createElement("textarea");
    information.id = "effect-information";
    information.rows = 6;
    information.placeholder = "Ex. Le client supprime finalement la couverture zinc du programme.";
    information.value = draft.information || "";
    informationBlock.append(information);

    const grid = document.createElement("div");
    grid.className = "effect-grid";
    const hintLabel = document.createElement("label");
    hintLabel.textContent = "Effet pressenti";
    const hint = document.createElement("select");
    hint.id = "effect-hint";
    for (const [value, label] of [
      ["", "Détection déterministe"],
      ["UPDATE", "UPDATE · compléter"],
      ["SUPERSEDE", "SUPERSEDE · remplacer"],
      ["CONFLICT", "CONFLICT · contradiction"],
      ["CREATE", "CREATE · nouvel objet"],
    ]) {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = label;
      option.selected = draft.effectHint === value;
      hint.append(option);
    }
    hintLabel.append(hint);

    const refsLabel = document.createElement("label");
    refsLabel.textContent = "Références explicites facultatives";
    const refs = document.createElement("input");
    refs.id = "effect-refs";
    refs.placeholder = "knowledge.id, issue-id, doc-id";
    refs.value = draft.refs || "";
    refsLabel.append(refs);
    grid.append(hintLabel, refsLabel);

    const action = document.createElement("button");
    action.type = "button";
    action.className = "primary-action";
    action.textContent = "Prévisualiser les effets";
    const message = document.createElement("p");
    message.className = "effect-message";
    message.setAttribute("role", "status");
    action.addEventListener("click", () => previewEffects({ information, hint, refs, action, message }));
    form.append(informationBlock, grid, action, message);
    openDialog("Rapprocher une information", form);
  }

  async function previewEffects({ information, hint, refs, action, message }) {
    const project = currentProject();
    const token = currentToken();
    const text = information.value.trim();
    const referenceValues = refs.value.split(",").map(value => value.trim()).filter(Boolean);
    writeDraft({ information: text, effectHint: hint.value, refs: refs.value });
    if (!project || !token) {
      message.textContent = "Ouvrez d’abord un projet avec une clé d’accès.";
      return;
    }
    if (text.length < 3) {
      message.textContent = "L’information est trop courte.";
      return;
    }

    action.disabled = true;
    message.textContent = "Recherche des objets existants…";
    try {
      const response = await fetch(`../v1/projects/${encodeURIComponent(project)}/effects/preview`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
        body: JSON.stringify({
          information: text,
          explicit_object_refs: referenceValues,
          effect_hint: hint.value || null,
          max_proposals: 5,
        }),
      });
      const payload = await response.json().catch(() => ({ detail: response.statusText }));
      if (!response.ok) throw new Error(payload.detail || response.statusText);
      moduleState.response = payload;
      moduleState.proposals = payload.proposals || [];
      byId("detail-dialog").close();
      renderEffectScene();
    } catch (error) {
      message.textContent = `Prévisualisation refusée : ${error.message}`;
    } finally {
      action.disabled = false;
    }
  }

  function openProposal(proposal) {
    const target = proposal.target;
    const eligibleKnowledgeUpdate = proposal.effect === "UPDATE" && target?.object_type === "knowledge";
    const wrapper = document.createElement("div");
    wrapper.className = "effect-proposal-detail";
    wrapper.append(
      section("Effet proposé", [
        `Effet : ${proposal.effect}`,
        `Origine de la qualification : ${proposal.effect_source}`,
        `Confiance : ${proposal.confidence}`,
        `Score de rapprochement : ${Math.round((proposal.score || 0) * 100)} %`,
      ]),
      section("Cible candidate", target ? [
        `Type : ${target.object_type}`,
        `Objet : ${target.object_id}`,
        `Titre : ${target.title}`,
        `Statut actuel : ${target.current_status}`,
      ] : [
        "Aucune cible existante suffisamment proche.",
        "Le type du nouvel objet reste à choisir par un humain.",
      ]),
      section("Raisons", proposal.reasons || ["Aucune raison exposée."]),
      section("Gouvernance", [
        "Confirmation humaine obligatoire.",
        eligibleKnowledgeUpdate
          ? "Seul un sas propriétaire Knowledge peut être préparé ; aucun effet générique n’est applicable."
          : "Aucune route d’application propriétaire n’est disponible pour cet effet ou cette cible.",
        ...(moduleState.response?.limits || []),
      ]),
    );

    if (eligibleKnowledgeUpdate) {
      const action = document.createElement("button");
      action.type = "button";
      action.className = "primary-action";
      action.textContent = "Préparer la mise à jour Knowledge";
      action.addEventListener("click", () => {
        document.dispatchEvent(new CustomEvent("pantheon:knowledge-update-request", {
          detail: {
            proposal,
            project: currentProject(),
            token: currentToken(),
          },
        }));
      });
      wrapper.append(action);
    }
    openDialog(`${proposal.effect} · proposition`, wrapper);
  }

  function addEffectsTab() {
    const rail = document.querySelector(".scene-rail");
    if (!rail || rail.querySelector('[data-scene="effects"]')) return;
    const button = document.createElement("button");
    button.className = "scene-tab";
    button.dataset.scene = "effects";
    button.type = "button";
    button.textContent = "Rapprochement";
    button.addEventListener("click", renderEffectScene);
    rail.append(button);
  }

  function enhanceQuestionnaireSummary() {
    const summary = byId("question-summary");
    if (!summary || summary.querySelector("[data-effect-from-questionnaire]")) return;
    const entries = [...summary.querySelectorAll("li")]
      .map(item => item.textContent)
      .filter(value => value && !value.startsWith("Aucun effet"));
    if (!entries.length) return;
    const action = document.createElement("button");
    action.type = "button";
    action.className = "secondary-action";
    action.dataset.effectFromQuestionnaire = "true";
    action.textContent = "Rapprocher ces réponses";
    action.addEventListener("click", () => {
      const draft = readDraft();
      writeDraft({ ...draft, information: entries.join("\n") });
      byId("detail-dialog").close();
      renderEffectScene();
      openEffectForm();
    });
    summary.append(action);
  }

  document.addEventListener("click", event => {
    if (event.target.closest(".questionnaire-form .primary-action")) {
      setTimeout(enhanceQuestionnaireSummary, 0);
    }
  });

  addEffectsTab();
})();
