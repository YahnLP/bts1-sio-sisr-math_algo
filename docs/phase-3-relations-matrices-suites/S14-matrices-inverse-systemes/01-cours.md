# Cours – Matrice inverse et résolution de systèmes

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S14 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S13 (produit de matrices).
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Définir** l'inverse d'une matrice carrée et **vérifier** qu'une matrice en est l'inverse ;
- [ ] **Écrire** un système linéaire sous la forme \(AX = B\) ;
- [ ] **Résoudre** un système de Cramer avec \(X = A^{-1}B\) ;
- [ ] **Calculer** l'inverse d'une matrice par la méthode itérative (opérations sur les lignes) ;
- [ ] **Reconnaître** une matrice non inversible au cours du calcul.

## I. L'inverse d'une matrice

Pour les nombres, diviser par \(a\) revient à multiplier par \(a^{-1}\). Pour les matrices, on ne « divise » pas (S13), mais certaines matrices **carrées** ont un **inverse**.

Une matrice carrée \(A\) d'ordre \(n\) est **inversible** s'il existe une matrice \(A^{-1}\) telle que :

\[
A\,A^{-1} = A^{-1}A = I_n
\]

**Exemple.** Pour \(A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\), on a \(A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\). Vérification :

\[
A\,A^{-1} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \qquad A^{-1}A = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
\]

Toutes les matrices carrées ne sont pas inversibles. Une matrice **non inversible** ne peut être « annulée » par aucune autre : par exemple \(\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}\), dont la seconde ligne est le double de la première (partie V).

## II. Un système sous forme matricielle

Un système linéaire s'écrit \(AX = B\), où \(A\) contient les coefficients, \(X\) les inconnues et \(B\) les seconds membres.

**Exemple.** Trois commandes de matériel réseau (prix **inconnus** en euros) : un câble (\(x\)), une prise (\(y\)) et un switch (\(z\)).

| Commande | Câbles | Prises | Switchs | Total |
|---|---|---|---|---|
| 1 | 2 | 1 | 1 | 31 € |
| 2 | 1 | 3 | 2 | 58 € |
| 3 | 3 | 2 | 1 | 39 € |

\[
\begin{pmatrix} 2 & 1 & 1 \\ 1 & 3 & 2 \\ 3 & 2 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 31 \\ 58 \\ 39 \end{pmatrix} \qquad\text{soit}\qquad AX = B
\]

## III. Résoudre avec l'inverse

Si \(A\) est inversible, on multiplie **à gauche** les deux membres par \(A^{-1}\) :

\[
AX = B \;\Longrightarrow\; A^{-1}AX = A^{-1}B \;\Longrightarrow\; X = A^{-1}B
\]

Le système admet alors **une seule solution** : on dit que c'est un **système de Cramer**.

> [!WARNING]
> Le produit n'est pas commutatif : c'est \(X = A^{-1}B\) et **non** \(X = B A^{-1}\) (ce produit n'a d'ailleurs pas la bonne taille pour une colonne \(B\)).

**Exemple 2 × 2.** \(\begin{cases} 2x + y = 7 \\ 5x + 3y = 18 \end{cases}\), soit \(\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}X = \begin{pmatrix} 7 \\ 18 \end{pmatrix}\). Avec \(A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\) :

\[
X = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix} \begin{pmatrix} 7 \\ 18 \end{pmatrix} = \begin{pmatrix} 3 \\ 1 \end{pmatrix}
\]

Donc \(x = 3\), \(y = 1\). Contrôle : \(2 \times 3 + 1 = 7\) et \(5 \times 3 + 3 \times 1 = 18\) ✓.

**Exemple 3 × 3** (les commandes de câbles, prises, switchs). La méthode de la partie IV donne \(A^{-1} = \dfrac{1}{4}\begin{pmatrix} 1 & -1 & 1 \\ -5 & 1 & 3 \\ 7 & 1 & -5 \end{pmatrix}\) (à vérifier : \(A A^{-1} = I\) ). Alors

\[
X = A^{-1}B = \begin{pmatrix} 3 \\ 5 \\ 20 \end{pmatrix}
\]

Un câble coûte 3 €, une prise 5 € et un switch 20 €.

## IV. Calculer l'inverse : la méthode itérative

On écrit \(A\) et la matrice identité **côte à côte** : \([A \mid I]\). On effectue sur les **lignes** des opérations autorisées jusqu'à transformer \(A\) en \(I\). Ce qui se trouve alors à droite est \(A^{-1}\) : \([I \mid A^{-1}]\).

Opérations autorisées sur les lignes :

| Opération | Notation |
|---|---|
| Multiplier une ligne par un nombre **non nul** | \(L_i \leftarrow k\,L_i\) |
| Ajouter à une ligne un multiple d'une autre | \(L_i \leftarrow L_i + k\,L_j\) |
| Échanger deux lignes | \(L_i \leftrightarrow L_j\) |

**Stratégie**, colonne par colonne : on obtient un **1** sur la diagonale (pivot), puis des **0** dans le reste de la colonne.

**Exemple 1.** \(A = \begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}\).

Matrice de départ \([A \mid I]\) :

\[
\left(\begin{array}{cc|cc} 2 & 1 & 1 & 0 \\ 5 & 3 & 0 & 1 \end{array}\right)
\]

\(L_1 \leftarrow \frac{1}{2}\,L_1\) :

\[
\left(\begin{array}{cc|cc} 1 & \frac{1}{2} & \frac{1}{2} & 0 \\ 5 & 3 & 0 & 1 \end{array}\right)
\]

\(L_2 \leftarrow L_2 - 5 L_1\) :

\[
\left(\begin{array}{cc|cc} 1 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & \frac{1}{2} & -\frac{5}{2} & 1 \end{array}\right)
\]

