# Protocole de création de produits Printful → Shopify (1paR'1)

Dernière mise à jour automatique : 2026-11-10 · Boutique : 1par1.fr (EUR)
Légende : ✅ validé (vérifié via Shopify) · ⬜ à faire · 🔎 à contrôler à la main (donnée Printful non lisible depuis Shopify)

## 1. Connecteurs recommandés (par ordre de priorité)

| Rôle | Connecteur | Pourquoi |
|---|---|---|
| Boutique / source de vérité | **Shopify** (déjà connecté) | Lecture produits, statut, prix, variantes, collections ; mise à jour de statut |
| Fabrication / POD | **Printful** (app Shopify native) | Placements broderie/impression, mockups, synchro variantes |
| Automatisation | **Zapier** (déjà connecté) | Déclencher une alerte/ligne de suivi à chaque nouveau produit ou changement de statut Shopify |
| Suivi d'équipe (cases à cocher) | **Notion** ou **monday.com** (déjà connectés) ou Google Sheets | Tableau partagé, une ligne par produit, une colonne par étape |
| Visuels / logo | **Canva** (déjà connecté : suppression d'arrière-plan, redimensionnement) | Préparer le logo (fond transparent, dimensions) avant import Printful |
| Notifications | **Gmail** / Slack | Prévenir l'équipe quand une étape est bloquée |

Recommandation : Shopify + Printful (production), Zapier (automatisation), **un seul** outil de suivi (Notion ou Sheets) pour éviter la dispersion.

## 2. Protocole étape par étape (chaque étape doit être validée avant la suivante)

1. **Produit Printful** (modèle, couleur, fournisseur)
2. **Tailles** (S → 2XL, etc.) et variantes de couleur
3. **Prix** (coût Printful + marge ; prix de vente cohérent entre variantes)
4. **Technique** : broderie ou impression (DTG)
5. **Placement poitrine** (gauche/droite/centre)
6. **Placement dos**
7. **Manche droite / manche gauche**
8. **Poignet droit / poignet gauche**
9. **Suppression de l'arrière-plan** du logo (si besoin, fond transparent PNG)
10. **Taille du logo** : width / height / position / résolution (réglages Printful)
11. **Variantes** : toutes créées, SKU présents, visuels par couleur
12. **Mockups & description** (titre, texte, type de produit, tags, images)
13. **Brouillon Shopify** relu (contrôle qualité équipe, commande test)
14. **Validation finale** par un second membre de l'équipe
15. **Publication** (statut ACTIF + canal Boutique en ligne + collection)

## 3. Suivi des produits actuels (audit Shopify du 2026-11-10)

Constat : **aucun produit n'est actif** sur la vitrine (3 archivés, 2 brouillons).

| Produit | Statut Shopify | 1-2 Produit/Tailles | 3 Prix | 4 Technique | 5-8 Placements | 9-10 Logo | 11 Variantes/SKU | 12 Fiche (desc./tags) | 13-14 Validation | 15 Publié |
|---|---|---|---|---|---|---|---|---|---|---|
| Sweat à Capuche Unisexe — Noir (`sweat-a-capuche-unisexe`) | Brouillon | ✅ | ✅ 69,90 € | ✅ broderie + DTG (tags) | 🔎 | 🔎 | ✅ S–2XL, SKU | ✅ tags / ⬜ vérifier texte | ⬜ | ⬜ |
| Sweat à Capuche Unisexe — Blanc (`sweat-a-capuche-unisexe-2`) | Brouillon | ✅ | ✅ 69,90 € | ✅ DTG (tag) | 🔎 | 🔎 | ✅ S–2XL, SKU | ✅ | ⬜ | ⬜ |
| Unisex Hoodie (`unisex-hoodie-1`) | Archivé | ✅ | ✅ 69,90 € | ✅ broderie + DTG | 🔎 | 🔎 | ✅ | ⬜ titre anglais | ⬜ | ⬜ (archivé) |
| Unisex Hoodie Blanc (`unisex-hoodie`) | Archivé | ✅ | ✅ 69,90 € | ⬜ aucun tag | 🔎 | 🔎 | ✅ | ⬜ titre anglais, aucun tag | ⬜ | ⬜ (archivé) |
| Sweat à Capuche blanc Unisexe (`sweat-a-capuche-unisexe-1`) | Archivé | ✅ | ✅ 69,90 € | ⬜ aucun tag | 🔎 | 🔎 | ✅ | ⬜ aucun tag, vendor « 1paR1 » (sans apostrophe) | ⬜ | ⬜ (archivé) |

### Anomalies relevées
- Les 5 produits annoncent 6 variantes mais seules 5 tailles (S–2XL) sont listées : vérifier la 6ᵉ variante dans Shopify/Printful.
- Vendeur incohérent : « 1paR'1 » vs « 1paR1 » (espace/apostrophe) → à harmoniser.
- Deux brouillons (Noir, Blanc) sont les candidats à publier : il reste placements/logo à contrôler dans Printful, puis validation équipe.
- Doublons probables entre produits archivés et brouillons (noir/blanc) : décider lesquels supprimer définitivement.
- Les placements (poitrine/dos/manches/poignets) et dimensions du logo ne sont pas lisibles depuis Shopify : à cocher manuellement depuis l'éditeur Printful.

## 4. Mise à jour régulière
Relancer l'audit (routine planifiée) : relire les produits Shopify, cocher les cases vérifiables, signaler tout produit publié qui ne remplit pas les étapes 1–14.
