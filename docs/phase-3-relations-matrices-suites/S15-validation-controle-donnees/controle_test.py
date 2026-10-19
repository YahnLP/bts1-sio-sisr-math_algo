assert somme_controle([10, 20, 30]) == 196 and somme_controle([255, 1]) == 0
assert somme_controle([]) == 0 and somme_controle([200, 100]) == 212
assert trame_valide([10, 20, 30], 196) is True and trame_valide([10, 20, 31], 196) is False
assert trame_valide([200, 100], 212) is True and trame_valide([], 0) is True
assert all(trame_valide([a, b], somme_controle([a, b])) for a in range(0, 256, 17) for b in range(0, 256, 13))
assert xor_controle([]) == 0 and xor_controle([5]) == 5 and xor_controle([5, 5]) == 0
assert xor_controle([0b1100, 0b1010]) == 0b0110 and xor_controle([1, 2, 4]) == 7
assert xor_controle([0xC0, 0xA8, 0x0A, 0x4D]) == 0x2F
