# Aide-mémoire – Inverse et systèmes

*BTS SIO SISR 1re année – Mathématiques pour l'informatique – S14*

> Un mot ou un sigle inconnu ? Passe la souris dessus, ou ouvre le [glossaire](../../ressources/glossaire.md).

## Inverse

- \(A\) carrée est inversible s'il existe \(A^{-1}\) avec \(A A^{-1} = A^{-1} A = I\).
- Vérification : calculer le produit.

## Système AX = B

- Si \(A\) est inversible : \(X = A^{-1}B\) (produit **à gauche**), solution unique.
- Sinon : aucune solution ou une infinité.

## Méthode des lignes

Partir de \([A \mid I]\), arriver à \([I \mid A^{-1}]\).

| Opération | Notation |
|---|---|
| Multiplier une ligne par \(k \neq 0\) | \(L_i \leftarrow k\,L_i\) |
| Ajouter un multiple d'une ligne | \(L_i \leftarrow L_i + k\,L_j\) |
| Échanger deux lignes | \(L_i \leftrightarrow L_j\) |

Pour chaque colonne : pivot **1** sur la diagonale, puis **0** ailleurs. Une ligne de zéros à gauche : non inversible.

## Python

```python
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 6)   # Fraction(1, 2), exact
```
