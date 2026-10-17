assert nombre_de_diviseurs(1) == 1
assert nombre_de_diviseurs(13) == 2
assert nombre_de_diviseurs(36) == 9
assert nombre_de_diviseurs(360) == 24
assert nombre_de_diviseurs(1024) == 11
assert nombre_de_diviseurs(5040) == 60
assert all(nombre_de_diviseurs(k) == len([d for d in range(1, k + 1) if k % d == 0]) for k in range(1, 300))
