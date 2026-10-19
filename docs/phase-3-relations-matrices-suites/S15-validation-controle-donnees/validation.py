def est_octet(s):
    """Vrai si s (chaîne) écrit un entier de 0 à 255 en décimal, sans zéro inutile au début."""
    if s == "" or not s.isdigit():
        return False
    # À compléter : refuser un zéro initial (sauf "0" seul), puis tester 0 <= int(s) <= 255
    return False

def ipv4_valide(s):
    """Vrai si s est une adresse IPv4 écrite en notation décimale pointée."""
    morceaux = s.split(".")
    # À compléter : exactement 4 morceaux, tous valides selon est_octet
    return False

def mac_valide(s):
    """Vrai si s a la forme AA:BB:CC:DD:EE:FF (6 groupes de 2 chiffres hexadécimaux)."""
    hexa = "0123456789abcdefABCDEF"
    groupes = s.split(":")
    # À compléter : 6 groupes, chacun de 2 caractères pris dans hexa
    return False
