def parties(elements):
    """Liste des 2**n parties de la liste elements, chacune sous forme d'ensemble."""
    n = len(elements)
    resultat = []
    for k in range(2 ** n):
        partie = set()
        for i in range(n):
            # À compléter : si le bit de rang i de k vaut 1, ajouter elements[i]
            pass
        resultat.append(partie)
    return resultat
