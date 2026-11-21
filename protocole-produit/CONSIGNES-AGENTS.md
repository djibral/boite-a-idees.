# Consignes communes à tous les agents — Protocole produit 1.paR'1

Page de suivi (protocole + cases + propositions) : https://claude.ai/artifact/Esko6o9uvELSpAVckJbX2e

Tout agent (tâche programmée ou session) qui touche aux produits de la boutique 1par1.fr suit ces règles.

## 1. Lire
- Lire les 25 étapes du protocole sur la page (A1–A13 Printful, B1–B8 fiche Shopify, C1–C4 mise en vente).
- Lire la base de la page : collections `produits`, `validations`, `propositions`.

## 2. Vérifier et constater
- Comparer chaque produit Shopify (Actif et Brouillon) à chaque étape.
- Mettre à jour `produits/<handle>` : pastilles `auto` (`ok` / `ko` / `na` + note), `autoKo`, `critical`, `auditedAt`.
- Ne jamais cocher une case de `validations` : les cases sont réservées à l'équipe.

## 3. Proposer
- Pour chaque écart, créer un document `propositions/<id>` :
  `product` (handle), `step` (ex. `b6`), `field`, `current`, `proposed`, `reason`,
  `kind` (`shopify` si un agent peut l'appliquer, `humain` si Printful / photo / échantillon),
  `status: "proposee"`, `proposedBy`, `proposedAt`.
- Ne pas recréer une proposition déjà existante, ni une proposition `refusee`.

## 4. Demander l'autorisation
- Envoyer une notification courte : nombre de propositions en attente + la plus importante.
- Seul le propriétaire (D'ji) décide (bouton Approuver / Refuser sur la page). La règle d'accès `propositions` est `write: owner`.

## 5. Appliquer (uniquement ce qui est approuvé)
- Appliquer sur Shopify **seulement** les propositions `status: "approuvee"` et `kind: "shopify"`, exactement comme écrites.
- Vérifier d'abord que la valeur actuelle correspond encore à `current` ; sinon, ne rien modifier et reposer la question.
- Après succès : `status: "appliquee"`, `appliedAt`. En cas d'échec : laisser `approuvee` et le signaler.
- Jamais : changer un prix, publier / archiver / supprimer un produit, ou toucher à Printful sans une proposition approuvée qui le dit explicitement.

## 6. Pas de nouvelle branche GitHub
- Ne jamais créer de branche, de commit ni de pull request pour le suivi quotidien : l'état des produits vit uniquement sur la [page de suivi](https://claude.ai/artifact/Esko6o9uvELSpAVckJbX2e).
- Ce dossier `protocole-produit/` ne change que sur demande explicite de D'ji.

## 7. Liens cliquables (obligatoire)
Dans chaque réponse, notification ou compte rendu, écrire les liens sous forme cliquable `[texte](https://…)`, jamais en texte brut ni en simple nom de fichier :
- la page de suivi : [Protocole Produit 1.paR'1](https://claude.ai/artifact/Esko6o9uvELSpAVckJbX2e)
- chaque produit cité : sa page boutique (`https://1par1.fr/products/<handle>`) et sa fiche admin (`https://1par1.fr/admin/products/<id>`)
- chaque fichier du dépôt cité : son lien GitHub (`https://github.com/djibral/boite-a-idees./blob/<branche>/<chemin>`)

## Phrase à ajouter au prompt de chaque tâche programmée
> Avant toute action sur les produits, lis et applique `protocole-produit/CONSIGNES-AGENTS.md` du dépôt boite-a-idees. (vérifier → proposer → attendre l'accord → appliquer).
