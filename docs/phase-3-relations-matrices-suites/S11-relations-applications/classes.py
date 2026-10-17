def classes(r, e):
    """Classes d'équivalence de r sur e, par plus petit élément croissant."""
    vus = set()
    resultat = []
    for x in sorted(e):
        if x in vus:
            continue
        classe = set()
        for y in e:
            # À compléter : ajouter y à la classe de x si (x, y) est dans r
            pass
        resultat.append(classe)
        # À compléter : mémoriser les éléments de la classe comme déjà vus
    return resultat
