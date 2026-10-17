def inverse_mod(a, n):
    for x in range(1, n):
        if (a * x) % n == 1:
            return x
    return None

def chiffrer(texte, a, b):
    """Chiffre un texte en majuscules avec y = a*x + b (mod 26)."""
    resultat = ""
    for lettre in texte:
        if "A" <= lettre <= "Z":
            x = ord(lettre) - 65
            y = ...      # à compléter
            resultat = resultat + chr(y + 65)
        else:
            resultat = resultat + lettre
    return resultat

def dechiffrer(texte, a, b):
    """Déchiffre : x = a' * (y - b) (mod 26), où a' est l'inverse de a."""
    a_inv = inverse_mod(a, 26)
    resultat = ""
    for lettre in texte:
        if "A" <= lettre <= "Z":
            y = ord(lettre) - 65
            x = ...      # à compléter
            resultat = resultat + chr(x + 65)
        else:
            resultat = resultat + lettre
    return resultat
