def compte_pairs(t):
    n = 0
    for i in range(1, len(t)):   # erreur : ...
        if t[i] % 2 == 0:
            n = n + 1
    return n

def est_croissant(t):
    for i in range(len(t) - 1):
        if t[i] <= t[i + 1]:
            return True   # erreur : ...
    return False

def pourcentage(partie, total):
    if total == 0:
        return 0
    return partie // total * 100   # erreur : ...
