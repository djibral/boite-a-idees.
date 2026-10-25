# Protocole de création produit — Printful → Shopify (1 paR'1)

> Dernière mise à jour automatique : **2026-10-25** (audit de la boutique Shopify : 6 produits).
> Règle d'or : **on ne passe à l'étape suivante qu'une fois la case cochée ET validée par un second regard.**
> Légende : `[x]` vérifié (preuve dans Shopify) · `[ ]` non conforme / à faire · `[?]` non vérifiable automatiquement (à contrôler dans Printful).

---

## 1. Meilleurs connecteurs pour automatiser le suivi

| Priorité | Connecteur | Rôle dans le protocole | Pourquoi |
|---|---|---|---|
| 1 | **Shopify** (déjà connecté) | Lire statut, variantes, prix, images, tags, descriptions ; passer en brouillon/actif ; collections | Source de vérité de la vitrine : permet de cocher automatiquement les cases vérifiables |
| 2 | **Printful ↔ Shopify (app native)** | Création produit, placements, variantes, synchro des prix et stocks | Seul endroit où se règlent broderie/impression, zones, taille du logo |
| 3 | **Notion** ou **monday.com** (déjà disponibles) | Tableau de suivi partagé : 1 ligne par produit, 1 colonne par étape (cases à cocher), statut Brouillon → Validé → Publié | Toute l'équipe voit l'avancement ; monday permet en plus des automatisations (alerte si une étape manque) |
| 4 | **Canva** (déjà disponible) | Préparation des logos : suppression d'arrière-plan, export PNG transparent, redimensionnement | Évite d'ouvrir un autre outil pour l'étape « arrière-plan / taille logo » |
| 5 | **Zapier** (déjà disponible) | Relier Shopify → Notion/monday/Google Sheets : nouveau produit = nouvelle ligne de suivi ; alerte e-mail si produit actif non conforme | Automatise la mise à jour de la check-list sans action manuelle |
| 6 | **Google Sheets / Drive** | Export de secours et archivage des preuves (captures de mockups) | Simple, partageable |
| 7 | **GitHub** (ce dépôt) | Historisation du protocole et des audits | Chaque mise à jour est datée et traçable |

**Recommandation** : socle = Shopify + Printful (natif) + Notion *ou* monday + Zapier pour la synchro. Canva pour les visuels.

---

## 2. Protocole étape par étape (à valider dans l'ordre)

