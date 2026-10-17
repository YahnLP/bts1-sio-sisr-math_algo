assert crible(1) == []
assert crible(2) == [2]
assert crible(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
assert len(crible(100)) == 25
assert crible(100)[-1] == 97
assert len(crible(1000)) == 168
