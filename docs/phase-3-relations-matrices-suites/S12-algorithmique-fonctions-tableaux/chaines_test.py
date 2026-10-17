assert inverse("serveur") == "ruevres" and inverse("") == ""
assert est_palindrome("radar") is True and est_palindrome("Kayak") is True
assert est_palindrome("serveur") is False
assert acronyme("systèmes et réseaux") == "SER"
assert acronyme("bts services informatiques aux organisations") == "BSIAO"
assert acronyme("") == ""
