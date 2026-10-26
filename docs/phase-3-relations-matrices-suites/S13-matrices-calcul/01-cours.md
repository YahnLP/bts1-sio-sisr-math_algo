# Cours – Matrices : définitions et opérations

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S13 – à lire avant les [exercices](02-exercices.md)*

> [!NOTE] Ce que tu dois savoir déjà
> - **Prérequis :** S12 (tableaux à deux dimensions) ; calcul numérique de base.
> - **Outils :** Papier, calculatrice, éditeur Python intégré au site

## À la fin de ce cours tu sauras

- [ ] **Lire** une matrice comme un tableau de nombres représentant une situation ;
- [ ] **Calculer** une somme, un produit par un réel, un produit de deux matrices ;
- [ ] **Vérifier** la compatibilité des tailles avant un produit ;
- [ ] **Expliquer** que le produit n'est pas commutatif et qu'on ne « divise » pas ;
- [ ] **Calculer** une puissance d'une matrice carrée et la matrice identité.

## I. Qu'est-ce qu'une matrice ?

Une **matrice** de taille \(m \times n\) est un tableau de nombres à \(m\) **lignes** et \(n\) **colonnes**. Le coefficient de la ligne \(i\) et de la colonne \(j\) se note \(a_{ij}\) (la ligne d'abord).

**Situation.** Trois configurations de postes sont décrites par leurs composants (quantités) ; les prix unitaires sont fictifs.

| Configuration | barrettes de RAM (8 Go) | SSD (500 Go) | écran |
|---|---|---|---|
| Bureautique | 1 | 1 | 1 |
| Développement | 2 | 1 | 2 |
| Graphisme | 4 | 2 | 2 |

La matrice des quantités est \(Q = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 2 \\ 4 & 2 & 2 \end{pmatrix}\), de taille \(3 \times 3\). Le coefficient \(q_{23}\) (ligne 2, colonne 3) vaut 2 : deux écrans pour la configuration « Développement ».

| Type | Définition | Exemple |
|---|---|---|
| **Matrice carrée** | autant de lignes que de colonnes | \(\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}\) |
| **Matrice ligne / colonne** | une seule ligne / une seule colonne | prix : \(\begin{pmatrix} 30 \\ 60 \\ 110 \end{pmatrix}\) |
| **Matrice nulle** | tous les coefficients valent 0 | \(\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}\) |
| **Matrice identité** \(I_n\) | carrée, 1 sur la diagonale, 0 ailleurs | \(I_3 = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\) |

## II. Somme et produit par un réel

On ne peut additionner que deux matrices de **même taille**, coefficient par coefficient. Le produit par un réel \(k\) multiplie **chaque** coefficient.

\[
\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} + \begin{pmatrix} 1 & 4 \\ 2 & 5 \end{pmatrix} = \begin{pmatrix} 3 & 5 \\ 2 & 8 \end{pmatrix} \qquad 3 \times \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} = \begin{pmatrix} 6 & 3 \\ 0 & 9 \end{pmatrix}
\]

Ces opérations se comportent comme celles des nombres : commutativité de la somme, distributivité de \(k\) sur la somme.

## III. Produit de deux matrices

Le produit \(A \times B\) n'existe que si le **nombre de colonnes de \(A\)** est égal au **nombre de lignes de \(B\)**. Si \(A\) est de taille \(m \times n\) et \(B\) de taille \(n \times p\), alors \(AB\) est de taille \(m \times p\).

\[
(m \times \underline{n})(\underline{n} \times p) \longrightarrow m \times p
\]

Le coefficient de la ligne \(i\) et de la colonne \(j\) de \(AB\) est :

\[
c_{ij} = a_{i1}\,b_{1j} + a_{i2}\,b_{2j} + \dots + a_{in}\,b_{nj}
\]

(on multiplie la ligne \(i\) de \(A\) par la colonne \(j\) de \(B\), terme à terme, puis on additionne).

**Exemple (coût des configurations).** \(Q\) est \(3 \times 3\) et \(P\) est \(3 \times 1\) : le produit existe et il est de taille \(3 \times 1\).

\[
Q P = \begin{pmatrix} 1 & 1 & 1 \\ 2 & 1 & 2 \\ 4 & 2 & 2 \end{pmatrix} \begin{pmatrix} 30 \\ 60 \\ 110 \end{pmatrix} = \begin{pmatrix} 200 \\ 340 \\ 460 \end{pmatrix}
\]

Détail de la première ligne : \(1 \times 30 + 1 \times 60 + 1 \times 110 = 200\). Pour la troisième : \(4 \times 30 + 2 \times 60 + 2 \times 110 = 460\). Le poste « Graphisme » coûte donc 460 €.

**Exemple 2 × 3 par 3 × 2.** Avec \(C = \begin{pmatrix} 1 & 2 & 0 \\ 3 & -1 & 4 \end{pmatrix}\) et \(D = \begin{pmatrix} 2 & 1 \\ 0 & 5 \\ -3 & 2 \end{pmatrix}\), \(CD\) est \(2 \times 2\) :

