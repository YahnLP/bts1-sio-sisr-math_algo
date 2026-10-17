assert il_existe(lambda x: x % 2 == 0, [3, 5, 8]) is True
assert il_existe(lambda x: x % 2 == 0, [3, 5, 7]) is False
assert il_existe(lambda x: x > 0, []) is False
assert il_existe(lambda x: x == 9, [3, 5, 7, 9]) is True
