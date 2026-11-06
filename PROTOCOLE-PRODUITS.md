# Protocole de création de produits — Printful → Shopify (1paR'1)

Dernière mise à jour : 2026-11-06 · Boutique : 1par1.fr (Shopify Basic, EUR)

Règle d'or : **aucune étape n'est cochée sans validation. On ne passe pas à l'étape suivante tant que la précédente n'est pas validée.**
Statuts produit : `BROUILLON` → `VALIDÉ (revue)` → `PUBLIÉ (ACTIVE)`.

## 1. Connecteurs recommandés

| Besoin | Connecteur | Rôle |
|---|---|---|
| Catalogue / fulfilment | **Printful ↔ Shopify** (app native) | Synchroniser produits, variantes, SKU, mockups |
| Boutique | **Shopify** (MCP connecté) | Audit statut, prix, variantes, publication |
| Visuels / logo | **Canva** (MCP connecté : remove-background, resize, export) | Suppression d'arrière-plan, mise à taille, export PNG transparent |
| Suivi d'équipe | **monday.com** (MCP connecté) ou **Notion** | Tableau de suivi, une ligne = un produit, une colonne = une étape |
| Automatisation | **Zapier** (MCP connecté) | Ex. : produit passe en « Validé » → notification équipe ; nouveau produit Shopify → ligne de suivi créée |
| Partage / archives | **Google Sheets / Drive** | Export de la checklist, mockups validés |
| Alertes | **Gmail** | Résumé hebdomadaire de l'audit |

Priorité de mise en place : 1) Printful↔Shopify, 2) monday.com (tableau de suivi), 3) Zapier (notifications), 4) Canva (visuels).

## 2. Checklist étape par étape (à valider produit par produit)

### Phase A — Choix du produit (Printful)
- [ ] A1. Produit de base choisi (ex. Unisex Premium Pullover Hoodie) — fiche Printful vérifiée
- [ ] A2. Couleur(s) retenue(s)
- [ ] A3. Tailles retenues (S, M, L, XL, 2XL…) et guide des tailles ajouté
- [ ] A4. Coût de revient Printful relevé (produit + impression/broderie + livraison)
- [ ] A5. **Prix de vente** fixé (marge ≥ objectif, TVA incluse, prix identique sur toutes les variantes sauf surcoût de taille voulu)

### Phase B — Technique de marquage
- [ ] B1. Méthode choisie : broderie ou impression (DTG)
- [ ] B2. Emplacement poitrine (gauche/droite/centre) défini
- [ ] B3. Emplacement dos défini (si besoin)
- [ ] B4. Manche droite / manche gauche (si besoin)
- [ ] B5. Poignet droit / poignet gauche (si besoin)
- [ ] B6. Limites broderie respectées (nombre de couleurs, finesse des détails, taille maxi de la zone)

### Phase C — Fichier logo / design
- [ ] C1. Fichier source haute définition (PNG/SVG)
- [ ] C2. Suppression de l'arrière-plan (si besoin) — PNG transparent contrôlé sur fond clair ET foncé
- [ ] C3. Taille du logo réglée : width = ___ · height = ___ (ratio conservé)
- [ ] C4. Position réglée (X/Y, centrage, distance au col/couture)
- [ ] C5. Résolution / DPI conforme aux exigences Printful
- [ ] C6. Contraste du logo vérifié sur chaque couleur de produit

### Phase D — Variantes & mockups
- [ ] D1. Toutes les variantes (taille × couleur) créées, SKU renseignés
- [ ] D2. Prix cohérent sur toutes les variantes
- [ ] D3. Mockups générés (face, dos, manches si concerné) et contrôlés
- [ ] D4. Image principale = face, ordre des images validé

### Phase E — Fiche Shopify
- [ ] E1. Titre clair et uniforme (ex. « Sweat à Capuche Unisexe — Noir »)
- [ ] E2. Description rédigée, cohérente avec la technique réelle (broderie vs impression)
- [ ] E3. Type de produit, vendeur (« 1paR'1 » — une seule orthographe), tags, collection
- [ ] E4. SEO (titre, méta-description, handle)
- [ ] E5. Poids / pays d'origine / livraison configurés
- [ ] E6. Commande test passée et suivie jusqu'à Printful

### Phase F — Validation & publication
- [ ] F1. **Revue croisée par une 2ᵉ personne** (toutes les cases A–E cochées)
- [ ] F2. Statut passé de Brouillon à Actif
- [ ] F3. Produit visible en boutique, ajouté à la collection vitrine
- [ ] F4. Contrôle post-publication (prix, variantes, images, panier)

## 3. Audit des produits de la boutique — 2026-11-06

Source : Shopify (5 produits). Les cases B/C/D ne sont pas lisibles via Shopify (réglages Printful) : elles restent à vérifier dans Printful par l'équipe.

| Produit | Statut Shopify | Prix | Variantes | Tags | A | B | C | D | E | F | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Unisex Hoodie Blanc (`unisex-hoodie`) | ARCHIVÉ | 69,90 € | 5 tailles | aucun | à vérifier | à vérifier | à vérifier | ✅ SKU + prix homogènes | ⚠️ titre non francisé, pas de tags | ❌ | Archivé — ne pas republier (doublon) |
| Unisex Hoodie (`unisex-hoodie-1`) | ARCHIVÉ | 69,90 € | 5 tailles | broderie, dtg | à vérifier | ⚠️ tags broderie ET dtg | à vérifier | ✅ | ⚠️ titre non francisé | ❌ | Archivé — doublon |
| Sweat à Capuche Unisexe — Noir | BROUILLON | 77,90 € | 5 tailles | broderie, catalogue, dtg | à vérifier | ⚠️ confirmer broderie poitrine + impression dos | à vérifier | ✅ | ✅ titre ; ⚠️ vendeur « 1paR'1 » | ❌ | Candidat principal à valider (F1) |
| Sweat à Capuche blanc Unisexe (`-1`) | ARCHIVÉ | 69,90 € | 5 tailles | aucun | à vérifier | à vérifier | à vérifier | ✅ | ⚠️ vendeur « 1paR1 » (sans apostrophe), description générique | ❌ | Archivé — doublon |
| Sweat à Capuche Unisexe — Blanc | BROUILLON | 69,90 € | 5 tailles | catalogue, dtg | à vérifier | ⚠️ impression seule | à vérifier | ✅ | ✅ titre | ❌ | Candidat à valider (F1) |

Points transverses :
- **Aucun produit n'est actuellement publié (ACTIVE)** : la vitrine est vide de produits vendables.
- Écart de prix Noir (77,90 €) vs Blanc (69,90 €) : valider qu'il correspond bien à la broderie en plus.
- Chaque produit a 5 variantes de taille mais Shopify en compte 6 : vérifier la variante supplémentaire éventuelle.
- Vendeur écrit de 3 façons (« 1paR'1 », « 1paR1 », « 1paR'1 ») : uniformiser.
- Stock affiché 9999 par variante : normal pour du print-on-demand, à ne pas modifier.

## 4. Prochaines actions
1. Valider A–E sur « Noir » et « Blanc » (brouillons), puis revue croisée F1.
2. Publier uniquement après F1 ; laisser les 3 archivés (doublons) tels quels.
3. Créer le tableau de suivi (monday.com ou Notion) avec une colonne par étape A1…F4 et brancher Zapier pour les notifications.
4. Rejouer cet audit chaque semaine (routine planifiée) et mettre à jour ce fichier.
