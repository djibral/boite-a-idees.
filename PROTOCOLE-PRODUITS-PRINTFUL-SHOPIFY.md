# Protocole de création de produits — Printful → Shopify (1paR'1)

Dernière mise à jour : 2026-10-29 (audit automatique, boutique `1par1.fr`, EUR).
Règle d'or : **une étape n'est cochée que lorsqu'elle est validée. On ne passe pas à la suivante sans validation.**

## 1. Connecteurs recommandés

| Besoin | Connecteur | Rôle dans le protocole |
|---|---|---|
| Catalogue, mockups, synchro produits | **Printful (app Shopify)** | Étapes 1–8 : création du produit, placements, variantes, publication |
| Boutique, statuts, prix, variantes | **Shopify (connecté)** | Étapes 9–12 : audit, publication, vitrine |
| Détourage / suppression d'arrière-plan, redimensionnement du logo | **Canva (connecté)** | Étape 5 : fichier PNG transparent, dimensions |
| Suivi d'équipe, cases à cocher, statuts par produit | **Notion** ou **monday.com** (connectés) | Tableau partagé : une ligne par produit, une colonne par étape |
| Automatisation (alerte brouillon, nouvelle ligne de suivi) | **Zapier** (connecté) | Shopify « produit créé/modifié » → ligne dans le tableau de suivi + notification |
| Stockage des visuels sources | **Google Drive / Sheets** | Archive des logos, export de la checklist |

Recommandation : **Printful + Shopify + Canva + Notion (ou monday.com) + Zapier**. Zapier relie Shopify au tableau de suivi pour que chaque produit créé génère automatiquement sa checklist.

## 2. Checklist par produit (à dupliquer pour chaque produit)

### A. Choix et configuration chez Printful
- [ ] 1. **Produit** choisi (modèle, fournisseur, qualité validée)
- [ ] 2. **Couleurs et tailles** retenues (S–2XL…)
- [ ] 3. **Prix** de vente fixé (coût Printful + marge + TVA, cohérent sur toutes les variantes)
- [ ] 4. **Technique** : broderie ou impression (DTG) choisie par zone
- [ ] 5. **Visuel** : arrière-plan supprimé si besoin (PNG transparent, haute résolution)
- [ ] 6. **Placements** : poitrine (gauche/droite) · dos · manche droite · manche gauche · poignet droit · poignet gauche
- [ ] 7. **Taille du logo** : width / height / position (haut, gauche), vérifiée sur l'aperçu pour chaque placement
- [ ] 8. **Variantes** : couleurs × tailles, SKU et photos par couleur
- [ ] 9. **Mockups** générés et contrôlés (aucun logo coupé ou décentré)

### B. Contrôle Shopify
- [ ] 10. **Titre, description, type, tags, vendor** conformes (français, sans faute)
- [ ] 11. **Prix** identique au prix validé à l'étape 3, sur toutes les variantes
- [ ] 12. **Images** : une photo par couleur, image principale correcte
- [ ] 13. **Produit de test commandé** (échantillon) et reçu conforme
- [ ] 14. **Validation finale** par un second membre de l'équipe

### C. Publication et vitrine
- [ ] 15. Statut passé de *Brouillon* à **Actif**
- [ ] 16. Ajouté à la **collection** / vitrine
- [ ] 17. Contrôle en ligne sur `1par1.fr` (affichage, panier, paiement)

## 3. Suivi de l'état de la boutique (audit du 2026-10-29)

Légende : ✅ vérifié automatiquement · ❓ à vérifier dans Printful / à la main (non vérifiable via Shopify).

| Produit | Statut Shopify | Variantes | Prix | Tags technique | 10 Titre/desc. | 11 Prix | 15 Actif | Étapes A (Printful) / 13–14 |
|---|---|---|---|---|---|---|---|---|
| Sweat à Capuche Unisexe — Noir | Brouillon | 5 tailles (S–2XL), 1 couleur | 69,90 € | broderie, dtg | ✅ | ✅ | ❌ | ❓ |
| Sweat à Capuche Unisexe — Marine, Royal & Blanc | Brouillon | 18 variantes (3 couleurs) | 69,90 € | broderie, dtg | ✅ | ✅ | ❌ | ❓ (image principale = visuel logo, pas un mockup produit) |
| Sweat à Capuche Unisexe — Blanc | Brouillon | 5 tailles | 69,90 € | broderie, dtg | ✅ | ✅ | ❌ | ❓ |
| Unisex Hoodie Blanc | Archivé | 5 | 69,90 € | aucun | ❌ titre en anglais, pas de tags | ✅ | — | Remplacé |
| Unisex Hoodie | Archivé | 5 | 69,90 € | broderie, dtg | ❌ titre en anglais | ✅ | — | Remplacé |
| Sweat à Capuche blanc Unisexe | Archivé | 5 | 69,90 € | aucun | ❌ description générique, vendor « 1paR1 » (écart) | ✅ | — | Remplacé |

### Constat
- **Aucun produit n'est actif** : 3 brouillons, 3 archivés. La vitrine est donc vide côté produits.
- Les 3 brouillons sont cohérents (prix 69,90 €, tags, description de marque) mais **aucun n'a passé les étapes 13–17**.
- Anomalie : l'unique produit multicolore n'indique que « Bleu marine » dans les 5 variantes listées sur 18 (à contrôler : 3 couleurs annoncées dans le titre).
- Écart de nom de vendor : « 1paR'1 » vs « 1paR1 » sur un produit archivé.
- Les étapes de placement/taille du logo (6–7) ne sont pas lisibles depuis Shopify : à cocher manuellement depuis l'éditeur Printful.

## 4. Mise à jour
Relancer l'audit régulièrement (routine planifiée) : compare les produits Shopify à cette checklist, met à jour les cases ✅/❌ et signale les produits qui sautent une étape.
