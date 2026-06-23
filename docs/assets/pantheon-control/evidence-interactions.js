// Swiper wiring, navigation between cards, overlays and the candidate-intent
// toast. State lives here; markup comes from evidence-render.js.

let evidenceProjects = [];
let pSw, sSw = [];
let selected = { p: 0, id: null };
let toastTimer, downPt, dragging = false;

function evidenceFind(id) {
  for (let pi = 0; pi < evidenceProjects.length; pi++) {
    const ci = evidenceProjects[pi].cards.findIndex(c => c.id === id);
    if (ci >= 0) return { pi, ci, c: evidenceProjects[pi].cards[ci] };
  }
}

function evidenceSetHead() {
  const p = evidenceProjects[selected.p];
  barProject.textContent = p.name;
  barPhase.textContent = 'Phase · ' + p.phase + ' · ' + p.cards.length + ' fiches';
}

function evidenceGoto(id) {
  const f = evidenceFind(id);
  if (!f) { evidenceToast('Fiche liée absente : ' + (id || '—')); return; }
  selected = { p: f.pi, id };
  pSw.slideTo(f.pi);
  evidenceSetHead();
  setTimeout(() => sSw[f.pi]?.slideTo(f.ci), 40);
  evidenceCloseOv();
}

function evidenceOpenOv(pi, id) {
  selected = { p: +pi, id };
  evidenceSetHead();
  evidenceRenderOv();
  ov.classList.add('open');
}

function evidenceCloseOv() {
  ov.classList.remove('open');
}

function evidenceRenderOv() {
  const p = evidenceProjects[selected.p];
  ovTitle.textContent = p.name + ' · ' + p.phase;
  ovSub.textContent = 'Vue registre · ' + selected.id;
  ovGrid.innerHTML = p.cards.map(c => evidenceMiniCard(c, evidenceRelClass(c, selected, evidenceProjects))).join('');
}

function evidenceOpenAdd() {
  const p = evidenceProjects[selected.p];
  panelTitle.textContent = 'Nouvelle fiche candidate';
  panelBody.innerHTML =
    '<section class="sec"><h4>Projet / phase</h4><p>' + escEv(p.name) + ' · ' + escEv(p.phase) + '</p></section>' +
    '<section class="sec"><h4>Champs minimaux</h4>' +
    '<div class="line"><b>Titre</b><span>Nom court du point de contrôle</span></div>' +
    '<div class="line"><b>Source</b><span>Mail, PDF, MD, plan ou extraction à rattacher</span></div>' +
    '<div class="line"><b>Statut</b><span>À qualifier, à vérifier, contradictoire, bloquant</span></div>' +
    '<div class="line"><b>Décideur</b><span>Architecte, client, BET, mairie, entreprise, assureur</span></div></section>' +
    '<section class="sec"><h4>Limite</h4><p>Création candidate uniquement. Aucun registre n’est modifié.</p>' +
    '<button data-a="candidate">Préparer candidate</button></section>';
  panel.classList.add('open');
}

function evidenceOpenPanel(a, id) {
  const f = evidenceFind(id), c = f?.c;
  panelTitle.textContent = a === 'more' ? 'Recherche complémentaire' : 'Fiche de revue';
  panelBody.innerHTML = a === 'more'
    ? '<section class="sec"><h4>Manques ciblés</h4><div class="line"><b>Manque</b><span>' + escEv(c.miss) + '</span></div>' +
      '<div class="line"><b>Décision</b><span>' + escEv(c.dec) + '</span></div></section>' +
      '<section class="sec"><h4>Workflow</h4><p>Base projet → courriels → corpus technique → sources contrôlées → Evidence Candidate + Evidence Pack Candidate.</p></section>'
    : '<section class="sec"><h4>Modification candidate</h4><p>Préparer une correction de fiche sans modifier le registre.</p></section>';
  panel.classList.add('open');
}

function evidenceClosePanel() { panel.classList.remove('open'); }
function evidenceToggleInfo() { inf.classList.toggle('open'); }

function evidenceToast(s) {
  to.textContent = s;
  to.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => to.classList.remove('show'), 2200);
}

function evidenceBind() {
  document.addEventListener('pointerdown', e => { downPt = { x: e.clientX, y: e.clientY }; dragging = false; });
  document.addEventListener('pointermove', e => {
    if (downPt && Math.hypot(e.clientX - downPt.x, e.clientY - downPt.y) > 12) dragging = true;
  });
  document.addEventListener('click', e => {
    const c = e.target.closest('.card');
    if (c && !dragging && !e.target.closest('button,input')) evidenceOpenOv(c.dataset.p, c.dataset.id);

    if (e.target.dataset.mini) {
      if (e.target.dataset.mini === selected.id) {
        const i = evidenceProjects[selected.p].cards.findIndex(c => c.id === selected.id);
        sSw[selected.p]?.slideTo(i);
        evidenceCloseOv();
      } else {
        selected.id = e.target.dataset.mini;
        evidenceRenderOv();
        const i = evidenceProjects[selected.p].cards.findIndex(c => c.id === selected.id);
        sSw[selected.p]?.slideTo(i);
      }
    }
    if (e.target.dataset.goto) evidenceGoto(e.target.dataset.goto);
    if (e.target.dataset.close) { evidenceClosePanel(); evidenceCloseOv(); }
    if (e.target.dataset.a) {
      evidenceToast('Pantheon · intention candidate : ' + e.target.dataset.a);
      if (['mod', 'more'].includes(e.target.dataset.a)) evidenceOpenPanel(e.target.dataset.a, e.target.dataset.id);
    }
  });
}

function evidenceInitSwiper() {
  sSw = [...document.querySelectorAll('.sSw')].map(s => new Swiper(s, {
    direction: 'vertical', slidesPerView: 1, spaceBetween: 8, nested: true, threshold: 8, touchAngle: 35,
  }));
  pSw = new Swiper('.pSw', {
    direction: 'horizontal', slidesPerView: 1, spaceBetween: 8, threshold: 8, touchAngle: 35,
    on: {
      slideChange() {
        selected.p = this.activeIndex;
        selected.id = evidenceProjects[selected.p].cards[0].id;
        evidenceSetHead();
      },
    },
  });
  evidenceSetHead();
}

async function evidenceRender() {
  evidenceProjects = await loadEvidenceProjects();
  selected.id = evidenceProjects[0].cards[0].id;
  mountPage('Preuves & statuts', '', tpl.innerHTML.replace('__PROJECTS__', evidenceRenderProjects(evidenceProjects)));
  evidenceBind();
  evidenceInitSwiper();
}