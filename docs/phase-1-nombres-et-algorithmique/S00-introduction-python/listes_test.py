assert somme_octets("192.168.1.10") == 371
assert somme_octets("0.0.0.0") == 0
assert somme_octets("255.255.255.255") == 1020
assert compte_superieurs([3, 9, 4, 12], 5) == 2
assert compte_superieurs([], 5) == 0
assert compte_superieurs([5, 5], 5) == 0
assert liste_carres(4) == [0, 1, 4, 9]
assert liste_carres(0) == []
assert liste_carres(1) == [0]
