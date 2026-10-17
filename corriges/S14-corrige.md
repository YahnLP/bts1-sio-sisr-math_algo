# Corrigé S14

## Exercices

Réponses détaillées dans les encadrés de la feuille d'exercices. Résultats clés :

- \(\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}^{-1} = \begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}\) ; \(\begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}^{-1} = \begin{pmatrix} 7 & -2 \\ -3 & 1 \end{pmatrix}\).
- \(\begin{pmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{pmatrix}^{-1} = \begin{pmatrix} -24 & 18 & 5 \\ 20 & -15 & -4 \\ -5 & 4 & 1 \end{pmatrix}\).
- Prix des commandes : 3 €, 5 €, 20 €.

## TP Python – solutions

```python
from fractions import Fraction

def identite(n):
    m = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(Fraction(1 if i == j else 0))
        m.append(ligne)
    return m

def produit(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = Fraction(0)
            for k in range(len(b)):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat
```

```python
from fractions import Fraction

def identite(n):
    m = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(Fraction(1 if i == j else 0))
        m.append(ligne)
    return m

def produit(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = Fraction(0)
            for k in range(len(b)):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def est_inverse(a, b):
    n = len(a)
    return produit(a, b) == identite(n) and produit(b, a) == identite(n)
```

```python
from fractions import Fraction

def identite(n):
    m = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(Fraction(1 if i == j else 0))
        m.append(ligne)
    return m

def produit(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = Fraction(0)
            for k in range(len(b)):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def inverse(a):
    """Inverse de a par la méthode des lignes, ou None si a n'est pas inversible."""
    n = len(a)
    g = []
    for i in range(n):
        g.append([Fraction(x) for x in a[i]] + identite(n)[i])
    for j in range(n):
        p = None
        for i in range(j, n):
            if g[i][j] != 0:
                p = i
                break
        if p is None:
            return None
        g[j], g[p] = g[p], g[j]
        pivot = g[j][j]
        g[j] = [x / pivot for x in g[j]]
        for i in range(n):
            if i != j and g[i][j] != 0:
                c = g[i][j]
                g[i] = [x - c * y for x, y in zip(g[i], g[j])]
    return [ligne[n:] for ligne in g]
```

```python
from fractions import Fraction

def identite(n):
    m = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(Fraction(1 if i == j else 0))
        m.append(ligne)
    return m

def produit(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = Fraction(0)
            for k in range(len(b)):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def inverse(a):
    """Inverse de a par la méthode des lignes, ou None si a n'est pas inversible."""
    n = len(a)
    g = []
    for i in range(n):
        g.append([Fraction(x) for x in a[i]] + identite(n)[i])
    for j in range(n):
        p = None
        for i in range(j, n):
            if g[i][j] != 0:
                p = i
                break
        if p is None:
            return None
        g[j], g[p] = g[p], g[j]
        pivot = g[j][j]
        g[j] = [x / pivot for x in g[j]]
        for i in range(n):
            if i != j and g[i][j] != 0:
                c = g[i][j]
                g[i] = [x - c * y for x, y in zip(g[i], g[j])]
    return [ligne[n:] for ligne in g]

def resoudre(a, b):
    """Solution de AX = B (liste de Fraction), ou None."""
    ai = inverse(a)
    if ai is None:
        return None
    x = []
    for i in range(len(ai)):
        s = Fraction(0)
        for k in range(len(b)):
            s = s + ai[i][k] * b[k]
        x.append(s)
    return x
```
