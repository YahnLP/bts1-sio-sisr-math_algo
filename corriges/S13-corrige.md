# Corrigé S13

## Exercices

Réponses détaillées dans les encadrés de la feuille d'exercices. Résultats clés :

- Coûts des configurations : \begin{pmatrix} 200 \\ 340 \\ 460 \end{pmatrix} (euros fictifs).
- \(AB = \begin{pmatrix} 4 & 13 \\ 6 & 15 \end{pmatrix}\) et \(BA = \begin{pmatrix} 2 & 13 \\ 4 & 17 \end{pmatrix}\).
- \(F^{10} = \begin{pmatrix} 89 & 55 \\ 55 & 34 \end{pmatrix}\).

## TP Python – solutions

```python
def somme(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(a[0])):
            ligne.append(a[i][j] + b[i][j])
        resultat.append(ligne)
    return resultat

def produit_reel(k, a):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(a[0])):
            ligne.append(k * a[i][j])
        resultat.append(ligne)
    return resultat
```

```python
def produit(a, b):
    """Produit de a (m x n) par b (n x p), ou None si les tailles sont incompatibles."""
    if len(a[0]) != len(b):
        return None
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat
```

```python
def produit(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def identite(n):
    m = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(1 if i == j else 0)
        m.append(ligne)
    return m

def puissance(a, p):
    r = identite(len(a))
    for _ in range(p):
        r = produit(r, a)
    return r
```

```python
def produit(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def fibonacci(n):
    """F(n) avec F(1) = F(2) = 1, par la puissance n de [[1, 1], [1, 0]]."""
    r = [[1, 0], [0, 1]]
    for _ in range(n):
        r = produit(r, [[1, 1], [1, 0]])
    return r[0][1]
```

```python
def couts(quantites, prix):
    resultat = []
    for ligne in quantites:
        total = 0
        for k in range(len(prix)):
            total = total + ligne[k] * prix[k]
        resultat.append(total)
    return resultat
```
