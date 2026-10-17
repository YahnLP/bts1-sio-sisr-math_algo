# Cours – Méthode de l'épreuve E3 et révisions

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S19 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S01 à S18.
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Connaître** le format de l'épreuve E3 et la manière de gérer son temps ;
- [ ] **Rédiger** une réponse complète : méthode, calcul, résultat, vérification ;
- [ ] **Identifier** ses points faibles par un auto-diagnostic ;
- [ ] **Composer** sans aide un sujet de 2 h et **se corriger** avec le barème ;
- [ ] **Écrire** un algorithme en Python sur un sujet type.

## I. Le format de l'épreuve E3

L'épreuve de mathématiques pour l'informatique est une **épreuve écrite** de **2 heures**, notée sur **20 points**, de **coefficient 3**. Le sujet comporte **deux ou trois exercices**, dont **un exercice de programmation** (en Python dans cette formation). Il n'y a pas de contrôle en cours de formation : l'évaluation est **terminale**.

> [!NOTE]
> Ce format est celui du document de déroulement de l'épreuve de la session 2026 : à **vérifier à chaque session** auprès du document en vigueur, notamment pour les moyens de calcul autorisés (calculatrice) (voir [Programme et épreuve E3](../../ressources/programme-e3.md)).

Les exercices s'appuient sur des **situations professionnelles** (adressage, droits d'accès, journaux, planification de projet). Les consignes précisent la **méthode à suivre** quand le programme l'exige (Dijkstra, MPM, niveaux, méthode des lignes).

## II. Gérer son temps

| Étape | Durée | Conseil |
|---|---|---|
| Lecture complète du sujet | 10 min | repérer les questions faciles et les points de chaque exercice |
| Exercices | environ 1 h 35 | environ **4,5 min par point** : un exercice à 6 points mérite environ 27 min |
| Relecture et vérification | 15 min | refaire un calcul par une autre voie, vérifier les unités et les cas limites |

- Commencer par l'exercice où l'on est le plus sûr.
- Ne pas rester bloqué : passer à la question suivante en indiquant où l'on en est ; les questions sont souvent **indépendantes**.
- Garder du temps pour l'exercice de programmation : il se prépare **au brouillon** (cas de base, variables, boucle) avant d'écrire le code.

## III. Rédiger une réponse complète

Une réponse de calcul comporte **quatre éléments** :

1. **La méthode** : « on applique l'algorithme d'Euclide », « on utilise la formule de la somme d'une suite géométrique » ;
2. **Le calcul**, avec les étapes intermédiaires (on peut perdre des points sur un résultat juste sans calcul) ;
3. **Le résultat**, avec son **unité** et une phrase de conclusion dans le contexte ;
4. **Une vérification** quand elle est rapide : reporter dans l'énoncé, contrôler un ordre de grandeur.

Pour un **algorithme** : donner l'entrée, la sortie, les variables, puis les instructions indentées ; en Python, des noms de variables parlants et un `return`.

## IV. Les erreurs qui coûtent des points

| Domaine | Erreur fréquente | Réflexe |
|---|---|---|
| Numération | oublier que les rangs commencent à 0 ; lire les restes dans le mauvais sens | vérifier en reconvertissant |
| Adressage | oublier de retirer 2 adresses (réseau et diffusion) | \(2^{32-n} - 2\) |
| Arithmétique | s'arrêter avant le reste nul | le PGCD est le **dernier reste non nul** |
| Congruences | simplifier sans inversibilité | n'inverser que si PGCD = 1 |
| Logique | nier une implication en \(\neg p \Rightarrow \neg q\) | \(\neg(p \Rightarrow q) \equiv p \wedge \neg q\) |
| Matrices | multiplier dans le mauvais ordre, tailles incompatibles | vérifier colonnes de \(A\) = lignes de \(B\) |
| Suites | confondre rang et nombre de termes | \(u_0, \dots, u_n\) : \(n + 1\) termes |
| Graphes | oublier un prédécesseur | retracer chaque arc dans le tableau |
| Python | indices de 0 à \(n - 1\) ; boucle sans variant | suivre les variables sur un petit exemple |

## V. Carte des notions

| Séance | Notion | À savoir faire |
|---|---|---|
| S01–S02 | Numération, réels, calcul binaire | convertir (2, 10, 16), additionner, arrondir |
| S03–S04, S12, S18 | Algorithmique | conditions, boucles, tableaux, chaînes, récursivité, complexité |
| S05–S07 | Arithmétique | division euclidienne, PGCD, premiers, congruences |
| S08–S10 | Logique et calcul booléen | tables, équivalences, quantificateurs, Karnaugh, masques |
| S11 | Relations et applications | propriétés, classes, injective/surjective/bijective |
| S13–S14 | Matrices | produit, puissances, inverse, systèmes |
| S15 | Suites | arithmétiques, géométriques, limites, seuils |
| S16–S17 | Graphes | matrice d'adjacence, niveaux, Dijkstra, MPM |

## À retenir

- E3 : écrit de 2 h, 20 points, coefficient 3, 2 ou 3 exercices dont un de programmation.
- Réponse complète = méthode, calcul, résultat avec unité, vérification.
- S'entraîner en conditions réelles : le sujet blanc de l'annexe se compose **sans aide** en 2 h, puis se corrige avec le barème.
