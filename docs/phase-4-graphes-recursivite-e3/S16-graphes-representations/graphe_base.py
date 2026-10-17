def matrice_adjacence(n, arcs):
    m = []
    for i in range(n):
        m.append([0] * n)
    for (a, b) in arcs:
        pass   # À compléter : mettre 1 dans la case (a, b)
    return m

def successeurs(m, i):
    liste = []
    for j in range(len(m)):
        # À compléter : ajouter j si m[i][j] vaut 1
        pass
    return liste

def demi_degres(m):
    n = len(m)
    ext = []
    inte = []
    for i in range(n):
        ext.append(0)   # À compléter : somme de la ligne i
    for j in range(n):
        s = 0
        for i in range(n):
            pass   # À compléter : ajouter m[i][j]
        inte.append(s)
    return (ext, inte)
