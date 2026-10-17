assert puissance_mod(7, 100, 10) == 1
assert puissance_mod(3, 2024, 10) == 1
assert puissance_mod(13, 2025, 10) == 3
assert puissance_mod(2, 10, 7) == 2
assert puissance_mod(5, 0, 7) == 1
assert puissance_mod(2, 100, 7) == 2
assert all(puissance_mod(a, k, 13) == pow(a, k, 13) for a in range(0, 15) for k in range(0, 30))
