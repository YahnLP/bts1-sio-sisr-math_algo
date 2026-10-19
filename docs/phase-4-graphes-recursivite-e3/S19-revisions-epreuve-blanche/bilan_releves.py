def bilan_releves(releves, seuil):
    """Pour une liste non vide : (minimum, maximum, nombre de relevés en alerte,
    pourcentage de relevés en alerte). Un relevé est en alerte s'il est > seuil."""
    mini = releves[0]
    maxi = releves[0]
    n = 0
    for r in releves:
        # À compléter : mettre à jour mini, maxi et n
        pass
    pourcentage = 0
    # À compléter : n * 100 / len(releves)  (multiplier avant de diviser)
    return (mini, maxi, n, pourcentage)
