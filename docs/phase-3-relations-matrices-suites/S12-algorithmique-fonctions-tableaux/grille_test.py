g = [[12, 8, 15, 10], [9, 14, 11, 7], [16, 13, 6, 18]]
assert somme_lignes(g) == [45, 41, 53]
assert somme_colonnes(g) == [37, 35, 32, 35]
assert transposee(g) == [[12, 9, 16], [8, 14, 13], [15, 11, 6], [10, 7, 18]]
assert transposee([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
assert sum(somme_lignes(g)) == sum(somme_colonnes(g)) == 139
