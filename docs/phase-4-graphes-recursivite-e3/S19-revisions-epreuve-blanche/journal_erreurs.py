def compte_erreurs(lignes):
    d = {}
    for ligne in lignes:
        c = ligne.split()
        # À compléter : si c[3] vaut "ERROR", incrémenter d[c[2]]
        # (la créer à 1 si l'adresse n'est pas encore dans d)
    return d

def adresse_la_plus_active(lignes):
    d = compte_erreurs(lignes)
    meilleure = None
    for adresse in sorted(d):
        # À compléter : garder l'adresse si elle a strictement plus d'erreurs que meilleure
        pass
    return meilleure
