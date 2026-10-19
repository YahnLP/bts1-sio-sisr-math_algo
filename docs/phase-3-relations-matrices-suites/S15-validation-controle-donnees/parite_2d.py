def lignes_incorrectes(g):
    """Indices des lignes de g dont le nombre de 1 est impair."""
    res = []
    for i in range(len(g)):
        # À compléter : si sum(g[i]) est impair, ajouter i à res
        pass
    return res

def colonnes_incorrectes(g):
    """Indices des colonnes de g dont le nombre de 1 est impair."""
    res = []
    for j in range(len(g[0])):
        total = 0
        # À compléter : additionner g[i][j] pour toutes les lignes i
        if total % 2 == 1:
            res.append(j)
    return res

def corrige(g):
    """Renvoie une copie de g où l'unique bit erroné (s'il y en a un) est rétabli."""
    copie = [ligne[:] for ligne in g]
    lignes = lignes_incorrectes(g)
    colonnes = colonnes_incorrectes(g)
    # À compléter : si une seule ligne i et une seule colonne j sont incorrectes,
    # inverser copie[i][j] (0 devient 1, 1 devient 0)
    return copie
