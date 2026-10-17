# Exercices – Inverse et systèmes linéaires

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S14*

> [!NOTE]
> **Comment travailler.** Cherche d'abord **sur papier**, avec la méthode du cours : écris les étapes, pas seulement le résultat. Ouvre ensuite « Voir la réponse » pour te corriger. À l'épreuve, **aucune réponse sans justification** n'est complète.

## Exercice 1 – Vérifier un inverse

1. Vérifier que \(\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\) est l'inverse de \(\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\).
2. La matrice \(\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}\) est-elle l'inverse de \(\begin{pmatrix} \frac{1}{2} & 0 \\ 0 & \frac{1}{2} \end{pmatrix}\) ? Et \(\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\) a-t-elle pour inverse \(\begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}\) ?

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix} \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\) et le produit dans l'autre ordre donne \(\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\) : c'est \(I_2\).
2. \(\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2\) : oui. Pour la seconde : \(\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I_2\) : oui aussi.

</details>

## Exercice 2 – Écrire un système en matrices

Écrire sous la forme \(AX = B\) : (a) \(\begin{cases} 3x + 2y = 12 \\ x - y = 1 \end{cases}\) ; (b) \(\begin{cases} x + y + z = 6 \\ 2x - y + z = 3 \\ x + 2y - z = 2 \end{cases}\). Vérifier que \((x, y) = (2{,}8\ ;\ 1{,}8)\) est solution de (a) et que \((x, y, z) = (1, 2, 3)\) est solution de (b).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) \(\begin{pmatrix} 3 & 2 \\ 1 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 12 \\ 1 \end{pmatrix}\) ; (b) \(\begin{pmatrix} 1 & 1 & 1 \\ 2 & -1 & 1 \\ 1 & 2 & -1 \end{pmatrix}\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 6 \\ 3 \\ 2 \end{pmatrix}\).
Contrôles : \(3 \times 2{,}8 + 2 \times 1{,}8 = 12\) et \(2{,}8 - 1{,}8 = 1\) ✓ ; \(A\,\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} = \begin{pmatrix} 6 \\ 3 \\ 2 \end{pmatrix} = B\) ✓.

</details>

## Exercice 3 – Résoudre avec l'inverse

On donne \(A = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}\) et \(A^{-1} = \begin{pmatrix} 7 & -2 \\ -3 & 1 \end{pmatrix}\). Résoudre \(\begin{cases} x + 2y = 5 \\ 3x + 7y = 16 \end{cases}\).

<details markdown="1">
<summary>Voir la réponse</summary>

\(X = A^{-1}B = \begin{pmatrix} 7 & -2 \\ -3 & 1 \end{pmatrix}\begin{pmatrix} 5 \\ 16 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}\) : \(x = 3\), \(y = 1\). Contrôle : \(x + 2y = 5\) et \(3x + 7y = 16\) ✓.

</details>

## Exercice 4 – Méthode des lignes (2 × 2)

Calculer par la méthode itérative l'inverse de \(\begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}\), puis de \(\begin{pmatrix} 0 & 2 \\ 3 & 1 \end{pmatrix}\).

<details markdown="1">
<summary>Voir la réponse</summary>

Matrice de départ \([A \mid I]\) :

\[
\left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 3 & 7 & 0 & 1 \end{array}\right)
\]

\(L_2 \leftarrow L_2 - 3 L_1\) :

\[
\left(\begin{array}{cc|cc} 1 & 2 & 1 & 0 \\ 0 & 1 & -3 & 1 \end{array}\right)
\]

\(L_1 \leftarrow L_1 - 2 L_2\) :

\[
\left(\begin{array}{cc|cc} 1 & 0 & 7 & -2 \\ 0 & 1 & -3 & 1 \end{array}\right)
\]


Pour la seconde matrice : \(A^{-1} = \begin{pmatrix} -\frac{1}{6} & \frac{1}{3} \\ \frac{1}{2} & 0 \end{pmatrix}\).

</details>

## Exercice 5 – Méthode des lignes (3 × 3)

Calculer l'inverse de \(A = \begin{pmatrix} 1 & 0 & 2 \\ 0 & 1 & 3 \\ 1 & 1 & 1 \end{pmatrix}\) et le vérifier.

<details markdown="1">
<summary>Voir la réponse</summary>

Matrice de départ \([A \mid I]\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & 1 & 3 & 0 & 1 & 0 \\ 1 & 1 & 1 & 0 & 0 & 1 \end{array}\right)
\]

\(L_3 \leftarrow L_3 - L_1\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & 1 & 3 & 0 & 1 & 0 \\ 0 & 1 & -1 & -1 & 0 & 1 \end{array}\right)
\]

