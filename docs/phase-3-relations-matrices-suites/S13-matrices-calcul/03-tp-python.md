---
render_macros: true
---

# TP Python – Calcul matriciel en Python

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S13*

> [!NOTE]
> **Comment ce TP fonctionne.** Chaque exercice a un éditeur Python intégré à la page (il s'exécute dans ton navigateur, rien à installer). Avant de lancer, écris sur ta feuille ce que tu **anticipes** (« J'anticipe »). Puis lance et compare. Le bouton **Valider** exécute des tests : un test réussi ne dispense pas de **comprendre** pourquoi.

Une matrice est une liste de listes : `[[1, 2], [3, 4]]` a 2 lignes et 2 colonnes ; `a[i][j]` est le coefficient de la ligne `i` et de la colonne `j` (indices à partir de 0).

## Exercice A – Somme et produit par un réel

Écris `somme(a, b)` (matrices de même taille) et `produit_reel(k, a)`. Les fonctions renvoient de **nouvelles** matrices.

**J'anticipe.** Quelle est la matrice de `somme([[1, 2]], [[3, 4]])` ?

{{ IDE('somme_matrices', MAX="+") }}

## Exercice B – Produit

Écris `produit(a, b)` qui renvoie le produit des matrices `a` et `b`, ou `None` si les tailles sont incompatibles (colonnes de `a` différent des lignes de `b`).

**Je comprends.** Combien de boucles imbriquées faut-il ? Que représente la boucle la plus intérieure ?

{{ IDE('produit_matrices', MAX="+") }}

## Exercice C – Identité et puissance

Écris `identite(n)` et `puissance(a, p)` (matrice carrée `a`, entier `p` ≥ 0, `puissance(a, 0)` est l'identité). Utilise `produit` (recopié dans l'éditeur).

{{ IDE('puissance_matrice', MAX="+") }}

## Exercice D – Fibonacci par les matrices

Écris `fibonacci(n)` (\(n \ge 1\)) qui renvoie \(F_n\) en lisant un coefficient de \(\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n\). `fibonacci(10)` doit donner 55.

{{ IDE('fibonacci_matriciel', MAX="+") }}

## Exercice E – Coût des configurations

Écris `couts(quantites, prix)` qui renvoie la liste des coûts de chaque configuration (`quantites` : matrice des quantités, `prix` : liste des prix unitaires).

{{ IDE('couts', MAX="+") }}
