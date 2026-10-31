# Connecteurs recommandés — protocole produit 1paR'1 (Printful → Shopify)

Recherche faite le 2026-10-31 dans le registre de connecteurs.

| Besoin du protocole | Connecteur | État | Usage |
|---|---|---|---|
| Boutique, produits, variantes, prix, statut, collections | **Shopify** | Connecté | Audit automatique des produits (statut, prix, variantes, tags, images) et publication (DRAFT → ACTIVE) |
| Suppression d'arrière-plan, redimensionnement du logo | **Canva** (`remove-background`, `resize-design`, `export-design`) | Disponible | Étape « logo » : fond transparent, export PNG, taille |
| Automatiser Printful ↔ Shopify, alertes | **Zapier** | Disponible | Printful a une app Zapier : déclencher une tâche/alerte à chaque nouveau produit synchronisé |
| Suivi d'équipe (cases à cocher partagées) | **Notion** ou **monday.com** | Disponibles | Une base « Produits » avec une propriété case à cocher par étape |
| Tableur de suivi | **Google Sheets** | Disponible | Export du tableau de suivi |
| Printful (catalogue, mockups, placements) | Aucun connecteur dédié trouvé | — | Utiliser l'app Printful native dans Shopify ; les réglages (placement, width/height) restent à saisir dans l'éditeur Printful |
| Autres gestionnaires de tâches | Trello, Todoist, MeisterTask | Non installés | Alternatives si l'équipe les utilise déjà |

**Limite connue :** Shopify ne sait pas si une broderie est sur la poitrine ou la manche, ni la taille du logo. Ces cases se cochent à la main dans `protocole-produit.html`.
