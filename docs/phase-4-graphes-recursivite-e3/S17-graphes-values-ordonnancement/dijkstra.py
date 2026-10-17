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
            # À compléter : si a est x, b n'est pas fixé et distance[x] + valeur < distance[b],
            # mettre à jour distance[b] et predecesseur[b]
            pass
    return (distance, predecesseur)

def reconstruire(predecesseur, cible):
    chemin = [cible]
    # À compléter : remonter les prédécesseurs jusqu'à la source (prédécesseur None)
    chemin.reverse()
    return chemin
