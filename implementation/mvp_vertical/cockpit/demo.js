(() => {
  if (!window.PANTHEON_COCKPIT_DEMO) return;

  const now = new Date().toISOString();
  const projectId = "demo-maison-normande";

  state.project = projectId;
  state.token = "";
  state.scene = "now";
  state.documents = [
    {
      card_id: "card-demo-document-001",
      document_id: "document-demo-001",
      title: "CCTP — Revêtements de sol",
      parent_project_id: projectId,
      source_ref: "fixture://documents/cctp-revetements.pdf",
      source_digest: "sha256:demo-document-source",
      media_type: "application/pdf",
      analysis_status: "partial",
      naming: {
        object_name: "CCTP — Revêtements de sol",
        document_type: "CCTP",
        phase_code: "DCE",
        revision_index: "A",
        phase_folder: "DCE / Pièces écrites",
      },
      extraction: {
        chunk_count: 42,
        converter: "Docling — fixture",
        converter_version: "demo",
        finished_at: now,
        quality_flags: ["tableaux à relire", "références produits à confirmer"],
        error: null,
      },
      authority: {
        is_source: true,
        is_evidence: false,
        is_memory: false,
      },
    },
  ];

  state.knowledge = [
    {
      card_id: "card-demo-knowledge-001",
      knowledge_id: "knowledge-demo-001",
      parent_project_id: projectId,
      title: "Synthèse candidate — prescriptions de revêtements",
      family: "prescription technique",
      version: 3,
      review_status: "generated_unreviewed",
      source_chunk_refs: ["chunk-004", "chunk-011", "chunk-019"],
      document_ref: "document-demo-001",
      markdown_digest: "sha256:demo-knowledge-markdown",
      created_by: "Hermes — résultat candidat fictif",
      created_at: now,
      updated_at: now,
    },
  ];

  state.workIssues = [
    {
      work_issue: {
        issue_id: "issue-demo-001",
        case_ref: projectId,
        title: "Vérifier les limites de prestation du lot revêtements",
        issue_type: "review",
        priority: "haute",
        status: "review",
        assigned_to: "human",
        requested_effect: "review_only",
        description: "Comparer la synthèse candidate au CCTP source et confirmer les points restant à arbitrer avant émission.",
        task_contract_ref: "task-contract-demo-001",
        context_pack_ref: "context-pack-demo-001",
        version: 2,
        updated_at: now,
      },
      comments: [
        {
          author: "Équipe projet",
          body: "Confirmer l’adaptation au plancher chauffant et la classe d’usage du parquet.",
        },
      ],
      hermes_runs: [
        {
          run_id: "run-demo-001",
          status: "done",
          normalized_return: {
            outcome: "candidate_return",
            summary: "Synthèse préparée ; deux réserves techniques restent ouvertes.",
          },
        },
      ],
      events: [
        {
          event_type: "review_requested",
          actor_kind: "system",
          occurred_at: now,
        },
      ],
    },
  ];

  state.resourceProfiles = {
    documents: new Map([
      [
        "document-demo-001",
        {
          document_id: "document-demo-001",
          format: {
            family: "pdf",
            extension: "pdf",
            media_type: "application/pdf",
          },
          content: {
            composition: "structured_text",
            has_text: true,
            has_images: false,
            has_tables: true,
            observed_table_items: 4,
          },
        },
      ],
    ]),
    knowledgeSites: new Map([
      [
        "knowledge-demo-001",
        [
          {
            url: "https://example.invalid/reglement-technique",
            host: "example.invalid",
            site_kind: "public_information_portal",
          },
        ],
      ],
    ]),
    crawlCapability: {
      status: "not_authorized",
      network_requests: 0,
    },
  };

  const project = $("project");
  const token = $("token");
  const load = $("load");
  if (project) project.value = projectId;
  if (token) token.value = "";
  if (load) load.disabled = true;

  const enforceDemoNetworkLabel = () => {
    const output = $("network");
    if (output) output.textContent = "démo · réseau bloqué";
  };
  window.addEventListener("online", enforceDemoNetworkLabel);
  window.addEventListener("offline", enforceDemoNetworkLabel);
  enforceDemoNetworkLabel();

  render();
  $("scene-status").textContent = `${currentModels().length} carte(s) fictive(s) · aucun appel API · aucun effet persistant.`;
})();