### Phase A — Choix du produit (Printful)
- [ ] **A1. Produit** choisi dans le catalogue Printful (ex. sweat à capuche unisexe premium)
- [ ] **A2. Couleurs** retenues (une fiche multi-couleurs ou une fiche par couleur — décision d'équipe)
- [ ] **A3. Tailles** : S, M, L, XL, 2XL, 3XL (vérifier que toutes existent)
- [ ] **A4. Prix** : coût Printful + marge = prix de vente TTC (actuel : 69,90 €) ; cohérent pour toutes les variantes
- [ ] **A5. Méthode** : broderie / impression DTG (étiquette `broderie` / `dtg`)

### Phase B — Conception (éditeur Printful)
- [ ] **B1. Placement poitrine** (gauche/droite) : broderie ou impression
- [ ] **B2. Placement dos**
- [ ] **B3. Manche gauche / droite** (si besoin)
- [ ] **B4. Poignet gauche / droite** (si besoin)
- [ ] **B5. Suppression de l'arrière-plan** du logo (PNG transparent, via Canva) — si besoin
- [ ] **B6. Taille du logo** : largeur (width) et hauteur (height) notées, ratio conservé, résolution suffisante (≥ 150 dpi à la taille d'impression)
- [ ] **B7. Position** (offset haut/centre) contrôlée sur le mockup
- [ ] **B8. Limites broderie** : nombre de couleurs de fil, taille max de la zone
- [ ] **B9. Variantes** : le design est bien appliqué à chaque couleur (contraste : logo clair sur fond sombre, etc.)

### Phase C — Fiche Shopify (brouillon)
- [ ] **C1. Titre** clair, en français (`Sweat à Capuche Unisexe — Couleur`)
- [ ] **C2. Description** en français : histoire, détails, taille, fabrication, entretien, livraison/retours, mentions légales (RSGP)
- [ ] **C3. Guide des tailles** (tableau) intégré
- [ ] **C4. Images** : face, dos, détail ; **au moins une image par couleur** ; texte alternatif renseigné
- [ ] **C5. Variantes / SKU / prix** cohérents (aucune variante manquante, aucun prix à 0)
- [ ] **C6. Type de produit, vendeur** (`1paR'1`, orthographe exacte) et **tags** renseignés
- [ ] **C7. Collection** assignée

### Phase D — Contrôle qualité avant publication
- [ ] **D1. Mockups** relus par une 2ᵉ personne
- [ ] **D2. Commande test** (échantillon Printful) reçue et validée — au moins pour tout nouveau design
- [ ] **D3. Validation** formelle (nom + date dans le tableau de suivi)

### Phase E — Publication et vitrine
- [ ] **E1. Statut passé en « Actif »**
- [ ] **E2. Visible sur la boutique en ligne** (canal publié) et dans la bonne collection
- [ ] **E3. Contrôle final sur mobile + desktop**
- [ ] **E4. Revue périodique** (cette mise à jour) : le produit reste conforme

---

## 3. Audit des produits déjà dans la boutique (2026-10-25)

Les points `B*`, `A5`, `D*` ne sont **pas lisibles via Shopify** : ils restent `[?]` tant qu'on ne les contrôle pas dans Printful.

| Produit | Statut | A3 tailles | A4 prix | C1 titre FR | C2 descr. FR | C3 guide tailles | C4 images | C6 type/vendeur/tags | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| **Sweat à Capuche Unisexe — Noir** (`12314591199496`) | Actif | [x] S→3XL (6) | [x] 69,90 € | [x] | [x] | [ ] lien seulement, pas de tableau | [x] 3 (face/dos/détail), alt OK | [x] | **À corriger** : ajouter le tableau des tailles |
| **Sweat à Capuche Unisexe — Marine, Royal & Blanc** (`12320832946440`) | Actif | [x] S→3XL × 3 couleurs (18) | [x] 69,90 € | [x] | [x] | [x] | [ ] 3 images seulement pour 3 couleurs ; aucune image Bleu roi | [x] | **À corriger** : ajouter les visuels manquants (Bleu roi, Blanc face) |
| **Sweat à Capuche Unisexe — Blanc** (`12347015463176`) | Actif | [x] S→3XL (6) | [x] 69,90 € | [x] | [x] | [x] | [x] 3 (face/dos/manche), alt OK | [x] | **Conforme** côté Shopify (reste B*/D* à confirmer) |
| Unisex Hoodie (`12303775203592`) | Archivé | [ ] 5 variantes listées, 3XL absent | [x] 69,90 € | [ ] anglais | [ ] anglais, incomplète | [ ] | [?] | [x] | Archivé — ne pas republier tel quel |
| Sweat à Capuche blanc Unisexe (`12346956054792`) | Archivé | [ ] 3XL absent | [x] 69,90 € | [x] | [ ] ancienne version | [ ] | [?] | [ ] vendeur `1paR1 ` (faute + espace), aucun tag | Archivé — doublon du « Blanc » actif |
| Unisex Hoodie (`12303774875912`) | Archivé | [ ] 3XL absent | [ ] 69,37 / 70,67 € (prix hétérogènes) | [ ] anglais | [ ] | [ ] | [?] | [ ] type `T-SHIRT`, aucun tag | Archivé — ancien brouillon |

### Actions prioritaires
1. **Noir** : coller le tableau des tailles (identique aux deux autres fiches).
2. **Marine/Royal/Blanc** : ajouter au moins une image par couleur manquante (Bleu roi, Blanc face/détail).
3. Vérifier dans Printful les étapes **B1–B9** des 3 produits actifs et les cocher ici.
4. Décider du sort des 3 produits archivés (suppression définitive ou conservation comme historique).

---

## 4. Comment mettre à jour ce document
1. Relancer l'audit (la tâche planifiée lit les produits Shopify en direct).
2. Passer chaque case à `[x]` seulement si la preuve est visible dans Shopify, ou après contrôle humain dans Printful.
3. Dater la ligne « Dernière mise à jour » en haut et conserver l'historique via les commits Git.
