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
        pass   # À compléter : durée = max de (t[x] + durée de x)
    successeurs = {}
    for x in taches:
        successeurs[x] = []
    for x in taches:
        for p in taches[x][1]:
            successeurs[p].append(x)
    tard = {}
    restantes = list(taches)
    tours = 0
    while len(restantes) > 0 and tours < 100:
        tours = tours + 1
        for x in restantes:
            if all(s in tard for s in successeurs[x]):
                fin = duree
                for s in successeurs[x]:
                    pass   # À compléter : fin = le plus petit des tard[s]
                tard[x] = fin - taches[x][0]
                restantes.remove(x)
                break
    marges = {}
    for x in taches:
        marges[x] = 0   # À compléter : tard[x] - t[x]
    critiques = []      # À compléter : tâches de marge nulle, triées
    return (duree, marges, critiques)
