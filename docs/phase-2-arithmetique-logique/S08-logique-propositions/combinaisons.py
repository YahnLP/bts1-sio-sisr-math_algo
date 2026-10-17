def combinaisons(n):
    """Liste des 2**n tuples de n booléens, dans l'ordre de la table de vérité."""
    liste = []
    for k in range(2 ** n):
        ligne = []
        for i in range(n):
            # À compléter : le bit de rang (n - 1 - i) de k, converti en booléen
            ligne.append(False)
        liste.append(tuple(ligne))
    return liste
