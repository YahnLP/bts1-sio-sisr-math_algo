assert pour_tout(lambda x: x % 2 == 1, [3, 5, 7, 9]) is True
assert pour_tout(lambda x: x > 4, [3, 5, 7]) is False
assert pour_tout(lambda x: x > 4, []) is True
assert pour_tout(lambda x: x == 3, [3, 3, 3]) is True
