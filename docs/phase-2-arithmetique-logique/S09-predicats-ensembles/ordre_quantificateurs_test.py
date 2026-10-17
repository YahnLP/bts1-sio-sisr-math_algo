U = ["u1", "u2"]
S = ["s1", "s2"]
diag = {("u1", "s1"), ("u2", "s2")}
assert chacun_a_un_serveur(diag, U, S) is True
assert un_serveur_pour_tous(diag, U, S) is False
commun = {("u1", "s1"), ("u2", "s1")}
assert chacun_a_un_serveur(commun, U, S) is True
assert un_serveur_pour_tous(commun, U, S) is True
assert chacun_a_un_serveur({("u1", "s1")}, U, S) is False
assert un_serveur_pour_tous(set(), U, S) is False
assert chacun_a_un_serveur(set(), [], S) is True
