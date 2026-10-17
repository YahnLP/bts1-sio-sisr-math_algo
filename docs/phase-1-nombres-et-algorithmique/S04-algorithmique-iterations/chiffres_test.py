assert somme_chiffres(2024) == 8
assert somme_chiffres(0) == 0
assert somme_chiffres(90210) == 12
assert nombre_chiffres(2024) == 4
assert nombre_chiffres(0) == 1
assert nombre_chiffres(9) == 1
assert nombre_chiffres(10) == 2
assert nombre_chiffres(90210) == 5
assert all(nombre_chiffres(k) == len(str(k)) for k in range(0, 5000))
