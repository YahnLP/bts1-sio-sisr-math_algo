assert additionneur_complet(1, 1, 1) == (1, 1)
assert additionneur_complet(1, 1, 0) == (0, 1)
assert additionneur_complet(1, 0, 0) == (1, 0)
assert additionneur_complet(0, 0, 0) == (0, 0)
assert additionne("0110", "0111") == "01101"
assert additionne("1", "1") == "10"
assert additionne("1111", "0001") == "10000"
assert additionne("1010", "0101") == "01111"
