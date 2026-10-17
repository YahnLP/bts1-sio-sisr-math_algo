def chacun_a_un_serveur(acces, utilisateurs, serveurs):
    """Pour tout utilisateur u, il existe un serveur s tel que (u, s) est dans acces."""
    for u in utilisateurs:
        trouve = False
        for s in serveurs:
            # À compléter : mémoriser qu'un serveur a été trouvé pour u
            pass
        if not trouve:
            return False
    return True

def un_serveur_pour_tous(acces, utilisateurs, serveurs):
    """Il existe un serveur s tel que, pour tout utilisateur u, (u, s) est dans acces."""
    for s in serveurs:
        tous = True
        for u in utilisateurs:
            # À compléter : si u n'a pas accès à s, alors s ne convient pas
            pass
        if tous:
            return True
    return False
