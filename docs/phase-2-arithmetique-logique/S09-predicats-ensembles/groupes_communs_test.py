G = {"Compta": {"ana", "ben", "chloé"}, "RH": {"chloé", "dan"}, "Direction": {"ben", "eli"}}
assert groupes_communs(G, "ana", "ben") == {"Compta"}
assert groupes_communs(G, "chloé", "dan") == {"RH"}
assert groupes_communs(G, "ana", "dan") == set()
assert groupes_communs(G, "ben", "ben") == {"Compta", "Direction"}
