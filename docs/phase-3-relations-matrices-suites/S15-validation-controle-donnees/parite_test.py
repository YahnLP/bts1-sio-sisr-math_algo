assert bit_parite([1, 0, 1, 1, 0, 0, 1]) == 0 and bit_parite([1, 0, 1, 1, 0, 0, 0]) == 1
assert bit_parite([]) == 0 and bit_parite([1]) == 1 and bit_parite([0, 0, 0]) == 0
assert ajoute_parite([1, 0, 1, 1, 0, 0, 0]) == [1, 0, 1, 1, 0, 0, 0, 1]
assert ajoute_parite([1, 1]) == [1, 1, 0]
m = [1, 0, 1]
assert ajoute_parite(m) == [1, 0, 1, 0] and m == [1, 0, 1]
assert mot_valide([1, 0, 1, 1, 0, 0, 1, 0]) is True and mot_valide([1, 0, 1, 1, 0, 0, 1, 1]) is False
assert mot_valide([1, 0, 1, 1, 0, 0, 0, 1]) is True
assert mot_valide([1, 0, 1, 1, 1, 0, 0, 1]) is False
assert mot_valide([1, 0, 0, 1, 0, 0, 1, 1]) is True
assert mot_valide([]) is True
