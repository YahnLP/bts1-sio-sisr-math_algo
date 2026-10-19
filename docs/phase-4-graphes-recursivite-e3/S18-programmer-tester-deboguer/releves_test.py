t = [21, 25, 27, 26, 31, 32, 33, 24, 29, 30]
assert nb_alertes(t, 25) == 7 and nb_alertes(t, 40) == 0 and nb_alertes([], 25) == 0
assert nb_alertes(t, 20) == 10 and nb_alertes([25], 25) == 0
assert premiere_alerte(t, 25) == 2 and premiere_alerte(t, 40) == -1 and premiere_alerte([], 25) == -1
assert premiere_alerte(t, 20) == 0 and premiere_alerte([30, 10], 25) == 0
assert plus_longue_serie(t, 25) == 5 and plus_longue_serie(t, 40) == 0 and plus_longue_serie([], 25) == 0
assert plus_longue_serie(t, 20) == 10 and plus_longue_serie([30, 10, 30], 25) == 1
assert plus_longue_serie([10, 30, 31, 10, 30, 31, 32], 25) == 3
assert ecart_max(t) == 9 and ecart_max([5]) == 0 and ecart_max([]) == 0
assert ecart_max([10, 10, 10]) == 0 and ecart_max([3, 8]) == 5 and ecart_max([8, 3]) == 5
assert t == [21, 25, 27, 26, 31, 32, 33, 24, 29, 30]