\(L_2 \leftarrow 2\,L_2\) :

\[
\left(\begin{array}{cc|cc} 1 & \frac{1}{2} & \frac{1}{2} & 0 \\ 0 & 1 & -5 & 2 \end{array}\right)
\]

\(L_1 \leftarrow L_1 - \frac{1}{2} L_2\) :

\[
\left(\begin{array}{cc|cc} 1 & 0 & 3 & -1 \\ 0 & 1 & -5 & 2 \end{array}\right)
\]


Donc \(A^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\), conforme à la partie I.

**Exemple 2.** \(A = \begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}\).

Matrice de départ \([A \mid I]\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & 4 & 0 & 1 & 0 \\ 5 & 6 & 0 & 0 & 0 & 1 \end{array}\right)
\]

\(L_3 \leftarrow L_3 - 5 L_1\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 2 & 3 & 1 & 0 & 0 \\ 0 & 1 & 4 & 0 & 1 & 0 \\ 0 & -4 & -15 & -5 & 0 & 1 \end{array}\right)
\]

\(L_1 \leftarrow L_1 - 2 L_2\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & -5 & 1 & -2 & 0 \\ 0 & 1 & 4 & 0 & 1 & 0 \\ 0 & -4 & -15 & -5 & 0 & 1 \end{array}\right)
\]

\(L_3 \leftarrow L_3 + 4 L_2\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & -5 & 1 & -2 & 0 \\ 0 & 1 & 4 & 0 & 1 & 0 \\ 0 & 0 & 1 & -5 & 4 & 1 \end{array}\right)
\]

\(L_1 \leftarrow L_1 + 5 L_3\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & -24 & 18 & 5 \\ 0 & 1 & 4 & 0 & 1 & 0 \\ 0 & 0 & 1 & -5 & 4 & 1 \end{array}\right)
\]

\(L_2 \leftarrow L_2 - 4 L_3\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & 0 & -24 & 18 & 5 \\ 0 & 1 & 0 & 20 & -15 & -4 \\ 0 & 0 & 1 & -5 & 4 & 1 \end{array}\right)
\]


D'où \(A^{-1} = \begin{pmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{pmatrix}\). Vérification par le produit : \(A A^{-1} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\).

> [!NOTE]
> **Toujours vérifier.** Un calcul d'inverse à la main comporte des risques d'erreur ; on contrôle avec \(A A^{-1} = I\) (la calculatrice ou Python le font immédiatement).

## V. Quand la matrice n'est pas inversible

Si, au cours de la méthode, on obtient une **ligne de zéros** à gauche (ou si aucun pivot non nul n'est disponible dans une colonne), la matrice **n'est pas inversible**.

**Exemple.** \(A = \begin{pmatrix} 1 & 1 & 1 \\ 1 & 2 & 3 \\ 2 & 3 & 4 \end{pmatrix}\) (la ligne 3 est la somme des lignes 1 et 2).

Matrice de départ \([A \mid I]\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 1 & 2 & 3 & 0 & 1 & 0 \\ 2 & 3 & 4 & 0 & 0 & 1 \end{array}\right)
\]

\(L_2 \leftarrow L_2 - L_1\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 1 & 2 & -1 & 1 & 0 \\ 2 & 3 & 4 & 0 & 0 & 1 \end{array}\right)
\]

\(L_3 \leftarrow L_3 - 2 L_1\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 1 & 1 & 1 & 0 & 0 \\ 0 & 1 & 2 & -1 & 1 & 0 \\ 0 & 1 & 2 & -2 & 0 & 1 \end{array}\right)
\]

\(L_1 \leftarrow L_1 - L_2\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & -1 & 2 & -1 & 0 \\ 0 & 1 & 2 & -1 & 1 & 0 \\ 0 & 1 & 2 & -2 & 0 & 1 \end{array}\right)
\]

\(L_3 \leftarrow L_3 - L_2\) :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & -1 & 2 & -1 & 0 \\ 0 & 1 & 2 & -1 & 1 & 0 \\ 0 & 0 & 0 & -1 & -1 & 1 \end{array}\right)
\]

Colonne 3 : aucun pivot non nul sous la diagonale — \(A\) n'est pas inversible :

\[
\left(\begin{array}{ccc|ccc} 1 & 0 & -1 & 2 & -1 & 0 \\ 0 & 1 & 2 & -1 & 1 & 0 \\ 0 & 0 & 0 & -1 & -1 & 1 \end{array}\right)
\]


Le système \(AX = B\) n'est alors pas de Cramer : il a soit **aucune** solution, soit une **infinité**. Exemple : \(\begin{cases} x + 2y = 3 \\ 2x + 4y = 6 \end{cases}\) a une infinité de solutions (la seconde équation est le double de la première), tandis que \(\begin{cases} x + 2y = 3 \\ 2x + 4y = 7 \end{cases}\) n'en a aucune (la seconde donnerait \(x + 2y = 3{,}5\)).

> [!NOTE]
> Le programme n'utilise ni le déterminant ni de critère théorique d'inversibilité : c'est le **déroulement de la méthode** qui permet de conclure.

## À retenir

- \(A\) est inversible s'il existe \(A^{-1}\) avec \(A A^{-1} = A^{-1}A = I\) ; il faut une matrice carrée.
- Un système s'écrit \(AX = B\) ; si \(A\) est inversible, \(X = A^{-1}B\) (produit **à gauche**).
- Méthode : partir de \([A \mid I]\), arriver à \([I \mid A^{-1}]\) par des opérations sur les lignes.
- Ligne de zéros : \(A\) n'est pas inversible.
- Toujours vérifier : \(A A^{-1} = I\) ; reporter la solution dans les équations.
