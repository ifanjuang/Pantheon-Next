// Loads the points-de-controle card data. Static fixture today; same shape
// a future read-only Pantheon endpoint could serve.
const EVIDENCE_DATA_URL = 'evidence_data.json';

async function loadEvidenceProjects() {
  const res = await fetch(EVIDENCE_DATA_URL);
  if (!res.ok) throw new Error('evidence_data.json unreachable: ' + res.status);
  const data = await res.json();
  return data.projects;
}
