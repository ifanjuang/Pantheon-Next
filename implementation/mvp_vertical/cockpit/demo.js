(() => {
  if (!window.PANTHEON_COCKPIT_DEMO) return;

  const now = new Date().toISOString();
  const demoActor = "Démonstration statique";

  Object.assign(iconPaths, {
    project: '<path d="M4 20V7.5L12 3l8 4.5V20z"/><path d="M8 20v-6h8v6M8 9h.01M12 9h.01M16 9h.01"/>',
    evidence: '<path d="M5 4.5h14v15H5z"/><path d="m8 12 2.3 2.3L16.5 8M8 17h8"/>',
    gate: '<path d="M7 21V4h10v17M3.5 21h17"/><path d="M10.5 11.5h.01"/>',
  });

  const references = [
    {
      knowledge_id: "reference-lexique-chantier",
      title: "Lexique technique et contractuel",
      family: "lexique professionnel",
      version: 5,
      review_status: "reviewed",
      source_chunk_refs: ["lexique-001", "lexique-014", "lexique-029"],
      document_ref: "corpus://reference/lexique-chantier",
      markdown_digest: "sha256:demo-lexique-reference",
      created_by: demoActor,
      created_at: now,
      updated_at: now,
    },
    {
      knowledge_id: "reference-ccag-travaux",
      title: "CCAG Travaux — corpus de référence",
      family: "référence contractuelle",
      version: 2,
      review_status: "reviewed",
      source_chunk_refs: ["ccag-003", "ccag-019", "ccag-042", "ccag-071"],
      document_ref: "corpus://reference/ccag-travaux",
      markdown_digest: "sha256:demo-ccag-reference",
      created_by: demoActor,
      created_at: now,
      updated_at: now,
    },
    {
      knowledge_id: "reference-dtu-43-1",
      title: "NF DTU 43.1 — étanchéité",
      family: "référence technique",
      version: 3,
      review_status: "needs_review",
      source_chunk_refs: ["dtu431-006", "dtu431-021", "dtu431-033"],
      document_ref: "corpus://reference/dtu-43-1",
      markdown_digest: "sha256:demo-dtu431-reference",
      created_by: demoActor,
      created_at: now,
      updated_at: now,
    },
    {
      knowledge_id: "reference-dtu-51-2",
      title: "NF DTU 51.2 — parquets collés",
      family: "référence technique",
      version: 1,
      review_status: "reviewed",
      source_chunk_refs: ["dtu512-004", "dtu512-017"],
      document_ref: "corpus://reference/dtu-51-2",
      markdown_digest: "sha256:demo-dtu512-reference",
      created_by: demoActor,
      created_at: now,
      updated_at: now,
    },
    {
      knowledge_id: "reference-accessibilite-erp",
      title: "Accessibilité ERP — points de contrôle",
      family: "guide réglementaire",
      version: 4,
      review_status: "reviewed",
      source_chunk_refs: ["erp-002", "erp-011", "erp-028"],
      document_ref: "corpus://reference/accessibilite-erp",
      markdown_digest: "sha256:demo-erp-reference",
      created_by: demoActor,
      created_at: now,
      updated_at: now,
    },
  ];

  const projects = [
    {
      id: "demo-maison-normande",
      title: "Maison normande",
      caseLabel: "Case MN-01",
      phase: "DCE",
      location: "Normandie",
      summary: "Réhabilitation et extension d’une maison individuelle.",
      status: "review",
      signal: "3 sujets ouverts · 1 décision attendue",
      context: {
        subject: "Finaliser le lot revêtements et ses interfaces",
        scope: "DCE · pièces écrites et cohérence technique",
        risks: "Plancher chauffant, limites de prestations, classes d’usage",
      },
      workIssues: [
        {
          work_issue: {
            issue_id: "issue-mn-revetements",
            case_ref: "MN-01",
            title: "Vérifier les limites du lot revêtements",
            issue_type: "review",
            priority: "haute",
            status: "review",
            assigned_to: "human",
            requested_effect: "review_only",
            description: "Comparer le CCTP, les plans et les références mobilisées avant émission.",
            task_contract_ref: "task-contract-mn-01",
            context_pack_ref: "context-pack-mn-revetements",
            version: 3,
            updated_at: now,
          },
          comments: [{ author: "Équipe projet", body: "Confirmer le parquet collé compatible avec le plancher chauffant." }],
          hermes_runs: [{ run_id: "run-mn-001", status: "done", normalized_return: { outcome: "candidate_return", summary: "Deux points techniques restent à arbitrer." } }],
          events: [{ event_type: "review_requested", actor_kind: "system", occurred_at: now }],
        },
        {
          work_issue: {
            issue_id: "issue-mn-etancheite",
            case_ref: "MN-01",
            title: "Qualifier l’interface terrasse et étanchéité",
            issue_type: "technical_review",
            priority: "normale",
            status: "open",
            assigned_to: "human",
            requested_effect: "analysis_only",
            description: "Vérifier le support, les relevés et la responsabilité du lot concerné.",
            task_contract_ref: "task-contract-mn-02",
            context_pack_ref: "context-pack-mn-etancheite",
            version: 1,
            updated_at: now,
          },
          comments: [],
          hermes_runs: [],
          events: [{ event_type: "issue_created", actor_kind: "human", occurred_at: now }],
        },
      ],
      documents: [
        {
          card_id: "card-mn-cctp-revetements",
          document_id: "document-mn-cctp-revetements",
          title: "CCTP — Revêtements de sol",
          parent_project_id: "MN-01",
          source_ref: "fixture://MN-01/DCE/CCTP-LOT-06.pdf",
          source_digest: "sha256:demo-mn-cctp",
          media_type: "application/pdf",
          analysis_status: "partial",
          naming: { object_name: "CCTP — Revêtements de sol", document_type: "CCTP", phase_code: "DCE", revision_index: "B1", phase_folder: "30_DCE / Pièces écrites" },
          extraction: { chunk_count: 42, converter: "Docling — fixture", converter_version: "demo", finished_at: now, quality_flags: ["tableaux à relire", "références produits à confirmer"], error: null },
          authority: { is_source: true, is_evidence: false, is_memory: false },
        },
        {
          card_id: "card-mn-plan-rdc",
          document_id: "document-mn-plan-rdc",
          title: "Plan RDC — repérage des sols",
          parent_project_id: "MN-01",
          source_ref: "fixture://MN-01/DCE/PLAN-RDC-SOLS.pdf",
          source_digest: "sha256:demo-mn-plan",
          media_type: "application/pdf",
          analysis_status: "ready",
          naming: { object_name: "Plan RDC — repérage des sols", document_type: "PLAN", phase_code: "DCE", revision_index: "A2", phase_folder: "30_DCE / Plans" },
          extraction: { chunk_count: 9, converter: "Docling — fixture", converter_version: "demo", finished_at: now, quality_flags: [], error: null },
          authority: { is_source: true, is_evidence: false, is_memory: false },
        },
        {
          card_id: "card-mn-ccap",
          document_id: "document-mn-ccap",
          title: "CCAP — marché de travaux",
          parent_project_id: "MN-01",
          source_ref: "fixture://MN-01/DCE/CCAP.pdf",
          source_digest: "sha256:demo-mn-ccap",
          media_type: "application/pdf",
          analysis_status: "ready",
          naming: { object_name: "CCAP — marché de travaux", document_type: "CCAP", phase_code: "DCE", revision_index: "A1", phase_folder: "30_DCE / Pièces administratives" },
          extraction: { chunk_count: 31, converter: "Docling — fixture", converter_version: "demo", finished_at: now, quality_flags: [], error: null },
          authority: { is_source: true, is_evidence: false, is_memory: false },
        },
      ],
      referenceIds: ["reference-lexique-chantier", "reference-ccag-travaux", "reference-dtu-43-1", "reference-dtu-51-2"],
      evidence: [
        {
          id: "evidence-mn-parquet",
          title: "Compatibilité du parquet collé",
          summary: "CCTP, plan de sols et référence technique rapprochés.",
          status: "needs_review",
          signal: "Support candidat · applicabilité à confirmer",
        },
        {
          id: "evidence-mn-limites",
          title: "Limites de prestations",
          summary: "CCAP et CCTP convergent, une interface reste ouverte.",
          status: "partial",
          signal: "Contradiction non résolue",
        },
      ],
      gates: [
        {
          id: "gate-mn-emission-dce",
          title: "Émission du lot 06",
          summary: "La version DCE ne doit pas être diffusée avant arbitrage des deux réserves.",
          status: "open",
          signal: "Décision humaine requise",
        },
      ],
    },
    {
      id: "demo-cabinet-medical",
      title: "Cabinet médical",
      caseLabel: "Case CM-04",
      phase: "Chantier",
      location: "Rouen",
      summary: "Aménagement d’un cabinet recevant du public.",
      status: "in_progress",
      signal: "2 revues · 1 point accessibilité",
      context: {
        subject: "Coordonner les modifications en cours de chantier",
        scope: "Chantier · sécurité, accessibilité et équipements",
        risks: "Sortie de secours, cloison serveur, accueil PMR",
      },
      workIssues: [
        {
          work_issue: {
            issue_id: "issue-cm-porte-cf",
            case_ref: "CM-04",
            title: "Contrôler la porte coupe-feu",
            issue_type: "site_review",
            priority: "haute",
            status: "in_progress",
            assigned_to: "human",
            requested_effect: "review_only",
            description: "Vérifier le sens d’ouverture et la cohérence avec le cheminement d’évacuation.",
            task_contract_ref: "task-contract-cm-01",
            context_pack_ref: "context-pack-cm-securite",
            version: 2,
            updated_at: now,
          },
          comments: [],
          hermes_runs: [],
          events: [{ event_type: "status_changed", actor_kind: "human", occurred_at: now }],
        },
      ],
      documents: [
        {
          card_id: "card-cm-plan-securite",
          document_id: "document-cm-plan-securite",
          title: "Plan sécurité et évacuation",
          parent_project_id: "CM-04",
          source_ref: "fixture://CM-04/CHANTIER/PLAN-SECURITE.pdf",
          source_digest: "sha256:demo-cm-plan",
          media_type: "application/pdf",
          analysis_status: "ready",
          naming: { object_name: "Plan sécurité et évacuation", document_type: "PLAN", phase_code: "CHANTIER", revision_index: "C2", phase_folder: "50_Chantier / Plans" },
          extraction: { chunk_count: 11, converter: "Docling — fixture", converter_version: "demo", finished_at: now, quality_flags: [], error: null },
          authority: { is_source: true, is_evidence: false, is_memory: false },
        },
        {
          card_id: "card-cm-cr",
          document_id: "document-cm-cr",
          title: "Compte rendu de chantier",
          parent_project_id: "CM-04",
          source_ref: "fixture://CM-04/CHANTIER/CR-12.pdf",
          source_digest: "sha256:demo-cm-cr",
          media_type: "application/pdf",
          analysis_status: "partial",
          naming: { object_name: "Compte rendu de chantier", document_type: "CR", phase_code: "CHANTIER", revision_index: "12", phase_folder: "50_Chantier / Comptes rendus" },
          extraction: { chunk_count: 18, converter: "Docling — fixture", converter_version: "demo", finished_at: now, quality_flags: ["photos non interprétées"], error: null },
          authority: { is_source: true, is_evidence: false, is_memory: false },
        },
      ],
      referenceIds: ["reference-lexique-chantier", "reference-accessibilite-erp", "reference-ccag-travaux"],
      evidence: [
        {
          id: "evidence-cm-evacuation",
          title: "Cheminement d’évacuation",
          summary: "Plan sécurité et observation chantier rapprochés.",
          status: "needs_review",
          signal: "Mesure sur site attendue",
        },
      ],
      gates: [
        {
          id: "gate-cm-validation-porte",
          title: "Validation de la porte",
          summary: "La commande définitive dépend du contrôle du passage utile.",
          status: "waiting",
          signal: "Information manquante",
        },
      ],
    },
    {
      id: "demo-villa-1875",
      title: "Villa 1875",
      caseLabel: "Case V1875-02",
      phase: "Diagnostic",
      location: "Normandie",
      summary: "Diagnostic et stratégie d’intervention sur une villa ancienne.",
      status: "open",
      signal: "2 sources à qualifier · 1 risque",
      context: {
        subject: "Qualifier l’état des colombages et les travaux urgents",
        scope: "Diagnostic · observations, prélèvements et priorités",
        risks: "Humidité, attaque biologique, perte de matière",
      },
      workIssues: [
        {
          work_issue: {
            issue_id: "issue-v1875-colombages",
            case_ref: "V1875-02",
            title: "Qualifier les altérations des colombages",
            issue_type: "diagnostic",
            priority: "haute",
            status: "waiting",
            assigned_to: "human",
            requested_effect: "analysis_only",
            description: "Distinguer les constats visibles des hypothèses nécessitant un diagnostic spécialisé.",
            task_contract_ref: "task-contract-v1875-01",
            context_pack_ref: "context-pack-v1875-diagnostic",
            version: 1,
            updated_at: now,
          },
          comments: [],
          hermes_runs: [],
          events: [{ event_type: "issue_created", actor_kind: "human", occurred_at: now }],
        },
      ],
      documents: [
        {
          card_id: "card-v1875-reportage",
          document_id: "document-v1875-reportage",
          title: "Reportage photographique",
          parent_project_id: "V1875-02",
          source_ref: "fixture://V1875/DIAGNOSTIC/PHOTOS.zip",
          source_digest: "sha256:demo-v1875-photos",
          media_type: "application/zip",
          analysis_status: "partial",
          naming: { object_name: "Reportage photographique", document_type: "PHOTOS", phase_code: "DIAG", revision_index: "A1", phase_folder: "10_Conception / Diagnostic" },
          extraction: { chunk_count: 0, converter: "Profil image — fixture", converter_version: "demo", finished_at: now, quality_flags: ["inspection visuelle non exhaustive"], error: null },
          authority: { is_source: true, is_evidence: false, is_memory: false },
        },
      ],
      referenceIds: ["reference-lexique-chantier", "reference-dtu-43-1"],
      evidence: [
        {
          id: "evidence-v1875-humidite",
          title: "Signal d’humidité",
          summary: "Photographies et notes de visite indiquent une zone à investiguer.",
          status: "partial",
          signal: "Hypothèse · diagnostic spécialisé requis",
        },
      ],
      gates: [
        {
          id: "gate-v1875-travaux-urgents",
          title: "Travaux urgents",
          summary: "Aucune prescription définitive avant qualification de la cause.",
          status: "open",
          signal: "Gate de prudence ouvert",
        },
      ],
    },
  ];

  let activeProjectId = projects[0].id;

  function projectModel(project) {
    return {
      id: `project-${project.id}`,
      kind: "project",
      typeLabel: "Projet",
      title: project.title,
      summary: `${project.caseLabel} · ${project.phase} · ${project.location}`,
      status: project.status,
      signal: project.signal,
      context: project.summary,
      event: null,
      attention: project.status === "review" ? "human" : null,
      responsibilities: [
        { icon: "scope", label: `Périmètre : ${project.context.scope}` },
        ...(project.status === "review" ? [{ icon: "decision", label: "Décision humaine attendue", attention: true }] : []),
      ],
      sections: [
        ["Projet", [project.caseLabel, project.summary, `Phase : ${project.phase}`, `Localisation : ${project.location}`]],
        ["Situation active", [project.context.subject, project.context.scope, `Risques : ${project.context.risks}`]],
        ["Navigation", ["Glisser vers le haut pour descendre dans le Deck du projet.", "Glisser horizontalement pour parcourir les cartes sœurs d’un même niveau."]],
      ],
    };
  }

  function contextModels(project) {
    return [
      {
        id: `context-${project.id}`,
        kind: "scope",
        typeLabel: "Situation",
        title: project.context.subject,
        summary: project.context.scope,
        status: "ready",
        signal: `Risques : ${project.context.risks}`,
        context: project.caseLabel,
        responsibilities: [
          { icon: "scope", label: "Périmètre actif" },
          { icon: "review", label: "Contexte visible et révisable" },
        ],
        sections: [
          ["Case et Situation", [project.caseLabel, project.context.subject]],
          ["Périmètre", [project.context.scope]],
          ["Risques connus", [project.context.risks]],
          ["Limite", ["Cette carte prépare le contexte. Elle ne constitue ni preuve, ni décision, ni mémoire."]],
        ],
      },
      {
        id: `task-contract-${project.id}`,
        kind: "work",
        typeLabel: "Task Contract",
        title: "Contrat de tâche borné",
        summary: "Sources, résultat attendu et effets autorisés déclarés.",
        status: "ready",
        signal: "Exécution externe seulement",
        context: project.caseLabel,
        responsibilities: [
          { icon: "scope", label: "Périmètre déclaré" },
          { icon: "hermes", label: "Hermes exécute après handoff borné" },
        ],
        sections: [
          ["Fonction", ["Borner le travail, les sources et le résultat candidat attendu."]],
          ["Exécution", ["Pantheon gouverne. Hermes exécute extérieurement. Le cockpit expose."]],
          ["Limite", ["Task Contract ≠ runtime task. Résultat candidat ≠ résultat approuvé."]],
        ],
      },
    ];
  }

  function evidenceModel(item, project) {
    return {
      id: item.id,
      kind: "evidence",
      typeLabel: "Evidence candidate",
      title: item.title,
      summary: item.summary,
      status: item.status,
      signal: item.signal,
      context: project.caseLabel,
      attention: "human",
      responsibilities: [
        { icon: "source", label: "Provenance à examiner" },
        { icon: "review", label: "Suffisance non décidée", attention: true },
      ],
      sections: [
        ["Fonction", [item.summary]],
        ["Statut", [statusLabel(item.status), item.signal]],
        ["Limites", ["Evidence candidate ≠ preuve validée.", "Les contradictions et lacunes restent visibles."]],
      ],
    };
  }

  function gateModel(item, project) {
    return {
      id: item.id,
      kind: "gate",
      typeLabel: "Gate",
      title: item.title,
      summary: item.summary,
      status: item.status,
      signal: item.signal,
      context: project.caseLabel,
      attention: "human",
      responsibilities: [
        { icon: "decision", label: "Décision humaine requise", attention: true },
        { icon: "scope", label: "Effet borné au projet" },
      ],
      sections: [
        ["Seuil", [item.summary]],
        ["État", [statusLabel(item.status), item.signal]],
        ["Limite", ["Gate ≠ Decision. Gate satisfait ≠ action exécutée."]],
      ],
    };
  }

  function traceModels(project) {
    return [
      {
        id: `trace-${project.id}`,
        kind: "history",
        typeLabel: "Trace",
        title: "Activité récente",
        summary: "Événements, versions et retours conservés sans devenir preuve.",
        status: "ready",
        signal: "Trace append-only · démonstration",
        context: project.caseLabel,
        responsibilities: [
          { icon: "history", label: "Historique visible" },
          { icon: "memory", label: "Trace ≠ mémoire gouvernée" },
        ],
        sections: [
          ["Derniers événements", ["Situation ouverte", "Document analysé", "Revue humaine demandée"]],
          ["Limite", ["Journal présent ≠ Evidence Pack. Trace conservée ≠ Registre Probatoire."]],
        ],
      },
    ];
  }

  function renderSelectableProject(project) {
    const card = renderCard(projectModel(project));
    card.classList.add("project-card");
    card.dataset.selected = String(project.id === activeProjectId);
    const oldButton = card.querySelector(".card-button");
    const button = oldButton.cloneNode(true);
    button.setAttribute("aria-label", `Ouvrir l’espace projet : ${project.title}`);
    button.setAttribute("aria-pressed", String(project.id === activeProjectId));
    oldButton.replaceWith(button);
    button.addEventListener("click", () => {
      activeProjectId = project.id;
      renderProjectSpace();
      document.getElementById("active-project-heading")?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
    return card;
  }

  function renderLevel({ title, eyebrow, description, models }) {
    const level = document.createElement("section");
    level.className = "hierarchy-level";

    const heading = document.createElement("header");
    heading.className = "level-heading";
    const copy = document.createElement("div");
    const label = document.createElement("p");
    label.className = "eyebrow";
    label.textContent = eyebrow;
    const h2 = document.createElement("h2");
    h2.textContent = title;
    const support = document.createElement("p");
    support.className = "level-description";
    support.textContent = description;
    copy.append(label, h2, support);
    const count = document.createElement("span");
    count.className = "level-count";
    count.textContent = `${models.length} carte${models.length > 1 ? "s" : ""}`;
    heading.append(copy, count);

    const rail = document.createElement("div");
    rail.className = "hierarchy-rail";
    for (const model of models) rail.append(renderCard(model));

    level.append(heading, rail);
    return level;
  }

  function populateResourceProfiles(project) {
    state.resourceProfiles = {
      documents: new Map(project.documents.map(item => [item.document_id, {
        document_id: item.document_id,
        format: {
          family: item.media_type === "application/pdf" ? "pdf" : item.media_type?.startsWith("image/") ? "image" : "archive",
          extension: item.media_type === "application/pdf" ? "pdf" : "zip",
          media_type: item.media_type,
        },
        content: {
          composition: item.media_type === "application/pdf" ? "structured_text" : "images_only",
          has_text: item.media_type === "application/pdf",
          has_images: item.media_type !== "application/pdf",
          has_tables: item.title.includes("CCTP") || item.title.includes("CCAP"),
          observed_table_items: item.title.includes("CCTP") ? 4 : 0,
        },
      }])),
      knowledgeSites: new Map(),
      crawlCapability: { status: "not_authorized", network_requests: 0 },
    };
  }

  function renderProjectSpace() {
    const project = projects.find(item => item.id === activeProjectId) || projects[0];
    state.project = project.id;
    state.token = "";
    state.documents = project.documents;
    state.workIssues = project.workIssues;
    state.knowledge = references.filter(item => project.referenceIds.includes(item.knowledge_id));
    populateResourceProfiles(project);

    const selector = document.getElementById("project-deck");
    selector.replaceChildren(...projects.map(renderSelectableProject));

    document.getElementById("active-project-heading").textContent = project.title;
    document.getElementById("active-project-meta").textContent = `${project.caseLabel} · ${project.phase} · ${project.location}`;
    document.getElementById("active-project-summary").textContent = project.summary;

    const hierarchy = document.getElementById("project-hierarchy");
    hierarchy.replaceChildren(
      renderLevel({
        eyebrow: "NIVEAU 01 · CASE",
        title: "Situation et périmètre",
        description: "Ce qui cadre le dossier avant tout travail ou toute preuve.",
        models: contextModels(project),
      }),
      renderLevel({
        eyebrow: "NIVEAU 02 · WORK",
        title: "Travail en cours",
        description: "Traitements, revues et résultats candidats à examiner.",
        models: project.workIssues.map(workIssueModel),
      }),
      renderLevel({
        eyebrow: "NIVEAU 03 · ASSETS",
        title: "Documents du projet",
        description: "Sources propres au dossier. Une carte document n’est pas la source elle-même.",
        models: project.documents.map(documentModel),
      }),
      renderLevel({
        eyebrow: "NIVEAU 04 · REFERENCE",
        title: "Références mobilisées",
        description: "Knowledge globale liée au projet sans devenir vérité propre au projet.",
        models: references
          .filter(item => project.referenceIds.includes(item.knowledge_id))
          .map(item => knowledgeModel({ ...item, parent_project_id: `Référence globale · mobilisée pour ${project.caseLabel}` })),
      }),
      renderLevel({
        eyebrow: "NIVEAU 05 · EVIDENCE",
        title: "Evidence candidates",
        description: "Supports et contradictions sélectionnés pour une revue déterminée.",
        models: project.evidence.map(item => evidenceModel(item, project)),
      }),
      renderLevel({
        eyebrow: "NIVEAU 06 · DECISION",
        title: "Gates et décisions",
        description: "Seuils ouverts avant toute conséquence ou diffusion.",
        models: project.gates.map(item => gateModel(item, project)),
      }),
      renderLevel({
        eyebrow: "NIVEAU 07 · TRACE",
        title: "Trace gouvernée",
        description: "Ce qui s’est produit et ce qui a été conservé, sans confusion avec la preuve.",
        models: traceModels(project),
      }),
    );
  }

  function renderReferenceSpace() {
    const deck = document.getElementById("reference-deck");
    deck.replaceChildren(...references.map(item => renderCard(knowledgeModel({ ...item, parent_project_id: "Espace de référence global" }))));
  }

  function showMode(mode) {
    const projectSpace = document.getElementById("project-space");
    const referenceSpace = document.getElementById("reference-space");
    const isProjects = mode === "projects";
    projectSpace.hidden = !isProjects;
    referenceSpace.hidden = isProjects;
    document.querySelectorAll("[data-demo-mode]").forEach(button => {
      const active = button.dataset.demoMode === mode;
      button.classList.toggle("is-active", active);
      button.setAttribute("aria-pressed", String(active));
    });
    if (!isProjects) renderReferenceSpace();
  }

  document.querySelectorAll("[data-demo-mode]").forEach(button => {
    button.addEventListener("click", () => showMode(button.dataset.demoMode));
  });

  const projectInput = document.getElementById("project");
  const tokenInput = document.getElementById("token");
  const loadButton = document.getElementById("load");
  if (projectInput) projectInput.value = activeProjectId;
  if (tokenInput) tokenInput.value = "";
  if (loadButton) loadButton.disabled = true;

  const network = document.getElementById("network");
  if (network) network.textContent = "démo · réseau bloqué";

  renderProjectSpace();
  renderReferenceSpace();
  showMode("projects");
})();
