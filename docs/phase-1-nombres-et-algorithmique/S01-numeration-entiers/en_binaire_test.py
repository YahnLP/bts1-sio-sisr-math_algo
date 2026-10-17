assert en_binaire(0) == "0"
assert en_binaire(1) == "1"
assert en_binaire(6) == "110"
assert en_binaire(37) == "100101"
assert en_binaire(205) == "11001101"
assert en_binaire(1000) == "1111101000"
assert all(en_binaire(k) == bin(k)[2:] for k in range(0, 300))
