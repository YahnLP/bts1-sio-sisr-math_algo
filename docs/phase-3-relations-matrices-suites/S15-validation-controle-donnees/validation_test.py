assert est_octet("0") is True and est_octet("255") is True and est_octet("77") is True
assert est_octet("256") is False and est_octet("-1") is False and est_octet("") is False
assert est_octet("012") is False and est_octet("1a") is False and est_octet("00") is False
assert ipv4_valide("192.168.10.77") is True and ipv4_valide("0.0.0.0") is True
assert ipv4_valide("192.168.10") is False and ipv4_valide("192.168.10.77.1") is False
assert ipv4_valide("192.168.300.1") is False and ipv4_valide("192.168.01.1") is False
assert ipv4_valide("192.168..1") is False and ipv4_valide("a.b.c.d") is False
assert mac_valide("00:1A:2b:3C:4d:5E") is True
assert mac_valide("00:1A:2b:3C:4d") is False and mac_valide("00:1A:2b:3C:4d:5G") is False
assert mac_valide("001A:2b:3C:4d:5E:6F") is False and mac_valide("0:1A:2b:3C:4d:5E") is False
