assert inverse_mod(7, 26) == 15
assert inverse_mod(5, 26) == 21
assert inverse_mod(5, 7) == 3
assert inverse_mod(2, 4) is None
assert inverse_mod(6, 9) is None
assert inverse_mod(13, 26) is None
assert [a for a in range(1, 12) if inverse_mod(a, 12) is not None] == [1, 5, 7, 11]
