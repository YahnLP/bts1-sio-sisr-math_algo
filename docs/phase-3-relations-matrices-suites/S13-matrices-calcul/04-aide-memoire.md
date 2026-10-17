# Aide-mémoire – Matrices : opérations

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S13*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Matrices

- Taille \(m \times n\) : \(m\) lignes, \(n\) colonnes ; \(a_{ij}\) : ligne \(i\), colonne \(j\).
- **Somme** : même taille, coefficient par coefficient. **Produit par \(k\)** : chaque coefficient.
- **Produit** \(AB\) : \((m \times n)(n \times p) = m \times p\) ;
  \(c_{ij} = \sum_{k} a_{ik}\,b_{kj}\).
- \(AB \neq BA\) en général ; \(AB = 0\) n'implique pas \(A = 0\) ou \(B = 0\).
- \((AB)C = A(BC)\) ; \(A(B + C) = AB + AC\) ; \(AI = IA = A\).
- \(A^n\) : seulement pour une matrice carrée ; \(A^0 = I\).

| Exemple | Résultat |
|---|---|
| Diagonale | \(\begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}^n = \begin{pmatrix} a^n & 0 \\ 0 & b^n \end{pmatrix}\) |
| Fibonacci | \(\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix}\) |

## Python

```python
a = [[1, 2], [3, 4]]   # a[i][j]
```
