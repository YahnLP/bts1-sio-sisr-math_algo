t = [21, 25, 27, 26, 31, 32, 33, 24, 29, 30]
assert bilan_releves(t, 25) == (21, 33, 7, 70.0)
assert bilan_releves([25], 25) == (25, 25, 0, 0.0)
assert bilan_releves([30], 25) == (30, 30, 1, 100.0)
assert bilan_releves([-5, -2, -9], -6) == (-9, -2, 2, 200 / 3)
assert bilan_releves([1, 2, 3, 4], 0) == (1, 4, 4, 100.0)
assert bilan_releves([1, 2, 3, 4], 3) == (1, 4, 1, 25.0)
assert t == [21, 25, 27, 26, 31, 32, 33, 24, 29, 30]
