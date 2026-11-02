# Protocole de création de produit — Printful → Shopify (1paR'1)

Dernière mise à jour : 2026-11-02 (relance automatique). Boutique : 1par1.fr (Shopify Basic, EUR).
Règle d'or : **une étape n'est jamais commencée tant que la précédente n'est pas cochée ET validée par une 2e personne.**
Légende : `[x]` validé · `[ ]` à faire · `[?]` non vérifiable automatiquement (contrôle humain requis).

---

## 1. Connecteurs recommandés (automatisation et suivi)

| Besoin | Connecteur | Statut dans cet environnement | Usage dans le protocole |
|---|---|---|---|
| Catalogue, statuts, prix, variantes | **Shopify** | Connecté | Audit automatique des produits (voir §4) |
| Création produit, mockups, tailles, broderie/impression | **Printful** (app native Shopify, ou via Zapier) | Pas de connecteur direct. Utiliser l'app Printful dans Shopify, ou **Zapier** | Étapes 1 à 8 |
| Suppression d'arrière-plan, redimensionnement du logo | **Canva** (`remove-background`, `resize-design`) | Connecté | Étapes 6 et 7 |
| Relier les outils, alertes quand un produit change de statut | **Zapier** | Connecté | Étape 10, notifications d'équipe |
| Tableau de suivi partagé avec cases à cocher | **Google Sheets** ou **Notion** ou **monday.com** | Connectés | Une ligne par produit, une colonne par étape |
| Rappels de relecture régulière | **Google Calendar** | Connecté | Revue hebdomadaire |

Recommandation : garder ce fichier comme référence unique de la procédure, et le tableau de suivi (Sheets ou Notion) comme vue d'équipe.

---

## 2. Procédure pas à pas (à répéter pour chaque produit)

### Étape 1 — Choix du produit chez Printful
- [ ] Modèle choisi (ex. Unisex Premium Pullover Hoodie), fournisseur et délai de production notés
- [ ] Couleurs retenues
- [ ] Validé par : ____ le ____

### Étape 2 — Tailles et variantes
- [ ] Gamme de tailles complète (S, M, L, XL, 2XL, plus 3XL si disponible)
- [ ] Une variante par couleur et par taille, aucune variante en trop
- [ ] SKU générés et cohérents
- [ ] Validé par : ____

### Étape 3 — Prix
- [ ] Coût Printful (produit + broderie/impression + expédition) relevé
- [ ] Prix de vente TTC fixé, marge calculée
- [ ] Même prix sur toutes les variantes (sauf supplément 2XL voulu)
- [ ] Validé par : ____

### Étape 4 — Technique : broderie ou impression
- [ ] Technique choisie par zone (broderie ou impression DTG)
- [ ] Nombre de couleurs de fil, limites de détail de la broderie vérifiés
- [ ] Tag Shopify posé (`broderie`, `dtg`)
- [ ] Validé par : ____

### Étape 5 — Emplacements
- [ ] Poitrine (gauche, droite ou centre)
- [ ] Dos
- [ ] Manche droite / manche gauche
- [ ] Poignet droit / poignet gauche
- [ ] Zones non utilisées explicitement vides
- [ ] Validé par : ____

### Étape 6 — Préparation du logo
- [ ] Fichier source en haute définition (PNG transparent ou vectoriel)
- [ ] Arrière-plan supprimé si besoin (Canva `remove-background`)
- [ ] Contrôle sur fond clair ET fond sombre (pas de halo)
- [ ] Validé par : ____

### Étape 7 — Taille et position du logo
- [ ] Largeur (width) et hauteur (height) notées pour chaque zone : ____ × ____ mm
- [ ] Position (haut, gauche) notée, alignement vérifié
- [ ] Respect des limites de zone Printful
- [ ] Validé par : ____

### Étape 8 — Variantes et mockups
- [ ] Mockups générés pour chaque couleur (face, dos, manches)
- [ ] Le logo reste lisible sur chaque couleur de vêtement
- [ ] Image principale = mockup du produit porté ou à plat, pas le fichier de design brut
- [ ] Validé par : ____

