# Corrigé S00

## Exercices

Réponses détaillées dans les encadrés de la feuille d'exercices. Résultats clés :

- Exercice 1 : `3 2` puis `18`. Exercice 2 : 8 ; `"53"` ; 8 ; `"53"` ; 6 ; `"r"` et `"u"`.
- Exercice 3 : `"ajourné"`, `"rattrapage"`, `"admis"`.
- Exercice 4 : 9, 16, 25, 36 ; `total` = 18. Exercice 5 : somme des chiffres de 2026 = 10.
- Exercice 7 : `4 4 16 43`.

## TP Python – solutions

```python
def quotient_reste(a, b):
    q = a // b
    r = a % b
    return (q, r)

def est_multiple(a, b):
    return a % b == 0

def conversion_secondes(s):
    heures = s // 3600
    reste = s % 3600
    minutes = reste // 60
    secondes = reste % 60
    return (heures, minutes, secondes)
```

```python
def premier_et_dernier(t):
    return t[0] + t[-1]

def entoure(t, c):
    return c + t + c

def nb_chiffres_texte(n):
    return len(str(n))

def somme_de_textes(a, b):
    return int(a) + int(b)
```

```python
def signe(n):
    if n < 0:
        return "négatif"
    elif n == 0:
        return "nul"
    else:
        return "positif"

def plus_grand(a, b):
    if a > b:
        return a
    else:
        return b

def resultat(note):
    if note < 8:
        return "ajourné"
    elif note < 10:
        return "rattrapage"
    else:
        return "admis"
```

```python
def somme_jusqua(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

def nb_chiffres(n):
    compteur = 0
    while n > 0 and compteur < 100:
        n = n // 10
        compteur = compteur + 1
    return compteur

def premiere_puissance(limite):
    k = 0
    while 2 ** k <= limite and k < 100:
        k = k + 1
    return k
```

```python
def somme_octets(adresse):
    total = 0
    for morceau in adresse.split("."):
        total = total + int(morceau)
    return total

def compte_superieurs(liste, seuil):
    n = 0
    for x in liste:
        if x > seuil:
            n = n + 1
    return n

def liste_carres(n):
    carres = []
    for i in range(n):
        carres.append(i * i)
    return carres
```

