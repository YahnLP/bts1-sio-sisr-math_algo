def est_reflexive(r, e):
    for x in e:
        # À compléter : renvoyer False si (x, x) n'est pas dans r
        pass
    return True

def est_symetrique(r):
    for (x, y) in r:
        # À compléter : renvoyer False si (y, x) n'est pas dans r
        pass
    return True

def est_antisymetrique(r):
    for (x, y) in r:
        # À compléter : renvoyer False si (y, x) est dans r avec x != y
        pass
    return True

def est_transitive(r):
    for (x, y) in r:
        for (z, t) in r:
            # À compléter : si y == z, le couple (x, t) doit être dans r
            pass
    return True
