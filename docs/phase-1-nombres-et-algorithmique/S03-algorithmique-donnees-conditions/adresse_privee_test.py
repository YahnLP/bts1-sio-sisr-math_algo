assert adresse_privee("10.4.5.6") is True
assert adresse_privee("172.16.0.1") is True
assert adresse_privee("172.31.255.254") is True
assert adresse_privee("172.32.0.1") is False
assert adresse_privee("172.15.0.1") is False
assert adresse_privee("192.168.0.1") is True
assert adresse_privee("192.169.0.1") is False
assert adresse_privee("8.8.8.8") is False
