def produit_bool(a, b):
    n = len(a)
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            v = 0
            for k in range(n):
                # À compléter : v vaut 1 si a[i][k] et b[k][j] valent 1
                pass
            ligne.append(v)
        resultat.append(ligne)
    return resultat

def fermeture(m):
    n = len(m)
    t = [ligne[:] for ligne in m]
    p = [ligne[:] for ligne in m]
    for _ in range(n - 1):
        p = produit_bool(p, m)
        for i in range(n):
            for j in range(n):
                pass   # À compléter : si p[i][j] vaut 1, mettre 1 dans t[i][j]
    return t
