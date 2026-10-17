# Corrigé S15

## Exercices

Réponses détaillées dans les encadrés de la feuille d'exercices. Résultats clés :

- \(v_n = 2^{n+2} - 1\) ; \(u_{10} = 47\), somme 297 ; \(5 \times 3^6 = 3645\), somme 5465.
- Sauvegardes : mois 32 (arithmétique), mois 24 (géométrique à 3 %).
- Seuils : 15 ans (1 000 € à 5 %), 7 ans (1 200 € à −20 %).

## TP Python – solutions

```python
from fractions import Fraction

def terme_arith(u0, r, n):
    return u0 + n * r

def terme_geom(u0, q, n):
    return u0 * q ** n

def somme_arith(u0, r, n):
    """u0 + ... + un : (nombre de termes) x (premier + dernier) / 2."""
    return Fraction((n + 1) * (u0 + terme_arith(u0, r, n)), 2)

def somme_geom(u0, q, n):
    """u0 + ... + un."""
    if q == 1:
        return (n + 1) * u0
    return u0 * (1 - q ** (n + 1)) / (1 - q)
```

```python
def suite(f, u0, n):
    """Liste [u0, u1, ..., un] avec u(k+1) = f(u(k))."""
    termes = [u0]
    u = u0
    for _ in range(n):
        u = f(u)
        termes.append(u)
    return termes
```

```python
def seuil_croissant(u0, q, limite):
    """Plus petit n tel que u0 q^n >= limite (q > 1)."""
    n = 0
    u = u0
    while u < limite:
        u = u * q
        n = n + 1
    return n

def seuil_decroissant(u0, q, limite):
    """Plus petit n tel que u0 q^n <= limite (0 < q < 1)."""
    n = 0
    u = u0
    while u > limite:
        u = u * q
        n = n + 1
    return n
```

```python
def somme_termes(f, a, b):
    """Somme des f(k) pour k de a à b inclus (0 si b < a)."""
    s = 0
    for k in range(a, b + 1):
        s = s + f(k)
    return s
```
