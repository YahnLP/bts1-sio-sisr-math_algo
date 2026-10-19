assert premier_et_dernier("python") == "pn"
assert premier_et_dernier("a") == "aa"
assert entoure("ab", "*") == "*ab*"
assert entoure("", "-") == "--"
assert nb_chiffres_texte(2026) == 4
assert nb_chiffres_texte(7) == 1
assert nb_chiffres_texte(0) == 1
assert somme_de_textes("12", "30") == 42
assert somme_de_textes("0", "0") == 0
assert somme_de_textes("255", "1") == 256
