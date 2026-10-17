def prefixe_vers_masque(n):
    """Masque décimal pointé d'un préfixe n (0 à 32)."""
    octets = []
    for i in range(4):
        bits = min(8, max(0, n - 8 * i))   # nombre de bits à 1 dans cet octet
        # À compléter : valeur de l'octet = 256 - 2 ** (8 - bits)
        octets.append("0")
    return ".".join(octets)

def adresse_reseau(ip, masque):
    """ET bit à bit, octet par octet."""
    a = ip.split(".")
    m = masque.split(".")
    octets = []
    for i in range(4):
        # À compléter : int(a[i]) & int(m[i])
        octets.append("0")
    return ".".join(octets)

def diffusion(ip, masque):
    """Adresse réseau dont tous les bits de machine sont à 1."""
    a = ip.split(".")
    m = masque.split(".")
    octets = []
    for i in range(4):
        # À compléter : (int(a[i]) & int(m[i])) | (255 - int(m[i]))
        octets.append("0")
    return ".".join(octets)

def nb_machines(n):
    """Nombre d'adresses utilisables pour le préfixe n."""
    return 0   # À compléter
