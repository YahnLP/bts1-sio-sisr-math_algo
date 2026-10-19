assert signe(-4) == "négatif"
assert signe(0) == "nul"
assert signe(12) == "positif"
assert plus_grand(3, 9) == 9
assert plus_grand(9, 3) == 9
assert plus_grand(5, 5) == 5
assert resultat(7.5) == "ajourné"
assert resultat(8) == "rattrapage"
assert resultat(9.9) == "rattrapage"
assert resultat(10) == "admis"
assert resultat(18) == "admis"
