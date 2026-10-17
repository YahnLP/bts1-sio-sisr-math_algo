# Corrigé S05

## Exercices

1. 100 = 7 × 14 + 2 ; 7 = 100 × 0 + 7 ; 2024 = 24 × 84 + 8 ; -23 = 6 × -4 + 1.
2. Vrai ; faux (n = 12) ; vrai ; faux.
3. Voir les tableaux de l'énoncé.
4. 6 ; 36 a 9 diviseurs.
5. 108 ; 21 ; 1.
6. 2 ; 240 (rapport 8 : 5).
7. 36 ; 75 ; 36 jours.
8. Voir la démonstration ; PGCD(48, 18) = 6.

## TP Python – solutions

```python
def division_euclidienne(a, b):
    """Renvoie (q, r) tels que a = b*q + r et 0 <= r < b (a >= 0, b > 0)."""
    q = 0
    r = a
    while r >= b:
        r = r - b
        q = q + 1
    return (q, r)
```

```python
def diviseurs(n):
    """Liste croissante des diviseurs positifs de n (n >= 1)."""
    liste = []
    for d in range(1, n + 1):
        if n % d == 0:
            liste.append(d)
    return liste
```

```python
def pgcd(a, b):
    """PGCD de deux entiers naturels non tous deux nuls (algorithme d'Euclide)."""
    while b != 0:
        a, b = b, a % b
    return a
```

```python
def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def ppcm(a, b):
    """PPCM de deux entiers strictement positifs."""
    return a * b // pgcd(a, b)

def premiers_entre_eux(a, b):
    """True si a et b sont premiers entre eux."""
    return pgcd(a, b) == 1
```

```python
def nombre_divisions(a, b):
    """Nombre de divisions euclidiennes de l'algorithme d'Euclide appliqué à (a, b), b > 0."""
    compteur = 0
    while b != 0:
        a, b = b, a % b
        compteur = compteur + 1
    return compteur
```
