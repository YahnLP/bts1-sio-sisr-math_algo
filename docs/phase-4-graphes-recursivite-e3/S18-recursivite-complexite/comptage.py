def recherche_sequentielle(t, x):
    comparaisons = 0
    for i in range(len(t)):
        # À compléter : compter la comparaison ; renvoyer (i, comparaisons) si t[i] == x
        pass
    return (-1, comparaisons)

def dichotomie(t, x):
    debut = 0
    fin = len(t) - 1
    comparaisons = 0
    while debut <= fin and comparaisons < 1000:
        milieu = (debut + fin) // 2
        # À compléter : compter la comparaison ; renvoyer (milieu, comparaisons) si t[milieu] == x ;
        # sinon réduire la zone à droite (debut) ou à gauche (fin)
        comparaisons = comparaisons + 1
    return (-1, comparaisons)
