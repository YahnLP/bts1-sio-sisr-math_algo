from fractions import Fraction

def identite(n):
    m = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(Fraction(1 if i == j else 0))
        m.append(ligne)
    return m

def produit(a, b):
    resultat = []
    for i in range(len(a)):
        ligne = []
        for j in range(len(b[0])):
            s = Fraction(0)
            for k in range(len(b)):
                s = s + a[i][k] * b[k][j]
            ligne.append(s)
        resultat.append(ligne)
    return resultat

def est_inverse(a, b):
    n = len(a)
    return False   # À compléter : AB et BA doivent être égaux à l'identité
