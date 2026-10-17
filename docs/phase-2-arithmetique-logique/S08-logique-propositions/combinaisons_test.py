assert combinaisons(1) == [(False,), (True,)]
assert combinaisons(2) == [(False, False), (False, True), (True, False), (True, True)]
assert combinaisons(3)[5] == (True, False, True)
assert len(combinaisons(4)) == 16
assert combinaisons(0) == [()]
