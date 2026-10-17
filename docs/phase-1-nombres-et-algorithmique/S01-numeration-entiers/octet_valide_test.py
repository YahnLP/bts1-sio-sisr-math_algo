assert octet_valide("0") is True
assert octet_valide("255") is True
assert octet_valide("128") is True
assert octet_valide("256") is False
assert octet_valide("-1") is False
assert octet_valide("") is False
assert octet_valide("1a") is False
