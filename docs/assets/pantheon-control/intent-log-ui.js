function boolLabel(value) {
  return value ? "yes" : "no";
}

function statusClass(status) {
  return `status-${String(status || "unknown").replace(/_/g, "-")}`;
}

function renderIntentCard(intent) {
  const flags = [
    ["truth", intent.affected_truth_claims],
    ["memory", intent.affected_memory],
    ["external", intent.possible_external_effect],
    ["canonical", intent.possible_canonical_effect]
  ];

  return `
    <article class="intent-card ${statusClass(intent.admissibility_status)}">
      <header>
        <div>
          <p class="eyebrow">${intent.id}</p>
          <h2>${intent.title}</h2>
        </div>
        <span class="status-pill ${statusClass(intent.admissibility_status)}">${intent.admissibility_status}</span>
      </header>

      <dl class="intent-grid">
        <div><dt>Origin runtime</dt><dd>${intent.origin_runtime}</dd></div>
        <div><dt>Origin module</dt><dd>${intent.origin_module}</dd></div>
        <div><dt>Scope</dt><dd>${intent.target_scope}</dd></div>
        <div><dt>Decision owner</dt><dd>${intent.decision_owner}</dd></div>
      </dl>

      <section>
        <h3>Proposed intention</h3>
        <p>${intent.proposed_intention}</p>
      </section>

      <section>
        <h3>Proposed task</h3>
        <p>${intent.proposed_task}</p>
      </section>

      <section class="flag-row" aria-label="consequential flags">
        ${flags.map(([label, value]) => `<span class="flag ${value ? "flag-risk" : ""}">${label}: ${boolLabel(value)}</span>`).join("")}
      </section>

      <section>
        <h3>Evidence required</h3>
        <p>${intent.evidence_required}</p>
      </section>

      <section>
        <h3>Approval requirement</h3>
        <p>${intent.approval_required}</p>
      </section>

      <footer>
        <span>Created ${intent.created_at}</span>
        <span>${intent.trace_refs.join(" · ")}</span>
      </footer>
    </article>
  `;
}

function renderIntentSummary(intents) {
  const counts = intents.reduce((acc, item) => {
    acc[item.admissibility_status] = (acc[item.admissibility_status] || 0) + 1;
    return acc;
  }, {});

  return Object.entries(counts)
    .map(([status, count]) => `<span class="summary-pill ${statusClass(status)}">${status}: ${count}</span>`)
    .join("");
}

function renderIntentLog() {
  const intents = window.PANTHEON_INTENT_LOG || [];
  const summary = document.querySelector("#intent-summary");
  const list = document.querySelector("#intent-list");

  if (!summary || !list) return;

  summary.innerHTML = renderIntentSummary(intents);
  list.innerHTML = intents.map(renderIntentCard).join("");
}

document.addEventListener("DOMContentLoaded", renderIntentLog);
