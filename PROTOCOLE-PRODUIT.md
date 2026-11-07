# Protocole de création produit — Printful → Shopify (1paR'1)

> Dernière mise à jour : **2026-11-07** (audit automatique de la boutique `1par1.fr`)
> Règle d'or : **aucune étape n'est sautée.** On ne passe à l'étape suivante qu'après avoir coché la précédente.
> Légende : ✅ validé · ❌ à corriger · ➖ non applicable · 🔎 non vérifiable automatiquement (à contrôler dans Printful)

---

## 1. Connecteurs recommandés (automatisation)

| Priorité | Connecteur | Rôle dans le protocole | État |
|---|---|---|---|
| 1 | **Shopify** (MCP) | Lecture de tous les produits, prix, variantes, médias, SEO, collections, publication ; écriture (passage Brouillon → Actif, correction alt/SEO). Source de vérité pour cocher les cases. | ✅ connecté |
| 2 | **Printful ↔ Shopify** (app native) | Création du produit (placement, taille logo, variantes), synchronisation des SKU et des coûts. Pas de connecteur MCP Printful disponible : les étapes 2–6 se font dans l'éditeur Printful. | à utiliser |
| 3 | **Canva** | Suppression d'arrière-plan du logo (`remove-background`), redimensionnement, export PNG transparent pour Printful, visuels annexes. | ✅ connecté |
| 4 | **Notion** *ou* **monday.com** | Tableau de suivi partagé par l'équipe : 1 ligne = 1 produit, 1 colonne case à cocher = 1 étape. Vue « Kanban » par étape. | ✅ connectés (choisir un seul) |
| 5 | **Zapier** | Automatisations : nouveau produit Shopify → ligne créée dans Notion/monday ; passage en Actif → notification à l'équipe. | ✅ connecté |
| 6 | **Google Sheets** | Alternative légère au tableau de suivi (export de l'audit ci-dessous). | ✅ connecté |

**Recommandation** : Shopify (vérité) + Canva (visuels) + **Notion** (tableau d'équipe, cases à cocher) + Zapier (pont automatique). Cette routine met à jour le présent fichier ; le même contenu peut être reflété dans Notion.

---

## 2. Protocole étape par étape (modèle à dupliquer par produit)

### Phase A — Conception (dans Printful)
- [ ] **A1. Choix du produit** (modèle, marque du blanc, fournisseur) et **coloris**
- [ ] **A2. Tailles** : S, M, L, XL, 2XL, 3XL — toutes activées
- [ ] **A3. Prix** : coût Printful relevé, prix de vente fixé, **marge ≥ 50 %** (livraison offerte dès 100 € incluse)
- [ ] **A4. Technique** : broderie ou impression (DTG), cohérente avec les tags `broderie` / `dtg`
- [ ] **A5. Emplacements** — cocher chaque zone utilisée :
  - [ ] Poitrine (gauche / droite)
  - [ ] Dos
  - [ ] Manche gauche · [ ] Manche droite
  - [ ] Poignet gauche · [ ] Poignet droit
- [ ] **A6. Arrière-plan du logo supprimé** (PNG transparent, via Canva `remove-background`) — si besoin
- [ ] **A7. Taille du logo** : largeur (width) et hauteur (height) réglées, position (haut/bas, centrage), résolution ≥ 150 dpi, dans la zone d'impression
- [ ] **A8. Variantes** : couleurs × tailles, une seule image de référence par couleur
- [ ] **A9. Mockups générés** (face, dos, côté/manche, détail) et relus

### Phase B — Fiche Shopify (statut *Brouillon*)
- [ ] **B1. Titre** au format `Type — Couleur` (ex. « Sweat à Capuche Unisexe — Noir »)
- [ ] **B2. Description** fidèle à la réalisation (emplacements, technique, composition)
- [ ] **B3. Images** : ≥ 3 (face, dos, détail) **avec texte alternatif descriptif** (pas « Product mockup »)
- [ ] **B4. Options** : « Taille » S→3XL ; SKU présents sur toutes les variantes
- [ ] **B5. SEO** : titre SEO + méta-description (≤ 160 car.), handle propre
- [ ] **B6. Collections** : « La collection » (+ « Page d'accueil » si mis en avant)
- [ ] **B7. Tags** : technique (`broderie`/`dtg`) + `catalogue`
- [ ] **B8. Type de produit / vendeur** renseignés (`Sweat à capuche` / `1paR'1`)

### Phase C — Validation avant exposition
- [ ] **C1. Commande test** (échantillon Printful) reçue et contrôlée : emplacement, taille du logo, qualité
- [ ] **C2. Relecture croisée** par un 2ᵉ membre de l'équipe (nom + date)
- [ ] **C3. Aperçu boutique** vérifié (mobile + ordinateur)

### Phase D — Publication
- [ ] **D1. Statut → Actif**
- [ ] **D2. Publié sur le canal « Boutique en ligne »**
- [ ] **D3. Visible en vitrine** (collection / page d'accueil) et lien fonctionnel
- [ ] **D4. Suivi post-publication** : 1ʳᵉ commande réelle contrôlée, retours clients

---

## 3. Audit de la boutique — état au 2026-11-07

Source : API Admin Shopify (5 produits trouvés). Les étapes A1, A4–A9, C1–C2 ne se lisent pas dans Shopify : elles restent à cocher à la main (🔎).

| Étape | Sweat Noir (`sweat-a-capuche-unisexe`) | Sweat Blanc (`sweat-a-capuche-unisexe-2`) | 3 anciens produits (archivés) |
|---|---|---|---|
| Statut Shopify | Brouillon | Brouillon | Archivé |
| A2 Tailles S→3XL | ✅ 6 tailles | ✅ 6 tailles | ✅ 6 tailles |
| A3 Prix / marge | ✅ 77,90 € · coût 32,37–34,97 € · marge ≈ 55–58 % | ✅ 69,90 € · coût 31,72–34,32 € · marge ≈ 51–55 % | ➖ 69,90 € |
| A4 Technique (tags) | ✅ `broderie`,`dtg` | ✅ `dtg` | ➖ |
| A5–A9 Printful | 🔎 à contrôler (poitrine gauche brodée + dos doré annoncés) | 🔎 à contrôler | ➖ |
| B1 Titre | ✅ | ✅ | ❌ formats incohérents |
| B2 Description | ✅ | ✅ | ➖ |
| B3 Images + alt | ✅ 3 images, alt descriptifs | ❌ 7 images dont 4 sans alt utile (« Product mockup » ou vide) | ❌ « Product mockup » |
| B4 Options / SKU | ✅ | ✅ | ✅ |
| B5 SEO | ❌ méta-description OK, **titre SEO manquant** | ❌ méta-description OK, **titre SEO manquant** | ❌ aucun |
| B6 Collections | ✅ Accueil + La collection | ✅ Accueil + La collection | ❌ aucune |
| B7 Tags | ✅ | ✅ | ❌ partiels |
| B8 Type / vendeur | ✅ | ✅ | ❌ vendeur « 1paR1 » / « 1paR'1 » incohérent |
| C1–C2 Validation | 🔎 non documentée | 🔎 non documentée | ➖ |
| D1 Actif | ❌ | ❌ | ➖ |
| D2 Publié (Boutique en ligne) | ❌ 0 canal | ❌ 0 canal | ➖ |
| D3 Vitrine | ❌ (non publié) | ❌ (non publié) | ➖ |

### Synthèse
- **Aucun produit n'est publié** : 2 brouillons (Noir, Blanc), 3 archivés (anciens essais, à ignorer ou supprimer).
- Les deux brouillons sont **proches de la fin de la phase B**. Actions restantes :
  1. Ajouter un **titre SEO** aux deux fiches.
  2. Corriger les **textes alternatifs** des 4 images du Blanc (« Product mockup » / vide).
  3. Valider en Phase C (échantillon + relecture), puis passer en **Actif** et publier sur la boutique en ligne.
- Point à confirmer dans Printful : le coût du Noir (broderie + impression dorée dos) est identique à celui d'un simple DTG ; vérifier que l'option broderie est bien comptée.

---

## 4. Mise à jour régulière
1. Relancer l'audit (routine planifiée) : lecture Shopify de tous les produits.
2. Cocher/décocher les cases de la section 3 selon l'état réel ; ajouter une colonne pour chaque nouveau produit.
3. Journal : `2026-11-07` — création du protocole + premier audit (0/2 produits publiables, 2 en phase B).
