# Connecteurs recommandés — automatiser le protocole produit

Boutique : 1par1.fr (Shopify, EUR). Produits fabriqués à la demande via Printful.

| Besoin | Connecteur | Statut dans cette session | Rôle |
|---|---|---|---|
| Lire/mettre à jour les produits (statut, variantes, prix, médias, SEO, collections) | [Shopify](https://1par1.fr/admin) | ✅ connecté | Source de vérité de l'audit (cases « auto ») |
| Suivi d'équipe visible par tous (cases, assignations, historique) | [monday.com](https://monday.com) ou [Notion](https://www.notion.so) | ✅ disponibles | Un tableau « 1 produit = 1 ligne, 1 colonne = 1 étape » |
| Supprimer l'arrière-plan, redimensionner, exporter le logo en PNG | [Canva](https://www.canva.com/features/background-remover/) | ✅ disponible | Étape 5 |
| Relier Printful ↔ autres outils (alerte à chaque produit synchronisé, commande test) | [Zapier](https://zapier.com/apps/printful/integrations) | ✅ disponible | Étapes 1, 4, 6, 9 (Printful n'a pas de connecteur MCP direct) |
| Tableur partagé / export de l'audit | [Google Sheets](https://sheets.google.com) | ✅ disponible | Alternative légère |
| Alertes de revue | **Gmail / Google Calendar** | ✅ disponibles | Rappel hebdomadaire |

**Limite importante** : [Printful](https://www.printful.com/dashboard/sync) n'est pas lisible directement ici. Les réglages de zones (poitrine, dos, manches, poignets) et de taille du logo (width/height) restent des cases **manuelles**, jamais cochées automatiquement. Un déclencheur Zapier « Printful – nouveau produit synchronisé » permet d'ouvrir automatiquement une ligne de suivi.

## Mise à jour régulière
Relancer l'audit Shopify (tâche planifiée) : il réécrit `data/audit.json` ; `protocole-produit.html` affiche l'état.
