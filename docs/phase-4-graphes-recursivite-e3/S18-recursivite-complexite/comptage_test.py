s = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]
assert recherche_sequentielle(s, 38) == (12, 13) and recherche_sequentielle(s, 2) == (0, 1)
assert recherche_sequentielle(s, 99) == (-1, 15)
assert dichotomie(s, 38) == (12, 4) and dichotomie(s, 23) == (7, 1)
assert dichotomie(s, 15)[0] == -1 and dichotomie(s, 15)[1] <= 4
assert max(dichotomie(s, x)[1] for x in s) == 4
t = list(range(1000))
assert max(dichotomie(t, x)[1] for x in t) == 10 and max(recherche_sequentielle(t, x)[1] for x in t) == 1000
assert dichotomie([], 3) == (-1, 0)
