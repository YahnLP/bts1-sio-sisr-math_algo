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
            return None   # circuit : aucune tâche ne peut commencer
        date = 0
        for p in taches[pret][1]:
            pass   # À compléter : date = max(date, t[p] + durée de p)
        t[pret] = date
        restantes.remove(pret)
    return t
