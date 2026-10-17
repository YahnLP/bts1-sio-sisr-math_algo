def position(t, x):
    for i in range(len(t)):
        # À compléter : renvoyer i si t[i] vaut x
        pass
    return -1

def compte(t, x):
    n = 0
    for y in t:
        # À compléter : compter les occurrences de x
        pass
    return n

def dichotomie(t, x):
    debut = 0
    fin = len(t) - 1
    while debut <= fin:
        milieu = (debut + fin) // 2
        # À compléter : comparer t[milieu] à x, renvoyer milieu si égal,
        # sinon réduire la zone à droite (debut) ou à gauche (fin).
        # Sans cette mise à jour la boucle ne s'arrête pas : on sort donc ici.
        break
    return -1
