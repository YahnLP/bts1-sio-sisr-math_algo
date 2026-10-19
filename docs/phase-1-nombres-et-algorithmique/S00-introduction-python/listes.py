def somme_octets(adresse):
    """Somme des quatre nombres d'une adresse comme "192.168.1.10"."""
    total = 0
    for morceau in adresse.split("."):
        pass   # À compléter : ajouter int(morceau) à total
    return total

def compte_superieurs(liste, seuil):
    """Nombre d'éléments de la liste strictement supérieurs à seuil."""
    n = 0
    for x in liste:
        pass   # À compléter : si x > seuil, ajouter 1 à n
    return n

def liste_carres(n):
    """Renvoie la liste des carrés de 0 à n - 1 : [0, 1, 4, ...] (liste vide si n vaut 0)."""
    carres = []
    for i in range(n):
        pass   # À compléter : ajouter i * i à la liste avec append
    return carres
