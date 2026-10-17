def somme_lignes(g):
    resultat = []
    for ligne in g:
        s = 0
        for x in ligne:
            # À compléter : accumuler dans s
            pass
        resultat.append(s)
    return resultat

def somme_colonnes(g):
    resultat = []
    for j in range(len(g[0])):
        s = 0
        for i in range(len(g)):
            # À compléter : ajouter g[i][j]
            pass
        resultat.append(s)
    return resultat

def transposee(g):
    resultat = []
    for j in range(len(g[0])):
        ligne = []
        for i in range(len(g)):
            # À compléter : ajouter g[i][j] à ligne
            pass
        resultat.append(ligne)
    return resultat
