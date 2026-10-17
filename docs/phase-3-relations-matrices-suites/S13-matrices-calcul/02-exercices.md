# Exercices – Sommes, produits et puissances de matrices

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S13*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Lire une matrice

On reprend \(Q = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 2 \\ 4 & 2 & 2 \end{pmatrix}\) (lignes : Bureautique, Développement, Graphisme ; colonnes : RAM, SSD, écran).

1. Quelle est sa taille ? Que valent \(q_{12}\) et \(q_{31}\) ? Que signifient-ils ?
2. Calculer \(2Q\). Que représente-t-elle pour un achat de deux postes de chaque type ?
3. Une seconde commande est décrite par \(R = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 0 \\ 2 & 2 & 2 \end{pmatrix}\). Calculer \(Q + R\).

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(3 \times 3\) ; \(q_{12} = 1\) (un SSD pour un poste de bureautique) ; \(q_{31} = 4\) (quatre barrettes de RAM pour un poste de graphisme).
2. \(2Q = \begin{pmatrix} 2 & 2 & 2 \\ 4 & 2 & 4 \\ 8 & 4 & 4 \end{pmatrix}\) : les quantités de composants pour deux postes de chaque type.
3. \(Q + R = \begin{pmatrix} 2 & 1 & 2 \\ 2 & 2 & 2 \\ 6 & 4 & 4 \end{pmatrix}\).

</details>

## Exercice 2 – Produits possibles ?

Pour chaque couple de tailles, dire si \(AB\) est défini, et sa taille : (a) \(2 \times 3\) et \(3 \times 4\) ; (b) \(3 \times 2\) et \(3 \times 2\) ; (c) \(4 \times 1\) et \(1 \times 5\) ; (d) \(3 \times 3\) et \(3 \times 1\). Dans les cas définis, \(BA\) l'est-il ?

<details markdown="1">
<summary>Voir la réponse</summary>

| | \(AB\) | Taille | \(BA\) défini ? |
|---|---|---|---|
| (a) | oui (3 = 3) | \(2 \times 4\) | non (4 ≠ 2) |
| (b) | non (2 ≠ 3) | — | non (2 ≠ 3) |
| (c) | oui (1 = 1) | \(4 \times 5\) | non (5 ≠ 4) |
| (d) | oui (3 = 3) | \(3 \times 1\) | non (1 ≠ 3) |

</details>

## Exercice 3 – Un produit à la main

Avec \(A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}\) et \(B = \begin{pmatrix} 1 & 4 \\ 2 & 5 \end{pmatrix}\), calculer \(AB\), \(BA\) et \(A + B\). Conclure sur la commutativité.

<details markdown="1">
<summary>Voir la réponse</summary>

\(AB = \begin{pmatrix} 4 & 13 \\ 6 & 15 \end{pmatrix}\) (par exemple \(c_{12} = 2 \times 4 + 1 \times 5 = 13\)) ; \(BA = \begin{pmatrix} 2 & 13 \\ 4 & 17 \end{pmatrix}\) ; \(A + B = \begin{pmatrix} 3 & 5 \\ 2 & 8 \end{pmatrix}\). \(AB \neq BA\) : le produit n'est pas commutatif.

</details>

## Exercice 4 – Rectangulaires

Calculer \(CD\) et \(DC\) pour \(C = \begin{pmatrix} 1 & 2 & 0 \\ 3 & -1 & 4 \end{pmatrix}\) et \(D = \begin{pmatrix} 2 & 1 \\ 0 & 5 \\ -3 & 2 \end{pmatrix}\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(CD = \begin{pmatrix} 2 & 11 \\ -6 & 6 \end{pmatrix}\) (taille \(2 \times 2\)) ; \(DC = \begin{pmatrix} 5 & 3 & 4 \\ 15 & -5 & 20 \\ 3 & -8 & 8 \end{pmatrix}\) (taille \(3 \times 3\)).

</details>

## Exercice 5 – Coûts

Avec \(Q\) de l'exercice 1 et deux grilles de prix en euros (fictives) pour (RAM, SSD, écran) : \(P_1 = (30, 60, 110)\) et \(P_2 = (25, 70, 90)\), on range les prix en colonnes dans \(P' = \begin{pmatrix} 30 & 25 \\ 60 & 70 \\ 110 & 90 \end{pmatrix}\).

1. Quelle est la taille de \(Q P'\) ? Que représentent ses colonnes ?
2. Calculer \(Q P'\). Quel fournisseur est le moins cher pour chaque configuration ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(Q P'\) est \(3 \times 2\) : une ligne par configuration, une colonne par fournisseur.
2. \(Q P' = \begin{pmatrix} 200 & 185 \\ 340 & 300 \\ 460 & 420 \end{pmatrix}\). Moins cher : Bureautique → fournisseur 2, Développement → fournisseur 2, Graphisme → fournisseur 2 (égalité s'il y en a : au premier).

</details>

## Exercice 6 – Pas de simplification

Soit \(A = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}\) et \(B = \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}\). Calculer \(AB\). Peut-on en conclure que \(A = 0\) ou \(B = 0\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

\(AB = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}\), alors que ni \(A\) ni \(B\) n'est nulle : on ne peut pas « diviser » par une matrice non nulle.

</details>

## Exercice 7 – Puissances

1. Calculer \(U^2\), \(U^3\), \(U^4\) pour \(U = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\) et conjecturer \(U^n\).
2. Donner \(D^n\) pour \(D = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}\).
3. Calculer \(F^2, F^3, F^4, F^5\) pour \(F = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\) et lire les nombres de Fibonacci.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(U^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\), \(U^3 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}\), \(U^4 = \begin{pmatrix} 1 & 4 \\ 0 & 1 \end{pmatrix}\) : \(U^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}\).
2. \(D^n = \begin{pmatrix} 2^n & 0 \\ 0 & 3^n \end{pmatrix}\).
3. \(F^2 = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}\), \(F^3 = \begin{pmatrix} 3 & 2 \\ 2 & 1 \end{pmatrix}\), \(F^4 = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}\), \(F^5 = \begin{pmatrix} 8 & 5 \\ 5 & 3 \end{pmatrix}\). Les coefficients sont les nombres de Fibonacci 1, 1, 2, 3, 5, 8.

</details>

## Exercice 8 – Une identité fausse

Avec \(A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\) et \(B = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}\), calculer \((A + B)^2\) et \(A^2 + 2AB + B^2\). Sont-ils égaux ? Pourquoi ?

<details markdown="1">
<summary>Voir la réponse</summary>

\((A + B)^2 = \begin{pmatrix} 10 & 8 \\ 12 & 10 \end{pmatrix}\) ; \(A^2 + 2AB + B^2 = \begin{pmatrix} 16 & 8 \\ 12 & 4 \end{pmatrix}\). Ils diffèrent. En développant correctement : \((A + B)^2 = A^2 + AB + BA + B^2\), et \(AB \neq BA\), donc on ne peut pas regrouper en \(2AB\).

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Additionner deux matrices ;
- [ ] Multiplier une matrice par un réel ;
- [ ] Calculer un produit de matrices ;
- [ ] Donner la taille du produit avant de calculer ;
- [ ] Calculer une puissance d'une matrice carrée.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________
