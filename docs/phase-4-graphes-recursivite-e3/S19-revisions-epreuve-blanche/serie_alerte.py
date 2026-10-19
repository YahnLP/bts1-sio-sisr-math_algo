def premiere_serie(releves, seuil, k):
    """Indice du premier relevé de la première série d'au moins k relevés consécutifs
    strictement supérieurs à seuil (k >= 1), ou -1 s'il n'y en a pas."""
    courante = 0
    for i in range(len(releves)):
        # À compléter : mettre à jour courante (+1 si en alerte, sinon retour à 0)
        # puis, si courante vaut k, renvoyer l'indice du début de la série
        pass
    return -1
