def echecs_par_adresse(lignes):
    d = {}
    for ligne in lignes:
        c = ligne.split()
        # À compléter : si c[3] vaut "LOGIN_FAILED", incrémenter d[c[2]]
        # (la créer à 1 si l'adresse n'est pas encore dans d)
    return d

def adresses_suspectes(lignes, seuil):
    d = echecs_par_adresse(lignes)
    liste = []
    for adresse in d:
        # À compléter : garder l'adresse si son nombre d'échecs est >= seuil
        pass
    return sorted(liste)
