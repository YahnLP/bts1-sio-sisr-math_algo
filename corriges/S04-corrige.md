# Corrigé S04

## Exercices

1. Voir la trace : s = 55.
2. i = 2187, c = 7.
3. Oui ; non (jamais égal à 0) ; non.
4. 1683.
5. 5 chiffres ; somme des chiffres de 2 024 = 8.
6. CD ; 100101.
7. m = 9, ​position 1.
8. 15 ; \(n(n-1)/2\).

## TP Python – solutions

```python
def somme_carres(n):
    """Renvoie 1² + 2² + ... + n²."""
    s = 0
    for i in range(1, n + 1):
        s = s + i * i
    return s
```

```python
def factorielle(n):
    """Renvoie n! (n entier >= 0)."""
    p = 1
    for i in range(2, n + 1):
        p = p * i
    return p
```

```python
def somme_chiffres(n):
    """Somme des chiffres décimaux de n (n >= 0)."""
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

def nombre_chiffres(n):
    """Nombre de chiffres décimaux de n (n >= 0) ; 0 s'écrit avec 1 chiffre."""
    if n == 0:
        return 1
    c = 0
    while n > 0:
        n = n // 10
        c = c + 1
    return c
```

```python
def mois_avant_saturation(capacite):
    """Plus petit k tel que 2**k >= capacite (capacite en Go, entier >= 1)."""
    volume = 1
    k = 0
    while volume < capacite:
        volume = volume * 2
        k = k + 1
    return k
```

```python
def plage(prefixe, debut, fin):
    """Liste des adresses prefixe.k pour k de debut à fin inclus."""
    adresses = []
    for k in range(debut, fin + 1):
        adresses.append(prefixe + "." + str(k))
    return adresses
```

```python
def syracuse(n):
    """Nombre d'étapes pour atteindre 1 (n >= 1)."""
    etapes = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        etapes = etapes + 1
    return etapes
```
