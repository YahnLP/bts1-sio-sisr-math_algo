def additionneur_complet(a, b, c):
    """Renvoie (somme, retenue) pour trois bits."""
    somme = 0     # À compléter : a ^ b ^ c
    retenue = 0   # À compléter : (a & b) | (c & (a ^ b))
    return (somme, retenue)

def additionne(x, y):
    """Additionne deux chaînes de bits de même longueur ; résultat sur une position de plus."""
    n = len(x)
    resultat = ""
    retenue = 0
    for i in range(n - 1, -1, -1):
        # À compléter : additionner les bits de rang i et la retenue,
        # ajouter la somme au début du résultat, mémoriser la nouvelle retenue
        pass
    return str(retenue) + resultat
