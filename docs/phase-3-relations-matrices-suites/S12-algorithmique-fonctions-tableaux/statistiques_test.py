t = [14, 3, 27, 9, 27, 5]
assert moyenne([12, 8, 15]) == 35 / 3
assert moyenne([4]) == 4
assert abs(moyenne(t) - 85 / 6) < 1e-9
assert maximum(t) == 27 and maximum([-5, -2, -9]) == -2
assert indice_du_max(t) == 2
assert indice_du_max([1, 2, 3]) == 2 and indice_du_max([9]) == 0
