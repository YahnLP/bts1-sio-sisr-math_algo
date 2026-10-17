# Corrigé S17

## Exercices

Réponses détaillées dans les encadrés de la feuille d'exercices. Résultats clés :

- Chemin minimal \(S \to T\) : S → B → A → C → D → T, valeur 13 ; \(A \to E\) : A → C → F → E, valeur 20.
- Projet de déploiement : durée 18 jours, chemin critique A → D → E → F → H.
- Projet de migration : durée 10 jours, tâches critiques B, C, D, E, F (deux chemins critiques).

## TP Python – solutions

```python
def dijkstra(arcs, source, sommets):
    inf = float("inf")
    distance = {}
    predecesseur = {}
    for v in sommets:
        distance[v] = inf
        predecesseur[v] = None
    distance[source] = 0
    fixes = []
    while len(fixes) < len(sommets):
        x = None
        for v in sommets:
            if v not in fixes and (x is None or distance[v] < distance[x]):
                x = v
        if distance[x] == inf:
            break
        fixes.append(x)
        for (a, b) in arcs:
            if a == x and b not in fixes and distance[x] + arcs[(a, b)] < distance[b]:
                distance[b] = distance[x] + arcs[(a, b)]
                predecesseur[b] = x
    return (distance, predecesseur)

def reconstruire(predecesseur, cible):
    chemin = [cible]
    while predecesseur[chemin[-1]] is not None:
        chemin.append(predecesseur[chemin[-1]])
    chemin.reverse()
    return chemin
```

```python
def dates_au_plus_tot(taches):
    t = {}
    restantes = list(taches)
    while len(restantes) > 0:
        pret = None
        for x in restantes:
            ok = True
            for p in taches[x][1]:
                if p not in t:
                    ok = False
            if ok:
                pret = x
                break
        if pret is None:
            return None
        date = 0
        for p in taches[pret][1]:
            if t[p] + taches[p][0] > date:
                date = t[p] + taches[p][0]
        t[pret] = date
        restantes.remove(pret)
    return t
```

```python
def dates_au_plus_tot(taches):
    t = {}
    restantes = list(taches)
    while len(restantes) > 0:
        pret = None
        for x in restantes:
            ok = True
            for p in taches[x][1]:
                if p not in t:
                    ok = False
            if ok:
                pret = x
                break
        if pret is None:
            return None
        date = 0
        for p in taches[pret][1]:
            if t[p] + taches[p][0] > date:
                date = t[p] + taches[p][0]
        t[pret] = date
        restantes.remove(pret)
    return t

def analyse(taches):
    """Renvoie (durée du projet, marges totales, liste triée des tâches critiques)."""
    t = dates_au_plus_tot(taches)
    duree = 0
    for x in taches:
        if t[x] + taches[x][0] > duree:
            duree = t[x] + taches[x][0]
    successeurs = {}
    for x in taches:
        successeurs[x] = []
    for x in taches:
        for p in taches[x][1]:
            successeurs[p].append(x)
    tard = {}
    restantes = list(taches)
    while len(restantes) > 0:
        for x in restantes:
            if all(s in tard for s in successeurs[x]):
                fin = duree
                for s in successeurs[x]:
                    if tard[s] < fin:
                        fin = tard[s]
                tard[x] = fin - taches[x][0]
                restantes.remove(x)
                break
    marges = {}
    for x in taches:
        marges[x] = tard[x] - t[x]
    critiques = sorted([x for x in taches if marges[x] == 0])
    return (duree, marges, critiques)
```
