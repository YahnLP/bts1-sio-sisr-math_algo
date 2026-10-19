def nb_alertes(releves, seuil):
    """Nombre de relevés strictement supérieurs à seuil."""
    n = 0
    for r in releves:
        # À compléter : compter les relevés en alerte
        pass
    return n

def premiere_alerte(releves, seuil):
    """Indice du premier relevé strictement supérieur à seuil, ou -1 s'il n'y en a pas."""
    for i in range(len(releves)):
        # À compléter : renvoyer i dès qu'un relevé dépasse le seuil
        pass
    return -1

def plus_longue_serie(releves, seuil):
    """Plus grand nombre de relevés consécutifs strictement supérieurs à seuil."""
    courante = 0
    meilleure = 0
    for r in releves:
        # À compléter : si r dépasse le seuil, courante augmente de 1, sinon elle retombe à 0 ;
        # mettre à jour meilleure
        pass
    return meilleure

def ecart_max(releves):
    """Plus grande différence, en valeur absolue, entre deux relevés consécutifs (0 s'il y a moins de 2 relevés)."""
    e = 0
    for i in range(len(releves) - 1):
        # À compléter : comparer abs(releves[i + 1] - releves[i]) à e
        pass
    return e
