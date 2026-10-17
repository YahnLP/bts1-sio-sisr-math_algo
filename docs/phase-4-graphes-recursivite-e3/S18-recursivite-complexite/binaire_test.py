assert binaire_rec(13) == "1101" and binaire_rec(100) == "1100100" and binaire_rec(0) == "0" and binaire_rec(1) == "1"
assert binaire_iter(13) == "1101" and binaire_iter(100) == "1100100" and binaire_iter(0) == "0" and binaire_iter(255) == "11111111"
assert all(binaire_rec(n) == binaire_iter(n) == bin(n)[2:] for n in range(0, 200))
