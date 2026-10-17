assert prefixe_vers_masque(24) == "255.255.255.0"
assert prefixe_vers_masque(26) == "255.255.255.192"
assert prefixe_vers_masque(20) == "255.255.240.0"
assert prefixe_vers_masque(21) == "255.255.248.0"
assert prefixe_vers_masque(0) == "0.0.0.0"
assert prefixe_vers_masque(32) == "255.255.255.255"
assert adresse_reseau("192.168.10.77", "255.255.255.192") == "192.168.10.64"
assert adresse_reseau("172.16.45.200", "255.255.240.0") == "172.16.32.0"
assert diffusion("192.168.10.77", "255.255.255.192") == "192.168.10.127"
assert diffusion("10.4.7.19", "255.255.248.0") == "10.4.7.255"
assert nb_machines(26) == 62
assert nb_machines(24) == 254
assert nb_machines(30) == 2
