t = [14, 3, 27, 9, 27, 5]
assert position(t, 27) == 2 and position(t, 5) == 5 and position(t, 99) == -1
assert compte(t, 27) == 2 and compte(t, 3) == 1 and compte(t, 0) == 0
s = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44]
assert dichotomie(s, 38) == 12 and dichotomie(s, 2) == 0 and dichotomie(s, 44) == 14
assert dichotomie(s, 15) == -1 and dichotomie(s, 1) == -1 and dichotomie(s, 99) == -1
assert dichotomie([], 3) == -1 and dichotomie([7], 7) == 0
assert all(dichotomie(s, x) == i for i, x in enumerate(s))