### Étape 9 — Fiche Shopify
- [ ] Titre clair, description complète (matière, entretien, technique, emplacements)
- [ ] Type de produit, vendeur (**« 1paR'1 » écrit pareil partout**), tags
- [ ] Collection assignée
- [ ] Guide des tailles
- [ ] Validé par : ____

### Étape 10 — Publication en brouillon puis relecture croisée
- [ ] Produit en **brouillon** (Draft), aperçu vérifié sur mobile et ordinateur
- [ ] Commande test (ou échantillon Printful) contrôlée
- [ ] Deuxième personne relit toutes les étapes ci-dessus
- [ ] Validé par : ____

### Étape 11 — Mise en vitrine
- [ ] Statut passé à **Actif**
- [ ] Visible dans la collection et sur le canal de vente
- [ ] Contrôle après publication (prix, photos, variantes, stock)
- [ ] Validé par : ____

---

## 3. Mise à jour régulière
1. Chaque semaine, relancer l'audit des produits Shopify (§4) et recocher.
2. Tout produit actif doit avoir les 11 étapes cochées. Sinon le repasser en brouillon.
3. Noter la date et l'auteur de chaque modification dans le tableau d'équipe.

---

## 4. Audit des produits Shopify au 2026-11-02

Source : lecture en direct de la boutique via le connecteur Shopify. 6 produits au total : **0 actif, 3 brouillons, 3 archivés**. Aucun produit n'est donc actuellement en vitrine.

Seuls les points lisibles via Shopify sont cochés. Les étapes 1, 4, 5, 6, 7 (emplacements, logo, tailles de logo) demandent de consulter Printful : elles restent `[?]`.

| Produit | Statut | Prix | Variantes | Tags | Étapes 2-3 (tailles, prix) | Étape 4 (tag technique) | Étape 8 (image principale) | Étape 9 (fiche) | Étapes 5-7 |
|---|---|---|---|---|---|---|---|---|---|
| Sweat à Capuche Unisexe — Noir | Brouillon | 77,90 € | 6 | broderie, catalogue, dtg | [x] | [x] | [x] mockup | [x] | [?] |
| Sweat à Capuche Unisexe — Marine, Royal & Blanc | Brouillon | 77,90 € | 18 | broderie, catalogue, dtg | [x] | [x] | **[ ] image = fichier de design brut** (`1R1_233mm_grand-dos_noir.png`) | [x] | [?] |
| Sweat à Capuche Unisexe — Blanc | Brouillon | 77,90 € | 6 | broderie, catalogue, dtg | [x] | [x] | [x] mockup | [x] | [?] |
| Unisex Hoodie Blanc | Archivé | 69,90 € | 6 | aucun | [x] | [ ] | [x] | [ ] titre non francisé, pas de tags | [?] |
| Unisex Hoodie | Archivé | 69,90 € | 6 | broderie, dtg | [x] | [x] | [x] | [ ] titre non francisé | [?] |
| Sweat à Capuche blanc Unisexe | Archivé | 69,90 € | 6 | aucun | [x] | [ ] | [x] | [ ] vendeur « 1paR1 » (différent de « 1paR'1 »), pas de tags | [?] |

### Points d'attention
1. **Rien n'est en vitrine** : les 3 brouillons sont les candidats à publier. Ils passent l'étape 9 sur les points lisibles, mais ni les étapes 5 à 7 ni l'étape 10 (relecture croisée) ne sont confirmées.
2. **« Marine, Royal & Blanc »** : l'image principale est un fichier de design, à remplacer par un mockup avant publication. Les 18 variantes (3 couleurs × 6 tailles) n'ont pas toutes été relues ici, seules 5 sont remontées par la lecture.
3. **Nombre de variantes** : chaque produit à 6 variantes n'affiche que 5 tailles (S à 2XL) dans la lecture. Vérifier la 6e variante (ou une variante par défaut inutile).
4. **Prix** : les brouillons sont à 77,90 €, les archivés à 69,90 €. À confirmer comme prix voulu à l'étape 3.
5. **Nettoyage** : le vendeur « 1paR1 » (sans apostrophe) est incohérent. Les 3 archivés peuvent rester archivés.
6. Les descriptions sont tronquées dans la lecture : leur contenu complet (emplacements, entretien) reste à relire à l'étape 9.

### Prochaine action recommandée
Terminer les étapes 5 à 8 sur le brouillon « Noir » en premier (il est le plus propre), faire la relecture croisée (étape 10), puis le passer en Actif.
