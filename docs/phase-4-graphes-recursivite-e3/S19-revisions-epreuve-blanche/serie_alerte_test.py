t = [21, 25, 27, 26, 31, 32, 33, 24, 29, 30]
assert premiere_serie(t, 25, 1) == 2 and premiere_serie(t, 25, 2) == 2
assert premiere_serie(t, 25, 3) == 2 and premiere_serie(t, 25, 5) == 2
assert premiere_serie(t, 25, 6) == -1 and premiere_serie([], 25, 1) == -1
u = [30, 10, 30, 31, 32, 10]
assert premiere_serie(u, 25, 1) == 0 and premiere_serie(u, 25, 2) == 2
assert premiere_serie(u, 25, 3) == 2 and premiere_serie(u, 25, 4) == -1
assert premiere_serie([10, 11, 30, 31], 25, 2) == 2
assert premiere_serie([25, 25, 25], 25, 1) == -1
