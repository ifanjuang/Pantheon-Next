/* Pantheon Control — connexions externes, accès sécurisés et instances locales.
   Documenté non implémenté. Aucune clé, aucun compte, aucun accès et aucune instance réelle ne sont modifiés. */

const EXTERNAL_CONNECTIONS = [
  {nom:'Claude (Anthropic)', type:'Compte IA cloud', etat:['Connecté','green'], identite:'Compte API', usage:'Raisonnement et rédaction longue. Toute utilisation reste cadrée par mission, coût et périmètre.'},
  {nom:'ChatGPT (OpenAI)', type:'Compte IA cloud', etat:['Non connecté','muted'], identite:'Clé API à configurer', usage:'IA polyvalente. Connexion externe soumise à configuration, coût et autorisation.'},
  {nom:'Gemini (Google)', type:'Compte IA cloud', etat:['Non connecté','muted'], identite:'Compte Google / API', usage:'Modèles multimodaux et grand contexte. Connexion externe à cadrer.'},
  {nom:'Mistral', type:'Compte IA cloud', etat:['Non connecté','muted'], identite:'Clé API à configurer', usage:'Modèles cloud européens. Connexion externe à cadrer.'},
  {nom:'Google Workspace', type:'Connecteur externe', etat:['À vérifier','yellow'], identite:'OAuth / compte agence', usage:'Gmail, Drive, Calendar. Accès externe soumis à scope, preuve et approval.'},
  {nom:'Notion', type:'Connecteur externe', etat:['Connecté','green'], identite:'Workspace Pantheon Next', usage:'Pilotage Kanban. Ne remplace pas le repo canonique.'},
  {nom:'GitHub', type:'Connecteur externe', etat:['Connecté','green'], identite:'Repo Pantheon-Next', usage:'Source canonique du dépôt, issues, PR et fichiers.'},
];

const ACCESS_CONNECTIONS = [
  {nom:'Accès privé sécurisé', type:'Accès distant privé', etat:['Candidate','blue'], identite:'VPN, Zero Trust, tunnel ou équivalent', usage:'Permettre un accès distant sans exposition publique directe. Le mécanisme exact reste à choisir selon sécurité, maintenance et coûts.'},
  {nom:'Passerelle d’accès', type:'Frontière réseau', etat:['Candidate','blue'], identite:'Reverse proxy, gateway, tunnel managé ou appliance sécurisée', usage:'Router une demande vers un service interne. Doit imposer authentification, TLS, scope, logs et révocation.'},
  {nom:'Route sous-domaine', type:'Routage externe', etat:['Candidate','blue'], identite:'Sous-domaine dédié, par exemple sur le domaine agence', usage:'Point d’entrée lisible vers une passerelle. Ne doit exposer que les vues explicitement autorisées.'},
  {nom:'Stockage local / NAS', type:'Ressource locale éventuelle', etat:['À vérifier','yellow'], identite:'NAS, serveur fichiers ou stockage équivalent', usage:'Stockage, sauvegarde ou support de fichiers. Ne devient pas source canonique sans statut documentaire.'},
  {nom:'Accès direct public', type:'Exposition directe', etat:['Déconseillé','red'], identite:'Port ouvert ou service publié sans passerelle', usage:'À éviter par défaut. Si nécessaire, nécessite justification, durcissement, logs, authentification forte et décision humaine.'},
];

const LOCAL_INSTANCES = [
  {nom:'Instance locale IA — Poste GPU principal', machine:'Atelier-01', service:'Ollama ou runtime équivalent', port:'11434', etat:['En ligne','green'], modeles:['qwen2.5:14b','qwen2.5-coder:14b','llava:13b'], usage:'Instance locale GPU. Les modèles tournent sur la machine, pas dans Pantheon.'},
  {nom:'Instance locale embeddings / recherche', machine:'Atelier-02', service:'Ollama ou runtime équivalent', port:'11434', etat:['En ligne','green'], modeles:['bge-m3','nomic-embed-text'], usage:'Instance locale orientée embeddings ou recherche. À traiter comme capacité locale.'},
  {nom:'Instance locale ponctuelle', machine:'Portable-Archi', service:'Ollama ou runtime équivalent', port:'11434', etat:['Éteint','muted'], modeles:['llama-guard'], usage:'Instance locale disponible seulement si la machine est réveillée et autorisée.'},
];
