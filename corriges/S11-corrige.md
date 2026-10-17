# Corrigé S11

## Exercices

1–10. Les réponses détaillées figurent dans les encadrés repliables de la feuille d'exercices (chaque nombre, chaque classe et chaque arête de diagramme est calculé à la génération).

Rappel des résultats clés :

- \(\lvert A \times B \times C \rvert = 30\) ; \(\lvert \text{protocoles} \times \text{ports} \rvert = 12\).
- Classes de la congruence modulo 3 sur \(\{1,\dots,10\}\) : \(\{1, 4, 7, 10\}\) ; \(\{2, 5, 8\}\) ; \(\{3, 6, 9\}\).
- Composées en 3 : \(g \circ f\) donne 49, \(f \circ g\) donne 19.
- 20 identifiants dans 8 cases : au moins 3 dans une même case.

## TP Python – solutions

```python
def produit(a, b):
    """Ensemble des couples (x, y), x dans a, y dans b."""
    resultat = set()
    for x in a:
        for y in b:
            resultat.add((x, y))
    return resultat
```

```python
def est_reflexive(r, e):
    for x in e:
        if (x, x) not in r:
            return False
    return True

def est_symetrique(r):
    for (x, y) in r:
        if (y, x) not in r:
            return False
    return True

def est_antisymetrique(r):
    for (x, y) in r:
        if (y, x) in r and x != y:
            return False
    return True

def est_transitive(r):
    for (x, y) in r:
        for (z, t) in r:
            if y == z and (x, t) not in r:
                return False
    return True
```

```python
def classes(r, e):
    """Classes d'équivalence de r sur e, par plus petit élément croissant."""
    vus = set()
    resultat = []
    for x in sorted(e):
        if x in vus:
            continue
        classe = set()
        for y in e:
            if (x, y) in r:
                classe.add(y)
        resultat.append(classe)
        vus = vus | classe
    return resultat
```

```python
def est_injective(f):
    valeurs = set()
    for x in f:
        valeurs.add(f[x])
    return len(valeurs) == len(f)

def est_surjective(f, b):
    valeurs = set()
    for x in f:
        valeurs.add(f[x])
    return valeurs == set(b)

def est_bijective(f, b):
    return est_injective(f) and est_surjective(f, b)
```

```python
def image_directe(f, x):
    """Ensemble des images des éléments de x."""
    resultat = set()
    for a in x:
        resultat.add(f[a])
    return resultat

def image_reciproque(f, y):
    """Ensemble des éléments de départ dont l'image est dans y."""
    resultat = set()
    for a in f:
        if f[a] in y:
            resultat.add(a)
    return resultat

def composee(g, f):
    """Dictionnaire de g o f : x -> g(f(x))."""
    resultat = {}
    for x in f:
        resultat[x] = g[f[x]]
    return resultat

def reciproque(f):
    """Application réciproque (b -> a), ou None si f n'est pas injective."""
    inverse = {}
    for a in f:
        if f[a] in inverse:
            return None
        inverse[f[a]] = a
    return inverse
```
