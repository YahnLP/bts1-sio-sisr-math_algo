from fractions import Fraction

def identite(n):
    m = []
    for i in range(n):
        ligne = []
        for j in range(n):
            # À compléter : 1 sur la diagonale, 0 ailleurs (en Fraction)
            ligne.append(Fraction(0))
        m.append(ligne)
    return m

def produit(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = Fraction(0)
            for k in range(len(b)):
                # À compléter : ajouter a[i][k] * b[k][j]
                pass
            ligne.append(s)
        resultat.append(ligne)
    return resultat
