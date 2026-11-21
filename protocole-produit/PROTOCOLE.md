# Protocole produit 1.paR'1 — de Printful à la vitrine Shopify

> **Où cocher ?** Uniquement sur la page de suivi partagée [Protocole Produit 1.paR'1](https://claude.ai/artifact/Esko6o9uvELSpAVckJbX2e) (25 étapes : A1–A13, B1–B8, C1–C4). Ce document est le **guide détaillé** de chaque étape ; sa numérotation (A1–A8, B1–B6, C1–C4) regroupe certaines étapes de la page. Règles de marque : *Bible de marque* (Notion).

> Objectif : **aucun produit en vitrine sans avoir passé toutes les étapes.**
> Chaque étape a un **critère de validation**. On ne passe à l'étape suivante que lorsque la case est cochée.
> Le tableau de suivi des produits déjà en boutique est sur la [page de suivi](https://claude.ai/artifact/Esko6o9uvELSpAVckJbX2e), mise à jour chaque matin. [`SUIVI-BOUTIQUE.md`](./SUIVI-BOUTIQUE.md) n'est qu'un instantané du 21/11/2026.

Légende : 🖐️ = vérification manuelle (dans Printful) · 🤖 = vérifiable automatiquement (Shopify, par la routine)

---

## PHASE A — Création dans Printful

### A1. Choix du produit 🖐️
- [ ] Produit de base choisi dans le catalogue Printful (ex. *Unisex Hoodie* Cotton Heritage / Gildan)
- [ ] Coloris choisi **un seul coloris par fiche produit** (règle 1.paR'1 actuelle : 1 fiche = 1 couleur)
- [ ] Fiche technique notée : composition, grammage, pays d'origine (sert pour la description, étape B3)
- **Validé si :** le produit et le coloris sont écrits dans la fiche de lancement.

### A2. Tailles 🖐️
- [ ] Tailles cochées : **S, M, L, XL, 2XL, 3XL** (standard sweat)
- [ ] Tailles non désirées décochées (ex. XS, 4XL, 5XL) pour ne pas créer de variantes inutiles
- **Validé si :** 6 tailles exactement, dans l'ordre S → 3XL.

### A3. Placements (technique par zone) 🖐️
Pour chaque zone, choisir **Broderie**, **Impression (DTG)** ou **Rien** :

| Zone | Technique | Fichier logo | Validé |
|---|---|---|---|
| Poitrine gauche | Broderie / DTG / — | | [ ] |
| Poitrine centre | Broderie / DTG / — | | [ ] |
| Dos | Broderie / DTG / — | | [ ] |
| Manche gauche | Broderie / DTG / — | | [ ] |
| Manche droite | Broderie / DTG / — | | [ ] |
| Poignet gauche | Broderie / — | | [ ] |
| Poignet droit | Broderie / — | | [ ] |

- **Validé si :** le tableau est rempli et correspond exactement à ce qui sera écrit dans le titre Shopify (étape B1).

### A4. Préparation du fichier logo 🖐️
- [ ] **Suppression de l'arrière-plan** si besoin (PNG transparent) — outil : Canva *Remove background* (connecteur Canva) ou l'outil Printful
- [ ] Résolution : **300 DPI** à la taille d'impression
- [ ] Broderie : **15 couleurs de fil max**, pas de dégradés, pas de traits < 1 mm, couleur de fil choisie dans la palette Printful (ex. or métallisé, marine)
- [ ] Contraste vérifié avec la couleur du tissu (logo clair sur tissu foncé et inversement)
- **Validé si :** aperçu Printful sans avertissement (« low resolution », « thin lines »).

### A5. Taille et position du logo (width / height) 🖐️
Valeurs de référence 1.paR'1 — **les maximums dépendent du modèle : toujours confirmer avec la zone affichée par l'éditeur Printful** (à ajuster dans l'éditeur Printful, champ *Width/Height* + *Position*) :

| Zone | Largeur max Printful | Largeur conseillée 1.paR'1 | Position |
|---|---|---|---|
| Poitrine gauche (broderie) | 4" (10,2 cm) | **3,5" – 4"** | aligné en haut de la zone, centré sur le cœur |
| Poitrine centre (broderie) | 4" (10,2 cm) | 3,5" – 4" | centré |
| Dos (DTG) | 12" (30,5 cm) | **10" – 12"** | centré, haut à ~3" sous le col |
| Manche (broderie) | 1,5" hauteur | 1,25" – 1,5" | centré sur la manche |
| Poignet (broderie) | 1" – 1,25" hauteur selon modèle | max autorisé | centré sur le poignet |

- [ ] Ratio largeur/hauteur **verrouillé** (pas de logo déformé)
- [ ] Logo centré (utiliser les boutons d'alignement Printful)
- [ ] Même taille de logo sur tous les coloris d'une même gamme
- **Validé si :** les mesures sont notées dans la fiche de lancement et identiques à la gamme.

### A6. Mockups 🖐️
- [ ] Générer au minimum : **face, dos, côté du poignet/manche brodé(e)**
- [ ] Vérifier sur chaque mockup : logo net, bien placé, bonne couleur de fil
- **Validé si :** ≥ 3 mockups, toutes les zones décorées sont visibles sur au moins une image.

### A7. Prix 🖐️ + 🤖
- [ ] Coût Printful (produit + broderie par zone + impression + livraison) noté
- [ ] Prix de vente fixé : **69,90 € pour les sweats** (prix gamme actuel), marge ≥ 40 % du prix HT
- [ ] Même prix sur toutes les tailles (sauf décision : surcoût 2XL/3XL)
- **Validé si :** 🤖 toutes les variantes ont le prix de la gamme.

### A8. Envoi vers Shopify (« Submit to store ») 🖐️
- [ ] Synchronisation Printful → Shopify faite, le produit arrive **en Brouillon (Draft)** — ne jamais le publier directement

---

## PHASE B — Fiche produit Shopify (le produit reste en Brouillon)

### B1. Titre 🤖
- [ ] Format : `Sweat à capuche 1.paR'1 — <Couleur>, <technique + zones>`
  ex. *Sweat à capuche 1.paR'1 — Noir, brodé poitrine et poignet, imprimé dos*
- [ ] Les zones citées = celles du tableau A3

### B2. Variantes 🤖
- [ ] Option nommée **« Taille »**, valeurs S → 3XL
- [ ] SKU Printful présent sur chaque variante
- [ ] Une image associée à chaque variante

### B3. Description 🤖
Gabarit 1.paR'1 obligatoire (copier depuis le sweat Noir) :
- [ ] « Un pas après l'autre » + L'histoire (1 % de mieux chaque jour)
- [ ] Caractéristiques (composition **exacte**, grammage, origine, zones décorées)
- [ ] Taille + lien **guide des tailles**
- [ ] Fabrication à la demande + délai
- [ ] Entretien
- [ ] Livraison et retours (liens politiques)
- [ ] Mentions légales **RSGP** (opérateur responsable + contact)

### B4. Médias 🤖
- [ ] ≥ 3 images (face / dos / détail brodé)
- [ ] Texte alternatif descriptif sur **chaque** image (jamais « Product mockup »)

### B5. Organisation 🤖
- [ ] Type de produit : `Sweat à capuche`
- [ ] Fournisseur : `1.paR'1`
- [ ] Tags : `catalogue` + technique(s) (`broderie`, `dtg`) + **couleur** (`noir`, `blanc`, `bleu`, `vert`…)
- [ ] Ajouté à la/les collection(s) concernée(s)

### B6. SEO 🤖
- [ ] Titre SEO : `<Produit> <couleur> brodé 1.paR'1 | 1par1.fr` (≤ 70 caractères)
- [ ] Méta-description ≤ 160 caractères, avec couleur, technique, tailles et prix

---

## PHASE C — Validation finale et mise en vente

### C1. Contrôle croisé 🖐️
- [ ] Une 2ᵉ personne relit la fiche (titre ↔ placements ↔ images ↔ description cohérents)
- [ ] Aperçu de la page produit sur mobile et ordinateur

### C2. Commande test (recommandé pour chaque nouveau modèle) 🖐️
- [ ] Échantillon commandé via Printful (remise échantillon) et contrôlé à réception

### C3. Publication 🤖
- [ ] Statut passé à **Actif** et publié sur la Boutique en ligne
- [ ] URL de la page produit fonctionnelle

### C4. Suivi continu 🤖
- [ ] La routine re-vérifie automatiquement tous les produits actifs et met à jour la [page de suivi](https://claude.ai/artifact/Esko6o9uvELSpAVckJbX2e)

---

## Connecteurs recommandés (automatisation)

| Besoin | Meilleur connecteur | Statut | Ce qu'il automatise |
|---|---|---|---|
| Audit des fiches, tags, SEO, statut, prix | **Shopify** (MCP) | ✅ connecté | Contrôles 🤖 des phases B et C, mise à jour du tableau de suivi |
| Arrière-plan, redimensionnement, export logo 300 DPI | **Canva** (MCP) | ✅ connecté | Étape A4 (*remove background*, export PNG) |
| Tableau de suivi partagé à cases à cocher | **GitHub** (ce dépôt) — ou **Notion** / **monday.com** / **Google Sheets** | ✅ connectés | Visibilité équipe, cases cochées, historique |
| Printful (placements, tailles logo, mockups, coûts) | **API Printful** (jeton privé) | ⚠️ pas de connecteur MCP ni Zapier | Phase A reste manuelle ; un script API pourrait lire les placements/dimensions et les coûts |
| Rappels de revue | **Google Agenda** / **Gmail** | ✅ connectés | Rappel hebdo de revue des brouillons |

> Prochaine amélioration possible : ajouter un jeton API Printful (variable d'environnement de la routine) pour vérifier automatiquement les étapes A2–A5 et A7 (placements, dimensions, coût → marge).
