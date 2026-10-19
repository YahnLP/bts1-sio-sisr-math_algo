def somme_controle(octets):
    """Octet c (0 à 255) tel que la somme des octets, plus c, soit un multiple de 256."""
    # À compléter : utiliser sum et le reste de la division par 256
    return 0

def trame_valide(octets, c):
    """Vrai si la somme des octets, plus c, est un multiple de 256."""
    # À compléter
    return False

def xor_controle(octets):
    """OU exclusif (^) de tous les octets ; 0 pour une liste vide."""
    r = 0
    for o in octets:
        # À compléter : combiner r et o avec ^
        pass
    return r