\(L_3 \leftarrow L_3 - L_2\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & 1 & 3 & 0 & 1 & 0 \\ 0 & 0 & -4 & -1 & -1 & 1 \end{array}\right)
\]

\(L_3 \leftarrow -\frac{1}{4}\,L_3\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & 2 & 1 & 0 & 0 \\ 0 & 1 & 3 & 0 & 1 & 0 \\ 0 & 0 & 1 & \frac{1}{4} & \frac{1}{4} & -\frac{1}{4} \end{array}\right)
\]

\(L_1 \leftarrow L_1 - 2 L_3\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\ 0 & 1 & 3 & 0 & 1 & 0 \\ 0 & 0 & 1 & \frac{1}{4} & \frac{1}{4} & -\frac{1}{4} \end{array}\right)
\]

\(L_2 \leftarrow L_2 - 3 L_3\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\ 0 & 1 & 0 & -\frac{3}{4} & \frac{1}{4} & \frac{3}{4} \\ 0 & 0 & 1 & \frac{1}{4} & \frac{1}{4} & -\frac{1}{4} \end{array}\right)
\]


\(A^{-1} = \begin{pmatrix} \frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\ -\frac{3}{4} & \frac{1}{4} & \frac{3}{4} \\ \frac{1}{4} & \frac{1}{4} & -\frac{1}{4} \end{pmatrix}\). Vérification : \(A A^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\).

</details>

## Exercice 6 – Détecter une matrice non inversible

Dire, en appliquant la méthode, si les matrices suivantes sont inversibles : (a) \(\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}\) ; (b) \(\begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 0 & 1 \end{pmatrix}\) ; (c) \(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\).

<details markdown="1">
<summary>Voir la réponse</summary>

(a) Non : la ligne 2 est le double de la ligne 1 ; après \(L_2 \leftarrow L_2 - 2L_1\) on obtient une ligne de zéros à gauche.
(b) Non : la ligne 2 est le double de la ligne 1 (non inversible, confirmé par la méthode).
(c) Oui : \(\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\) est son propre inverse (échanger deux lignes deux fois) ; la méthode demande un échange \(L_1 \leftrightarrow L_2\).

</details>

## Exercice 7 – Facturation

Un prestataire facture trois types d'intervention (prix unitaires \(x\), \(y\), \(z\) inconnus) :

- 2 interventions de type 1, 1 de type 2 et 1 de type 3 : 31 € ;
- 1 de type 1, 3 de type 2 et 2 de type 3 : 58 € ;
- 3 de type 1, 2 de type 2 et 1 de type 3 : 39 €.

1. Écrire \(AX = B\).
2. Sachant que \(A^{-1} = \frac{1}{4}\begin{pmatrix} 1 & -1 & 1 \\ -5 & 1 & 3 \\ 7 & 1 & -5 \end{pmatrix}\) (à vérifier), trouver les prix.

<details markdown="1">
<summary>Voir la réponse</summary>

1. \(\begin{pmatrix} 2 & 1 & 1 \\ 1 & 3 & 2 \\ 3 & 2 & 1 \end{pmatrix}X = \begin{pmatrix} 31 \\ 58 \\ 39 \end{pmatrix}\).
2. Vérification de l'inverse : \(A A^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\). Puis \(X = A^{-1}B = \begin{pmatrix} 3 \\ 5 \\ 20 \end{pmatrix}\) : prix 3 €, 5 € et 20 €.

</details>

## Exercice 8 – Piège de l'ordre

Pour \(AX = B\) avec \(A\) inversible, un étudiant écrit \(X = BA^{-1}\). Pour \(A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\) et \(B = \begin{pmatrix} 7 \\ 18 \end{pmatrix}\) (colonne), quelle est la taille de \(B A^{-1}\) ? Conclure.

<details markdown="1">
<summary>Voir la réponse</summary>

\(B\) est \(2 \times 1\) et \(A^{-1}\) est \(2 \times 2\) : le produit \(B A^{-1}\) n'est pas défini (1 colonne contre 2 lignes). La bonne écriture est \(X = A^{-1}B\), de taille \(2 \times 1\).

</details>


## Je sais faire

Coche honnêtement ; ce que tu ne coches pas se reprend avant la séance suivante.

- [ ] Vérifier qu'une matrice est l'inverse d'une autre ;
- [ ] Poser un système sous la forme \(AX = B\) ;
- [ ] Résoudre un système de Cramer ;
- [ ] Appliquer la méthode des lignes pour inverser ;
- [ ] Détecter qu'une matrice n'est pas inversible.

**Ce que je dois reprendre :** ______________________

**Ma question à poser à l'enseignant :** ______________________
