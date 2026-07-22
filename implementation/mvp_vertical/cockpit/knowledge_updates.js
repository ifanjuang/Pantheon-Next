(() => {
  const byId = id => document.getElementById(id);
  const ACTOR_KEY = "pantheon-human-actor";

  function typeLockup() {
    const wrapper = document.createElement("div");
    wrapper.className = "type-lockup";
    wrapper.innerHTML = '<span class="type-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5.5c2.7-.9 5.3-.5 8 1.1v14c-2.7-1.6-5.3-2-8-1.1z"/><path d="M20 5.5c-2.7-.9-5.3-.5-8 1.1v14c2.7-1.6 5.3-2 8-1.1z"/></svg></span><span class="type-label">Knowledge Update</span>';
    return wrapper;
  }

  function section(title, content) {
    const wrapper = document.createElement("section");
    wrapper.className = "detail-section";
    const heading = document.createElement("h3");
    heading.textContent = title;
    wrapper.append(heading, content);
    return wrapper;
  }

  function paragraph(text) {
    const value = document.createElement("p");
    value.textContent = text;
    return value;
  }

  function messageNode() {
    const message = document.createElement("p");
    message.className = "effect-message";
    message.setAttribute("role", "status");
    return message;
  }

  function openDialog(title, content) {
    byId("detail-kind").replaceChildren(typeLockup());
    const target = byId("detail-content");
    target.replaceChildren();
    const heading = document.createElement("h2");
    heading.id = "detail-title";
    heading.textContent = title;
    target.append(heading, content);
    const dialog = byId("detail-dialog");
    if (!dialog.open) dialog.showModal();
  }

  async function requestJson(path, { token, actor, method = "GET", body } = {}) {
    const headers = { Authorization: `Bearer ${token}` };
    if (actor) headers["X-Pantheon-Human-Actor"] = actor;
    if (body !== undefined) headers["Content-Type"] = "application/json";
    const response = await fetch(path, {
      method,
      headers,
      body: body === undefined ? undefined : JSON.stringify(body),
    });
    const payload = await response.json().catch(() => ({ detail: response.statusText }));
    if (!response.ok) throw new Error(payload.detail || response.statusText);
    return payload;
  }

  async function requestMarkdown(path, token) {
    const response = await fetch(path, { headers: { Authorization: `Bearer ${token}` } });
    if (!response.ok) {
      const payload = await response.json().catch(() => ({ detail: response.statusText }));
      throw new Error(payload.detail || response.statusText);
    }
    return response.text();
  }

  function idempotencyKey() {
    if (globalThis.crypto?.randomUUID) return `cockpit-${globalThis.crypto.randomUUID()}`;
    return `cockpit-${Date.now()}-${Math.random().toString(16).slice(2)}`;
  }

  async function openKnowledgeUpdate({ proposal, project, token }) {
    const target = proposal?.target;
    if (!project || !token || proposal?.effect !== "UPDATE" || target?.object_type !== "knowledge") {
      return;
    }

    const loading = document.createElement("div");
    loading.className = "knowledge-update-flow";
    loading.append(paragraph("Chargement du Markdown propriétaire…"));
    openDialog("Préparer la mise à jour Knowledge", loading);

    try {
      const knowledgeId = target.object_id;
      const encodedId = encodeURIComponent(knowledgeId);
      const [card, markdown] = await Promise.all([
        requestJson(`../v1/knowledge/${encodedId}`, { token }),
        requestMarkdown(`../v1/knowledge/${encodedId}/markdown`, token),
      ]);
      renderEditor({ proposal, project, token, card, markdown });
    } catch (error) {
      loading.replaceChildren(paragraph(`Chargement refusé : ${error.message}`));
    }
  }

  function renderEditor({ proposal, project, token, card, markdown }) {
    const flow = document.createElement("div");
    flow.className = "knowledge-update-flow";
    flow.append(
      section("Périmètre", paragraph(
        `UPDATE de ${card.knowledge_id}, version ${card.version}. Le statut ${card.review_status} sera conservé.`
      )),
      section("Identité", paragraph(
        "L’identité ci-dessous est déclarée et liée à la clé éditeur partagée. Cette assurance reste partielle."
      )),
    );

    const actorLabel = document.createElement("label");
    actorLabel.textContent = "Identité humaine déclarée";
    const actor = document.createElement("input");
    actor.autocomplete = "username";
    actor.placeholder = "prenom.nom ou identifiant interne";
    actor.value = sessionStorage.getItem(ACTOR_KEY) || "";
    actorLabel.append(actor);

    const markdownLabel = document.createElement("label");
    markdownLabel.textContent = "Markdown proposé";
    const proposed = document.createElement("textarea");
    proposed.rows = 18;
    proposed.className = "knowledge-markdown-editor";
    proposed.value = markdown;
    markdownLabel.append(proposed);

    const previewButton = document.createElement("button");
    previewButton.type = "button";
    previewButton.className = "primary-action";
    previewButton.textContent = "Prévisualiser le diff signé";
    const message = messageNode();
    const previewArea = document.createElement("div");
    previewArea.className = "knowledge-update-preview";

    previewButton.addEventListener("click", async () => {
      const humanActor = actor.value.trim();
      const candidateMarkdown = proposed.value;
      if (!humanActor) {
        message.textContent = "L’identité humaine déclarée est obligatoire.";
        return;
      }
      if (!candidateMarkdown.trim()) {
        message.textContent = "Le Markdown proposé ne peut pas être vide.";
        return;
      }
      sessionStorage.setItem(ACTOR_KEY, humanActor);
      previewButton.disabled = true;
      message.textContent = "Calcul du diff et signature de l’effet exact…";
      previewArea.replaceChildren();
      try {
        const preview = await requestJson(
          `../v1/projects/${encodeURIComponent(project)}/knowledge/${encodeURIComponent(card.knowledge_id)}/updates/preview`,
          {
            token,
            actor: humanActor,
            method: "POST",
            body: {
              proposed_markdown: candidateMarkdown,
              expected_version: card.version,
              review_status: null,
            },
          },
        );
        message.textContent = "Diff prêt. Relisez-le puis saisissez la confirmation exacte.";
        renderSignedPreview({
          previewArea,
          preview,
          project,
          token,
          actor: humanActor,
          card,
          proposed,
          candidateMarkdown,
        });
      } catch (error) {
        message.textContent = `Prévisualisation refusée : ${error.message}`;
      } finally {
        previewButton.disabled = false;
      }
    });

    flow.append(actorLabel, markdownLabel, previewButton, message, previewArea);
    openDialog(`UPDATE · ${proposal.target.title}`, flow);
  }

  function renderSignedPreview({ previewArea, preview, project, token, actor, card, proposed, candidateMarkdown }) {
    const updateIdempotencyKey = idempotencyKey();
    const diff = document.createElement("pre");
    diff.className = "knowledge-diff";
    diff.textContent = preview.diff || "Aucune différence textuelle affichable.";

    const identity = paragraph(
      `Acteur : ${preview.identity.declared_actor} · assurance ${preview.identity.assurance} · expiration ${new Date(preview.confirmation.expires_at * 1000).toLocaleTimeString("fr-FR")}.`
    );
    const phraseLabel = document.createElement("label");
    phraseLabel.textContent = `Saisir exactement : ${preview.confirmation.phrase}`;
    const phrase = document.createElement("input");
    phrase.autocomplete = "off";
    phraseLabel.append(phrase);

    const applyButton = document.createElement("button");
    applyButton.type = "button";
    applyButton.className = "primary-action consequential-action";
    applyButton.textContent = "Appliquer cet UPDATE exact";
    applyButton.disabled = true;
    const result = messageNode();
    phrase.addEventListener("input", () => {
      applyButton.disabled = phrase.value !== preview.confirmation.phrase;
    });

    applyButton.addEventListener("click", async () => {
      if (proposed.value !== candidateMarkdown) {
        result.textContent = "Le Markdown a changé après la prévisualisation. Recalculez le diff.";
        applyButton.disabled = true;
        return;
      }
      applyButton.disabled = true;
      result.textContent = "Application transactionnelle de l’UPDATE…";
      try {
        const applied = await requestJson(
          `../v1/projects/${encodeURIComponent(project)}/knowledge/${encodeURIComponent(card.knowledge_id)}/updates/apply`,
          {
            token,
            actor,
            method: "POST",
            body: {
              proposed_markdown: candidateMarkdown,
              expected_version: card.version,
              review_status: null,
              base_markdown_digest: preview.base_markdown_digest,
              confirmation_token: preview.confirmation.token,
              confirmation_expires_at: preview.confirmation.expires_at,
              confirmation_phrase: phrase.value,
              idempotency_key: updateIdempotencyKey,
            },
          },
        );
        result.textContent = `UPDATE appliqué. Version actuelle : ${applied.knowledge.version}. Le statut de revue reste ${applied.knowledge.review_status}.`;
        phrase.disabled = true;
        proposed.disabled = true;
        document.dispatchEvent(new CustomEvent("pantheon:knowledge-updated", { detail: applied }));
      } catch (error) {
        result.textContent = `Application refusée : ${error.message}`;
        applyButton.disabled = false;
      }
    });

    previewArea.replaceChildren(
      section("Diff signé", diff),
      section("Identité et expiration", identity),
      phraseLabel,
      applyButton,
      result,
    );
  }

  document.addEventListener("pantheon:knowledge-update-request", event => {
    openKnowledgeUpdate(event.detail || {});
  });

  document.addEventListener("pantheon:knowledge-updated", () => {
    const load = byId("load");
    if (load && !load.disabled) load.click();
  });
})();
