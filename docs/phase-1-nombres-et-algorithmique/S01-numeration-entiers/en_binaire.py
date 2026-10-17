def en_binaire(n):
    """Renvoie l'écriture binaire (texte) de l'entier naturel n."""
    if n == 0:
        return "0"
    texte = ""
    while n > 0:
        reste = ...        # à compléter : reste de la division de n par 2
        texte = ... + texte   # à compléter : on place le chiffre à gauche
        n = ...            # à compléter : quotient de la division par 2
    return texte
