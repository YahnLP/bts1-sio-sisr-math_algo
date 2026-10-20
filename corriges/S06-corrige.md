# Corrigé S06

## Exercices

1. Premiers : 53, 59, 97, 101, 223. Composés : le reste.
2. 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59.
3. Voir le ​tableau de l'énoncé.
4. 24 ; 11 ; 60.
5. 6 et 1260 ; 36 et 7 560.
6. 997 est premier (restes non nuls pour les premiers ≤ 31).
7. 3233 = 53 × 61.
8. \(f(40) = 1681 = 41^2\).

## TP Python – solutions

```python
def est_premier(n):
    """True si l'entier n est premier."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True
```

```python
def crible(N):
    """Liste des nombres premiers <= N (crible d'Ératosthène)."""
    est_premier = [True] * (N + 1)
    for k in (0, 1):
        if k <= N:
            est_premier[k] = False
    p = 2
    while p * p <= N:
        if est_premier[p]:
            for m in range(p * p, N + 1, p):
                est_premier[m] = False
        p = p + 1
    return [k for k in range(N + 1) if est_premier[k]]
```

```python
def decomposition(n):
    """Dictionnaire {premier: exposant} de la décomposition de n >= 2."""
    resultat = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat[d] = resultat.get(d, 0) + 1
            n = n // d
        d = d + 1
    if n > 1:
        resultat[n] = resultat.get(n, 0) + 1
    return resultat
```

```python
def decomposition(n):
    resultat = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            resultat[d] = resultat.get(d, 0) + 1
            n = n // d
        d = d + 1
    if n > 1:
        resultat[n] = resultat.get(n, 0) + 1
    return resultat

def nombre_de_diviseurs(n):
    """Nombre de diviseurs positifs de n >= 1."""
    produit = 1
    for exposant in decomposition(n).values():
        produit = produit * (exposant + 1)
    return produit
```

```python
def est_premier(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d = d + 1
    return True

def premiers_palindromes(N):
    """Liste croissante des nombres premiers palindromes <= N."""
    liste = []
    for k in range(2, N + 1):
        texte = str(k)
        if texte == texte[::-1] and est_premier(k):
            liste.append(k)
    return liste
```
