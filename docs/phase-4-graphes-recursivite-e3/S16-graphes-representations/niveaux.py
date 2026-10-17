def niveaux(m):
    """Niveaux d'un graphe sans circuit, ou None s'il y a un circuit."""
    n = len(m)
    restants = list(range(n))
    resultat = []
    tours = 0
    while len(restants) > 0 and tours < n:
        tours = tours + 1
        niveau = []
        for j in restants:
            sans_pred = True
            for i in restants:
                pass   # À compléter : si m[i][j] vaut 1, j a un prédécesseur parmi les restants
            if sans_pred:
                niveau.append(j)
        # À compléter : si le niveau est vide, renvoyer None (circuit) ;
        # sinon l'ajouter au résultat et retirer ses sommets de restants
        break
    return resultat