\[
CD = \begin{pmatrix} 2 & 11 \\ -6 & 6 \end{pmatrix} \qquad (c_{12} = 1 \times 1 + 2 \times 5 + 0 \times 2 = 11)
\]

et \(DC\) existe aussi, mais de taille \(3 \times 3\) : \(CD \neq DC\), ne serait-ce que par la taille.

### Ce qui change par rapport aux nombres

> [!WARNING]
> **Le produit n'est pas commutatif.** Avec \(A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}\) et \(B = \begin{pmatrix} 1 & 4 \\ 2 & 5 \end{pmatrix}\) :
> \(AB = \begin{pmatrix} 4 & 13 \\ 6 & 15 \end{pmatrix}\) mais \(BA = \begin{pmatrix} 2 & 13 \\ 4 & 17 \end{pmatrix}\).
>
> **On peut avoir \(AB = 0\) sans que \(A\) ni \(B\) soit nulle.** Par exemple \(\begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}\). On ne peut donc pas « simplifier » : de \(AB = AC\) on ne déduit pas \(B = C\), et on ne « divise » pas par une matrice (l'inverse, quand il existe, est l'objet de S14).

Ce qui reste vrai : \((AB)C = A(BC)\) (associativité), \(A(B + C) = AB + AC\), et \(A I = I A = A\) pour la matrice identité de même taille.

## IV. Puissances d'une matrice carrée

\(A^n = A \times A \times \dots \times A\) (\(n\) facteurs), \(A^0 = I\). Seules les matrices **carrées** ont des puissances.

**Matrice diagonale.** Pour \(D = \begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}\) : \(D^2 = \begin{pmatrix} 4 & 0 \\ 0 & 9 \end{pmatrix}\), \(D^3 = \begin{pmatrix} 8 & 0 \\ 0 & 27 \end{pmatrix}\), et en général \(D^n = \begin{pmatrix} 2^n & 0 \\ 0 & 3^n \end{pmatrix}\) (vérifié jusqu'à \(n = 11\)).

**Une matrice triangulaire.** Pour \(U = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}\) : \(U^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}\), \(U^3 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}\). On conjecture \(U^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}\) (vérifié pour \(n\) de 0 à 20).

**Les nombres de Fibonacci.** Soit \(F = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}\). Ses puissances contiennent la suite \(1, 1, 2, 3, 5, 8, \dots\) :

\[
F^{10} = \begin{pmatrix} 89 & 55 \\ 55 & 34 \end{pmatrix} \quad \text{donc } F_{10} = 55,\ F_{11} = 89,\ F_9 = 34
\]

En général \(F^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}\) (contrôlé pour \(n\) de 1 à 24).

**Un processus discret.** Un serveur est soit *disponible* (état 1), soit *en panne* (état 2). Chaque jour, s'il est disponible il le reste avec la probabilité 0,9 ; s'il est en panne il redevient disponible avec la probabilité 0,4. On range ces probabilités dans la matrice de transition (une ligne = un état de départ, la somme d'une ligne vaut 1) :

\[
P = \begin{pmatrix} 0{,}9 & 0{,}1 \\ 0{,}4 & 0{,}6 \end{pmatrix}
\]

Si le serveur est disponible aujourd'hui, la ligne \(X_0 = (1\ \ 0)\) décrit la situation. La répartition au jour \(n\) est \(X_n = X_0 P^n\) :

\[
X_1 = (0{,}9\ \ 0{,}1), \quad X_2 = X_0 P^2 = (0{,}85\ \ 0{,}15), \quad X_3 = (0{,}825\ \ 0{,}175)
\]

Après quelques dizaines de jours, \(X_n\) se stabilise autour de \((0{,}8\ \ 0{,}2)\) : à long terme le serveur est disponible 80 % du temps, quel que soit l'état de départ. C'est l'intérêt des puissances de matrices : décrire l'évolution d'un système d'un pas au suivant.

> [!NOTE]
> **Calculatrice.** Le programme autorise la calculatrice pour les sommes, produits et puissances de matrices. Les calculs à la main servent à **comprendre** ; pour un exercice avec une calculatrice, on écrit les matrices, on indique l'opération et on recopie le résultat.

## À retenir

- Matrice \(m \times n\) : \(m\) lignes, \(n\) colonnes ; \(a_{ij}\) = ligne \(i\), colonne \(j\).
- Somme : même taille. Produit \(AB\) : colonnes de \(A\) = lignes de \(B\), résultat \(m \times p\).
- \(AB \neq BA\) en général ; \(AB = 0\) n'implique pas \(A = 0\) ou \(B = 0\).
- \(A I = I A = A\) ; \((AB)C = A(BC)\) ; puissances pour les matrices carrées.
