def maximum(t):
    m = 0   # erreur : ...
    for x in t:
        if x > m:
            m = x
    return m

def somme_positifs_moyenne(t):
    s = 0
    n = 0
    for x in t:
        if x > 0:
            s = s + x
        n = n + 1   # erreur : ...
    if n == 0:
        return 0
    return s / n

def trie_sans_modifier(t):
    r = t   # erreur : ...
    r.sort()
    return r
