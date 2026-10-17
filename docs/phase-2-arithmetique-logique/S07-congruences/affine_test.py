assert chiffrer("AFFINE", 5, 8) == "IHHWVC"
assert chiffrer("OK", 7, 3) == "XV"
assert chiffrer("BONJOUR", 1, 3) == "ERQMRXU"
assert chiffrer("RESEAU", 1, 5) == "WJXJFZ"
assert dechiffrer("IHHWVC", 5, 8) == "AFFINE"
assert dechiffrer("KHOOR ZRUOG", 1, 3) == "HELLO WORLD"
assert dechiffrer("XV", 7, 3) == "OK"
assert all(dechiffrer(chiffrer("BTS SIO SISR", a, b), a, b) == "BTS SIO SISR" for a in (1, 3, 5, 7, 9, 11) for b in range(26))
