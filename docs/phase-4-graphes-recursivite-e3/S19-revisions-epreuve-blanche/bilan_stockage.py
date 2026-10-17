def volumes(v0, q, n):
    liste = [v0]
    v = v0
    for _ in range(n):
        # À compléter : calculer le volume du mois suivant et l'ajouter à la liste
        pass
    return liste

def bilan(v0, q, capacite):
    n = 0
    v = v0
    while v < capacite and n < 10000:
        # À compléter : passer au mois suivant
        pass
    return (n, v)
