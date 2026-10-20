# Corrigé S18

## Exercices

Réponses détaillées dans les encadrés de la feuille d'exercices. Résultats clés :

- `premiere_alerte([21, 25, 27, 26, 31], 25)` = 2 ; avec le seuil 40 : \(-1\).
- ​Suivi de `ecart_max([10, 14, 12, 12, 18])` : `d` = 4, 2, 0, 6 ; résultat 6.
- `est_croissant` : l'erreur est l'arrêt trop tôt (`return True` dans la boucle) ; `pourcentage(1, 4)` renvoie 0 à cause de `//`.
- `pic([12, 40, 33, 40, 7])` = `(40, 1)`.

## TP Python – solutions

```python
def nb_alertes(releves, seuil):
    n = 0
    for r in releves:
        if r > seuil:
            n = n + 1
    return n

def premiere_alerte(releves, seuil):
    for i in range(len(releves)):
        if releves[i] > seuil:
            return i
    return -1

def plus_longue_serie(releves, seuil):
    courante = 0
    meilleure = 0
    for r in releves:
        if r > seuil:
            courante = courante + 1
        else:
            courante = 0
        if courante > meilleure:
            meilleure = courante
    return meilleure

def ecart_max(releves):
    e = 0
    for i in range(len(releves) - 1):
        d = abs(releves[i + 1] - releves[i])
        if d > e:
            e = d
    return e
```

```python
def maximum(t):
    m = t[0]
    for x in t:
        if x > m:
            m = x
    return m

def somme_positifs_moyenne(t):
    s = 0
    n = 0
    for x in t:
        if x > 0:
            s = s + x
            n = n + 1
    if n == 0:
        return 0
    return s / n

def trie_sans_modifier(t):
    r = list(t)
    r.sort()
    return r
```

```python
def compte_pairs(t):
    n = 0
    for i in range(len(t)):
        if t[i] % 2 == 0:
            n = n + 1
    return n

def est_croissant(t):
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return False
    return True

def pourcentage(partie, total):
    if total == 0:
        return 0
    return partie * 100 / total
```

Erreurs de `debug.py` : `maximum` initialisait `m` à 0 (faux pour des valeurs négatives) ; `somme_positifs_moyenne` comptait aussi les valeurs négatives ; `trie_sans_modifier` triait la liste de l'appelant (`r = t` ne copie pas).

Erreurs de `debug2.py` : `compte_pairs` ignorait l'indice 0 (`range(1, ...)`) ; `est_croissant` s'arrêtait dès le premier couple en ordre ; `pourcentage` faisait une division entière ​avant de multiplier.
