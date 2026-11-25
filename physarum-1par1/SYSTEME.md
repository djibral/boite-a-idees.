# Système Blob 1par1 — architecture

Un système inspiré du Physarum polycephalum pour faire vivre 1par1.fr sur le net : il explore, sent ce qui nourrit (les ventes), renforce ce qui circule, élague les impasses et garde une mémoire de ce qu'il a appris.

Visualisation de référence : [labyrinthe.html](./labyrinthe.html) (le blob trouve le plus court chemin entre A et B).

## A et B

- **A, aujourd'hui (relevé du 25/11/2026)** : boutique prête, 5 sweats en vente, 0 € de CA réel, 213 sessions en 90 jours (presque toutes en accès direct), 3 réseaux reliés à Metricool (Instagram, TikTok, YouTube). Détail : [memoire/releve-2026-11-25.md](./memoire/releve-2026-11-25.md).
- **B, l'objectif** : 300 000 €. Horizon de travail : fin 2027.

Le blob ne vise pas B d'un coup. Il avance de source de nourriture en source de nourriture :

| Palier | Seuil | Ce qu'il prouve |
|---|---|---|
| P0 Allumage | 1re vente réelle (hors commande test) | Quelqu'un d'extérieur paie |
| P1 Preuve | 10 ventes | L'offre convertit ; on connaît les premiers canaux qui nourrissent |
| P2 Traction | 100 ventes (≈ 7 000 € CA) | Un canal répète ; premiers avis clients |
| P3 Rentable | 1 000 € de marge nette par mois | Le réseau se finance lui-même |
| P4 Rythme | 25 000 € de CA par mois | Cadence d'un 300 000 € annuel |

## Contexte (réponses du 25/11/2026)

- **Statut** : micro-entreprise, a priori en franchise de TVA. Demande au greffe d'Antibes refusée, motif à clarifier avant d'encaisser des ventes.
- **Livraison** (vérifié dans Shopify) : France 7,90 €, Express 10,99 €, offerte dès 100 €. UE 22 €, international 29 €. Printful facture ~7,29 € pour la France.
- **Comptes** : réseaux au nom de 1paR1.officiel ; Instagram, TikTok et YouTube reliés à Metricool, les autres pas encore.
- **Catalogue prévu** : t-shirt (~35 €), casquette ; produit numérique « Un pas à la fois » de Coach Ray et Inès (vidéo et/ou bande dessinée).
- **Budget** : 0 € par mois. Tout passe par les outils gratuits et le contenu organique.
- **Campagne en cours** : [campagnes/noel-2026.md](./campagnes/noel-2026.md).
- **Relevé automatique** : chaque lundi matin (tâche planifiée), rapport dans `memoire/releve-AAAA-MM-JJ.md`.

## Ordre de grandeur (sweat à 69,90 €)

- Marge par sweat avant pub : environ **26 à 33 €** (prix Printful 34,37 à 42 €, moins ~2,30 € de frais de paiement). À confirmer avec le régime de TVA.
- **300 000 € de CA** ≈ 4 300 sweats ≈ 360 par mois ≈ 12 par jour.
- **300 000 € de bénéfice** ≈ 11 500 sweats ≈ 800 000 € de CA avec un seul produit.
- Avec 1 à 2 % de conversion, 4 300 ventes demandent 215 000 à 430 000 visites par an.

Conséquence : un seul produit à 70 € ne suffira pas. Il faut élargir le catalogue (prix d'entrée plus bas, produits à forte marge) et faire tourner un canal d'acquisition qui coûte moins de ~26 € par vente.

## Les organes

| Organe | Rôle biologique | Version 1par1 | Source |
|---|---|---|---|
| **Capteurs** | Sentir nutriments, lumière, obstacles | Relevé ventes, paniers, sessions, sources de trafic ; stats des posts ; tendances | Shopify, Metricool, vidIQ (TikTok/Insta/YouTube), OpenSEO |
| **Front d'exploration** | Avancer partout en éventail | Lots de contenus courts (Famille 1 paR 1), angles produits, nouveaux canaux, nouvelles fiches | [short-video-automation](../short-video-automation), [univers-1par1](../univers-1par1) |
| **Tubes** | Transporter le cytoplasme | Chaque chemin vers une vente : canal → contenu → page produit → panier | Liens UTM obligatoires sur chaque publication |
| **Renforcement** | Épaissir le tube parcouru | Plus de fréquence et de déclinaisons sur ce qui amène des clics boutique et des ventes | Règles ci-dessous |
| **Élagage** | Rétracter le tube vide, par les bouts | On arrête un format ou un angle sous le seuil | Règles ci-dessous |
| **Mémoire** | Trace laissée sur le substrat, habituation | Journal des tests, tendances absorbées, leçons | [memoire/](./memoire) |

## La nourriture (ce qui compte)

Ordre de valeur des signaux, du plus nourrissant au moins nourrissant :

1. Vente (CA, marge)
2. Passage en caisse, ajout au panier
3. Clic vers 1par1.fr (UTM)
4. Enregistrement, partage
5. Commentaire, abonnement
6. Vue, like : ne nourrit pas seul

## Le cycle (hebdomadaire au démarrage)

1. **Sentir** (lundi) : relevé Shopify + Metricool, rangé dans `memoire/`.
2. **Explorer** : proposer le lot de la semaine (ex. 5 shorts, 2 angles produit, 1 test de canal), chacun avec son UTM.
3. **Valider** : vous validez (niveau d'autonomie actuel, voir plus bas).
4. **Renforcer / élaguer** (lundi suivant) : appliquer les règles, noter la leçon dans le journal.

Règles de départ (à ajuster quand les données arrivent) :

- **Renforcer** un format ou un angle qui amène au moins 1 ajout au panier ou 1 % de clics boutique : on le décline 3 fois.
- **Élaguer** un format qui fait 0 clic boutique après 5 publications.
- **Ne jamais élaguer** une piste en moins de 7 jours : c'est trop tôt pour juger.
- **Garder 20 %** de l'effort en exploration pure, même quand une piste marche. Le blob qui arrête d'explorer meurt quand sa source s'épuise.

## Autonomie

| Niveau | Statut | Ce que le blob fait seul | Ce que vous validez |
|---|---|---|---|
| (a) | **Actif** | Lit les données, propose lots, textes, fiches, rapports | Tout ce qui est publié ou modifié |
| (b) | Prochaine étape | Publie le contenu programmé | Prix, promos, fiches produit, pub |
| (c) | Plus tard | Gère un budget pub plafonné | Le plafond et les règles d'arrêt |

## Limites à ne jamais franchir (proposition, à valider)

- Pas de promesse santé, minceur ou médicale (l'univers parle de sport et de mobilité).
- Pas de prix sous le seuil de marge fixé (à définir).
- Pas de faux avis, faux compteurs de stock ou fausse urgence.
- Pas de tendance politique, religieuse ou de drame d'actualité.
- Pas de musique sous droits dans les vidéos de marque.
