def binaire_rec(n):
    # À compléter : si n < 2, c'est str(n) ; sinon binaire_rec(n // 2) suivi du bit n % 2
    return ""

def binaire_iter(n):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        # À compléter : ajouter le bit n % 2 au DÉBUT de s, puis diviser n par 2
        n = 0
    return s
