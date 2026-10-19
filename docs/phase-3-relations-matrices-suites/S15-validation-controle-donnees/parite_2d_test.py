ok = [[1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
assert lignes_incorrectes(ok) == [] and colonnes_incorrectes(ok) == []
ko = [[1, 0, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
assert lignes_incorrectes(ko) == [1] and colonnes_incorrectes(ko) == [2]
assert corrige(ko) == ok
assert corrige(ok) == ok
ko2 = [[1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 1]]
assert lignes_incorrectes(ko2) == [3] and colonnes_incorrectes(ko2) == [3]
assert corrige(ko2) == ok
ko3 = [[1, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
assert corrige(ko3) == ok
assert ko[1][2] == 0
