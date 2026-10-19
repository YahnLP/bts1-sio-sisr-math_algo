# Lis ce script, anticipe ce qu'il affiche, puis lance-le.
# Ensuite modifie les nombres et relance.

def nb_chiffres(n):
    """Nombre de chiffres décimaux de l'entier n (n > 0)."""
    compteur = 0
    while n > 0:
        n = n // 10
        compteur = compteur + 1
    return compteur

print(nb_chiffres(7))
print(nb_chiffres(2026))

for k in range(1, 4):
    print("reste de", k * 5, "divisé par 3 :", (k * 5) % 3)
