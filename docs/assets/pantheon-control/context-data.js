/* Pantheon Control — données mock du Contexte de travail proposé.
   Documenté non implémenté. Aucune sélection réelle de KB, aucun appel Hermes. */

const CONTEXT_MODES = [
  {
    id:'rapide',
    label:'Rapide',
    tone:'green',
    usage:'Demande simple, faible enjeu, documents actifs uniquement.',
    includes:['Documents actifs du projet','Identité projet','Derniers fichiers à jour'],
    excludes:['Archives','Anciennes versions','Brouillons IA','Documents à vérifier'],
  },
  {
    id:'prudent',
    label:'Prudent',
    tone:'yellow',
    usage:'Sujet réglementaire, technique, contractuel ou responsabilité.',
    includes:['Documents actifs du projet','Documentation générale pertinente','Références mission / responsabilité','Sources à vérifier visibles avec réserve'],
    excludes:['Archives par défaut','Anciennes versions','Brouillons IA','Documents non relus comme preuve'],
  },
  {
    id:'contentieux',
    label:'Contentieux',
    tone:'red',
    usage:'Assurance, litige, réception, impayé, responsabilité ou chronologie.',
    includes:['Documents actifs','Archives importantes','Communications','Comptes rendus','Décisions passées','Références responsabilité'],
    excludes:['Brouillons IA non relus','Documents sans statut','Généralités non pertinentes'],
  },
];

const WORK_CONTEXT_PROPOSALS = [
  {
    id:'CTX-IT249-001',
    title:'Répondre au mail entreprise — façade / IT249',
    request:'Réponds à ce mail entreprise sur la façade, sans validation technique implicite.',
    detected_project:'FLOQUET',
    confidence:['Projet détecté 82%','blue'],
    request_type:['Réponse entreprise sensible','orange'],
    risk:['Sensible','orange'],
    mode:['Prudent','yellow'],
    included:[
      {label:'Documents actifs FLOQUET', reason:'Le mail concerne un projet identifié et une réponse courante.'},
      {label:'CCTP / DCE actif', reason:'Vérifier le périmètre de conception et les prescriptions connues.'},
      {label:'Avis techniques façade actifs ou candidats', reason:'Le sujet touche au complexe de façade.'},
      {label:'Documentation générale incendie / façade', reason:'Détection IT249, façade, exécution.'},
      {label:'Références mission / responsabilité architecte', reason:'Le mail contient une demande de validation.'},
    ],
    excluded:[
      {label:'Archives projet', reason:'Demande courante ; les anciennes versions risquent de polluer la réponse.'},
      {label:'Plans remplacés', reason:'Versions obsolètes exclues par défaut.'},
      {label:'Brouillons IA et branches refusées', reason:'Productions de travail, pas sources documentaires.'},
      {label:'Documents non relus', reason:'Affichés comme manques ou réserves, pas comme preuve.'},
    ],
    missing:[
      {label:'PV feu / classement', why:'Nécessaire pour éviter une validation technique non justifiée.'},
      {label:'Note technique entreprise', why:'L’entreprise doit justifier son système.'},
      {label:'Détail jonction façade-plancher', why:'Point sensible de propagation incendie.'},
    ],
    why:[
      'Le message contient “valider” et “exécution”.',
      'Le sujet détecté touche façade / IT249.',
      'La demande vient d’une entreprise.',
      'Les justificatifs techniques ne sont pas présents dans le contexte actif.',
      'Le risque principal est une validation technique implicite.'
    ],
    lock:'Le contexte accepté resterait verrouillé pour cette branche de réponse.',
  },
  {
    id:'CTX-SUMMARY-001',
    title:'Résumé projet courant',
    request:'Fais-moi un résumé rapide du projet FLOQUET.',
    detected_project:'FLOQUET',
    confidence:['Projet confirmé','green'],
    request_type:['Synthèse simple','green'],
    risk:['Faible','green'],
    mode:['Rapide','green'],
    included:[
      {label:'Documents actifs FLOQUET', reason:'Résumé courant du projet.'},
      {label:'Identité projet', reason:'Adresse, phase, client, statut.'},
    ],
    excluded:[
      {label:'Archives', reason:'Non nécessaires pour une synthèse courante.'},
      {label:'Documentation générale', reason:'Pas de recherche réglementaire demandée.'},
      {label:'Brouillons IA', reason:'Travail non documentaire.'},
    ],
    missing:[],
    why:[
      'La demande ne contient pas de signal réglementaire ou contentieux.',
      'Le projet est explicitement nommé.',
      'Le besoin est une synthèse courante.'
    ],
    lock:'Le contexte rapide limite la réponse aux documents actifs.',
  },
  {
    id:'CTX-INSURANCE-001',
    title:'Préparer une chronologie assureur',
    request:'Prépare une chronologie factuelle pour mon assureur.',
    detected_project:'CHAMPSAUR',
    confidence:['Projet probable 74%','yellow'],
    request_type:['Assurance / chronologie','red'],
    risk:['Critique','red'],
    mode:['Contentieux','red'],
    included:[
      {label:'Documents actifs CHAMPSAUR', reason:'Base factuelle courante.'},
      {label:'Archives importantes', reason:'Historique nécessaire pour une chronologie.'},
      {label:'Mails et communications', reason:'Dates et demandes formulées.'},
      {label:'CR chantier / RDV / visios', reason:'Séquence factuelle et rappels.'},
      {label:'Décisions et preuves candidates', reason:'Points à qualifier, pas à surinterpréter.'},
    ],
    excluded:[
      {label:'Brouillons IA non relus', reason:'Ne doivent pas devenir des sources.'},
      {label:'Documents sans statut', reason:'À classer avant usage.'},
    ],
    missing:[
      {label:'Contrat de mission', why:'Indispensable pour cadrer le périmètre.'},
      {label:'Dernier état des règlements', why:'Nécessaire si le sujet porte sur honoraires ou impayés.'},
    ],
    why:[
      'La demande mentionne l’assureur.',
      'Le format attendu est une chronologie factuelle.',
      'Le mode Contentieux permet d’inclure les archives importantes, avec étiquettes.'
    ],
    lock:'Le contexte contentieux doit rester explicite et horodaté.',
  },
];
