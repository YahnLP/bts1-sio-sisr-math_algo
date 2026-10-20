# Corrigé S09

## Exercices

1. Voir les réponses repliables de chaque exercice.
2. Pour les négations, on ​échange chaque quantificateur et on nie le prédicat final.
3. Pour le cardinal : \(70 + 45 - 25 = 90\) personnes au moins dans l'un des deux ensembles ; sur 100, il en reste 10 dans aucun.

## TP Python – solutions

```python
def pour_tout(pred, liste):
    """Vrai si pred(x) est vrai pour tous les éléments (vrai pour une liste vide)."""
    for x in liste:
        if not pred(x):
            return False
    return True
```

```python
def il_existe(pred, liste):
    """Vrai si pred(x) est vrai pour au moins un élément (faux pour une liste vide)."""
    for x in liste:
        if pred(x):
            return True
    return False
```

```python
def chacun_a_un_serveur(acces, utilisateurs, serveurs):
    """Pour tout utilisateur u, il existe un serveur s tel que (u, s) est dans acces."""
    for u in utilisateurs:
        trouve = False
        for s in serveurs:
            if (u, s) in acces:
                trouve = True
        if not trouve:
            return False
    return True

def un_serveur_pour_tous(acces, utilisateurs, serveurs):
    """Il existe un serveur s tel que, pour tout utilisateur u, (u, s) est dans acces."""
    for s in serveurs:
        tous = True
        for u in utilisateurs:
            if (u, s) not in acces:
                tous = False
        if tous:
            return True
    return False
```

```python
def operations(a, b):
    """Renvoie (a ∩ b, a ∪ b, a \\ b, a Δ b) sans les opérateurs d'ensembles."""
    inter = set()
    reunion = set()
    diff = set()
    for x in a:
        reunion.add(x)
        if x in b:
            inter.add(x)
        else:
            diff.add(x)
    sym = set()
    for x in b:
        reunion.add(x)
        if x not in a:
            sym.add(x)
    for x in diff:
        sym.add(x)
    return (inter, reunion, diff, sym)
```

```python
def parties(elements):
    """Liste des 2**n parties de la liste elements, chacune sous forme d'ensemble."""
    n = len(elements)
    resultat = []
    for k in range(2 ** n):
        partie = set()
        for i in range(n):
            if (k >> i) & 1 == 1:
                partie.add(elements[i])
        resultat.append(partie)
    return resultat
```

```python
def groupes_communs(groupes, u, v):
    """Ensemble des noms de groupes contenant à la fois u et v."""
    communs = set()
    for nom in groupes:
        if u in groupes[nom] and v in groupes[nom]:
            communs.add(nom)
    return communs
```
