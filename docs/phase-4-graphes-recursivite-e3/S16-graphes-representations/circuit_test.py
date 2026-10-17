assert a_un_circuit([[0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 0]]) is True
assert a_un_circuit([[0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]) is False
assert a_un_circuit([[1]]) is True
assert a_un_circuit([[0]]) is False
assert a_un_circuit([[0, 1], [1, 0]]) is True
assert a_un_circuit([[0, 1], [0, 0]]) is False
