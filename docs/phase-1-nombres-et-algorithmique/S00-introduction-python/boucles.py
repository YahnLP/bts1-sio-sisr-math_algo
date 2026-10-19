def somme_jusqua(n):
    """Renvoie 1 + 2 + ... + n (0 si n vaut 0), avec une boucle for."""
    total = 0
    for i in range(1, n + 1):
        pass   # À compléter : ajouter i à total
    return total

def nb_chiffres(n):
    """Nombre de chiffres décimaux de l'entier n > 0, avec une boucle while."""
    compteur = 0
    # La condition « compteur < 100 » évite une boucle infinie si tu te trompes.
    while n > 0 and compteur < 100:
        # À compléter : diviser n par 10 (quotient) et ajouter 1 à compteur
        pass
    return compteur

def premiere_puissance(limite):
    """Plus petit entier k >= 0 tel que 2 ** k > limite, avec une boucle while."""
    k = 0
    while 2 ** k <= limite and k < 100:
        pass   # À compléter : augmenter k de 1
    return k
